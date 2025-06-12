import numpy as np
import gym
from gym import spaces
import time
from stable_baselines3 import DQN
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.env_checker import check_env
import pytesseract
from PIL import Image

end_string = "TOTAL DISTANCE"

def check_if_done(state):
    text = pytesseract.image_to_string(Image.fromarray(image_array))
    print(text)
    if substring in text:
        return True
    else:
        return False

def get_reward(state):
    if check_if_done(state):
        return -100
    else: 
        return 1

class TrafficEnv(gym.Env):
    def __init__(self, get_frame_fn, action_fn):
        super(TrafficEnv, self).__init__()
        self.get_image = get_frame_fn 
        self.actions = action_fn

        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(low=0, high=225, shape=(84,84, 1), dtype=np.uint8)
    def reset(self):
        return self.get_image()

    def step(self, action):
        self.actions[action]()
        next_state = self.get_image()
        reward = self._get_reward(next_state)
        done = self._check_done(next_state)

        return next_state, reward, done, {}
    
    def _get_state(self):
        return get_frame()

    def _get_reward(self, state):
        return get_reward(state)
    
    def _check_done(self, state):
        return check_if_done(state)



__all__ = ["TrafficEnv"]

