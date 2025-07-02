## Installation

1. py -m venv .venv
2. .venv/Scripts/activate
3. pip install -r requirements.txt

## Run server locally

uvicorn main:app --reload --host 0.0.0.0 --port 8080

## Deploying to Fly

flyctl deploy

## Testing script locally

1. Update the `local_scrape_testing` URL to the URL you want to scrape.
2. Install playwright: `playwright install`
3. Run `py main.py`
