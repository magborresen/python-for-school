## Trigonometri 

`math` har indbyggede funktioner til at finde sinus, cosinus og tanget. Ved alle disse funktioner, giver man en tal/vinkel, som man ønsker at finde sinus, cosinus eller tanget til. Python vil herefter vise resultatet i radianer. Dette kan laves om til grader, hvis man ønsker dette. Nedenstående eksempler vil vise hvordan man finder sinus, cosinus og tangent til tal der både er angivet i radianer og i grader.

Men for at vi kan bruge nogle af disse smarte funktioner, må vi nok hellere lige få importeret `math` biblioteket først. 

import math

# Sinus i radianer
math.sin(40)

# Sinus i grader
math.sin(math.radians(40))

# Cosinus i radianer
math.cos(40)

# Cosins i grader
math.cos(math.radians(40))

# Tangent i radianer
math.tan(40)

# Tangent i grader
math.tan(math.radians(40))

Hvis man ønsker resultatet i grader, skal man f.eks. putte `math.sin(40)` ind i funktionen `math.degrees()`. Konventionen for at gøre dette i programmering er normalt, at man gemmer `math.sin(40)` i en variable, og derefter putter man variable ind i `math.degrees()`. Se nedenstående for eksempel

# Find resultat i grader
resultat_radian = math.sin(40)

# Nu er resultatet i radianer gemt i variablen 'resultat_radian'. Nu kan resultatet findes i grader
math.degrees(resultat_radian)

# Find resultat i grader
resultat_radian = math.cos(40)

# Nu er resultatet i radianer gemt i variablen 'resultat_radian'. Nu kan resultatet findes i grader
math.degrees(resultat_radian)

# Find resultat i grader
resultat_radian = math.tan(40)

# Nu er resultatet i radianer gemt i variablen 'resultat_radian'. Nu kan resultatet findes i grader
math.degrees(resultat_radian)

### Trekantsløser

En stor del af matematikværktøjer i folkeskolen og på gymnasiet er at kunne løse trekanter nemt. WordMat har f.eks. en trekantsløser, der gør det grafisk nemt at indtaste 3 kendte værdier omkring trekanten og efterfølgende få udregnet de resterende værdier. Python har ikke et grafisk værktøj til dette, men ikke desto mindre findes der en trekantsløser. Denne kommer i et eksternt bibliotek som skal hentes vha. pip. For at hente biblioteket, skrives i terminalen eller i commando prompt.

`pip3 install trianglesolver`

Når denne er installeret, skal den blot importeres, hvorefter alle funktioner frit kan bruges. Importeringen foregår ligesom med `math` biblioteket.
Man ønsker dog normalt ikke at skulle skrive `trianglesolver` hver gang man skal benytte sig af biblioteket. Derfor kan man importere det og give det et kaldenavn, som forkortelse. Python ved så herefter at hver gang man skriver dette kaldenavn, så referere man til `trianglesolver`.

For at importere med et kaldenavn, gør man følgende

`import trianglesolver as ts`

import trianglesolver as ts

`trianglesolver` er nu importeret og alle funktioner er tilgængelige. Når man skal bruge biblioteket, skal man blot referere til det som `ts`. 

Hvis man vil løse en trekant, skal man som minimum kende tre karakteristiske dele omkring trekanten. Det kan enten være siderne, vinklerne eller nogen af siderne og nogle af vinklerne. Trekanten ABC, har siderne `a=3` og `b=4` og vinkel `C=25 grader` og man skal finde siden c. Denne kan man nu løse med `trianglesolver`. Først skal alle siderne i trekanten defineres, dette kan heldigvis gøres på en enkelt linje. Disse variable skal sættes lig med noget. Altså de skal indeholde et eller andet. I dette tilfælde, skal de indeholde løsningen. For at definere hvordan `trianglesolver` skal finde løsningen, skal man bruge den indbyggede funktion `solve()`. I `solve()` skal man angive de kendte værdier og hvad de er lig med. Se eksemplet nedenfor

a, b, c, A, B, C = ts.solve(a=3, b=4, C=25*ts.degree)

Nu er løsningen altså gemt i de 6 variable `a, b, c, A, B, C`. Derved her vi nu alle siderne gemt i `a, b, c` og vinklerne gemt i `A, B, C`. Grunden til at man ganger C værdien med `ts.degree` er, at `trianglesolver` forventer en værdi i radianer, men da opgavens værdi var i grader, skal denne altså konverteres til radianer.

Man kan nu få Python til at vise resultatet for siden c. Dette gøres ved blot at skrive c i en celle.

c

Side c har altså længden 1,8. Det er vigtigt at huske at Python angiver decimal tal med et `.` og __IKKE__ et `,`. 

Man kan også få angivet de ukendte vinkler `A` og `B`. Dette gøres på samme måde som ved siden `c`. Dog er resultatet af `A og B` lige nu angivet i radianer, så dette skal omskrives til grader. Dette gøres ved blot at dividere med den samme konstant `ts.degree` som der blev multipliceret med tidligere.

A / ts.degree

B / ts.degree

`A` har altså en vinkel på 44,7 grader og `B` har en vinkel på 110,3 grader.