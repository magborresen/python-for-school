# Forord

Jeg har igennem min, nu (langvarie) uddannelsesvej v�ret udsat for diverse v�rkt�jer inden for matematikken. I folkeskolen var det en blyant, et stykke papir og en Texas Instruments lommeregner. Det blev sidenhen erstattet p� gymnasiet af v�rkt�jet Maple, som enten bliver din bedste ven eller den v�rste fjende. For mig var det nr. 2 mulighed. Matematik bet�d ikke s�rlig meget for mig dengang, og det gjorde processen ved at forst� hvordan en v�rkt�j som Maple fungere, derfor heller ikke. 

Sidenhen er jeg blevet klogere og da jeg ville begynde at l�se enkeltfag op, for at komme ind p� ingeni�r studiet, fik jeg af min matematikl�rer p� HF-Enkeltfag at her brugte man WordMat. WordMat fungere som en tredjeparts udvidelse til Microsoft Word. Det er udviklet af en meget entusiastisk gymnasiel�rer p� Sj�lland og har haft sit indtog p� mange gymnasier i Danmark, da system er gratis. 
Og gratis er her n�gleordet, for et v�rkt�j som Maple er ikke gratis. Licenser til s�danne professionelle v�rkt�jer er dyre og det f�r mange gymnasier og institutioner til, at ligge pengepungen i lommen og lede efter alternative l�sninger. 

Her finder man s� WordMat som lige pludselig er gratis og som g�r at eleverne kan skrive deres opgaver og lave udregninger direkte i Word. Herefter har l�reren s� mulighed for, ved at bruge en l�rer udvidelse til WordMat, at rette opgaverne direkte i samme dokument. Det er da skide smart. Eller hvad? Ja, det g�r da helt sikkert livet nemmere for skole og l�rer. Skolen slipper for, at smide penge efter et dyre licenser til programmer som Maple og l�rerne f�r mindre besv�r ved at rette opgaver. 

Men hvad med dem det egentlig drejer som om, eleverne? Hvad f�r de ud af det? Ved at benytte sig af programmer som WordMat istedet for Maple, fratager man eleverne en gylden mulighed for at blive klar til deres videre akademiske f�rden. WordMat har p� ingen m�de noget som helst indtog nogen andre steder end i gymnasierne. Det samme kan udmiddelbart siges for Maple. WordMat er komfortabelt for eleverne idet de allerede kender til Microsoft Word milj�et. Problemet opst�r lige s� snart eleven er f�rdig med sin gymnasielle uddannelse og vil starte p� universitetet. Alt viden omkring brugen af WordMat er her fuldst�ndig ubrugeligt. Eleverne har hermed brugt op til 3 �r (Hvis det ikke allerede er blevet till�rt i folkeskolen) p�, at l�re et system som de aldrig kommer til at bruge igen. Men hvad betyder det? Det var jo billigt for skolen og nemt for l�reren.

Jeg kan selvf�lgelig sagtens sidde og pr�dike om hvor frustrende jeg synes denne l�sning er, og hvor frustreret jeg selv var da jeg selv stod i situationen. Maple er for dyrt til at alle skoler vil adoptere det. WordMat er for ustabilt, urelevant og ugennemt�nkt til at det b�r till�res af elever. Derfor opstiller jeg et foreslag til �ndring af IT-Hj�lpermidler til brug i b�de folkeskole og gymnasier. Det er n�dvendigt at eleverne for noget med fra deres studietid, som de kan benytte sig af senere, enten p� en videreg�ende uddannelse, eller i erhvervs livet. 
Det er utrolig meget oppe i tiden, at vi gerne vil l�re b�rn og unge at programmere i en tidlig alder. Jeg er derfor af den overbevisning, at matematik undervisning og programmering b�r kombineres. Det er tog fag som sidel�bende komplimentere hinanden p� stort set alle naturvidenskabelige videreg�ende uddannelser. De fleste universiteter idag, benytter sig af programmet MATLAB. MATLAB er dog et produkt som skal k�bes licens til. Derfor vil det, som Maple, ikke l�se problemet med at der skal indk�bes dyre licenser til alle elever. Der er simpelthen brug for en anden l�sning. Hertil indtroducere jeg Python. 

Python er et programmeringssprog som er baseret sproget C. Men i forhold til C er Python nemt at l�re idet syntaxen (selve grammatikken) er utrolig overskuelig. Python har indbyggede matematik biblioteker til de mest basaler elementer i matematikken. Der kan derudover nemt installeres og importeres flere biblioteker til de mere grafiske og komplekse dele af matematikken. Det bedste ved Python er, at det er open-source, hvilket betyder at det er gratis at installere og benytte. Jeg har derudover endnu ikke st�dt p� et bibliotek som ikke er open-source og dermed ogs� gratis at installere. Det betyder dermed nul omkostninger for skolerne. Python er desuden benyttet i stor stil i erhvervslivet da det ikke blot kan benyttes til matematik, men ogs� til form�l som webudvikling, databasestyring, simuleringer, Machine Learning, kunstig intelligens og meget mere. 

Til Python, er der en udvidelse som hedder "Jupyter Notebook". Denne tekst er f.eks. skrevet i en s�dan "notesbog". Jupyter Notebooks g�r det nemt at have individuelle celler med kode. Det vil sige at i hver celle, kan der repr�senteres en opgave. N�r eleven har f�rdiggjort sin opgave og vil aflevere den, giver Jupyter mulighed for at eksportere opgaven som PDF. Herefter kan den afleveres hvor l�reren har s� har nem mulighed for at skrive kommentarer i PDF filen. 

Alt det her, er selvf�lgelig nemt for mig, at sidde og liste op. Jeg vil derfor benytte resten af denne Jupyter Noteboook tit, at vise hvordan Python kan benyttes. Dette kan benyttes b�de som reference af l�rere og elever.

Inden vi begynder, vil jeg til sidst sige at form�let med dette er, at skabe en universel m�de at arbejde og l�re p�. For mig at se, nytter det ikke noget at der kommer elever ud af vores ungdomsuddannelser, som er opl�rt i 5 forskellige matematiske v�rkt�jer. Det handler om at klarg�re elever til livet. Men samtidigt handler det ogs� om at give elever en bl�d introduktion til programmering, hvilket jeg vil mene at matematik delen hj�lper med. 


```{toctree}
:hidden:
:titlesonly:
:caption: Kom Igang

installation
basal-jupyter
basal-python
```


```{toctree}
:hidden:
:titlesonly:
:caption: Matematik med Python

basal-matematik
trigonometri
ligninger
funktioner
```
