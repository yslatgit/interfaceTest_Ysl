import yaml
import os

# PATH = os.path.split(os.path.realpath("_file_"))[0]
# configPath = os.path.join(PATH, "config.yaml")

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))

class ReadConfig:

    def __init__(self,key):
        self.key = key
        self.configPath = PATH("config.yaml")
        # print(self.configPath)

    def readconfig(self):
        with open(self.configPath,'r') as f:
            r = yaml.load(f.read())
        return r[self.key]

# print(readconfig("EMAIL"))
if __name__ == '__main__':
    
    r = ReadConfig("EMAIL")
    print(r.readconfig())