%matplotlib inline

## Funktioner

En af de vigtigste aspekter i matematikken er funktioner. Så det er uden tvivl vigtigt at vores værktøjer kan finde ud af at arbejde med funktion. Det kan vores yndlingsværktøj `sympy` heldigvis langt hen ad vejen. Jeg vil undlade at gennemgå formler for forskellige funktioner, for det er ikke det der er meningen med denne note. Jeg vil i stedet gå igennem hvilke værktøjer `sympy` giver os til at arbejde med funktioner og hvordan de bruges.

### Hældningskoefficienter

Jeg har tidligere vist hvordan man kan lave sine egne Python funktioner til at lave udregninger for sig. Det kan man selvfølgelig også gøre når man skal udregne sådan noget som hældningskoefficienter, til forskellige former for funktioner. Jeg vil nedenfor vise hvordan man kan lave en funktion der kan finde hældningskoefficienten for en lineær funktion, når man bliver givet to punkter. Jeg vil lade det være optil læseren selv at find på hvordan man kan gøre det til andre funktionstyper.

# Først defineres funktionen
def lin_finder(x1, y1, x2, y2):
    # Der defineres en variabel som indeholder resultatet af udregningen for hældningkoefficienten.
    resultat = (y2-y1)/(x2-x1)
    
    #Resultatet printes efterfølgende på skærmen
    print ("Hældningskoefficienten er: " + str(resultat))

Det er en meget nem funktion, og størstedelen af tiden vil det nok give mere mening, bare at lave udregningen for sig selv i en enkelt celle. Men ikke desto mindre, kan vi jo nu prøve den af.

lin_finder(1, 0.5, 3, 4)

Det virker jo helt som det skal

### Grafisk fremstilling

Det er selvfølgelig vigtigt at vi kan lave et plot af vores funktion for at kunne lave en visuel inspektion. `sympy` gør det heldigvis virkelig nemt at få lavet et plot, af den funktion man arbejder med. Men som altid, skal vi selvfølgelig altid importere funktionaliteten først. Så vi skal importere `plot()` funktionen. 

from sympy import plot

Nu har vi altså funktionen til at kunne tegne vores funktioner. 

Vi kan prøve at tegne funktionen $x^2$, som jo er en parabel. For at kunne gøre det, skal vi først have defineret overfor Python hvad `x` egentlig er. Vi kunne godt sige `x = 5`, som vi normalt ville gøre. Men i dette tilfælde vil vi jo gerne tegne en graf, så derfor vil vi gerne have at `x` kan være en masse forskellige værdier. 
Det har `sympy` heldigvis en hurtig løsning på, vi skal blot importere `x` fra deres underbibliotek af variable. Det gør vi som vist nedenfor.

from sympy.abc import x

Nu har vi `x` importeret som en `sympy` variabel og kan dermed bruge den til at lave vores plot som vist nedenfor.

plot(x**2)

Det er også muligt at tegne flere funktioner ind i ét koordinatsystem. Det gør man ved at 

plot(x**2, x)