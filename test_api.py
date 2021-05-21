import unittest
import requests 

class TestApi(unittest.TestCase):
    URL = 'http://aszok-api-1.herokuapp.com/'
    AUTH = ('aleksander','szok')
    
    NEW_TEXT = {'text':'example message 3'}
    CHANGE_TEXT = {'text':'example change message 1'}

    def get_text_url(self, text_id):
        return "{}/text/{}".format(TestApi.URL, text_id)
    
    # test GET method
    def test_get_text(self):
        text_id = 1
        r = requests.get(self.get_text_url(text_id))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 3)
        
    @unittest.expectedFailure
    def test_get_text_bad_url(self):
        r = requests.get(TestApi.URL+'/0')
        self.assertEqual(r.status_code, 200)
    
    # test POST method
    def test_post_new_text(self):
        r = requests.post(TestApi.URL + '/text', TestApi.NEW_TEXT, auth = TestApi.AUTH)
        self.assertEqual(r.status_code, 201)      
        
    # test if we get what we post before
#     def test_get_after_post(self):
#         text_id = 13
#         r = requests.get(self.get_text_url(text_id))
#         self.assertDictEqual(TestApi.NEW_TEXT, {'text': r.json()['text']})
    
    # test PUT method
    def test_overwrite_old_text(self):
        text_id = 1
        r = requests.put(self.get_text_url(text_id), TestApi.CHANGE_TEXT, auth = TestApi.AUTH)
        self.assertEqual(r.status_code, 200)
    # test DELETE method
    def test_delete_text(self):
        text_id = 11
        r = requests.delete(self.get_text_url(text_id), auth=TestApi.AUTH)
        self.assertEqual(r.status_code, 204)

if __name__ == '__main__':
    unittest.main()