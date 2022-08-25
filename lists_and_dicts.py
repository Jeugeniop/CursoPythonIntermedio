from multiprocessing.sharedctypes import Value


def run():
    my_list = [1,"Hello",True,4.5]
    my_dict = {"firstname":"Juan","lastname":"Eugenio"}

    super_list = [
        {"firstname":"Juan","lastname":"Eugenio"},
        {"firstname":"Miguel","lastname":"Morin"},
        {"firstname":"Jose","lastname":"Garcia"},
        {"firstname":"Susana","lastname":"Martinez"},
        {"firstname":"Pepe","lastname":"Rodelo"}    
    ]

    super_dict = {
        "natural_nums" : [1,2,3,4,5],
        "integer_nums" : [-1,-2,0,1,2],
        "floating_nums" : [1.1,4.5,6.43]
    }

    print("Imprimiendo super diccionario")
    for key, value in super_dict.items():
        print(key,"-",value)

    print("Imprimiendo super lista")
    for key in super_list:
        print(key)


if __name__ == '__main__':
    run()
