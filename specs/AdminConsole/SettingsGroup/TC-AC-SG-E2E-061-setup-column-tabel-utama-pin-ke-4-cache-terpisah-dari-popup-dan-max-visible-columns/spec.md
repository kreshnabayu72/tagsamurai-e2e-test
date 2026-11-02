---
id: TC-AC-SG-E2E-061-setup-column-tabel-utama-pin-ke-4-cache-terpisah-dari-popup-dan-max-visible-columns
title: "Setup Column Tabel Utama: Pin ke-4 Diblok, Cache Terpisah dari Popup, dan Max Visible Columns"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-220
  - TC-AC-SG-221
  - TC-AC-SG-222
coverage:
  web: automated
---

# Setup Column Tabel Utama: Pin ke-4 Diblok, Cache Terpisah dari Popup, dan Max Visible Columns

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1, nama tampil `Budi Santoso`) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): `Pohon Uji Utama` entitas Principal (Pre-setup #16, #17), node `All Groups` terpilih, 14 group; `Region A` memiliki Total User 5 sehingga popup Users dapat dibuka dari angka Total User baris `Region A`. Konfigurasi sistem (Pre-setup #34): Max Visible Columns 20 (default).
- Kelima kolom data tampil secara default. Spec ini menyembunyikan kolom Total Member lewat Overlay Column Visibility (langkah 11) dan menampilkannya kembali (langkah 19): hook `before` dan `after` spec ini menghapus preferensi kolom tabel di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE; lihat `suite.md`).
- Kemampuan teknis: Fixture BE untuk baseline `Pohon Uji Utama`, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

### TC-AC-SG-220: Pin ke-4 diblok setelah tiga kolom terpin

1. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
2. Pin kolom Group, Total User, dan Total Member
3. Hover ikon Pin kolom Modified By
4. Verifikasi ikon Pin kolom lain disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
5. Unpin kolom Total Member
6. Verifikasi ikon Pin kolom Modified By aktif kembali
7. Klik `[✕]` untuk menutup modal tanpa menyimpan

### TC-AC-SG-221: Pengaturan kolom tabel utama tersimpan terpisah dari tabel popup

8. Klik angka Total User baris `Region A` untuk membuka popup Users
9. Catat daftar kolom popup Users sebagai pembanding
10. Tutup popup Users
11. Klik header kolom Actions `⋯`, lalu hapus centang kolom Total Member
12. Tutup Overlay Column Visibility
13. Klik angka Total User baris `Region A` untuk membuka popup Users
14. Verifikasi kolom popup Users sama dengan daftar pada langkah 9 (hide Total Member di tabel utama tidak memengaruhi kolom popup)
15. Tutup popup Users
16. Refresh browser (F5)
17. Verifikasi kolom Total Member tetap tersembunyi di tabel utama

### TC-AC-SG-222: Max Visible Columns tidak membatasi tabel utama yang hanya memiliki 5 kolom

18. Klik header kolom Actions `⋯`
19. Centang kembali kolom Total Member sehingga seluruh 5 kolom tercentang
20. Verifikasi seluruh 5 kolom dapat dicentang tanpa pesan batas (batas Max Visible Columns 20 tidak tercapai)

## Notes

- Langkah penghubung (S-03): langkah 7 (membatalkan perubahan pin modal, tanpa menyimpan), langkah 9 (membaca daftar kolom popup sebagai baseline), langkah 10, 12, dan 15 (menutup popup/overlay), langkah 19 (memulihkan kolom Total Member sekaligus menjadi aksi "Centang seluruh 5 kolom" TC-222).
- Temuan untuk QA:
  - TC-AC-SG-221: Expected tidak menyebut daftar kolom popup Users yang diharapkan; spec membandingkan kolom popup sebelum dan sesudah hide (langkah 9 dan 14) alih-alih menyebut nama kolom.
  - TC-AC-SG-222: Expected tidak menyebut teks pesan batas yang dimaksud; langkah 20 mengasersi tidak ada pesan batas apa pun yang tampil.
