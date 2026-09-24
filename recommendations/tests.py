from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from accounts.models import User
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

	def test_no_required_skills(self):
		self.assertEqual(0.0, candidate_score(set(), {1, 2}))


class RecommendationViewTests(TestCase):
	def test_anonymous_user_is_redirected(self):
		response = self.client.get(reverse('recommendations:jobs'))

		self.assertEqual(response.status_code, 302)
		self.assertIn('/accounts/login/', response.url)

	def test_recruiter_is_forbidden(self):
		recruiter = User.objects.create_user(
			username='recruiter',
			password='password123',
			first_name='Test',
			last_name='Recruiter',
			user_type=User.UserType.Recruiter,
		)
		self.client.force_login(recruiter)

		response = self.client.get(reverse('recommendations:jobs'))

		self.assertEqual(response.status_code, 403)
