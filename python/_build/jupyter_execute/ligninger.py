## Ligninger

Meget matematik på gymnasiet vil foregå ved ligningsløsning. Ofte bliver ligninger så komplekse, at det ikke længere giver mening at løse dem i hånden. Derfor bruger man normalt et CAS værktøj. CAS værktøjet kender vi normalt som WordMat, TI-Nspire eller Maple osv. I Pythons biblioteker, findes der også CAS værktøjer. Det vil altså sige at CAS ikke er en medfødt funktion i Python. Men man skal altså importere et bibliotek, ligesom vi har set før, for at benytte sig af CAS. Der er forskellige biblioteker til dette. Nogle større, nogle mindre. Det bibliotek jeg vil bruge her, hedder `Sympy` og er uden tvivl et af de største biblioteker (Hvis ikke det største). 

Det vil sige at vi jo først skal have importeret `Sympy` for at kunne bruge det. Det ved vi jo allerede hvordan man gør. Jeg har tænkt mig at importere det, således at jeg blot kan bruge forkortelsen `sp` for at benytty dets funktioner. Vi kommer desuden til at bruge `math` biblioteket også, så det må vi hellere importere på samme tid.

For at få vores resultater til at se godt ud, kan vi også importere `init_printing` fra sympy. Derefter kører vi funktionen. Resultatet af dette kan ses længere nede.

import sympy as sp
from sympy import init_printing
import math

init_printing()

Sådan, nu har vi altså adgang til alle funktioner som sympy kommer med. Men da vi i først omgang kun skal bruge det, til at løse ligninger. Giver det mening kun at importere den funktionalitet. I Python kan man importere "under biblioteker" kaldet klasser, for kun at benytte de funktioner som kommer i disse. Den klasse som indeholder ligningsløsning i `sympy` hedder `solvers`, hvori der i den klasse findes en metode der hedder `solve`. `solve` er selve den funktion (metode) som vi bruger til at finde løsningen til en ligning. Derfor kan vi importere `solve` således

from sympy.solvers import solve

Nu er vi klar til nemt at kunne løse ligninger. Hvis vi får opgivet en ligning der er opgivet som lig med 0, kan vi altså løse den. 

F.eks. ligningen $x+5x-7=0$

I Python fungere potenser ved at man sætter `**` mellem sit tal/variabel og potensen. I `solve` funktionen indsætter vi først den venstre side af den ovenstående funktion. Derefter sætter vi et komma og specificire hvilken variabel vi vil løse for. Men da `x` endnu ikke er defineret som noget, skal vi først have gjort det. Her kan vi importere variablen fra `sympy` så den ved hvad vi snakker om. Klassen `sympy.abc` indeholder alle bogstaver som variable. Derfor kan vi importere følgende

from sympy.abc import x

Hvorefter vi kan løse ligning 

solve(x+5*x-7, x)

Vi kan se at vores resultat er fint printet pga. vi har importeret og kørt `init_printing`

Ligninger med flere variable klarer `sympy` også uden problemer. Vi skal blot lige definere en ekstra variabel først, ligesom vi definerede `x` tidligere. Så lad os definere `y` denne gang.

from sympy.abc import y

Nu kan vi så forsøge at løse en ligning der indeholder flere variable. Vi bliver selvfølgelig stadig nødt til at løse ligningen for en variabel ad gangen, men vi bliver i det mindste hjulpet på vej.

Lad os prøve at løse ligningen 

$$5x+17y+7=0$$

Når vi skal indsætte vores variabel efter kommaet, definere vi blot den variabel vi vil løse for. Det vil sige at hvis vi vil løse ligningen for `x` gør vi som nedenstående eksempel.

solve(5*x+17*y+7, x)

Hvis vi istedet vil løse for `y`, ser det således ud.

solve(5*x+17*y+7, y)

Løsningerne kan nu bruges til at bestemme de to variable. 

### Absolutte værdier

I Python arbejder vi selvfølgelig også med absolutte værdier. Så der findes altså en funktion, som kommer indbygget i Python, der finder den absolutte værdi af hvad end man fodre den med. Denne funktion hedder blot `abs()` af det engelske __absolute__. Lad os prøve den af og se om det virker.

abs(-7)

abs(15-27)

abs(-2*20)

Vi ser altså funktionen virker med alle de udtryk vi fodre den med. Den kan også bruges hvis vi f.eks. vil gange den absolutte værdi af et tal, med et andet tal. Lad os prøve at gange den absolutte værdi af $-20$ med $4$.

abs(-20)*4

