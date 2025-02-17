# GA4 Properties configurator
## Purpose of this application
This Python application has been developed with the aim of dynamically configuring GA4 properties. 
It has been developed using Pycharm and is intended to be executed locally, directly from the code editor. 

At the time of creation of this repo, the code makes use of the Google Analytics Admin API Python client to dynamically 
configured and populate a given GA4 property's custom dimensions (event params, user properties and items). This is done
by means of accessing and leveraging a .csv file with these custom dimensions information with the Pandas Python library.
Authentication with the GA Admin API in Google Cloud is accomplished through a Service Account.

The dependencies of this Python application are listed in this repo's requirements.txt file. Following are the links to 
the used Python libraries :

[google-auth-oauthlib](https://pypi.org/project/google-auth-oauthlib/)

[google-analytics-admin](https://pypi.org/project/google-analytics-admin/)

[pandas](https://pypi.org/project/pandas/)

## Steps to implement this development
### Enable the Google Analytics Admin API and create a Service Account
Enable the [Google Analytics Admin API](https://developers.google.com/analytics/devguides/config/admin/v1?hl=es_419) in your Google Cloud Project. Create a Service Account within the
same project and set its permissions accordingly so that it can interact with the GA Admin API (Eg Editor role).
You will need to enable a JSON credential file within this Service Account and download it to keep it in a safe place.
Do not share these credentials.

Grant access to this Service Account to the GA4 property you wish to dynamically configure with and editor role.

### Install the Google Auth, GA Admin and pandas Python libraries
In order to dynamically configure a GA4 property through the Google Cloud GA Admin API, you 
first need to authenticate yourself with this API. There are several ways to do this and I have 
chosen to do it with a Service Account credential JSON file for this app. In order to do so, instalation 
of the google-auth-oauthlib package is necessary. This is done with the following command in your terminal: 

```
pip install google-auth-oauthlib
```
In order to install the google-analytics-admin Python package, execute the following command in your terminal:
```
google-analytics-admin
```
This app relies on a .csv file stored in the root folder. This .csv file contains the information of the GA4 custom
dimensions to be dynamically configured. In order to read this .csv file, the pandas library needs to be instaled. 
This can be done with the following command: 
```
pip install pandas
```
