import play
import screen_view as sv
from rl import TrafficEnv
from stable_baselines3 import PPO 
import gymnasium as gym
from stable_baselines3.common.env_checker import check_env

#run without sudo so that the screenshots work. 

env = TrafficEnv()
check_env(env)

model = PPO("CnnPolicy", env, verbose=1)
model.learn(total_timesteps=100)
model.save("ppo_traffic_env")
