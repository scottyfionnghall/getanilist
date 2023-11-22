import requests
import sys

print('Starting...')

query = '''
query ($userName: String) { # Define which variables will be used in the query (id)
  MediaListCollection(userName: $userName, type: MANGA, status: PLANNING, sort: MEDIA_TITLE_ROMAJI) {
    lists {
      name
      entries {
        mediaId
        media {
          title {
            romaji
          }
          status
        }
      }
    }
  }
}
'''

variables = {
    'userName': str(sys.argv[1]),
}


url = 'https://graphql.anilist.co'

response = requests.post(url, json={'query': query, 'variables': variables})
data = response.json()
with open('output.txt','w',encoding='utf-8') as f:
    for i in data["data"]["MediaListCollection"]["lists"]:
        for j in i["entries"]:
            if j["media"]["status"] == "FINISHED":
                for k,v in j["media"]["title"].items():
                    f.write(v+'\n')

print("Finished!")