import numpy as np
import sys
import json
import matplotlib.pyplot as plt

zero = np.array(
    [
        0.0,
        0.9659259,
        0.49999982,
        -0.7071069,
        -0.8660252,
        0.2588196,
        1.0,
        0.2588185,
        -0.8660258,
        -0.70710677,
        0.500001,
        0.96592546,
        -6.755325e-7,
        -0.9659258,
        -0.49999905,
        0.70710707,
        0.8660246,
        -0.25881982,
        -1.0,
        -0.2588197,
        0.8660266,
        0.70710564,
        -0.50000244,
        -0.96592575,
        1.351065e-6,
        0.96592647,
        0.5000001,
        -0.70710754,
        -0.8660243,
        0.25881863,
        1.0,
        0.2588172,
        -0.86602694,
        -0.7071038,
        0.5000014,
        0.9659251,
        -1.1924881e-7,
        -0.96592516,
        -0.5000012,
        0.70710933,
        0.866023,
        -0.25881743,
        -1.0,
        -0.2588184,
        0.86602825,
        0.70710737,
        -0.5000003,
        -0.96592546,
    ]
)

one = np.array(
    [
        -0.0,
        -0.9659259,
        -0.49999982,
        0.7071069,
        0.8660252,
        -0.2588196,
        -1.0,
        -0.2588185,
        0.8660258,
        0.70710677,
        -0.500001,
        -0.96592546,
        6.755325e-7,
        0.9659258,
        0.49999905,
        -0.70710707,
        -0.8660246,
        0.25881982,
        1.0,
        0.2588197,
        -0.8660266,
        -0.70710564,
        0.50000244,
        0.96592575,
        -1.351065e-6,
        -0.96592647,
        -0.5000001,
        0.70710754,
        0.8660243,
        -0.25881863,
        -1.0,
        -0.2588172,
        0.86602694,
        0.7071038,
        -0.5000014,
        -0.9659251,
        1.1924881e-7,
        0.96592516,
        0.5000012,
        -0.70710933,
        -0.866023,
        0.25881743,
        1.0,
        0.2588184,
        -0.86602825,
        -0.70710737,
        0.5000003,
        0.96592546,
    ]
)

filename = sys.argv[1]
with open(filename) as f:
    sample = np.array(json.loads(f.read()))

plt.style.use("seaborn-poster")


def draw_amplitude(t, x):
    plt.figure(figsize=(8, 6))
    plt.plot(t, x, "r")
    plt.ylabel("Amplitude")

    plt.show()


# sampling rate
sr = 48000
# sampling interval
ts = 1.0 / sr
t = np.arange(0, len(sample) * ts - 1e-8, ts)
draw_amplitude(t, sample * one)

print(sum(sample * one))
