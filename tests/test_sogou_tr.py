''' test translate hellow world '''
import pytest
# import asyncio
from time import sleep

from loguru import logger

from sogou_tr_async import sogou_tr_async


@pytest.mark.asyncio
async def test_empty():
    ''' async test empty '''
    text = ''
    trtext = await sogou_tr_async(text)
    assert trtext == ''


@pytest.mark.asyncio
async def test_same_from_to():
    ''' async test same_from_to '''
    text = 'text'
    trtext = await sogou_tr_async(text, 'en', 'en')
    assert trtext == text


@pytest.mark.sogou
@pytest.mark.asyncio
async def test_auto_from_to():
    ''' async test auto_from_to '''
    text = 'text'
    sleep(3)  # needed to circumpt
    trtext = await sogou_tr_async(text, 'auto', 'auto')
    sleep(3)
    trtext1 = await sogou_tr_async(text, 'auto', 'zh')
    assert trtext == trtext1


@pytest.mark.sogou
@pytest.mark.asyncio
async def test_from_chinese():
    ''' async test from_chinese '''
    text = '测试'
    sleep(3)
    trtext = await sogou_tr_async(text, 'chinese', 'en')
    sleep(3)
    trtext1 = await sogou_tr_async(text, 'zh', 'en')
    assert trtext == trtext1


@pytest.mark.sogou
@pytest.mark.asyncio
async def test_to_chinese():
    ''' async test to_chinese '''
    text = 'test'
    sleep(3)
    trtext = await sogou_tr_async(text, 'en', 'chinese')
    sleep(3)
    trtext1 = await sogou_tr_async(text, 'en', 'zh')
    assert trtext == trtext1


@pytest.mark.sogou
@pytest.mark.asyncio
async def test_fuzz_from():
    ''' async test fuzzy from '''
    text = 'test'
    sleep(3)
    trtext = await sogou_tr_async(text, 'enn', 'zh')
    sleep(3)
    trtext1 = await sogou_tr_async(text, 'en', 'zh')
    assert trtext == trtext1


@pytest.mark.asyncio
async def test_fuzz_to():
    ''' async test fuzzy to '''
    text = 'test'
    sleep(3)
    trtext = await sogou_tr_async(text, 'en', 'zhh')
    sleep(3)
    trtext1 = await sogou_tr_async(text, 'en', 'zh')
    assert trtext == trtext1


@pytest.mark.asyncio
async def test_debug_true():
    ''' async test fuzzy from '''
    text = 'test'
    sleep(3)
    trtext = await sogou_tr_async(text, 'en', 'zh', debug=1)
    assert trtext[1] is None


@pytest.mark.asyncio
async def test_abc():
    ''' async test fuzzy from '''
    text = 'test abc'
    sleep(3)
    trtext = await sogou_tr_async(text, 'en', 'zh')
    assert '测试' in trtext
