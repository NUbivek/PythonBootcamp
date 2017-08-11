def shopping():

    shopping_list = ["Milk", "Bread", "Bananas"]
    len_of_list = len(shopping_list)
    cart = []


    while len_of_list>0:
        for item in shopping_list:
            cart.append(item)

    print("cart",cart)

shopping()




