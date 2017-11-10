class GoldRoom(object):
    def _init(self):
        self.name = "Gold Room"
        self.size = 100
        self.reward = ''

    def prologue(self):
        print "Welcome you to Gold Room!"
        print "You are the first man to come here, and you are so lucky!"
        print "I will give you something for rewarding you."
        print "Please input what you want."

    def dialogue(self):
        if self.reward.upper() == "DOLLAR":
            print "You should know I only have gold, and do you want some gold?"
            self.reward = raw_input(">")
            if self.reward.upper() == "YES" or "Y":
                print "Fool man, you are so greedy that I will give you no gold!"
            elif self.reward.upper() == "NO" or "N":
                print "You are a nice man, and I will give you many gold."
            else:
                print "Pardon? Can you speak once more?"
                self.reward = raw_input(">")
        else:
            pass

    def startGame(self):
        self.prologue()
        self.reward = raw_input(">")
        self.dialogue()



