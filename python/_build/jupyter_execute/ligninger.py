## Ligninger

Meget matematik p� gymnasiet vil foreg� ved ligningsl�sning. Ofte bliver ligninger s� komplekse, at det ikke l�ngere giver mening at l�se dem i h�nden. Derfor bruger man normalt et CAS v�rkt�j. CAS v�rkt�jet kender vi normalt som WordMat, TI-Nspire eller Maple osv. I Pythons biblioteker, findes der ogs� CAS v�rkt�jer. Det vil alts� sige at CAS ikke er en medf�dt funktion i Python. Men man skal alts� importere et bibliotek, ligesom vi har set f�r, for at benytte sig af CAS. Der er forskellige biblioteker til dette. Nogle st�rre, nogle mindre. Det bibliotek jeg vil bruge her, hedder `Sympy` og er uden tvivl et af de st�rste biblioteker (Hvis ikke det st�rste). 

Det vil sige at vi jo f�rst skal have importeret `Sympy` for at kunne bruge det. Det ved vi jo allerede hvordan man g�r. Jeg har t�nkt mig at importere det, s�ledes at jeg blot kan bruge forkortelsen `sp` for at benytty dets funktioner. Vi kommer desuden til at bruge `math` biblioteket ogs�, s� det m� vi hellere importere p� samme tid.

For at f� vores resultater til at se godt ud, kan vi ogs� importere `init_printing` fra sympy. Derefter k�rer vi funktionen. Resultatet af dette kan ses l�ngere nede.

import sympy as sp
from sympy import init_printing
import math

init_printing()

S�dan, nu har vi alts� adgang til alle funktioner som sympy kommer med. Men da vi i f�rst omgang kun skal bruge det, til at l�se ligninger. Giver det mening kun at importere den funktionalitet. I Python kan man importere "under biblioteker" kaldet klasser, for kun at benytte de funktioner som kommer i disse. Den klasse som indeholder ligningsl�sning i `sympy` hedder `solvers`, hvori der i den klasse findes en metode der hedder `solve`. `solve` er selve den funktion (metode) som vi bruger til at finde l�sningen til en ligning. Derfor kan vi importere `solve` s�ledes

from sympy.solvers import solve

Nu er vi klar til nemt at kunne l�se ligninger. Hvis vi f�r opgivet en ligning der er opgivet som lig med 0, kan vi alts� l�se den. 

F.eks. ligningen $x+5x-7=0$

I Python fungere potenser ved at man s�tter `**` mellem sit tal/variabel og potensen. I `solve` funktionen inds�tter vi f�rst den venstre side af den ovenst�ende funktion. Derefter s�tter vi et komma og specificire hvilken variabel vi vil l�se for. Men da `x` endnu ikke er defineret som noget, skal vi f�rst have gjort det. Her kan vi importere variablen fra `sympy` s� den ved hvad vi snakker om. Klassen `sympy.abc` indeholder alle bogstaver som variable. Derfor kan vi importere f�lgende

from sympy.abc import x

Hvorefter vi kan l�se ligning 

solve(x+5*x-7, x)

Vi kan se at vores resultat er fint printet pga. vi har importeret og k�rt `init_printing`

Ligninger med flere variable klarer `sympy` ogs� uden problemer. Vi skal blot lige definere en ekstra variabel f�rst, ligesom vi definerede `x` tidligere. S� lad os definere `y` denne gang.

from sympy.abc import y

Nu kan vi s� fors�ge at l�se en ligning der indeholder flere variable. Vi bliver selvf�lgelig stadig n�dt til at l�se ligningen for en variabel ad gangen, men vi bliver i det mindste hjulpet p� vej.

Lad os pr�ve at l�se ligningen 

$$5x+17y+7=0$$

N�r vi skal inds�tte vores variabel efter kommaet, definere vi blot den variabel vi vil l�se for. Det vil sige at hvis vi vil l�se ligningen for `x` g�r vi som nedenst�ende eksempel.

solve(5*x+17*y+7, x)

Hvis vi istedet vil l�se for `y`, ser det s�ledes ud.

solve(5*x+17*y+7, y)

L�sningerne kan nu bruges til at bestemme de to variable. 

### Absolutte v�rdier

I Python arbejder vi selvf�lgelig ogs� med absolutte v�rdier. S� der findes alts� en funktion, som kommer indbygget i Python, der finder den absolutte v�rdi af hvad end man fodre den med. Denne funktion hedder blot `abs()` af det engelske __absolute__. Lad os pr�ve den af og se om det virker.

abs(-7)

abs(15-27)

abs(-2*20)

Vi ser alts� funktionen virker med alle de udtryk vi fodre den med. Den kan ogs� bruges hvis vi f.eks. vil gange den absolutte v�rdi af et tal, med et andet tal. Lad os pr�ve at gange den absolutte v�rdi af $-20$ med $4$.

