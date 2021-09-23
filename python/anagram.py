x = [c.lower() for c in "My Pearl"]
X = "1"
while X == "1":
    y = [c for c in x]
    z = []
    while(len(y) > 0):
        q = input("")
        if q in y:
            y.pop(y.index(q))
            z.append(q)
            print("<" + "".join(y))
            print(">" + "".join(z))
            print(len(x) * "-")
        else:
            print("All used up")
    X = input("Try again? Press 1")
