# Statistik

Statistik er måske en af de vigtigste begreber inden for hverdags matematik. I min optik, bør der gøres meget mere ud af at lære statistik i folkeskolen. Men lad nu det ligge.

Vi skal i denne artikel kigge på hvordan vi kan bruge Python til at hjælpe os med statistik. Ofte går statistik dog også ud på at finde den bedste måde at formidle data til andre på. Derfor kigger vi også på hvordan Python kan hjælpe os med at visualisere vores statistiske data så vi nemt kan forklare det til andre.

Til vores held, er der i Python 3 et indbygget statistik bibliotek, som kan hjælpe os med alle de basale funktioner som man finder i folkeskole statistik. 

Så lad os starte med at importere det. Biblioteket hedder `statistics`, jeg importere det således, at jeg efterfølgende kan bruge forkortelsen `st`. Det gør jeg som nedenstående.

import statistics as st

De mest anvendte termer inden for statistik i folkeskolen er __hyppighed, frekvens, middelværdi, typetal__ og __median__. Så lad os tage dem én ad gangen.

## Hyppighed

Ved hyppighed kigger vi f.eks. på hvor mange gange det samme til optræder i vores datasæt. Datasættet er blot en reference til alle de tal vi er blevet opgivet. 