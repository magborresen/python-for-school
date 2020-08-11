# Hvad er Jupyter Notebooks?



Jupyter Notebooks er ved denne bog er skrevet i. Det er web baseret platform, der g�r det muligt at skrive Python scripts. Jupyter Notebooks fungere som et celle baseret v�rkt�j. Det betyder, at man i �n notebook, faktisk kan skrive s� mange scripts som man har lyst til. Dette g�res blot i individuelle celler. Hvis scriptet har et output, vil det blot blive vist under den p�g�ldende celle. 

Vi kan bruge dette til at lave matematiske udregninger, f.eks. kan du nedenfor se en celle hvor jeg har benyttet en matematisk operator til at l�gge to tal sammen. Dette er markeret i h�jre side som __In__, hvortil nedenunder vil der v�re markeret et output som __Out__

2 + 2

Det vigtige er her, at Jupyter Notebooks fungere p� den m�de at hvis der er flere operationer som giver et output, s� vil det kune v�re outputtet af den sidste operation som bliver vist. Se eksemplet nedenfor.

2 + 2
3 + 4

Derfor, hvis vi gerne vil vise flere outputs p� �n gang, skal vi gemme hvert output i en variabel og s� bruge funktionen `print` (som findes i stort set alle programmeringssprog), til at printe det ud i vores output.

## Hvad er Markdown?
Jupyter Notebooks muligg�re desuden brugen af Markdown. Derfor kan en notebook ogs� bruges som en tekstbehandler, s�som Microsoft Word. Dog p� et noget lavere niveau. Hvor Word er mere "What You See Is What You Get", s� kr�ver Markdown at man kender de forskellige genveje. 

Markdown benyttes i Jupyter Notebooks til tekst formatering. Det er super nemt at l�re, selvom der ikke er noget generelt interface som der er i Microsoft Word. Vi er ogs� lidt mere begr�nsede end vi er i Word. Men til det vi har t�nkt os at bruge det til, s� har vi mere end rigeligt funktionalitet. Som tidligere n�vnt, s� er denne bog skrevet i Jupyter Notebooks. Men selve formateringen af hele bogen er mere eller mindre i Markdown. Undtagen kode blokkene selvf�lgelig. 

## Andre formatteringsmuligheder

Udover Markdown, giver Jupyter Notebooks, mulighed for at benytte Latex formattering. Det er super fedt, i forhold til at skrive ligninger i en notebook. Vi kan endda konfigurere vores notebook, s�ledes at n�r vi laver matematik vha. Python, s� bliver resultater ogs� formateret i Latex, s� det er letl�seligt. Det kunne f.eks. se s�ledes ud

$$\frac{5}{4} \cdot 27$$

I Jupyter Notebooks, har elever mulighed for at lave matematik og naturvidenskabelige afleveringer. Fordi der er en celle opdeling af notebooks, betyder det at de er letl�selige. Desuden findes der en udvidelse til Jupyter, der giver mulighed for at lave og rette opgaver, direkte i Jupyter Notebooks. Udvidelsen giver ogs� mulighed for at autorette funktioner. Denne udvidelse hedder `nbgrader`. Den skal vi nok komme til at snakke mere om.

