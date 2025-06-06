from play_from import focus_on_iphone, click_on_play, choose_car, game_mode, choose_location, pause_game, continue_game
from screen_view import get_frame



def test_click_and_screenshot():
    get_frame()
	focus_on_iphone()
	click_on_play()
	get_frame()
	get_frame()
	get_frame()
	choose_car()
	get_frame()
	game_mode()
	choose_location()
	get_frame()
	pause_game()
	continue_game()
	get_frame()
