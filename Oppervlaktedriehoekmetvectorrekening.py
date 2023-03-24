"""
Deze functie berekent de oppervlakte van een driehoek ABC in de 3D ruimte,
gegeven de x-, y- en z-coördinaat van de drie punten. De gebruikte methode
is gebaseerd op vectorrekening.
"""

import math

def bereken_oppervlakte(xA, yA, zA, xB, yB, zB, xC, yC, zC):
# Definitie van de punten als tupples in python
    puntA = (xA, yA, zA)
    puntB = (xB, yB, zC)
    puntC = (xC, yC, zC)
# Berekening bestaat uit verschillende delen
    ## Bereken de lengte van de basis => we kiezen AB als basis en bepalen de lengte via de norm van vector AB
    vector_AB = (xB-xA,yB-yA,zB-zA)
    basis = norm(vector_AB)
    ## Bereken de hoogte van de driehoek door projectie van vector AC op AB en vervolgens pythagoras toe te passen
    ## in de driehoek gevormd door vector AC en de projectie van AC op AB.
    vector_AC = (xC-xA,yC-yA,zC-zA)
    lengte_AC = norm(vector_AC)
    productAC_AB = vector_AC[0]*vector_AB[0]+vector_AC[1]*vector_AB[1]+vector_AC[2]*vector_AB[2]
    lengte_projectie = productAC_AB/basis
    hoogte = math.sqrt(lengte_AC**2-lengte_projectie**2)
    ## Oppervlakte driehoek is 1/2xbasisxhoogte
    oppervlakte = 1/2*basis*hoogte
# Finale output is een zin die het resultaat beschrijft
    print("De oppervlakte van de driehoek ABC bedraagt ", oppervlakte, " vierkante meter. De punten zijn A",puntA,", B", puntB, " en C", puntC,".", sep="")

def norm(vector):
    x = vector[0]
    y = vector [1]
    z = vector [2]
    norm = math.sqrt(x*x+y*y+z*z)
    return norm

bereken_oppervlakte(0,0,0,2,0,0,4,6,0)