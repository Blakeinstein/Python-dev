from sudoku import Sudoku
import pygame
class App:
    def __init__(self, board):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 628, 628
        self.node = [0, 0]
        self.board = board
        self.selected = [-1, -1]
        self.input_mode = True
        self.font = None
        self.keydict = {
            pygame.K_0: 0,
            pygame.K_1: 1,
            pygame.K_2: 2,
            pygame.K_3: 3,
            pygame.K_4: 4,
            pygame.K_5: 5,
            pygame.K_6: 6,
            pygame.K_7: 7,
            pygame.K_8: 8,
            pygame.K_9: 9,
            pygame.K_KP0: 0,
            pygame.K_KP1: 1,
            pygame.K_KP2: 2,
            pygame.K_KP3: 3,
            pygame.K_KP4: 4,
            pygame.K_KP5: 5,
            pygame.K_KP6: 6,
            pygame.K_KP7: 7,
            pygame.K_KP8: 8,
            pygame.K_KP9: 9
        }
    def on_start(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.font = pygame.font.Font(pygame.font.match_font('aerial'), 40)
        icon = pygame.image.load("assets/sudoku.png")
        #by https://www.flaticon.com/authors/surang
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Sudoku Solver")
        return True
    def set_select_hover(self, screen):
        width, height = pygame.mouse.get_pos()
        rect = pygame.Rect(width - width%70, height - height%70, 70, 70)
        pygame.draw.rect(screen, (100, 100, 100), rect)
        rect = pygame.Rect(width - width%70 + 2, height - height%70 + 2, 64, 64)
        pygame.draw.rect(screen, (255, 255, 255), rect)
        return screen
    def set_select(self, event):
        col, row = event.pos
        col = col//70
        row = row //70
        if self.selected == [col, row]:
            self.selected = [-1, -1]
        else:
            self.selected = [col, row]
    def draw_select(self, screen):
        width = self.selected[0]*70
        height = self.selected[1]*70
        rect = pygame.Rect(width, height, 70, 70)
        pygame.draw.rect(screen, (30, 30, 30), rect)
        rect = pygame.Rect(width + 2, height  + 2, 64, 64)
        pygame.draw.rect(screen, (255, 255, 255), rect)
    def input(self, event):
        if event.key == pygame.K_SPACE:
            self.input_mode = False
            self.step_solve()
        elif event.key in self.keydict:
            if not self.selected == [-1,-1]:
                self.board.arr[self.selected[1]][self.selected[0]] = self.keydict[event.key]
        elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
            self.input_mode = False
            self.board.solve()
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            self.input(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.set_select(event)
            self.on_render()
    def on_render(self):
        screen = pygame.display.get_surface()
        screen.fill((0, 0, 0))
        for height in range(9):
            for width in range(9):
                rect = pygame.Rect(width*70, height*70, 68, 68)
                pygame.draw.rect(screen, (255, 255, 255), rect)
        if self.input_mode:
            self.set_select_hover(screen)
            self.draw_select(screen)
        for height in range(9):
            for width in range(9):
                if not self.board.arr[height][width] == 0:
                    value = self.font.render(str(self.board.arr[height][width]), True, (0, 0, 0))
                    valrect = value.get_rect()
                    valrect.center = (width*70 + 34, height*70 + 34)
                    screen.blit(value, valrect)
        pygame.display.flip()
        return screen
    def step_solve(self):
        self.board.node = [0, 0]
        if not self.board.find():
            return True
        row = self.board.node[0]
        col = self.board.node[1]
        for num in range(0, 10):
            if self.board.check(row, col, num):
                self.board.arr[row][col] = num
                self.on_render()
                pygame.time.delay(100)
                if self.step_solve():
                    return True
                self.board.arr[row][col] = 0
        return False
    def on_execute(self):
        if not self.on_start():
            self._running = False
        while self._running:
            screen = self.on_render()
            self.set_select_hover(screen)
            for event in pygame.event.get():
                self.on_event(event)
            pygame.time.delay(100)
        pygame.quit()
if __name__ == "__main__":
    BOARD = Sudoku([
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]
    ])
    """easy[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]hard[
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]
    ]"""
    GAME = App(BOARD)
    GAME.on_execute()
