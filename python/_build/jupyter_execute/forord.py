# Forord

Jeg har igennem min, nu (langvarie) uddannelsesvej været udsat for diverse værktøjer inden for matematikken. I folkeskolen var det en blyant, et stykke papir og en Texas Instruments lommeregner. Det blev sidenhen erstattet på gymnasiet af værktøjet Maple, som enten bliver din bedste ven eller den værste fjende. For mig var det nr. 2 mulighed. Matematik betød ikke særlig meget for mig dengang, og det gjorde processen ved at forstå hvordan en værktøj som Maple fungere, derfor heller ikke. 

Sidenhen er jeg blevet klogere og da jeg ville begynde at læse enkeltfag op, for at komme ind på ingeniør studiet, fik jeg af min matematiklærer på HF-Enkeltfag at her brugte man WordMat. WordMat fungere som en tredjeparts udvidelse til Microsoft Word. Det er udviklet af en meget entusiastisk gymnasielærer på Sjælland og har haft sit indtog på mange gymnasier i Danmark, da system er gratis. 
Og gratis er her nøgleordet, for et værktøj som Maple er ikke gratis. Licenser til sådanne professionelle værktøjer er dyre og det får mange gymnasier og institutioner til, at ligge pengepungen i lommen og lede efter alternative løsninger. 

Her finder man så WordMat som lige pludselig er gratis og som gør at eleverne kan skrive deres opgaver og lave udregninger direkte i Word. Herefter har læreren så mulighed for, ved at bruge en lærer udvidelse til WordMat, at rette opgaverne direkte i samme dokument. Det er da skide smart. Eller hvad? Ja, det gør da helt sikkert livet nemmere for skole og lærer. Skolen slipper for, at smide penge efter et dyre licenser til programmer som Maple og lærerne får mindre besvær ved at rette opgaver. 

Men hvad med dem det egentlig drejer som om, eleverne? Hvad får de ud af det? Ved at benytte sig af programmer som WordMat istedet for Maple, fratager man eleverne en gylden mulighed for at blive klar til deres videre akademiske færden. WordMat har på ingen måde noget som helst indtog nogen andre steder end i gymnasierne. Det samme kan udmiddelbart siges for Maple. WordMat er komfortabelt for eleverne idet de allerede kender til Microsoft Word miljøet. Problemet opstår lige så snart eleven er færdig med sin gymnasielle uddannelse og vil starte på universitetet. Alt viden omkring brugen af WordMat er her fuldstændig ubrugeligt. Eleverne har hermed brugt op til 3 år (Hvis det ikke allerede er blevet tillært i folkeskolen) på, at lære et system som de aldrig kommer til at bruge igen. Men hvad betyder det? Det var jo billigt for skolen og nemt for læreren.

Jeg kan selvfølgelig sagtens sidde og prædike om hvor frustrende jeg synes denne løsning er, og hvor frustreret jeg selv var da jeg selv stod i situationen. Maple er for dyrt til at alle skoler vil adoptere det. WordMat er for ustabilt, urelevant og ugennemtænkt til at det bør tillæres af elever. Derfor opstiller jeg et foreslag til ændring af IT-Hjælpermidler til brug i både folkeskole og gymnasier. Det er nødvendigt at eleverne for noget med fra deres studietid, som de kan benytte sig af senere, enten på en videregående uddannelse, eller i erhvervs livet. 
Det er utrolig meget oppe i tiden, at vi gerne vil lære børn og unge at programmere i en tidlig alder. Jeg er derfor af den overbevisning, at matematik undervisning og programmering bør kombineres. Det er tog fag som sideløbende komplimentere hinanden på stort set alle naturvidenskabelige videregående uddannelser. De fleste universiteter idag, benytter sig af programmet MATLAB. MATLAB er dog et produkt som skal købes licens til. Derfor vil det, som Maple, ikke løse problemet med at der skal indkøbes dyre licenser til alle elever. Der er simpelthen brug for en anden løsning. Hertil indtroducere jeg Python. 

Python er et programmeringssprog som er baseret sproget C. Men i forhold til C er Python nemt at lære idet syntaxen (selve grammatikken) er utrolig overskuelig. Python har indbyggede matematik biblioteker til de mest basaler elementer i matematikken. Der kan derudover nemt installeres og importeres flere biblioteker til de mere grafiske og komplekse dele af matematikken. Det bedste ved Python er, at det er open-source, hvilket betyder at det er gratis at installere og benytte. Jeg har derudover endnu ikke stødt på et bibliotek som ikke er open-source og dermed også gratis at installere. Det betyder dermed nul omkostninger for skolerne. Python er desuden benyttet i stor stil i erhvervslivet da det ikke blot kan benyttes til matematik, men også til formål som webudvikling, databasestyring, simuleringer, Machine Learning, kunstig intelligens og meget mere. 

Til Python, er der en udvidelse som hedder "Jupyter Notebook". Denne tekst er f.eks. skrevet i en sådan "notesbog". Jupyter Notebooks gør det nemt at have individuelle celler med kode. Det vil sige at i hver celle, kan der repræsenteres en opgave. Når eleven har færdiggjort sin opgave og vil aflevere den, giver Jupyter mulighed for at eksportere opgaven som PDF. Herefter kan den afleveres hvor læreren har så har nem mulighed for at skrive kommentarer i PDF filen. 

Alt det her, er selvfølgelig nemt for mig, at sidde og liste op. Jeg vil derfor benytte resten af denne Jupyter Noteboook tit, at vise hvordan Python kan benyttes. Dette kan benyttes både som reference af lærere og elever.

Inden vi begynder, vil jeg til sidst sige at formålet med dette er, at skabe en universel måde at arbejde og lære på. For mig at se, nytter det ikke noget at der kommer elever ud af vores ungdomsuddannelser, som er oplært i 5 forskellige matematiske værktøjer. Det handler om at klargøre elever til livet. Men samtidigt handler det også om at give elever en blød introduktion til programmering, hvilket jeg vil mene at matematik delen hjælper med. 


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
