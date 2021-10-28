import configparser

config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        URL=config.get('common info','baseURL')
        return  URL
    @staticmethod
    def getUserEmail():
        userName=config.get('common info','username')
        return userName
    @staticmethod
    def getPassword():
        pwd=config.get('common info','password')
        return pwd