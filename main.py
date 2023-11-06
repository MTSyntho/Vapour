from nicegui import ui
import webview

def openStore():
	print(storeSelection)
	ui.notify("You Selected '{}'".format(storeSelection))
	ui.label(storeSelection)
	if storeSelection==1:
		webview.create_window('Vapour - itch.io', 'https://itch.io/')
		webview.start()
	if storeSelection==2:
		webview.create_window('Vapour - GameJolt', 'https://gamejolt.com/')
		webview.start()

with ui.header(elevated=True).style('background-color: #47126b').classes('w-full items-center justify-between'):
	with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #571089') as left_drawer:
		with ui.header(elevated=True).style('background-color: #242424'):
			ui.label('Vapour')

		with ui.dialog() as dialog, ui.card():
			ui.label('Select A Game Store!')
			storeSelection = ui.select({1: 'itch.io', 2: 'GameJolt'}).classes('w-40')
			with ui.row():
				ui.button('Open', on_click=openStore)
				ui.button('Close', on_click=lambda: dialog.close) 

		ui.button('Game Stores', on_click=dialog.open)
		ui.button('Game Collection', on_click=lambda: ui.notify('You clicked me!'))
		ui.button('Downloaded Games', on_click=lambda: ui.notify('You clicked me!'))
	ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
	ui.label('')
	ui.label('Vapour')
	ui.label('')

with ui.card().tight():
    with ui.image('https://picsum.photos/id/684/640/360'):
        ui.label('Vapour is a free application that allows\nfor easy downloading of games from Store Pages\nlike itch.io, GameJolt as such.')
        ui.button('Game Stores', on_click=lambda: ui.notify('You clicked me!'))
        ui.button('Downloaded Games', on_click=lambda: ui.notify('You clicked me!'))
ui.run(title='Vapour', dark=True, native=True)