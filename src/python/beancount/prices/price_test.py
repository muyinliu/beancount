"""Tests for main driver for price fetching.
"""
__author__ = "Martin Blais <blais@furius.ca>"

import textwrap
import datetime
import unittest
import tempfile
import os
from os import path
from unittest import mock
from urllib import request
from urllib import error

from beancount.prices import price
from beancount.prices import find_prices
from beancount.prices.sources import google
from beancount.core.number import D, Decimal
from beancount.utils import test_utils
from beancount.parser import cmptest
from beancount import loader


class TestSetupCache(unittest.TestCase):

    def test_clear_cache_unset(self):
        with mock.patch('os.remove') as mock_remove:
            with tempfile.TemporaryDirectory() as tmpdir:
                price.setup_cache(None, True)
        self.assertEqual(0, mock_remove.call_count)

    def test_clear_cache_not_present(self):
        with mock.patch('os.remove') as mock_remove:
            with tempfile.TemporaryDirectory() as tmpdir:
                filename = path.join(tmpdir, 'cache.db')
                price.setup_cache(filename, True)
                self.assertEqual(0, mock_remove.call_count)
                self.assertTrue(path.exists(filename))

    def test_clear_cache_present(self):
        mock_remove = mock.MagicMock()
        real_remove = os.remove
        def remove(*args):
            mock_remove(*args)
            real_remove(*args)
        with mock.patch('os.remove', remove):
            with tempfile.TemporaryDirectory() as tmpdir:
                filename = path.join(tmpdir, 'cache.db')
                open(filename, 'w')
                price.setup_cache(filename, True)
                self.assertEqual(1, mock_remove.call_count)
                self.assertTrue(path.exists(filename))

    def test_leave_cache(self):
        with mock.patch('os.remove') as mock_remove:
            with tempfile.TemporaryDirectory() as tmpdir:
                filename = path.join(tmpdir, 'cache.db')
                open(filename, 'w')
                price.setup_cache(None, False)
                self.assertEqual(0, mock_remove.call_count)
                self.assertTrue(path.exists(filename))


class TestProcessArguments(unittest.TestCase):

    def test_filename_not_exists(self):
        with test_utils.capture('stderr') as stderr:
            with self.assertRaises(SystemExit):
                args, jobs, _ = test_utils.run_with_args(
                    price.process_args, ['--no-cache', '/some/file.beancount'])

    @test_utils.docfile
    def test_explicit_file__badcontents(self, filename):
        """
        2015-01-01 open Assets:Invest
        2015-01-01 open USD ;; Error
        """
        with test_utils.capture('stderr') as stderr:
            args, jobs, _ = test_utils.run_with_args(
                price.process_args, ['--no-cache', filename])
            self.assertEqual([], jobs)

    def test_filename_exists(self):
        with tempfile.NamedTemporaryFile('w') as tmpfile:
            with test_utils.capture('stderr') as stderr:
                args, jobs, _ = test_utils.run_with_args(
                    price.process_args, ['--no-cache', tmpfile.name])
                self.assertEqual([], jobs)  # Empty file.

    def test_expressions(self):
        with test_utils.capture('stderr') as stderr:
            args, jobs, _ = test_utils.run_with_args(
                price.process_args, ['--no-cache', '-e', 'google/NASDAQ:AAPL'])
            self.assertEqual(
                [find_prices.DatedPrice(
                    'NASDAQ:AAPL', None, None,
                    [find_prices.PriceSource(google, 'NASDAQ:AAPL', False)])], jobs)


class TestClobber(cmptest.TestCase):

    @loader.load_doc()
    def setUp(self, entries, _, __):
        """
          ;; Existing file.
          2015-01-05 price HDV                                 75.56 USD
          2015-01-23 price HDV                                 77.34 USD
          2015-02-06 price HDV                                 77.16 USD
          2015-02-12 price HDV                                 78.17 USD
          2015-05-01 price HDV                                 77.48 USD
          2015-06-02 price HDV                                 76.33 USD
          2015-06-29 price HDV                                 73.74 USD
          2015-07-06 price HDV                                 73.79 USD
          2015-08-11 price HDV                                 74.19 USD
          2015-09-04 price HDV                                 68.98 USD
        """
        self.entries = entries

        # New entries.
        self.price_entries, _, __ = loader.load_string("""
          2015-01-27 price HDV                                 76.83 USD
          2015-02-06 price HDV                                 77.16 USD
          2015-02-19 price HDV                                  77.5 USD
          2015-06-02 price HDV                                 76.33 USD
          2015-06-19 price HDV                                    76 USD
          2015-07-06 price HDV                                 73.79 USD
          2015-07-31 price HDV                                 74.64 USD
          2015-08-11 price HDV                                 74.20 USD ;; Different
        """, dedent=True)

    def test_clobber_nodiffs(self):
        new_price_entries, _ = price.filter_redundant_prices(self.price_entries, self.entries,
                                                             diffs=False)
        self.assertEqualEntries("""
          2015-01-27 price HDV                                 76.83 USD
          2015-02-19 price HDV                                  77.5 USD
          2015-06-19 price HDV                                    76 USD
          2015-07-31 price HDV                                 74.64 USD
        """, new_price_entries)

    def test_clobber_diffs(self):
        new_price_entries, _ = price.filter_redundant_prices(self.price_entries, self.entries,
                                                             diffs=True)
        self.assertEqualEntries("""
          2015-01-27 price HDV                                 76.83 USD
          2015-02-19 price HDV                                  77.5 USD
          2015-06-19 price HDV                                    76 USD
          2015-07-31 price HDV                                 74.64 USD
          2015-08-11 price HDV                                 74.20 USD ;; Different
        """, new_price_entries)



# FIXME: TODO - Behavior to be implemented and tested.
"""
    parser.add_argument('-t', '--always-invert', action='store_true',
                        help=("Never just swap currencies for inversion, invert the actual "
                              "rate when necessary, so that all price definitions are in "
                              "the expected order"))
"""


__incomplete__ = True
