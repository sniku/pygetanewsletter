import xmlrpclib
import hashlib

class GAN(object):
    API_URL = 'http://admin.getanewsletter.com/api/v0.1/'

    def __init__(self, username, password):
        self.api = xmlrpclib.ServerProxy(self.API_URL)
        self.username = username
        self.password = password

    def list_supported_methods(self):
        '''
        This is helper function that prints all the methods supported by the API.
        '''
        print '#' * 60
        print 'Supported methods'

        for p in self.api.system.listMethods():
            print '\n\n'
            print '#' * 60
            print p
            print '#' * 60
            print self.api.system.methodHelp(p)

    def login(self):
        '''
        This is helper function that takes care of authentication.
        '''

        out = self.api.nonces.challenge(self.username)
        salt, nonce = out['salt'], out['nonce']

        hashed_password = salt + self.password
        hashed_password = hashlib.sha1(hashed_password).hexdigest()
        hashed_password = hashlib.md5(hashed_password + nonce).hexdigest()

        self.encrypted_password = hashed_password

        return self.api.nonces.verify(self.username, self.encrypted_password)

