from nose.tools import assert_equal

from main import return_true

class Tests():
	def test_it_should_be_true(self):
		assert_equal(return_true(), True)