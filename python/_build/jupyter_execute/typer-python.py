# Typer i Python

Som i alle andre programmeringssprog så findes der nogle forskellige typer som et stykke data (som regel en variabel) kan have. Der er ikke så mange typer at holde styr på, i hvert fald ikke i basis syntaxen. Jeg har forsøgt at give et kort overblik over dem her.

* Int
    * Int er en forkortelse for Integer, hvilket i programmeringsverdenen betyder et hel tal. En Integer type kan være et heltal der både er positivt og negativt. Men det kan __ikke__ være et decimal tal.

* Float
    * Float er en forkortelse for floating point number, hvilket i programmeringsverdenen betyder et decimal tal. Tallet kan både være positivt og negativt
    
* Str
    * Str er en forkortelse for string, hvilket i programmeringsverdenen blot er en tekst streng.
    
* Bool
    * Bool er en forkortelse for boolean. Boolsk logik er utroligt meget brugt inden for programmeringsverdenen. Det er altså en værdi som enten kan være sand eller falsk.
    
* Andre typer
    * Der findes masser af andre typer i Python og man vil hurtigt opdage at hvert bibliotek man importere, også henter nye typer med sig. De ovenstående typer er de mest basale i Python og dem der er vigtigst and kende.

## Konvertering af typer

Vi kan også gøre det sammen med variable. Vi definere igen `detHerErEnVariabel=15` ligesom i sidste afsnit.

detHerErEnVariabel = 15

print("Det her er vores variable " + str(detHerErEnVariabel))

Det er nødvendigt at gøre det på denne måde da Python ikke kan sætte en tekst streng og et tal sammen. Og det er netop det vi gør med det `+` vi har sat i eksemplet ovenfor. Det betyder basalt set at vi konkatenere to tekst strenge sammen. Hvis vi forsøger at gøre det uden `str` funtionen, så får vi en fejl

print("Det her er vores variable " + detHerErEnVariabel)

Vi ser ved fejlen at Python fortæller os at en tekst streng ikke kan konkateneres sammen med en `int`, hvilket står for __Integer__. Mens `str` står for __String__.

Desuden viser det ovenstående eksempel at det er muligt at benytte variable som er blevet defineret i tidligere celler. Alle variable som bliver defineret i en Notebook er tilgængelige igennem alle celler i hele den Notebook. Eller, det er ikke helt rigtigt, for variablen er kun tilgængelig i celler efter den er blevet defineret. 

Man kan altid finde ud af hvilken type af variable man arbejder med, ved at bruge funktionen `type()` og indtaste sin variable i parentesen, som set nedenfor.

type(detHerErEnVariabel)

`detHerErEnVariabel` er typen __Integer__, altså et heltal. Hvilket vi også havde regnet med. Vi kan også regne med decimaltal, i computerens verden er det dog en helt anden mundfuld. Derfor kaldes decimaltal ikke for __Integers__, men istedet for __Float__.

Kan vi så også konvertere en `int` til en `str`? Ja, selvfølgelig kan vi det. Hvis du tænker dig lidt om, har du nok også allerede svaret på hvordan vi kan gøre det.

Lad os sige at vi har følgende tekststreng

tal = "1000"

For det blotte øje ligner det at der bare står tallet 1000. Det gør der sådan set også, men det er af typen `string` fordi vi har puttet to gåseøjne omkring. Så hvis vi forsøger at ligge `tal` sammen med et andet tilfældigt tal, som er defineret som en `int`, så får vi

tal2 = 1000

print(tal + tal2)

Python tror altså vi forsøger at lave det der hedder __String konkatenering__. Hvor man simpelthen ligger to `str` typer sammen. Men det er jo ikke det vi vil. Derfor skal vi først konveretere `tal` variablen til en `int` type. Det gør vi ved

print(int(tal) + tal2)

Så får vi det rigtige resultat!

## Ekstra for sjov

Det næste her er ikke nødvendig læsning for at kunne benytte Python til matematiske formål. Men jeg synes at det er rart nok lige at komme ind på hvad __String konkatenering__ egentlig er, nu hvor jeg nævnte det. 

Det foregår ved at man kan ligge to `str` typer sammen. Det vil sige at hvis vi konvertere `tal2` til en `str` i stedet for at konvertere `tal` til en `int`, så kan vi stadig ligge dem sammen.

print(tal + str(tal2))

Som vi kan se, betyder konkatenering blot at vi lægger den ene tekststreng lige bagved den anden.

