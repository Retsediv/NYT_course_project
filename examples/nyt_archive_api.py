from nytimesarchive import ArchiveAPI

api = ArchiveAPI('edfee37ae9e24f848d39bd3976afa7bd')

print(api.query(2016, 11))
