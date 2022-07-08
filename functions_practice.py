# function named hello()
def hello():
    print("Howdy there!")
# function named pack()
def pack(r, a, w):
    return [ r, a, w]
# function called eat_lunch() accepts a list of length and print out series of strings
def eat_lunch(my_list):
    if len(my_list) == 0:
        print("I have no lunch") 
    else:
        for i in range(len(my_list)):
            if i == 0:
                print(f"First I eat {my_list[0]}")
            else:
                print(f"Next I eat {my_list[i]}")

hello()
print(pack("r", "a", "w"))
print(pack(1, 2, 3))
eat_lunch([])
eat_lunch(["burger"])
eat_lunch(["salad", "pizza", "kabobs", "dessert"]) 
