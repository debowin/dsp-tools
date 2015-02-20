__author__ = 'Debojeet_Chatterjee'
import matplotlib.pyplot as plt


def get_vector():
    """
    Takes a vector as input from the user.
    :return: tuple representing the vector
    """
    x0 = int(raw_input("Enter the X: "))
    x1 = int(raw_input("Enter the Y: "))

    return x0, x1


def show_vector(vector, *args):
    """
    displays the given vector
    :param vector: the vector to be displayed
    :return:
    """
    plt.grid(True)
    if args is ():
        operands = [(0, 0)]
    else:
        operands = args
    vectors = [vector]
    vectors.extend(operands)
    u, v = zip(*vectors)
    colors = [0]
    colors.extend([1]*len(operands))
    plt.quiver([0], [0], u, v, colors, angles='xy', scale_units='xy', scale=1)
    x_max = max([vector[0] for vector in vectors])
    y_max = max([vector[1] for vector in vectors])

    plt.xlim([-1.2*x_max, 1.2*x_max])
    plt.ylim([-1.2*y_max, 1.2*y_max])

    plt.show()


def vector_scaling(vector_one, constant):
    """
    scales a given vector.
    :param vector_one: the input vector
    :param constant: the constant to scale the vector by
    :return: the scaled vector
    """
    return vector_one[0] * constant, vector_one[1] * constant


def vector_sum(vector_one, vector_two):
    """
    creates a resultant vector.
    :param vector_one: the first input vector
    :param vector_two: the second input vector
    :return: the resultant sum vector
    """
    return vector_one[0] + vector_two[0], vector_one[1] + vector_two[1]


def main():
    """
    main function
    :return:
    """
    vector_one = get_vector()
    show_vector(vector_one)

    scaled_vector = vector_scaling(vector_one, 3)
    show_vector(scaled_vector, vector_one)

    vector_two = get_vector()
    show_vector(vector_two)

    scaled_vector = vector_scaling(vector_two, 3)
    show_vector(scaled_vector, vector_two)

    resultant = vector_sum(vector_one, vector_two)
    show_vector(resultant, vector_one, vector_two)


if __name__ == "__main__":
    main()