---
id: TC-0003-loading-no-result-read-failure
title: Loading empty search result and read failure with retry resilience
priority: High
caseType: Negative
status: ready-for-automation
coverage:
  web: automated
---

# Loading empty search result and read failure with retry resilience

## Prerequisites
- Login as Role: Total Control

## Test Steps

1. Observe loading component while fetching table data
2. Search with non-existent query "zzznotfound"
3. Verify "No results found" empty state appears
4. Simulate fetch failure (500 server error)
5. Verify "Failed to load data" error state and `[Retry]` CTA appear
6. Click `[Retry]` button
7. Verify table recovers and displays data once response succeeds
