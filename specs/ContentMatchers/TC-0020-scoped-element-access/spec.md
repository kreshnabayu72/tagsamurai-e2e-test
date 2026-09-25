---
id: TC-0020-scoped-element-access
title: element.get()/getAll() resolves a child scoped to its parent's own subtree
priority: High
caseType: Positive
status: ready-for-automation
coverage:
  web: automated
  mobile: automated
---

# element.get()/getAll() resolves a child scoped to its parent's own subtree

## Test Steps
1. Open the matchers page and assert the overview section is visible
2. From the overview section, resolve the page subtitle via `.get()` and assert it exists — the
   subtitle is a real descendant, so the scoped lookup finds it
3. From the same overview section, resolve the submit button via `.get()` and assert it does NOT
   exist — the submit button lives in a different section entirely, so this only passes if the
   lookup is genuinely scoped to overview's own subtree rather than silently falling back to a
   page-wide match
