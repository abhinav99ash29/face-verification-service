from tinydb import TinyDB, Query

db = TinyDB('db.json')
item = Query()


def write(identityId, encoding):
    results = db.search(item.identityId == identityId)
    if len(results) == 0:
        data = {"identityId": identityId, "encoding": encoding}
        db.insert(data)
        return True
    else:
        db.update({"encoding": encoding}, item.identityId == identityId)
        return True

def search(identityId):
    results = db.search(item.identityId == identityId)
    knownEnc = []
    for result in results:
        knownEnc.append(result['encoding'])

    return knownEnc