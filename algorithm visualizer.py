import random
import pygame

pygame.init()

class DrawInformation:
    black = 0,0,0
    white = 255,255,255
    green = 0,255,255
    red = 255,0,0
    grey = 128,128,128
    bg_color = white

    gradients = [
        grey,
        (160,160,160),
        (192,192,192)
    ]
    font = pygame.font.SysFont('comicsans',30)
    largefont = pygame.font.SysFont('comicsans',40)

    sidepad = 100 #empty spaces in the corners
    toppad = 150

    def __init__(self, width,height,lst): #will take in width,height, list
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    def set_list(self,lst):
        self.lst = lst
        self.max_val = max(lst)
        self.min_val = min(lst)

        self.block_width = round((self.width - self.sidepad)/len(lst))
        self.block_height = round((self.height - self.toppad) / (self.max_val - self.min_val))

        self.start_x = self.sidepad // 2

def draw(draw_info):
    draw_info.window.fill(draw_info.bg_color)

    controls = draw_info.font.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1,draw_info.black)
    draw_info.window.blit(controls,(draw_info.width/2 - controls.get_width()/2,5))

    sorting = draw_info.font.render("I - Insertion Sort | B - Bubble Sort", 1, draw_info.black)
    draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 35))

    draw_list(draw_info)
    pygame.display.update()

def draw_list(draw_info):
    lst = draw_info.lst

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color = draw_info.gradients[i % 3]

        pygame.draw.rect(draw_info.window,color,(x,y,draw_info.block_width,draw_info.block_height))



def generate_starting_list(n,min_val,max_val):
    lst = []
    for _ in range(n):
        val = random.randint(min_val,max_val)
        lst.append(val)

    return lst

def bubble_sort(draw_info,ascending = True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if num1 > num2 and ascending or (num1 < num2 and not ascending):
                lst[j], lst[j+1] = lst[j + 1], lst[j]
                draw_list(draw_info, {j: draw_info.green, j + 1: draw_info.red}, True)
                yield True
    return lst

def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    lst = generate_starting_list(n,min_val,max_val)
    draw_info = DrawInformation(1000,600,lst)
    sorting = False
    ascending = True

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = generate_starting_list(n,min_val,max_val)
                draw_info.set_list(lst)
                sorting = False

            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True

            elif event.key == pygame.K_q and not sorting:
                ascending = True

            elif event.key == pygame.K_d and not sorting:
                ascending = False

    pygame.quit()

if __name__ == "__main__":
    main()


#45:29