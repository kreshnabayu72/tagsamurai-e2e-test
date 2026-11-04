---
id: TC-FA-TDC-E2E-142-isolasi-data-antar-client-daftar-baca-dan-class-code-sama
title: "Isolasi Data Antar Client: Daftar Class, Request Baca, Deactivate, Delete, dan Bulk Deactivate Lintas Client Ditolak serta Class Code yang Sama Boleh Dipakai di Dua Client"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-859
  - TC-FA-TDC-860
  - TC-FA-TDC-861
  - TC-FA-TDC-862
  - TC-FA-TDC-863
  - TC-FA-TDC-864
coverage:
  web: automated
---

# Isolasi Data Antar Client: Daftar Class, Request Baca, Deactivate, Delete, dan Bulk Deactivate Lintas Client Ditolak serta Class Code yang Sama Boleh Dipakai di Dua Client

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI: Total Control pada Client A (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Akun aktor Client B: Total Control pada Client B (dua tenant). Email tidak tertulis di TC dan disediakan tim FE; password lewat `Spectra.env.FA_TC_CLIENTB_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Client B dipakai lewat sesi API aktor (token) untuk membaca status dan memanggil request langsung; sesi UI hanya untuk Client A.
- Login sesi UI Client A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk dua client, Client A dan Client B), sesi API aktor untuk kedua client (token yang tidak dihitung sebagai sesi web) termasuk request langsung ke server, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`. Kemampuan tambahan: pembacaan jumlah entri Changelog class pada Client B lewat fixture BE (disediakan tim FE/BE); endpoint request langsung tidak dikarang (S-13) dan disediakan tim BE.
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus atau dipulihkan di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `clientANb4` | `NB-4` | Client A: Active, Used By 0 |
| `clientBOnly` | `CLIENTB-ONLY` | Client B: Active, Used By 0, tanpa Last Posted Tax Year; tidak ada di Client A; ID class diketahui penguji untuk request langsung (langkah 7 sampai 24) |
| `clientBNb9` | `NB-9` | Client B: sudah ada; Client A tidak memiliki `NB-9` (dipakai pada TC-FA-TDC-864) |

- Urutan: pembacaan UI (TC-FA-TDC-859), request langsung (TC-FA-TDC-860 sampai TC-FA-TDC-863), lalu Create (TC-FA-TDC-864) di akhir karena menambah data (S-10).
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal dan dua client berbagi environment.

## Test Steps

### TC-FA-TDC-859: Daftar class hanya memuat class milik client aktor

1. Ketik Search `CLIENTB-ONLY`, tekan Enter
2. Verifikasi Empty State hasil pencarian `No results found`
3. Klik `(←)` pada kotak Search
4. Verifikasi baris `NB-4` tampil di tabel
5. Verifikasi seluruh baris tabel adalah class milik Client A menurut fixture
6. Verifikasi tabel tidak memuat `CLIENTB-ONLY`

### TC-FA-TDC-860: Request baca langsung class milik client lain tidak mengembalikan data client lain

7. Sesi API aktor Client A: kirim request baca langsung class berdasarkan ID `CLIENTB-ONLY` dengan token aktor Client A
8. Verifikasi respons tidak memuat data class `CLIENTB-ONLY` milik Client B
9. Verifikasi class `CLIENTB-ONLY` tidak ditemukan untuk Client A

### TC-FA-TDC-861: Request langsung Deactivate class milik client lain ditolak

10. Catat baseline jumlah entri Changelog class `CLIENTB-ONLY` pada Client B lewat fixture BE
11. Sesi API aktor Client A: kirim request langsung untuk menonaktifkan class `CLIENTB-ONLY` dengan token aktor Client A
12. Verifikasi server menolak request
13. Sesi API aktor Client B: baca status `CLIENTB-ONLY` dengan token aktor Client B
14. Verifikasi status `CLIENTB-ONLY` tetap Active
15. Verifikasi jumlah entri Changelog class `CLIENTB-ONLY` pada Client B sama dengan baseline langkah 10 (tidak ada entri log baru)

### TC-FA-TDC-862: Request langsung Delete class milik client lain ditolak

16. Sesi API aktor Client A: kirim request langsung untuk menghapus class `CLIENTB-ONLY` dengan token aktor Client A
17. Verifikasi server menolak request
18. Sesi API aktor Client B: baca daftar class dengan token aktor Client B
19. Verifikasi class `CLIENTB-ONLY` tetap ada pada Client B

### TC-FA-TDC-863: Request langsung bulk Deactivate yang mencampur class client lain tidak memproses class client lain

20. Catat baseline jumlah entri Changelog class `CLIENTB-ONLY` pada Client B lewat fixture BE
21. Sesi API aktor Client A: kirim request langsung bulk Deactivate untuk `NB-4` dan `CLIENTB-ONLY` dengan token aktor Client A
22. Sesi API aktor Client B: baca status `CLIENTB-ONLY` dengan token aktor Client B
23. Verifikasi status `CLIENTB-ONLY` tetap Active pada Client B
24. Verifikasi jumlah entri Changelog class `CLIENTB-ONLY` pada Client B sama dengan baseline langkah 20 (tidak ada entri log baru)

### TC-FA-TDC-864: Class Code yang sama boleh dipakai di dua client berbeda

25. Klik `+ Class`
26. Isi form: Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Code `NB-9`, Class Name `Kelompok 9 uji`, Asset Type `Non-building`, Useful Life `10`, Allowed Methods `Straight Line`
27. Klik `[Submit]`
28. Verifikasi muncul toast sukses: `Success, tax depreciation class has been created.`
29. Verifikasi caption `Class code already exists` tidak muncul
30. Ketik Search `NB-9`, tekan Enter
31. Verifikasi baris `NB-9` tampil di tabel Client A dengan Class Name `Kelompok 9 uji`
32. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC-FA-TDC-860, TC-FA-TDC-861, TC-FA-TDC-862, dan TC-FA-TDC-863 adalah TC kelas a (defense-in-depth) dengan Expected respons API; tetap masuk spec FE+BE karena TC granular tetap sumber dan tiap TC tepat satu spec (K-1). Spec ini bukan spec kelas a: TC dikelompokkan di sini karena objek ujinya isolasi dua tenant (kelas c).
- Request langsung (langkah 7, 11, 16, 21): asersi hanya respons server dan state data lewat sesi API aktor atau fixture BE; pengalihan halaman, toast, dan tampilan tidak diasersi (8b.1). Langkah 13, 18, dan 22 adalah sesi API aktor Client B yang hanya membaca.
- Langkah penghubung (S-03): langkah 1 (Search yang dinyatakan langkah TC), langkah 3 (mengosongkan Search; 8b.9), langkah 10 dan 20 (baseline Changelog, S-12, 8b.10), langkah 30 (Search agar baris target ada di halaman teramati; R-16, 8b.13), langkah 32 (mengosongkan Search).
- Langkah 4 dan 5 (anchor): baris `NB-4` yang tampil membuktikan tabel sudah dimuat sebelum asersi universal langkah 5 dan absence langkah 6 (8b.2). Langkah 2 (Empty State hasil Search) adalah anchor sah untuk absence hasil Search.
- Langkah 15 dan 24 (absence log pada Client B): jumlah entri dibandingkan dengan baseline (S-12); respons penolakan langkah 12 dan status Active langkah 23 menjadi anchor bahwa request sudah diproses server. Asersi ini ditulis di spec ini karena TC kelas c ini tidak dimuat spec absence (S-05).
- Langkah 29 (caption tidak muncul): toast sukses langkah 28 menjadi anchor positif bahwa respons server sudah diproses (8b.2).
- Temuan untuk QA:
  - Email akun Total Control Client A dan Client B tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code `NB-4`, `CLIENTB-ONLY`, dan `NB-9` ditulis literal tanpa suffix `{runId}-<NNN>` karena nilai kode itu menjadi objek asersi (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - TC-FA-TDC-860 sampai TC-FA-TDC-863 tidak menyebut status respons (misalnya 403 atau 404) untuk "Server menolak request" atau "tidak ditemukan"; spec mengasersi bahwa request ditolak atau class tidak ditemukan tanpa kode status. Endpoint request langsung tidak disebut TC dan tidak dikarang (S-13).
  - TC-FA-TDC-863 Expected tidak menyebut hasil untuk `NB-4` milik Client A (apakah dinonaktifkan atau seluruh request ditolak); spec tidak mengasersinya (S-01). `NB-4` dipulihkan ke Active di hook `after`.
  - TC-FA-TDC-859 Expected b ("hanya memuat class milik Client A") ditulis sebagai asersi universal dengan anchor baris `NB-4` dan daftar class Client A dari fixture; TC tidak menyebut jumlah baris.
  - TC-FA-TDC-864 Post Condition tidak ada; TC tidak memberi langkah observasi log untuk Client A, sehingga log tidak diasersi.
  - Kolom Automation TC-FA-TDC-859 sampai TC-FA-TDC-864 memuat `Automatable`.
