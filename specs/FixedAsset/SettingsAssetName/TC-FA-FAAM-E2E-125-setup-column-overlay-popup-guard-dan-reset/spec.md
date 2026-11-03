---
id: TC-FA-FAAM-E2E-125-setup-column-overlay-popup-guard-dan-reset
title: "Setup Column: Overlay Column Visibility, Popup, Reset to Default, Discard, dan Guard Pin"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-402
  - TC-FA-FAAM-403
  - TC-FA-FAAM-426
  - TC-FA-FAAM-429
coverage:
  web: automated
---

# Setup Column: Overlay Column Visibility, Popup, Reset to Default, Discard, dan Guard Pin

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`).
- Kemampuan teknis: drag and drop, scroll horizontal tabel, hapus preferensi kolom di browser (disediakan tim FE).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: konfigurasi kolom tabel utama (preferensi di browser) diubah spec ini. Pemulihan: hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`; kemampuan disediakan tim FE; spec ini terdaftar di `suite.md`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-402: Screening Overlay Column Visibility
1. Arahkan kursor ke header kolom Actions (⋯)
2. Verifikasi tooltip `Column Visibility` tampil
3. Klik header kolom Actions (⋯)
4. Verifikasi overlay memuat 12 kolom data
5. Verifikasi tiap kolom data pada overlay memiliki checkbox `☑`
6. Verifikasi tiap kolom data pada overlay memiliki drag handle
7. Verifikasi kolom Checkbox dan Actions tidak muncul di overlay
8. Verifikasi item `Setup Column...` di bagian bawah overlay
### TC-FA-FAAM-429: Overlay Column Visibility menerapkan perubahan langsung tanpa Save
9. Uncheck `Code` pada overlay
10. Drag `Brand` ke awal pada overlay
11. Verifikasi perubahan langsung diterapkan ke tabel: kolom `Code` hilang dan kolom `Brand` berada di awal
12. Verifikasi overlay tidak memiliki tombol Save
13. Tekan F5
14. Verifikasi perubahan tersimpan: kolom `Code` tetap hilang setelah F5
15. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, lalu tekan F5
### TC-FA-FAAM-403: Screening Popup Setup Column dan live preview
16. Klik header Actions (⋯), lalu klik `Setup Column...`
17. Verifikasi header popup berjudul `Setup Column`
18. Verifikasi deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
19. Verifikasi icon `[✕]` pada header popup
20. Verifikasi body memuat 12 baris kolom `☑ Hideable`
21. Verifikasi tiap baris kolom memiliki drag handle
22. Verifikasi tiap baris kolom memiliki icon Pin
23. Verifikasi Live Preview tampil di body popup
24. Verifikasi footer memuat `[Reset to Default]` dan `[Save]`
25. Verifikasi footer tidak memuat `[Cancel]`
### TC-FA-FAAM-426: Menutup Setup Column dengan [✕] atau Esc membuang perubahan preview
26. Uncheck `Code` pada popup Setup Column
27. Klik `[✕]`
28. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir: kolom `Code` tampil (penutupan dengan `[✕]`)
29. Buka Popup Setup Column dan uncheck `Code`
30. Tekan Esc
31. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir: kolom `Code` tampil (penutupan dengan Esc)

## Notes

- Urutan di spec: overlay (TC-FA-FAAM-402 dan 429) lebih dulu, lalu popup (TC-FA-FAAM-403 dan 426). TC-FA-FAAM-429 menyimpan perubahan tanpa Save, sehingga konfigurasi dipulihkan sesudahnya (S-09).
- Langkah penghubung (aksi tanpa `Verifikasi`): pemulihan konfigurasi kolom setelah TC-FA-FAAM-429, membuka popup, dan menutup popup dengan `[✕]` atau Esc yang membuang perubahan preview (TC-FA-FAAM-426), sehingga tidak ada form dirty yang tertinggal.
- Verifikasi "tidak memiliki tombol Save" (TC-FA-FAAM-429) dan `[Cancel]` (TC-FA-FAAM-403) beranchor Verifikasi elemen lain pada surface yang sama sudah tampil (bagian 8b butir 2).
- Guard satu kolom, batas pin tiga kolom, dan Reset to Default ada di spec 145.
