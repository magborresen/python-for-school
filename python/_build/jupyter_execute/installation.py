# Installation

Vi skal have installeret de komponenter der er n�dvendige for at kunne g�re brug af Jupyter Notebooks. Den vigtigste ingrediens er selvf�lgelig Python. Der er flere m�der at installere Python p�, men for at bruge command line/terminalen mindst muligt, s� foresl�r jeg at installere Python igennem Anaconda distributionen. Anaconda giver en grafisk interface, til installering af selve Python, biblioteker og Jupyter Notebooks. Det kan umiddelbart v�re skr�mmende at benytte command line, hvis det er f�rste gang. [S� derfor vil jeg anbefale at downloade Anaconda Pyton 3.x herfra](https://www.anaconda.com/products/individual).

Det skal siges at Python kommer pr�installeret p� Mac og Linux. Dog vil jeg stadig anbefale at benytte Anaconda Distributionen af Python, da den simpelthen bare er nemmere at have med at g�re, fordi den har det her grafiske interface.

Installationen burde v�re rimelig gnidningsfri. 

Det smarte ved at bruge Anaconda er, at Anaconda Navigator f�lger med. Det betyder at i stedet for at benytte Windows Command Line eller MacOS Terminale, s� kan vi benytte os af en grafisk nagivator. Desuden kan Jupyter Notebooks �bnes direkte her igennem. Jupyter Notebooks, burde komme som standard sammen med installationen af Anaconda. 

## Installation af biblioteker

For at kunne benytte de funktionaliteter, som eksterne Python Biblioteker giver os, er vi n�dt til at kunne installere dem. Dette er heldigvis nemt at g�re nu hvor vi har Anaconda installeret. 

I Python er det muligt at lave noget der hedder virtuelle milj�er. Det betyder, at n�r du laver �t bestemt Python program, s� kan du bruge �t milj�, med nogle bestemt versioner af biblioteker. Mens du kan arbejde p� et andet program med nogle andre versioner af de samme biblioteker. Det er ikke noget vi vil g� i dybden med nu, men i programmeringsverdenen er det meget omtalt. Derfor synes jeg det er vigtigt at g�re opm�rksom p� det.

For nu, installere vi blot bibliotekerne globalt. Det vil sige, at hver gang vi starter en ny notebook, s� benytter vi de samme versioner af bibliotekerne som i alle vores andre notebooks.  

Installationen af biblioteker foreg�r igennem terminalen. Det kan v�re lidt skr�mmende hvis det er f�rste gang man �bner den, men bare rolig. Vi skal kun skrive �n enkelt linje.

Det foreg�r mere eller mindre p� samme m�de for Mac og Windows. P� en Mac skal du �bne det program der hedder __Terminal__. Mens p� Windows skal du �bne __Command Prompt__. Du f�r nu en sort boks op p� din sk�rm, med en mark�r der blinker, der viser at den er klar til at modtage tekst. Det eneste vi skal g�re nu er at, skrive `conda install` efterfulgt at navnet p� det bibliotek du gerne vil installere. 

I l�bet af bogen kommer vi f.eks. til at benytte biblioteket `sympy` en del. S� hvis vi skriver `conda install sympy`, s� vil Anaconda automatisk installere `sympy` og g�re det klart til brug. 

Det var s�dan set det hele.