def total(*a):
    total_of_numbers = 0
    for i in a:
        total_of_numbers += i
    return total_of_numbers


def discount(amount,rate=12):
    disc = amount * rate / 100
    return disc


name = "rohan"

age = 45