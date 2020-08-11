# Geometri

Nu begynder vi at skulle have det lidt sjovt. For geometri best�r hovedsageligt at nemme regne metoder, som multiplikation og division. Men det kan v�re en god m�de at l�re at lave sine egne Python funktioner p�. Det kan v�re sv�rt at huske alle de forskellige formler til udregning af f.eks. Arealer af geometriske figurer. Derfor kunne det v�re fedt hvis vi kunne lave en funktion, der tager et parametre ind og spytter resultatet ud til os. Udover at l�re eleverne hvordan en Python funktion fungere, giver det m�ske ogs� en bedre forst�else af hvordan selve matematikken fungere.

S� lad os pr�ve at dykke ned i det. Vi kommer ikke rigtigt til at have brug for nogle biblioteker til at hj�lpe os med udregninger i f�rste omgang. Lad os derfor, starte med at kigge p� hvordan man definere en Python funktion.

## Find areal af retvinklet trekant

Man bruger syntaxen `def` til at fort�lle, at nu starter jeg en ny definition af en funktion. Dette er efterfulgt af et mellemrum og s� et funktionsnavn. Hvis jeg ville lave en funktion der kunne udregne areal af en retvinklet trekant, ville jeg m�ske kalde den for `areal_retvinklet`. Min funktionsdefinition ville derfor v�re `def areal_retvinklet()`.

Nu t�nker du sikkert hvad de to parenteser i enden laver der og det er ogs� et godt sp�rgsm�l. De er meget vigtige i forhold til at skulle lave udregningen. For hvad for nogle parametre skal man kende for at kunne udregne arealet af en retvinklet trekant? Nemlig, man skal bruge h�jde og grundlinje. Disse to enheder skal vi bruge som parametre i vores funktion og det er dem som vi skal definere inde i vores parenteser. S� det kunne f.eks. v�re `def areal_retvinklet(hojde, grundlinje)`. Dette fort�ller Python, at n�r nogen fors�ger at bruge funktionen `areal_retvinklet`, s� skal de angive en h�jde og en grundlinje. Ellers vil funktionen give en fejl.

Lad os pr�ve bare at definere en tom funktion.

def areal_retvinklet(hojde, grundlinje):
    return hojde, grundlinje

Vi har nu defineret en funktion der hedder `areal_retvinklet` som tager en h�jde og en grundlinje v�rdi ind og spytter v�rdierne direkte ud igen. S� hvis vi fors�ger at bruge funktionen s� f�r vi

areal_retvinklet(5, 10)

Alts� f�r vi som forventet bare det samme ud, som vi smed ind. `5` repr�sentere v�rdien for h�jden og `10` repr�sentere v�rdien for grundlinjen. Vi kan bruge funktionen i hvilken som helst celle, s� l�nge den celle vi benytter funktionen i, ligger efter den celle hvor funktionen er defineret.

Men vi skal alts� have udregnet arealet af denne her trekant der har en h�jde af `5` og en grundlinje af `10`.

Formlen for at udregne areal af en retvinklet trekant kender vi alle som $\frac{1}{2} \cdot h�jde \cdot grundlinje$

S� vi kan jo skrive denne formel ind i vores funktion. Det g�r vi over den linje hvor der st�r `return hojde, grundlinje`. Lad os putte resultatet af udregningen ned i en variabel, som vi kalder for `areal`.

def areal_retvinklet(hojde, grundlinje):
    areal = 1/2 * hojde * grundlinje
    return hojde, grundlinje

Hvad sker der s� nu, hvis vi igen fors�ger at benytte funktionen?

areal_retvinklet(5, 10)

�v... Vi f�r stadig bare vores input ud som output. Men hov, hvad betyder `return` egentlig? `return` er det som en Python funktion returnere. N�r Python l�ser `return` s� antager den at funktionen er slut og v�rdien der returneres kastes ud som output. Det er ikke strengt n�dvendigt at benytte `return` i en Python funktion. Men i programmeringsverdenen er det anset for at v�re god praksis.

S� vi skal have �ndret vores returneringsv�rdi. Heldigvis proppede vi resultatet af vores udregning ned i en variabel. S� hvad nu hvis vi bare returnere `areal` i stedet?

def areal_retvinklet(hojde, grundlinje):
    areal = 1/2 * hojde * grundlinje
    return areal

