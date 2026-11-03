---
id: TC-FA-CAT-E2E-082-popup-detail-empty-terfilter-description-kosong-excess-dan-tabel-assets
title: "Popup Detail Category: Empty State Terfilter, Description Kosong, Node Excess, dan Isi Tabel Assets Exact-Match"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-276
  - TC-FA-CAT-277
  - TC-FA-CAT-282
  - TC-FA-CAT-281
coverage:
  web: automated
---

# Popup Detail Category: Empty State Terfilter, Description Kosong, Node Excess, dan Isi Tabel Assets Exact-Match

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua lewat langkah Ganti akun: Total Control pada client CatExcess (Pre-setup #31), password `Spectra.env.FA_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 `Electronics` berisi `Laptop` dan `Monitor` (Description kosong, Code `ELEC-MN`); #22 node `Laptop` dengan 12 aset terhitung (10 Active, 1 Draft, 1 Waiting for Approval) dan 3 aset tidak terhitung (2 Disposed, 1 Deleted); #31 `Furniture` (Excess, 5 aset).
- Seed client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-276: Search tanpa hasil pada tabel Assets menampilkan empty state terfilter

1. Klik node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
3. Verifikasi tabel Assets tampil dengan sedikitnya satu baris
4. Ketik Search `zzzz`, tekan Enter
5. Verifikasi area tabel menampilkan Title `No results found` dan Description `Try adjusting your search or filter.`
6. Klik `(←)` pada kotak Search
7. Klik icon Close (✕)

### TC-FA-CAT-277: Description kosong tampil strip dan Code tampil terisi

8. Klik elipsis (⋯) pada baris `Monitor` > `Detail`
9. Verifikasi Description menampilkan `—`
10. Verifikasi Code menampilkan `ELEC-MN` (terisi, tidak pernah `—`)
11. Klik icon Close (✕)

### TC-FA-CAT-282: Tabel Assets memuat aset exact-match node dengan lifecycle Draft, Waiting for Approval, dan Active

12. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
13. Atur jumlah baris per halaman menjadi 25
14. Hitung baris tabel dan perhatikan Status tiap baris
15. Verifikasi tabel memuat tepat 12 aset
16. Verifikasi 10 aset berstatus Active, 1 Draft, dan 1 Waiting for Approval
17. Verifikasi aset Disposed dan Deleted tidak tampil
18. Verifikasi tidak ada aset dari descendant node
19. Klik icon Close (✕)

### TC-FA-CAT-281: Popup Detail tetap tersedia untuk node Excess

20. Logout, lalu login sebagai Total Control client CatExcess (password `Spectra.env.FA_TC_PASSWORD`)
21. Klik elipsis (⋯) pada baris `Furniture` (Excess) > `Detail`
22. Verifikasi popup `Category Detail` terbuka
23. Verifikasi tabel Assets memuat 5 aset di `Furniture`
24. Verifikasi tidak ada aksi tulis di popup

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Urutan TC: TC-FA-CAT-276, TC-FA-CAT-277, TC-FA-CAT-282, lalu TC-FA-CAT-281 (client berbeda terakhir).
- Pada TC-FA-CAT-282 jumlah baris per halaman diatur sebelum menghitung baris (di TC langkah menghitung mendahului pengaturan), karena pagination default 10 tidak dapat menampilkan 12 baris.
- Langkah penghubung (tanpa `Verifikasi`, S-03/S-09): klik node sidebar, `(←)` pada Search, icon Close (✕), pengaturan jumlah baris, Logout dan login pada Ganti akun.
- Temuan untuk QA:
  - TC-FA-CAT-282 mengurutkan langkah menghitung sebelum mengatur jumlah baris per halaman; lihat catatan di atas.
  - TC-FA-CAT-281 tidak menyebut cara memeriksa "tidak ada aksi tulis"; spec mengasersi tidak ada aksi tulis tanpa merinci elemennya.
  - TC-FA-CAT-276 judul menyebut Filter tetapi langkah hanya memakai Search.
