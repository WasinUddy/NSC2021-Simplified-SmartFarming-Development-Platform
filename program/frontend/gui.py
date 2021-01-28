# Graphic User Interface of program
from frontend.Page import *
import sys


# quit pygame
def Quit():
    pg.quit()
    sys.exit()


# object for all gui
class Gui:
    # initalizing the program
    def __init__(self):
        # check if running
        self.running = True
        # menu page check
        self.MENU = True
        # normal advance tutorial
        self.NORMAL = False
        self.ADVANCE = False
        self.TUTORIAL = False

        self.width, self.height = WIDTH, HEIGHT
        # self.surface = pg.display.set_mode((self.width, self.height), pg.RESIZABLE)
        self.surface = pg.display.set_mode((self.width, self.height))
        pg.display.set_icon(ICON)
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font(FONTNAME)
        self.held = False
        self.clicked = False
        self.click = None
        self.loaddata()

    # loaddata
    def loaddata(self):
        self.logo = pg.transform.scale(LOGO, (240, 240))
        self.Normal_page = Normal(self.surface)
        self.Advance_page = Advance(self.surface)
        self.Tutorial_page = Tutorial(self.surface)
        self.buttons = []
        self.choices = []
        self.tables = []
        self.amounts = []
        self.insert = []
        self.result = ''
        self.cursor_current_position = None



    # create graphic user interface
    def run(self):
        # run
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    # update current status of the program
    def update(self):
        # display fps
        pg.display.set_caption(TITLE + " fps:{: .2f}".format(self.clock.get_fps()))

        # calling Advance class in Page.py
        self.Advance_page.update(self.clicked, self.cursor_current_position, self.width, self.height)
        # set what need to be done in to these variable (type is list) for input of method in def run
        self.buttons = self.Advance_page.button
        self.choices = self.Advance_page.choice
        self.tables = self.Advance_page.tables
        self.amounts = self.Advance_page.amount
        self.insert = self.Advance_page.text

        # scanning which button that cursor are hovering on
        for button in self.buttons:
            button.isOver(self.cursor_current_position)

        # if the page have dropdown menu
        if self.choices is not None:

            # update avaliable choice in dropdown menu
            for choice in self.choices:
                choice.update(self.clicked, self.cursor_current_position)
                # result after update to be shown in dropdown menu
                self.result = str(choice.default)

        # update amount and insert
        if self.amounts is not None or self.insert is not None:
            for amount_and_insert in self.amounts + self.insert:
                amount_and_insert.update()

    # Draw required elements on screen
    def draw(self):

        # draw background color
        self.surface.fill(bgcolor)

        self.Advance_page.draw(self.drawtext, self.cursor_current_position)

        # draw all button
        for button in self.buttons:
            button.draw(self.clicked)

        # draw dropdown menu
        

        # draw all amount
        if self.amounts is not None:
            for amount_and_insert in self.amounts + self.insert:
                amount_and_insert.draw(self.surface)

        # draw all table
        if self.tables is not None:
            for table in self.tables:
                table.draw()

        if self.choices is not None:
            for choice in self.choices:
                choice.draw()

        # update flip display
        pg.display.flip()

    # update current status
    def events(self):
        # get cursor position
        self.cursor_current_position = pg.mouse.get_pos()

        # get pygame event
        for event in pg.event.get():

            # quit button
            if event.type == pg.QUIT:
                if self.running:
                    self.running = False

            # screen size
            '''if event.type == pg.VIDEORESIZE:
                self.width, self.height = event.w, event.h
                self.surface = pg.display.set_mode((self.width, self.height), pg.RESIZABLE)'''
            # pass event variable to sprite handle event function
            if self.choices is not None:
                for choice in self.choices:
                    choice.handle_event(event)
            if self.amounts or self.insert is not None:
                for amount_and_insert in self.amounts + self.insert:
                    amount_and_insert.handle_event(event)
            if self.tables is not None:
                for table in self.tables:
                    table.handle_event(event)

        # get left click 
        self.click = pg.mouse.get_pressed()
        # tell if click or not
        self.clicked = False
        if self.click[0]:
            if not self.held:
                self.clicked = True
            self.held = True
        else:
            self.held = False

    # draw text on screen
    def drawtext(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        # midtop
        self.surface.blit(text_surface, text_rect)