Lad os pr�ve at benytte funktionen igen.

areal_retvinklet(5, 10)

Det ser mere rigtigt ud! Og vi kan hurtigt bekr�fte med vores egen regning i h�nden at arealet af en retvinklet trekant med h�jden 5 og grundlinje 10 __er__ 25. 

## Areal af cirkel

Okay, areal af en trekant er ret nem. Men der findes jo selvf�lgelig en geometrisk figur som er en lidt h�rdere n�d at kn�kke, nemlig cirklen. For her skal vi b�de af noget til at st� i anden og samtidigt skal vi ogs� bruge $\pi$. S� selvom jeg i starten lovede at vi ikke skulle bruge nogle biblioteker, s� kan jeg ikke helt holde den alligevel. 

Vi kan heldigvis n�jes med bare at bruge det standard `math` bibliotek i Python, som giver os alt den funktionalitet vi skal bruge, og mere til. 

Men vi skal have lavet en funktion igen som kan lave udregningen for arealet af en cirkel, som vi selvf�lgelig allesammen kender som $\pi \cdot r^2$.

Vi skal derfor bruge en funktion der kan tage radiun ind som en parameter og spytte resultatet ud i form af cirklen areal. Lad os pr�ve at lave en funktion der hedder `areal_cirkel`.

def areal_cirkel(radius):
    return radius

Vi har nu f�et defineret funktionen. Men ligesom f�r, vil den bare spytte sit input ud som output. S� vi skal have sat radius i anden og ganget den med $\pi$. S� lad os derfor lige f� importeret $\pi$.

from math import pi

Nu kan vi frit bruge `pi` som om det bare var et normalt tal. Vi kan endda se hvor mange decimaler Python har p� $\pi$.

pi

Okay, s� langt s� godt. Nu har vi $\pi$ klar. Nu skal vi bare have fundet ud af hvordan vi s�tter radius i anden. I python kan man opl�fte et tal ved at bruge operatoren `**`, alts� to gangetegn lige efter hinanden. Fordi vi skal have sat radius i anden, s� kan vi bruge `radius**2`.

Lad os pr�ve at smide det ind i vores funktion. Ligesom f�r, s� gemmer vi resultatet i variablen `areal`

def areal_cirkel(radius):
    areal = radius**2 * pi
    return areal

Hvad sker der s� hvis vi pr�ver at bruge funktionen nu? Vi giver den en radius p� `5` og ser hvad vi f�r ud.

areal_cirkel(5)

Jamen det ser jo helt rigtigt ud!.

## Arealet af en trapez

Selvom arealet for en trapez er relativt nemt at regne, s� er der alligevel en del skridt involveret. Man skal f�rst have delt trapezen op i to trekanter og finde arealet af disse. Derefter l�gges de to arealer sammen. Vi kan selvf�lgelig bare s�tte ting udenfor parantes og f� formlen $A = \frac{1}{2} \cdot h \cdot (a_1 + a_2)$. Hvor $a_1$ og $a_2$ er de parallele sider i trapezen og $h$ er h�jden.

Men hvad nu hvis vi kunne lave en funktion, der tager de to parallele sider samt h�jden som parameter og k�rer hele sm�ren igennem. Alts�, deler trapezen op i to trekanter, finde arealet af disse og til sidst beregne arealet af trapezen. Det giver m�ske et bedre overblik over hvordan den tidligere formel opst�r.

S� lad os pr�ve det engang. Vi laver en funktion der hedder `areal_trapez(a1, a2, h)`. Den tager 3 parametre ind, l�ngden af de to parallelle sider `a1` og `a2`, samt h�jden `h`.

def areal_trapez(a1, a2, h):
    # Vi udregner f�rst arealet af den ene trekant og gemmer den i variablen t1
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

I denne funktion har vi ingen `return` v�rdi, som n�vnt tidligere er det heller ikke n�dvendigt for at en funktion fungere. P� et h�jere kode niveau bliver det dog set som normalt at man bruger en `return` v�rdi i sine funktioner. Men det er slet ikke det niveau vi er p� endnu.

Lad os pr�ve at se om vores areal funktion virker

areal_trapez(1, 2, 1)

Som vi kan se, f�r vi alle resultaterne printet som vi har bedt om og de ser alle korrekte ud!