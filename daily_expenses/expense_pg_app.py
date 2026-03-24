import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
import pandas as pd
import psycopg2
import win32api
import tempfile

# ----------------- PostgreSQL CONFIG -----------------
PG_HOST = "localhost"
PG_PORT = 5433
PG_DBNAME = "expenses_db"   # change as needed
PG_USER = "postgres"        # change as needed
PG_PASSWORD = "Basu@123"  # change as needed

# ----------------- DB HELPERS -----------------
def get_connection():
    return psycopg2.connect(
        host=PG_HOST,
        port=PG_PORT,
        dbname=PG_DBNAME,
        user=PG_USER,
        password=PG_PASSWORD
    )

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id SERIAL PRIMARY KEY,
            date DATE NOT NULL,
            category VARCHAR(100) NOT NULL,
            description TEXT,
            amount NUMERIC(12,2) NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

# ----------------- CRUD FUNCTIONS -----------------
def add_expense():
    date_str = entry_date.get().strip()
    category = combo_category.get().strip()
    desc = entry_desc.get().strip()
    amount_text = entry_amount.get().strip()

    if not date_str or not category or not amount_text:
        messagebox.showwarning("Missing fields", "Date, category and amount are required.")
        return

    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        amount = float(amount_text)
    except ValueError:
        messagebox.showwarning(
            "Invalid input",
            "Amount must be a number and date must be in YYYY-MM-DD format."
        )
        return

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO expenses (date, category, description, amount) VALUES (%s, %s, %s, %s)",
            (date_str, category, desc, amount)
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Database Error", f"Could not add expense:\n{e}")
        return

    clear_entries()
    refresh_list(apply_filters=True)
    messagebox.showinfo("Success", "Expense added successfully.")

def on_tree_select(event):
    selected = tree.selection()
    if not selected:
        return

    item_id = selected[0]
    values = tree.item(item_id, "values")
    tags = tree.item(item_id, "tags")
    if not tags:
        return

    expense_id = tags[0]

    entry_date.delete(0, tk.END)
    entry_date.insert(0, values[0])

    combo_category.set(values[1])

    entry_desc.delete(0, tk.END)
    entry_desc.insert(0, values[2])

    entry_amount.delete(0, tk.END)
    entry_amount.insert(0, values[3])

    global current_selected_id
    current_selected_id = expense_id

def update_expense():
    global current_selected_id
    if not current_selected_id:
        messagebox.showwarning("No selection", "Select a row to update from the list.")
        return

    date_str = entry_date.get().strip()
    category = combo_category.get().strip()
    desc = entry_desc.get().strip()
    amount_text = entry_amount.get().strip()

    if not date_str or not category or not amount_text:
        messagebox.showwarning("Missing fields", "Date, category and amount are required.")
        return

    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        amount = float(amount_text)
    except ValueError:
        messagebox.showwarning(
            "Invalid input",
            "Amount must be a number and date must be in YYYY-MM-DD format."
        )
        return

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE expenses
            SET date = %s,
                category = %s,
                description = %s,
                amount = %s
            WHERE id = %s
            """,
            (date_str, category, desc, amount, current_selected_id)
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Database Error", f"Could not update expense:\n{e}")
        return

    clear_entries()
    refresh_list(apply_filters=True)
    messagebox.showinfo("Updated", "Expense updated successfully.")
    current_selected_id = None

# ----------------- LOAD + FILTER -----------------
def build_filters(single_date=None, start_date=None, end_date=None):
    """
    WHERE date = ? for single_date
    WHERE date BETWEEN ? AND ? for range. [web:61][web:64]
    """
    where_clauses = []
    params = []

    if single_date:
        where_clauses.append("date = %s")
        params.append(single_date)

    if start_date and end_date:
        where_clauses.append("date BETWEEN %s AND %s")
        params.extend([start_date, end_date])

    where_sql = ""
    if where_clauses:
        where_sql = "WHERE " + " AND ".join(where_clauses)

    return where_sql, params

def refresh_list(apply_filters=False):
    single_date = None
    start_date = None
    end_date = None

    if apply_filters:
        sd = search_date_entry.get().strip()
        fd = from_date_entry.get().strip()
        td = to_date_entry.get().strip()

        if sd:
            try:
                datetime.strptime(sd, "%Y-%m-%d")
                single_date = sd
            except ValueError:
                messagebox.showwarning("Invalid date", "Search Date must be YYYY-MM-DD.")
                return

        if fd or td:
            if not fd or not td:
                messagebox.showwarning("Missing range", "Both From and To dates are required for range search.")
                return
            try:
                datetime.strptime(fd, "%Y-%m-%d")
                datetime.strptime(td, "%Y-%m-%d")
                start_date = fd
                end_date = td
            except ValueError:
                messagebox.showwarning("Invalid range", "From/To dates must be YYYY-MM-DD.")
                return

    where_sql, params = build_filters(single_date, start_date, end_date)

    for row in tree.get_children():
        tree.delete(row)

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT id, date, category, description, amount
            FROM expenses
            {where_sql}
            ORDER BY date DESC, id DESC
        """, params)
        rows = cur.fetchall()
        cur.close()

        cur = conn.cursor()
        cur.execute(f"""
            SELECT COALESCE(SUM(amount), 0)
            FROM expenses
            {where_sql}
        """, params)
        total = cur.fetchone()[0] or 0

        cur.execute(f"""
            SELECT category, COALESCE(SUM(amount),0) AS total
            FROM expenses
            {where_sql}
            GROUP BY category
            ORDER BY category
        """, params)
        cat_rows = cur.fetchall()
        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Database Error", f"Could not load expenses:\n{e}")
        return

    for _id, date, cat, desc, amt in rows:
        tree.insert(
            "",
            "end",
            values=(date.strftime("%Y-%m-%d"), cat, desc or "", f"{float(amt):.2f}"),
            tags=(str(_id),)
        )

    label_total.config(text=f"Total: ₹{float(total):.2f}")

    if cat_rows:
        parts = [f"{cat}: ₹{float(t):.2f}" for cat, t in cat_rows]
        label_cat_totals.config(text="Category Totals: " + " | ".join(parts))
    else:
        label_cat_totals.config(text="Category Totals: -")

