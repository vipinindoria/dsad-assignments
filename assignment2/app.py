import argparse
import math


class IOUtils:
    """
    Utility class for I/O operations
    """
    def __init__(self, config):
        """
        Constructor
        :param args:
        """
        self.args = config

    def read_from_file(self):
        """
        Reads the input file and returns the Adjacency list for the graph
        :return: matrix: Dict of Lists, Adjacency list for the graph
        """
        adjacency_dict = {}
        city_to_index = {}
        city_distance_matrix = []
        unique_cities = set()
        index = 0
        for line in self.args.inputfile:
            line = line.strip()
            if line:
                start_city, end_city, distance = [int(elm) for elm in line.split('/')]
                city_distance_matrix.append([start_city, end_city, distance])
                unique_cities.add(start_city)
                unique_cities.add(end_city)
        self.args.inputfile.close()
        for city in unique_cities:
            city_to_index[city] = index
            index += 1
        for city_distance in city_distance_matrix:
            start_city, end_city, distance = city_distance
            if city_to_index[start_city] not in adjacency_dict:
                adjacency_dict[city_to_index[start_city]] = [[city_to_index[end_city], distance]]
            else:
                adjacency_dict[city_to_index[start_city]].append([city_to_index[end_city], distance])
        return adjacency_dict

    def write_to_file(self, matrix):
        """
        Writes the shortest distances between all pairs of major cities and towns within the state X in matrix
        format to output file
        :param matrix: List of Lists, Shortest distances between all pairs of major cities and towns within the state X
        :return: None
        """
        output_file = self.args.outputfile if args.outputfile else args.inputfile.name.replace('input', 'output')
        for row in matrix:
            output_file.write(','.join(map(str, row)) + '\n')
        output_file.close()


class CommonUtils:
    """
    Class for utility functions
    """

    """
    Constructor for the class
    param adjacency_dict: Dict of Lists, Adjacency list for the graph
    """
    def __init__(self, adjacency_dict):
        self.adjacency_dict = adjacency_dict

    def create_adjacency_matrix(self):
        """
        Creates the adjacency matrix for the graph
        :return: matrix: List of Lists, Adjacency matrix for the graph
        """
        matrix = [[math.inf if i != j else 0 for i in range(len(self.adjacency_dict))]
                  for j in range(len(self.adjacency_dict))]

        for start_city in self.adjacency_dict:
            for end_city, distance in self.adjacency_dict[start_city]:
                matrix[start_city][end_city] = distance
        return matrix


class ShortestPath:
    """Floyd Warshall algorithm for finding shortest path among cities"""
    def __init__(self, matrix):
        """
        Constructor
        :param matrix: List of Lists, Adjacency matrix for the graph
        """
        self.matrix = matrix
        self.n = len(matrix)

    def solve(self):
        """
        Implementation of Floyd Warshall algorithm for finding shortest path among cities
        :return: matrix: List of Lists, Shortest distances between all pairs of major cities and towns within the state X
        """
        for k in range(self.n):
            for r in range(self.n):
                for c in range(self.n):
                    self.matrix[r][c] = min(self.matrix[r][c], self.matrix[r][k] + self.matrix[k][c])
        return self.matrix


if __name__ == '__main__':
    # Get Arguments
    parser = argparse.ArgumentParser(description="Application to find the shortest distances "
                                                 "between all pairs of major cities and towns within the state.")
    parser.add_argument('-i', '--inputfile', type=argparse.FileType('r'), help='Input File Path', required=True)
    parser.add_argument('-o', '--outputfile', type=argparse.FileType('w'), help='Output File Path')
    args = parser.parse_args()

    # Read Input File
    io_obj = IOUtils(args)
    graph = io_obj.read_from_file()

    # Create Adjacency Matrix
    common_obj = CommonUtils(graph)
    adj_matrix = common_obj.create_adjacency_matrix()

    # Solve
    distances = ShortestPath(adj_matrix).solve()

    # Write Output
    io_obj.write_to_file(distances)
