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

### Grafisk fremstilling

Det er selvfølgelig vigtigt at vi kan lave et plot af vores funktion for at kunne lave en visuel inspektion. `sympy` gør det heldigvis virkelig nemt at få lavet et plot, af den funktion man arbejder med. Men som altid, skal vi selvfølgelig altid importere funktionaliteten først. Så vi skal importere `plot()` funktionen. 

from sympy import plot

Nu har vi altså funktionen til at kunne tegne vores funktioner. 

Vi kan prøve at tegne funktionen $x^2$, som jo er en parabel.

plot(x**2)

