#final Code
print("\n")
menu = {
    "Vadapav" : 50,
    "Dabeli" : 30,
    "Bhel" : 70,
    "Puff" : 100,
    "Sednwhich" : 45,

}

mycart = {}
total_price = []
status = True 
while status == True:

    print("No\tMenu\t\tPrice")
    print("-"*30)
    counter = 1

    for k,v in menu.items():
        print(f"{counter}\t{k}\t\t{v}")
        counter +=1

    print("\n")
    select_item = input("what do you like to eat ?: ").capitalize()
    if select_item in menu:
        print(f"Yes, {select_item} is available")
        print("\n")
    else:
        print(f"Sorry '{select_item}' is not available please select item from the menu only Thank You...!!")
        break
        
    no_of_qty = input(f"How Many '{select_item}' do You want ?: ")
    if no_of_qty.isdigit() == False:
        print("Your odder is not valid") 
        status = False
    else:
        no_of_qty = int(no_of_qty)
        print("\n")
        print(f"Your order '{no_of_qty} {select_item}' has been placed...!!")
        mycart[select_item] = no_of_qty * menu[select_item]
        print(mycart)
        
        for price in mycart.values():
            total_price.append(price)    
        choice = input("do you want to add more product press 'y' for yes and press 'n' for no : ")

        if choice=='n' or choice=='no' or choice=='No':
            status = False
        else:
            status = True

if sum(total_price) > 0:
    
    print("Total Price:",sum(total_price))