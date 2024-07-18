## This is course material for Introduction to Modern Artificial Intelligence
## Example code: cartpole_dqn.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020-2024. Intelligent Racing Inc. Not permitted for commercial use

# Please make sure to install openAI gym module
# pip install gym==0.17.3
# pip install pyglet==1.5.29

import random
import gym
import os
import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense

# from tensorflow.keras.optimizers import Adam
from keras.optimizers import Adam

EPISODES = 100


class PIDController:
    def __init__(self, kp, kd, ki):
        self.kp = kp
        self.kd = kd
        self.ki = ki
        self.prev_error = 0
        self.integral = 0

    def compute(self, error, dt):
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        self.prev_error = error
        return self.kp * error + self.kd * derivative + self.ki * derivative


if __name__ == "__main__":
    env = gym.make("CartPole-v1")
    pid = PIDController(kp=1, ki=0.5, kd=0.01)
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n
    done = False

    for e in range(EPISODES):
        state = env.reset()
        for time in range(500):
            env.render()
            pole_angle = state[2]  # The pole angle is the third state variable
            error = pole_angle
            control_signal = pid.compute(
                error, dt=0.02
            )  # Assume a fixed time step of 0.02s
            action = (
                0 if control_signal < 0 else 1
            )  # Apply action based on control signal

            next_state, reward, done, info = env.step(action)  # Only 4 values returned
            state = next_state

            if done:
                print(f"Episode: {e}/{EPISODES}, Score: {time}")
                break
