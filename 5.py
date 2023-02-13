"""Напиши функцию на Python, выполняющую сравнение версий. Условия: 
Return -1 if version A is older than version B 
Return 0 if versions A and B are equivalent 
Return 1 if version A is newer than version B 
Each subsection is supposed to be interpreted as a number, therefore 1.10 > 1.1."""

from distutils.version import LooseVersion
import unittest

def compare_version(first_version: str, second_version: str) -> int:
    if tuple(map(int, (first_version.split(".")))) > tuple(map(int, (second_version.split(".")))):
        return -1
    elif tuple(map(int, (first_version.split(".")))) < tuple(map(int, (second_version.split(".")))):
        return 1
    else:
        return 0

def compare_version_looseversion(first_version: str, second_version: str) -> int:
    if LooseVersion(first_version) > LooseVersion(second_version):
        return -1
    elif LooseVersion(first_version) < LooseVersion(second_version):
        return 1
    else:
        return 0


class TestVersionCompare(unittest.TestCase):
    def test_correct_own_function(self):
        self.assertEqual(compare_version("1.0.0", "1.0.0"), 0)
        self.assertEqual(compare_version("1.0.0", "0.0.9"), -1)
        self.assertEqual(compare_version("1.10", "1.1"), -1)
        self.assertEqual(compare_version("1.0.0", "1.1.1"), 1)

    def test_correct_looseversion(self):
        self.assertEqual(compare_version_looseversion("1.0.0", "1.0.0"), 0)
        self.assertEqual(compare_version_looseversion("1.0.0", "0.0.9"), -1)
        self.assertEqual(compare_version_looseversion("1.10", "1.1"), -1)
        self.assertEqual(compare_version_looseversion("1.0.0", "1.1.1"), 1)


if __name__ == "__main__":
    unittest.main()
