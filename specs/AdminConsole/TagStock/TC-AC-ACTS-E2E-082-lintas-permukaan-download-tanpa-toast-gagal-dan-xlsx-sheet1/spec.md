---
id: TC-AC-ACTS-E2E-082-lintas-permukaan-download-tanpa-toast-gagal-dan-xlsx-sheet1
title: "Lintas Enam Permukaan: Download Sukses Tanpa Toast, Gagal dengan Toast Error, dan Workbook XLSX Satu Sheet"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-106
  - TC-AC-ACTS-107
  - TC-AC-ACTS-110
coverage:
  web: automated
---

# Lintas Enam Permukaan: Download Sukses Tanpa Toast, Gagal dengan Toast Error, dan Workbook XLSX Satu Sheet

## Prerequisites

- Mode: FE+BE. Intercept respons Download dengan 5xx lewat `Spectra.intercept()` di atas backend nyata (satu kegagalan 5xx).
- Akun aktor: Total Control Principal `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Tabel "Permukaan yang diuji" (enam permukaan; langkah 1 sampai 12 diulang untuk setiap baris tabel):

| No | Permukaan | Cara membuka | Nama file pada toast gagal |
|---|---|---|---|
| 1 | Stock List | TAG > Stock | `TAG-Stock` |
| 2 | Detail SKU Tab Available | Stock List, row action Detail pada SKU `RFID-ASSET-CORE-R5`, Tab Available | nama file permukaan tanpa extension (TC hanya memberi contoh Stock List) |
| 3 | Detail SKU Tab In Use | Detail SKU `RFID-ASSET-CORE-R5`, Tab In Use | nama file permukaan tanpa extension |
| 4 | Modal Event Log | Detail SKU `RFID-ASSET-CORE-R5`, tombol `[Event Log]` | nama file permukaan tanpa extension |
| 5 | Approvals Tab Active | Tutup modal Event Log dengan klik (X), lalu Approvals > TAG Stock, Tab Active | `TAG-Stock` (TC-AC-ACTS-776) |
| 6 | Approvals Tab History | Approvals > TAG Stock, Tab History | `TAG-Stock` (TC-AC-ACTS-776) |

- Data uji: tiap permukaan memuat lebih dari 10 baris (disiapkan seeding).
- Kemampuan teknis disediakan tim FE: pembaca isi berkas CSV dan XLSX yang diunduh (jumlah sheet dan nama sheet). Intercept dilepas segera setelah asersi (S-09).
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-106 (diulang per permukaan): Download sukses tidak menampilkan toast

1. Buka permukaan sesuai kolom Cara membuka pada tabel "Permukaan yang diuji"
2. Klik Download, pilih Download as CSV
3. Verifikasi tidak ada toast sukses setelah Download
4. Verifikasi berkas CSV terunduh

### TC-AC-ACTS-110 (diulang per permukaan): Download XLSX memuat satu sheet bernama Sheet1

5. Klik Download, pilih Download as XLSX
6. Buka workbook yang terunduh
7. Verifikasi workbook berisi tepat satu sheet bernama `Sheet1`

### TC-AC-ACTS-107 (diulang per permukaan): Download gagal menampilkan toast error dengan nama file

8. Intercept respons Download dengan 5xx
9. Klik Download, pilih Download as CSV
10. Verifikasi toast error "Error, failed to download [File Name]." dengan `[File Name]` nama file permukaan tanpa extension (kolom Nama file pada toast gagal)
11. Lepas intercept respons Download
12. Tunggu toast lama hilang otomatis

## Notes

- Mode: FE+BE. Satu TC memuat enam permukaan ("pada setiap permukaan"); satu TC tetap satu spec, jadi langkah 1 sampai 12 diulang untuk setiap baris tabel "Permukaan yang diuji" (8b butir 7, "Untuk setiap baris tabel ... (langkah 1 sampai 12)"). Spec ini melewati sekitar 35 langkah (12 langkah nominal, 72 langkah dengan ekspansi enam permukaan); alasan: semua blok satu kelas harness dan satu dataset, hanya parameter permukaan yang berubah.
- Pembagian spec 080 sampai 083 (satu dataset enam permukaan): gabungan keempat spec berisi 55 langkah nominal dan 330 langkah dengan ekspansi enam permukaan, jauh melewati batas ukuran sekitar 35 langkah, sehingga topik satu dataset dipisah per kelompok TC (bagian 3 prinsip 1, keputusan 2026-10-21): 080 (TC-AC-ACTS-102 dan 103: cakupan baris), 081 (TC-AC-ACTS-104 dan 105: kolom Setup Column), 082 (TC-AC-ACTS-106, 107, dan 110: toast, kegagalan, workbook), 083 (TC-AC-ACTS-108 dan 109: hasil kosong dan isi CSV). TC-AC-ACTS-107 (kegagalan 5xx) adalah satu-satunya TC objek-uji ringan kelas b di spec ini (P-5 butir b, paling banyak dua) sehingga tidak perlu spec resilience sendiri; asersi workbook satu sheet adalah struktur berkas, bukan nilai sel.
- P-5 butir (b): TC-AC-ACTS-107 adalah satu kegagalan 5xx objek-uji ringan (intercept di atas backend nyata) pada permukaan yang sama dengan TC-AC-ACTS-106 dan TC-AC-ACTS-110; jumlah TC objek-uji ringan dalam spec ini satu.
- Urutan TC-AC-ACTS-110 sebelum TC-AC-ACTS-107 supaya kegagalan yang dipaksa berada di akhir tiap iterasi; langkah 11 dan 12 adalah langkah penghubung tanpa Verifikasi (S-03, S-09). Untuk permukaan 5, kolom "Cara membuka" menutup modal Event Log permukaan 4 lebih dulu (modal menutupi sidebar; hook `afterEach` tidak berjalan antar iterasi).
- Asersi absence toast sukses (langkah 3) diletakkan segera setelah pemicu Download dan sebelum asersi berkas; pemicunya dan berkas terunduh (langkah 4) menjadi anchor positif (8b butir 11).
- Temuan untuk QA:
  - TC-AC-ACTS-107 hanya memberi contoh nama file Stock List (`TAG-Stock`); nama file permukaan lain tidak disebut (TC-AC-ACTS-776 menyebut `TAG-Stock` untuk Approvals).
  - Pembaca isi berkas CSV dan XLSX tidak didefinisikan di TC, PRD, atau LLD (disediakan tim FE).
