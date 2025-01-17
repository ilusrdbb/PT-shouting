import asyncio
import random

from aiohttp import ClientSession
from tenacity import retry, stop_after_attempt

from utils import config, log


@retry(stop=stop_after_attempt(3))
async def get(url: str, params: dict, headers: dict, session: ClientSession) -> str:
    if config.read('sleep_time') > 0:
        await asyncio.sleep(random.random() * config.read('sleep_time'))
    proxy = config.read('proxy_url') if config.read('proxy_url') else None
    timeout = config.read('time_out')
    try:
        res = await session.get(url=url, headers=headers, params=params, proxy=proxy, timeout=timeout)
        if not res.status == 200:
            raise Exception()
        res_text = await res.text()
        return res_text
    except Exception:
        log.info("%s 请求失败！" % url)
        return None