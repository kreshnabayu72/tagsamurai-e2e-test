---
id: TC-AC-ACTS-E2E-081-lintas-permukaan-download-kolom-hide-dan-unhide
title: "Lintas Enam Permukaan: Download Mengikuti Kolom yang Tampil, Kolom Di-Hide Tidak Ikut dan Di-Unhide Ikut"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-104
  - TC-AC-ACTS-105
coverage:
  web: automated
---

# Lintas Enam Permukaan: Download Mengikuti Kolom yang Tampil, Kolom Di-Hide Tidak Ikut dan Di-Unhide Ikut

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Tabel "Permukaan yang diuji" (enam permukaan; langkah 1 sampai 13 diulang untuk setiap baris tabel):

| No | Permukaan | Cara membuka |
|---|---|---|
| 1 | Stock List | TAG > Stock |
| 2 | Detail SKU Tab Available | Stock List, row action Detail pada SKU `RFID-ASSET-CORE-R5`, Tab Available |
| 3 | Detail SKU Tab In Use | Detail SKU `RFID-ASSET-CORE-R5`, Tab In Use |
| 4 | Modal Event Log | Detail SKU `RFID-ASSET-CORE-R5`, tombol `[Event Log]` |
| 5 | Approvals Tab Active | Tutup modal Event Log dengan klik (X), lalu Approvals > TAG Stock, Tab Active |
| 6 | Approvals Tab History | Approvals > TAG Stock, Tab History |

- Data uji: tiap permukaan memuat lebih dari 10 baris (disiapkan seeding). Kolom uji tiap permukaan adalah satu kolom hideable yang dipilih penguji (TC tidak menyebut kolomnya).
- Konfigurasi kolom Setup Column yang disimpan spec ini dihapus lewat penghapusan preferensi kolom tabel di browser pada hook `before` dan `after` (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE.
- Kemampuan teknis disediakan tim FE: pembaca isi berkas XLSX yang diunduh (daftar kolom header).
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-104 (diulang per permukaan): Kolom di-hide tidak ikut diekspor

1. Buka permukaan sesuai kolom Cara membuka pada tabel "Permukaan yang diuji"
2. Buka Setup Column (Column Visibility), sembunyikan satu kolom hideable, klik `[Save]`
3. Klik Download, pilih Download as XLSX
4. Verifikasi tidak ada toast atau peringatan tambahan setelah Download
5. Verifikasi berkas XLSX terunduh
6. Buka berkas XLSX yang terunduh
7. Verifikasi berkas tidak memuat kolom yang disembunyikan

### TC-AC-ACTS-105 (diulang per permukaan): Kolom yang di-unhide kembali ikut diekspor

8. Buka Setup Column, tampilkan kembali semua kolom, klik `[Save]`
9. Buka Setup Column, sembunyikan satu kolom hideable, klik `[Save]`
10. Buka Setup Column, tampilkan kembali kolom yang sama, klik `[Save]`
11. Klik Download, pilih Download as XLSX
12. Buka berkas XLSX yang terunduh
13. Verifikasi berkas memuat kembali kolom tersebut

## Notes

- Mode: FE+BE. Satu TC memuat enam permukaan ("pada setiap permukaan"); satu TC tetap satu spec, jadi langkah 1 sampai 13 diulang untuk setiap baris tabel "Permukaan yang diuji" (8b butir 7, "Untuk setiap baris tabel ... (langkah 1 sampai 13)"). Spec ini melewati sekitar 35 langkah (13 langkah nominal, 78 langkah dengan ekspansi enam permukaan); alasan: semua blok satu kelas harness dan satu dataset, hanya parameter permukaan yang berubah.
- Pembagian spec 080 sampai 083 (satu dataset enam permukaan): gabungan keempat spec berisi 55 langkah nominal dan 330 langkah dengan ekspansi enam permukaan, jauh melewati batas ukuran sekitar 35 langkah, sehingga topik satu dataset dipisah per kelompok TC (bagian 3 prinsip 1, keputusan 2026-10-21): 080 (TC-AC-ACTS-102 dan 103: cakupan baris), 081 (TC-AC-ACTS-104 dan 105: kolom Setup Column), 082 (TC-AC-ACTS-106, 107, dan 110: toast, kegagalan, workbook), 083 (TC-AC-ACTS-108 dan 109: hasil kosong dan isi CSV). Spec ini memuat asersi kolom berkas (nama kolom header, fungsional), bukan nilai sel; isi byte berkas (kelas f) hanya ada di spec 083.
- Langkah penghubung tanpa awalan Verifikasi (S-03): langkah 8 (menampilkan kembali semua kolom agar TC-AC-ACTS-105 mulai dari keadaan semua kolom tampil, S-09), langkah 9 dan 10 (aksi sembunyikan lalu tampilkan kembali sesuai langkah TC). Untuk permukaan 5, kolom "Cara membuka" menutup modal Event Log permukaan 4 lebih dulu (modal menutupi sidebar; hook `afterEach` tidak berjalan antar iterasi).
- Asersi absence "tanpa toast atau peringatan tambahan" (langkah 4) diletakkan segera setelah pemicu Download dan sebelum asersi berkas; pemicunya dan berkas terunduh (langkah 5) menjadi anchor positif (8b butir 11).
- Temuan untuk QA:
  - TC-AC-ACTS-104 dan TC-AC-ACTS-105 menyebut "Column Visibility" sedangkan halaman memakai istilah Setup Column; spec memakai Setup Column (Column Visibility).
  - TC tidak menyebut kolom yang disembunyikan di tiap permukaan; spec memakai satu kolom hideable pilihan penguji.
