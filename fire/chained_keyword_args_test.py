"""Regression tests for chained argument parsing."""

from fire import core
from fire import testutils


class ChainedKeywordArgumentsTest(testutils.BaseTestCase):

  def testRepeatedKeywordIsLeftForLaterCall(self):
    def fn(param=0):
      return param

    spec = core.inspectutils.GetFullArgSpec(fn)
    kwargs, remaining_kwargs, remaining_args = core._ParseKeywordArgs(
        ['--param=3', 'next', '--param=5'], spec)

    self.assertEqual(kwargs, {'param': '3'})
    self.assertEqual(remaining_kwargs, ['--param=5'])
    self.assertEqual(remaining_args, ['next'])


  def testKeywordAfterFilledPositionalIsLeftForLaterCall(self):
    def fn(param=0):
      return param

    spec = core.inspectutils.GetFullArgSpec(fn)
    kwargs, remaining_kwargs, remaining_args = core._ParseKeywordArgs(
        ['3', 'next', '--param=5'], spec)

    self.assertEqual(kwargs, {})
    self.assertEqual(remaining_kwargs, ['--param=5'])
    self.assertEqual(remaining_args, ['3', 'next'])


if __name__ == '__main__':
  testutils.main()
