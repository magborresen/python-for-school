# Geometri

Nu begynder vi at skulle have det lidt sjovt. For geometri består hovedsageligt at nemme regne metoder, som multiplikation og division. Men det kan være en god måde at lære at lave sine egne Python funktioner på. Det kan være svært at huske alle de forskellige formler til udregning af f.eks. Arealer af geometriske figurer. Derfor kunne det være fedt hvis vi kunne lave en funktion, der tager et parametre ind og spytter resultatet ud til os. Udover at lære eleverne hvordan en Python funktion fungere, giver det måske også en bedre forståelse af hvordan selve matematikken fungere.

Så lad os prøve at dykke ned i det. Vi kommer ikke rigtigt til at have brug for nogle biblioteker til at hjælpe os med udregninger i første omgang. Lad os derfor, starte med at kigge på hvordan man definere en Python funktion.

## Find areal af retvinklet trekant

Man bruger syntaxen `def` til at fortælle, at nu starter jeg en ny definition af en funktion. Dette er efterfulgt af et mellemrum og så et funktionsnavn. Hvis jeg ville lave en funktion der kunne udregne areal af en retvinklet trekant, ville jeg måske kalde den for `areal_retvinklet`. Min funktionsdefinition ville derfor være `def areal_retvinklet()`.

Nu tænker du sikkert hvad de to parenteser i enden laver der og det er også et godt spørgsmål. De er meget vigtige i forhold til at skulle lave udregningen. For hvad for nogle parametre skal man kende for at kunne udregne arealet af en retvinklet trekant? Nemlig, man skal bruge højde og grundlinje. Disse to enheder skal vi bruge som parametre i vores funktion og det er dem som vi skal definere inde i vores parenteser. Så det kunne f.eks. være `def areal_retvinklet(hojde, grundlinje)`. Dette fortæller Python, at når nogen forsøger at bruge funktionen `areal_retvinklet`, så skal de angive en højde og en grundlinje. Ellers vil funktionen give en fejl.

Lad os prøve bare at definere en tom funktion.

def areal_retvinklet(hojde, grundlinje):
    return hojde, grundlinje

Vi har nu defineret en funktion der hedder `areal_retvinklet` som tager en højde og en grundlinje værdi ind og spytter værdierne direkte ud igen. Så hvis vi forsøger at bruge funktionen så får vi

areal_retvinklet(5, 10)

Altså får vi som forventet bare det samme ud, som vi smed ind. `5` repræsentere værdien for højden og `10` repræsentere værdien for grundlinjen. Vi kan bruge funktionen i hvilken som helst celle, så længe den celle vi benytter funktionen i, ligger efter den celle hvor funktionen er defineret.

Men vi skal altså have udregnet arealet af denne her trekant der har en højde af `5` og en grundlinje af `10`.

Formlen for at udregne areal af en retvinklet trekant kender vi alle som $\frac{1}{2} \cdot højde \cdot grundlinje$

Så vi kan jo skrive denne formel ind i vores funktion. Det gør vi over den linje hvor der står `return hojde, grundlinje`. Lad os putte resultatet af udregningen ned i en variabel, som vi kalder for `areal`.

def areal_retvinklet(hojde, grundlinje):
    areal = 1/2 * hojde * grundlinje
    return hojde, grundlinje

Hvad sker der så nu, hvis vi igen forsøger at benytte funktionen?

areal_retvinklet(5, 10)

Øv... Vi får stadig bare vores input ud som output. Men hov, hvad betyder `return` egentlig? `return` er det som en Python funktion returnere. Når Python læser `return` så antager den at funktionen er slut og værdien der returneres kastes ud som output. Det er ikke strengt nødvendigt at benytte `return` i en Python funktion. Men i programmeringsverdenen er det anset for at være god praksis.

Så vi skal have ændret vores returneringsværdi. Heldigvis proppede vi resultatet af vores udregning ned i en variabel. Så hvad nu hvis vi bare returnere `areal` i stedet?

def areal_retvinklet(hojde, grundlinje):
    areal = 1/2 * hojde * grundlinje
    return areal

Lad os prøve at benytte funktionen igen.

areal_retvinklet(5, 10)

Det ser mere rigtigt ud! Og vi kan hurtigt bekræfte med vores egen regning i hånden at arealet af en retvinklet trekant med højden 5 og grundlinje 10 __er__ 25. 

