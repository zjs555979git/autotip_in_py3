def tip(dinner_price):
    """(float) -> float
    ##calulate and print all three tips to the user##
    >>> tip(345.67)
    10% tip $38.24 $380.24
    15% tip $51.86 $397.53
    20% tip $69.13 $414.80
    >>>
    """
    ten_tip = dinner_price * 0.10
    fifteen_tip = dinner_price * 0.15
    twenty_tip = dinner_price * 0.20

    print(f"10% ${ten_tip:.2f} Grand Total ${dinner_price + ten_tip:.2f}")
    print(f"15% ${fifteen_tip:.2f} Grand Total ${dinner_price + fifteen_tip:.2f}")
    print(f"20% ${twenty_tip:.2f} Grand Total ${dinner_price + twenty_tip:.2f}")
dinner_input = input("how much was dinner? ")
dinner_price = float(dinner_input)

tip(dinner_price)
