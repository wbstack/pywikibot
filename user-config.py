from os import environ

if environ.get('TARGET_WIKI_USERNAME'):
    authenticate[environ.get('TARGET_WIKI_HOSTNAME')] = (
        environ.get('TARGET_WIKI_CONSUMER_TOKEN'),
        environ.get('TARGET_WIKI_CONSUMER_SECRET'),
        environ.get('TARGET_WIKI_ACCESS_TOKEN'),
        environ.get('TARGET_WIKI_ACCESS_SECRET'),
    )
    usernames['target']['en'] = environ.get('TARGET_WIKI_USERNAME')

if environ.get('SOURCE_WIKI_USERNAME'):
    authenticate[environ.get('SOURCE_WIKI_HOSTNAME')] = (
        environ.get('SOURCE_WIKI_CONSUMER_TOKEN'),
        environ.get('SOURCE_WIKI_CONSUMER_SECRET'),
        environ.get('SOURCE_WIKI_ACCESS_TOKEN'),
        environ.get('SOURCE_WIKI_ACCESS_SECRET'),
    )
    usernames['source']['en'] = environ.get('SOURCE_WIKI_USERNAME')
