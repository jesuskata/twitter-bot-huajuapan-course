import twitter
# import os
from decouple import config

api_client = twitter.Api(
    consumer_key=config('CONSUMER_KEY'),
    consumer_secret=config('CONSUMER_SECRET'),
    access_token_key=config('ACCESS_TOKEN_KEY'),
    access_token_secret=config('ACCESS_TOKEN_SECRET')
)

result = api_client.PostUpdate(
    "I am trolling secretly the Galileo's account with decouple installed."
)
print(result)

# image_path = os.path.abspath('logos-for-linux.jpeg')

# result = api_client.PostUpdate(
#     "Learning #python with Galileo at #huajuapan",
#     media=image_path
# )

# print(result)
