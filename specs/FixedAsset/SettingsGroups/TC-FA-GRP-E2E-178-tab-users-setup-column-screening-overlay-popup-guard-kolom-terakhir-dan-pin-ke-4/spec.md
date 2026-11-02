---
id: TC-FA-GRP-E2E-178-tab-users-setup-column-screening-overlay-popup-guard-kolom-terakhir-dan-pin-ke-4
title: "Tab Users Setup Column: Screening Overlay dan Popup, Guard Kolom Terakhir, dan Pin ke-4 Diblok"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-630
  - TC-FA-GRP-631
  - TC-FA-GRP-665
  - TC-FA-GRP-1089
coverage:
  web: automated
---

# Tab Users Setup Column: Screening Overlay dan Popup, Guard Kolom Terakhir, dan Pin ke-4 Diblok

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role, dan Custom Field User `Phone {runId}` di-seed per spec lewat sesi API aktor di `before` dan dihapus di `after` (Data Dinamis, disediakan tim FE/BE). Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- Max Visible Columns pada System Limits mengikuti nilai aktif client; spec tidak mengubahnya.
- State yang diubah spec: draf perubahan Setup Column yang tidak disimpan (ditutup lewat `(X)`); tidak ada konfigurasi tersimpan. Keadaan awal: belum ada kolom yang terpin. Pemulihan: hapus preferensi kolom di browser di hook `after` (kemampuan disediakan tim FE).

## Test Steps

1. Klik angka Total User Warehouse A

### TC-630: Screening overlay Column Visibility

2. Hover icon (⋯) di header kolom terakhir
3. Verifikasi tooltip Column Visibility tampil
4. Klik icon (⋯)
5. Verifikasi item `Setup Column...` ada di bagian bawah panel overlay
6. Verifikasi daftar kolom berurutan: Name (Hideable, checked, enabled), Email (Hideable, checked, enabled), Position (Hideable, checked, enabled), Division (Hideable, checked, enabled), Group Role (Hideable, checked, enabled), Activation Status (Curated, unchecked, enabled), Temporary User (Curated, unchecked, enabled), Temporary Until (Curated, unchecked, enabled), TAG (Curated, unchecked, enabled), Custom Field `Phone {runId}` (Curated, unchecked, enabled)
7. Verifikasi tiap baris kolom punya drag handle
8. Tekan Esc untuk menutup overlay

### TC-631: Screening popup Setup Column

9. Klik icon (⋯)
10. Klik [Setup Column]
11. Verifikasi header popup memuat title Setup Column, teks panduan drag/check/pin, dan icon close (X)
12. Verifikasi body memuat daftar kolom Name, Email, Position, Division, Group Role (Hideable, checked, enabled) dan Activation Status, Temporary User, Temporary Until, TAG, Custom Field `Phone {runId}` (Curated, unchecked, enabled) dengan drag handle dan icon Pin
13. Verifikasi Live Preview menampilkan header kolom dan sel data sesuai tabel asli
14. Verifikasi footer memuat [Reset to Default] (text, primary) dan [Save] (filled, success)
15. Verifikasi footer tidak memuat [Cancel]

### TC-665: Guard kolom terakhir yang visible

16. Uncheck seluruh kolom kecuali satu
17. Hover checkbox kolom yang tersisa
18. Verifikasi checkbox kolom terakhir disabled (tetap tampil)
19. Verifikasi tooltip "At least one column must remain visible." tampil
20. Klik (X) untuk menutup popup tanpa menyimpan

### TC-1089: Pin ke-4 diblok

21. Klik icon (⋯), klik [Setup Column]
22. Klik icon Pin Name, Email, dan Position
23. Verifikasi kolom Name, Email, dan Position berstatus terpin
24. Hover icon Pin kolom Division
25. Verifikasi icon Pin kolom Division disabled (tidak dapat diklik, kolom tidak beku)
26. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.` tampil
27. Klik icon Pin Position untuk unpin
28. Hover icon Pin kolom Division
29. Verifikasi icon Pin kolom Division kembali aktif
30. Klik (X) untuk menutup popup tanpa menyimpan

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): menutup overlay dengan Esc setelah TC-630, menutup popup lewat `(X)` setelah TC-665 dan TC-1089 (draf tidak disimpan; modal Setup Column tidak punya [Cancel]), dan membuka ulang overlay dan popup pada TC-1089.
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-630 dan TC-631 menyebut "Custom Field aktif (mis. Phone)"; spec memakai Custom Field `Phone {runId}` (seed spec) sebagai kolom ke-10. TC-665 "uncheck seluruh kolom kecuali satu" tidak menyebut kolom yang tersisa; spec mengikuti TC dan tidak menyebut kolom tertentu.
