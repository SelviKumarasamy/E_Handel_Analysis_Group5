#                                        E-Hadelsanalysis


## Project beskrivning

I det här projektet arbetar vi med försäljningsdata för att identifiera användbara mönster och ta fram värdefulla insikter för ledningen inför nästa kampanjperiod.

Projektet är en gruppuppgift där vi använder Python för att analysera data, skapa funktioner och visualisera försäljningsresultat.

## Projektmål

 Målet med projektet är att besvara följande frågor:

1. Identifiera vilka produktkategorier som genererar högst intäkt.
2. Identifiera vilka städer som genererar högst intäkt.
3. Analysera försäljningstrender över tid.
4. Beräkna och förstå det genomsnittliga ordervärdet (AOV).
5. Identifiera de tre produktkategorier som genererar högst intäkt.
6. Upptäcka ovanliga värden eller oväntade försäljningsmönster.


## GitHub-repository

https://github.com/SelviKumarasamy/E_Handel_Analysis_Group5.git

## Projektstruktur

```text
├── data/
│   └── ecommerce_sales.csv
│
├── notebooks/
│   └── report.ipynb
│
├── src/
│   ├── __init__.py
│   ├── io_utils.py
│   ├── metrics.py
│   └── viz.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Dataset

Projektet använder datasetet (data/ecommerce_sales.csv)

## Teknik och verktyg

- **Python 3.14.7** – Programmering och dataanalys.
- Pandas – Datahantering och analys av försäljningsdata.
- NumPy – Beräkningar och statistisk analys.
- Matplotlib – Visualisering av försäljningsresultat.
- Jupyter Notebook – Interaktiv analys och rapportering.
- Git och GitHub – Versionshantering, koddelning och samarbete.
 
## Installation och start

### Steg 1: Klona projektet

git clone https://github.com/SelviKumarasamy/E_Handel_Analysis_Group5.git

cd E_Handel_Analysis_Group5

### Steg 2: Skapa en virtuell miljö

python -m venv .venv

### Steg 3: Aktivera den virtuella miljön

.venv\Scripts\activate

### Steg 4: Installera beroenden

Installera  Python-bibliotek som anges i requirements.txt

python -m pip install -r requirements.txt


## Nyckeltal (KPI)

- **Total intäkt:**  3,502,767.23 kr
- **Totalt antal sålda enheter:**  7463
- **Antal unika ordrar:**  2500
- **Genomsnittligt ordervärde:**  1 401,11 kr

## Figurer

## Slutsatsar från Analyserad Data

- Analysen visar att **Electronics** genererar högst intäkt,
med en total intäkt på **1 364 228,07 kr**.

- De tre kategorier som genererar högst intäkt är
**Electronics**, **Sports** och **Clothing**.

- **Stockholm** har den högsta totala intäkten i det analyserade
materialet med **1 227 201,94 kr**.

- Intäkten är högst under **Januari, med 664 083,32 kr** och lägst under **Mars, med 487 602,00 kr**.

- Electronics är kategorin med högst total intäkt i samtliga fem städer. Januari är den bästa månaden för Electronics i Göteborg, Malmö och Stockholm. I Uppsala är det februari och i Västerås juni.

## Grupparbete och samarbete

Fråga 1 - Anton Ahnstedt

Fråga 2 - Selvi Kumarasamy

Fråga 3 - Victor Lundström

Fråga 4 - Emma Lundbäck

Fråga 5 - Jena Greos

Fråga 6 -  Alla tillsammans

Vi hörde av oss till William, fick inget svar under dessa veckor. Så vi har exkluderat William under arbetets gång.

Projektet genomförs gemensamt av sex gruppmedlemmar. Arbetet delas upp så att varje medlem ansvarar för en separat ett specifikt nyckeltal.

Vi använder Git och GitHub för versionshantering, koddelning och samarbete. En Kanban-tavla används för att planera, fördela och följa upp arbetsuppgifter.

Varje gruppmedlem ansvarar för att utveckla, testa och dokumentera sin del av analysen. Därefter sammanförs de olika delarna i en gemensam rapport.

Vi strävar efter att skriva tydlig och återanvändbar kod genom att använda funktioner och separata Python-moduler. Detta gör projektet enklare att testa, underhålla och vidareutveckla.

## Rekommendationer



