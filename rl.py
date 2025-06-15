import gymnasium as gym
import numpy as np
from gymnasium import spaces
import play
import screen_view as sv


class CustomEnv(gym.Env):
    """Custom Environment that follows gym interface."""

    metadata = {"render_modes": ["human"], "render_fps": 30}

    def __init__(self, arg1, arg2, ...):
        super().__init__()
        # Define action and observation space
        # [direction, brake] => direction ∈ [-1, 1], brake ∈ [0, 1]
        self.action_space = spaces.Tuple((spaces.Discrete(4),
                                          spaces.Box(low=np.array([0.0]), high=np.array([1.0]), dtype=np.float64)))
        # Example for using image as input (channel-first; channel-last also works):
        # Assume get_frame returns image of shape (HEIGHT, WIDTH, 3) and dtype np.uint8
        HEIGHT, WIDTH, CHANNELS = 600, 1320, 4 
        self.observation_space = spaces.Box(low=0, high=255,
                                            shape=(HEIGHT, WIDTH CHANNELS), dtype=np.uint8)

    def step(self, action):
        a, m = action
        if a == 0:
            pass   
        elif a == 1:
            self.left(t=m)
        elif a == 2:
            self.right(t=m)
        elif a == 3:
            self.brake(t=m)
        else:
            raise ValueError(f"Invalid action number: {a}")
        

        observation = self.get_frame()
        reward, terminated = self.get_reward_and_is_finished(observation)

        return observation, reward, terminated

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        return self.get_frame(), {}

    def render(self):
        pass

    def close(self):
        pass
    
    def left(self, t=0.1):
        play.left(t=t)

    def right(self, t=0.1):
        play.right(t=t)

    def brake(self, t=0.1):
        play.brake(t=t)
    
    def get_frame(self):
        return sv.get_frame()

    def get_reward_and_is_finished(self, obs):
        end = sv.is_terminated(obs)
        if end:
            score = sv.get_score(obs)
            return 0.01*score, end
        else:
            return 1, end

