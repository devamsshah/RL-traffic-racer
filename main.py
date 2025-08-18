import play
import screen_view as sv
from rl import TrafficEnv
from stable_baselines3 import PPO 
import gymnasium as gym
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.callbacks import CheckpointCallback
import os


#run without sudo so that the screenshots work. 


def custom_lr_schedule(progress_remaining: float) -> float:
    x = 1-progress_remaining
    return math.exp(-x) + 0.07 * math.sin(70 * x)


env = TrafficEnv()
check_env(env)

checkpoint_callback = CheckpointCallback(
    save_freq=1000,                  # Save every 1000 steps
    save_path="./checkpoints/",        # Directory to save checkpoints
    name_prefix="ppo_traffic_env_v=1_ns=200_bs=10_g=0.05_ws=5_ts=100000", 
    save_replay_buffer=False,
    save_vecnormalize=False
)

checkpoint_path = "./checkpoints/ppo_traffic_env_v=1_ns=200_bs=10_g=0.05_ws=5_ts=100000_10000_steps.zip"
if os.path.exists(checkpoint_path):
    model = PPO.load(checkpoint_path, env=env)
    print("Loaded model from latest checkpoint.")
else:
    model = PPO("CnnPolicy", env, learning_rate=custom_lr_schedule, verbose=1, n_steps=200, batch_size=10, gamma = 0.15, stats_window_size=5)
    print("Initialized new model.")

model.learn(total_timesteps=10000, callback=checkpoint_callback)
ts = int(model.num_timesteps)
now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"ppo_traffic_env_v1_ns200_bs10_g0.05_ws5_{now}_{ts}_steps"
model.save("ppo_traffic_env_v=1_ns=200_bs=10_g=0.05_ws=5_ts=100000", exclude=["env"])
print(f"Saved final model as {filename}.zip")
