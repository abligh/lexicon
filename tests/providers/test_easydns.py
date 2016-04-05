# Test for one implementation of the interface
from lexicon.providers.easydns import Provider
from integration_tests import IntegrationTests
from unittest import TestCase
import pytest

# # Hook into testing framework by inheriting unittest.TestCase and reuse
# # the tests which *each and every* implementation of the interface must
# # pass, by inheritance from define_tests.TheTests
# @pytest.mark.skip(reason="no way of currently testing this, no api key")
# class EasyDnsProviderTests(TestCase, IntegrationTests):
#
#     Provider = Provider
#     provider_name = 'easydns'
#     domain = 'capsulecd.com'
#     provider_opts = {'api_endpoint': 'http://sandbox.rest.easydns.net'}
#     def _filter_headers(self):
#         return ['Authorization']