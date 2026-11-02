---
id: TC-FA-GRP-E2E-265-tab-assets-warranty-expiry-penanda-warna-dash-no-access-time-zone-client-dan-tidak-memengaruhi-sort-filter-download
title: "Tab Assets Warranty Expiry Penanda Warna: Sel Dash dan No Access Tanpa Warna, Hari Ini Mengikuti Time Zone General Settings, dan Tidak Memengaruhi Sort/Filter"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1281
  - TC-FA-GRP-1282
  - TC-FA-GRP-1283
coverage:
  web: automated
---

# Tab Assets Warranty Expiry Penanda Warna: Sel Dash dan No Access Tanpa Warna, Hari Ini Mengikuti Time Zone General Settings, dan Tidak Memengaruhi Sort/Filter

## Prerequisites

- Mode: FE+BE.
- Akun warrantyWatch (Pre-setup No 21; Group Role Manage purchase pada Value Warranty Node): `warrantyWatch_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_WARRANTYWATCH_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun noValueAccess (Pre-setup No 16; tanpa View asset value, Manage purchase, maupun Manage accounting): `noValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_NOVALUEACCESS_PASSWORD`. Dipakai lewat langkah ganti akun eksplisit.
- Hook suite (`suite.md`) berlaku: sesi API aktor, fixture BE, flag Guided Tooltip `seen`, dan pemulihan state global; tidak ditulis ulang di sini.
- General Settings client: Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (dibaca; tidak diubah).
- Data Value Warranty Node (Tabel Dinamis No 19; tanggal Warranty Expiry diisi ulang relatif terhadap hari uji di hook `before`, kemampuan disediakan tim FE/BE): W1 `Laptop Dell - 5` (hari uji − 1), W2 `Laptop Dell - 6` (hari uji), W3 `Laptop Dell - 7` (hari uji + 1), W4 `Laptop Dell - 8` (hari uji + 30), W5 `Laptop Dell - 9` (hari uji + 31), W6 `Laptop Dell - 10` (belum ada). Akun WW memegang Manage Group R pada node ini.
- Kemampuan teknis: mengisi ulang tanggal Warranty W1–W6 relatif terhadap hari uji; mengendalikan waktu sistem uji (jam server dan jam browser diatur bersama) dan mengubah Time Zone General Settings (disediakan tim FE/BE); menghapus preferensi kolom Setup Column di browser (disediakan tim FE); membuka dan membaca isi berkas CSV unduhan (nilai sel, hyphen `-`) disediakan tim FE.
- State global yang diubah: waktu sistem uji dan Time Zone General Settings (semula Asia/Jakarta). Pemulihan di hook `after`. Suite serial (`parallel: false`).
- Preferensi kolom Setup Column yang disimpan spec ini dihapus dari browser di hook `after` (kemampuan disediakan tim FE).

## Test Steps

### TC-FA-GRP-1281: Sel `—` dan `No access` tidak diberi warna

1. Buka Detail Value Warranty Node (Tab Assets)
2. Buka Popup Setup Column, centang kolom Warranty Expiry, klik [Save]
3. Verifikasi W6 menampilkan `—` tanpa warna
4. Buka Popup Setup Column, hilangkan centang kolom Warranty Expiry, klik [Save]
5. Logout
6. Login sebagai akun noValueAccess
7. Buka Detail Value Warranty Node (Tab Assets)
8. Buka Popup Setup Column, centang kolom Warranty Expiry, klik [Save]
9. Verifikasi seluruh sel Warranty Expiry menampilkan `No access` tanpa warna danger/warning, walau tanggal aslinya lewat atau segera habis
10. Hover salah satu sel `No access`
11. Verifikasi tooltip hanya "Requires Manage purchase access in this group."
12. Buka Popup Setup Column, hilangkan centang kolom Warranty Expiry, klik [Save]
13. Logout
14. Login sebagai akun warrantyWatch

### TC-FA-GRP-1283: Penanda warna tidak memengaruhi Sort, Filter, dan isi berkas Download

15. Buka Detail Value Warranty Node (Tab Assets)
16. Buka Popup Setup Column, centang kolom Warranty Expiry, klik [Save]
17. Klik header Warranty Expiry (Oldest First)
18. Verifikasi urutan: W1 (lewat), W2, W3, W4, W5 menurut tanggal, baris `—` (W6) di akhir
19. Klik icon Filter, isi rentang Warranty Expiry yang memuat W1 sampai W3, klik [Apply]
20. Verifikasi W1 dan W3 (di dalam rentang) tampil walau berbeda kelas warna
21. Klik icon Download, pilih Download as CSV
22. Buka berkas
23. Verifikasi berkas memuat tanggal asli W1 sampai W5 (format DD/MM/YYYY sesuai General Settings) tanpa warna atau teks penanda
24. Verifikasi W6 ditulis `-` pada berkas
25. Klik icon Filter, klik [Clear Field], klik [Apply]

### TC-FA-GRP-1282: Hari ini mengikuti Time Zone General Settings

26. Atur waktu sistem uji sehingga tanggal UTC lebih awal sehari dari tanggal Asia/Jakarta (mis. 20:00 UTC = 03:00 hari berikutnya di Jakarta), isi ulang W2 dengan tanggal Jakarta saat itu
27. Muat ulang tab
28. Hover sel W2
29. Verifikasi W2 (tanggal = hari ini menurut Asia/Jakarta) menampilkan warning "Warranty expires soon", bukan danger
30. Ubah Time Zone General Settings ke zona yang tanggalnya masih sehari sebelumnya (mis. UTC), muat ulang tab
31. Hover sel W2
32. Verifikasi W2 (besok menurut zona itu) tetap menampilkan warning, bukan danger

## Notes

- Urutan TC: TC-1281 (ganti akun ke NVA lalu kembali ke WW), TC-1283, lalu TC-1282 paling akhir karena mengubah state global (waktu sistem dan Time Zone); perubahan urutan dari TC.
- TC-1283 butir c (isi berkas CSV) dicatat dalam spec fungsional ini (P-10): unduhan dilakukan pada filter dan sort yang sama dengan asersi UI butir sebelumnya, klausa isi berkas (butir c) diletakkan setelah klausa UI TC itu.
- Langkah penghubung (S-03): menghilangkan centang Warranty Expiry sebelum ganti akun; `[Clear Field]` dan `[Apply]` untuk membersihkan filter.
- Temuan untuk QA:
  - TC-1283 butir b 'rentang yang memuat W1 dan W3' tidak menyebut batas tanggal persis; spec memakai rentang W1 sampai W3 (memuat juga W2).
  - TC-1282 'zona yang tanggalnya masih sehari sebelumnya' tidak menyebut zona; spec memakai contoh UTC.
  - TC-1281 butir a hanya mengasersi W6; asumsi W1–W5 tidak diasersi di blok ini.
  - TC-1283 menyebut tanggal asli tanpa nilai konkret karena tanggal relatif terhadap hari uji; spec mengasersi tanggal W1 sampai W5 sesuai hasil seeding hari itu.
  - Berkas diunduh pada alur yang sama dengan Sort dan Filter sehingga kondisi filter saat Download tidak tegas dalam TC; asersi 'seluruh baris' dan W6 mengasumsikan semua baris tercakup.
  - TC-1282 memverifikasi teks tooltip "Warranty expires soon" tanpa menyebut langkah Hover; spec menambah Hover sel W2 sebelum tiap Verifikasi.
