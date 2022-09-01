from cmath import sqrt
import math

def run():
    dic_reto = {i : sqrt(i) for i in range(1,1001)}
    
    #for i in range(1,101):
    #    if i % 3 != 0:
    #        dic_reto[i] = i**3
     
    print(dic_reto)




if __name__ == '__main__':
    run()