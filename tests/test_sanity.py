''' sanity check
'''
import pytest

from sogou_tr_async import sogou_tr_async


@pytest.mark.asyncio
async def test_sanity():
    ''' sanity check '''
    await sogou_tr_async()
    assert 1
