a=int(input())
if a%2==1:
    print("Weird")
elif a%2==0:
    if a>=2 and a<=5:
        print("Not Weird")
    if 6<=a and a<=20:
        print("Weird")
    if a>20:
        print("Not Weird")
