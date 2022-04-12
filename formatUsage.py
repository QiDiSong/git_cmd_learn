def myfun(name, times):
    for i in range(times):
        print(f"i love {name}")


if __name__ == '__main__':
    name = input("Please input the name you love: ")
    times = int(input("Please input the times you love: "))
    myfun(name, times)