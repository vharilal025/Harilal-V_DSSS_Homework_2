import unittest
from math_quiz import produce_random_integer, choose_random_operator,make_maths_question

class TestMathGame(unittest.TestCase):

    def test_produce_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = produce_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_choose_random_operator(self):
        # Test if the chosen operator is one of the specified operators
        operators = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random values
            operator = choose_random_operator()
            self.assertIn(operator, operators)

    def test_make_maths_question(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (9, 5, '-', '9 - 5', 4),
            (3, 6, '*', '3 * 6', 18),
            
        ]

        for number1, number2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = make_maths_question(number1, number2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
