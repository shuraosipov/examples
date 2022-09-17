## About
This example shows how to use the [Microsoft Graph API](https://docs.microsoft.com/en-us/graph/api/resources/azure-ad-overview?view=graph-rest-1.0) to [list all applications](https://learn.microsoft.com/en-us/graph/api/application-list?view=graph-rest-1.0&tabs=http) in the Azure AD which have redirectUris starting with a provided keyword.

## Prerequisites
Set `ConsistencyLevel` header to `eventual`

```
https://graph.microsoft.com/v1.0/applications?$filter=web/redirectUris/any(s,startswith(s,'https://myapp.com')&$count=true&$select=appId,displayName,web/redirectUris
```


## References
[Advanced query capabilities on Azure AD directory objects](https://learn.microsoft.com/en-us/graph/aad-advanced-queries?tabs=http)