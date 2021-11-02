import os
import unittest
import main
from dotenv import load_dotenv

load_dotenv()


class TestMainFunctions(unittest.TestCase):
    def test_get_topics_correct_input(self):
        topic1 = "Elon"
        topic2 = "Bezos"

        topics = main.get_topics()

        self.assertIsInstance(topics, list)
        self.assertEqual(len(topics), 2)
        self.assertEqual(topics[0], "Elon")
        self.assertEqual(topics[1], "Bezos")

    def test_get_topics_zero_topics(self):
        topics = main.get_topics()
        self.assertIsInstance(topics, str)
        self.assertEqual(
            topics,
            "\nIt seems like you didn't enter anything to compare. Please enter 2 items.\n"
        )

    def test_get_topics_one_topic(self):
        topics = main.get_topics()
        self.assertIsInstance(topics, str)
        self.assertEqual(
            topics,
            "\nAh... It looks like you only entered one thing to compare. Please enter another item with it.\n"
        )

    def test_get_topics_three_topics(self):
        topics = main.get_topics()
        self.assertIsInstance(topics, str)
        self.assertEqual(
            topics,
            "\nWoah! Someone is ambitious... this can only handle 2 items at a time.\n"
        )