## Areal af cirkel

Okay, areal af en trekant er ret nem. Men der findes jo selvfølgelig en geometrisk figur som er en lidt hårdere nød at knække, nemlig cirklen. For her skal vi både af noget til at stå i anden og samtidigt skal vi også bruge $\pi$. Så selvom jeg i starten lovede at vi ikke skulle bruge nogle biblioteker, så kan jeg ikke helt holde den alligevel. 

Vi kan heldigvis nøjes med bare at bruge det standard `math` bibliotek i Python, som giver os alt den funktionalitet vi skal bruge, og mere til. 

Men vi skal have lavet en funktion igen som kan lave udregningen for arealet af en cirkel, som vi selvfølgelig allesammen kender som $\pi \cdot r^2$.

Vi skal derfor bruge en funktion der kan tage radiun ind som en parameter og spytte resultatet ud i form af cirklen areal. Lad os prøve at lave en funktion der hedder `areal_cirkel`.

def areal_cirkel(radius):
    return radius

Vi har nu fået defineret funktionen. Men ligesom før, vil den bare spytte sit input ud som output. Så vi skal have sat radius i anden og ganget den med $\pi$. Så lad os derfor lige få importeret $\pi$.

from math import pi

Nu kan vi frit bruge `pi` som om det bare var et normalt tal. Vi kan endda se hvor mange decimaler Python har på $\pi$.

pi

Okay, så langt så godt. Nu har vi $\pi$ klar. Nu skal vi bare have fundet ud af hvordan vi sætter radius i anden. I python kan man opløfte et tal ved at bruge operatoren `**`, altså to gangetegn lige efter hinanden. Fordi vi skal have sat radius i anden, så kan vi bruge `radius**2`.

Lad os prøve at smide det ind i vores funktion. Ligesom før, så gemmer vi resultatet i variablen `areal`

def areal_cirkel(radius):
    areal = radius**2 * pi
    return areal

Hvad sker der så hvis vi prøver at bruge funktionen nu? Vi giver den en radius på `5` og ser hvad vi får ud.

areal_cirkel(5)

Jamen det ser jo helt rigtigt ud!.

## Arealet af en trapez

Selvom arealet for en trapez er relativt nemt at regne, så er der alligevel en del skridt involveret. Man skal først have delt trapezen op i to trekanter og finde arealet af disse. Derefter lægges de to arealer sammen. Vi kan selvfølgelig bare sætte ting udenfor parantes og få formlen $A = \frac{1}{2} \cdot h \cdot (a_1 + a_2)$. Hvor $a_1$ og $a_2$ er de parallele sider i trapezen og $h$ er højden.

Men hvad nu hvis vi kunne lave en funktion, der tager de to parallele sider samt højden som parameter og kører hele smøren igennem. Altså, deler trapezen op i to trekanter, finde arealet af disse og til sidst beregne arealet af trapezen. Det giver måske et bedre overblik over hvordan den tidligere formel opstår.

Så lad os prøve det engang. Vi laver en funktion der hedder `areal_trapez(a1, a2, h)`. Den tager 3 parametre ind, længden af de to parallelle sider `a1` og `a2`, samt højden `h`.

def areal_trapez(a1, a2, h):
    # Vi udregner først arealet af den ene trekant og gemmer den i variablen t1
    t1 = 1/2 * h * a1
    
    # Print arealet af t1
    print("Arealet af trekant 1 er: " + str(t1))
    
    # Nu beregner vi arealet af den anden trekant og gemmer den i variablen t2
    t2 = 1/2 * h * a2
    
    # Print arealet af t2
    print("Arealet af trekant 2 er: " + str(t2))
    
    # Nu kan vi ligge de to tal sammen og gemme dem i variablen areal
    areal = t1 + t2
    
    # Print arealet af trapzen
    print("Arealet af trapzen er: " + str(areal))

I denne funktion har vi ingen `return` værdi, som nævnt tidligere er det heller ikke nødvendigt for at en funktion fungere. På et højere kode niveau bliver det dog set som normalt at man bruger en `return` værdi i sine funktioner. Men det er slet ikke det niveau vi er på endnu.

Lad os prøve at se om vores areal funktion virker

areal_trapez(1, 2, 1)

Som vi kan se, får vi alle resultaterne printet som vi har bedt om og de ser alle korrekte ud!