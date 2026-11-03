---
id: TC-AC-ACTS-E2E-083-lintas-permukaan-download-hasil-kosong-dan-csv-pemisah-bom-kutip
title: "Lintas Enam Permukaan: Download Hasil Filter Kosong Berisi Header Saja dan CSV Pemisah Koma, UTF-8 BOM, serta Kutip"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-108
  - TC-AC-ACTS-109
coverage:
  web: automated
---

# Lintas Enam Permukaan: Download Hasil Filter Kosong Berisi Header Saja dan CSV Pemisah Koma, UTF-8 BOM, serta Kutip

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Tabel "Permukaan yang diuji" (enam permukaan; langkah 1 sampai 16 diulang untuk setiap baris tabel):

| No | Permukaan | Cara membuka |
|---|---|---|
| 1 | Stock List | TAG > Stock |
| 2 | Detail SKU Tab Available | Stock List, row action Detail pada SKU `RFID-ASSET-CORE-R5`, Tab Available |
| 3 | Detail SKU Tab In Use | Detail SKU `RFID-ASSET-CORE-R5`, Tab In Use |
| 4 | Modal Event Log | Detail SKU `RFID-ASSET-CORE-R5`, tombol `[Event Log]` |
| 5 | Approvals Tab Active | Tutup modal Event Log dengan klik (X), lalu Approvals > TAG Stock, Tab Active |
| 6 | Approvals Tab History | Approvals > TAG Stock, Tab History |

- Data uji: tiap permukaan memuat lebih dari 10 baris, dan sedikitnya satu baris memuat sel berisi `a,b`, sel berisi `x"y`, dan sel berisi baris baru (disiapkan seeding; TC tidak menyebut kolom dan cara seeding di tiap permukaan). Keyword Search yang tidak punya hasil: `zzz-tidak-ada-{runId}`.
- Kemampuan teknis disediakan tim FE (kelas f, isi berkas): pembaca byte berkas CSV yang diunduh (pemisah, BOM, kutip) dan pembaca daftar kolom header.
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-108 (diulang per permukaan): Download hasil filter kosong menghasilkan berkas berisi header saja

1. Buka permukaan sesuai kolom Cara membuka pada tabel "Permukaan yang diuji"
2. Ketik Search `zzz-tidak-ada-{runId}`, tekan Enter
3. Verifikasi empty state "No results found" tampil
4. Verifikasi tombol Download tetap aktif
5. Klik Download, pilih Download as CSV
6. Verifikasi tidak ada toast setelah Download
7. Verifikasi berkas CSV terunduh
8. Baca berkas CSV yang terunduh
9. Verifikasi berkas hanya memuat baris header kolom yang tampil
10. Klik `(←)` pada kotak Search

### TC-AC-ACTS-109 (diulang per permukaan): CSV berpemisah koma, UTF-8 BOM, dan nilai bertanda kutip dibungkus

11. Klik Download, pilih Download as CSV pada data yang memuat sel `a,b`, `x"y`, dan baris baru
12. Baca byte berkas CSV yang terunduh
13. Verifikasi pemisah kolom adalah koma
14. Verifikasi encoding UTF-8 dengan BOM
15. Verifikasi nilai berisi koma, kutip, atau baris baru dibungkus kutip ganda
16. Verifikasi kutip di dalam nilai digandakan

## Notes

- Mode: FE+BE. Satu TC memuat enam permukaan ("pada setiap permukaan"); satu TC tetap satu spec, jadi langkah 1 sampai 16 diulang untuk setiap baris tabel "Permukaan yang diuji" (8b butir 7, "Untuk setiap baris tabel ... (langkah 1 sampai 16)"). Spec ini melewati sekitar 35 langkah (16 langkah nominal, 96 langkah dengan ekspansi enam permukaan); alasan: semua blok satu kelas harness (isi berkas, kelas f ringan) dan satu dataset, hanya parameter permukaan yang berubah.
- Pembagian spec 080 sampai 083 (satu dataset enam permukaan): gabungan keempat spec berisi 55 langkah nominal dan 330 langkah dengan ekspansi enam permukaan, jauh melewati batas ukuran sekitar 35 langkah, sehingga topik satu dataset dipisah per kelompok TC (bagian 3 prinsip 1, keputusan 2026-10-21): 080 (TC-AC-ACTS-102 dan 103: cakupan baris), 081 (TC-AC-ACTS-104 dan 105: kolom Setup Column), 082 (TC-AC-ACTS-106, 107, dan 110: toast, kegagalan, workbook), 083 (TC-AC-ACTS-108 dan 109: hasil kosong dan isi CSV). Spec ini memuat asersi isi berkas (kelas f: pemisah, BOM, kutip) satu-satunya di keluarga ini, bersama TC-AC-ACTS-108 (berkas header saja) yang memakai pembaca berkas yang sama.
- Langkah penghubung tanpa Verifikasi (S-03): langkah 2 (Search tanpa hasil sebagai aksi TC-AC-ACTS-108, dicatat menurut R-16) dan langkah 10 (menutup Search sebelum TC-AC-ACTS-109, S-09). Untuk permukaan 5, kolom "Cara membuka" menutup modal Event Log permukaan 4 lebih dulu (modal menutupi sidebar; hook `afterEach` tidak berjalan antar iterasi). Empty state (langkah 3) adalah anchor positif untuk asersi berkas hanya berisi header (8b butir 2).
- Asersi absence toast (langkah 6) diletakkan segera setelah pemicu Download dan sebelum asersi berkas; berkas terunduh (langkah 7) menjadi anchor positif (8b butir 11).
- Temuan untuk QA:
  - TC-AC-ACTS-109 meminta sel `a,b`, `x"y`, dan baris baru di keenam permukaan tanpa menyebut kolom atau cara seeding; spec menuliskannya sebagai kebutuhan seeding.
  - TC-AC-ACTS-108 menyebut "Tombol Download tetap aktif" pada hasil kosong tanpa memasukkannya ke Expected; spec mengasersinya karena ia bagian langkah TC.
