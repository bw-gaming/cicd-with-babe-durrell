import { blockPage } from "../../fixtures/bjeu-123blackjack";
const { test, expect } = require("@playwright/test");

test.describe('Verify page loading', () => {
    let page;

    test.beforeAll(async ({ browser }) => {
        page = await browser.newPage();
    });

    for (const { path, selectors } of blockPage.block) {
        const url = path;

        for (const selectorObj of selectors) {
            const { displayName, selector } = selectorObj;

            test(`${url}/ Check existence of *${displayName}*`, async () => {
                await page.goto(blockPage.baseUrl + path);
                const elementExists = await page.locator(selector).count() > 0;
                if (elementExists) {
                    console.log(`Selector ${displayName} exists`);
                } else {
                    console.log(`Selector ${displayName} does not exist`);
                }
                expect(elementExists).toBeTruthy();
            });
        }
    }

    test.afterAll(async ({ browser }) => {
        await page.context().close();
    });
});
