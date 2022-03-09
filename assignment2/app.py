import argparse
import math

hash_size = 10


class HashTable:
    """
    Hash table class
    """
    def __init__(self, size):
        """
        Constructor
        :param size: Integer, size of the hash table
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        """
        Hashing function
        :param key: String, key to be hashed
        :return: Integer, Hash value
        """
        if isinstance(key, str):
            return sum(ord(c) for c in key) % self.size
        else:
            return key % self.size

    def insert(self, key, value):
        """
        Inserts the key-value pair in the hash table
        :param key: String, key to be inserted
        :param value: String, value to be inserted
        :return: List of tuples, list of key-value pairs
        """
        index = self.hash(key)
        if self.table[index] is not None:
            for kvp in self.table[index]:
                if kvp[0] == key:
                    if value not in kvp[1]:
                        kvp[1].append(value)
                    break
            else:
                self.table[index].append([key, [value]])
        else:
            self.table[index].append((key, [value]))

    def get(self, key):
        """
        Returns the value corresponding to the key
        :param key: String, key to be searched
        :return: Any, value corresponding to the key
        """
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v[0]
        return None

    def __getitem__(self, key):
        """
        Returns the value corresponding to the key
        :param key: String, key to be searched
        :return: Value corresponding to the key
        """
        return self.get(key)

    def __setitem__(self, key, value):
        """
        Inserts the key-value pair in the hash table
        :param key: key to be inserted
        :param value: value to be inserted
        :return: key-value pair
        """
        self.insert(key, value)

    def __contains__(self, key):
        """
        Checks if the key is present in the hash table
        :param key: String, key to be searched
        :return: Boolean, True if key is present, False otherwise
        """
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return True
        return False

    def __str__(self):
        """
        Returns the string representation of the hash table
        :return: String, string representation of the hash table
        """
        return str(self.table)

    def __iter__(self):
        """
        Returns an iterator for the hash table
        :return: Iterator
        """
        return iter(self.table)


class IOUtils:
    """
    Utility class for I/O operations
    """
    def __init__(self, config):
        """
        Constructor
        :param config:
        """
        self.args = config

    def read_from_file(self):
        """
        Reads the input file and returns the Adjacency list for the graph
        :return: matrix: Dict of Lists, Adjacency list for the graph
        """
        adjacency_dict = HashTable(hash_size)
        city_to_index = HashTable(hash_size)
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
            city_to_index.insert(city, index)
            index += 1
        for city_distance in city_distance_matrix:
            start_city, end_city, distance = city_distance
            if city_to_index[start_city] not in adjacency_dict:
                adjacency_dict.insert(city_to_index[start_city], [[city_to_index[end_city], distance]])
            else:
                adjacency_dict[city_to_index[start_city]].append([city_to_index[end_city], distance])
        return city_to_index, unique_cities, adjacency_dict

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
    def __init__(self, adjacency_dict, cities_idx, cities):
        self.adjacency_dict = adjacency_dict
        self.total_cities = len(cities)
        self.cities_idx = cities_idx
        self.cities = cities

    def create_adjacency_matrix(self):
        """
        Creates the adjacency matrix for the graph
        :return: matrix: List of Lists, Adjacency matrix for the graph
        """
        matrix = [[math.inf if i != j else 0 for i in range(self.total_cities)]
                  for j in range(self.total_cities)]

        for city in self.cities:
            index = self.cities_idx[city]
            if index in self.adjacency_dict:
                start_city = index
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
        :return: matrix: List of Lists, Shortest distances between all of the major cities and towns within the state X
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
    city_index, all_cities, graph = io_obj.read_from_file()

    # Create Adjacency Matrix
    common_obj = CommonUtils(graph, city_index, all_cities)
    adj_matrix = common_obj.create_adjacency_matrix()

    # Solve
    distances = ShortestPath(adj_matrix).solve()

    # Write Output
    io_obj.write_to_file(distances)
