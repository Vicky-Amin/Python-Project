main_product = {} # blank dictionary 

# main_product = {
#     "Vadapav":{
#         'qty' : 20,
#         'price' :20,
#     },
#     "Bhel":{
#         'qty' : 20,
#         'price' :20,
#     },
# }

status = True 
while status:
    spec_dict= {} # inner dictionary 
    product = input("Enter product name : ")
    qty = int(input("Enter qty : "))
    price = int(input("Enter price : "))
    
    spec_dict["qty"] = qty
    spec_dict["price"] = price 
    print(spec_dict)

    if product in main_product.keys():
        old_qty = main_product[product]['qty']
        new_qty = old_qty + qty
        spec_dict["qty"] = new_qty
        spec_dict["price"] = price 
        main_product[product] = spec_dict
    else:
        main_product[product] = spec_dict
    print(main_product)
    choice = input("do you want to add more product press 'y' for yes and press 'n' for no : ")
    if choice=='n' or choice=='no' or choice=='No':
        status = False
    else:
        status = True

all_price = []
for k in main_product.keys():
    price = main_product[k]["price"]
    all_price.append(price)
print(f"Total Cost {all_price}")
#total_price = sum(all_price)