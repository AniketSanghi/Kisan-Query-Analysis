## Programming Language Required
- python 3.6.9

## Packages Required
* selenium

## Link to project on github
[Kisan Query Analysis](https://github.com/neilrs123/Kisan-Query-Analysis)

## Directory Structure
- `scraping` contains codes to scrape the complete dataset in the form of csv files
- `preprocessing` contains codes to convert the csv files to construct a single json file after relevant preprocessing
- `data` contains all the csv files and preprocessed json file
- `library` contains json file storing coordinates of states to plot data on states of India
- All the analysis are independent from each other and the codes are contained in their respective directories:
  - [Classfication](Classification)
  - [FAQ](FAQ)
  - [General Analysis](<General Analysis>)
  - [government scheme analysis](<government scheme analysis>)
  - [plant_protection_analysis](plant_protection_analysis)
  - [weather](weather)

## How to execute the project
- To scrape the data either do:
  1.
    - `cd scraping`
    - Download latest mozilla geckodriver from [here](https://github.com/mozilla/geckodriver/releases)
    - Place the downloaded driver inside `drivers` directory with name: `geckodriver`. So, final structure should be `drivers/geckodriver`.
    - ```
      chmod 700 *.sh
      bash scraping.sh
      ```
      But this can take more than 24hrs depending on your internet connection.

     OR

  2.
    - We have uploaded the scraped data to google drive, so you can download the zip of the dataset from [here](https://drive.google.com/file/d/1KCynUm5sG9muGJ3RXpziZgCgkpqjpWas/view?usp=sharing)
    - `mkdir -p data`
    - Extract the zip inside `data/`
    - Finally `data/dataset/` should contains just all the csv files.

- To preprocess the data either do:
  1. ```
     cd preprocessing
     chmod 700 *.sh
     bash preprocess.sh
     ```
     This can take around 10 minutes depending on your system architecture.

     OR

  2.
    - We have uploaded the preprocessed data to google drive, so you can download the preprocessed zip from [here](https://drive.google.com/file/d/1aCLOxUS2FRKzrbmMjrSeOsgrnJ1AAQH9/view?usp=sharing)
    - `mkdir -p data`
    - Extract the zip inside `data/`
    - Finally `data.json` should be present inside `data/` directory.

- After scraping and preprocessing, to get results from each of the analysis refer to READMEs of the corresponding analysis directories:
  - [Classfication](Classification)
  - [FAQ](FAQ)
  - [General Analysis](<General Analysis>)
  - [government scheme analysis](<government scheme analysis>)
  - [plant_protection_analysis](plant_protection_analysis)
  - [weather](weather)
