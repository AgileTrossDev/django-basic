from envparse import env
from dotenv import load_dotenv


# Loads OAUTH support in dev environments.
if env('CLIENT_ID', None) is None:
    load_dotenv()
    load_dotenv(env('CLIENT_LOCATION'))


def service_url(name, api, diet):
    return "service://{}/{}/{}".format(name, api, diet)


MY_SERVICE_URL = service_url("PULL_APP_NAME_FROM_ENV",
                             "PULL API VERSION FROM ENV",
                             "PULL environment")