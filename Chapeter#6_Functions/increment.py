# def main():
# 	x = 1
# 	print("Before the call, x is: ",x)
# 	increment(x)
# 	print("After the call, x is: ", x)
#
#
# def increment(n):
# 	n+=1
# 	print("\tn insdie the function is, ", n)
#
# main()
#

def main():
	x = 1
	print("Before the call, x is: ", x)
	increment(x)
	print("After the call x is: ", x)

def increment(x):
	x = x + 1
	print("X inside of the function is: ", x)
if __name__ == "__main__":
	main()