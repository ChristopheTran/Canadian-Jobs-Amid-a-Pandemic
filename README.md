# Data Science Project
## Team: Citadel Corpos

There is increasing concern for living in big cities, due to unemployment and the cost of living. This
project scrapes and analyzes job postings from job boards to optimize job selections based on
Key Performance Indicators including quality of life index and crime rates for various regions.

- The KPI data is obtained from https://numbeo.com. 
- The current job market is analyzed by obtaining job posting data from https://www.jobbank.gc.ca.

## Setup Instructions:
The notebook that analyzes that datasets is called Final_Notebook.ipynb. For the Final_notebook.ipynb notebook to run successfuly, the DataSet folder is required to be in the same dirctory as the Final_notebook.ipynb file. All the python dependencies to run the code is located within the notebook.

The code used to scrape the numbeo and job bank data is located within the DataCollection.
- scrapeJobPosting.py :  scrapes each of the job posts within https://www.jobbank.gc.ca, extracts the main html content of each page and saves the result within .bz2 files named mainsList. The files can be found with the DataSet/JobPostProcessed directory. 
- JobPostScrapeDetails.py : iterates through each of the files within the DataSet/JobPostProcessed directory and parses the HTML to extract job post details such as the job title and the expected pay. The job details are then stored in a .csv file in the DataSet/JobPostDetails directory
- scrapeNumbeo.ipynb: scrapes the public web pages within the https://numbeo.com website and then uploads the result to a .csv file within the DataSet/Numbeo Data directory. The exact web pages that are scrapped is listed below. The data for each of the webpages is stored within its own .csv file. 

  - https://www.numbeo.com/cost-of-living/country_result.jsp?country=Canada
  - https://www.numbeo.com/property-investment/country_result.jsp?country=Canada
  - https://www.numbeo.com/health-care/country_result.jsp?country=Canada
  - https://www.numbeo.com/traffic/country_result.jsp?country=Canada
  - https://www.numbeo.com/quality-of-life/country_result.jsp?country=Canada
  - https://www.numbeo.com/crime/country_result.jsp?country=Canada 

## **Team Members**:
- Bejamine Melone
- Christophe Tran
- Christopher Wang
- Rahul Anikumar
- Michael Patsula

