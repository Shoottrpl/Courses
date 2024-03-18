def func2():
    try:
        return  1 / 0
    except:
        print("func2 error")

def func1():
    try:
        return func2()
    except:
        print("func1 error")


print(1)
print(2)
print(3)
func1()
print(4)