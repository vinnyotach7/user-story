import unittest
from app.models import Comment,Pitch, User
from app import db

class CommentTest(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_comment = Comment("This is a new comment")


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comments,"This is a new comment")
      
    def test_save_pitch(self):
        """
        To tests on whether comments are being saved
        """
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)