---
id: TC-AC-SG-E2E-060-setup-column-tabel-utama-reset-to-default-reorder-pin-dan-unpin
title: "Setup Column Tabel Utama: Reset to Default, Reorder, serta Pin dan Unpin"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-217
  - TC-AC-SG-218
  - TC-AC-SG-219
coverage:
  web: automated
---

# Setup Column Tabel Utama: Reset to Default, Reorder, serta Pin dan Unpin

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1, nama tampil `Budi Santoso`) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): `Pohon Uji Utama` entitas Principal (Pre-setup #16), node `All Groups` terpilih, 14 group.
- Kelima kolom data tampil secara default dengan urutan default modul: Group, Total User, Total Member, Modified By, Last Updated. Spec ini menyimpan konfigurasi kolom lewat `[Save]` (langkah 7, 11, 15, 20): hook `before` dan `after` spec ini menghapus preferensi kolom tabel di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE; lihat `suite.md`).
- Perkecil lebar jendela browser (langkah 16) memerlukan kontrol viewport dari runner web; viewport dipulihkan di langkah 23.
- Kemampuan teknis: Fixture BE untuk baseline `Pohon Uji Utama`, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

### TC-AC-SG-217: Reset to Default mengembalikan konfigurasi ke default modul dan masuk preview

1. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
2. Hapus centang Total Member
3. Seret Last Updated ke posisi kedua pada daftar modal
4. Klik `[Reset to Default]`
5. Verifikasi kelima kolom (Group, Total User, Total Member, Modified By, Last Updated) tercentang sebagai preview
6. Verifikasi urutan kolom kembali ke default: Group, Total User, Total Member, Modified By, Last Updated
7. Klik `[Save]`
8. Verifikasi tabel menampilkan kelima kolom dengan urutan default (permanen setelah `[Save]`)

### TC-AC-SG-218: Reorder kolom lewat drag di modal Setup Column

9. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
10. Seret Last Updated ke posisi kedua
11. Klik `[Save]`
12. Verifikasi urutan kolom di tabel: Group, Last Updated, Total User, Total Member, Modified By

### TC-AC-SG-219: Pin dan unpin kolom membekukan kolom ke kiri saat scroll horizontal

13. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
14. Pin kolom Group
15. Klik `[Save]`
16. Perkecil lebar jendela hingga tabel scroll horizontal, lalu scroll tabel ke kanan
17. Verifikasi kolom Group tetap di posisi kiri (setelah Checkbox) saat tabel di-scroll
18. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
19. Unpin kolom Group
20. Klik `[Save]`
21. Scroll tabel ke kanan
22. Verifikasi kolom Group ikut bergeser saat tabel di-scroll
23. Pulihkan lebar jendela ke ukuran semula

## Notes

- Langkah penghubung (S-03): langkah 23 (memulihkan viewport, S-09). Langkah 3 memilih posisi kedua untuk "ubah urutan" yang tidak ditulis rinci di TC-217; pilihan itu mengikuti langkah TC-218.
- Konfigurasi kolom yang disimpan tidak dipulihkan dengan `[Reset to Default]` kecuali sebagai objek uji TC-217; hook `after` menghapus preferensi kolom (lihat Prerequisites).
- Temuan untuk QA:
  - TC-AC-SG-217: langkah 4 "ubah urutan" tidak menyebut kolom yang dipindah; spec memilih Last Updated ke posisi kedua.
  - TC-AC-SG-219: lebar jendela "hingga tabel scroll horizontal" tidak disebut angkanya; ditentukan oleh skrip.