abs(-20)*4

S� vi kan uden problemer regne med absolutte v�rdier i Python.

### Andengradsligningen

Andengradsligningen som vi allesammen kender den, kommer p� formen $ax^2+bx+c=0$. Denne kan vi selvf�lgelig ogs� regne i Python. Dette g�res igen blot med `sympy`'s `solve` funktion. Lad os pr�ve med 3 forskellige andengradsligninger som vi ved giver enten 2 l�sninger, 1 l�sning eller ingen l�sninger.

Ligningen $2x^2+6x+4=0$ b�r give os to l�sninger.

solve(2*x**2+6*x+4, x)

Det g�r den alts� ogs�.

Lad os pr�ve med ligningen $x^2-2x+1=0$ som b�r give os �n enkelt l�sning.

solve(x**2-2*x+1, x)

Det holder alts� ogs� stik.

Lad os til sidst fors�ge os med ligningen $2x^2-2x+1=0$ som b�r give os 0 l�sninger.

solve(2*x**2-2*x+1, x)

Ah, denne l�sninger giver os alts� noget med nogle komplekse tal. Det skal man lige have i baghovedet. Python kan godt finde ud af at arbejde med komplekse tal. N�r man s� arbejder p� gymnasie niveau, vil der selvf�lgelig v�re nogle tidspunkter, som i andengradsligningen, hvor der egentlig findes en l�sning. Men vi v�lger at sige at der ingen l�sning er, fordi vi endnu ikke har l�rt at arbejde med komplekse tal.

S� vi kan alts� sagtens, ved hj�lp af `sympy`, arbejde med andengradsligninger. 

Men lad os nu for sjovs skyld, sige at vi er interesseret i at vide hvordan flowet for udregningen ser ud for et v�rkt�j som `sympy`. Det kan vi nemlig nemt ved bare at lave vores egen funktion til at l�se andengradsligningen. Det kunne ogs� v�re at vi godt kunne t�nke os at f� skrevet diskriminanten ud i stedet for blot resultatet. 

Hvis vi skal laves vores egen Python funktion, s� er der lige et par basale ting vi skal vide f�rst. For at definere en funktion, skal vi blot skrive `def` efterfulgt af et mellemrum, et funktionsnavn, to parenteser og et kolon. Det kunne f.eks. s� s�dan her ud `def dette_er_en_funktion()`. Husk at vi stadig ikke kan bruge mellemrum imellem variabel navne i Python og det kan vi alts� heller ikke i funktions navne. Derfor bruger jeg underscores. 

Indenfor de to parenteser kan vi definere det vi kalder for parametre. Det er alts� ligesom n�r vi bruge `solve()` funktionen i `sympy`. Her har vi 2 parametre i og med at vi f�rst inds�tter en ligningen eftefulgt af et komma og derefter den variabel vi vil l�se med hensyn til. Det samme kan vi g�re for vores egen funktion. De parametre der er vigtig for os at vide for at l�se en andengradsligning er, selvf�lgelig `a`, `b` og `c`. S� vi kan alts� lave en funktion som ser s�ledes ud `def andengrads_loser(a, b, c):`. Lad os pr�ve det i en kode celle.

# Defin�r funktionen
def andengrads_loser(a, b, c):
    # Alt hvad der er indrykket med 4 mellemrum fort�ller Python at det h�rer til denne funktion
    
    # F�rst findes diskriminanten ved den kendte formel
    d = b**2 - 4 * a * c
    
    # Der benyttes et boolsk udtryk til at vurdere om determinaten er st�rre eller mindre end 0
    if d < 0:
        # Hvis determinanten er mindre end 0
        print ("Der er ingen l�sninger til denne ligning")
    else:
        # Hvis determinanten er st�rre end 0
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        
        print ("Diskriminanten er: " + str(d))
        print ("Den ene l�sning er: " + str(x1))
        print ("Den anden l�sning er: " + str(x2))

Jeg er lige blevet n�dt til at skrive alt koden p� �n gang, da man ikke bare kan definere funktioner uden at give nogen form for kode. Men det er ogs� okay. Jeg har skrevet nogle kommentarer ned igennem koden, der gerne skulle g�re det nemmere at f�lge med i. Vi beregner alts� f�rst determinanten ud fra de parametre som er givet ved `a`, `b` og `c` n�r funktionen bliver kaldt. Herefter benyttes et boolsk udtryk til at finde ud af om determinanten er st�rre eller mindre end 0. Hvis determinanten er mindre end 0, printer vi til brugeren at der ikke findes nogen l�sninger. Det vil alts� sige at hvis `d < 0` er sand, vil der ikke v�re nogen l�sninger. Hvis den derimod er falsk, vil l�sningerne blive udreget og printet til brugeren. 

