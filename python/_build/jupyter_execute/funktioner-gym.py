# Funktioner

Da vi tidligere har gennemg�et matematikken for folkeskole niveau, kommer vi nu til det lidt mere dybdeg�ende. Det er muligvis ogs� her at Python virkelig kommer til en ret som et CAS v�rkt�j til at kunne hj�lpe eleverne. Husk at m�den hvorp� funktioner kan plottes er beskrevet mere i dybden p� siden omkring Funktioner p� Folkeskoleniveau. Men for en god ordens skyld, kan vi lige tage en hurtigt opfrisker her.

Vi bruger som s�dvanligt `sympy` til at illustrere vores funktioner. Der findes ogs� andre biblioteker, men `sympy`'s CAS funktionalitet, g�r det nemt og bekvemt at arbejde med. S� for at kunne benytte plot funktionen fra `sympy` skal vi alts� have importeret det.

from sympy import plot

Nu har vi alts� importeret `plot` funktionen fra `sympy`, s� nu skal vi bruge en variabel som `sympy` kan lave CAS udregninger med. Til dette bruger vi ofte variablen `x`. Det er dog ikke en helt almindelig variabel, for det er en special type som vi importere fra `sympy`. Det g�r vi som vist nedenfor. 

from sympy.abc import x

Det er ikke kun `x` vi kan importere, men hvilken som helt bogstav vi har lyst til at bruge. N�r vi skal plotte en funktion g�r vi som vist nedenfor.

plot(x**2)

Hvis vi gemmer en funktion i en Python variabel, kan vi ogs� plotte den ved blot at bruge variabel navnet. F.eks. kan vi pr�ve at gemme funktionen `x**3` i en variabel ved navn `funktion`.

funktion = x**3

Nu kan vi s� blot sige `plot(funktion)` for at f� vist resultatet

plot(funktion)

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

