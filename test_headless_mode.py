import asyncio
import time
from pyppeteer import launch
from urllib.parse import urlparse

WEBSITE_LIST = ['https://pushlead.net'
                ]

start = time.time()


async def fetch(url):
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})
    await page.goto(f'{url}', {'waitUntil': 'load'})
    await page.screenshot({'path': f'img/{urlparse(url)[1]}.png'})
    # content = await page.evaluate('document.body.textContent', force_expr=True)
    # element = await page.querySelector('title')
    # title = await page.evaluate('(element) => element.textContent', element)
    # print(title)
    await page.close()
    await browser.close()


async def run():
    tasks = []

    for url in WEBSITE_LIST:
        task = asyncio.ensure_future(fetch(url))
        tasks.append(task)

    responses = await asyncio.gather(*tasks)
    # print(responses)


# asyncio.get_event_loop().run_until_complete(fetch(WEBSITE_LIST))
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run())
loop.run_until_complete(future)

print(f'It took {time.time() - start} seconds.')
