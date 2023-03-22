from core.config import BASE_URL_CHECK
import aiohttp

async def get(url):
    url = BASE_URL_CHECK + url
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(response.status, await response.read())
                return {'status': 19, 'msg': 'response server ' + str(response.status)}



async def info(ip):
    url = f'/{ip}'
    return await get(url)

async def info2(ip):
    url = f'/{ip}'
    return await get(url)

async def blacklists(ip):
    url = f'/blacklist/{ip}'
    return await get(url)


