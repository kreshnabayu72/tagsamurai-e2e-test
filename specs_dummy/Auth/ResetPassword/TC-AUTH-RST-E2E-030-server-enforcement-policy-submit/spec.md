---
id: TC-AUTH-RST-E2E-030-server-enforcement-policy-submit
title: "Penegakan aturan Password Policy oleh server pada submit Setup New Password (Defense-in-Depth)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-122
  - TC-AUTH-RST-124
coverage:
  web: automated
---

# Penegakan aturan Password Policy oleh server pada submit Setup New Password (Defense-in-Depth)

## Prerequisites

- User belum login (guest); form Setup New Password terbuka dengan token valid.
- Environment uji terisolasi dengan kemampuan pengiriman HTTP request langsung ke endpoint backend (`Mode: mock`).

## Test Steps

### Penolakan oleh server terhadap payload tidak valid (Bypass UI)

1. Kirimkan HTTP request langsung ke endpoint `/confirm` dengan Confirm Password kosong atau tidak cocok
2. Verifikasi server menolak request dengan status HTTP 400 atau 422
3. Kirimkan HTTP request langsung ke endpoint `/confirm` dengan password yang melanggar policy
4. Verifikasi server menegakkan Password Policy secara independen dari validasi browser

## Notes

- Sesuai PRD §6 V-AUTHRST-04 s/d V-AUTHRST-07 dan §9.4.3 Must NOT 5, server memvalidasi password baru secara independen dan menolak payload yang tidak konsisten/melanggar policy tanpa mengonsumsi token reset.
- Spec ini hasil dekomposisi dari `TC-AUTH-RST-E2E-016` (gap GAP-RST-E2E-001): uji enforcement server dipisah dari uji validasi client form Setup New Password.