from os import environ

from pywikibot import family

class Family(family.WikibaseFamily):
    name = 'target'

    langs = {
        'en': None,
    }

    def hostname(self, code):
        return environ.get('TARGET_WIKI_HOSTNAME')

    def protocol(self, code):
        return environ.get('TARGET_WIKI_PROTOCOL', 'HTTPS')
