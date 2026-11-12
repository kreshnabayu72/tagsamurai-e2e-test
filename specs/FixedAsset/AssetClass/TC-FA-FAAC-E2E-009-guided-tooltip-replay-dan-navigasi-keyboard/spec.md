---
id: TC-FA-FAAC-E2E-009-guided-tooltip-replay-dan-navigasi-keyboard
title: "Guided Tooltip Tab Asset Class: Replay Lewat Tombol [?] dan Navigasi Keyboard Enter dan Panah"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-52
  - TC-FA-FAAC-53
coverage:
  web: automated
---

# Guided Tooltip Tab Asset Class: Replay Lewat Tombol [?] dan Navigasi Keyboard Enter dan Panah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini. Pengecualian atas hook `beforeEach` dan hook suite: spec Guided Tooltip tidak memakai penyetelan flag true oleh hook suite dan membuka layarnya sendiri lewat sidebar sesudah flag diatur; spec mengatur flag `guided_tooltip_seen_fa-asset-class` per blok (langkah 1 dan 10). Hook `after` memulihkan flag ke nilai awal dan mengembalikan sesi ke akun default suite.
- Kemampuan teknis: mengatur, membaca, dan memulihkan flag `guided_tooltip_seen_fa-asset-class` untuk akun Total Control; disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah flag Guided Tooltip akun aktor.

## Test Steps

### TC-FA-FAAC-52: Replay walkthrough lewat tombol question-mark di sebelah Breadcrumb

1. Atur flag `guided_tooltip_seen_fa-asset-class` sudah tersimpan untuk akun Total Control
2. Klik menu Accounting di sidebar
3. Klik tab Asset Class
4. Arahkan kursor ke icon `[?]` tepat di sebelah kanan Breadcrumb
5. Verifikasi tooltip hover icon berbunyi `Show guide`
6. Klik icon `[?]`
7. Verifikasi walkthrough dimulai dari `Step 1 of 8` dengan Title `Set Up in Order`
8. Verifikasi flag `guided_tooltip_seen_fa-asset-class` tetap tersimpan (tidak di-reset) lewat kemampuan baca BE

### TC-FA-FAAC-53: Navigasi keyboard Guided Tooltip dengan Enter, panah kanan, dan panah kiri

9. Klik menu Dashboard di sidebar
10. Atur flag `guided_tooltip_seen_fa-asset-class` belum tersimpan untuk akun Total Control
11. Klik menu Accounting di sidebar
12. Klik tab Asset Class
13. Verifikasi tooltip mendapat keyboard focus
14. Tekan Enter
15. Verifikasi tooltip pindah ke `Step 2 of 8`
16. Tekan panah kanan
17. Verifikasi tooltip pindah ke `Step 3 of 8`
18. Tekan panah kiri
19. Verifikasi tooltip kembali ke `Step 2 of 8`
20. Klik menu Dashboard di sidebar

## Notes

- Langkah penghubung (S-03): langkah 1 dan 10 (mengatur flag sebagai precondition tiap TC), langkah 2 dan 3 serta 11 dan 12 (membuka tab Asset Class lewat sidebar sesudah flag diatur), langkah 9 (pindah halaman agar walkthrough hasil replay tertutup tanpa mengubah flag; perilaku TC-FA-FAAC-55), langkah 20 (pindah halaman agar walkthrough yang masih terbuka tertutup tanpa menyimpan flag, sama dengan langkah 9).
- Temuan untuk QA:
  - TC-FA-FAAC-52 butir c ("Flag seen tidak di-reset") tidak memberi cara cek; spec memakai kemampuan baca BE (langkah 8) tanpa endpoint karangan.
