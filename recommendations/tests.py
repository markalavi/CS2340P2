from django.test import SimpleTestCase
from recommendations.scoring import candidate_score

class CandidateScoreTests(SimpleTestCase):
    
    def test_partial_skill_match(self):
        required_skill_ids = {1, 2}
        candidate_skill_ids = {1, 3, 4}
        expected_score = 0.5
        self.assertEqual(expected_score, candidate_score(required_skill_ids, candidate_skill_ids))
        
    def test_full_match(self):
        required_skill_ids = {1, 2}
        candidate_skill_ids = {1, 2, 3}
        expected_score = 1.0
        self.assertEqual(expected_score, candidate_score(required_skill_ids, candidate_skill_ids))
        
    def test_no_match(self):
        required_skill_ids = {1, 2, 3}
        candidate_skill_ids = {4, 5, 6}
        expected_score = 0.0
        self.assertEqual(expected_score, candidate_score(required_skill_ids, candidate_skill_ids))