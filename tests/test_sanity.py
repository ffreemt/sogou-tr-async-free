''' sanity check
'''
import pytest  # type: ignore

from sogou_tr_async import sogou_tr_async


@pytest.mark.asyncio
async def test_sanity():
    ''' sanity check '''
    await sogou_tr_async('a')
    assert 1
