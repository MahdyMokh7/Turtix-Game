class Tile :
    def __init__(self, a_inp) -> None:
        self.a = a_inp

    def get_attr(self):
        return self.a


class Map:
    def __init__(self) -> None:
        self.map_game = [[Tile(i * j) for i in range(5)] for j in range(10)]





for row in list_a:
    for col in row:
        print(col.get_attr(), end=' ')
    print()

