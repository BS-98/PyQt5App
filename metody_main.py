# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:45:06 2018

@author: Bartek

"""

from math import sqrt
import matplotlib.pyplot as plt



def wykres(A_X,A_Y,B_X,B_Y,C_X,C_Y,D_X,D_Y):
    
    bx1 = plt.subplot(111)
    bx1.set_ylabel('Y [m]')
    bx1.set_xlabel('X [m]')
    bx1.yaxis.grid(True, which='major')
    bx1.xaxis.grid(True, which='major')
    
    if ((B_X - A_X)*(D_Y - C_Y) - (B_Y - A_Y)*(D_X - C_X)) == 0:
        
        txt = "Proste są równoległe. Punkt P nie istnieje"
        let = ["A", "B", "C", "D"]
        
        X = [A_X, B_X, C_X, D_X]
        Y = [A_Y, B_Y, C_Y, D_Y]
        
        P_X = "---"
        P_Y = "---"
        
        bx1.scatter(X, Y)
        bx1.plot([A_X, B_X], [A_Y, B_Y])
        bx1.plot([C_X, D_X], [C_Y, D_Y])
        
        for (x, y, l) in zip(X ,Y ,enumerate(let)):
            bx1.annotate("{}({};{})".format(l[1],x,y), xy=(x,y))
            
        plt.show()
        with open('Proj1_sem2.txt', 'w+') as plik:
            plik.write(38*'-')
            plik.write('\n|{:^8}|{:^13}|{:^13}|\n'.format('Punkt', 'X', 'Y'))
            plik.write(38*'-')
            plik.write('\n|{:^8}|{:^13}|{:^13}|\n'.format('A', round(A_X,3), round(A_Y,3)))
            plik.write(38*'-')
            plik.write('\n|{:^8}|{:^13}|{:^13}|\n'.format('B', round(B_X,3), round(B_Y,3)))
            plik.write(38*'-')
            plik.write('\n|{:^8}|{:^13}|{:^13}|\n'.format('C', round(C_X,3), round(C_Y,3)))
            plik.write(38*'-')
            plik.write('\n|{:^8}|{:^13}|{:^13}|\n'.format('D', round(D_X,3), round(D_Y,3)))
            plik.write(38*'-')
            plik.write('\n|{:^8}|{:^13}|{:^13}|\n'.format('P', '-', '-'))
            
    elif ((B_X - A_X)*(D_Y - C_Y) - (B_Y - A_Y)*(D_X - C_X)) != 0:
        t1 = (((C_X - A_X)*(D_Y - C_Y) - (C_Y - A_Y)*(D_X - C_X))/((B_X - A_X)*(D_Y - C_Y) - (B_Y - A_Y)*(D_X - C_X)))
        t2 = (((C_X - A_X)*(B_Y - A_Y) - (C_Y - A_Y)*(B_X - A_X))/((B_X - A_X)*(D_Y - C_Y) - (B_Y - A_Y)*(D_X - C_X)))


        P_X = round(A_X + t1*(B_X - A_X),3)
        P_Y = round(A_Y + t1*(B_Y - A_Y),3)

        if (0 <= t1 <= 1) and (0 <= t2 <= 1):
            txt = "Położenie punktu P: Punkt przecięcia należy do obu przecinanych odcinków"
        elif (0 <= t1 <= 1) and ((0 > t2) or (t2 > 1)):
            txt = "Położenie punktu P: Punkt przecięcia leży na przedłużeniu odcinka"
        elif ((0 > t1) or ( t1 > 1)) and (0 <= t2 <= 1):
            txt = "Położenie punktu P: Punkt przecięcia leży na przedłużeniu odcinka"
        else:
            txt = "Położenie punktu P: Punkt przecięcia leży na przedłużeniu odcinków"
            
        odl_PA = sqrt((A_X - P_X)**2 + (A_Y- P_Y)**2 )
        odl_PB = sqrt((B_X - P_X)**2 + (B_Y- P_Y)**2 )
        odl_PC = sqrt((C_X - P_X)**2 + (C_Y- P_Y)**2 )
        odl_PD = sqrt((D_X - P_X)**2 + (D_Y- P_Y)**2 )
        
        if odl_PA < odl_PB:
            bx1.plot([A_X, P_X], [A_Y, P_Y], linestyle='--', color='red')
        else:
            bx1.plot([B_X, P_X], [B_Y, P_Y], linestyle='--', color='red')
        
        if odl_PC < odl_PD:
            bx1.plot([C_X, P_X], [C_Y, P_Y], linestyle='--', color='green')
        else:
            bx1.plot([D_X, P_X], [D_Y, P_Y], linestyle='--', color='green')
            
        let = ["A", "B", "C", "D", "P"]
        
        X2 = [A_X, B_X, C_X, D_X, P_X]
        Y2 = [A_Y, B_Y, C_Y, D_Y, P_Y]
        
        bx1.scatter(X2, Y2)
        bx1.plot([A_X, B_X], [A_Y, B_Y], color='red')
        bx1.plot([C_X, D_X], [C_Y, D_Y], color='green')
        

        
        
        for (x,y,l) in zip(X2,Y2,enumerate(let)):
            bx1.annotate("{}({};{})".format(l[1],round(x, 3), round(y, 3)), xy=(x,y))
        plt.show()    
#        plt.waitforbuttonpress(0)
#        plt.close()
        
        with open('Proj1_sem2.txt', 'w+') as plik:
            plik.write(38*'-')
            plik.write('\n|{:^8}|{:^13}|{:^13}|\n'.format('Punkt', 'X', 'Y'))
            plik.write(38*'-')
            plik.write('\n|{:^8}|{:^13}|{:^13}|\n'.format('A', round(A_X,3), round(A_Y,3)))
            plik.write(38*'-')
            plik.write('\n|{:^8}|{:^13}|{:^13}|\n'.format('B', round(B_X,3), round(B_Y,3)))
            plik.write(38*'-')
            plik.write('\n|{:^8}|{:^13}|{:^13}|\n'.format('C', round(C_X,3), round(C_Y,3)))
            plik.write(38*'-')
            plik.write('\n|{:^8}|{:^13}|{:^13}|\n'.format('D', round(D_X,3), round(D_Y,3)))
            plik.write(38*'-')
            plik.write('\n|{:^8}|{:^13}|{:^13}|\n'.format('P', round(P_X,3), round(P_Y,3)))

    return bx1,txt,P_X,P_Y


if __name__=='__main__':
    
    A_X = 1
    A_Y = 1
    
    B_X = 1
    B_Y = 3
    
    C_X = 4
    C_Y = 3
    
    D_X = 4
    D_Y = 8
    
    bx1,txt,P_X,P_Y = wykres(A_X,A_Y,B_X,B_Y,C_X,C_Y,D_X,D_Y)