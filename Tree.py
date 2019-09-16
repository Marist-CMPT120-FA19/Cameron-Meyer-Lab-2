def tree():
    height= int(input("How big do you want the tree to be?: "))
    i= 1
    h= height
    while height >0:
        print(' ' * (height-1) + "#" * (i))
        height -=1
        i +=2
    print(" " * (h-1) + "#")
tree()
