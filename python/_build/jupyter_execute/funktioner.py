## Funktioner

En af de vigtigste aspekter i matematikken er funktioner. S� det er uden tvivl vigtigt at vores v�rkt�jer kan finde ud af at arbejde med funktion. Det kan vores yndlingsv�rkt�j `sympy` heldigvis langt hen ad vejen. Jeg vil undlade at gennemg� formler for forskellige funktioner, for det er ikke det der er meningen med denne note. Jeg vil i stedet g� igennem hvilke v�rkt�jer `sympy` giver os til at arbejde med funktioner og hvordan de bruges.

### H�ldningskoefficienter

Jeg har tidligere vist hvordan man kan lave sine egne Python funktioner til at lave udregninger for sig. Det kan man selvf�lgelig ogs� g�re n�r man skal udregne s�dan noget som h�ldningskoefficienter, til forskellige former for funktioner. Jeg vil nedenfor vise hvordan man kan lave en funktion der kan finde h�ldningskoefficienten for en line�r funktion, n�r man bliver givet to punkter. Jeg vil lade det v�re optil l�seren selv at find p� hvordan man kan g�re det til andre funktionstyper.

# F�rst defineres funktionen
def lin_finder(x1, y1, x2, y2):
    # Der defineres en variabel som indeholder resultatet af udregningen for h�ldningkoefficienten.
    resultat = (y2-y1)/(x2-x1)
    
    #Resultatet printes efterf�lgende p� sk�rmen
    print ("H�ldningskoefficienten er: " + str(resultat))

Det er en meget nem funktion, og st�rstedelen af tiden vil det nok give mere mening, bare at lave udregningen for sig selv i en enkelt celle. Men ikke desto mindre, kan vi jo nu pr�ve den af.

lin_finder(1, 0.5, 3, 4)

Det virker jo helt som det skal

### Grafisk fremstilling

Det er selvf�lgelig vigtigt at vi kan lave et plot af vores funktion for at kunne lave en visuel inspektion. `sympy` g�r det heldigvis virkelig nemt at f� lavet et plot, af den funktion man arbejder med. Men som altid, skal vi selvf�lgelig altid importere funktionaliteten f�rst. S� vi skal importere `plot()` funktionen. 

from sympy import plot

Nu har vi alts� funktionen til at kunne tegne vores funktioner. 

Vi kan pr�ve at tegne funktionen $x^2$, som jo er en parabel. For at kunne g�re det, skal vi f�rst have defineret overfor Python hvad `x` egentlig er. Vi kunne godt sige `x = 5`, som vi normalt ville g�re. Men i dette tilf�lde vil vi jo gerne tegne en graf, s� derfor vil vi gerne have at `x` kan v�re en masse forskellige v�rdier. 
Det har `sympy` heldigvis en hurtig l�sning p�, vi skal blot importere `x` fra deres underbibliotek af variable. Det g�r vi som vist nedenfor.

from sympy.abc import x

Nu har vi `x` importeret som en `sympy` variabel og kan dermed bruge den til at lave vores plot som vist nedenfor.

plot(x**2)

Det er ogs� muligt at tegne flere funktioner ind i �t koordinatsystem. Det g�r man ved at 

plot(x**2, x)

Vi kan ogs� plotte inden for et bestemt omr�de. F.eks. kan man se at i eksemplerne ovenfor, plottes x-aksen fra -10.0 til 10.0. Vi kan g�re aksen st�rre eller mindre ved at specificere intervallet n�r vi kalder funktionen. Lad os pr�ve at plotte $x^2$ igen, men denne gang kun i intervallet -5.0 til 5.0

plot(x**2, (x, -5, 5))

Vi skal alts� blot inds�tte en parentes i stedet for kun at definere at det er variablen `x` vi vil plotte. For at g�re det helt klart, s� hvis vi blot vil plotte $x^2$ og lade `sympy` tage sig af akse-v�rdierne, s� skriver vi blot `plot(x**2)`. Men hvis vi vil styre akse-v�rdierne p� x-aksen, s� skriver vi alts� `plot(x**2, (x, -5, 5))`.

Vi kan ogs� godt styrer akse-v�rdierne for y-aksen og vi kan ogs� g�re x-aksen s� lang vi �nsker. Men det vil jeg gennemg� Funktioner for Gymnasier, da jeg ikke mener det er relavent for folkeskole elever. 

