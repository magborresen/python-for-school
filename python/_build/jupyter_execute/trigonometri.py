## Trigonometri 

`math` har indbyggede funktioner til at finde sinus, cosinus og tanget. Ved alle disse funktioner, giver man en tal/vinkel, som man �nsker at finde sinus, cosinus eller tanget til. Python vil herefter vise resultatet i radianer. Dette kan laves om til grader, hvis man �nsker dette. Nedenst�ende eksempler vil vise hvordan man finder sinus, cosinus og tangent til tal der b�de er angivet i radianer og i grader.

Men for at vi kan bruge nogle af disse smarte funktioner, m� vi nok hellere lige f� importeret `math` biblioteket f�rst. 

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

Hvis man �nsker resultatet i grader, skal man f.eks. putte `math.sin(40)` ind i funktionen `math.degrees()`. Konventionen for at g�re dette i programmering er normalt, at man gemmer `math.sin(40)` i en variable, og derefter putter man variable ind i `math.degrees()`. Se nedenst�ende for eksempel

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

### Trekantsl�ser

En stor del af matematikv�rkt�jer i folkeskolen og p� gymnasiet er at kunne l�se trekanter nemt. WordMat har f.eks. en trekantsl�ser, der g�r det grafisk nemt at indtaste 3 kendte v�rdier omkring trekanten og efterf�lgende f� udregnet de resterende v�rdier. Python har ikke et grafisk v�rkt�j til dette, men ikke desto mindre findes der en trekantsl�ser. Denne kommer i et eksternt bibliotek som skal hentes vha. pip. For at hente biblioteket, skrives i terminalen eller i commando prompt.

`pip3 install trianglesolver`

N�r denne er installeret, skal den blot importeres, hvorefter alle funktioner frit kan bruges. Importeringen foreg�r ligesom med `math` biblioteket.
Man �nsker dog normalt ikke at skulle skrive `trianglesolver` hver gang man skal benytte sig af biblioteket. Derfor kan man importere det og give det et kaldenavn, som forkortelse. Python ved s� herefter at hver gang man skriver dette kaldenavn, s� referere man til `trianglesolver`.

For at importere med et kaldenavn, g�r man f�lgende

`import trianglesolver as ts`

import trianglesolver as ts

`trianglesolver` er nu importeret og alle funktioner er tilg�ngelige. N�r man skal bruge biblioteket, skal man blot referere til det som `ts`. 

Hvis man vil l�se en trekant, skal man som minimum kende tre karakteristiske dele omkring trekanten. Det kan enten v�re siderne, vinklerne eller nogen af siderne og nogle af vinklerne. Trekanten ABC, har siderne `a=3` og `b=4` og vinkel `C=25 grader` og man skal finde siden c. Denne kan man nu l�se med `trianglesolver`. F�rst skal alle siderne i trekanten defineres, dette kan heldigvis g�res p� en enkelt linje. Disse variable skal s�ttes lig med noget. Alts� de skal indeholde et eller andet. I dette tilf�lde, skal de indeholde l�sningen. For at definere hvordan `trianglesolver` skal finde l�sningen, skal man bruge den indbyggede funktion `solve()`. I `solve()` skal man angive de kendte v�rdier og hvad de er lig med. Se eksemplet nedenfor

a, b, c, A, B, C = ts.solve(a=3, b=4, C=25*ts.degree)

Nu er l�sningen alts� gemt i de 6 variable `a, b, c, A, B, C`. Derved her vi nu alle siderne gemt i `a, b, c` og vinklerne gemt i `A, B, C`. Grunden til at man ganger C v�rdien med `ts.degree` er, at `trianglesolver` forventer en v�rdi i radianer, men da opgavens v�rdi var i grader, skal denne alts� konverteres til radianer.

Man kan nu f� Python til at vise resultatet for siden c. Dette g�res ved blot at skrive c i en celle.

c

Side c har alts� l�ngden 1,8. Det er vigtigt at huske at Python angiver decimal tal med et `.` og __IKKE__ et `,`. 

Man kan ogs� f� angivet de ukendte vinkler `A` og `B`. Dette g�res p� samme m�de som ved siden `c`. Dog er resultatet af `A og B` lige nu angivet i radianer, s� dette skal omskrives til grader. Dette g�res ved blot at dividere med den samme konstant `ts.degree` som der blev multipliceret med tidligere.

A / ts.degree

B / ts.degree

`A` har alts� en vinkel p� 44,7 grader og `B` har en vinkel p� 110,3 grader.