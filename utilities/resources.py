class ApiResources:
    apikey = 'd6fa171a71b818ffd0455d1c59b8c554'
    ts = '1668507926'
    hash = '0605d67484f892bc6f57b83297be12f5'

    getStories = f'/stories?limit=5&offset=100&apikey={apikey}&ts={ts}&hash={hash}'
    getCharatersOne = f'/characters/1011198?apikey={apikey}&ts={ts}&hash={hash}'
    getCharatersTwo = f'/characters/1011297?apikey={apikey}&ts={ts}&hash={hash}'
    getCharatersThree = f'/characters/1011456?apikey={apikey}&ts={ts}&hash={hash}'
    getCharatersNotFound = f'/characters/7748?apikey={apikey}&ts={ts}&hash={hash}'
