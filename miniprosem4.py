import random
n=0
r=0
m=0
while(n!=5):
    print("Items avialble in our store:")
    print("1.Maggie-----Rs 10")
    print("2.Pasta--------Rs 20")
    print("3.Cake--------Rs 40")
    print("4.Chocolate--Rs 20")
    print("5.To Proceed ")
    n=int(input("Enter your choice:"))
    if(n==1):
        mq=int(input("Enter the qantity:"))
        m=10*mq
        r=r+m
        print("Maggie added of cost : Rs",m)
    if(n==2):
        pq=int(input("Enter the qantity:"))
        p=20*pq
        r=r+p
        print("Pasta added of cost : Rs",p)
    if(n==3):
        cq=int(input("Enter the qantity:"))
        c=40*cq
        r=r+c
        print("Cake added of cost : Rs",c)
    if(n==4):
        coq=int(input("Enter the qantity:"))
        co=20*coq
        r=r+co
        print("Chocolate added of cost : Rs",co)
    if(n==5):
        print("Total value of items in your cart is :",r)
        break

print("1.Cash on delivery")
print("2.Parking pickup")
print("3.Store pickup")
m=int(input("Select Mode of delivery:"))
if(m==1):
    print("Enter your Address")
    dr=input("Enter your flat no.")
    fn=input("Enter your Apartment name")
    ct=input("Enter City name")
    st=input("Enter state name")
    print("Your items will be delivered to")
    print(dr,"\n",fn,"\n",ct,"\n",st,"\n")
    print("Ordered succesfully")
    cp=int(input("To Check possibility for changing mode press 1 \n "))
    if(cp==1):
           rid=random.randint(0,1)
           if(rid==0):
                print("Order shipped cant change mode")
           if(rid==1):
                print("1.Parking pickup")
                print("2.Store pickup")
                f=int(input("Select the mode to change"))
                if(f==1):
                    print("Order placed ,Collect your items at Parking slot")
                    pid=int(input("Enter the parking id: "))
                    print("Your OTP is :")
                    OTP = random.randint(111111,999999)
                    print(OTP)
                if(f==2):
                    print("Order placed ,Collect your items at Store")
if(m==2):
    print("Order placed ,Collect your items at Parking slot")
    pid=int(input("Enter the parking id: "))
    print("Your OTP is :")
    OTP = random.randint(111111,999999)
    print(OTP)
if(m==3):
    print("Order placed ,Collect your items at Store")









