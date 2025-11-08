def sum(i1, i2):
    result = 0
    for i in range(i1, i2 +1):
        result += i
    return result

def max(i1, i2):
    if i1> i2:
        return i1
    else:
        return i2

def main():
    print("Sum from 1 to 10 is ", sum(1, 10))
    print("Sum from 11 to 20 is ", sum(11, 20))
    print("Max integer of 1 and 5 is: ", max(1,5))
main()