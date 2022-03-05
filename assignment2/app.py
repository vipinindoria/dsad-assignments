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
        Reads the input file and returns the Adjacency matrix for the graph
        :return: matrix: List of Lists, Adjacency matrix for the graph
        """
        matrix = []
        line_no = 0
        for line in self.args.inputfile:
            idx = 0
            row = []
            for elm in line.split(','):
                if idx != line_no and int(elm) == 0:
                    row.append(math.inf)
                else:
                    row.append(int(elm))
                idx += 1
            line_no += 1
            matrix.append(row)
        self.args.inputfile.close()
        return matrix

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

    # Solve
    distances = ShortestPath(graph).solve()

    # Write Output
    io_obj.write_to_file(distances)
