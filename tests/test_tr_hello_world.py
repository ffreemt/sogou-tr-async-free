''' test translate hellow world '''
import pytest

from loguru import logger

from sogou_tr_async import sogou_tr_async


@pytest.mark.asyncio
async def test_hello_world():
    ''' async test hello world '''
    text = 'hello world'
    trtext = await sogou_tr_async(text)
    logger.debug(trtext)
    assert '世界' in trtext
