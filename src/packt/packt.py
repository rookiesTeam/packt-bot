#
#   Packt user abstraction.
#

from bs4 import BeautifulSoup
import requests

# Base Packt website url
PACKT_URL = "https://www.packtpub.com"
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'}
PAYLOAD = {'email':'','form_id':'packt_user_login_form','password':''}


class User:

    def __init__(self):
        # TODO: add initial data configurations (requests session, session headers, ...)
        pass

    def login(self, email, password):
        # TODO: perform user login. Return a boolean which specifies if the login was successful or not.
        pass

    def find_free_ebook(self):
        #find the free ebook url. Return it if found, else return None.
        
        link_to_free = PACKT_URL+'/packt/offers/free-learning'
        req = requests.get(link_to_free, headers=headers)
        soup = BeautifulSoup(req.text,'html.parser')
        link = soup.find("a", class_="twelve-days-claim").get('href')

        return link

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
