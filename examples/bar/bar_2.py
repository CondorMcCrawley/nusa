# -*- coding: utf-8 -*-
# ***********************************
#  Author: Pedro Jorge De Los Santos     
#  E-mail: delossantosmfq@gmail.com 
#  License: MIT License
# ***********************************
from nusa.core import *
from nusa.model import *
from nusa.element import *

def test2():
    """
    Kattan, P.I. (2003). MATLAB guide to finite elements, an interactive approach.
    Example 3.1, pp. 29
    """
    E = 210e6
    A = 0.003
    P = -10
    L1, L2 = 1.5, 1
    UX3 = 0.002
    
    m1 = BarModel("Bar model 02")
    
    n1 = Node((0,0))
    n2 = Node((1.5,0))
    n3 = Node((2.5,0))
    
    e1 = Bar((n1,n2),E,A)
    e2 = Bar((n2,n3),E,A)
    
    for nd in (n1,n2,n3): m1.add_node(nd)
    for el in (e1,e2): m1.add_element(el)
    
    m1.add_force(n2, (P,))
    m1.add_constraint(n1, ux=0.0)
    m1.add_constraint(n3, ux=UX3)
    m1.solve()
    print(m1.U)
    
    
if __name__ == '__main__':
    test2()
