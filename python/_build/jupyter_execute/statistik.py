# Statistik

Statistik er m�ske en af de vigtigste begreber inden for hverdags matematik. I min optik, b�r der g�res meget mere ud af at l�re statistik i folkeskolen. Men lad nu det ligge.

Vi skal i denne artikel kigge p� hvordan vi kan bruge Python til at hj�lpe os med statistik. Ofte g�r statistik dog ogs� ud p� at finde den bedste m�de at formidle data til andre p�. Derfor kigger vi ogs� p� hvordan Python kan hj�lpe os med at visualisere vores statistiske data s� vi nemt kan forklare det til andre.

Til vores held, er der i Python 3 et indbygget statistik bibliotek, som kan hj�lpe os med alle de basale funktioner som man finder i folkeskole statistik. 

S� lad os starte med at importere det. Biblioteket hedder `statistics`, jeg importere det s�ledes, at jeg efterf�lgende kan bruge forkortelsen `st`. Det g�r jeg som nedenst�ende.

import statistics as st

De mest anvendte termer inden for statistik i folkeskolen er __hyppighed, frekvens, middelv�rdi, typetal__ og __median__. S� lad os tage dem �n ad gangen.

## Hyppighed

Ved hyppighed kigger vi f.eks. p� hvor mange gange det samme til optr�der i vores datas�t. Datas�ttet er blot en reference til alle de tal vi er blevet opgivet. 