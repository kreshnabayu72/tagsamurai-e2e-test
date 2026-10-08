---
id: TC-GS-DIV-E2E-017-create-modal-validasi-field-code-keunikan
title: "Validasi Keunikan Code pada Create: Debounce ~500ms Case-Insensitive Per Entitas"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-48
coverage:
  web: automated
---

# Validasi Keunikan Code pada Create: Debounce ~500ms Case-Insensitive Per Entitas

## Prerequisites

- Login sebagai Role: Total Control
- Division dengan Code "FIN" sudah ada di entitas uji
- User berada di Global Settings > User > Division
- Division `Finance` dengan Code `FIN` sudah ada

## Test Steps

1. Klik `[+ Division]`
2. Isi Division Name `Financial Planning`
3. Ketik `fin` pada Code lalu berhenti mengetik ~500ms
4. Verifikasi Code berubah menjadi `FIN` saat mengetik
5. Verifikasi Setelah debounce ~500ms muncul error inline `Code already exists`

## Notes

- Memvalidasi error V-07 ("Code already exists") saat mengetik kode duplicate case-insensitive (misal "fin") dengan debounce ~500ms (PRD §6, §9.9).
- Sumber pemetaan test case granular: TC-GS-DIV-48.
