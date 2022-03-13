import requests, json

main = json.loads(open("process.json", "r").read())

print("This is not a valid avatar URL, changed to default avatar.") if not main['avatar_url'].startswith("https://") or not main['avatar_url'].startswith("http://") else None

data = {
  "username": main['username'],
  "avatar_url": main['avatar_url'],
  "content": main['content']
}
requests.post(main['url'], json=data)

print("Message Sent!")
