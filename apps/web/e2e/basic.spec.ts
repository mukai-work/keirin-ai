import { test, expect } from '@playwright/test';

test('basic flow', async ({ page }) => {
  await page.goto('/');
  await page.waitForSelector('text=Keirin AI');
  const button = page.getByRole('button', { name: '予想開始' });
  await expect(button).toBeEnabled({ timeout: 30000 });
  await button.click();
  await page.waitForSelector('text=選手');
});
