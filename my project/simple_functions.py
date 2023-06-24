from lib2to3.pgen2.token import NAME
from turtle import width
from unicodedata import name



name1 = 'bungalow'
width1 = 23
height1 = 34
mass1 = 1000

name2 = 'detached'
width2 = 33
height2 = 67
mass2 = 4300

name3 = 'self content'
width3 = 88
height3 = 98
mass3 = 4500

name4 = 'storey'
width4 = 65
height4 = 49
mass4 = 23000

def vol_calculator(name, width, height, mass):
    volume = mass / (width * height)
    area = width*height
    print('BULIDING NAME:' +' ' +  name )
    print('Area of the building:' + '' + str(area))
    print('Volume of the building:' + '' + str(volume))
    print('FINAL COMMENTS:')
    if volume > 10:
        print('Reinforcement needed for the '  + name)
    else:
        print('Reinforcement not needed for the ' + name)
        print("")


volume1 = vol_calculator(name1, width1, height1, mass1)
volume2 = vol_calculator(name2, width2, height2, mass2)
volume3 = vol_calculator(name3, width3, height3, mass3)
volume4 = vol_calculator(name4, width4, height4, mass4)
