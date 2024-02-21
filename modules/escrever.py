
def map_txt_Driver(arquivo):
    with open("DriverMapped.txt", "a" , encoding="utf-8") as file:
        file.writelines(arquivo + '\n')
...

