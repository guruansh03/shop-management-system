import csv
def input_for_AP():
    f = open('Stocks of andhra pradesh.csv', 'w', newline='')
    w = csv.writer(f)
    w.writerow(['Sr.no.', 'Product Name', 'Price per Item', 'Stock'])
    while True:
        s = int(input("Enter Sr.no --"))
        pb = input("Enter Product Name --")
        pp = int(input("Enter Price per Item --"))
        st = int(input("Enter Stock --"))
        dl = [s, pb, pp, st]
        w.writerow(dl)
        c = input("Do you want to enter more data?<Y/N>")
        if c in "Nn":
            break
def input_for_PB():
    f = open('Stocks of Punjab.csv', 'w', newline='')
    w = csv.writer(f)
    w.writerow(['Sr.no.', 'Product Name', 'Price per Item', 'Stock'])
    while True:
        s = int(input("Enter Sr.no --"))
        pb = input("Enter Product Name --")
        pp = int(input("Enter Price per Item --"))
        st = int(input("Enter Stock --"))
        dl = [s, pb, pp, st]
        w.writerow(dl)
        c = input("Do you want to enter more data?<Y/N>")
        if c in "Nn":
            break
def dis_AP_M():
    f = open('Stocks of andhra pradesh.csv', 'r', newline='')
    r = csv.reader(f)
    l=[]
    for i in r:
        print(i)
def dis_PB_M():
    f = open('Stocks of Punjab.csv', 'r', newline='')
    r = csv.reader(f)
    l=[]
    for i in r:
        print(i)
def Dis_AP_cus():
    name=input("Please Enter Your Name --")
    number=int(input("Please Enter Your Mobile Number --"))
    add=input("Please Enter Your Address --")
    f = open('Stocks of andhra pradesh.csv', 'r', newline='')
    f2= open('cus_AP.csv','w',newline='')
    r = csv.reader(f)
    r2 = csv.writer(f2)
    r2.writerow(['Sr No','Item Bought','Quantity Bought','Total Price'])
    l=[]
    for i in r:
        print(i)
        l=l+i
        tp=0
    while True:
        rt=input('Enter Sr no of Product you want to buy!')
        for rec in range(0,len(l)):
            if l[rec]==rt:
                print("Sr. no--",l[rec])
                print("Name--",l[rec+1])
                print("Price--",l[rec+2])
                print("Stock--",l[rec+3])
                qq=int(input("Please Enter The Quanity You Would like to Buy"))
                d=qq*int(l[rec+2])
                tp=tp+d
                ad=[l[rec],l[rec+1],qq,d]
                r2.writerow(ad)
        c_h=input("Do you want to buy more items?<Y/N>")
        if c_h in "Nn":
            break
    f2.close()
    f3= open('cus_AP.csv','r',newline='')
    f4=csv.reader(f3)
    print('----------------------------------------------------------------------------------')
    print('----------------------------------------------------------------------------------')
    print('------------------Welcome To Nation Clothing Store Delhi (^o^)--------------------')
    print('----------------------------------------------------------------------------------')
    print('----------------------------------------------------------------------------------')
    print("Name:",name,"                          ","Mobile No:",number)
    print("Address:",add)
    print('----------------------------------------------------------------------------------')
    print("Items Purchased:")
    for i in f4:
        print(i)
    print('----------------------------------------------------------------------------------')
    
    print('----------------------------------------------------------------------------------')    
    print("Your Total is --",tp,"+ 12% GST-- ",tp+0.12*tp)
    print('----------------------------------------------------------------------------------')
    print("Thank You For Shopping with Us!! :)\nWe Hope To See You Again!!!")
    
def Dis_PB_cus():
    name=input("Please Enter Your Name --")
    number=int(input("Please Enter Your Mobile Number --"))
    add=input("Please Enter Your Address --")
    f = open('Stocks of punjab.csv', 'r', newline='')
    f2= open('cus_PB.csv','w',newline='')
    r = csv.reader(f)
    r2 = csv.writer(f2)
    r2.writerow(['Sr No','Item Bought','Quantity Bought','Total Price'])
    l=[]
    for i in r:
        print(i)
        l=l+i
        tp=0
    while True:
        rt=input('Enter Sr no of Product you want to buy!')
        for rec in range(0,len(l)):
            if l[rec]==rt:
                print("Sr. no--",l[rec])

 
                print("Price--",l[rec+2])
                print("Stock--",l[rec+3])
                qq=int(input("Please Enter The Quanity You Would like to Buy"))
                d=qq*int(l[rec+2])
                tp=tp+d
                ad=[l[rec],l[rec+1],qq,d]
                r2.writerow(ad)
        c_h=input("Do you want to buy more items?<Y/N>")
        if c_h in "Nn":
            break
    f2.close()
    f3= open('cus_PB.csv','r',newline='')
    f4=csv.reader(f3)
    print('----------------------------------------------------------------------------------')
    print('----------------------------------------------------------------------------------')
    print('------------------Welcome To Nation Clothing Store Delhi (^o^)--------------------')
    print('----------------------------------------------------------------------------------')
    print('----------------------------------------------------------------------------------')
    print("Name:",name,"                          ","Mobile No:",number)
    print("Address:",add)
    print('----------------------------------------------------------------------------------')
    print("Items Purchased:")
    for i in f4:
        print(i)
    print('----------------------------------------------------------------------------------')
    
    print('----------------------------------------------------------------------------------')    
    print("Your Total is --",tp,"+ 12% GST-- ",tp+0.12*tp)
    print('----------------------------------------------------------------------------------')
    print("Thank You For Shopping with Us!! :)\nWe Hope To See You Again!!!")        
