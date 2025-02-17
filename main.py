from google.oauth2 import service_account
from google.analytics import admin_v1beta
import pandas

#Manage API credentials
SERVICE_ACCOUNT_FILE = ''
GA4_ADMIN_API_SCOPE = ['https://www.googleapis.com/auth/analytics.edit']
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,scopes=GA4_ADMIN_API_SCOPE)
print(credentials)
# Create a client
client = admin_v1beta.AnalyticsAdminServiceClient(credentials=credentials)
print(client)

#GA4 property info
PARENT = 'properties/475522842'

#Generate custom dimension lists from csv
data = pandas.read_csv('custom_dimensions_definition.csv')
custom_dimension_names = data["custom_dimension_name"].tolist()
custom_dimension_scopes = data["custom_dimension_scope"].tolist()
custom_dimension_descriptions = data["custom_dimension_description"].tolist()

#Iterate over these lists and...
for i in range(len(custom_dimension_names)):
    #...create custom dimension
    custom_dimension = admin_v1beta.CustomDimension()
    custom_dimension.parameter_name = custom_dimension_names[i]
    custom_dimension.display_name = custom_dimension_names[i]
    custom_dimension.scope = custom_dimension_scopes[i]
    custom_dimension.description = custom_dimension_descriptions[i]

    #...create custom dimension request
    request = admin_v1beta.CreateCustomDimensionRequest({
        "parent": PARENT,
        "custom_dimension": custom_dimension,
    })


    #...launch request
    try:
        response = client.create_custom_dimension(request=request,timeout=5)
        print(response.name)
    except Exception as e:
        print(f"There has been the following error: {e}")
