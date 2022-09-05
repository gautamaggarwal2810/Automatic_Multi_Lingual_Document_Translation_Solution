
import unittest
import os
import json
from workflowCompletionHandler import lambda_handler

class TestWorkflowCompletionHandler(unittest.TestCase):

    def test_workflowCompletionHandler(self):
        print( os.getcwd())
        io = open(os.getcwd() + "/test/workflowCompletedEvent.json","r")
        event = json.load(io)
        lambda_handler( event, "")





if __name__ == '__main__':
    unittest.main()
