from fastapi import FastAPI, Request
from playwright.async_api import async_playwright
import asyncio

app = FastAPI()

@app.get("/test")
async def test():
    return {
        "content": "Successful GET from test endpoint"
    }

@app.post("/scrape")
async def scrape(request: Request):
    data = await request.json()
    url = data.get("url")

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        html = await page.content()
        await browser.close()
        return {"html": html}

"""
Local testing commands
"""

async def local_scrape_testing():
    url = "https://pebble-creek-golf-club-v2.book.teeitup.com/?course=18302&date=2025-07-01&max=9999"
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)

        locator = page.get_by_role("gridcell", name="6", exact=True)
        await locator.click()

        # query = await page.query_selector(".MuiPickersDay-root")
        # print(element)
        # await page.get_by_role("button", name="6").click()
        await page.pause()
        # await browser.close()

# Test run
if __name__ == "__main__":
    asyncio.run(local_scrape_testing())