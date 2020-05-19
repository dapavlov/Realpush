import asyncio
import time

from async_timeout import timeout
from pyppeteer import launch
from urllib.parse import urlparse

from Databases.PostgreSQL import run_server

# _, WEBSITE_LIST = run_server()
WEBSITE_LIST = ['https://testtesttest.icu/index.html']
start = time.time()


async def fetch(url, browser):
    page = await browser.newPage()
    try:
        await page.setViewport({'width': 1980, 'height': 1080})
        await page.goto(f'{url}', {'waitUntil': 'domcontentloaded'})
        # await page.waitForNavigation({'waitUntil': 'networkidle2'})
        # cookies = await page.cookies()
        await page.waitForSelector('iframe', {'visible': 'true'})
        elementHandle = await page.querySelector('iframe')
        frame = await elementHandle.contentFrame()
        # await frame.waitForXPath('/html/body/div', {'timeout': 10000})
        await frame.waitForSelector('div[class="container"]', {'visible': 'true'})
        # await frame.waitFor(10000)
        await frame.waitForSelector('div[class="item"]', {'visible': 'true'})
        await page.screenshot({'path': f'img/{urlparse(url)[1]}.png'})

        # await page.click('#mainMenu > div.menu__item.menu__item_header.open-popup.account-interface > a')
        # await page.type('#session_email', 'admin@adwirk.com')
        # await page.type('#session_password', 'ChD@s8g(@42++26')
        # await page.click('#signinPopup > form > div.form__bottom > div > button')

        # await page.goto('https://pushlead.net/subscriptions/81/edit')
        # await page.waitFor(3000)
        # await page.waitForSelector('body > div > div.content > div > div > form > div:nth-child(6) > div:nth-child(1) > div > span > span.selection > span')
        # await page.click('body > div > div.content > div > div > form > div:nth-child(6) > div:nth-child(1) > div > span')
        # content = await page.evaluate('document.body.textContent', force_expr=True)
        # results = []
        # element = await page.querySelectorAll('subscription[landing]')
        # title = await page.evaluate('(element) => element.textContent', element)
    except TimeoutError:
        print(f'Timeout for: {url}')
    finally:
        await page.close()


async def callback(req):
    print(f'Request: {req.url}')


async def run():
    browser = await launch(headless=True, autoClose=False, args=['--no-sandbox',
                                                                 '--start-maximized,',
                                                                 '--disable-web-security',
                                                                 '--disable-features=IsolateOrigins,site-per-process'])
    tasks = []

    for url in WEBSITE_LIST:
        task = asyncio.ensure_future(fetch(url, browser))
        tasks.append(task)

    responses = await asyncio.gather(*tasks)
    await browser.close()
    print(responses)


loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run())
loop.run_until_complete(future)

print(f'It took {time.time() - start} seconds.')
