from os import environ

authenticate[environ.get('TARGET_WIKI_HOSTNAME')] = (
    environ.get('TARGET_WIKI_CONSUMER_TOKEN'),
    environ.get('TARGET_WIKI_CONSUMER_SECRET'),
    environ.get('TARGET_WIKI_ACCESS_TOKEN'),
    environ.get('TARGET_WIKI_ACCESS_SECRET'),
)
