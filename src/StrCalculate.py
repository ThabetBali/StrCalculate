def StrCalculate(number: str):
    if number == "":
        return 0
    digits = number.split(",")
    sum = 0
    for digit in digits:
        sum += int(digit)
    return sum
