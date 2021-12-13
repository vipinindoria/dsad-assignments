import argparse


class ShortestTransformationSequence:
    def __init__(self, s, t, words):
        self.s = s
        self.t = t
        self.words = words

    def solve(self):
        if self.s == self.t:
            return 0, None
        return None, None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Application to Find the Shortest Transformation Sequence"
                                                 " to Reach a Target String from Source String.")
    parser.add_argument('-i', '--inputfile', type=argparse.FileType('r'), help='Input File Path', required=True)
    parser.add_argument('-o', '--outputfile', type=argparse.FileType('w'), help='Output File Path')
    args = parser.parse_args()

    # Read Input
    begin_word = args.inputfile.readline().split("=")[1].strip()
    end_word = args.inputfile.readline().split("=")[1].strip()
    dict_list = args.inputfile.readline().split("=")[1].strip().split(",")
    dict_list = [word.strip() for word in dict_list]
    args.inputfile.close()

    # Solve
    sts = ShortestTransformationSequence(begin_word, end_word, dict_list)
    sts_length, st = sts.solve()

    # Write Output
    output_file = args.outputfile if args.outputfile else args.inputfile.name.replace('input', 'output')
    with open(output_file, 'w') as f:
        f.write(f'Length of shortest  transformation sequence : {sts_length}\n')
        f.write(f'The shortest transformation is: {st}\n')
    f.close()
