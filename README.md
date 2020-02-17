# sogou-tr-async-free ![Python3.6|3.7 package](https://github.com/ffreemt/sogou-tr-async-free/workflows/Python3.6%7C3.7%20package/badge.svg)[![codecov](https://codecov.io/gh/ffreemt/sogou-tr-async-free/branch/master/graph/badge.svg)](https://codecov.io/gh/ffreemt/sogou-tr-async)[![PyPI version](https://badge.fury.io/py/sogou-tr-async-free.svg)](https://badge.fury.io/py/sogou-tr-async-free)
Sogou translate for free with async and proxy support

### Installation

```pip install -U sogou-tr-async-free```

To validate installation
```
python -c "import sogou_tr_async; print(sogou_tr_async.__version__)"
0.0.1
```

### Usage

```
import asyncio
from sogou_tr_async import sogou_tr_async

res = asyncio.get_event_loop().run_until_complete(sogou_tr_async('test this and that'))
print(res)
# '测试这个和那个'

tests = [f'test {elm}' for elm in [1, 3, 4]]
coros = [sogou_tr_async(elm) for elm in tests]

loop = asyncio.get_event_loop()
res = loop.run_until_complete(asyncio.gather(*coros))
print(res)
# ['测试1', '测试3', '测试4']

```
Note that sogou translate seems to have a very strict rate limit policy. Hence, proxies must be used for batch translation. For example,
```
import asyncio
from sogou_tr_async import sogou_tr_async

tests = [f'test {elm}' for elm in [1, 3, 4]]
proxies = [proxy1, proxy2, proxy3]
coros = [sogou_tr_async(elm, proxy=proxies[idx]) for idx, elm in enumerate(tests)]

loop = asyncio.get_event_loop()
res = loop.run_until_complete(asyncio.gather(*coros))

```

### Acknowledgments

* Thanks to everyone whose code was used
