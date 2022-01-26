# Python Stock Analyzer with MongoDB

[![Git](https://app.soluble.cloud/api/v1/public/badges/33d565d4-196d-435f-9861-4b6d7fe2a495.svg?orgId=650162616495)](https://app.soluble.cloud/repos/details/github.com/james-leha/stockanalysiswithalphavantage?orgId=650162616495)  

*Python solution using the Alpha Vantage free stock API and Azure Cosmos MongoDB API for data storage*

Alpha Vantage delivers a free API for real time financial data and most used finance indicators in a simple json or pandas format. This module implements a python interface to the free API provided by Alpha
Vantage (http://www.alphavantage.co/). It requires a free API key, that can be requested on http://www.alphavantage.co/support/#api-key. You can have a look at all the API calls available in their documentation http://www.alphavantage.co/documentation

The Alpha Vantage Python wrapper module is has been leverage to simplify the querying process. The module repo located here: https://github.com/RomelTorres/alpha_vantage 

The Azure Cosmos DB service implements wire protocols for common NoSQL APIs including Cassandra, MongoDB, Gremlin, and Azure Table Storage. This allows you to use your familiar NoSQL client drivers and tools to interact with your Cosmos database. If you wish to store Alpha Vantage API results in a databse, obtain a connection string for you Azure Cosmos DB or equivalent database service. More information on Azure Cosmos DB: https://docs.microsoft.com/en-us/azure/cosmos-db/mongodb-introduction

## News

* As of 3/29/20, this is still a proof of concept solution that can return stock results, store the results for a user in a MongoDB, and query that MongoDB for analysis work in Python.

## Pre-Requisites

* An Alpha Vantage API Key, there is a FREE version of the API Key you can obtain from: https://www.alphavantage.co/
* A noSQL database connection string, the current version is using a MongoDB to Insert, Update, and Query data. Some functionality can be utilized without a database, however.
* Using the dotenv package to store our environmental variables in a secure manner. You'll want to create a .env file to store your relevant API Key, connection strings, etc. Documentation available here: https://pypi.org/project/python-dotenv/
* Python 3.8.1 is the latest version this application is developed on
* Pip Modules, outlined in Install section

## Install
To install the Alpha Vantage package use:
```shell
pip install alpha_vantage
```
Or install with pandas support, simply install pandas too:
```shell
pip install alpha_vantage pandas
```
To install the dotnev package use:
```shell
pip install -U python-dotenv
```
To install the azure cosmos package use:
```shell
pip install azure-cosmos
```
To install the pymongo package use:
```shell
pip install pymongo
```

## Setup
View the Environment_Settings folder, you will find a *.env_sample* file. 
```shell
API_KEY=YOUR_API_KEY_HERE
DB_CONNECTION_STRING=your_connectionstring://value_here
```
For the *settings.py* file in this folder to work and create a global variable for usage, copy the content from the *.env_sample* file into a *.env* file (this is the file name the dotenv module searches for). Input your API_KEY and DB_CONNECTION_STRING values into this file.

## Alpha Vantage Python Wrapper
To utilize the base modules provided from the Alpha Vantage python wrapper modules, use the files in the AlphaVantageMethods folder.

Each of these scripts will use the settings.API_KEY value you updated in the Setup section, run an Alpha Vantage API method, and populate the results returned into a plot or dataframe.

More detailed explanation can be viewed: https://github.com/RomelTorres/alpha_vantage/blob/develop/README.md

This is meant for quick reference while developing further features of the application

## Usage - Retrieve Dailies Results
The *TimeSeries_RetrieveDailies_InsertToDB.py* file is utilizing the Alpha Vantage and Azure Cosmos modules to return Time Series 
results and upload to your Azure Cosmos DB service.

Modify the following variable to adjust how many days of data you want returned:

```python
#Number of rows(time frame) you want returned from the query
rowsOfData = 1
```

This script will return stock results for the specified stock symbol and timeframe. The results are converted to a dictionary and will be iterated through to add relevant fields (symbol, username, date, percentages, etc.)

The following will insert the dictionary objects into your Azure Cosmos DB (comment these two lines if you have not setup a connection to an Azure Cosmos DB):

```python
AzCosmos = AzureCosmoDB_Insert.AzureCosmosCRUD(ts_DictDataConverted)
AzCosmos.insertDataToMongo()
```

## TODOs:
* Update the database when the user makes a stock result request that creates duplicate data
* Add further processing of stock results for trend analysis and recommendation
* Add unit tests to implement TDD
