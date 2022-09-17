import msal
import configparser
import requests



def get_token(settings):
    app = msal.ConfidentialClientApplication(
        azure_settings['client_id'],
        authority=(f"https://login.microsoftonline.com/{azure_settings['tenant_id']}/"),
        client_credential=azure_settings['client_secret'],
    )

    token = None
    token = app.acquire_token_for_client(scopes=[azure_settings['scope']])

    if "access_token" in token:
        #`print(token["access_token"])
        return token["access_token"]
    else:
        print(token.get("error"))
        print(token.get("error_description"))
        print(token.get("correlation_id"))  # You may need this when reporting a bug
        raise Exception("Failed to acquire token")
    

def list_applications(access_token, service_url):
    headers = {'Authorization': 'Bearer ' + access_token, 'ConsistencyLevel': 'eventual'}
    # url = f"https://graph.microsoft.com/v1.0/applications?$filter=web/redirectUris/any(s,startswith(s,'{service_url}')&$count=true&$select=appId,displayName"
    url = f"https://graph.microsoft.com/v1.0/applications"
    response = requests.get(url, headers=headers)
    print(response.text)

if __name__ == "__main__":
    # Load settings
    config = configparser.ConfigParser()
    config.read(['config.cfg', 'config.dev.cfg'])
    azure_settings = config['azure']

    token = get_token(azure_settings)
    list_applications(token, service_url="https://myapp.com")




    

