for i in range(1,201):
    if i%7==0 and i%5!=0:
        if(i>195):
            print(i)
            break
        print(i, end=",")