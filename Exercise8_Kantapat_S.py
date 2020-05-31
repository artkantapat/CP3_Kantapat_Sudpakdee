pro1 = 10
pro2 = 20
pro3 = 30
username = input("Username : ")
password = input("Password : ")
if username == "admin" and password == "1234" :
    print("Welcom to the shop!!")
    print("------------------------")
    print("รายการสินค้าด้านล่างนี้")
    print("1. Product-1 : 10 บาท")
    print("2. Product-2 : 20 บาท")
    print("3. Product-3 : 30 บาท")
    print("------------------------")
    pro1qty = int(input("ีะบุจำนวนที่ต้องการ Product-1 >>>"))
    pro2qty = int(input("ีะบุจำนวนที่ต้องการ Product-2 >>>"))
    pro3qty = int(input("ีะบุจำนวนที่ต้องการ Product-3 >>>"))
    total = pro1qty*pro1+pro2qty*pro2+pro3qty*pro3
    print("------------------------")
    print("สรุปราคาที่ต้องชำระ",total, " บาท")
    print("------------------------")
    print("ขอขอบคุณที่มาใช้บริการ")
    print("------------------------")



else :
    print("Wrong Username or Password")