Så vi kan uden problemer regne med absolutte værdier i Python.

### Andengradsligningen

Andengradsligningen som vi allesammen kender den, kommer på formen $ax^2+bx+c=0$. Denne kan vi selvfølgelig også regne i Python. Dette gøres igen blot med `sympy`'s `solve` funktion. Lad os prøve med 3 forskellige andengradsligninger som vi ved giver enten 2 løsninger, 1 løsning eller ingen løsninger.

Ligningen $2x^2+6x+4=0$ bør give os to løsninger.

solve(2*x**2+6*x+4, x)

Det gør den altså også.

Lad os prøve med ligningen $x^2-2x+1=0$ som bør give os én enkelt løsning.

solve(x**2-2*x+1, x)

Det holder altså også stik.

Lad os til sidst forsøge os med ligningen $2x^2-2x+1=0$ som bør give os 0 løsninger.

solve(2*x**2-2*x+1, x)

Ah, denne løsninger giver os altså noget med nogle komplekse tal. Det skal man lige have i baghovedet. Python kan godt finde ud af at arbejde med komplekse tal. Når man så arbejder på gymnasie niveau, vil der selvfølgelig være nogle tidspunkter, som i andengradsligningen, hvor der egentlig findes en løsning. Men vi vælger at sige at der ingen løsning er, fordi vi endnu ikke har lært at arbejde med komplekse tal.

Så vi kan altså sagtens, ved hjælp af `sympy`, arbejde med andengradsligninger. 

Men lad os nu for sjovs skyld, sige at vi er interesseret i at vide hvordan flowet for udregningen ser ud for et værktøj som `sympy`. Det kan vi nemlig nemt ved bare at lave vores egen funktion til at løse andengradsligningen. Det kunne også være at vi godt kunne tænke os at få skrevet diskriminanten ud i stedet for blot resultatet. 

Hvis vi skal laves vores egen Python funktion, så er der lige et par basale ting vi skal vide først. For at definere en funktion, skal vi blot skrive `def` efterfulgt af et mellemrum, et funktionsnavn, to parenteser og et kolon. Det kunne f.eks. så sådan her ud `def dette_er_en_funktion()`. Husk at vi stadig ikke kan bruge mellemrum imellem variabel navne i Python og det kan vi altså heller ikke i funktions navne. Derfor bruger jeg underscores. 

Indenfor de to parenteser kan vi definere det vi kalder for parametre. Det er altså ligesom når vi bruge `solve()` funktionen i `sympy`. Her har vi 2 parametre i og med at vi først indsætter en ligningen eftefulgt af et komma og derefter den variabel vi vil løse med hensyn til. Det samme kan vi gøre for vores egen funktion. De parametre der er vigtig for os at vide for at løse en andengradsligning er, selvfølgelig `a`, `b` og `c`. Så vi kan altså lave en funktion som ser således ud `def andengrads_loser(a, b, c):`. Lad os prøve det i en kode celle.

# Definér funktionen
def andengrads_loser(a, b, c):
    # Alt hvad der er indrykket med 4 mellemrum fortæller Python at det hører til denne funktion
    
    # Først findes diskriminanten ved den kendte formel
    d = b**2 - 4 * a * c
    
    # Der benyttes et boolsk udtryk til at vurdere om determinaten er større eller mindre end 0
    if d < 0:
        # Hvis determinanten er mindre end 0
        print ("Der er ingen løsninger til denne ligning")
    else:
        # Hvis determinanten er større end 0
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        
        print ("Diskriminanten er: " + str(d))
        print ("Den ene løsning er: " + str(x1))
        print ("Den anden løsning er: " + str(x2))

Jeg er lige blevet nødt til at skrive alt koden på én gang, da man ikke bare kan definere funktioner uden at give nogen form for kode. Men det er også okay. Jeg har skrevet nogle kommentarer ned igennem koden, der gerne skulle gøre det nemmere at følge med i. Vi beregner altså først determinanten ud fra de parametre som er givet ved `a`, `b` og `c` når funktionen bliver kaldt. Herefter benyttes et boolsk udtryk til at finde ud af om determinanten er større eller mindre end 0. Hvis determinanten er mindre end 0, printer vi til brugeren at der ikke findes nogen løsninger. Det vil altså sige at hvis `d < 0` er sand, vil der ikke være nogen løsninger. Hvis den derimod er falsk, vil løsningerne blive udreget og printet til brugeren. 

Men hvad nu hvis determinanten er præcis $0$? Tja, lige nu vil koden bare finde frem til løsningen og derefter printe den 2 gange. Men vi kan sagtens tage højde for tilfældet blot ved at indsætte et lille stykke boolsk logik mere. Se nedenfor.

