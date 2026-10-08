---
id: TC-GS-DIV-E2E-026-create-division-resilience-server-500-timeout-dan-double-submit
title: "Ketahanan Form Create: Guard Double Submit, Kegagalan Server 500, dan Network Timeout Retry"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-67
  - TC-GS-DIV-76
  - TC-GS-DIV-77
coverage:
  web: automated
---

# Ketahanan Form Create: Guard Double Submit, Kegagalan Server 500, dan Network Timeout Retry

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Mode: mock (Spectra.intercept())
- Kebutuhan mock: intercept POST /divisions untuk simulasi 500 dan network timeout
- User berada di Global Settings > User > Division

## Test Steps

### Menutup form Create yang kosong tidak memunculkan dialog Unsaved Changes (TC-GS-DIV-67)

1. Klik `[+ Division]`
2. Klik icon close `[✕]`
3. Verifikasi Modal langsung tertutup
4. Verifikasi Dialog Unsaved Changes tidak muncul

### Create gagal 5xx mempertahankan form dan input (TC-GS-DIV-76)

5. Klik `[+ Division]`
6. Isi Division Name `Planning` dan Code `PLN`
7. Paksa respons simpan 5xx
8. Klik `[Submit]`
9. Verifikasi Muncul toast error: `Error, failed to create division.`
10. Verifikasi Modal tetap terbuka dengan Division Name dan Code dipertahankan
11. Verifikasi Tombol `[Submit]` kembali enabled untuk retry manual
12. Verifikasi Record tidak dibuat

### Create timeout mempertahankan form dan input (TC-GS-DIV-77)

13. Klik `[+ Division]`
14. Isi Division Name `Planning` dan Code `PLN`
15. Buat request simpan melewati timeout klien
16. Klik `[Submit]`
17. Verifikasi Muncul toast error: `Connection problem. Please try again.` dengan tombol `[Try Again]`
18. Verifikasi Modal tetap terbuka dengan input dipertahankan dan `[Submit]` enabled kembali

## Notes

- Memvalidasi pencegahan double-submit di client, penanganan error 500 (form tetap terbuka, input dipertahankan), dan toast connection problem dengan tombol [Try Again] (PRD §4.3, §9.6).
- Sumber pemetaan test case granular: TC-GS-DIV-67, TC-GS-DIV-76, TC-GS-DIV-77.
