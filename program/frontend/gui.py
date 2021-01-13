# Graphic User Interface of program
from frontend.Page import *
import sys

#quit pygame
def Quit():
    pg.quit()
    sys.exit()

#object for all gui
class Gui:
    #initalizing the program
    def __init__(self):
        #check if running
        self.running = True
        #menu page check
        self.MENU = True
        #normal advance tutorial
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

    # menu page
    def Menu(self):
        # set which page we are on
        self.MENU, self.NORMAL, self.ADVANCE, self.TUTORIAL = True, False, False, False

        # create button object required in Menu page
        self.advance_button = Button(self.surface, butgreen, self.width * 1 / 10, self.height *4/5, self.width * 4 // 5, 75,
                              "โหมดผู้เชี่ยวชาญ", txtbrown, None, 40)
        self.normal_button = Button(self.surface, butgreen, self.width * 1 / 10, self.height / 2 + 75, self.width * 4 // 5, 75,
                             "โหมดใช้งานง่าย", txtbrown, None, 40)
        self.tutorial_button = Button(self.surface, butgreen, self.width * 1 / 10, self.height / 2 - 25, self.width * 4 // 5,75,
                               "คู่มือการใช้งาน", txtbrown, None, 40)

        # add created object to menu page
        self.Menu_Button = [self.tutorial_button, self.normal_button, self.advance_button]

    # create graphic user interface
    def run(self):
        # load menu page as starting page
        self.Menu()

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

        # current status in menu page 
        if self.MENU:

            # if clicked on normal_mode_button
            if self.normal_button.isOver(self.cursor_current_position) and self.clicked:

                # move to normal normal page
                self.NORMAL = True
                self.Normal_page.page = 1
                self.MENU = False
            
            # if clicked on advance_mode_button 
            elif self.advance_button.isOver(self.cursor_current_position) and self.clicked:

                # move to advance mode page
                self.ADVANCE = True
                self.Advance_page.page = 1
                self.MENU = False

            # if clicked on tutorial_mode_button
            elif self.tutorial_button.isOver(self.cursor_current_position) and self.clicked:

                # move to tutorial mode page
                self.TUTORIAL = True
                self.Tutorial_page.page = 1
                self.MENU = False
            
            # reset all variable in menu page
            self.buttons = self.Menu_Button
            self.choices = []
            self.tables = []
            self.amounts = []
            self.insert = []

        # if in tutorial page
        elif self.TUTORIAL:

            # calling Tutorial class in Page.py
            self.Tutorial_page.update(self.clicked, self.cursor_current_position)

            # if exit tutorial page return to menu
            if self.Tutorial_page.page == 0:
                self.Menu()
            self.buttons = self.Tutorial_page.button

        # if in normal page
        elif self.NORMAL:

            # calling Normal class in Page.py
            self.Normal_page.update(self.clicked, self.cursor_current_position)

            # if exit normal page return to menu
            if self.Normal_page.page == 0:
                self.Menu()
            self.buttons = self.Normal_page.button

        # if in advanve page 
        elif self.ADVANCE:

            # calling Advance class in Page.py
            self.Advance_page.update(self.clicked, self.cursor_current_position, self.width, self.height)

            # if exit advance page return to menu
            if self.Advance_page.page == 0:
                self.Menu()

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

        # if in Menu: draw menu
        if self.MENU:
            
            # draw image(logo)
            self.surface.blit(self.logo, (self.width / 2 - 120, self.height /4 - 120))

            #=set all attribute for required button to draw
            self.advance_button.x, self.advance_button.y, self.advance_button.width, self.advance_button.height = self.width * 1 / 10\
                , self.height *4/5, self.width * 4 // 5, self.height*1/8
            self.normal_button.x, self.normal_button.y, self.normal_button.width, self.normal_button.height = \
                self.width * 1 / 10, self.height *4/5 - self.height*1/8 - 25, self.width * 4 // 5, self.height*1/8
            self.tutorial_button.x, self.tutorial_button.y, self.tutorial_button.width, self.tutorial_button.height = \
                self.width * 1 / 10, self.height *4/5 - 2*(self.height*1/8 + 25),self.width * 4 // 5, self.height*1/8

            # pack all button in to one list 
            self.Menu_Button = [self.tutorial_button, self.normal_button, self.advance_button]

        elif self.TUTORIAL:
            self.Tutorial_page.draw(self.drawtext)
        elif self.NORMAL:
            self.Normal_page.draw(self.drawtext)
        elif self.ADVANCE:
            self.Advance_page.draw(self.drawtext, self.cursor_current_position)
    
        # draw all button
        for button in self.buttons:
            button.draw(self.clicked)
    
        # draw dropdown menu
        if self.choices is not None:
            for choice in self.choices:
                choice.draw()

        # draw all amount
        if self.amounts is not None:
            for amount_and_insert in self.amounts + self.insert:
                amount_and_insert.draw(self.surface)
        
        # draw all table
        if self.tables is not None:
            for table in self.tables:
                table.draw()

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
