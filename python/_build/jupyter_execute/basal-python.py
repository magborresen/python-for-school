# Start her

M�ske har du t�sket dig igennem mine forord og ved derfor allerede hvorfor jeg synes at Python i folkeskolen og gymnasiet er en god id�. Men hvis ikke, eller hvis du bare har lyst til at h�rer lidt mere omrking hvorfor jeg synes Python er s� fedt. S� l�s med her.

Python er det vi kalder for en __General Purpose Programming Language__. Alts� kort fortalt, et programmeringssprog som har mange anvendelser. I Pythons tilf�lde er det dog bare utroligt mange anvendelser. Og der kommer flere dag for dag.

Ikke nok med at vi kan bruge Python til at hj�lpe os med matematikken i form af CAS. Jamen s� kan vi faktisk ogs� bygge hele webplatforme (hjemmesider og applikationer i webbrowseren) i Python. Instagram's hjemmeside er f.eks. bygget ved hj�lp af Python biblioteket `Django`. Vi kan ogs� bruge Python til at lave programmer p� vores computer. Jeg skal senere vise hvordan vi kan benytte biblioteket `tkinter` til at lave en simpel lommeregner med en grafisk interface. Derudover kan Python ogs� benyttes til noget lidt mere h�ndgribeligt. `circuit Python` er begyndt at vende indtog blandt nybegyndere og hobby folk til at programmere mikrokontrollere i elektriske kredsl�b s�som Arduino. Det g�r barrieren for at komme igang v�senligt mindre, da man ikke l�ngere er n�dsaget til at l�re `C`.

## Det er meget fint, men hvad s� nu?

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

## Typer i Python

Som i alle andre programmeringssprog s� findes der nogle forskellige typer som et stykke data (som regel en variabel) kan have. Der er ikke s� mange typer at holde styr p�, i hvert fald ikke i basis syntaxen. Jeg har fors�gt at give et kort overblik over dem her.

* Int
    * Int er en forkortelse for Integer, hvilket i programmeringsverdenen betyder et hel tal. En Integer type kan v�re et heltal der b�de er positivt og negativt. Men det kan __ikke__ v�re et decimal tal.

* Float
    * Float er en forkortelse for floating point number, hvilket i programmeringsverdenen betyder et decimal tal. Tallet kan b�de v�re positivt og negativt
    
* Str
    * Str er en forkortelse for string, hvilket i programmeringsverdenen blot er en tekst streng.
    
* Bool
    * Bool er en forkortelse for boolean. Boolsk logik er utroligt meget brugt inden for programmeringsverdenen. Det er alts� en v�rdi som enten kan v�re sand eller falsk.
    
* Andre typer
    * Der findes masser af andre typer i Python og man vil hurtigt opdage at hvert bibliotek man importere, ogs� henter nye typer med sig. De ovenst�ende typer er de mest basale i Python og dem der er vigtigst and kende.

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