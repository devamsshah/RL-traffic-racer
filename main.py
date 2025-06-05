from play_from import focus_on_iphone, click_on_play, choose_car, game_mode, choose_location, pause_game, continue_game, play, enter_to_allow, left, right, brake
from screen_view import get_frame
import time
from rl import TrafficEnv
from stable_baselines3 import DQN

#ACTIONS = {
#    0: lambda: brake(),
#    1: lambda: left(),
#    2: lambda: right()
#}
#
#env = TrafficEnv(get_frame_fn=get_frame, action_fn=ACTIONS)
#model = DQN("CnnPolicy", env, verbose=1)
#model.learn(total_timesteps=10000)
#
#
get_frame()
focus_on_iphone()
enter_to_allow()
focus_on_iphone()
click_on_play()
get_frame()
get_frame()
get_frame()
