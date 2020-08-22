# Typer i Python

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

Vi kan ogs� g�re det sammen med variable. Vi definere igen `detHerErEnVariabel=15` ligesom i sidste afsnit.

detHerErEnVariabel = 15

print("Det her er vores variable " + str(detHerErEnVariabel))

Det er n�dvendigt at g�re det p� denne m�de da Python ikke kan s�tte en tekst streng og et tal sammen. Og det er netop det vi g�r med det `+` vi har sat i eksemplet ovenfor. Det betyder basalt set at vi konkatenere to tekst strenge sammen. Hvis vi fors�ger at g�re det uden `str` funtionen, s� f�r vi en fejl

print("Det her er vores variable " + detHerErEnVariabel)

Vi ser ved fejlen at Python fort�ller os at en tekst streng ikke kan konkateneres sammen med en `int`, hvilket st�r for __Integer__. Mens `str` st�r for __String__.

Desuden viser det ovenst�ende eksempel at det er muligt at benytte variable som er blevet defineret i tidligere celler. Alle variable som bliver defineret i en Notebook er tilg�ngelige igennem alle celler i hele den Notebook. Eller, det er ikke helt rigtigt, for variablen er kun tilg�ngelig i celler efter den er blevet defineret. 

Man kan altid finde ud af hvilken type af variable man arbejder med, ved at bruge funktionen `type()` og indtaste sin variable i parentesen, som set nedenfor.

type(detHerErEnVariabel)

`detHerErEnVariabel` er typen __Integer__, alts� et heltal. Hvilket vi ogs� havde regnet med. Vi kan ogs� regne med decimaltal, i computerens verden er det dog en helt anden mundfuld. Derfor kaldes decimaltal ikke for __Integers__, men istedet for __Float__.

Kan vi s� ogs� konvertere en `int` til en `str`? Ja, selvf�lgelig kan vi det. Hvis du t�nker dig lidt om, har du nok ogs� allerede svaret p� hvordan vi kan g�re det.

Lad os sige at vi har f�lgende tekststreng

tal = "1000"

For det blotte �je ligner det at der bare st�r tallet 1000. Det g�r der s�dan set ogs�, men det er af typen `string` fordi vi har puttet to g�se�jne omkring. S� hvis vi fors�ger at ligge `tal` sammen med et andet tilf�ldigt tal, som er defineret som en `int`, s� f�r vi

tal2 = 1000

print(tal + tal2)

Python tror alts� vi fors�ger at lave det der hedder __String konkatenering__. Hvor man simpelthen ligger to `str` typer sammen. Men det er jo ikke det vi vil. Derfor skal vi f�rst konveretere `tal` variablen til en `int` type. Det g�r vi ved

print(int(tal) + tal2)

S� f�r vi det rigtige resultat!

## Ekstra for sjov

Det n�ste her er ikke n�dvendig l�sning for at kunne benytte Python til matematiske form�l. Men jeg synes at det er rart nok lige at komme ind p� hvad __String konkatenering__ egentlig er, nu hvor jeg n�vnte det. 

Det foreg�r ved at man kan ligge to `str` typer sammen. Det vil sige at hvis vi konvertere `tal2` til en `str` i stedet for at konvertere `tal` til en `int`, s� kan vi stadig ligge dem sammen.

print(tal + str(tal2))

Som vi kan se, betyder konkatenering blot at vi l�gger den ene tekststreng lige bagved den anden.

