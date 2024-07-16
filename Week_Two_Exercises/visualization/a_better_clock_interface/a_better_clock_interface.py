import os
from datetime import datetime, timezone
import numpy as np
import matplotlib.pyplot as plt

# Initialization, define some constant
path = os.path.dirname(os.path.abspath(__file__))
filename = path + "/clock_background.png"
background = plt.imread(filename)

SECOND_HAND_LENGTH = 200
SECOND_HAND_WIDTH = 2
MINUTE_HAND_LENGTH = 150
MINUTE_HAND_WIDTH = 3
HOUR_HAND_LENGTH = 100
HOUR_HAND_WIDTH = 5
GMT_HAND_LENGTH = 150
GMT_HAND_WIDTH = 3
center = np.array([256, 256])


def clock_hand_vector(angle, length):
    """Generates a numpy array for the coordinate to go to.

    Args:
        angle (int or float): Angle of the required vector
        length (int or float): Length of the clock hand

    Returns:
        np.ndarray: Gives an array of length 2
    """
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
        (hour / 12 * 2 * np.pi) + ((minute / 60 * 2 * np.pi) / 12), HOUR_HAND_LENGTH
    )
    minute_vector = clock_hand_vector(
        (minute / 60 * 2 * np.pi) + ((second / 60 * 2 * np.pi) / 60), MINUTE_HAND_LENGTH
    )
    second_vector = clock_hand_vector(second / 60 * 2 * np.pi, SECOND_HAND_LENGTH)
    gmt_vector = clock_hand_vector(
        (gmt_hour / 24 * 2 * np.pi)
        + ((gmt_minute / 120 * 2 * np.pi) / 12)
        + ((gmt_second / 7200 * 2 * np.pi) / 720),
        GMT_HAND_LENGTH,
    )
    plt.arrow(
        center[0],
        center[1],
        hour_vector[0],
        hour_vector[1],
        linewidth=HOUR_HAND_WIDTH,
        color="black",
    )
    plt.arrow(
        center[0],
        center[1],
        minute_vector[0],
        minute_vector[1],
        linewidth=MINUTE_HAND_WIDTH,
        color="black",
    )
    plt.arrow(
        center[0],
        center[1],
        second_vector[0],
        second_vector[1],
        linewidth=SECOND_HAND_WIDTH,
        color="red",
    )
    plt.arrow(
        center[0],
        center[1],
        gmt_vector[0],
        gmt_vector[1],
        linewidth=GMT_HAND_WIDTH,
        color="yellow",
    )

    plt.pause(0.1)
    plt.clf()
