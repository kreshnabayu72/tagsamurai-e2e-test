---
id: TC-AC-ACTS-E2E-080-lintas-permukaan-download-seluruh-baris-dan-hasil-search-filter
title: "Lintas Enam Permukaan: Download Tanpa Search/Filter Mengekspor Seluruh Baris dan dengan Search/Filter Hanya yang Cocok"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-102
  - TC-AC-ACTS-103
coverage:
  web: automated
---

# Lintas Enam Permukaan: Download Tanpa Search/Filter Mengekspor Seluruh Baris dan dengan Search/Filter Hanya yang Cocok

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Tabel "Permukaan yang diuji" (enam permukaan; langkah 1 sampai 14 diulang untuk setiap baris tabel):

| No | Permukaan | Cara membuka |
|---|---|---|
| 1 | Stock List | TAG > Stock |
| 2 | Detail SKU Tab Available | Stock List, row action Detail pada SKU `RFID-ASSET-CORE-R5`, Tab Available |
| 3 | Detail SKU Tab In Use | Detail SKU `RFID-ASSET-CORE-R5`, Tab In Use |
| 4 | Modal Event Log | Detail SKU `RFID-ASSET-CORE-R5`, tombol `[Event Log]` |
| 5 | Approvals Tab Active | Tutup modal Event Log dengan klik (X), lalu Approvals > TAG Stock, Tab Active |
| 6 | Approvals Tab History | Approvals > TAG Stock, Tab History |

- Data uji: tiap permukaan memuat lebih dari 10 baris dengan satu keyword Search dan satu nilai Filter yang menyaring sebagian baris (disiapkan seeding; TC tidak merinci nilainya, lihat Temuan untuk QA). Jumlah total baris (N) tiap permukaan dibaca lewat kemampuan baca BE sebelum Download (8b butir 10, karena permukaan audit trail bersama bertambah selama suite), bukan dari seeding atau halaman tabel.
- Kemampuan teknis disediakan tim FE: pembaca isi berkas CSV yang diunduh (menghitung baris data dan membaca urutan baris), seeding data enam permukaan, dan kemampuan baca BE (jumlah total baris tiap permukaan).
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-102 (diulang per permukaan): Download tanpa Search/Filter mengekspor seluruh baris

1. Buka permukaan sesuai kolom Cara membuka pada tabel "Permukaan yang diuji"
2. Pastikan kotak Search kosong dan Filter bersih pada permukaan itu
3. Catat N total baris permukaan itu lewat kemampuan baca BE
4. Klik Download, pilih Download as CSV
5. Baca berkas CSV yang terunduh
6. Verifikasi jumlah baris data berkas sama dengan N yang dicatat pada langkah 3 (seluruh baris, bukan satu halaman)

### TC-AC-ACTS-103 (diulang per permukaan): Download dengan Search dan Filter hanya mengekspor baris yang cocok

7. Ketik Search keyword yang menyaring sebagian baris, tekan Enter
8. Terapkan Filter yang menyaring sebagian baris
9. Klik Download, pilih Download as CSV
10. Baca berkas CSV yang terunduh
11. Verifikasi tabel menampilkan sedikitnya satu baris hasil Search dan Filter
12. Verifikasi berkas hanya memuat baris hasil Search dan Filter (dan tab aktif)
13. Verifikasi urutan baris berkas sesuai sort aktif tabel
14. Klik `(←)` pada kotak Search dan bersihkan Filter

## Notes

- Mode: FE+BE. Satu TC memuat enam permukaan ("pada setiap permukaan"); satu TC tetap satu spec, jadi langkah 1 sampai 14 diulang untuk setiap baris tabel "Permukaan yang diuji" (8b butir 7, "Untuk setiap baris tabel ... (langkah 1 sampai 14)"). Spec ini melewati sekitar 35 langkah (14 langkah nominal, 84 langkah dengan ekspansi enam permukaan); alasan: semua blok satu kelas harness dan satu dataset, hanya parameter permukaan yang berubah.
- Pembagian spec 080 sampai 083 (satu dataset enam permukaan): gabungan keempat spec berisi 55 langkah nominal dan 330 langkah dengan ekspansi enam permukaan, jauh melewati batas ukuran sekitar 35 langkah, sehingga topik satu dataset dipisah per kelompok TC (bagian 3 prinsip 1, keputusan 2026-10-21): 080 (TC-AC-ACTS-102 dan 103: cakupan baris), 081 (TC-AC-ACTS-104 dan 105: kolom Setup Column), 082 (TC-AC-ACTS-106, 107, dan 110: toast, kegagalan, workbook), 083 (TC-AC-ACTS-108 dan 109: hasil kosong dan isi CSV). Spec ini memuat asersi jumlah baris dan urutan (fungsional); isi byte berkas (kelas f) hanya ada di spec 083.
- Langkah penghubung tanpa awalan Verifikasi (S-03): langkah 2 (memastikan Search/Filter bersih sebagai precondition TC-AC-ACTS-102), langkah 3 (mencatat N lewat BE, S-12), langkah 7 dan 8 (Search dan Filter sebagai aksi TC-AC-ACTS-103; Search dicatat sebagai langkah penghubung menurut R-16), langkah 14 (membersihkan Search/Filter sebelum permukaan berikutnya, S-09). Untuk permukaan 5, kolom "Cara membuka" menutup modal Event Log permukaan 4 lebih dulu (modal menutupi sidebar; hook `afterEach` tidak berjalan antar iterasi).
- Verifikasi tabel menampilkan sedikitnya satu baris (langkah 11) adalah anchor positif untuk asersi universal "hanya baris hasil Search dan Filter" (8b butir 2).
- Temuan untuk QA:
  - TC-AC-ACTS-102 dan TC-AC-ACTS-103 menyebut "Data uji tiap permukaan lebih dari 10 baris" tanpa menyebut keyword Search, nilai Filter, dan N per permukaan; spec menuliskannya sebagai kebutuhan seeding.
  - TC-AC-ACTS-103 menyebut "urut sesuai sort aktif" tanpa menyebut sort yang aktif; spec memakai urutan tabel yang sedang tampil sebagai sort aktif.
  - Pembaca isi berkas unduhan tidak didefinisikan di TC, PRD, atau LLD (disediakan tim FE).
