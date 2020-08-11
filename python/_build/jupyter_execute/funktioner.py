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

### Differentiering

Det er selvf�lgelig vigtigt at vores CAS v�rkt�j kan finde ud af at differentiere funktioner. Det er jo en stor del af matematikken, og heldigvis kan vi prise os lykkelige med, at det ikke er noget problem for `sympy`. Vi skal, som altid, blot importere funktionaliteten f�rst. Den funktion vi skal importere hedder `diff()`. F�r vi kan g�re det skal vi dog altid lige huske at importere vores variable ind med ogs�. Vi vil bruge variabel navnet `x` i det her tilf�lde.

from sympy import diff
from sympy.abc import x

Vi kan nu differentiere alle de funktioner vi overhovedet kan komme i tanke om, s� lad os pr�ve det af. Vi vil pr�ve at differentiere den velkendte funktion $x^2$.

diff(x**2, x)

Fedt, det giver os jo ingen problemer. I `diff()` funktionen definere vi alts� f�rst hvilken matematisk funktion vi gerne vil differentiere. Efterf�lgende s�tter vi et komma og definere hvilken variabel vi gerne vil differentiere med hensyn til. Nu vil den hurtige l�ser s� sp�rge "Betyder det at vi kan differentiere funktion med flere variable?", og ja, det g�r det. Det er nok ikke super relevant p� gymnasieniveau, men nu f�r i den med nu hvor vi alligvel er i gang. 

For at differentiere funktione $x^2+y^2$ i forhold til $y$, skal vi alts� blot efter kommaet, specificere at det er `y` der skal differentieres i forhold til.

Vi skal huske at importere `y` fra sympy inden vi fors�ger at differentiere.

from sympy.abc import y

diff(x**2+y**2, y)

Og s� er der differentieret i forhold til `y`. 

Vi kan selvf�lgelig altid gemme resultatet for vores differentierede funktion i en variabel, s� vi kan bruge det senere.

differentiale = diff(x**2, x)

Nu kan vi s� bruge denne nye variabel i hvilken som helst celle vi vil. Den skal dog komme efter den celle hvor vi definerede variablen (Cellen over denne).

differentiale

Vi kan ogs� anvende den i efterf�lgende beregninger.

# Vi ganger resultatet af differentiale variablen med 2.
differentiale * 2

### Integration

N�r vi kan differentiere, bliver vi selvf�lgelig ogs� n�d til at kunne integrere. Den opgave klarer `sympy` ogs� uden problemer. Vi skal igen blot lige importere en funktion der kan hj�lpe os. Integrations funktionen i `sympy` hedder `integrate()`. Den kan vi lige importere hurtigt.

from sympy import integrate

Vi kan nu integrere alle de funktioner vi vil. Lad os pr�ve med at integrere den samme funktion som vi differentierede f�r, nemlig $x^2$.

integrate(x**2, x)

Det giver alts� ingen problemer. Vi kan integrere hvilke som helst funktion, som et helt almindeligt CAS program ogs� kan integrere. Hvad nu hvis vi skal integrere med gr�nsev�rdier? Jamen det er selvf�lgelig stadig dejligt nemt. Vi skal blot definere dem i en parentes sammen med den variabel der skal integreres med hensyn til. Hvis vi vil integrere den tidligere funktion $x^2$ fra $0$ til $\infty$, kommer det til at se ud som nedenst�ende.

# Vi skal lige have importeret uendelig
from sympy import oo

# Nu kan integralet udregnes
integrate(x**2, (x, 0, oo))

Som det ses ovenfor, kan `sympy` sagtens finde ud af at arbejde med $\infty$. Det skal blot importeres f�rst, ligesom det meste andet funktionalitet. Herefter udregner vi integralet. Efter vi definere hvilken funktion der �nskes integreret, inds�tter vi et par parenteser hvor vi definere variabel, nedre gr�nse og �vre gr�nse. Og som vi kan se, er vores resultat totalt valid.

Som vi s� tidligere med differentialet, kan vi selvf�lgelig ogs� gemme resultatet af vores integrale funktion i en variabel. 

integrale = integrate(x**2, x)

Nu kan vi bruge vores variabel `integrale` lige n�r vi ville, s� l�nge at vi bruger den i en celle der kommer efter den vi har defineret variablen i. 

integrale

Vi kan ogs� bruge variablen til efterf�lgende beregninger. 

integrale * 2

### Grafisk fremstilling

Det er selvf�lgelig vigtigt at vi kan lave et plot af vores funktion for at kunne lave en visuel inspektion. `sympy` g�r det heldigvis virkelig nemt at f� lavet et plot, af den funktion man arbejder med. Men som altid, skal vi selvf�lgelig altid importere funktionaliteten f�rst. S� vi skal importere `plot()` funktionen. 

from sympy import plot

Nu har vi alts� funktionen til at kunne tegne vores funktioner. 

Vi kan pr�ve at tegne funktionen $x^2$, som jo er en parabel.

plot(x**2)

