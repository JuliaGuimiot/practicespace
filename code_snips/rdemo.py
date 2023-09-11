import requests

# payload = {'username': 'julia', 'password': 'testing'}
# r = requests.post('https://httpbin.org/post', data=payload)
# r_dict = r.json()
# print(r_dict['form'])

payload = {'username': 'julia', 'password': 'testing'}
r = requests.put('https://httpbin.org/put', data=payload)
r_dict = r.json()
print(r_dict['form'])

# with open('comic.png', 'wb') as f:
#     f.write(r.content)
# print(r.text)
# print(r.status_code)
# print(r.ok)
# print(r.headers)

https://api.nasa.gov/planetary/apod?api_key=fk2YV5AGTMCgI8eI5xa7MWOOytzKuF55bZOOcV04
