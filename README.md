rentmap
=======

Visualizer of the Zillow Observed Rent Index and other useful geographical properties.


Usage
-----
1.  Clone this repository.
2.  Get the submodules with `git submodule update --init`
3.  Create and activate a new Python virtual environment.
    ```
    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
    ```
4.  Download the Zillow Observed Rent Index data with 'Zip Codes' geography from
    [Zillow Research](https://www.zillow.com/research/data/) into
    `data/Zip_ZORI_AllHomesPlusMultifamily_SSA.csv`.
5.  Run `python -m rentmap`
6.  Open the resulting HTML file in your browser.


Visualized Data
---------------
 - [x] [Zillow Observed Rent Index (ZORI)](https://www.zillow.com/research/data/)
 - [x] [Midwifery Friendliness](https://mana.org/about-midwives/state-by-state)
 - [x] [Political affiliation](https://github.com/Prooffreader/election_2016_data/tree/master/data)
 - [x] [Vaccine laws](https://www.cdc.gov/phlp/docs/school-vaccinations.pdf)
 - [x] [Homeschooling laws](https://hslda.org/legal)
 - [ ] Crime Data
    - [x] [Colorado](https://crime-data-explorer.fr.cloud.gov/pages/home)
    - [ ] Other states...
 - [ ] Climate
    - Temperature
    - Humidity
    - Mosquitoes