# Definér funktionen
def andengrads_loser(a, b, c):
    # Alt hvad der er indrykket med 4 mellemrum fortæller Python at det hører til denne funktion
    
    # Først findes diskriminanten ved den kendte formel
    d = b**2 - 4 * a * c
    
    # Der benyttes et boolsk udtryk til at vurdere om determinaten er større eller mindre end 0
    if d < 0:
        # Hvis determinanten er mindre end 0
        print ("Der er ingen løsninger til denne ligning")
    elif d == 0:
        x1 = (-b + math.sqrt(d))/(2*a)
        
        print ("Diskriminanten er: " + str(d))
        print ("Den eneste løsning der findes er: " + str(d))
    else:
        # Hvis determinanten er større end 0
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        
        print ("Diskriminanten er: " + str(d))
        print ("Den ene løsning er: " + str(x1))
        print ("Den anden løsning er: " + str(x2))

Med disse få ekstra linjer kode, kan vi også tjekke om diskriminanten er lig med $0$ og printe dette ud til brugeren. 

Lad os teste vores nye funktion med de samme andengradsligninger, vi testede tidligere.

andengrads_loser(2, 6, 4)

andengrads_loser(1, 2, 1)

andengrads_loser(2, -2, 1)

Vores andengradsligningsløser fungere altså ganske fint efter hensigten.

### Simplificering

Nogle gange kan der være behov for at simplicere nogle tal. Det kan man gøre med `sympy`. Det vil sige at vi altså tager et stort udtryk og gør det mindre. Det gør vi med `sympy` funktionen `simplify`, så den skal vi selvfølgelig lige have importeret først. 

from sympy import simplify, cos, sin

Nu kan vi så bruge funktionen til at simplificere et stort eller træls udtryk. Det kan f.eks. være $cos^2(x)+sin^2(x)$, som vi jo allesammen ved er det samme som $1$. Men ved `sympy` også det?

simplify(cos(x)**2+sin(x)**2)

Selvfølgelig ved `sympy` det! Men hvad nu hvis vi har en stor brøk som vi gerne vil have skaleret lidt ned? Vi kan jo prøve med brøken

$$\frac{x^3+x^1-x-1}{x^2+2x+1}$$

Den kan simplificeres helt ned til $x-1$ så lad os se om `sympy` kan det.

simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1))

Ingen problem.

### Expandering

Af mangel på bedre ord, kommer dette afsnit til at hedde ekspandering. Vi kan altså nogle gange have behov for at få udvidet en udtryk der står inden for et par parenteser. Eller vi kan have flere parenteser der skal ganges sammen. Det kan `sympy` selvfølgelig hjælpe med. Vi skal bare bruge funktionen `expand()`. Så den får vi lige importeret.

from sympy import expand

Så, lad os prøve at se hvordan vi kan udvide et udtryk som $(x-1)^2$.

expand((x-1)**2)

Det giver altså det resultat som vi havde forventet. Hvad så hvis, vi har 2 parenteser der er ganget sammen? Som f.eks. $(x+1)\cdot (x-1)$

expand((x+1)*(x-1))

Det er heller ingen problem. Kan vi mon gøre det med flere end 2 parenteser.

expand((x+1)*(x-1)*(x+2))

Selvfølgelig.

### Faktorisering

Faktorisering er en af de ting man bliver rigtig glad for at man er god til. Men man kan selvfølgelig altid blive hjulpet lidt på vej af vores yndlingsværktøj, `sympy`. Vi skal blot bruge funktionen `factor`, så vi må hellere lige importere den.

from sympy import factor

Lad os så prøve at faktorisere et begreb som $x^3-x^2+x-1$.

factor(x**3-x**2+x-1)

Det klarer vi uden problemer. Det virker selvfølgelig også med udtryk der indeholder flere variable. Vi skal bare huske at importere alle vores variable først fra `sympy.abc`. Hvilket betyder, at hvis vi vil faktorisere et udtryk med flere variable, skal de importeres som vi har set tidligere, men ser igen her.

from sympy.abc import y, z

Nu har vi altså importeret `y` og `z` og kan bruge disse på ligefod med `x`. Lad os prøve at faktorisere et lidt større udtryk med flere variable, såsom $$x^2\cdot z + 4\cdot x\cdot y\cdot z + 4\cdot y^2\cdot z$$

factor(x**2*z + 4*x*y*z + 4*y**2*z)

Uden problemer. 