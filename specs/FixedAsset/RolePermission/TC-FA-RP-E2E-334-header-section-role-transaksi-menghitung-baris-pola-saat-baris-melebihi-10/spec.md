---
id: TC-FA-RP-E2E-334-header-section-role-transaksi-menghitung-baris-pola-saat-baris-melebihi-10
title: "Header section Role Transaksi menghitung seluruh baris termasuk baris pola saat jumlah baris melebihi 10, dan seluruh baris tampil tanpa pagination"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1167
coverage:
  web: automated
---

# Header section Role Transaksi menghitung seluruh baris termasuk baris pola saat jumlah baris melebihi 10, dan seluruh baris tampil tanpa pagination

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `Company Volume` (Pre-setup #23, `Total Control Volume`), email disediakan tim FE (email tidak tertulis di Pre-setup TC; lihat Temuan untuk QA), password `Spectra.env.FA_VOLUME_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Env var yang dipakai: `FA_VOLUME_TC_PASSWORD`, `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.
- Data Pre-setup (Company Volume): #23 (`Bulk User 1` sampai `Bulk User 120`, Active, Activated), #18 (pohon Group; node `Head Office`), dan #19 (seed Role Transaksi; baris pola Transaction Role Asset Admin dan Approver untuk Total Control dan Default User ada pada setiap node dan sub-tab). Identitas Pre-setup mengacu ke fixture `Fixture.fixedAssetRolePermission` (belum ada di repo, tanpa password; ditandai untuk tim FE).
- Kelas harness: volume data (prinsip 13e, Company Volume #23). Satu TC, satu spec.
- Precondition: kesepuluh `Bulk User` di bawah tidak memegang peran Asset Admin pada `Head Office` sub-tab `Disposal` di awal spec (di-seed bersih lewat seeding API di hook `before`; kemampuan disediakan tim FE/BE, tanpa endpoint karangan).
- Jumlah N dibaca dari header section `Asset Admin` pada langkah 4 (bukan diturunkan dari seeding), karena TC tidak menyebut nilainya; asersi berikutnya memakai N+10.
- State yang diubah dan pemulihannya: penugasan Asset Admin `Bulk User 1` sampai `Bulk User 10` pada `Head Office` sub-tab `Disposal` dan entri Changelog Assign dan Remove yang dihasilkannya. Pemulihan dilakukan langkah 22 sampai 25 (Remove per baris); hook `after` menghapus sisa penugasan kesepuluh user itu lewat seeding API tanpa berasumsi langkah 22 sampai 25 selesai. Karena target aksi tulis adalah data Pre-setup (S-06, pengecualian 2026-10-30), pemulihan dijamin fixture backend yang disediakan tim FE/BE dan suite berjalan serial; efek tersisa hanya entri Changelog (audit trail permanen).

Tabel "Bulk User yang di-Assign" (urutan baris = urutan iterasi langkah 10 dan 11 serta 22 sampai 25):

| No | Name |
|---|---|
| 1 | `Bulk User 1` |
| 2 | `Bulk User 2` |
| 3 | `Bulk User 3` |
| 4 | `Bulk User 4` |
| 5 | `Bulk User 5` |
| 6 | `Bulk User 6` |
| 7 | `Bulk User 7` |
| 8 | `Bulk User 8` |
| 9 | `Bulk User 9` |
| 10 | `Bulk User 10` |

## Test Steps

### TC-FA-RP-1167: Header section Role Transaksi menghitung seluruh baris termasuk baris pola saat jumlah baris melebihi 10, dan seluruh baris tampil tanpa pagination

1. Klik Tab `Transaction Role`
2. Klik sub-tab `Disposal`
3. Klik node `Head Office` di Sidebar Group Tree
4. Catat jumlah N pada header section `Asset Admin` sebagai baseline
5. Verifikasi header section `Asset Admin` memuat `N users` (atau `1 user` bila N = 1)
6. Klik header section `Asset Admin` untuk membuka section
7. Verifikasi N mencakup baris pola yang tampil biasa: jumlah baris pada tabel section `Asset Admin`, termasuk baris pola Total Control, sama dengan N
8. Klik header section `Asset Admin` untuk menutup section
9. Klik `[+ Assign]` pada section `Asset Admin`
10. Untuk setiap baris tabel "Bulk User yang di-Assign" (langkah 10 dan 11 diulang): ketik Search nama baris pada popup Assign, tekan Enter
11. Centang baris dengan Name persis nama baris itu pada hasil Search popup Assign
12. Klik `[Assign]`
13. Verifikasi header section `Asset Admin` memuat `N+10 users` (N dari langkah 4 ditambah 10)
14. Klik header section `Asset Admin` untuk membuka section
15. Verifikasi tabel menampilkan seluruh N+10 baris, termasuk baris pola
16. Verifikasi seluruh N+10 baris tampil dalam satu tampilan tanpa pagination
17. Verifikasi tidak ada kontrol halaman di bagian bawah tabel
18. Ketik Search `Bulk User 1`, tekan Enter
19. Verifikasi tabel tersaring ke baris `Bulk User 1` dan `Bulk User 10`
20. Verifikasi header section `Asset Admin` tetap `N+10 users`
21. Kosongkan isi kotak search, tekan Enter
22. Untuk setiap baris tabel "Bulk User yang di-Assign" (langkah 22 sampai 25 diulang): ketik Search nama baris, tekan Enter
23. Klik `[⋯]` pada baris dengan Name persis nama baris itu, lalu klik `Remove`
24. Klik `[Remove]` pada dialog
25. Klik `(←)` pada kotak Search
26. Verifikasi header section `Asset Admin` kembali `N users`

## Notes

- Spec ini memuat 26 langkah. Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-1167). Subjudul `###` memetakan langkah ke id TC granular. Mode FE+BE; tidak ada intercept.
- Langkah penghubung (S-03): langkah 1 sampai 3 (membuka Tab, sub-tab, dan node; langkah TC 1 dan prasyarat b), langkah 6, 8, dan 14 (membuka atau menutup section `Asset Admin`; langkah 8 menutup section supaya langkah TC 4 "buka section" dikerjakan dari state tertutup yang deterministik), langkah 9 sampai 12 (aksi Assign, langkah TC 3), langkah 10 dan 11 (Search di popup Assign dan centang baris, R-22; satu `Bulk User` per iterasi karena Table User Picker berpaginasi 10 baris), langkah 18, 21, 22, dan 25 (Search, R-16 dan R-23), langkah 23 dan 24 (aksi Remove per baris, langkah TC 6).
- Asersi tambahan di luar TC (S-03): langkah 7 (jumlah baris tabel section sama dengan N, tafsiran klausa "N mencakup baris pola yang tampil biasa"), langkah 15 sebagai anchor positif bagi asersi tersaring langkah 19 (butir 8b.2: universal "tersaring ke baris ..." didahului baris pembanding pada surface yang sama).
- Langkah berulang (8b.7): langkah 10 sampai 11 diulang 10 kali dan langkah 22 sampai 25 diulang 10 kali; parameter per iterasi ada di tabel Prerequisites, tanpa langkah bersyarat, dan tidak ada `Verifikasi` di dalam blok ulang. Ekspansi: 26 langkah nominal menjadi sekitar 80 langkah setelah ekspansi, di atas smell sekitar 35. Alasan dipertahankan dalam satu spec: TC berisi satu alur utuh (Assign sepuluh user, amati header, hitung baris, Search, Remove sepuluh baris) yang tidak dapat dipotong tanpa kehilangan makna, kelasnya tunggal (volume data), dan Expected d bergantung pada penugasan yang dibangun Expected a sampai c. Nomor cadangan 348 tidak dipakai.
- Search dibersihkan pada langkah 21 dan 25 sebelum asersi berikutnya mengandalkan tabel penuh (S-09). Setelah langkah 26 tidak ada state yang tersisa selain entri Changelog.
- Pemulihan ke N baris dilakukan oleh TC itu sendiri (langkah 22 sampai 25, langkah TC 6); hook `after` hanya cadangan.
- Temuan untuk QA:
  - TC-FA-RP-1167 langkah 3 menyebut `[+ Assign]` tanpa menyebut section; spec mengasumsikan `[+ Assign]` pada section `Asset Admin`, sesuai langkah 2 dan 4 TC yang berfokus pada section itu.
  - TC-FA-RP-1167 tidak menyebut apakah section `Asset Admin` awalnya terbuka atau tertutup dan apakah klik header berfungsi sebagai toggle; spec mengasumsikan section awal tertutup dan klik header membuka atau menutupnya (langkah 6, 8, 14). Bila section selalu terbuka, langkah 6, 8, dan 14 dihapus.
  - TC-FA-RP-1167 menyebut memilih `Bulk User 1` sampai `Bulk User 10` tanpa cara menemukannya di Table User Picker (120 kandidat, 10 per halaman). Spec memakai Search per user (langkah 10) dan mengasumsikan centang bertahan antar Search; bila tidak, centang kesepuluh user lewat penelusuran halaman.
  - TC-FA-RP-1167 tidak menyebut toast hasil Assign dan Remove, sehingga spec tidak mengasersinya.
  - Pre-setup #23 tidak merinci baris pola Transaction Role dan penugasan Asset Admin di `Company Volume`, padahal TC mensyaratkan #19 dan #18 pada client yang sama; spec mengasumsikan #19 tersedia di `Company Volume` dan N dibaca runtime. Email akun Total Control `Company Volume` tidak tertulis di Pre-setup TC.
  - TC-FA-RP-1167 Expected c menyebut baris `Bulk User 1` dan `Bulk User 10` tersaring dari Search `Bulk User 1`; ini bergantung pada tidak adanya `Bulk User 11` sampai `Bulk User 19` dan seterusnya di section `Asset Admin` (di-seed bersih sesuai Prerequisites).
  - Pernyataan Pre-setup bersama di `suite.md` tidak menyebut Pre-setup #23 dan jaminan pemulihan penugasan `Bulk User`; pemulihan dijamin tim FE/BE dan dicatat di Prerequisites spec ini.
