---
id: TC-GS-DIV-E2E-036-edit-division-resilience-server-failure-dan-double-submit
title: "Ketahanan Form Edit: Guard Double Submit Save, Penanganan Server 500, dan Network Timeout dengan Tombol Try Again"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-106
  - TC-GS-DIV-110
  - TC-GS-DIV-111
coverage:
  web: automated
---

# Ketahanan Form Edit: Guard Double Submit Save, Penanganan Server 500, dan Network Timeout dengan Tombol Try Again

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Mode: mock (Spectra.intercept())
- Kebutuhan mock: intercept PATCH /divisions untuk simulasi 500 dan timeout
- User berada di Global Settings > User > Division
- Division `Accounting` (Code `ACC`) sudah dibuat (TC-GS-DIV-30)

## Test Steps

### Menutup form Edit tanpa perubahan tidak memunculkan dialog Unsaved Changes (TC-GS-DIV-106)

1. Buka row action baris `Accounting` lalu klik `Edit`
2. Klik icon close `[✕]`
3. Verifikasi Modal langsung tertutup
4. Verifikasi Dialog Unsaved Changes tidak muncul

### Edit gagal 5xx mempertahankan form dan input (TC-GS-DIV-110)

5. Buka row action baris `Accounting` lalu klik `Edit`
6. Ubah Division Name menjadi `Accounting Retry`
7. Paksa respons simpan 5xx
8. Klik `[Save]`
9. Verifikasi Muncul toast error: `Error, failed to update division.`
10. Verifikasi Modal tetap terbuka dengan input dipertahankan dan `[Save]` enabled kembali
11. Verifikasi Perubahan tidak tersimpan

### Edit timeout mempertahankan form dan input (TC-GS-DIV-111)

12. Buka row action baris `Accounting` lalu klik `Edit`
13. Ubah Division Name menjadi `Accounting Retry`
14. Buat request simpan melewati timeout klien
15. Klik `[Save]`
16. Verifikasi Muncul toast error: `Connection problem. Please try again.` dengan tombol `[Try Again]`
17. Verifikasi Modal tetap terbuka dengan input dipertahankan dan `[Save]` enabled kembali

## Notes

- Memvalidasi guard double submit pada tombol [Save], penanganan error 500, dan toast timeout "Connection problem. Please try again." + [Try Again] (PRD §4.3, §9.6).
- Sumber pemetaan test case granular: TC-GS-DIV-106, TC-GS-DIV-110, TC-GS-DIV-111.
