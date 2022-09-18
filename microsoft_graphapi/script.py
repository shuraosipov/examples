import configparser
import argparse
from azure.identity import ClientSecretCredential
from msgraph.core import GraphClient


def filter_apps_by_web_redirect_uri(app_client, service_url, selected_properties):
    result = app_client.get(
        '/applications',
        params={
            '$filter': f"web/redirectUris/any(s:startsWith(s, \'{service_url}\'))",
            '$count': 'true',
            '$select': ",".join(selected_properties)
        },
        headers={
            'ConsistencyLevel': 'eventual'
        }
    )
    return result.json()


def pretty_print_apps(apps):
    for app in apps['value']:
        print(f"App ID: {app['appId']}")
        print(f"Display Name: {app['displayName']}")
        print("")

    


if __name__ == "__main__":
    # Load settings
    config = configparser.ConfigParser()
    config.read(['config.cfg', 'config.dev.cfg'])
    azure_settings = config['azure']

    credential = ClientSecretCredential(
        tenant_id=azure_settings['tenant_id'],
        client_id=azure_settings['client_id'],
        client_secret=azure_settings['client_secret'],
    )

    # argparser for service url
    parser = argparse.ArgumentParser()
    parser.add_argument("service_url", help="The service url to filter applications by")
    args = parser.parse_args()
    service_url = args.service_url

    app_client = GraphClient(credential=credential,scopes=[azure_settings['scope']])
    result = filter_apps_by_web_redirect_uri(app_client, service_url, selected_properties=['appId', 'displayName'])
    pretty_print_apps(result)
