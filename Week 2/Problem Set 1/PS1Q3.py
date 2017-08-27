# Problem Set 1, Question 3
# This asks the user for his/her order and returns the number of hamburgers, waters, and salads ordered.

# This is an example order.
order = 'hamburger water salad water hamburger salad salad'

# This is the function that counts the numbers of each order.
def item_order (order):
    order_list = [0, 0, 0] # Creates a variable to count the numbers of each item.
    # Goes through each letter and sees if they match particular strings.
    for word in range(len(order)):
        # Goes through each word and sees if it matches hamburger, water, or salad.
        if (order [word : word + 9] == 'hamburger'):
            order_list[0] += 1
        elif (order [word : word + 5] == 'water'):
            order_list[1] += 1
        elif (order [word : word + 5] == 'salad'):
            order_list[2] += 1
    # Returns a final statement with the count of each item in the proper format.
    return ("salad:" + str(order_list[2]) + " hamburger:" + str(order_list[0]) + " water:" + str(order_list[1]))