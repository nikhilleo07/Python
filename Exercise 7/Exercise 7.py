class luffyclass():
    def __init__(self,anime):
        print("Executing luffyclass constructor")
        self.message=anime
    def animename(self):
        print(self.message)
luffy=luffyclass("One Piece")
luffy.animename()
print(type(luffy))