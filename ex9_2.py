DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    try:
        present_discount = customer.get("discount")
        price = price * (1 - present_discount)
        return price
    except:
        price = price * (1 - DEFAULT_DISCOUNT)
        return price