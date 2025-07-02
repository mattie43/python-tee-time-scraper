from fastapi import FastAPI, Request
from playwright.async_api import async_playwright
import asyncio

app = FastAPI()

@app.get("/testing")
async def testing():
    return {
        "content": "Successful GET for testing page"
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

async def test_scrape(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        html = await page.content()
        await page.pause()
        await browser.close()
        return html

# Test run
if __name__ == "__main__":
    asyncio.run(test_scrape("https://example.com"))