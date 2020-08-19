# Funktioner

Da vi tidligere har gennemgået matematikken for folkeskole niveau, kommer vi nu til det lidt mere dybdegående. Det er muligvis også her at Python virkelig kommer til en ret som et CAS værktøj til at kunne hjælpe eleverne. Husk at måden hvorpå funktioner kan plottes er beskrevet mere i dybden på siden omkring Funktioner på Folkeskoleniveau. Men for en god ordens skyld, kan vi lige tage en hurtigt opfrisker her.

Vi bruger som sædvanligt `sympy` til at illustrere vores funktioner. Der findes også andre biblioteker, men `sympy`'s CAS funktionalitet, gør det nemt og bekvemt at arbejde med. Så for at kunne benytte plot funktionen fra `sympy` skal vi altså have importeret det.

from sympy import plot

Nu har vi altså importeret `plot` funktionen fra `sympy`, så nu skal vi bruge en variabel som `sympy` kan lave CAS udregninger med. Til dette bruger vi ofte variablen `x`. Det er dog ikke en helt almindelig variabel, for det er en special type som vi importere fra `sympy`. Det gør vi som vist nedenfor. 

from sympy.abc import x

Det er ikke kun `x` vi kan importere, men hvilken som helt bogstav vi har lyst til at bruge. Når vi skal plotte en funktion gør vi som vist nedenfor.

plot(x**2)

Hvis vi gemmer en funktion i en Python variabel, kan vi også plotte den ved blot at bruge variabel navnet. F.eks. kan vi prøve at gemme funktionen `x**3` i en variabel ved navn `funktion`.

funktion = x**3

Nu kan vi så blot sige `plot(funktion)` for at få vist resultatet

plot(funktion)

### Differentiering

Det er selvfølgelig vigtigt at vores CAS værktøj kan finde ud af at differentiere funktioner. Det er jo en stor del af matematikken, og heldigvis kan vi prise os lykkelige med, at det ikke er noget problem for `sympy`. Vi skal, som altid, blot importere funktionaliteten først. Den funktion vi skal importere hedder `diff()`. Før vi kan gøre det skal vi dog altid lige huske at importere vores variable ind med også. Vi vil bruge variabel navnet `x` i det her tilfælde.

from sympy import diff
from sympy.abc import x

Vi kan nu differentiere alle de funktioner vi overhovedet kan komme i tanke om, så lad os prøve det af. Vi vil prøve at differentiere den velkendte funktion $x^2$.

diff(x**2, x)

Fedt, det giver os jo ingen problemer. I `diff()` funktionen definere vi altså først hvilken matematisk funktion vi gerne vil differentiere. Efterfølgende sætter vi et komma og definere hvilken variabel vi gerne vil differentiere med hensyn til. Nu vil den hurtige læser så spørge "Betyder det at vi kan differentiere funktion med flere variable?", og ja, det gør det. Det er nok ikke super relevant på gymnasieniveau, men nu får i den med nu hvor vi alligvel er i gang. 

For at differentiere funktione $x^2+y^2$ i forhold til $y$, skal vi altså blot efter kommaet, specificere at det er `y` der skal differentieres i forhold til.

Vi skal huske at importere `y` fra sympy inden vi forsøger at differentiere.

from sympy.abc import y

diff(x**2+y**2, y)

Og så er der differentieret i forhold til `y`. 

Vi kan selvfølgelig altid gemme resultatet for vores differentierede funktion i en variabel, så vi kan bruge det senere.

differentiale = diff(x**2, x)

Nu kan vi så bruge denne nye variabel i hvilken som helst celle vi vil. Den skal dog komme efter den celle hvor vi definerede variablen (Cellen over denne).

differentiale

Vi kan også anvende den i efterfølgende beregninger.

# Vi ganger resultatet af differentiale variablen med 2.
differentiale * 2

### Integration

Når vi kan differentiere, bliver vi selvfølgelig også nød til at kunne integrere. Den opgave klarer `sympy` også uden problemer. Vi skal igen blot lige importere en funktion der kan hjælpe os. Integrations funktionen i `sympy` hedder `integrate()`. Den kan vi lige importere hurtigt.

from sympy import integrate

Vi kan nu integrere alle de funktioner vi vil. Lad os prøve med at integrere den samme funktion som vi differentierede før, nemlig $x^2$.

integrate(x**2, x)

Det giver altså ingen problemer. Vi kan integrere hvilke som helst funktion, som et helt almindeligt CAS program også kan integrere. Hvad nu hvis vi skal integrere med grænseværdier? Jamen det er selvfølgelig stadig dejligt nemt. Vi skal blot definere dem i en parentes sammen med den variabel der skal integreres med hensyn til. Hvis vi vil integrere den tidligere funktion $x^2$ fra $0$ til $\infty$, kommer det til at se ud som nedenstående.

# Vi skal lige have importeret uendelig
from sympy import oo

# Nu kan integralet udregnes
integrate(x**2, (x, 0, oo))

Som det ses ovenfor, kan `sympy` sagtens finde ud af at arbejde med $\infty$. Det skal blot importeres først, ligesom det meste andet funktionalitet. Herefter udregner vi integralet. Efter vi definere hvilken funktion der ønskes integreret, indsætter vi et par parenteser hvor vi definere variabel, nedre grænse og øvre grænse. Og som vi kan se, er vores resultat totalt valid.

Som vi så tidligere med differentialet, kan vi selvfølgelig også gemme resultatet af vores integrale funktion i en variabel. 

integrale = integrate(x**2, x)

Nu kan vi bruge vores variabel `integrale` lige når vi ville, så længe at vi bruger den i en celle der kommer efter den vi har defineret variablen i. 

integrale

Vi kan også bruge variablen til efterfølgende beregninger. 

integrale * 2

