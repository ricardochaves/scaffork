import unittest

from scaffork.base_64 import get_base_64


class TestBase64(unittest.TestCase):
    def test_base_64_from_url(self):
        url = "https://raw.githubusercontent.com/scaffork/scaffork/master/.mdlrc"
        base = get_base_64(url)
        self.assertEqual("cnVsZXMgIn5NRDAxMyI=", base)

    def test_base_64_from_file(self):
        f = "./tests/data/.mdlrc"
        base = get_base_64(f)
        self.assertEqual("cnVsZXMgIn5NRDAxMyI=", base)
