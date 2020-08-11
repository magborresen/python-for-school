# Hvad er Jupyter Notebooks?



Jupyter Notebooks er ved denne bog er skrevet i. Det er web baseret platform, der gør det muligt at skrive Python scripts. Jupyter Notebooks fungere som et celle baseret værktøj. Det betyder, at man i én notebook, faktisk kan skrive så mange scripts som man har lyst til. Dette gøres blot i individuelle celler. Hvis scriptet har et output, vil det blot blive vist under den pågældende celle. 

Vi kan bruge dette til at lave matematiske udregninger, f.eks. kan du nedenfor se en celle hvor jeg har benyttet en matematisk operator til at lægge to tal sammen. Dette er markeret i højre side som __In__, hvortil nedenunder vil der være markeret et output som __Out__

2 + 2

Det vigtige er her, at Jupyter Notebooks fungere på den måde at hvis der er flere operationer som giver et output, så vil det kune være outputtet af den sidste operation som bliver vist. Se eksemplet nedenfor.

2 + 2
3 + 4

Derfor, hvis vi gerne vil vise flere outputs på én gang, skal vi gemme hvert output i en variabel og så bruge funktionen `print` (som findes i stort set alle programmeringssprog), til at printe det ud i vores output.

## Hvad er Markdown?
Jupyter Notebooks muliggøre desuden brugen af Markdown. Derfor kan en notebook også bruges som en tekstbehandler, såsom Microsoft Word. Dog på et noget lavere niveau. Hvor Word er mere "What You See Is What You Get", så kræver Markdown at man kender de forskellige genveje. 

Markdown benyttes i Jupyter Notebooks til tekst formatering. Det er super nemt at lære, selvom der ikke er noget generelt interface som der er i Microsoft Word. Vi er også lidt mere begrænsede end vi er i Word. Men til det vi har tænkt os at bruge det til, så har vi mere end rigeligt funktionalitet. Som tidligere nævnt, så er denne bog skrevet i Jupyter Notebooks. Men selve formateringen af hele bogen er mere eller mindre i Markdown. Undtagen kode blokkene selvfølgelig. 

## Andre formatteringsmuligheder

Udover Markdown, giver Jupyter Notebooks, mulighed for at benytte Latex formattering. Det er super fedt, i forhold til at skrive ligninger i en notebook. Vi kan endda konfigurere vores notebook, således at når vi laver matematik vha. Python, så bliver resultater også formateret i Latex, så det er letlæseligt. Det kunne f.eks. se således ud

$$\frac{5}{4} \cdot 27$$

I Jupyter Notebooks, har elever mulighed for at lave matematik og naturvidenskabelige afleveringer. Fordi der er en celle opdeling af notebooks, betyder det at de er letlæselige. Desuden findes der en udvidelse til Jupyter, der giver mulighed for at lave og rette opgaver, direkte i Jupyter Notebooks. Udvidelsen giver også mulighed for at autorette funktioner. Denne udvidelse hedder `nbgrader`. Den skal vi nok komme til at snakke mere om.

