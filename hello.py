import pymongo

client = pymongo.MongoClient('localhost', 27017)
welden = client['weldan']
sheet_tab = welden['sheet_tab']

path = '/home/asule/文档/ASule.txt'
with open(path, 'r') as f:
    links = f.readlines()
    for index , line in enumerate(links):
        data = {
            'hello': index,
            'asule': line,
            'words' : len(line.split())
        }
        sheet_tab.insert_one(data)
