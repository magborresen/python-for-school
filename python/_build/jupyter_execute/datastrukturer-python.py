# Datastrukturer i Python

Uha, det lyder allerede som noget meget teknisk når man har ordet datastruktur i en overskrift. Men heldigvis er det rigtig simpelt takket være Python. Datastrukturer er en vigtig del af alle programmeringssprog. De sørger for at vi kan opbevarer en større mængde data end blot det der kan være i en variabel. I Python finder vi generelt 3 datastrukturer __Lister__, __Tuples__ og __Dictionaries__. I folkeskole matematik kunne jeg forestille mig at __lister__ godt kunne blive brugt. Generelt bruger jeg ikke selv __Tuples__ så meget, da jeg synes de to andre strukturer har flere fordele. Lad os kigge på dem én for én og se hvordan de virker. 

## Lister

En liste er defineret ved hjælp af to klammer `[]`. Imellem de to klammer, har man så alt sin data. Dataen kan både være tal, decimaltal, tekst, variable eller en blanding af alle disse. Lister kan også gemmes som almindelige variable, hvilket gør at de er nemme at tilgå. Desuden er lister fede fordi de lader os ændre dataen i dem. Det er ikke alle datastrukturere der tillader ændringer i data. Lad os prøve at definere en liste der indeholder tallene `1`, `2` og `3`. Vi gemmer den som `liste`.

liste = [1, 2, 3]

Som det ses, så adskiller man sine data med et komma `,`. Lad os prøve at bruge `print()` funktionen på listen og se hvad der sker.

print(liste)

Vi får simpelthen bare hele listen ud... Men hvad nu hvis jeg gerne vil have fat i noget bestemt data i listen? Her kan vi bruge det vi kalder for indeksering. Vi skal blote skrive listens navn (`liste` i dette tilfælde) og specificere indenfor to klammer `[]` hvilken position vi ønsker at tilgå. Python benytter, som alle andre programmeringssprog, nul-indeksering. Det vil sige at vi starter fra 0. Da der i vores liste står `1` i første position, skal vi altså have fat i indeks `0`. Det gør vi ved

print(liste[0])

Og vupti, så har vi vores første position.

Hvis vi gerne vil have den sidste position i listen, så skal vi huske at vi starter med at tælle fra nul. I og med at vi har 3 stykker data i vores liste, så vil den sidste position altså være defineret som position `2`. Lad os prøve at printe den.

print(liste[2])

Fantastisk, det virker jo helt perfekt! Lad os for sjovs skyld, se hvad der sker, hvis vi giver et tal der er udenfor listens indeks, hvilket i dette tilfælde vil være `3`.

print(liste[3])

Vi får bare en fejl der siger at indekset ikke er inden for den rækkevidde listen har. Så husk derfor altid at tælle fra 0. Det kan spare en masse hovedpiner!

Det er også muligt at benytte negativ indeksering. Det betyder at hvis vi skriver `liste[-1]`, så vil vi få det stykke data ud, som står på den sidste position i listen. I tilfælde af vores variabel `liste`, vil det altså være `3`. 

print(liste[-1])

## Tuples

Tuples fungere lidt ligesom lister. Der er dog et par væsentlige forskelle. Første og fremmest, defineres en tuple ved at benytte parenteser `()` i stedet for klammer `[]`. Derudover er tuples ordnet, hvilket lister også er. Det betyder at data du propper ind, vil altid beholde samme position i tuplen eller listen. I modsætning til lister, så kan tuples ikke ændres når de først er lavet. Det vil sige, at hvis vi laver variablen `enTuple` som indeholder dataen `1`, `2` og `3`. Så kan den altså ikke ændres.

enTuple = (1, 2, 3)

print(enTuple)

Der er sikkert en rigtig god grund til at skulle bruge tuples. Men indenfor CAS og matematikens verden, har jeg endnu ikke haft brug for at benytte dem. Så derfor vil jeg ikke komme mere ind på dem. Men nu ved du de findes og der er tonsvis af information omkring dem overalt på internettet :-)

## Dictionaries

En Dictionary (dict) fungere lidt ligesom den lyder. Det er opslagsværk. En ordbog vil måske være en god analogi. Hvor man i en ordbog har et ord og en definition, har man i en dict, en __key__ og en __value__. En __key__ kan være alle datatyper. Men man ser ofte at der benyttes en tekststreng fordi det er nemmest at referere til, når man skal have data ud. Denne __key__ fungere ligesom ordet i ordbogen. Vores __value__ derimod fungere som ordets definition. Her kan vi specificere stort set lige hvad vi vil: en str, en int, en float, en liste, en tuple eller en helt ny dict. Dicts er smarte fordi den kan indehold utroligt meget data og de gør det let at tilgå. 