Men hvad nu hvis determinanten er pr�cis $0$? Tja, lige nu vil koden bare finde frem til l�sningen og derefter printe den 2 gange. Men vi kan sagtens tage h�jde for tilf�ldet blot ved at inds�tte et lille stykke boolsk logik mere. Se nedenfor.

# Defin�r funktionen
def andengrads_loser(a, b, c):
    # Alt hvad der er indrykket med 4 mellemrum fort�ller Python at det h�rer til denne funktion
    
    # F�rst findes diskriminanten ved den kendte formel
    d = b**2 - 4 * a * c
    
    # Der benyttes et boolsk udtryk til at vurdere om determinaten er st�rre eller mindre end 0
    if d < 0:
        # Hvis determinanten er mindre end 0
        print ("Der er ingen l�sninger til denne ligning")
    elif d == 0:
        x1 = (-b + math.sqrt(d))/(2*a)
        
        print ("Diskriminanten er: " + str(d))
        print ("Den eneste l�sning der findes er: " + str(d))
    else:
        # Hvis determinanten er st�rre end 0
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        
        print ("Diskriminanten er: " + str(d))
        print ("Den ene l�sning er: " + str(x1))
        print ("Den anden l�sning er: " + str(x2))

Med disse f� ekstra linjer kode, kan vi ogs� tjekke om diskriminanten er lig med $0$ og printe dette ud til brugeren. 

Lad os teste vores nye funktion med de samme andengradsligninger, vi testede tidligere.

andengrads_loser(2, 6, 4)

andengrads_loser(1, 2, 1)

andengrads_loser(2, -2, 1)

Vores andengradsligningsl�ser fungere alts� ganske fint efter hensigten.

### Simplificering

Nogle gange kan der v�re behov for at simplicere nogle tal. Det kan man g�re med `sympy`. Det vil sige at vi alts� tager et stort udtryk og g�r det mindre. Det g�r vi med `sympy` funktionen `simplify`, s� den skal vi selvf�lgelig lige have importeret f�rst. 

from sympy import simplify, cos, sin

Nu kan vi s� bruge funktionen til at simplificere et stort eller tr�ls udtryk. Det kan f.eks. v�re $cos^2(x)+sin^2(x)$, som vi jo allesammen ved er det samme som $1$. Men ved `sympy` ogs� det?

simplify(cos(x)**2+sin(x)**2)

Selvf�lgelig ved `sympy` det! Men hvad nu hvis vi har en stor br�k som vi gerne vil have skaleret lidt ned? Vi kan jo pr�ve med br�ken

$$\frac{x^3+x^1-x-1}{x^2+2x+1}$$

Den kan simplificeres helt ned til $x-1$ s� lad os se om `sympy` kan det.

simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1))

Ingen problem.

### Expandering

Af mangel p� bedre ord, kommer dette afsnit til at hedde ekspandering. Vi kan alts� nogle gange have behov for at f� udvidet en udtryk der st�r inden for et par parenteser. Eller vi kan have flere parenteser der skal ganges sammen. Det kan `sympy` selvf�lgelig hj�lpe med. Vi skal bare bruge funktionen `expand()`. S� den f�r vi lige importeret.

from sympy import expand

S�, lad os pr�ve at se hvordan vi kan udvide et udtryk som $(x-1)^2$.

expand((x-1)**2)

Det giver alts� det resultat som vi havde forventet. Hvad s� hvis, vi har 2 parenteser der er ganget sammen? Som f.eks. $(x+1)\cdot (x-1)$

expand((x+1)*(x-1))

Det er heller ingen problem. Kan vi mon g�re det med flere end 2 parenteser.

expand((x+1)*(x-1)*(x+2))

Selvf�lgelig.

### Faktorisering

Faktorisering er en af de ting man bliver rigtig glad for at man er god til. Men man kan selvf�lgelig altid blive hjulpet lidt p� vej af vores yndlingsv�rkt�j, `sympy`. Vi skal blot bruge funktionen `factor`, s� vi m� hellere lige importere den.

from sympy import factor

Lad os s� pr�ve at faktorisere et begreb som $x^3-x^2+x-1$.

factor(x**3-x**2+x-1)

Det klarer vi uden problemer. Det virker selvf�lgelig ogs� med udtryk der indeholder flere variable. Vi skal bare huske at importere alle vores variable f�rst fra `sympy.abc`. Hvilket betyder, at hvis vi vil faktorisere et udtryk med flere variable, skal de importeres som vi har set tidligere, men ser igen her.

from sympy.abc import y, z

Nu har vi alts� importeret `y` og `z` og kan bruge disse p� ligefod med `x`. Lad os pr�ve at faktorisere et lidt st�rre udtryk med flere variable, s�som $$x^2\cdot z + 4\cdot x\cdot y\cdot z + 4\cdot y^2\cdot z$$

factor(x**2*z + 4*x*y*z + 4*y**2*z)

Uden problemer. 