# Variabler i Python

En variabel i Python bliver brugt til at gemme v�rdier i. Det vil sige at det alts� ikke fungere som i matematik hvor man f.eks. har en ukendt variabel. For at kunne bruge en variabel, skal den f�rst deklareres. Det betyder i alt sin enkelthed bare at man fort�ller Python f.eks. at `x = 3`. Hermed vil variablen `x` nu indeholde v�rdien `3`.

Det er vigtigt at forst� hvad variabler er i Python da de er smarte at arbejde med i forhold til alt i matematik. Det er heldigvis ikke s� besv�rligt. Variabler beh�ver heller ikke kun hedde enkelte bogstaver. Det vil sige at en variabel godt kan hedde `detHerErEnVariabel`. Generelt ser man bare gerne at man enten benytter sig af det der hedder _camelCase_ eller underscore `_`. Det skyldes at der ikke m� v�re mellemrum i variabelnavne. _camelCase_ fungere ved at man har et variabelnavn der best�r af flere ord. Her skriver man det f�rste ord med sm�t, i de efterf�lgende ord skriver man det f�rste bogstav med stort. Det tidligere eksempel p� et variabel navn er for eksempel i _camelCase_. Det nemmeste er dog nok bare at s�tte et underscore `_` mellem hvert ord.

Jeg vil igennem denne guide bruge variabler, s� kig med og se om brikkerne ikke hurtigt falder p� plads. Nedenfor kan du se et eksempel p� brug af en variabel.

# Her deklarere vi vores variabel
detHerErEnVariabel = 15

# Vi kan efterf�lgende skrive ud hvad vores variabel indeholder
print (detHerErEnVariabel)

Det smarte ved variable er ogs�, at de g�r det muligt at have flere outputs pr. celle i ens notebooks. Vi kan lave to variable og f� dem begge ud som output fra samme celle. Samtidigt kan vi benytte os af variabler der er blevet deklareret (defineret) i tidligere celler. Det vil sige at vores variabel `detHerErEnVariabel`, kan vi ogs� bruge i den n�ste celle nedenfor:

# Her deklarere vi vores variabel
detHerErEnVariabel = 15
detHerErEnNyVariabel = 17

# Vi kan efterf�lgende skrive ud hvad vores variabel indeholder
print (detHerErEnVariabel)
print (detHerErEnNyVariabel)

`print` funktionen g�r det ogs� muligt at print almindeligt tekst, med eller uden sin variabel. Det kr�ver bare at man s�tter enten `""` eller `''` rundt om sin tekst inde i parentesen.

print("Det her er bare tekst")