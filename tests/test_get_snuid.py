''' test get_snuid '''

import pytest  # monkeypatch
# import requests
import httpx

from sogou_tr_async import get_snuid


def test_get_snuid():
    ''' test_get_snuid '''
    assert len(get_snuid()) == 32


def test_get_snuid_monkeypatch(monkeypatch):
    ''' test_get_snuid '''

    def raise_():
        raise Exception()

    # monkeypatch.setattr(requests, "get", raise_)
    monkeypatch.setattr(httpx, "get", raise_)
    # test the except branch
    assert get_snuid() == ''
