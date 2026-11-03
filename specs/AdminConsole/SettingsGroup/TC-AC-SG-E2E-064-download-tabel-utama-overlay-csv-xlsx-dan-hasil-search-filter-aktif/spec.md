---
id: TC-AC-SG-E2E-064-download-tabel-utama-overlay-csv-xlsx-dan-hasil-search-filter-aktif
title: "Download Tabel Utama: Overlay CSV dan XLSX serta Hasil Search dan Filter Aktif"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-231
  - TC-AC-SG-234
coverage:
  web: automated
---

# Download Tabel Utama: Overlay CSV dan XLSX serta Hasil Search dan Filter Aktif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1, nama tampil `Budi Santoso`) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): `Pohon Uji Utama` entitas Principal (Pre-setup #16, #20), node `All Groups` terpilih, 14 group. Nilai yang dipakai: `Branch 1` dan `Branch 2` ber-Modified By `Admin B` (dua-duanya cocok dengan Search `Branch` dan Filter Modified By `Admin B`).
- Kemampuan teknis: membaca isi berkas hasil unduhan (nama berkas, baris, kolom) disediakan tim FE; Fixture BE untuk baseline `Pohon Uji Utama` disediakan tim FE/BE (lihat `suite.md`).
- Kelima kolom data tampil secara default; preferensi kolom di browser bersih.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

### TC-AC-SG-231: Overlay Download menawarkan CSV dan XLSX

1. Hover ikon Download pada toolbar
2. Verifikasi tooltip `Download` tampil
3. Klik ikon Download pada toolbar
4. Verifikasi overlay berisi opsi `Download as CSV` dan `Download as XLSX`

### TC-AC-SG-234: Download mengikuti hasil Search dan Filter aktif

5. Tutup overlay Download
6. Ketik Search `Branch`, tekan Enter
7. Klik ikon Filter pada toolbar
8. Pilih `Admin B` pada Modified By, klik `[Apply]`
9. Klik ikon Download pada toolbar
10. Klik `Download as CSV`
11. Verifikasi berkas hanya berisi 2 baris data (`Branch 1` dan `Branch 2`), sama dengan seluruh baris hasil Search dan Filter aktif pada tabel

## Notes

- Langkah penghubung (S-03): langkah 5 (menutup overlay Download sebelum TC-AC-SG-234).
- TC-AC-SG-232 (Download CSV: nilai sel angka dan format tanggal) ada di spec 112 (kelas f).
- Temuan untuk QA:
  - TC-AC-SG-234: Expected "mencakup seluruh baris cocok lintas halaman" tidak teruji lintas halaman karena hasil Search dan Filter hanya 2 baris (satu halaman pada page size 10); asersi memakai jumlah baris berkas sama dengan seluruh baris hasil. Usulan: Search/Filter yang menghasilkan lebih dari 10 baris.
