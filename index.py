import bitly_api
api_user = "theutkarshjaiswal"
api_key = "R_3efc580d3cff4e048d700ffbaa26684e"
bitly = bitly_api.Connection(api_user, api_key)

response = bitly.shorten('http://google.com/')

# Now let us print the Bitly URL
print(response)
