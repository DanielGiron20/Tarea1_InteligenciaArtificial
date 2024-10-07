def tabla(n: int):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

n = int(input("Introduce un número: "))
tabla(n)