from Circle import Circle
def main():
    myCircle = Circle()

    n = 5
    printArea(myCircle, n)
    print()

def printArea(c, times):
    print("Radius\t\tArea")
    while times >=1:
        print(f"{c.radius} \t\t {c.getArea()}")
        c.radius = c.radius + 1
        times = times -1

main()
