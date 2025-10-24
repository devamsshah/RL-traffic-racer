# Traffic Racer RL

## Introduction

This is an exploratory project I built to dive into reinforcement learning (RL). The main goal was to train an RL agent to play the popular mobile game **Traffic Racer**. Along the way, I experimented with different algorithms and frameworks, gaining hands-on experience with core RL concepts and implementation details.*


---

## Project Overview

* **Environment**: Built a simplified version of Traffic Racer as an RL environment.
* **Algorithms**: Explored training with algorithms provided in popular RL libraries.
* **Frameworks**: Leveraged PyTorch and Gym for model training, environment interaction, and evaluation.
* **Focus Areas**:

  * Designing and tuning a reward function.
  * Understanding how policies evolve over training.
  * Managing checkpoints and experiment tracking.

---

## Results and Usage

The trained models can play the Traffic Racer environment with varying levels of success depending on the training run.

To **use the results**:

1. Load the environment (custom Gym-compatible wrapper).
2. Load a saved checkpoint (stored under `./checkpoints/`).
3. Run inference to watch the model play.

The project includes examples of checkpoints and evaluation scripts that demonstrate the model’s behavior.

---

## What I Learned

Through this project, I was able to:

* Gain practical experience with **PyTorch** for building and training RL models.
* Learn how to set up and interact with environments using **OpenAI Gym**.
* Deepen my understanding of the **theory behind RL algorithms** such as PPO and how they converge through trial and error.
* Recognize the importance of **reward function design**, and how even small changes can dramatically impact agent performance.

---

## Future Directions

Looking ahead, I see several exciting opportunities to extend this work:

* **Richer input signals**: Beyond screenshots, incorporating game-state information (speed, position, distances to obstacles) would allow for more nuanced decision-making.
* **Advanced reward functions**: More sophisticated reward shaping could encourage strategies beyond just survival (e.g., overtaking cars, maintaining smooth speed).
* **Scaling up**: Testing larger models and distributed training setups could accelerate learning and push performance further.

---

## What the Project Includes

* Code for training and evaluating RL agents on a Traffic Racer–like environment.
* Checkpoints of trained models.
* Scripts for logging, evaluation, and visualization.


---

## Reflections

This project gave me a foundation in RL and the confidence to tackle more ambitious problems in the future. More than just training agents, it taught me how to design an experiment, shape rewards, and systematic debugging skills I can carry into research and practical applications.

*This project is not intended as a production-ready implementation, but rather as a learning experience to understand the building blocks of RL environments, models, and training pipelines.
