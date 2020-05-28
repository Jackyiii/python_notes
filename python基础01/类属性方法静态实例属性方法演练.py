class Game:
    topScore = 0

    def __init__(self, playerName):
        self.playerName = playerName

    @staticmethod
    def showHelp():
        print("显示游戏帮助信息")

    @classmethod
    def showTopScore(cls):
        print("历史最高得分是%s" % (cls.topScore))

    def startGame(self):
        print("%s玩家开始了游戏" % self.playerName)

player1=Game("狒狒")
Game.showHelp()
Game.showTopScore()
player1.startGame()