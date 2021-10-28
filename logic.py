import math

class SectorArea:
    def __init__(self):
        central_angle = self.centralangle
        chord_length = self.chordlength
        sector_area = self.sectorarea
        arc_length = self.arclength
        diameter = self.diameter
        radius = self.radius

    def set_diameter_radius(self):
        pass

    def return_sector_area(self, centralangle, radius):
        if centralangle and radius:
            area = centralangle/360
            area = area

    def return_arc_length(self, centralangle, radius):
        pass

    def return_chord_length(self, diameter, radius):
        pass
        #Equation = 2(math.sqrt(radius ** 2 - diameter ** 2)
        #Breaking it up into smaller equations.

        chordlength =


    def return_all_values(self):
        pass


def diamter_radius(d, r):
    if (d and not r):




def sector_area_receive(math_values):
    central_angle = math_values.get('centralangle')
    chord_length = math_values.get('chordlength')
    sector_area = math_values.get('sectorarea')
    arc_length = math_values.get('arclength')
    diameter = math_values.get('diameter')
    radius = math_values.get('radius')

    data = SectorArea(central_angle, chord_length, sector_area, arc_length, diameter, radius)




def deg_to_rad(deg):
    """
    Function that changes degrees to radians.
    :param deg: degree input value
    :return: number in radians
    """
    deg = deg * math.pi
    rad = deg / 180
    return rad

def rad_to_deg(rad):
    """
    Function that changes radians to degrees.
    :param rad: radian input value
    :return: number in degrees
    """
    print("Radians to degrees function initiated.")
    rad = rad * 180
    deg = rad / math.pi
    return deg


def triangle_solve(*data): # fixme: Will need to finish this function after data movement is switched over. Will make it easier to handle the problem (less code).
    print("Triangle solver function initiated.")
    a, b, c, A, B, C = data[0],data[2],data[4],data[6],data[8],data[10]
    values = [a,b,c,A,B,C]
    chars = {
        "a": data[0],
        "b": data[2],
        "c": data[4],
        "A": data[6],
        "B": data[8],
        "C": data[10]
    }
    missing = 0
    missing_value = []
    missing_char = []
    index = 0
    for i in data:
        if i == False:
            missing = missing + 1
            if missing > 3:
                return "Yeah right pal, I'm gonna need more atleast 3 values."
            index = index + 1
            index = i - 1
            missing_value.append(i[index])
            #for key in chars:


def distance_calculate(xvalues, yvalues, verified):
    """
    Function that calculates the distance between to verteces
    :param xvalues: X1 and X2 input on ('distance.html')
    :param yvalues: Y1 and Y2 input on ('distance.html')
    :param verified: true if all values are present, false if not.
    :return: The answer for 'dist' value.
    """
    print("Distance Calculator running...")
    if verified:
        dist = math.sqrt(((xvalues[1] - xvalues[0]) ** 2) + ((yvalues[1] - yvalues[0]) ** 2))
        return f'Answer: {str(dist)}'
    elif verified is False or None:
        return "You need to input all 4 values for correct calculations."


def pythag_calculate(a_data, b_data, c_data):
    """
    Function that takes a_data, b_data, c_data, finds the missing side and computes and returns.
    :return: a 'result' for HTML webpage (pythag.html)
    """
    print("Pythagorean Theorum Calculator running...")
    if (a_data[1] and b_data[1]) and (c_data[1] == False):
        c_data[0] = a_data[0] ** 2 + b_data[0] ** 2
        c_data[0] = math.sqrt(c_data[0])
        return "C value is: ", c_data[0]
    if (a_data[1] and c_data[1]) and (b_data[1] == False):
        b_data[0] = a_data[0] ** 2 + c_data[0] ** 2
        b_data[0] = math.sqrt(b_data[0])
        return "B value is: ", b_data[0]
    if (b_data[1] and c_data[1]) and (a_data[1] == False):
        a_data[0] = b_data[0] ** 2 + c_data[0] ** 2
        a_data[0] = math.sqrt(a_data[0])
        return "A value is: ", a_data[0]
    elif (b_data[1] and c_data[1] and a_data[1]):
        return "Triangle is solved, no values needed."
    else:
        return "The triangle can only be solved if two values are input."



"""
Commented out this function because the future of data checking might be a little different.

def check_lists(*args):
    print("Check list function initiated.")
    inputdata = []
    inputvalues = []
    indexer = 0
    placeholder = 1
    max_length = 0
    for arg in args:
        max_length = max_length + 1
        if (len(arg[0])) <= 0:
            inputvalues.append(False)
            inputdata.append(arg[0])
            print("False value found.")
        if (len(arg[0])) > 0:
            print(arg[0], "is a valid number.")
            try:
                inputdata.append(int(arg[0]))
            except ValueError as err:
                return err
            inputvalues.append(True)
    while indexer < max_length:
        inputdata.insert(placeholder, inputvalues[indexer])
        indexer = indexer + 1
        placeholder = placeholder + 2
    return inputdata
"""