import argparse
from itertools import product


class IOUtils:
    def __init__(self, args):
        self.args = args

    def read_from_file(self):
        begin_word = self.args.inputfile.readline().split("=")[1].strip().strip('"').strip("'")
        end_word = self.args.inputfile.readline().split("=")[1].strip().strip('"').strip("'")
        dict_list = self.args.inputfile.readline().split("=")[1].strip().split(",")
        dict_list = [word.strip().strip('"').strip("'") for word in dict_list]
        args.inputfile.close()
        return begin_word, end_word, dict_list

    def write_to_file(self, sts_length, st):
        output_file = self.args.outputfile if args.outputfile else args.inputfile.name.replace('input', 'output')
        with open(output_file, 'w') as f:
            f.write(f'Length of shortest  transformation sequence : {sts_length}\n')
            f.write(f'The shortest transformation is: {st}\n')
        f.close()


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return sum(ord(c) for c in key) % self.size

    def insert(self, key, value):
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
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return
        raise KeyError(key)

    def __str__(self):
        return str(self.table)

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.table)

    def __iter__(self):
        for i in range(len(self.table)):
            for k, v in self.table[i]:
                yield k, v

    def __contains__(self, key):
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return True
        return False

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __delitem__(self, key):
        self.delete(key)


class GraphUtils:
    def __init__(self, vertices):
        self.buckets = HashTable(10)
        self.graph = HashTable(10)
        self.vertices = vertices

    def build_graph(self):
        for vertex in self.vertices:
            for i in range(len(vertex)):
                bucket = '{}_{}'.format(vertex[:i], vertex[i + 1:])
                self.buckets.insert(bucket, vertex)
        for table_row in self.buckets.table:
            for elm in table_row:
                mutual_neighbors = elm[1]
                for vertex1, vertex2 in product(mutual_neighbors, repeat=2):
                    if vertex1 != vertex2:
                        self.graph.insert(vertex1, vertex2)
                        self.graph.insert(vertex2, vertex1)

        return self.graph


class ShortestTransformationSequence:
    def __init__(self, s, t, words):
        self.s = s
        self.t = t
        self.words = words

    def get_shortest_transformation_sequence(self, graph):
        visited = set()
        queue = [[self.s]]
        while queue:
            path = queue.pop(0)
            vertex = path[-1]
            yield vertex, path
            if graph.get(vertex) is not None:
                for neighbor in set(graph.get(vertex)) - visited:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])

    def solve(self):
        if self.s == self.t:
            return 0, "Start and end words are same."

        self.words.append(self.s)
        graph = GraphUtils(self.words).build_graph()
        for vertex, path in self.get_shortest_transformation_sequence(graph):
            if vertex == self.t:
                return len(path), ' -> '.join(path)
        return -1, "No transformation sequence found."


if __name__ == '__main__':
    # Get Arguments
    parser = argparse.ArgumentParser(description="Application to Find the Shortest Transformation Sequence"
                                                 " to Reach a Target String from Source String.")
    parser.add_argument('-i', '--inputfile', type=argparse.FileType('r'), help='Input File Path', required=True)
    parser.add_argument('-o', '--outputfile', type=argparse.FileType('w'), help='Output File Path')
    args = parser.parse_args()

    # Read Input
    io_obj = IOUtils(args)
    begin_word, end_word, dict_list = io_obj.read_from_file()

    # Solve
    sts_length, st = ShortestTransformationSequence(begin_word, end_word, dict_list).solve()

    # Write Output
    io_obj.write_to_file(sts_length, st)
