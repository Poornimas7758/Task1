import bitly_api

Access_Token= '5ec198c238de85906c57a962e548dfb804159eea'

connection=bitly_api.Connection(access_token=Access_Token)

url=input("Enter the long url:   ")

short_url = connection.shorten(url)

print('short url is  ',short_url['url'])