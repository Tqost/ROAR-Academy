from datetime import datetime, timezone
import matplotlib.pyplot as plt
import os
import numpy as np
import time

# Initialization, define some constant
path = os.path.dirname(os.path.abspath(__file__))
filename = path + "/clock_background.png"
background = plt.imread(filename)

second_hand_length = 200
second_hand_width = 2
minute_hand_length = 150
minute_hand_width = 3
hour_hand_length = 100
hour_hand_width = 5
gmt_hand_length = 150
gmt_hand_width = 3
center = np.array([256, 256])


def clock_hand_vector(angle, length):
    return np.array([length * np.sin(angle), -length * np.cos(angle)])


# draw an image background
fig, ax = plt.subplots()

while True:
    plt.imshow(background)
    # plt.subplots_adjust(left=0.10, bottom=0.10, top=0.90, right=0.90)
    plt.axis("off")
    # First retrieve the time
    now_time = datetime.now()
    hour = now_time.hour
    if hour > 12:
        hour = hour - 12
    minute = now_time.minute
    second = now_time.second
    gmt_time = datetime.now(timezone.utc)
    gmt_hour = gmt_time.hour
    gmt_minute = gmt_time.minute
    gmt_second = gmt_time.second

    # Calculate end points of hour, minute, second

    hour_vector = clock_hand_vector(
        (hour / 12 * 2 * np.pi) + ((minute / 60 * 2 * np.pi) / 12), hour_hand_length
    )
    minute_vector = clock_hand_vector(
        (minute / 60 * 2 * np.pi) + ((second / 60 * 2 * np.pi) / 60), minute_hand_length
    )
    second_vector = clock_hand_vector(second / 60 * 2 * np.pi, second_hand_length)
    gmt_vector = clock_hand_vector(
        (gmt_hour / 24 * 2 * np.pi)
        + ((gmt_minute / 120 * 2 * np.pi) / 12)
        + ((gmt_second / 7200 * 2 * np.pi) / 720),
        gmt_hand_length,
    )
    plt.arrow(
        center[0],
        center[1],
        hour_vector[0],
        hour_vector[1],
        linewidth=hour_hand_width,
        color="black",
    )
    plt.arrow(
        center[0],
        center[1],
        minute_vector[0],
        minute_vector[1],
        linewidth=minute_hand_width,
        color="black",
    )
    plt.arrow(
        center[0],
        center[1],
        second_vector[0],
        second_vector[1],
        linewidth=second_hand_width,
        color="red",
    )
    plt.arrow(
        center[0],
        center[1],
        gmt_vector[0],
        gmt_vector[1],
        linewidth=gmt_hand_width,
        color="yellow",
    )

    plt.pause(0.1)
    plt.clf()
