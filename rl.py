import gymnasium as gym
import numpy as np
from gymnasium import spaces
import play, time
import screen_view as sv

class TrafficEnv(gym.Env):
    """Custom Environment that follows gym interface."""

    metadata = {"render_modes": ["human"], "render_fps": 30}

    def __init__(self):
        super().__init__()
        play.play()
        self.training_start_time = time.time()
        self.no_score = 0  #keeps track of the number of times score wasnt been able to scan
        # Define action and observation space
        # [direction, brake] => direction ∈ [-1, 1], brake ∈ [0, 1]
        self.action_space = spaces.Box(low=np.array([0.0, 0.0]),
                               high=np.array([3.0, 1.0]),
                                       dtype=np.float64)
        # Example for using image as input (channel-first; channel-last also works):
        # Assume get_frame returns image of shape (HEIGHT, WIDTH, 3) and dtype np.uint8
        HEIGHT, WIDTH, CHANNELS = 600, 1320, 4 
        self.observation_space = spaces.Box(low=0, high=255,
                                            shape=(HEIGHT, WIDTH, CHANNELS), dtype=np.uint8)

    def step(self, action):
        action_type = int(np.clip(round(action[0]), 0, 3))  # round and clip to 0–3
        magnitude = float(np.clip(action[1], 0.0, 1.0))     # magnitude 0.0–1.0
	    
        act = ""
        if action_type == 0:
            act = "nothing"
        elif action_type == 1:
            act = "left"
            self.left(magnitude)
        elif action_type == 2:
            act = "right"
            self.right(magnitude)
        elif action_type == 3:
            act = "brake"
            self.brake(magnitude)
        else:
            act = "ERROR"
        observation = self.get_frame()
        reward, terminated = self.get_reward_and_is_finished(observation)
        
        info = {
            "action_taken": act+": "+str(magnitude),
            "time_elapsed": time.time() - self.training_start_time
        }
        return observation, reward, terminated, False, info

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        play.play_again()
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
            score, self.no_score = sv.get_score(self.no_score, frame=obs)
            return (0.01*score)-10, end
        else:
            return 0.01, end

