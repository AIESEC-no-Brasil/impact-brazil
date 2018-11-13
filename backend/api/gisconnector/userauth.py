import json
from urllib.parse import unquote
from requests import session
from bs4 import BeautifulSoup
from . import config


# Logs into OP
# Returns: (Login_Successful?, Error or Access Token)
def yop_login(un, pw):
    # Create a session
    s = session()

    # Try to extract the authenticity token
    try:
        login_content = s.get(config.yop_login_url).content
        bs = BeautifulSoup(login_content, features="html.parser")
    except Exception as e:
        return False, str(e)

    authenticity_token = bs.find("input", {'name': "authenticity_token"})
    if authenticity_token is None:
        return False, "Authenticity token not found"

    authenticity_token = authenticity_token['value']

    # Post our payload
    payload = {
        'authenticity_token': authenticity_token,
        'user[email]': un,
        'user[password]': pw
    }

    s.post(config.yop_login_post_url, data=payload)

    # Get the access_token from the relevant cookie
    try:
        access_token = json.loads(unquote(s.cookies['aiesec_token']))
        access_token = access_token['token']['access_token']
    except Exception as e:
        return False, str(e)

    if access_token == "":
        return False, "Access token was blank"

    # Return the access_token
    return True, access_token