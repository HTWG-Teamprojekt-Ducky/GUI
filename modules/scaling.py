scaled_coordinates_ = {}
gui_final_coordinates_ = {}

def global_to_scaled_coordinates(list_of_coordinates):
    """
    This scaling to scale the coordinates from yaml file and obtain a
    tile size of 2.8 cm. We take the global coordinates and add the
    coordinates with itself and 1 for scaling.
    """

    for element in list_of_coordinates:

        gui_coordinates = []

        for coordinates in element:
            integer_part, decimal_part = map(int, str(coordinates).split(".", 1))

            # global tiles coordinates remain same while scaling
            # the elements inside the tiles needs to scaled
            # so we always scale the decimal part
            scaled_integer_part = integer_part

            # scaling is done in two steps here
            # we double the coordinate
            scaled_decimal_part1 = decimal_part + decimal_part
            # add one to the the scaled decimal
            scaled_decimal_part2 = decimal_part + decimal_part + 1

            # TODO:format to keep trailing zeros
            scaled_coordinate1 = (float(str(scaled_integer_part) + "." + str(scaled_decimal_part1)))
            scaled_coordinate2 = (float(str(scaled_integer_part) + "." + str(scaled_decimal_part2)))

            gui_coordinates.append((scaled_coordinate1, scaled_coordinate2))

        scaled_coordinates_[element] = gui_coordinates

    print("scaled coordinates - ", scaled_coordinates_)


def scaled_to_gui_coordinates():
    list_values = scaled_coordinates_.values()
    counter = 0
    for scaled_element in list_values:

        gui_coordinates = []

        for scaled_coordinate1, scaled_coordinate2 in scaled_element:

            integer_part1, decimal_part1 = map(int, str(scaled_coordinate1).split(".", 1))
            integer_part2, decimal_part2 = map(int, str(scaled_coordinate2).split(".", 1))

            if integer_part1 == 0:
                scaled_integer_part1 = integer_part1
            else:
                scaled_integer_part1 = integer_part1 * 120

            scaled_decimal_part1 = decimal_part1 * 6

            if integer_part2 == 0:
                scaled_integer_part2 = integer_part2
            else:
                scaled_integer_part2 = integer_part2 * 120

            scaled_decimal_part2 = decimal_part2 * 6

            final_scaled_x_and_y1 = scaled_integer_part1 + scaled_decimal_part1
            final_scaled_x_and_y2 = scaled_integer_part2 + scaled_decimal_part2

            gui_coordinates.append(final_scaled_x_and_y1)
            gui_coordinates.append(final_scaled_x_and_y2)

        gui_final_coordinates_[counter] = gui_coordinates
        counter = counter + 1

    print("gui final coordinates - ", gui_final_coordinates_)

    global_to_scaled_coordinates(array_of_local_coordinates)
    scaled_to_gui_coordinates()

def convert_to_ducky_four_coordinates(a, b):
    # TODO: Set bounds so that ducky generated stays on road

    x, y, x1, y1 = 0, 0, 0, 0

    if a != 0 & b != 0:
        x1, y1 = 2 * a, 2 * b
        x, y = x1 - 42, y1 - 72

    return x, y, x1, y1