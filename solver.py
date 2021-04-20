import math
def solve(a,b,c):
	D = b*b-4*a*c
	if a != 0 and D == 0:
		x1 = (-b + math.sqrt(D))/(2*a)
		return(1,x1)
	elif a != 0 and D > 0:
		x1 = (-b+math.sqrt(D))/(2*a)
		x2 = (-b-math.sqrt(D))/(2*a)
		return(2, x1, x2)
	elif a == 0 and b == 0 and c != 0:
		return('No roots')
	elif a == 0 and b != 0:
		return(1, -c/b)
	elif a != 0 and D < 0:
		return('No real roots')
	elif a == 0 and b == 0 and c == 0:
		return('Infinite roots')

if __name__=="__main__":
	print(solve(1,2,1))