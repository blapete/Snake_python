class GameConfig():
    FPS = 8
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    CELLSIZE = 20
    assert WINDOW_WIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
    assert WINDOW_HEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
    CELLWIDTH = int(WINDOW_WIDTH / CELLSIZE)
    CELLHEIGHT = int(WINDOW_HEIGHT / CELLSIZE)

    
    # window dimension = 640 x 480
    # if cell size = 20 ...
    # cell count = 32 x 24


    # game colors
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    DARKGREEN = (0,155,0)
    DARKGRAY = (40,40,40)
    BG_COLOR = BLACK