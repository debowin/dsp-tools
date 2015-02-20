"""
simulation of operator blocks on digital signals:
    adder
    multiplier
    delay
    recursive filter
also make a player based on the Karplus-Strong algorithm. (audio)
maybe write your signals into a wave file and then play it.
"""
import simple_signals
import numpy as np

__author__ = 'Debojeet_Chatterjee'

X_MAX = 100
x_axis = np.arange(-X_MAX, X_MAX + 1)


def adder(signal_one, signal_two):
    """
    y[n] = x1[n] + x2[n]
    :param signal_one:
    :param signal_two:
    :return:
    """
    signal_sum = []
    for i in zip(signal_one, signal_two):
        signal_sum.append(i[0] + i[1])
    return signal_sum


def multiplier(signal, constant):
    """
    y[n] = a * x[n]
    :param signal:
    :param constant:
    :return:
    """
    product_signal = [i * constant for i in signal]
    return product_signal


def delay(signal, amount):
    """
    y[n] = x[n-d]
    :param signal:
    :param amount:
    :return:
    """
    delayed = [0] * amount
    for i in range(amount, len(signal)):
        delayed.append(signal[i - amount])
    return delayed


def recursive_filter(signal, window, constant):
    """
    y[n] = a*y[n-M] + x[n]
    :param signal:
    :param window:
    :param constant:
    :return:
    """
    for i in range(window, len(signal)):
        signal[i] += constant * signal[i - window]
    return signal


def moving_average(signal, window):
    """
    y[n] = 1/N*sum{m:0->N-1}(x[n-m])
    :param signal:
    :param window:
    :return:
    """
    average_signal = []
    for i in range(window, len(signal)):
        signal_sum = 0
        for n in range(window):
            signal_sum += signal[i - n]
        average_signal.append(signal_sum / window)
    return np.concatenate((np.zeros(window), average_signal))


def inner_product(signal_one, signal_two, window):
    """
    y[n] = sum{m:-window->window}(x1[n] * x2[n])
    :param signal_one:
    :param signal_two:
    :return:
    """
    remainder = len(signal_one) / 2 - window
    product_signal = []
    result = 0
    signal_one = signal_one[remainder:-remainder]
    signal_two = signal_two[remainder:-remainder]
    for i in range(len(signal_one)):
        product = signal_one[i] * signal_two[i]
        result += product
        product_signal.append(product)
    return np.concatenate((np.zeros(remainder), product_signal, np.zeros(remainder))), result


def get_signal(constant, width, amplitude, phase, frequency):
    """
    pick a type of signal and return the
    corresponding constructed signal.
    :return:
    """
    choice = int(raw_input('Signal Type? ')) - 1
    if choice < 2:
        # basic signals
        signal = simple_signals.SIGNALS_DICT[choice](x_axis)
    elif choice == 2:
        # zero mean sawtooth
        signal = simple_signals.SIGNALS_DICT[choice](x_axis, width)
    elif choice == 3:
        # exponential decay
        signal = simple_signals.SIGNALS_DICT[choice](x_axis, constant)
    else:
        # trigonometric signals
        signal = simple_signals.trigonometric_signal(simple_signals.TRIGONOMETRIC_FUNCTIONS[choice - 4], x_axis,
                                                     amplitude, phase, frequency)
    simple_signals.show_graph(x_axis, signal)
    return signal


def main():
    # Signal 1
    signal_one = get_signal(3.0 / 4, 10, 1, 0, 2 * np.pi / 50)

    # Signal 2
    signal_two = get_signal(3.0 / 4, 10, 1, 0, 2 * np.pi / 20)

    choice = int(
        raw_input(
            "\nWhich operation?\n1)Adder\n2)Multiplier\n3)Delay\n4)Recursive Filter\n5)Moving Average\n6)Inner Product\nChoose: "))

    constant = 0.9
    amount = 5
    window = 51
    if choice == 1:
        result_signal = adder(signal_one, signal_two)
        simple_signals.show_graph(x_axis, result_signal, operands=[signal_one, signal_two])
    elif choice == 2:
        result_signal = multiplier(signal_one, constant)
        simple_signals.show_graph(x_axis, result_signal, operands=[signal_one])
        result_signal = multiplier(signal_two, constant)
        simple_signals.show_graph(x_axis, result_signal, operands=[signal_two])
    elif choice == 3:
        result_signal = delay(signal_one, amount)
        simple_signals.show_graph(x_axis, result_signal, operands=[signal_one])
        result_signal = delay(signal_two, amount)
        simple_signals.show_graph(x_axis, result_signal, operands=[signal_two])
    elif choice == 4:
        result_signal = recursive_filter(signal_one, window, constant)
        simple_signals.show_graph(x_axis, result_signal, operands=[signal_one])
        result_signal = recursive_filter(signal_two, window, constant)
        simple_signals.show_graph(x_axis, result_signal, operands=[signal_two])
    elif choice == 5:
        result_signal = moving_average(signal_one, window)
        simple_signals.show_graph(x_axis, result_signal, operands=[signal_one])
        result_signal = moving_average(signal_two, window)
        simple_signals.show_graph(x_axis, result_signal, operands=[signal_two])
    elif choice == 6:
        result_signal, result = inner_product(signal_one, signal_two, window)
        print "Inner Product: ", result
        simple_signals.show_graph(x_axis, result_signal, operands=[signal_one, signal_two])


if __name__ == "__main__":
    main()