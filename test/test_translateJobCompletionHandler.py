
import unittest
import os
import json
from translateJobCompletionHandler import lambda_handler

class TestTranslateJobCompletionHandler(unittest.TestCase):

    os.environ["FLOW_DEF_ARN"] = "arn:aws:sagemaker:us-east-1:883228185105:flow-definition/translate-a2i-hrw-custom"

    def test_translateJobCompletionHandler(self):
        event = '{"jobId": "512dfe4c71ca6e1ef2a50b9220dcb870"}'
        lambda_handler( json.loads(event), "")





if __name__ == '__main__':
    unittest.main()
