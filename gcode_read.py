#READS GCODE FILE AND EXTRACTS CARTESIAN X Y Z
from pygcode import Line
import re

#reads gcode file
def unpack_contents(filename):
    return_list = []
    with open(filename, 'r') as r_gcode:
        for this_line in r_gcode.readlines():
            try:
                line = Line(this_line)
                return_list.append(str(line))
            except:
                continue
    return return_list

#input x y or z as options
def get_axis_coordinate(axis, line):
    try:
        given_coordinate = re.search(F'{axis}(.*?) ',line).group(1)
        return given_coordinate
    except:
        pass

#returns dictionary for XYZ
def coordinate_contents(contents):
    coords = {'X':0,'Y':0,'Z':0}
    return_list=[]
    for line in contents:
        return_dict={}
        for coord in coords.keys():
            given_coordinate = get_axis_coordinate(coord,line)
            if given_coordinate is not None:
                return_dict[coord] = given_coordinate
                coords[coord] = given_coordinate
            else:
                return_dict[coord] = coords[coord]
        return_list.append(return_dict)
    return return_list


if __name__ == "__main__":
    print(coordinate_contents(unpack_contents('test.gcode')))
