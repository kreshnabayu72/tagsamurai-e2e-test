---
id: TC-GS-DIV-E2E-021-create-modal-clear-field-reset
title: "Interaksi Form Create: Pengosongan Input Form via Tombol Clear Field Tanpa Menutup Modal"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-64
coverage:
  web: automated
---

# Interaksi Form Create: Pengosongan Input Form via Tombol Clear Field Tanpa Menutup Modal

## Prerequisites

- Login sebagai Role: Total Control
- Buka Modal Create Division dan isi field Division Name dan Code
- User berada di Global Settings > User > Division

## Test Steps

1. Klik `[+ Division]`
2. Centang `Stay on this form after submitting`
3. Isi Division Name `Finance` dan Code `fin@`
4. Tunggu error inline tampil
5. Klik `[Clear Field]`
6. Verifikasi Division Name dan Code kosong
7. Verifikasi Border error dan pesan error inline hilang
8. Verifikasi Modal tetap terbuka dan dialog Unsaved Changes tidak muncul
9. Verifikasi Checkbox `Stay on this form after submitting` tetap tercentang

## Notes

- Memvalidasi fungsi tombol [Clear Field] pada modal Create: mengosongkan seluruh field input tanpa menutup modal, tidak memicu dialog unsaved changes, dan modal tetap terbuka siap diisi ulang (FI-05, PRD §4.4).
- Sumber pemetaan test case granular: TC-GS-DIV-64.
