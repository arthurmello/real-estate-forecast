# REAL ESTATE VALUE ESTIMATION

This code contains a preliminary analysis on the transfer data, the purpose of which is to estimate the real estate value of a building (house or apartment)
from data such as its location and the demographic data relating to its postal code. The project was focused on the south west of France data.

It also contains an application with an interface, where it is possible to enter this information on a building and receive a sale price estimate.

# HOW TO USE THIS PROJECT

The Jupyter notebook already contains all the necessary information, so there is no need to run it.

To launch the application, you must first install the necessary libraries with the command `$ pip install -r requirements.txt`. Then, in the "app" folder, launch the application with the python app.py command. It will therefore be accessible from the URL http://localhost:5000/.

The application is used to estimate the value of a property (apartment or house). Once launched, to use it, you must enter the following information:

- Postal code
- Type of premises (Apartment / House)
- Actual building area (in m2)
- Land area (in m2)
- Number of main rooms
- Target price (the price estimated by the real estate agent)

# FOLDER STRUCTURE
```
case_study
│   README.md
│   exploration.ipynb
│
└───app
│   │   app.py
│   │   estimation.py
│   │   insee_code_postal
│   │   model.sav
│   │
│   └───templates
│       │   index.html
│       │   file112.txt
│   
└───data
    │   agence.csv
    │   france.csv
    │   insee_commune.csv
    │   localisation_commune.csv
```
