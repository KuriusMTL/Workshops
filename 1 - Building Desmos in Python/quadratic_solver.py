def solve_quadratic(a,b,c):
    try:
        answer1 = float((-b + (b**2-4*a*c)**0.5)/(2*a))
        answer2 = float((-b - (b**2-4*a*c)**0.5)/(2*a))

        if answer1 == answer2:
            return answer1

        else:
            return answer1, answer2
    except:
        print("Unsolvable")


while True:
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    print("Answer: "+ str(solve_quadratic(a,b,c)))
