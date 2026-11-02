---
id: TC-AC-SG-E2E-112-isi-file-csv-group-nilai-sel-angka-dan-format-tanggal
title: "Isi File CSV Group: Berkas Seluruh Baris, Nilai Sel Angka, dan Format Tanggal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-232
coverage:
  web: automated
---

# Isi File CSV Group: Berkas Seluruh Baris, Nilai Sel Angka, dan Format Tanggal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1, nama tampil `Budi Santoso`) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): `Pohon Uji Utama` entitas Principal (Pre-setup #16, #17, #19, #20), node `All Groups` terpilih, 14 group. Nilai yang dipakai: `Region A` Total User 5, Total Member 4; format tanggal Last Updated mengikuti General Settings akun uji.
- Kemampuan teknis (kelas f, binary buffer): membaca isi berkas CSV hasil unduhan (nama berkas, header, jumlah baris, nilai sel) disediakan tim FE; Fixture BE untuk baseline `Pohon Uji Utama` disediakan tim FE/BE (lihat `suite.md`).
- Kelima kolom data tampil secara default; preferensi kolom di browser bersih.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

### TC-AC-SG-232: Download CSV berisi seluruh baris dan kolom visible tanpa toast sukses

1. Klik ikon Download pada toolbar
2. Klik `Download as CSV`
3. Verifikasi tidak ada toast sukses
4. Verifikasi berkas terunduh bernama `Groups.csv`
5. Verifikasi header kolom berkas: Group, Total User, Total Member, Modified By, Last Updated
6. Verifikasi berkas berisi 14 baris data
7. Verifikasi sel Total User dan Total Member baris `Region A` berupa angka asli (5 dan 4)
8. Verifikasi format tanggal kolom Last Updated pada berkas mengikuti General Settings

## Notes

- Langkah 3 (absence toast) diletakkan segera setelah pemicu dan sebelum asersi artefak; pemicu (langkah 2) menjadi anchor dan artefak `Groups.csv` (langkah 4) membuktikan Download selesai (8b butir 11).
- Langkah 7: Expected "angka asli" tanpa nama baris; spec memakai `Region A` menurut Pre-setup #17 dan #19.
- Temuan untuk QA:
  - TC-AC-SG-232 Expected b ("format tanggal mengikuti General Settings") tidak menyebut format literal; langkah 8 membandingkan dengan format Last Updated pada tabel/General Settings akun uji. Usulan: Pre-setup menyebut format tanggal akun uji.
