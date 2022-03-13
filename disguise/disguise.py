import requests, json

main = json.loads(open("process.json", "r").read())


try:
    condition = main['avatar_url'].startswith('https://') or main['avatar_url'].startswith('http://')
except AttributeError:
    condition = True

i = "This is not a valid avatar URL, changed to default avatar." if condition == True else ""
print(i)

if condition:
    main['avatar_url'] = ''

data = {
  "username": main['username'],
  "avatar_url": main['avatar_url'],
  "content": main['content']
}

try:
    r = requests.post(main['url'], json=data)
    r.raise_for_status()
    print("Message Sent!")
except Exception as error:
    print("Error: " + str(error))
