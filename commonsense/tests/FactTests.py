from commonsense.logical_classes import Fact
import pandas as pd
import unittest

class TestFact(unittest.TestCase):

    def test_initialization(self):
        fact = Fact('penguin', 'isA', 'bird')
        self.assertTrue(fact.subject == 'penguin', 'Subject incorrectly initialized in fact')
        self.assertTrue(fact.predicate == 'isA', 'Predicate incorrectly initialized in fact')
        self.assertTrue(fact.object == 'bird', 'Object incorrectly initialized in fact')
        self.assertTrue(fact.reason is None, 'Reason incorrectly initialized in fact')
        self.assertTrue(fact.score == 1.0, 'Score incorrectly initialized in fact')

        pass

    def test_get_infix_fact_list(self):
        fact = Fact('penguin', 'isA', 'bird')
        infixList = fact.get_infix_fact_list()

        self.assertTrue(len(infixList) == 3, 'list of incorrect size returned by get_infix_fact_list')
        self.assertTrue(infixList[0] == [fact.subject, fact.predicate,
                                 fact.object], 'Incorrect value, should be of the following form [subject, predicate, object]')
        self.assertTrue(infixList[1] == fact.reason, 'Incorrect value, should be fact reason')
        self.assertTrue(infixList[2] == fact.score, 'Incorrect value, should be fact score')

        pass

    def test_to_data_frame(self):
        fact = Fact('penguin', 'isA', 'bird')
        dataframe = fact.to_data_frame()

        self.assertTrue(type(dataframe) is pd.DataFrame, 'to_data_frame returned an incorrect type')

        pass

if __name__ == "__main__":
    unittest.main()
