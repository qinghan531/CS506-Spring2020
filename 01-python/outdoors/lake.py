def draw_lake(length=50, width=50, boat=True, x=2, y=2):
    for i in range(length):
        for j in range(width):
            if(boat==True and x==j and y==i):
                print("\____/", end = "")
            else:
                print("~", end = "")
        print()
    return

