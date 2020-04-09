import random
class Router(object):
    def db_for_read(self,model,**hints):
       return "salve"

  # return random.choice(['slave','slave1'])

    def db_for_write(self,model,**hints):
        return "default"
    # return random.choice(['default','master'])