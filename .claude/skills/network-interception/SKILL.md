---
name: network-interception
description: The Spectra.intercept() API for deterministic network mocking in TestSpectra — InterceptRule/MockResponse/MockHandle shapes, respondOnce vs respondWith sequential polling, aborting requests, and waitForCall/callCount assertions. Use whenever a test needs to mock, stub, or assert on an API call instead of hitting the real backend.
---

# Skill: Network Interception (`Spectra.intercept`)

Use this skill whenever a test needs deterministic control over a network response — mocking an
API, simulating an error, or asserting a call happened — rather than depending on a real backend.

---

## 1. Rule & Handle Shapes

```typescript
interface InterceptRule {
  url: string | RegExp; // supports glob, e.g. '**/api/v1/payments/charge'
  method?: 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH' | 'ALL';
  response?: MockResponse | ((request: InterceptedRequest) => MockResponse | Promise<MockResponse>);
}

interface MockResponse {
  status?: number; // default: 200
  headers?: Record<string, string>;
  body?: any;
  delayMs?: number;
}

interface MockHandle {
  respondWith(response: MockResponse): this; // default response for all subsequent matches
  respondOnce(response: MockResponse): this; // one-time FIFO-queued response
  abort(errorCode?: 'Failed' | 'Aborted' | 'TimedOut' | 'ConnectionReset'): this;
  waitForCall(options?: { timeout?: number; count?: number }): Promise<InterceptedRequest>;
  readonly callCount: number;
  readonly calls: InterceptedRequest[];
}
```

`Spectra.intercept(rule)` is `async` and returns a `MockHandle` — always `await` it before
interacting with the UI that triggers the call.

---

## 2. Pattern: Single-Shot Static Mock

```typescript
it('should mock payment failure response gracefully', async () => {
  const paymentMock = await Spectra.intercept({
    url: '**/api/v1/payments/charge',
    method: 'POST',
    response: {
      status: 402,
      headers: { 'content-type': 'application/json' },
      body: { error: 'insufficient_funds', message: 'Your card was declined due to insufficient funds.' },
    },
  });

  await CheckoutPage.submitPaymentButton.click();

  await paymentMock.waitForCall({ timeout: 5000 });
  expect(paymentMock.callCount).toBe(1);

  await CheckoutPage.errorBanner.shouldBeVisible();
  await CheckoutPage.errorBanner.shouldContainText('insufficient funds');
});
```

---

## 3. Pattern: Multi-Response Sequential Polling

Use `respondOnce` (FIFO queue, consumed one per matching request) plus a trailing `respondWith`
default for status-polling / retry flows:

```typescript
it('should poll export job status until completed', async () => {
  const jobMock = await Spectra.intercept({ url: '**/api/v1/export/job-99', method: 'GET' });

  jobMock.respondOnce({ status: 200, body: { status: 'pending' } });
  jobMock.respondOnce({ status: 200, body: { status: 'processing' } });
  jobMock.respondWith({ status: 200, body: { status: 'completed', downloadUrl: '/files/report.pdf' } });

  await ExportPage.startExportButton.click();
  await ExportPage.downloadLink.shouldBeVisible();
});
```

---

## 4. Pattern: Simulating a Network Failure

```typescript
it('should handle offline mode gracefully when sync fails', async () => {
  const syncMock = await Spectra.intercept({ url: '**/api/v1/sync' });
  syncMock.abort('ConnectionReset');

  await DashboardPage.syncButton.click();
  await DashboardPage.offlineBanner.shouldBeVisible();
});
```

---

## 5. Conventions

- Prefer glob URL patterns (`'**/api/v1/...'`) over exact origin strings so mocks survive
  environment/base-URL changes between local, staging, and CI.
- Only mock what the test is actually about — don't blanket-intercept every domain; the linter and
  reviewers expect `monitoredDomains` in `spectra.config.ts` (see the `workspace-structure` skill)
  to reflect real traffic, and over-mocking hides real integration regressions.
- Always assert on the mock (`waitForCall` / `callCount`) when the test's purpose is to verify the
  request was made — don't just assert on UI state and silently hope the mock fired.
- Every real (non-mocked) network call made during a run is separately captured and written to
  `.testspectra/reports/network-resources.json` for post-run diagnostics — you don't need to record
  this yourself.
