## About
This example shows how to use the [Microsoft Graph API](https://docs.microsoft.com/en-us/graph/api/resources/azure-ad-overview?view=graph-rest-1.0) to [list all applications](https://learn.microsoft.com/en-us/graph/api/application-list?view=graph-rest-1.0&tabs=http) in the Azure AD which have redirectUris starting with a provided keyword.

The original idea is to match a service URL (for example https://myapp.com) to the client_id of the application registered in Azure by examining the redirectUris of the application.

## Prerequisites
Update config.cfg with your Azure AD tenant ID, client ID, client secret and scope.
```
[azure]
client_id = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
client_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
tenant_id = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
application_id = https://graph.microsoft.com
scope = https://graph.microsoft.com/.default
```

Install the required packages:
```
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

# Usage
We will be using the following URL to filter the applications. 

```
https://graph.microsoft.com/v1.0/applications?$filter=web/redirectUris/any(s:startsWith(s,+'https://myapp.com'))&$count=true&$select=appId,displayName
```

Run script.py and provide the URL to filter the applications.
```
python script.py https://myapp.com

Output:
App ID: ed4exxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
Display Name: my-test-app
```

## Findings
- This query could return multiple applications with the same redirectUri.
- Some apps use different redirectUris than the service URL, so the query could return no results.

## References
- [Advanced query capabilities on Azure AD directory objects](https://learn.microsoft.com/en-us/graph/aad-advanced-queries?tabs=http)
- https://github.com/microsoftgraph/msgraph-sdk-python-core
- https://learn.microsoft.com/en-us/graph/tutorials/python?tabs=aad&tutorial-step=3
