while True:
    try:
        [A, B, C] = input().split(" ")
        if A == B == C:
            print("*")
        elif A == B:
            print("C")
        elif B == C:
            print("A")
        else:
            print("B")
    except EOFError:
        break
