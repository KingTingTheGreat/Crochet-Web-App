class Yarn:
    #maybe add an attribute for gauge/how many oz in one sc and chain stitch
    def __init__(self, hex:str, name:str, weight:int, gauge:float):
        self.hex:str = hex
        self.name:str = name
        self.weight:int = weight
        #stitches per inch
        self.gauge:float = gauge
    
YARN_COLORS= [Yarn('#ffffff','White',4,3),
              Yarn('#ffafc7','Pink',4,3),
              Yarn('#73d7ee','BabyBlue',4,3),
              Yarn('#613915','Brown',4,3),
              Yarn('#000000','Black',4,3),
              Yarn('#e50000','Red',4,3),
              Yarn('#ff8d00','Orange',4,3),
              Yarn('#ffee00','Yellow',4,3),
              Yarn('#028121','Green',4,3),
              Yarn('#004cff','Blue',4,3),
              Yarn('#760088','Purple',4,3)]