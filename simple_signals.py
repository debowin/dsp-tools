"""
look into spines.
"""

__author__ = 'Debojeet_Chatterjee'
import matplotlib.pyplot as plt
import numpy as np


def unit_impulse_function(n):
    if n == 0:
        return 1.0
    return 0


def unit_impulse_signal(x_axis):
    """
    delta[n] =  1 if n=0,
                0 otherwise.
    :return:
    """
    signal = []
    for n in x_axis:
        signal.append(unit_impulse_function(n))
    return signal


def unit_step_function(n):
    """
    u[n] =  0 if n<0,
            1 otherwise.
    :return:
    """
    if n < 0:
        return 0
    return 1.0


def unit_step_signal(x_axis):
    """
    u[n] =  0 if n<0,
            1 otherwise.
    :return:
    """
    signal = []
    for n in x_axis:
        signal.append(unit_step_function(n))
    return signal


def exponential_decay_function(n, constant):
    """
    y[n] =  |a|**n * u[n] where 0<a<1.
    :return:
    """
    if n > 0:
        return constant**n * unit_step_function(n)
    return 0


def exponential_decay_signal(x_axis, constant):
    """
    y[n] =  |a|**n * u[n] where 0<a<1.
    :return:
    """
    signal = []
    for n in x_axis:
        signal.append(exponential_decay_function(n, constant))
    return signal


def zero_mean_sawtooth_function(n, width):
    """
    period = 2 * width
    y[n] =  2*n/period if n in period
            0 elsewhere.
    :return:
    """
    if -width <= n <= width:
        return float(n)/width
    return 0


def zero_mean_sawtooth_signal(x_axis, width):
    """
    y[n] =  2*n/period if n in period
            0 elsewhere.
    :return:
    """
    signal = []
    for n in x_axis:
        signal.append(zero_mean_sawtooth_function(n, width))
    return signal


def round_off(decimal):
    """
    round off a number to its closest integer value.
    """
    if decimal - int(decimal) > 0.5:
        return int(decimal) + 1
    elif decimal - int(decimal) < -0.5:
        return int(decimal) - 1
    return int(decimal)


def trigonometric_signal(function, x_axis, amplitude, phase, frequency, one_period=False):
    """
    type denotes which trigonometric function to use.
    if one_period is True, only returns non zero values
    for a single period. (useful for recursive filter)
    :return:
    """
    trigonometric = []
    half_period = round_off(np.pi / frequency)
    if one_period and len(x_axis) > 2 * half_period:
        for n in range(-half_period, half_period + 1):
            trigonometric.append(amplitude * function(n, frequency, phase))
        trigonometric = np.concatenate(
            (np.zeros(len(x_axis) / 2 - half_period), trigonometric, np.zeros(len(x_axis) / 2 - half_period)))
    else:
        for n in x_axis:
            trigonometric.append(amplitude * function(n, frequency, phase))
    return trigonometric


def sine_function(value, frequency, phase):
    """
    y[n] = sin(frequency*n + phase)
    :return:
    """
    return np.sin(value * frequency + phase)


def cosine_function(value, frequency, phase):
    """
    y[n] = cos(frequency*n + phase)
    :return:
    """
    return np.cos(value * frequency + phase)


def tan_function(value, frequency, phase):
    """
    y[n] = tan(frequency*n + phase)
    :return:
    """
    return np.sin(value * frequency + phase) / np.cos(value * frequency + phase)


def cot_function(value, frequency, phase):
    """
    y[n] = tan(frequency*n + phase)
    :return:
    """
    return np.cos(value * frequency + phase) / np.sin(value * frequency + phase)


def sec_function(value, frequency, phase):
    """
    y[n] = tan(frequency*n + phase)
    :return:
    """
    return 1.0 / np.cos(value * frequency + phase)


def cosec_function(value, frequency, phase):
    """
    y[n] = tan(frequency*n + phase)
    :return:
    """
    return 1.0 / np.sin(value * frequency + phase)


SIGNALS_DICT = [
    unit_impulse_signal,
    unit_step_signal,
    zero_mean_sawtooth_signal,
    exponential_decay_signal,
    trigonometric_signal
]

TRIGONOMETRIC_FUNCTIONS = [
    sine_function,
    cosine_function,
    tan_function,
    cot_function,
    sec_function,
    cosec_function
]


def show_graph(x_axis, y_axis, func=plt.stem, display_size=0, operands=None):
    """
    displays the graph for given X and Y coordinates.
    :param x_axis:
    :param y_axis:
    :return:
    """
    colors = ['g', 'r', 'c', 'm', 'y', 'k']
    plt.grid(True)
    func(x_axis, y_axis, label='resultant')
    if not operands:
        operands = []
    for arg in operands:
        plt.plot(x_axis, arg, colors[operands.index(arg)], label='signal %d' % (operands.index(arg)+1))
        plt.legend()
    y_max = max([abs(i) for i in y_axis])
    if display_size == 0:
        display_size = len(x_axis) / 2
    plt.axis([-display_size, display_size, -1.5 * y_max, 1.5 * y_max])
    plt.show()


def main():
    """
    main function
    :return:
    """
    x_max = 100
    x_axis = np.arange(-x_max, x_max + 1)
    choice = int(raw_input("Which signal do you want to see? "))

    constant = 3.0 / 4
    width = 10
    amplitude = 1
    phase = 0  # np.pi/2
    frequency = 2 * np.pi / 30  # the denominator is actually the period you want
    graph_type = plt.stem
    if choice < 2:
        # basic signals
        signal = SIGNALS_DICT[choice](x_axis)
    elif choice == 2:
        # zero mean sawtooth
        signal = SIGNALS_DICT[choice](x_axis, width)
    elif choice == 3:
        # exponential decay
        signal = SIGNALS_DICT[choice](x_axis, constant)
    else:
        # trigonometric signals
        signal = trigonometric_signal(TRIGONOMETRIC_FUNCTIONS[choice - 4], x_axis, amplitude, phase, frequency, False)
        graph_type = plt.plot
    show_graph(x_axis, signal, graph_type, display_size=20)


if __name__ == "__main__":
    main()
