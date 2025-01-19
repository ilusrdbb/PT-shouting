import datetime

import aiohttp
from utils import config, request, log


class Process(object):

    def __init__(self):
        self.site = None
        self.session = None
        self.header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "",
            "Accept-Language": "zh-CN,zh;q=0.9,zh-HK;q=0.8,en-US;q=0.7,en;q=0.6",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        }
        self.params = {
            "shout": "我喊",
            "sent": "yes",
            "type": "shoutbox"
        }

    async def run(self):
        # 读取有cookie值的站点
        sites = [{"name": key, "cookie": value} for key, value in config.read("cookie").items() if value]
        for site_info in sites:
            self.header["Cookie"] = site_info["cookie"]
            self.site = site_info["name"]
            jar = aiohttp.CookieJar(unsafe=True)
            conn = aiohttp.TCPConnector(ssl=False)
            async with aiohttp.ClientSession(connector=conn, trust_env=True, cookie_jar=jar) as session:
                self.session = session
                if self.site == "qingwa":
                    await self.shouting_qingwa()
                if self.site == "tosky":
                    await self.shouting_tosky()
                if self.site == "cyanbug":
                    await self.shouting_cyanbug()

    async def shouting_qingwa(self):
        url = config.read("shouting_url")[self.site]
        # 青蛙喊上传
        upload_content = config.read("shouting_content")[self.site]["upload"]
        if upload_content:
            self.params["shbox_text"] = upload_content
            res = await request.get(url, self.params, self.header, self.session)
            if res and upload_content in res:
                log.info("青蛙喊上传成功！")
            else:
                log.info(res)
        # 青蛙喊下载
        download_content = config.read("shouting_content")[self.site]["upload"]
        if download_content:
            self.params["shbox_text"] = download_content
            res = await request.get(url, self.params, self.header, self.session)
            if res and download_content in res:
                log.info("青蛙喊下载成功！")
            else:
                log.info(res)

    async def shouting_tosky(self):
        url = config.read("shouting_url")[self.site]
        # tosky喊上传
        upload_content = config.read("shouting_content")[self.site]["upload"]
        if upload_content:
            self.params["shbox_text"] = upload_content
            res = await request.get(url, self.params, self.header, self.session)
            if res and upload_content in res:
                log.info("tosky喊上传成功！")
            else:
                log.info(res)
        # tosky喊魔力
        point_content = config.read("shouting_content")[self.site]["point"]
        if point_content:
            self.params["shbox_text"] = point_content
            res = await request.get(url, self.params, self.header, self.session)
            if res and point_content in res:
                log.info("tosky喊魔力成功！")
            else:
                log.info(res)

    async def shouting_cyanbug(self):
        url = config.read("shouting_url")[self.site]
        # 大青虫喊上传
        upload_content = config.read("shouting_content")[self.site]["upload"]
        if upload_content:
            self.params["shbox_text"] = upload_content
            res = await request.get(url, self.params, self.header, self.session)
            if res and upload_content in res:
                log.info("大青虫喊上传成功！")
            else:
                log.info(res)
        # 大青虫喊魔力
        point_content = config.read("shouting_content")[self.site]["point"]
        if point_content:
            self.params["shbox_text"] = point_content
            res = await request.get(url, self.params, self.header, self.session)
            if res and point_content in res:
                log.info("大青虫喊魔力成功！")
            else:
                log.info(res)
        # 当前日期
        day = datetime.date.today().day
        if config.read("shouting_content")[self.site]["month_day"] == day:
            # 彩虹id
            colorful_content = config.read("shouting_content")[self.site]["colorful"]
            if colorful_content:
                self.params["shbox_text"] = colorful_content
                res = await request.get(url, self.params, self.header, self.session)
                if res and colorful_content in res:
                    log.info("大青虫喊彩虹id成功！")
                else:
                    log.info(res)
            # vip
            vip_content = config.read("shouting_content")[self.site]["vip"]
            if vip_content:
                self.params["shbox_text"] = vip_content
                res = await request.get(url, self.params, self.header, self.session)
                if res and vip_content in res:
                    log.info("大青虫喊vip成功！")
                else:
                    log.info(res)