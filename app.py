from itertools import product

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
                # print(list(product(mutual_neighbors, repeat=2)))
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
            for neighbor in set(graph.get(vertex)) - visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    def solve(self):
        if self.s == self.t:
            return 0, self.s

        self.words.append(self.s)
        graph = GraphUtils(self.words).build_graph()
        for vertex, path in self.get_shortest_transformation_sequence(graph):
            if vertex == self.t:
                return len(path), ' -> '.join(path)
        return -1, None


if __name__ == '__main__':
    # Initialize basic variables
    beginWord = ""
    endWord = ""
    Dict = []

    # Input handling
    with open('inputPS14.txt', 'r') as input_file:
        lines = input_file.readlines()
        for i in lines:
            linelist = i.strip('\n').split('=')
            if linelist[0].strip(' ') == 'beginWord':
                beginWord = linelist[1].strip(' ')
            if linelist[0].strip(' ') == 'endWord':
                endWord = linelist[1].strip(' ')
            if linelist[0].strip(' ') == 'Dict':
                for x in linelist[1].split(','):
                    Dict.append(x.strip(' '))
    input_file.close()

    # Adding the start and end words to the graph if not present
    if beginWord not in Dict:
        Dict.append(beginWord)
    if endWord not in Dict:
        Dict.append(endWord)

    # Solve
    sts_length, st = ShortestTransformationSequence(beginWord, endWord, Dict).solve()

    # Write Output
    with open('outputPS14.txt', 'w') as output_file:
        output_file.write(f'Length of shortest  transformation sequence : {sts_length}\n')
        output_file.write(f'The shortest transformation is: {st}\n')
    output_file.close()