def up_AP():
    f = open('Stocks of andhra pradesh.csv', 'r+', newline='')
    r = csv.reader(f)
    l=[]
    for i in r:
        print(i)
        l=l+i
    while True:
        rt=input('Enter Sr no of Product you to change stock')
        for rec in range(0,len(l)):
            if l[rec]==rt:
                print("Sr. no--",l[rec])
                print("Name--",l[rec+1])
                print("Price--",l[rec+2])
                print("Stock--",l[rec+3])
                qq=int(input("Please Enter The new stock"))
                l[rec+3]=qq
        c_h=input("Do you want to change more stock?<Y/N>")
        if c_h in "Nn":
            break
    print("Stock Updated!")
def up_PB():
    f = open('Stocks of punjab.csv', 'r+', newline='')
    r = csv.reader(f)
    l=[]
    for i in r:
        print(i)
        l=l+i
    while True:
        rt=input('Enter Sr no of Product you to change stock')
        for rec in range(0,len(l)):
            if l[rec]==rt:
                print("Sr. no--",l[rec])
                print("Name--",l[rec+1])
                print("Price--",l[rec+2])
                print("Stock--",l[rec+3])
                qq=int(input("Please Enter The new stock"))
                l[rec+3]=qq
        c_h=input("Do you want to change more stock?<Y/N>")
        if c_h in "Nn":
            break
    print("Stock Updated!")
def MAIN():
    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print("Hello User!! Welcome To Nation Clothing Store Delhi (^o^) \nWe Ship Clothes all Over India and Have all Themes of Clothes For your Preferred Region!!\nOur Products are High in Quality and Long lasting! Waiting to be uniquely Yours!!")
    while True:
        print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        c = int(input("Please Choose Your Profile!! \n1. Press 1 For Manager/Worker.\n2.Press 2 For Customer!"))
        print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if c == 1:
            while True:
                print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                cc = int(input("Please Choose Your Action!\n1.Press 1 to Enter list of Items for Sale\n2.Press 2 for Displaying data!\n3.Press 3 to update data"))
                print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                if cc == 1:
                    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    ccc = int(input("Please Choose Region\n1.Press 1 for Andhra Pradesh\n2.Press 2 for Punjab"))
                    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    if ccc == 1:
                        input_for_AP()
                    elif ccc==2:
                        input_for_PB()
                    else:
                        Print("Wrong Input!!")
                if cc == 2:
                    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    fc= int(input("Please Choose Region<1 for Andhra Pradesh and 2 for Punjab"))
                    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    if fc == 1:
                        dis_AP_M()
                    if fc == 2:
                        dis_PB_M()
                if cc==3:
                    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    sc=int(input("Please Choose which Stock to update <1 For Andhra Pradesh. 2 For Punjab>"))
                    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    if sc==1:
                        up_AP()

                    if sc==2:
                        up_PB()
            ss=input("Do you want to Perform any more actions?<y/n>")
            if ss in "Nn":
                break

        tt=input("Do you want to Change Profile??<Y/n>")
        if tt in "Nn":
                break
    if c == 2:
        print("Welcome Customer!! We are Pleased to See you!!")
        print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        cs=int(input("Please Choose which Theme Clothes You would Prefer!! \n1.Press 1 for Andhra Pradesh \n2.Press 2 for Punjab"))
        if cs==1:
            Dis_AP_cus()
        if cs==2:
            Dis_PB_cus()
    if c ==3:
        print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        su=int(input("Please Choose which Stock to update! \n1.Press 1 for Andhra Pradesh \n2.Press 2 for Punjab"))
        print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if su==1:
            up_AP()
        if su==2:
            up_PB()        
MAIN()
            
        









