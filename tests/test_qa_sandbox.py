from playwright.sync_api import Page, expect


def test_qa_sandbox_opens(page: Page) -> None:
    page.goto("https://t-qa.ru/trainers/qa-sandbox")
    expect(page.get_by_role("heading", name="QA-песочница", exact=True)).to_be_visible()