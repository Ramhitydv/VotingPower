# test_votingpower.py
"""
Tests for VotingPower module.
"""

import unittest
from votingpower import VotingPower

class TestVotingPower(unittest.TestCase):
    """Test cases for VotingPower class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VotingPower()
        self.assertIsInstance(instance, VotingPower)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VotingPower()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