def clear_entries():
    entry_date.delete(0, tk.END)
    entry_date.insert(0, datetime.now().strftime("%Y-%m-%d"))
    combo_category.set("Food")
    entry_desc.delete(0, tk.END)
    entry_amount.delete(0, tk.END)

    global current_selected_id
    current_selected_id = None

def clear_filters():
    search_date_entry.delete(0, tk.END)
    from_date_entry.delete(0, tk.END)
    to_date_entry.delete(0, tk.END)
    refresh_list(apply_filters=False)

def delete_expense():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("No selection", "Please select an expense to delete.")
        return

    item = selected[0]
    tags = tree.item(item, "tags")
    if not tags:
        messagebox.showwarning("Error", "Could not determine selected expense ID.")
        return

    expense_id = tags[0]

    if not messagebox.askyesno("Confirm", "Delete this expense?"):
        return

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM expenses WHERE id = %s", (expense_id,))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Database Error", f"Could not delete expense:\n{e}")
        return

    clear_entries()
    refresh_list(apply_filters=True)

# ----------------- EXPORT TO EXCEL -----------------
def export_to_excel():
    single_date = search_date_entry.get().strip()
    fd = from_date_entry.get().strip()
    td = to_date_entry.get().strip()

    sd = None
    start_date = None
    end_date = None

    if single_date:
        try:
            datetime.strptime(single_date, "%Y-%m-%d")
            sd = single_date
        except ValueError:
            messagebox.showwarning("Invalid date", "Search Date must be YYYY-MM-DD.")
            return

    if fd or td:
        if not fd or not td:
            messagebox.showwarning("Missing range", "Both From and To dates are required for range export.")
            return
        try:
            datetime.strptime(fd, "%Y-%m-%d")
            datetime.strptime(td, "%Y-%m-%d")
            start_date = fd
            end_date = td
        except ValueError:
            messagebox.showwarning("Invalid range", "From/To dates must be YYYY-MM-DD.")
            return

    where_sql, params = build_filters(sd, start_date, end_date)

    try:
        conn = get_connection()
        query = f"""
            SELECT date AS "Date",
                   category AS "Category",
                   description AS "Description",
                   amount AS "Amount"
            FROM expenses
            {where_sql}
            ORDER BY date DESC, id DESC
        """
        df = pd.read_sql_query(query, conn, params=params)
        conn.close()
    except Exception as e:
        messagebox.showerror("Database Error", f"Could not fetch data for export:\n{e}")
        return

    if df.empty:
        messagebox.showinfo("No data", "No expenses to export for this filter.")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Excel files", "*.xlsx")],
        title="Save Expenses As"
    )

    if not file_path:
        return

    try:
        df.to_excel(file_path, index=False)
        messagebox.showinfo("Export complete", f"Expenses exported to:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to export:\n{e}")

