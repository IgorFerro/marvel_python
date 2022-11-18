class ApiResources:
    apikey = ''
    ts = ''
    hash = ''

    getStories = f'/stories?limit=5&offset=100&apikey={apikey}&ts={ts}&hash={hash}'
    getCharatersOne = f'/characters/1011198?apikey={apikey}&ts={ts}&hash={hash}'
    getCharatersTwo = f'/characters/1011297?apikey={apikey}&ts={ts}&hash={hash}'
    getCharatersThree = f'/characters/1011456?apikey={apikey}&ts={ts}&hash={hash}'
    getCharatersNotFound = f'/characters/7748?apikey={apikey}&ts={ts}&hash={hash}'
