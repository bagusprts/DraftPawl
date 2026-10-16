# test_draftpawl.py
"""
Tests for DraftPawl module.
"""

import unittest
from draftpawl import DraftPawl

class TestDraftPawl(unittest.TestCase):
    """Test cases for DraftPawl class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DraftPawl()
        self.assertIsInstance(instance, DraftPawl)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DraftPawl()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
