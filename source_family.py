from os import environ

from pywikibot import family

class Family(family.Family):
    name = 'source'

    langs = {
        'en': None,
    }

    def hostname(self, code):
        return environ.get('SOURCE_WIKI_HOSTNAME')
