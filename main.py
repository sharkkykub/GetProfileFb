from time import time
from httpx import get

def get_profile(user_id: str):
    responseGetRedirect = get(f'https://graph.facebook.com/{user_id}/picture?height=500&access_token=6628568379%7Cc1e620fa708a1d5696fb991c1bde5662')
    responseProfile = get(responseGetRedirect.headers['location']).content
    open(f'{user_id}_{int(time())}.jpg', 'wb').write(responseProfile)
    print('Success')
    
def main():
    userId = input('USER_ID => ')
    get_profile(userId)

if (__name__ == "__main__"):
    main()