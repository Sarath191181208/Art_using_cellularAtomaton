import pygame
import random 
import numpy as np
from threading import Thread
from numba import njit
from colors import *

# profiling tools

import cProfile
import pstats

pygame.init()
clock = pygame.time.Clock()
WIN = pygame.display.set_mode((500, 500))
pygame.display.set_caption('')
FPS = 60
def PYtxt(txt: str, fontSize: int = 28, font: str = 'freesansbold.ttf', fontColour: tuple = (0, 0, 0)):
    return (pygame.font.Font(font, fontSize)).render(txt, True, fontColour)

WHITE = (215, 215, 215)
GREAY = (70, 70, 70)
BLACK = (0, 0, 0)
BLUE = (10, 40, 100)
checksClr = BLUE
boardClr = WHITE
txtClr = GREAY

class Grid():
    def __init__(self, cols: int = 4, rows: int = 4, width: int = 400, height: int = 400,WIN = None):
        self.rows = cols
        self.cols = rows
        self.cubes = [
            [Cube(0, i, j, width, height, self.cols, self.rows,WIN)
             for j in range(self.cols)]
            for i in range(self.rows)
        ]
        self.width = width
        self.height = height
        self.win = WIN

        self.previous = []
        self.matrix = []

        self.n = 14 
        self.colors = []
        for _ in range(self.n):
            self.colors.append(Color(random.randint(0,255), random.randint(0,255), random.randint(0,255)));


    def draw(self):

        for row_mat,row_cubes in zip(self.matrix,self.cubes):
            for val,cube in zip(row_mat,row_cubes):
                cube.change_color(self.colors[val])
                cube.draw()

        # self.draw_grid()

    def draw_grid(self):
        rowGap = self.height / self.rows
        colGap = self.width / self.cols

        thick = 1
        # pygame.draw.line(win, (0, 0, 0), (i * rowGap, 0),i * rowGap, self.height), thick)
        for i in range(self.rows+1):
            pygame.draw.line(self.win, BLACK, (0, i*rowGap),(self.height, rowGap*i), thick)
        for i in range(self.cols+1):
            pygame.draw.line(self.win, BLACK, (i*colGap, 0), (colGap*i, self.width))
        
    def iter(self):
        for row in self.cubes:
            helper_row = []   
            for cube in row:
                cube.val = random.randint(0,self.n-1)
                cube.change_color(self.colors[cube.val])
                helper_row.append(cube.val)
            self.matrix.append(helper_row)
        self.matrix = np.array(self.matrix, dtype=np.int8)
        self.draw()
    
    def clicked(self):
        pass

    def update(self):
        self.matrix = create(self.matrix, self.rows, self.cols, self.n)
        self.draw()

@njit
def create(mat, rows, cols, n):
    tmp_matrix = mat.copy()

    for i in range(rows -1):
        for j in range(cols -1):

            nxt_val = (mat[i][j] + 1)% n 

            if ( nxt_val == mat[i][(j+1)%(cols)]
            or  nxt_val == mat[(i+1)%(rows)][j]    
            or  nxt_val == mat[(i-1+rows)%(rows)][j] 
            or  nxt_val == mat[i][((j-1)+(rows)%(rows))] ):
                tmp_matrix[i][j] = nxt_val

    return(tmp_matrix.copy())
class Cube():
    def __init__(self, value, row, col, width, height, cols, rows,win):
        self.val = value

        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.cols = cols
        self.rows = rows
        self.centerFactor = 10
        self.win = win

        self.color = WHITE

    def draw(self):
        rowGap = self.height / self.rows
        colGap = self.width / self.cols
        x = self.col * colGap
        y = self.row * rowGap
        pygame.draw.rect(self.win, self.color, pygame.Rect(x, y, colGap, rowGap))
    
    def update(self):
        self.draw()

    def change_color(self,color):
        self.color = color

def main():
    run = True

    rows = 50

    board = Grid(cols=rows, rows=rows, width=500, height=500, WIN= WIN)
    board.iter()

    # while run:
    for _ in range(1000):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(WHITE)

        t = Thread(target= board.update(), args=(10,))
        t.start()
        # t.join()

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':

    with cProfile.Profile() as pr:
        main()
    
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats() 
    stats.dump_stats(filename='profile.prof')