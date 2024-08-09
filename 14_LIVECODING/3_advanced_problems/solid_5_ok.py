from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass


class StripePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing payment of {amount} using Stripe")


class PyPalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing payment of {amount} using PyPal")


class OrderProcessor:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def process_order(self, amount: float):
        self.payment_processor.process_payment(amount)
        print("Order processed")


# Пример использования
current_payment_processor = StripePaymentProcessor()
order_processor = OrderProcessor(current_payment_processor)
order_processor.process_order(100.0)
