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

