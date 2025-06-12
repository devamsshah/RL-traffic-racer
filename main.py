import play #import click_on_play, choose_car, game_mode, choose_location, pause_game, continue_game, play, left, right, brake
from screen_view import get_frame, focus_on_iphone
from rl import TrafficEnv
from stable_baselines3 import DQN

#run without sudo so that the screenshots work. 

ACTIONS = {
    0: lambda: brake(),
    1: lambda: left(),
    2: lambda: right(),
    3: lambda: nothing()
}

play.play()

#env = TrafficEnv(get_frame_fn=get_frame, action_fn=ACTIONS)
#model = DQN("CnnPolicy", env, verbose=1)
#model.learn(total_timesteps=10000)



