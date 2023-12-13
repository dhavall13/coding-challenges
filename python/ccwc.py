import sys
import argparse

parser = argparse.ArgumentParser(
    description="CCWC", formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument("filename", nargs="?", help="filename")
parser.add_argument("-c", "--count", action="store_true", help="count bytes in a file")
parser.add_argument("-l", "--lines", action="store_true", help="count lines in a file")
parser.add_argument("-w", "--words", action="store_true", help="count words in a file")
parser.add_argument(
    "-m", "--characters", action="store_true", help="count characters in a file"
)


args = parser.parse_args()

if args.filename:
    try:
        with open(args.filename, "r") as f:
            data = f.read()
    except FileNotFoundError:
        print("File not found")
        exit(1)
else:
    data = sys.stdin.read()


class WordCount:
    def __init__(self, data):
        self.data = data

    def count_bytes(self):
        return len(self.data.encode("utf-8"))

    def count_lines(self):
        return len(self.data.split("\n")) - 1

    def count_words(self):
        return len(self.data.split())

    def count_characters(self):
        return len(self.data)

    def run(self):
        if args.count:
            print(self.count_bytes(), end=" ")
        elif args.lines:
            print(self.count_lines(), end=" ")
        elif args.words:
            print(self.count_words(), end=" ")

        elif args.characters:
            print(self.count_characters(), end=" ")

        else:
            print(
                f"Bytes: {self.count_bytes()}",
                f"Lines: {self.count_lines()}",
                f"Words: {self.count_words()}",
                f"Characters: {self.count_characters()}",
                end=" ",
            )
        if args.filename:
            print(args.filename, end=" ")
        print()


WordCount(data).run()
