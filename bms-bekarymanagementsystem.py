

import pandas as pd
import datetime as time
import random
print("NandiPuram Bakeary Store.")
print("CAKE SECTION, Block-3522, Order Taking=True, BMS- System")
in_orderId = []
active = True
orders_dict= {}
def genOId():
    n = random.randint(1000, 2000)
    while n in in_orderId:
        n = random.randint(1000, 2000)
    return n
    in_orderId.append(n)


def saveCsv(orderId):

    if orderId in orders_dict:
        order_det = orders_dict[orderId]

        headTitle = order_det["Name"] + "'s_order.csv"

        pd.DataFrame([order_det]).to_csv(headTitle, index=False)
        print("Done")
    else:
        print("Id not found")
def takeOrder():
    global order_detail
    name = input("Enter your name: ")
    order = input("Order: ")
    orderId = genOId()
    date = time.datetime.now().strftime('%Y-%m-%d')
    order_detail = {
            "Name": name,
            "Order": order,
            "OrderId": orderId,
            "Date": date

            }
    orders_dict[orderId] = order_detail
    print("Order taken ! Yor order id is ", orderId)
    print(displayOrder(orderId))

def displayOrder(orderId):
    if orderId in orders_dict:
        print("Order Desk")
        for key, val in orders_dict[orderId].items():
            print(f"{key} : {val}")
    else:
        print("Order not found, recheck your Id")




def main():
    print("Welcome to trinindapurama bekary store")
    while active:
        print("Chsoe one option from here")
        print("""
                Put Order -type 1
                View Order -type 2
                Save In Excel -type 3
                quit - 4

              """)
        choice = int(input("</>: "))
        if choice < 1 or choice > 4:
            print("Invalid Choice")
        elif choice == 1:

            takeOrder()
        elif choice == 2:
            orderId = int(input("Enter your Order Id :"))
            displayOrder(orderId)
        elif choice == 3:
            corderId = int(input("Enter your order Id: "))
            saveCsv(corderId)
            print("CSV Format downloaded, check your folder")
        elif choice == 4:
            print("Thanks for being with us")
            break




if __name__ == "__main__":
    main()

