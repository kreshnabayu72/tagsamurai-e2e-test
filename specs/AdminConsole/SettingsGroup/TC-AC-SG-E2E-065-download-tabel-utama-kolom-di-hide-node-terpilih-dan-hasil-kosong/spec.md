---
id: TC-AC-SG-E2E-065-download-tabel-utama-kolom-di-hide-node-terpilih-dan-hasil-kosong
title: "Download Tabel Utama: Kolom Di-hide, Node Terpilih, dan Hasil Kosong"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-235
  - TC-AC-SG-237
  - TC-AC-SG-238
coverage:
  web: automated
---

# Download Tabel Utama: Kolom Di-hide, Node Terpilih, dan Hasil Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1, nama tampil `Budi Santoso`) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): `Pohon Uji Utama` entitas Principal (Pre-setup #16), node `All Groups` terpilih, 14 group. Nilai yang dipakai: `Region A` memiliki 4 descendant (`Branch 1`, `Branch 2`, `Floor 1`, `Room 301`).
- Kelima kolom data tampil secara default. Spec ini menyembunyikan kolom Modified By lewat Overlay Column Visibility (langkah 1) dan menampilkannya kembali (langkah 7): hook `before` dan `after` spec ini menghapus preferensi kolom tabel di browser (kemampuan disediakan tim FE).
- Kemampuan teknis: membaca isi berkas hasil unduhan (nama kolom, jumlah baris) disediakan tim FE; Fixture BE untuk baseline `Pohon Uji Utama` disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

### TC-AC-SG-235: Download tidak menyertakan kolom yang di-hide

1. Klik header kolom Actions `⋯`, lalu hapus centang kolom Modified By
2. Tutup Overlay Column Visibility
3. Klik ikon Download pada toolbar
4. Klik `Download as CSV`
5. Verifikasi tidak ada peringatan tambahan
6. Verifikasi berkas memiliki kolom Group, Total User, Total Member, dan Last Updated tetapi tidak memiliki kolom Modified By
7. Klik header kolom Actions `⋯`, centang kembali kolom Modified By, lalu tutup overlay

### TC-AC-SG-237: Download pada node terpilih hanya berisi descendant node itu

8. Klik node `Region A` di sidebar
9. Klik ikon Download pada toolbar
10. Klik `Download as CSV`
11. Verifikasi berkas berisi 4 baris descendant `Region A`
12. Verifikasi berkas tidak memuat group di luar node `Region A` (hanya 4 dari 14 group pada tree)

### TC-AC-SG-238: Download hasil kosong hanya berisi baris header

13. Klik node `All Groups` di sidebar
14. Ketik Search `zzzxxx`, tekan Enter
15. Klik ikon Download pada toolbar
16. Klik `Download as CSV`
17. Verifikasi berkas berisi baris header kolom
18. Verifikasi berkas tidak berisi baris data

## Notes

- Langkah penghubung (S-03): langkah 2 (menutup overlay), langkah 7 (memulihkan kolom Modified By, S-09), langkah 13 (mengembalikan node `All Groups`).
- Langkah 5 (absence peringatan) diletakkan segera setelah pemicu (langkah 4) dan sebelum asersi artefak (8b butir 11). Langkah 6 mengikutkan kolom lain sebagai anchor positif atas kolom Modified By yang tidak ada. Langkah 12 didahului langkah 11 (4 baris descendant). Langkah 18 didahului langkah 17 (baris header).
- Temuan untuk QA:
  - TC-AC-SG-237: Expected "4 baris descendant `Region A`" tidak menyebut nama baris; spec membaca jumlah baris berkas dan tidak membaca nilai sel.
