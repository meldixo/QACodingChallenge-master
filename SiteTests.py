import unittest
import requests  

# Author:        Melissa Dixon
# Last updated:  2020-09-16 

# To run this test:                  python SiteTests.py
# If requests package is not found:  pip install requests


class SiteTests(unittest.TestCase):

    # set the site to test
    site = 'https://www.google.com'
    # site = 'https://httpstat.us/417'  # FOR TEST DEBUGGING: this site should cause the test to fail

    def test_site_available(self):
        # check whether the test site is available (available sites get a 200 response)
        res = requests.get(self.site, timeout=1)

        # If status code 200 is returned, the site is available
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':

    unittest.main()

