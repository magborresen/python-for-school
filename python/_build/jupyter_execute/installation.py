# Installation

Vi skal have installeret de komponenter der er nødvendige for at kunne gøre brug af Jupyter Notebooks. Den vigtigste ingrediens er selvfølgelig Python. Der er flere måder at installere Python på, men for at bruge command line/terminalen mindst muligt, så foreslår jeg at installere Python igennem Anaconda distributionen. Anaconda giver en grafisk interface, til installering af selve Python, biblioteker og Jupyter Notebooks. Det kan umiddelbart være skræmmende at benytte command line, hvis det er første gang. [Så derfor vil jeg anbefale at downloade Anaconda Pyton 3.x herfra](https://www.anaconda.com/products/individual).

Det skal siges at Python kommer præinstalleret på Mac og Linux. Dog vil jeg stadig anbefale at benytte Anaconda Distributionen af Python, da den simpelthen bare er nemmere at have med at gøre, fordi den har det her grafiske interface.

Installationen burde være rimelig gnidningsfri. 

Det smarte ved at bruge Anaconda er, at Anaconda Navigator følger med. Det betyder at i stedet for at benytte Windows Command Line eller MacOS Terminale, så kan vi benytte os af en grafisk nagivator. Desuden kan Jupyter Notebooks åbnes direkte her igennem. Jupyter Notebooks, burde komme som standard sammen med installationen af Anaconda. 

## Installation af biblioteker

For at kunne benytte de funktionaliteter, som eksterne Python Biblioteker giver os, er vi nødt til at kunne installere dem. Dette er heldigvis nemt at gøre nu hvor vi har Anaconda installeret. 

I Python er det muligt at lave noget der hedder virtuelle miljøer. Det betyder, at når du laver ét bestemt Python program, så kan du bruge ét miljø, med nogle bestemt versioner af biblioteker. Mens du kan arbejde på et andet program med nogle andre versioner af de samme biblioteker. Det er ikke noget vi vil gå i dybden med nu, men i programmeringsverdenen er det meget omtalt. Derfor synes jeg det er vigtigt at gøre opmærksom på det.

For nu, installere vi blot bibliotekerne globalt. Det vil sige, at hver gang vi starter en ny notebook, så benytter vi de samme versioner af bibliotekerne som i alle vores andre notebooks.  

Installationen af biblioteker foregår igennem terminalen. Det kan være lidt skræmmende hvis det er første gang man åbner den, men bare rolig. Vi skal kun skrive én enkelt linje.

Det foregår mere eller mindre på samme måde for Mac og Windows. På en Mac skal du åbne det program der hedder __Terminal__. Mens på Windows skal du åbne __Command Prompt__. Du får nu en sort boks op på din skærm, med en markør der blinker, der viser at den er klar til at modtage tekst. Det eneste vi skal gøre nu er at, skrive `conda install` efterfulgt at navnet på det bibliotek du gerne vil installere. 

I løbet af bogen kommer vi f.eks. til at benytte biblioteket `sympy` en del. Så hvis vi skriver `conda install sympy`, så vil Anaconda automatisk installere `sympy` og gøre det klart til brug. 

Det var sådan set det hele.