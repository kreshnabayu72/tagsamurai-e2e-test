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

1. Ketik Search `Value Warranty Node` pada Groups List, tekan Enter
2. Buka Detail Value Warranty Node (Tab Assets)
3. Buka Popup Setup Column, centang kolom Warranty Expiry, klik [Save]
4. Verifikasi W6 menampilkan `—` tanpa warna
5. Buka Popup Setup Column, hilangkan centang kolom Warranty Expiry, klik [Save]
6. Logout
7. Login sebagai akun noValueAccess
8. Buka Fixed Asset > Settings > Groups
9. Ketik Search `Value Warranty Node` pada Groups List, tekan Enter
10. Buka Detail Value Warranty Node (Tab Assets)
11. Buka Popup Setup Column, centang kolom Warranty Expiry, klik [Save]
12. Verifikasi seluruh sel Warranty Expiry menampilkan `No access` tanpa warna danger/warning, walau tanggal aslinya lewat atau segera habis
13. Hover salah satu sel `No access`
14. Verifikasi tooltip hanya "Requires Manage purchase access in this group."
15. Buka Popup Setup Column, hilangkan centang kolom Warranty Expiry, klik [Save]
16. Logout
17. Login sebagai akun warrantyWatch
18. Buka Fixed Asset > Settings > Groups

### TC-FA-GRP-1283: Penanda warna tidak memengaruhi Sort, Filter, dan isi berkas Download

19. Ketik Search `Value Warranty Node` pada Groups List, tekan Enter
20. Buka Detail Value Warranty Node (Tab Assets)
21. Buka Popup Setup Column, centang kolom Warranty Expiry, klik [Save]
22. Klik header Warranty Expiry (Oldest First)
23. Verifikasi urutan: W1 (lewat), W2, W3, W4, W5 menurut tanggal, baris `—` (W6) di akhir
24. Klik icon Filter, isi rentang Warranty Expiry yang memuat W1 sampai W3, klik [Apply]
25. Verifikasi W1 dan W3 (di dalam rentang) tampil walau berbeda kelas warna
26. Klik icon Filter, klik [Clear Field], klik [Apply]
27. Klik icon Download, pilih Download as CSV
28. Buka berkas
29. Verifikasi berkas memuat tanggal asli W1 sampai W5 (format DD/MM/YYYY sesuai General Settings) tanpa warna atau teks penanda
30. Verifikasi W6 ditulis `-` pada berkas

### TC-FA-GRP-1282: Hari ini mengikuti Time Zone General Settings

31. Atur waktu sistem uji sehingga tanggal UTC lebih awal sehari dari tanggal Asia/Jakarta (mis. 20:00 UTC = 03:00 hari berikutnya di Jakarta), isi ulang W2 dengan tanggal Jakarta saat itu
32. Muat ulang tab
33. Ketik Search `Value Warranty Node` pada Groups List, tekan Enter
34. Buka Detail Value Warranty Node (Tab Assets)
35. Hover sel W2
36. Verifikasi W2 (tanggal = hari ini menurut Asia/Jakarta) menampilkan warning "Warranty expires soon", bukan danger
37. Ubah Time Zone General Settings ke zona yang tanggalnya masih sehari sebelumnya (mis. UTC), muat ulang tab
38. Buka Fixed Asset > Settings > Groups
39. Ketik Search `Value Warranty Node` pada Groups List, tekan Enter
40. Buka Detail Value Warranty Node (Tab Assets)
41. Hover sel W2
42. Verifikasi W2 (besok menurut zona itu) tetap menampilkan warning, bukan danger

## Notes

- Urutan TC: TC-1281 (ganti akun ke NVA lalu kembali ke WW), TC-1283, lalu TC-1282 paling akhir karena mengubah state global (waktu sistem dan Time Zone); perubahan urutan dari TC.
- TC-1283 butir c (isi berkas CSV) dicatat dalam spec fungsional ini (P-10): unduhan dilakukan pada sort yang sama dengan asersi UI butir sebelumnya (filter dibersihkan lebih dulu), klausa isi berkas (butir c) diletakkan setelah klausa UI TC itu.
- Langkah penghubung (S-03): menghilangkan centang Warranty Expiry sebelum ganti akun; `Buka Fixed Asset > Settings > Groups` sesudah tiap login akun lain karena hook `beforeEach` hanya membuka halaman untuk akun pertama (S-14); `Buka Fixed Asset > Settings > Groups` dan `Buka Detail Value Warranty Node (Tab Assets)` sesudah muat ulang tab atau ubah Time Zone karena Popup Detail Group tertutup (A-9); `[Clear Field]` dan `[Apply]` membersihkan filter sebelum Download supaya asersi berkas W1 sampai W5 berlaku atas seluruh baris (TC-1283 butir c).
- Alasan di atas ~35 langkah: tiga blok TC pada satu dataset (Value Warranty Node, kolom Warranty Expiry) dengan dua ganti akun; tiap blok berdiri sendiri dan blok sesudah ganti akun tetap bermakna walau blok sebelumnya gagal.
- Langkah penghubung (S-03, S-14, R-16): sebelum tiap `Buka Detail` ditambahkan Search Groups List dengan nama group target (`Value Warranty Node`), karena client memiliki lebih dari 10 node level 1 dan page size 10 sehingga baris target tidak dijamin berada di halaman 1; Search hilang setelah F5, login, atau buka ulang halaman Groups sehingga dipasang lagi.
- Temuan untuk QA:
  - TC-1283 butir b 'rentang yang memuat W1 dan W3' tidak menyebut batas tanggal persis; spec memakai rentang W1 sampai W3 (memuat juga W2).
  - TC-1282 'zona yang tanggalnya masih sehari sebelumnya' tidak menyebut zona; spec memakai contoh UTC.
  - TC-1281 butir a hanya mengasersi W6; asumsi W1–W5 tidak diasersi di blok ini.
  - TC-1283 menyebut tanggal asli tanpa nilai konkret karena tanggal relatif terhadap hari uji; spec mengasersi tanggal W1 sampai W5 sesuai hasil seeding hari itu.
  - Kondisi filter saat Download tidak tegas dalam TC; spec membersihkan filter sebelum Download sehingga asersi 'seluruh baris' dan W6 berlaku atas semua baris.
  - TC-1282 memverifikasi teks tooltip "Warranty expires soon" tanpa menyebut langkah Hover; spec menambah Hover sel W2 sebelum tiap Verifikasi.
