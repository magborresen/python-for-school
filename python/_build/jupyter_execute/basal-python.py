# Hvorfor Python?

Hvis man sidder på en Mac eller Linux computer vil Python allerede være præinstalleret. Hvis man sidder på en Windows computer derimod, skal Python installeres. Jeg vedhæfter et link til en guide for installation.

Der findes 2 versioner af Python. Python 2 og Python 3. I denne notesbog, vil der dog blive brugt Python 3, da Python 2 ikke længere vil være supporteret fra udviklerne i 2020. 

For at kunne udarbejder matematik afleveringer og prøver med Python, foreslår jeg at installere Jupyter Notebooks. Dette gøres ved hjælp af Python indbyggede pakke distrubtionssystem kaldet pip. Jeg vedhæfter en guide til hvordan Jupyter Notebooks installeres, samt hvordan man bruger pip generelt. Når Python er installeret kræver pip ingen ekstra opsætning, og man vil kunne bruge funktionaliteten med det samme. pip sørger for at installere pakker automatisk og korrekt.

Når Python, pip og Jupyter Notebooks er blevet sat op, kan vi begynde.

## Hvad er en variabel?

En variabel i Python bliver brugt til at gemme værdier i. Det vil sige at det altså ikke fungere som i matematik hvor man f.eks. har en ukendt variabel. For at kunne bruge en variabel, skal den først deklareres. Det betyder i alt sin enkelthed bare at man fortæller Python f.eks. at `x = 3`. Hermed vil variablen `x` nu indeholde værdien `3`.

Det er vigtigt at forstå hvad variabler er i Python da de er smarte at arbejde med i forhold til alt i matematik. Det er heldigvis ikke så besværligt. Variabler behøver heller ikke kun hedde enkelte bogstaver. Det vil sige at en variabel godt kan hedde `detHerErEnVariabel`. Generelt ser man bare gerne at man enten benytter sig af det der hedder _camelCase_ eller underscore `_`. Det skyldes at der ikke må være mellemrum i variabelnavne. _camelCase_ fungere ved at man har et variabelnavn der består af flere ord. Her skriver man det første ord med småt, i de efterfølgende ord skriver man det første bogstav med stort. Det tidligere eksempel på et variabel navn er for eksempel i _camelCase_. Det nemmeste er dog nok bare at sætte et underscore `_` mellem hvert ord.

Jeg vil igennem denne guide bruge variabler, så kig med og se om brikkerne ikke hurtigt falder på plads. Nedenfor kan du se et eksempel på brug af en variabel.

# Her deklarere vi vores variabel
detHerErEnVariabel = 15

# Vi kan efterfølgende skrive ud hvad vores variabel indeholder
print (detHerErEnVariabel)

Det smarte ved variable er også, at de gør det muligt at have flere outputs pr. celle i ens notebooks. Vi kan lave to variable og få dem begge ud som output fra samme celle.

# Her deklarere vi vores variabel
detHerErEnVariabel = 15
detHerErEnNyVariabel = 17

# Vi kan efterfølgende skrive ud hvad vores variabel indeholder
print (detHerErEnVariabel)
print (detHerErEnNyVariabel)

`print` funktionen gør det også muligt at print almindeligt tekst, med eller uden sin variabel. Det kræver bare at man sætter enten `""` eller `''` rundt om sin tekst inde i parentesen.

print("Det her er bare tekst")

## Konvertering af typer

Vi kan også gøre det sammen med variable.

print("Det her er vores variable " + str(detHerErEnVariabel))

Som det kan ses i eksemplet ovenfor, så er det muligt at lægge et tal og et stykke tekst sammen. Det er det fordi vi bruger funktionen `str()`. Denne funktion tager et tal ind i parentesen og omdanner det til en tekst streng. 

Det er nødvendigt at gøre det på denne måde da Python ikke kan sætte en tekst streng og et tal sammen. Og det er netop det vi gør med det `+` vi har sat i eksemplet ovenfor. Det betyder basalt set at vi konkatenere to tekst strenge sammen. Hvis vi forsøger at gøre det uden `str` funtionen, så får vi en fejl

print("Det her er vores variable " + detHerErEnVariabel)

Vi ser ved fejlen at Python fortæller os at en tekst streng ikke kan konkateneres sammen med en `int`, hvilket står for __Integer__. Mens `str` står for __String__.

Desuden viser det ovenstående eksempel at det er muligt at benytte variable som er blevet defineret i tidligere celler. Alle variable som bliver defineret i en Notebook er tilgængelige igennem alle celler i hele den Notebook. Eller, det er ikke helt rigtigt, for variablen er kun tilgængelig i celler efter den er blevet defineret. 

Man kan altid finde ud af hvilken type af variable man arbejder med, ved at bruge funktionen `type()` og indtaste sin variable i parentesen, som set nedenfor.

type(detHerErEnVariabel)

`detHerErEnVariabel` er typen __Integer__, altså et heltal. Hvilket vi også havde regnet med. Vi kan også regne med decimaltal, i computerens verden er det dog en helt anden mundfuld. Derfor kaldes decimaltal ikke for __Integers__, men istedet for __Float__.