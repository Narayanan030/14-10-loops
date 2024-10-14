def func(n):
    for i in range(n+1):
        print(i*"*")
    print("\n")    
    
    for i in range(n,0,-1):
        print(i*"*")
    print("\n")
    
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for j in range(i, n):
            print("* ", end="")
        print()
    print("\n")    
        
    for i in range(n):
        for j in range(n, i, -1):
            print(" ", end="")
        for k in range(i + 1):
            print("* ", end="")
        print()

func(5)