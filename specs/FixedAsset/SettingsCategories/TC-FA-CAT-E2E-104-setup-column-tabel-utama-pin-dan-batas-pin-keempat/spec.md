---
id: TC-FA-CAT-E2E-104-setup-column-tabel-utama-pin-dan-batas-pin-keempat
title: "Setup Column Tabel Utama: Pin Kolom Membekukan Kolom saat Scroll Horizontal dan Batas Pin Keempat"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-357
  - TC-FA-CAT-358
coverage:
  web: automated
---

# Setup Column Tabel Utama: Pin Kolom Membekukan Kolom saat Scroll Horizontal dan Batas Pin Keempat

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMany (Pre-setup #24), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #24 (CatMany), hanya dibaca dan tidak diubah: 30 kategori L1 `Seed Cat 01` sampai `Seed Cat 30`. Seed client disediakan tim FE/BE (lihat Hook suite di `suite.md`); fixture `fixtures/settings-categories.json` disediakan tim FE.
- Lebar viewport diatur cukup sempit sehingga tabel utama dapat di-scroll horizontal (langkah 1).
- Kolom untuk langkah berulang (langkah 2 sampai 13):

  | Kolom |
  |---|
  | `Category` |
  | `Code` |
  | `Total Asset` |
  | `Modified By` |
  | `Last Updated` |

- State yang diubah spec: konfigurasi Pin kolom tabel utama (disimpan lewat `[Save]`). Hook `after` memulihkannya dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Flag Guided Tooltip halaman Categories di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-357: Pin kolom membekukan kolom saat scroll horizontal dan persist

1. Atur lebar viewport sehingga tabel utama dapat di-scroll horizontal
2. Klik header Actions (⋯) > `Setup Column...`
3. Klik icon Pin pada kolom `Category`
4. Klik `[Save]`
5. Scroll tabel secara horizontal
6. Verifikasi kolom `Category` tetap di kiri saat scroll horizontal
7. Tekan F5
8. Verifikasi Pin kolom `Category` bertahan setelah F5
9. Klik header Actions (⋯) > `Setup Column...`
10. Unpin kolom `Category`
11. Klik `[Save]`
12. Scroll tabel secara horizontal
13. Verifikasi kolom `Category` ikut scroll
14. Ulangi langkah 2 sampai 13 untuk setiap kolom lain pada tabel Prerequisites (`Code`, `Total Asset`, `Modified By`, `Last Updated`)

### TC-FA-CAT-358: Pin ke-4 dibatasi

15. Klik header Actions (⋯) > `Setup Column...`
16. Klik icon Pin pada kolom `Category`
17. Klik icon Pin pada kolom `Code`
18. Klik icon Pin pada kolom `Total Asset`
19. Hover icon Pin kolom keempat `Modified By`
20. Verifikasi icon Pin kolom `Modified By` disabled
21. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
22. Klik icon Close (✕)

## Notes

- Langkah berulang: langkah 2 sampai 13 diulang untuk lima kolom pada tabel Prerequisites (idiom "Untuk setiap baris tabel", butir 8b.7); `Verifikasi` tetap satu per klausa. Hitungan dengan ekspansi sekitar 62 langkah. Alasan: blok per kolom satu halaman, satu dataset, satu kelas harness, dan berdiri sendiri; kegagalan satu kolom tidak membuat kolom lain kehilangan makna, dan kelima blok adalah bentuk TC-357 itu sendiri.
- Langkah penghubung (S-03): langkah 1 (viewport), 22 (menutup popup tanpa Save; Pin tiga kolom pada TC-358 tidak disimpan).
- Temuan untuk QA:
  - TC-357 tidak menyebut lebar viewport yang membuat tabel overflow horizontal; spec memakai langkah 1 dan kemampuan itu dicatat sebagai kebutuhan tim FE.
  - Unpin ditulis pada popup Setup Column yang dibuka ulang (langkah 9) karena TC menulis "unpin ... lalu Save" sesudah F5.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
