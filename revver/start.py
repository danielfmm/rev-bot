from revver import revbot
from revver import config as c


def run():
    if c.price_limit == 0.0:
        revbot.express()
    else:
        revbot.main()



