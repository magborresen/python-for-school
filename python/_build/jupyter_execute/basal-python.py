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

