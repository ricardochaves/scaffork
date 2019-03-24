import os
import subprocess
import unittest


class TestSedFiles(unittest.TestCase):
    def test_sed_regx(self):
        file = "/tmp/test_py.txt"
        try:
            os.remove(file)
        except BaseException:
            pass
        with open(file, "w+") as f:
            f.write("[![Maintainability](https://api.codeclimate.com/v1/badges/7bcb7590d6962bee18eb/maintainability)]")

        value = "https://api.codeclimate.com/v1/badges/123/maintainability"
        regex_coverage = r"Maintainability](\(https://api.codeclimate.com/v1/badges/.*?maintainability)"
        subprocess.call([f"perl -p -i -e 's;{regex_coverage};Maintainability]({value};g' {file}"], shell=True)

        with open(file) as f:
            self.assertEqual(f.readlines()[0].replace("\n", ""), f"[![Maintainability]({value})]")

    def test_sed_simple_regx(self):
        file = "/tmp/test_py.txt"
        try:
            os.remove(file)
        except BaseException:
            pass
        with open(file, "w+") as f:
            f.write("ricardo")

        value = "daniel"
        regex_coverage = r"ricar.."
        subprocess.call([f"perl -p -i -e 's;{regex_coverage};{value};g' {file}"], shell=True)

        with open(file) as f:
            self.assertEqual(f.readlines()[0].replace("\n", ""), value)

    def test_sed_complex_regx(self):
        file = "/tmp/test_py.txt"
        try:
            os.remove(file)
        except BaseException:
            pass
        with open(file, "w+") as f:
            f.write("http://www.test/ricardo/paulo")

        value = "daniel"
        regex_coverage = r"http://www.test/ri.*?o/paulo"
        subprocess.call([f"perl -p -i -e 's;{regex_coverage};{value};g' {file}"], shell=True)

        with open(file) as f:
            self.assertEqual(value, f.readlines()[0].replace("\n", ""))
