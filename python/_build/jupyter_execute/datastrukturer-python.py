# Datastrukturer i Python

Uha, det lyder allerede som noget meget teknisk n�r man har ordet datastruktur i en overskrift. Men heldigvis er det rigtig simpelt takket v�re Python. Datastrukturer er en vigtig del af alle programmeringssprog. De s�rger for at vi kan opbevarer en st�rre m�ngde data end blot det der kan v�re i en variabel. I Python finder vi generelt 3 datastrukturer __Lister__, __Tuples__ og __Dictionaries__. I folkeskole matematik kunne jeg forestille mig at __lister__ godt kunne blive brugt. Generelt bruger jeg ikke selv __Tuples__ s� meget, da jeg synes de to andre strukturer har flere fordele. Lad os kigge p� dem �n for �n og se hvordan de virker. 

## Lister

En liste er defineret ved hj�lp af to klammer `[]`. Imellem de to klammer, har man s� alt sin data. Dataen kan b�de v�re tal, decimaltal, tekst, variable eller en blanding af alle disse. Lister kan ogs� gemmes som almindelige variable, hvilket g�r at de er nemme at tilg�. Desuden er lister fede fordi de lader os �ndre dataen i dem. Det er ikke alle datastrukturere der tillader �ndringer i data. Lad os pr�ve at definere en liste der indeholder tallene `1`, `2` og `3`. Vi gemmer den som `liste`.

liste = [1, 2, 3]

Som det ses, s� adskiller man sine data med et komma `,`. Lad os pr�ve at bruge `print()` funktionen p� listen og se hvad der sker.

print(liste)

Vi f�r simpelthen bare hele listen ud... Men hvad nu hvis jeg gerne vil have fat i noget bestemt data i listen? Her kan vi bruge det vi kalder for indeksering. Vi skal blote skrive listens navn (`liste` i dette tilf�lde) og specificere indenfor to klammer `[]` hvilken position vi �nsker at tilg�. Python benytter, som alle andre programmeringssprog, nul-indeksering. Det vil sige at vi starter fra 0. Da der i vores liste st�r `1` i f�rste position, skal vi alts� have fat i indeks `0`. Det g�r vi ved

print(liste[0])

Og vupti, s� har vi vores f�rste position.

Hvis vi gerne vil have den sidste position i listen, s� skal vi huske at vi starter med at t�lle fra nul. I og med at vi har 3 stykker data i vores liste, s� vil den sidste position alts� v�re defineret som position `2`. Lad os pr�ve at printe den.

print(liste[2])

Fantastisk, det virker jo helt perfekt! Lad os for sjovs skyld, se hvad der sker, hvis vi giver et tal der er udenfor listens indeks, hvilket i dette tilf�lde vil v�re `3`.

print(liste[3])

Vi f�r bare en fejl der siger at indekset ikke er inden for den r�kkevidde listen har. S� husk derfor altid at t�lle fra 0. Det kan spare en masse hovedpiner!

Det er ogs� muligt at benytte negativ indeksering. Det betyder at hvis vi skriver `liste[-1]`, s� vil vi f� det stykke data ud, som st�r p� den sidste position i listen. I tilf�lde af vores variabel `liste`, vil det alts� v�re `3`. 

print(liste[-1])

## Tuples

Tuples fungere lidt ligesom lister. Der er dog et par v�sentlige forskelle. F�rste og fremmest, defineres en tuple ved at benytte parenteser `()` i stedet for klammer `[]`. Derudover er tuples ordnet, hvilket lister ogs� er. Det betyder at data du propper ind, vil altid beholde samme position i tuplen eller listen. I mods�tning til lister, s� kan tuples ikke �ndres n�r de f�rst er lavet. Det vil sige, at hvis vi laver variablen `enTuple` som indeholder dataen `1`, `2` og `3`. S� kan den alts� ikke �ndres.

enTuple = (1, 2, 3)

print(enTuple)

Der er sikkert en rigtig god grund til at skulle bruge tuples. Men indenfor CAS og matematikens verden, har jeg endnu ikke haft brug for at benytte dem. S� derfor vil jeg ikke komme mere ind p� dem. Men nu ved du de findes og der er tonsvis af information omkring dem overalt p� internettet :-)

## Dictionaries

En Dictionary (dict) fungere lidt ligesom den lyder. Det er opslagsv�rk. En ordbog vil m�ske v�re en god analogi. Hvor man i en ordbog har et ord og en definition, har man i en dict, en __key__ og en __value__. En __key__ kan v�re alle datatyper. Men man ser ofte at der benyttes en tekststreng fordi det er nemmest at referere til, n�r man skal have data ud. Denne __key__ fungere ligesom ordet i ordbogen. Vores __value__ derimod fungere som ordets definition. Her kan vi specificere stort set lige hvad vi vil: en str, en int, en float, en liste, en tuple eller en helt ny dict. Dicts er smarte fordi den kan indehold utroligt meget data og de g�r det let at tilg�. 

