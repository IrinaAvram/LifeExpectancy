# How more doctors translates into longer lifespans (even for men)

This project portrays to the first exercise of the Digital Preservation course, in the summer semester of 2018, at the Vienna University of Technology.
The project relies on two datasets, one regarding life expectancy and the other regarding doctors per 1000 inhabitants since 2015, 
and another one contains demographic data regarding Vienna.
The correlation between the increase in doctors per 1000 inhabitants and the life expectancy in Vienna is showcased, 
as well as the difference between the life expectancy of males and females.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Install Jupyter using Anaconda

  * First, [download](https://www.anaconda.com/download/) Anaconda. We recommend downloading Anaconda’s latest Python 3 version.

  * Second, install the version of Anaconda which you downloaded, following the instructions on the download page.
  
* Register for a plot.ly [account](https://plot.ly/accounts/login/?action=signup)


### Installing


* Run the jupiter notebook either by executing the following command from the terminal:

```
jupyter notebook
```

Or by opening the application ```Jupyter Notebook``` (For Windows Systems) 



* Create a new notebook and paste the code from the ```scripts``` folder of this project into the notebook.
* Edit the following line ```pt.set_credentials_file(username='<INSERT USERNAME HERE>', api_key='<INSERT API KEY HERE>')```
to contain your credentials.
* Ensure the paths to the ```input``` folder of this project are correct throughout the code.
* Run the notebook.



## Built With

* [Jupyter Notebooks](http://jupyter.org/) - The framework used for the computations
* [Plot.ly](https://plot.ly/) - Library used for generating the graphs




## Authors

* **Irina Avram** - ORCID ID: 0000-0001-9034-9043
* **Victor - Gabriel Dulca** - ORCID ID: 0000-0001-5537-1843



## License

The data produced by this experiment, is released under the Creative Commons Attribution-ShareAlike 4.0 International license,
as to comply with the attribution requirements of the previous paragraph, 
while the code is released under version 3 of the GNU GENERAL PUBLIC LICENSE.

## Acknowledgments

* Stadt Wien – data.wien.gv.at - [Demographic indicators in Vienna since 1961](https://www.wien.gv.at/statistik/ogd/vie_005.csv)  (Accessed on 21 March 2018)
* OECD (2018), Doctors (indicator). doi: 10.1787/4355e1ec-en (Accessed on 21 March 2018)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1209826.svg)](https://doi.org/10.5281/zenodo.1209826)
