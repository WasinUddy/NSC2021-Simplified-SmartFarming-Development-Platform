from frontend.gui import Gui
g = Gui()

while g.running:
    g.run()
    '''g.Advance_page.page2_result['OUTPUT'] = g.Advance_page.page2_result.pop('items')
    g.Advance_page.page2_result['INPUT'] = g.Advance_page.page2_result.pop('amount')
    g.Advance_page.page2_result['CONDITION'] = g.Advance_page.page2_result.pop('used_digital_pins')
    g.Advance_page.page2_result['VALUE'] = g.Advance_page.page2_result.pop('used_analog_pins')
    print(g.Advance_page.page1_result)
    print(g.Advance_page.page2_result)
'''
