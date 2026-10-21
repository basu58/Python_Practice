# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# DBTITLE 1,Cell 1
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self):
        pass

class Amazon(PaymentGateway):
    def pay(self):
        print('Pay for amazon using razorpay')

b = Amazon()

b.pay()