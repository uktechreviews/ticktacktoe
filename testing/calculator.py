def MyCalculator(num1 :int, num2 :int, operation: str):
    try:
        return int(num1) + int(num2)
    except:
        return 0