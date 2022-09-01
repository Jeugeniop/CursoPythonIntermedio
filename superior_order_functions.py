from functools import reduce

def run():
    #filter
    my_list = [1,4,5,6,9,13,19,21]
    odd = list(filter(lambda x: x%2 != 0, my_list))

    #map
    my_list_2 = [1,2,3,4,5]
    squares = list(map(lambda x: x**2, my_list_2))

    #reduce
    my_list_3 = [2,2,2,2,2]
    all_multiplied = reduce(lambda a, b: a * b,my_list_3)

    print(odd)
    print(squares)
    print(all_multiplied)

if __name__ == '__main__':
    run()