#Kaip buvo atlikta 2 dalis
Pačioj įdėjos įgyvendinimui, buvo naudotas: Naive Gaussian bayes metodas.

Idėjos pasisėmiau iš: https://www.youtube.com/watch?v=H3EjCKtlVog

Duomenis buvo padailtinti į mokymo, testavimo aibes.
Šis metodas patogus tuom, kad leidžia paliginti duomenis tarp dviejų klasiu, tuo pačiu priskirti tuos duomenis tai arba kitai klasei.
Kaip buvo atlikta:
1. Buvo paskaičiuota kiekvienos klasės:
1.1. p (kiek dažnai pasitaikė iš duomenų aibės);
1.2. požymių vidurkį;
1.3. standartini pasiskirtimą
2. nuskaityti testavimo duomenis
3. skaičiuojamas nuskaitytų duomenų klasės įvertis:
3.1. paskaičiuojama naudojant log, kad išvengti klaidų su mažais skaičiais;
4. paliginamos dviejų klasių paskaičiuoti įverčiai. Kieno didesnis, tai klasei ir priskiriamas.

# IS-Lab1 (LT)
Intelektualiosios sistemos. Pirmojo laboratorinio darbo užduotis.
# Tikslas
Išmokti savarankiškai suprogramuoti paprasto tiesinio klasifikatoriaus mokymo (parametrų skaičiavimo) algoritmą.
# Užduotys (maks. 8 balai)
1. Sukurkite paprasto klasifikatoriaus (Perceptrono) išėjimui apskaičiuoti skirtą programą. Klasifikatorius turi skirstyti objektus į dvi klases, pagal du požymius. Išėjimo skaičiavimas atliekamas pagal formulę:
y = 1, kai x1\*w1 + x2\*w2 + b > 0; y = -1, kai x1\*w1 + x2\*w2 + b <= 0; čia w1, w2 ir b parametrai, kurie turi būti sugeneruojami naudojant atsitiktinių skaičių generatorių (MATLAB pvz.: w1 = randn(1);) pirmąją programos veikimo iteraciją ir vėliau atnaujinami mokymo algoritmu; x1 ir x2 yra objektų požymiai, apskaičiuoti Matlab funkcijomis, esančiomis paruoštame kodo ruošinyje arba Data.txt faile (kiekvienoje eilutėje yra toks duomenų formatas: *požymis1, požymis2, norimas_atsakymas*), jei ketinate naudoti ne Matlab.
2. Parašykite mokymo algoritmą sukurto klasifikatoriaus parametrams apskaičiuoti. Naudokite šią parametrų atnaujinimo formulę:
w1(n+1) = w1(n) + eta\*e(n)\*x1(n); čia 0 < eta < 1; e(n) = d(n) - y(n); - klaida (momentinė klaida), apskaičiuota palyginus norimą atsakymą su tuo, kuris gautas klasifikatoriaus išėjime.
w2(n+1) = w2(n) + eta\*e(n)\*x2(n);
b(n+1) = b(n) + eta\*e(n);
# Papildoma užduotis (papildomi 2 balai)
Išspręskite šį klasifikavimo uždavinį naudodami Naive Bayes Classifier.
Kelios nuorodos į paprastai pateiktus šio tipo klasifikatoriaus taikymo pavyzdžius:
- http://www.statsoft.com/textbook/naive-bayes-classifier
- https://en.wikipedia.org/wiki/Naive_Bayes_classifier
# Rekomenduojama literatūra
- Neural Networks and Learning Machines (3rd Edition), 54 psl., 1.1 lentelė
