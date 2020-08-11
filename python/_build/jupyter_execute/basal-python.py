# Hvorfor Python?

Hvis man sidder p� en Mac eller Linux computer vil Python allerede v�re pr�installeret. Hvis man sidder p� en Windows computer derimod, skal Python installeres. Jeg vedh�fter et link til en guide for installation.

Der findes 2 versioner af Python. Python 2 og Python 3. I denne notesbog, vil der dog blive brugt Python 3, da Python 2 ikke l�ngere vil v�re supporteret fra udviklerne i 2020. 

For at kunne udarbejder matematik afleveringer og pr�ver med Python, foresl�r jeg at installere Jupyter Notebooks. Dette g�res ved hj�lp af Python indbyggede pakke distrubtionssystem kaldet pip. Jeg vedh�fter en guide til hvordan Jupyter Notebooks installeres, samt hvordan man bruger pip generelt. N�r Python er installeret kr�ver pip ingen ekstra ops�tning, og man vil kunne bruge funktionaliteten med det samme. pip s�rger for at installere pakker automatisk og korrekt.

N�r Python, pip og Jupyter Notebooks er blevet sat op, kan vi begynde.

## Hvad er en variabel?

En variabel i Python bliver brugt til at gemme v�rdier i. Det vil sige at det alts� ikke fungere som i matematik hvor man f.eks. har en ukendt variabel. For at kunne bruge en variabel, skal den f�rst deklareres. Det betyder i alt sin enkelthed bare at man fort�ller Python f.eks. at `x = 3`. Hermed vil variablen `x` nu indeholde v�rdien `3`.

Det er vigtigt at forst� hvad variabler er i Python da de er smarte at arbejde med i forhold til alt i matematik. Det er heldigvis ikke s� besv�rligt. Variabler beh�ver heller ikke kun hedde enkelte bogstaver. Det vil sige at en variabel godt kan hedde `detHerErEnVariabel`. Generelt ser man bare gerne at man enten benytter sig af det der hedder _camelCase_ eller underscore `_`. Det skyldes at der ikke m� v�re mellemrum i variabelnavne. _camelCase_ fungere ved at man har et variabelnavn der best�r af flere ord. Her skriver man det f�rste ord med sm�t, i de efterf�lgende ord skriver man det f�rste bogstav med stort. Det tidligere eksempel p� et variabel navn er for eksempel i _camelCase_. Det nemmeste er dog nok bare at s�tte et underscore `_` mellem hvert ord.

Jeg vil igennem denne guide bruge variabler, s� kig med og se om brikkerne ikke hurtigt falder p� plads. Nedenfor kan du se et eksempel p� brug af en variabel.

# Her deklarere vi vores variabel
detHerErEnVariabel = 15

# Vi kan efterf�lgende skrive ud hvad vores variabel indeholder
print (detHerErEnVariabel)

Det smarte ved variable er ogs�, at de g�r det muligt at have flere outputs pr. celle i ens notebooks. Vi kan lave to variable og f� dem begge ud som output fra samme celle.

# Her deklarere vi vores variabel
detHerErEnVariabel = 15
detHerErEnNyVariabel = 17

# Vi kan efterf�lgende skrive ud hvad vores variabel indeholder
print (detHerErEnVariabel)
print (detHerErEnNyVariabel)

`print` funktionen g�r det ogs� muligt at print almindeligt tekst, med eller uden sin variabel. Det kr�ver bare at man s�tter enten `""` eller `''` rundt om sin tekst inde i parentesen.

print("Det her er bare tekst")

## Konvertering af typer

Vi kan ogs� g�re det sammen med variable.

print("Det her er vores variable " + str(detHerErEnVariabel))

Som det kan ses i eksemplet ovenfor, s� er det muligt at l�gge et tal og et stykke tekst sammen. Det er det fordi vi bruger funktionen `str()`. Denne funktion tager et tal ind i parentesen og omdanner det til en tekst streng. 

Det er n�dvendigt at g�re det p� denne m�de da Python ikke kan s�tte en tekst streng og et tal sammen. Og det er netop det vi g�r med det `+` vi har sat i eksemplet ovenfor. Det betyder basalt set at vi konkatenere to tekst strenge sammen. Hvis vi fors�ger at g�re det uden `str` funtionen, s� f�r vi en fejl

print("Det her er vores variable " + detHerErEnVariabel)

Vi ser ved fejlen at Python fort�ller os at en tekst streng ikke kan konkateneres sammen med en `int`, hvilket st�r for __Integer__. Mens `str` st�r for __String__.

Desuden viser det ovenst�ende eksempel at det er muligt at benytte variable som er blevet defineret i tidligere celler. Alle variable som bliver defineret i en Notebook er tilg�ngelige igennem alle celler i hele den Notebook. Eller, det er ikke helt rigtigt, for variablen er kun tilg�ngelig i celler efter den er blevet defineret. 

Man kan altid finde ud af hvilken type af variable man arbejder med, ved at bruge funktionen `type()` og indtaste sin variable i parentesen, som set nedenfor.

type(detHerErEnVariabel)

`detHerErEnVariabel` er typen __Integer__, alts� et heltal. Hvilket vi ogs� havde regnet med. Vi kan ogs� regne med decimaltal, i computerens verden er det dog en helt anden mundfuld. Derfor kaldes decimaltal ikke for __Integers__, men istedet for __Float__.