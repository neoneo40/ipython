import requests
res = requests.get('https://automatetheboringstuff.com/files/RomeoAndJuliet.txt')

res.raise_for_status()

playFile = open('src/RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()