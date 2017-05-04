#
#   Packt user abstraction.
#

from bs4 import BeautifulSoup
import requests

# Base Packt website url
PACKT_URL = "https://www.packtpub.com"


class User:

    def __init__(self):
        # TODO: add initial data configurations (requests session, session headers, ...)
        pass

    def login(self, email, password):
        # TODO: perform user login. Return a boolean which specifies if the login was successful or not.
        pass

    def find_free_ebook(self):
        # TODO: find the free ebook url. Return it if found, else return None.
        pass

    def take_free_ebook(self, ebook_url):
        # TODO: take the free ebook. Return a boolean which specifies if the ebook was taken or not.
        pass

    def get_user_ebooks(self):
        # TODO: inspect the user library and return the ebooks that the user owns in an array. If no ebook was found,
        # return an empty array.

        # Array structure:
        #
        # [
        #   {
        #     id: <ebook_id>,
        #     title: <ebook_title>,
        #     links:
        #       [
        #         {
        #           url: <ebook_download_url>,
        #           type: <ebook_download_url_type>
        #         },
        #         ...
        #       ]
        #   },
        #   ...
        # ]

        pass

    def get_ebook_download_url(self, url):
        # TODO: return the real download url (from the storage server). Return None if the url could not be retrieved.
        pass
