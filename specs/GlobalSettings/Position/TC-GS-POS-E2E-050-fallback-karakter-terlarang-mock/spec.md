---
id: TC-GS-POS-E2E-050-fallback-karakter-terlarang-mock
title: Fallback Karakter Terlarang saat DOM Dimanipulasi (Mock)
priority: Medium
caseType: Edge Case
status: draft
sourceTc:
  - TC-GS-POS-36
  - TC-GS-POS-102
coverage:
  web: automated
mock: true
---

# Fallback Karakter Terlarang saat DOM Dimanipulasi (Mock)

## Prerequisites

- Mode: mock
- Menggunakan **mock** (bersama 049).
- Menguji skenario edge case terkait sanitasi/fallback karakter terlarang saat input dimanipulasi di DOM (atau validasi sisi klien yang robust).
- Form Create/Edit Position (field Name).

## Test Steps

### A. Input karakter terlarang via normal typing

1. Buka form Create Position.
2. Masukkan nama dengan karakter terlarang sesuai aturan aplikasi (jika ada daftar karakter terlarang).
3. Coba Submit.
4. Verifikasi validasi client-side menampilkan pesan error atau mencegah submit; tidak ada request dikirim jika invalid.

### B. DOM manipulation simulation (robustness)

5. Simulasikan manipulasi nilai input via DOM (mock scenario) untuk menguji fallback.
6. Verifikasi sistem memiliki fallback: nilai yang tidak valid disanitasi, atau validasi tetap berjalan dan menolak.
7. Pastikan tidak terjadi XSS atau crash UI.
8. Submit dengan nilai hasil manipulasi → harus ditolak oleh validasi (client/server).

### C. Edit form

9. Ulang skenario serupa pada form Edit Position.
10. Verifikasi perilaku konsisten dengan form Create.
11. Verifikasi pesan error konsisten (sesuai TC-GS-POS-36,102).

### D. Boundary & recovery

12. Masukkan nilai valid setelah percobaan invalid → form kembali valid, dapat di-Submit.
13. Verifikasi state form bersih, tidak ada artefak error yang tertinggal.

## Notes

- Fokus pada defensive programming: validasi harus tetap bekerja meski nilai di-set via DOM manipulation.
- Hanya 049 dan 050 memakai mock. Hindari mengubah implementasi production, cukup verifikasi perilaku via test harness/mock.
