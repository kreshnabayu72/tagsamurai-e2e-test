---
id: TC-GS-USER-E2E-071-security-defense-in-depth-xss-dan-sql-sanitasi
title: "Security: Sanitasi script XSS dan keyword SQL injection pada form dan pencarian"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-980
  - TC-GS-USER-981
  - TC-GS-USER-982
coverage:
  web: automated
---

# Security: Sanitasi script XSS dan keyword SQL injection pada form dan pencarian

## Prerequisites

- Berada di Global Settings > User > User List

## Test Steps

### Uji Sanitasi Input dan Pencarian

1. Buka modal Create User, masukkan payload script `<script>alert(1)</script>` pada First Name, submit form
2. Verifikasi teks tampil aman sebagai literal string tanpa eksekusi script
3. Ketik payload SQL injection `%' OR 1=1 --` pada search box, verifikasi pencarian ditangani literal tanpa error sistem

## Notes

- Menggabungkan 3 test case granular (TC-GS-USER-980 s.d. TC-GS-USER-982).
