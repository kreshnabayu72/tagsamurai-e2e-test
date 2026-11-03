---
id: TC-FA-CAT-E2E-102-setup-column-tabel-utama-overlay-popup-dan-ceklis-kolom
title: "Setup Column Tabel Utama: Overlay Column Visibility, Popup Setup Column, dan Ceklis Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-353
  - TC-FA-CAT-354
  - TC-FA-CAT-355
coverage:
  web: automated
---

# Setup Column Tabel Utama: Overlay Column Visibility, Popup Setup Column, dan Ceklis Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMany (Pre-setup #24), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #24 (CatMany), hanya dibaca dan tidak diubah: 30 kategori L1 `Seed Cat 01` sampai `Seed Cat 30`. Seed client disediakan tim FE/BE (lihat Hook suite di `suite.md`); fixture `fixtures/settings-categories.json` disediakan tim FE.
- Kolom untuk langkah berulang (langkah 13 sampai 16):

  | Kolom |
  |---|
  | `Category` |
  | `Code` |
  | `Total Asset` |
  | `Modified By` |
  | `Last Updated` |

- State yang diubah spec: konfigurasi kolom tabel utama (disimpan lewat `[Save]` pada langkah 20). Hook `after` memulihkannya dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`; konfigurasi kolom tidak diubah spec lain karena disimpan per browser.
- Flag Guided Tooltip halaman Categories di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-353: Screening overlay Column Visibility

1. Klik header kolom Actions (⋯)
2. Verifikasi overlay memuat item `Setup Column...` di bagian bawah
3. Verifikasi daftar kolom Category, Code, Total Asset, Modified By, Last Updated masing-masing dengan checkbox ☑ Hideable (checked, enabled) dan drag handle
4. Verifikasi Checkbox dan Actions tidak muncul sebagai baris di daftar
5. Tutup overlay dengan menekan `Esc`

### TC-FA-CAT-354: Screening popup Setup Column dan Live Preview

6. Klik header Actions (⋯) > `Setup Column...`
7. Verifikasi zona Header: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan icon Close (✕)
8. Verifikasi zona Body: daftar lima kolom dengan checkbox, drag handle, icon Pin, dan Live Preview tabel
9. Verifikasi zona Footer: `[Reset to Default]` dan `[Save]` rata kanan
10. Verifikasi tidak ada `[Cancel]` pada zona Footer

### TC-FA-CAT-355: Ceklis dan unceklis kolom lewat popup

11. Tutup popup Setup Column dengan icon Close (✕)
12. Klik header Actions (⋯) > `Setup Column...`
13. Hilangkan centang kolom `Category`
14. Verifikasi Live Preview menyembunyikan kolom `Category`
15. Centang kembali kolom `Category`
16. Verifikasi Live Preview menampilkan kembali kolom `Category`
17. Ulangi langkah 13 sampai 16 untuk setiap kolom lain pada tabel Prerequisites (`Code`, `Total Asset`, `Modified By`, `Last Updated`)
18. Hilangkan centang kolom `Total Asset`
19. Hilangkan centang kolom `Modified By`
20. Klik `[Save]`
21. Verifikasi kolom `Total Asset` dan `Modified By` tidak ada di tabel
22. Tekan F5
23. Verifikasi kolom `Total Asset` dan `Modified By` tetap tidak ada di tabel (konfigurasi bertahan setelah F5)

## Notes

- Langkah berulang: langkah 13 sampai 16 diulang untuk lima kolom pada tabel Prerequisites (idiom "Untuk setiap baris tabel", butir 8b.7); `Verifikasi` tetap satu per klausa. Hitungan dengan ekspansi sekitar 40 langkah. Alasan: seluruh blok satu halaman, satu dataset, dan satu kelas harness, serta berdiri sendiri; kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Langkah penghubung (S-03): langkah 5 (menutup overlay), 11 (menutup popup), dan 12 (membuka ulang popup untuk TC-355).
- Temuan untuk QA:
  - TC-355 butir a sampai e menyebut hasil "Live Preview" tetapi tidak menyebut cara mengamati preview versus tabel; spec mengasersi preview pada popup dan tabel baru setelah `[Save]` (langkah 21).
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
