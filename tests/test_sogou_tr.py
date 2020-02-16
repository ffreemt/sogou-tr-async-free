''' test translate hellow world '''
import pytest

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


@pytest.mark.asyncio
async def test_auto_from_to():
    ''' async test auto_from_to '''
    text = 'text'
    trtext = await sogou_tr_async(text, 'auto', 'auto')
    trtext1 = await sogou_tr_async(text, 'auto', 'zh')
    assert trtext == trtext1


@pytest.mark.asyncio
async def test_from_chinese():
    ''' async test from_chinese '''
    text = '测试'
    trtext = await sogou_tr_async(text, 'chinese', 'en')
    trtext1 = await sogou_tr_async(text, 'zh', 'en')
    assert trtext == trtext1


@pytest.mark.asyncio
async def test_to_chinese():
    ''' async test to_chinese '''
    text = 'test'
    trtext = await sogou_tr_async(text, 'en', 'chinese')
    trtext1 = await sogou_tr_async(text, 'en', 'zh')
    assert trtext == trtext1


@pytest.mark.asyncio
async def test_fuzz_from():
    ''' async test fuzzy from '''
    text = 'test'
    trtext = await sogou_tr_async(text, 'enn', 'zh')
    trtext1 = await sogou_tr_async(text, 'en', 'zh')
    assert trtext == trtext1


@pytest.mark.asyncio
async def test_fuzz_to():
    ''' async test fuzzy to '''
    text = 'test'
    trtext = await sogou_tr_async(text, 'en', 'zhh')
    trtext1 = await sogou_tr_async(text, 'en', 'zh')
    assert trtext == trtext1


@pytest.mark.asyncio
async def test_debug_true():
    ''' async test fuzzy from '''
    text = 'test'
    trtext = await sogou_tr_async(text, 'en', 'zh', debug=1)
    assert trtext[1] is None
