from time import *
#Use the time library
print("hello")
i = input("what your order?:")
print("ok",i,"and?:")
u = input("")
#order registration
if u == "none":
    print("ok pls wait 4min")
else:
    print(i,"and",u,"pls wait 4min")
sleep(4)
print("sir sir sir! oh hi your order is ready")
#Prepare the order
y = input("cash or card?:")
if y == "cash":
    print("ok",i,"and",u,"can be 125$")
    sleep(2)
    print("tnx nice to meet you")
else:
    print("ok",i,"and",u,"can be 125$")
    sleep(2)
    print("tnx nice to meet you")
#Order payment
