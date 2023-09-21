# Initial Smoke test_Page loading and Element existence

## Playwright Documentation

*Please spend some time going through the Playwright documentation. Here is the link to the doc below:*

[Playwright Documentation](https://playwright.dev/docs/intro)

## Starting Your Playwright Test

- You should have Node.js/npm already installed.
- To install Playwright, run this command: `npm install -D @playwright/test`
- To install Playwright webdriver,run this command: `npm install playwright`
- The e2e tests should be found in the `./e2e-tests/element-existence` directory
- To run E2E tests with Playwright: 
    1. run: `npm run test` (to run e2e tests to all the supported browsers).
    2. run: `npm run test:chrome` (to run e2e tests solely on chrome browser).

## Generate allure report

*Please spend some time going through the allure-playwright documentation. Here is the link to the doc below:*

[allure-playwright Documentation](https://playwright.dev/docs/intro)

- To generate allure report, run this command: `npm run allure:generate`
- To open allure report, run this command: `npm run allure:open`

## Adding Scripts to Run Tests on the Command Line or Pipeline

- You can add more scripts in the "scripts" object located in the `package.json` file.

## Adding More Tests

- Tests are found in the `e2e-tests/element-existence` directory.
- You can navigate to that directory to add or update tests.
- Classes are defined in the `pages` directory.

## Test Data

- Test data are defined in the `fixture` directory.
- You can navigate to that directory to add or update `test data`.