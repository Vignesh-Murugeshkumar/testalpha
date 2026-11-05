""""Title: Gift Card Pairing at Checkout
Difficulty: Easy
Scenario: An online store lets customers pay with a gift card whose balance must be used up exactly. At
checkout, the system must find two different items in the customer's cart whose prices add up to exactly the
gift-card balance.
Sample input:
6
120 45 80 200 35 150
235
Sample output:
3 4"""
def gift_card_pairing(cart,gift_card_balance):
    seen = {}
    for i in range(len(cart)):
        price = cart[i]
        complement=gift_card_balance-price
        if complement in seen :
            return seen[complement],i
        seen[price]=i
    return None
cart = [120, 45, 80, 200, 35, 150]
gift_card_balance = 235
print(gift_card_pairing(cart, gift_card_balance))  # Output: True