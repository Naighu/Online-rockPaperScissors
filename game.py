
class Game:
    def __init__(self,id):
        self.id = id
        self.p1Went = False
        self.p2Went = False
        self.picked = []
        self.ready = False
        self.quit = False
    def connected(self):
        return self.ready
    def reset(self):
        self.p1Went = False
        self.p2Went = False
        print("reseted")
        try:
            self.picked.clear()
        except:
            pass
    def play(self,player,move):
        if player == 0:
            self.p1Went = True
            self.picked.insert(0,move)
        else:
            self.picked.insert(1,move)
            self.p2Went = True
    def winner(self):
        p1 = self.picked[0][0].upper()
        p2 = self.picked[1][0].upper()
        if p1 == 'R' and p2 == 'S':
            winner = 0
        elif p1 == 'R' and p2 == 'P':
            winner = 1
        elif p1 == p2:
            winner = -1
        elif p1 == 'P' and p2 == 'S':
            winner = 1
        elif p1 == 'P' and p2 == 'R':
            winner = 0
        elif p1 == 'S' and p2 == 'P':
            winner = 0
        elif p1 == 'S' and p2 == 'R':
            winner = 1
        return winner

    