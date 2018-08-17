from person_registry import * 

import unittest

class TestPersonRegistry(unittest.TestCase):

    def test_getting_unregistered_date(self):
        pr =  PersonRegistry()
        self.assertEqual(pr.get_birh_date('joe'), None)
    
    def test_getting_registered_date(self):
        pr =  PersonRegistry()
        pr.add_person('jake','2001-12-01')
        self.assertEqual(pr.get_birh_date('jake'), '2001-12-01')

    def test_getting_removed_date(self):
        pr =  PersonRegistry()
        pr.add_person('jassie','2001-12-01')
        pr.remove_person('jassie')
        self.assertEqual(pr.get_birh_date('jassie'), None)   
 
    def test_getting_updated_date(self):
        pr =  PersonRegistry()
        pr.add_person('jake','2001-12-01')
        pr.add_person('jake','2001-12-23')
        self.assertEqual(pr.get_birh_date('jake'), '2001-12-23')

if __name__ == '__main__':
    unittest.main()

