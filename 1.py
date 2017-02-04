def high_and_low(text):
    args = list(map(int,text.split()))
    result = str(max(args)) + " " + str(min(args))
    return result

print(high_and_low("-22 5 6 -25 70 -33 100 99"))
