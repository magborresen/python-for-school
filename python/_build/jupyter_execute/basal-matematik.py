## Basal Matematik

Python kan ud af boksen, finde ud af en masse ting selv. Dette inkludere basale matematiske operatorer, s�som addition, substration, multiplikation og division. Dette g�res mere eller mindre, som p� en normal lommeregner. Python indbyggede logik g�r, at alle matematiske regler er forudindstillede. Derved ved Python f.eks. godt at division og multiplikation kommer f�r addition og subtraktion.

# Addtion
3 + 3

# Subtraktion
3 - 4

# Multiplikation
5 * 10

# Divsion
10 / 5

# Addition og division
10 / 6 + 7 / 20

# Eksponent
4**5

I Python kan man desuden benytte det der kaldes for sammenlignelses operatorer. Disse vil ikke vise et tal, men en udtalelse om situation er sandt eller falsk. 

Disse operatorer kan bl.a. v�re nyttige n�r der skal laves br�kregning for at tjekke om den ene br�k er st�rre end den anden.

# Er 3 st�rre end 4?
3 > 4

# Er 2 mindre end 4?
2 < 4

# Med br�ker
2/4 < 7/10

# Er 4 lig med 4?
4 == 4

# Er 4 lig med 5?
4 == 5

# Er 4 ikke lig med 5?
4 != 5

Disse er nok mere anvendelige i generel programmering, end de er i matematik. Men ikke desto mindre, er de gode at kende til.

## Mere funktionalitet

Hvis man har brug for mere "avancerede" funktioner, kan man benytte sig af det indbyggede matematik bibliotek i Python. For at benytte dette, skal man importere det. Importering er nemt og man kan enten importere hele eller dele af biblioteket. Importering foreg�r s�ledes:

import math

Matematik bibliotekket er nu importeret og det betyder at vi kan bruge dets funktioner. For hver funktion man �nsker at benytte, skal det specificeres at man �nsker at finde den i `math` biblioteket. I dette dokument vil de mest anvendte, men ikke alle, funktioner fra biblioteket blive vist. Hvis man �nsker at se hvad biblioteket ellers kan, skal man kigge i dokumentationen. Denne kan findes her: https://docs.python.org/3.4/library/math.html.

# Kvadratrod
math.sqrt(4)

# Potenser
2**3

# pi er indbygget i math
math.pi

# e er indbygget i math
math.e

# Naturlig logaritme til basen e 
math.log(2)

# Hvis man �nsker en anden base end e, angives den efter den f�rste tal
math.log(2, 5)

# Naturlig logaritme til basen 10, er normalt mere pr�cis ved at bruge
math.log10(2)

Dette er de mest basale former for funktioner af matematik i Python. Men man kan selvf�lgelig meget mere end det. I de n�ste kapitler af bogen vil forskellige biblioteker blive benyttet til at l�se matematiske opgaver. 