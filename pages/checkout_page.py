from playwright.sync_api import Page, expect


class Checkout:
    base_url = "https://demowebshop.tricentis.com"
    product_url = f"{base_url}/digital-slr-camera"

    def __init__(self, page: Page):
        self.page = page

    def navigate_to_product(self):
        self.page.goto(self.product_url)

    def select_product(self):
        pass

    def get_selected_variant_label(self) -> str:
        return ""

    def add_to_cart(self):
        self.page.locator("#add-to-cart-button-18").click()
        expect(
            self.page.locator(".bar-notification.success")
        ).to_be_visible(timeout=10_000)

    def open_cart(self):
        self.page.goto(f"{self.base_url}/cart")

    def assert_cart_contains(self, product_name: str, quantity: int = 1):
        name_cell = self.page.locator(".cart-item-row .product-name").first
        expect(name_cell).to_contain_text(product_name)

        qty_input = self.page.locator(".cart-item-row input.qty-input").first
        expect(qty_input).to_have_value(str(quantity))

    def assert_cart_variant(self, variant_text: str):
        variant_cell = self.page.locator(".cart-item-row .attributes").first
        expect(variant_cell).to_contain_text(variant_text)

    def proceed_to_checkout(self):
        self.page.locator("#termsofservice").check()
        self.page.get_by_role("button", name="Checkout").click()

    def fill_billing_address(self, data: dict):

        new_addr = self.page.locator("#billing-address-select")
        if new_addr.is_visible():
            new_addr.select_option(label="New Address")

        self.page.locator("#BillingNewAddress_CountryId").select_option(
            label=data["country"]
        )
        self.page.wait_for_load_state("networkidle")

        self.page.locator("#BillingNewAddress_City").fill(data["city"])
        self.page.locator("#BillingNewAddress_Address1").fill(data["address"])
        self.page.locator("#BillingNewAddress_ZipPostalCode").fill(data["zip"])
        self.page.locator("#BillingNewAddress_PhoneNumber").fill(data["phone"])
        self.page.get_by_role("button", name="Continue").click()

    def shipping_address(self):
        self.page.get_by_role("button", name="Continue").click()

    def shipping_method(self):
        self.page.get_by_role("radio", name="Ground (0.00)").check()
        self.page.get_by_role("button", name="Continue").click()

    def fill_payment_method(self):
        self.page.get_by_role("radio", name="Credit Card Credit Card").check()
        self.page.get_by_role("button", name="Continue").click()

    def fill_payment_info(self, data: dict):
        self.page.locator("#CreditCardType").select_option(label=data["card_type"])
        self.page.locator("#CardholderName").fill(data["cardholder"])
        self.page.locator("#CardNumber").fill(data["card_number"])
        self.page.locator("#ExpireYear").select_option(data["expiry_year"])
        self.page.get_by_label("Expiration date").select_option(data["expiry_month"])
        self.page.locator("#CardCode").fill(data["cvv"])
        self.page.get_by_role("button", name="Continue").click()

    def confirm_order(self):
        self.page.get_by_role("button", name="Confirm").click()

    def assert_order_confirmed(self):
        confirmation = self.page.locator(".order-completed .title")
        expect(confirmation).to_be_visible(timeout=15_000)
        expect(confirmation).to_contain_text("Your order has been successfully processed")