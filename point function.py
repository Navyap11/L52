class pointeyy:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    
position1= pointeyy(2,3)
print(position1)