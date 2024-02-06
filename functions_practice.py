def hello():
    print("Hello World")

def pack(arg1,arg2,arg3):
    return [arg1,arg2,arg3]

def eat_lunch(my_list):
    if len(my_list) == 0:
        print("I have nothing to eat!")
    else:
        for i in range(len(my_list)):
            if i == 0:
                print(f"First I eat {my_list[0]}")
            else:
                print(f"Next I eat {my_list[1]}")

hello()
print(pack("arg1","arg2","arg3"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])