import unittest
from app.models import Pitch, User
from app import db

class PitchTest(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_pitch = Pitch("This is a new pitch")


    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.comments,"This is a new pitch")
      
    def test_save_pitch(self):
        """
        To tests on whether pitches are being saved
        """
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)