# ----------------- PRINT REPORT -----------------
def print_report():
    single_date = None
    start_date = None
    end_date = None

    sd = search_date_entry.get().strip()
    fd = from_date_entry.get().strip()
    td = to_date_entry.get().strip()

    if sd:
        try:
            datetime.strptime(sd, "%Y-%m-%d")
            single_date = sd
        except ValueError:
            messagebox.showwarning("Invalid date", "Search Date must be YYYY-MM-DD.")
            return

    if fd or td:
        if not fd or not td:
            messagebox.showwarning("Missing range", "Both From and To dates are required for range print.")
            return
        try:
            datetime.strptime(fd, "%Y-%m-%d")
            datetime.strptime(td, "%Y-%m-%d")
            start_date = fd
            end_date = td
        except ValueError:
            messagebox.showwarning("Invalid range", "From/To dates must be YYYY-MM-DD.")
            return

    where_sql, params = build_filters(single_date, start_date, end_date)

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT date, category, description, amount
            FROM expenses
            {where_sql}
            ORDER BY date DESC, id DESC
        """, params)
        rows = cur.fetchall()

        cur.execute(f"""
            SELECT COALESCE(SUM(amount), 0)
            FROM expenses
            {where_sql}
        """, params)
        total = cur.fetchone()[0] or 0

        cur.execute(f"""
            SELECT category, COALESCE(SUM(amount),0) AS total
            FROM expenses
            {where_sql}
            GROUP BY category
            ORDER BY category
        """, params)
        cat_rows = cur.fetchall()

        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Database Error", f"Could not fetch data for print:\n{e}")
        return

    if not rows:
        messagebox.showinfo("No data", "No expenses to print for this filter.")
        return

    lines = []
    lines.append("Daily Expense Report")
    lines.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    if single_date:
        lines.append(f"Filter: Date = {single_date}")
    if start_date and end_date:
        lines.append(f"Filter: Range {start_date} to {end_date}")
    lines.append("-" * 60)
    lines.append(f"{'Date':<12} {'Category':<15} {'Amount':>10}  Description")
    lines.append("-" * 60)

    for date, cat, desc, amt in rows:
        date_str = date.strftime("%Y-%m-%d")
        desc_str = (desc or "").replace("\n", " ")
        lines.append(f"{date_str:<12} {cat:<15} ₹{float(amt):>8.2f}  {desc_str}")

    lines.append("-" * 60)
    lines.append(f"TOTAL: ₹{float(total):.2f}")
    lines.append("Category Totals:")
    for cat, t in cat_rows:
        lines.append(f"  {cat}: ₹{float(t):.2f}")
    lines.append("-" * 60)

    report_text = "\n".join(lines)

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as tmp:
            tmp.write(report_text)
            tmp_path = tmp.name
        win32api.ShellExecute(0, "print", tmp_path, None, ".", 0)
        messagebox.showinfo("Print", "Report sent to printer (via default text editor).")
    except Exception as e:
        messagebox.showerror("Print Error", f"Could not print:\n{e}")

# ----------------- GUI SETUP -----------------
init_db()
current_selected_id = None

root = tk.Tk()
root.title("Daily Expense Notebook (PostgreSQL)")
# icon: place expense.ico in same folder
try:
    root.iconbitmap(default="expense.ico")
except Exception:
    pass  # ignore if icon missing or non-Windows [web:72]
root.geometry("960x760")
root.resizable(False, False)

# Input frame
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10, padx=10, fill="x")

tk.Label(frame_inputs, text="Date (YYYY-MM-DD):").grid(row=0, column=0, sticky="w", padx=5, pady=2)
entry_date = tk.Entry(frame_inputs, width=15)
entry_date.grid(row=0, column=1, padx=5, pady=2)
entry_date.insert(0, datetime.now().strftime("%Y-%m-%d"))

tk.Label(frame_inputs, text="Category:").grid(row=0, column=2, sticky="w", padx=5, pady=2)
combo_category = ttk.Combobox(
    frame_inputs,
    values=["Food", "Transport", "Shopping", "Rent", "Utilities", "Entertainment", "Health", "Other"],
    state="readonly",
    width=18
)
combo_category.grid(row=0, column=3, padx=5, pady=2)
combo_category.set("Food")

tk.Label(frame_inputs, text="Description:").grid(row=1, column=0, sticky="w", padx=5, pady=2)
entry_desc = tk.Entry(frame_inputs, width=65)
entry_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=2, sticky="w")

tk.Label(frame_inputs, text="Amount (₹):").grid(row=2, column=0, sticky="w", padx=5, pady=2)
entry_amount = tk.Entry(frame_inputs, width=15)
entry_amount.grid(row=2, column=1, padx=5, pady=2)

btn_add = tk.Button(frame_inputs, text="Add Expense", command=add_expense, bg="green", fg="white", width=14)
btn_add.grid(row=2, column=2, padx=5, pady=5)

btn_update = tk.Button(frame_inputs, text="Update Selected", command=update_expense, bg="orange", fg="black", width=14)
btn_update.grid(row=2, column=3, padx=5, pady=5)

btn_clear = tk.Button(frame_inputs, text="Clear", command=clear_entries, width=14)
btn_clear.grid(row=3, column=3, padx=5, pady=5, sticky="e")

# Search frame
frame_search = tk.LabelFrame(root, text="Search / Filter by Date", padx=10, pady=5)
frame_search.pack(padx=10, pady=5, fill="x")

tk.Label(frame_search, text="Date (exact):").grid(row=0, column=0, padx=5, pady=2, sticky="w")
search_date_entry = tk.Entry(frame_search, width=12)
search_date_entry.grid(row=0, column=1, padx=5, pady=2)

tk.Label(frame_search, text="From:").grid(row=0, column=2, padx=5, pady=2, sticky="w")
from_date_entry = tk.Entry(frame_search, width=12)
from_date_entry.grid(row=0, column=3, padx=5, pady=2)

tk.Label(frame_search, text="To:").grid(row=0, column=4, padx=5, pady=2, sticky="w")
to_date_entry = tk.Entry(frame_search, width=12)
to_date_entry.grid(row=0, column=5, padx=5, pady=2)

btn_apply_filter = tk.Button(frame_search, text="Apply Filter", command=lambda: refresh_list(apply_filters=True), width=12)
btn_apply_filter.grid(row=0, column=6, padx=10, pady=2)

btn_clear_filter = tk.Button(frame_search, text="Clear Filter", command=clear_filters, width=12)
btn_clear_filter.grid(row=0, column=7, padx=5, pady=2)

# List frame
frame_list = tk.Frame(root)
frame_list.pack(pady=10, padx=10, fill="both", expand=True)

columns = ("Date", "Category", "Description", "Amount")
tree = ttk.Treeview(frame_list, columns=columns, show="headings", height=15)
tree.heading("Date", text="Date")
tree.heading("Category", text="Category")
tree.heading("Description", text="Description")
tree.heading("Amount", text="Amount (₹)")

tree.column("Date", width=110, anchor="center")
tree.column("Category", width=120, anchor="center")
tree.column("Description", width=480, anchor="w")
tree.column("Amount", width=120, anchor="center")

tree.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(frame_list, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

tree.bind("<<TreeviewSelect>>", on_tree_select)

# Bottom buttons
frame_bottom = tk.Frame(root)
frame_bottom.pack(pady=5)

btn_delete = tk.Button(frame_bottom, text="Delete Selected", command=delete_expense, bg="red", fg="white", width=16)
btn_delete.grid(row=0, column=0, padx=5, pady=5)

btn_export = tk.Button(frame_bottom, text="Export to Excel", command=export_to_excel, bg="blue", fg="white", width=16)
btn_export.grid(row=0, column=1, padx=5, pady=5)

btn_print = tk.Button(frame_bottom, text="Print Report", command=print_report, bg="purple", fg="white", width=16)
btn_print.grid(row=0, column=2, padx=5, pady=5)

label_total = tk.Label(root, text="Total: ₹0.00", font=("Arial", 12, "bold"))
label_total.pack(pady=3)

label_cat_totals = tk.Label(root, text="Category Totals: -", font=("Arial", 10))
label_cat_totals.pack(pady=3)

refresh_list(apply_filters=False)
root.mainloop()
