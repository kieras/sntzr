import unittest
import re
from sntzr import replacers_fn


class ReplacersFn(unittest.TestCase):
    def test_random_company_name(self):
        """
        Test if random_company_name function generates something like 'Acme'
        """
        pattern = re.compile(r'[\w\d_-]+')
        result = replacers_fn.random_company_name()
        match = re.findall(pattern, result)

        self.assertTrue(len(match) == 1)


    def test_sid(self):
        """
        Test if sid function generates something like 'sid_123ABC12_1'
        """
        pattern = re.compile(r'sid_[0-9a-zA-Z]+_[0-9A-Z]+')
        result = replacers_fn.sid()
        match = re.findall(pattern, result)

        self.assertTrue(len(match) == 1)


    def test_guid(self):
        """
        Test if guid function generates something like 'b9c0cd3a-ed45-8b37-2003-9df67ec3e295'
        """
        pattern = re.compile(r'[A-Fa-f0-9]{8}(?:-[A-Fa-f0-9]{4}){3}-[A-Fa-f0-9]{12}')
        result = replacers_fn.guid()
        match = re.findall(pattern, result)

        self.assertTrue(len(match) == 1)


if __name__ == '__main__':
    unittest.main()