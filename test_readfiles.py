import unittest
import readfiles


class TestReadFiles(unittest.TestCase):

    def test_get_data(self):
        # test case to confirm tat we are gettin data from the file

        with open("test.txt", "r") as handle:
            data = handle.read()
            self.assertEqual(data, readfiles.read_file("test.txt"))

    def test_nonfile(self):

        # test t confirm that an exception is raised when the wrong file is inputted
        self.assertEqual(None, readfiles.read_file("tests.txt"))

    def test_single_word(self):
        with open("test.txt", "r") as handle:
            data = handle.read()
            counter = 0
            for word in data.split():
                if word == 'Python':
                    counter += 1
                    return counter
                    self.assertEqual(
                        counter, readfiles.single_word("test.txt"))

    def test_lines(self):
        with open("test.txt", "r") as handle:
            data = handle.readlines()
            self.assertEqual(data, readfiles.line_number("test.txt"))

    def test_longest_number(self):
        with open("test.txt", "r") as handle:
            data = handle.read()
            results = []
            for x in data.split():
                word_length = len(x)
                if word_length == 16:
                    word_length = x
                    results.append(word_length)
                    return results
                    self.assertEqual(
                        results, readfiles.longest_number("test.txt"))


if __name__ == '__main__':
    unittest.main(verbosity=2)
