---
id: TC-FA-CAT-E2E-148-penanda-masa-garansi-warranty-expiry-batas-30-hari-dan-tanpa-pengaruh
title: "Penanda Masa Garansi Kolom Warranty Expiry: Expired, Expires Soon, Batas 30 Hari, dan Tanpa Pengaruh pada Sort, Filter, Search, Download"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-694
  - TC-FA-CAT-695
  - TC-FA-CAT-697
coverage:
  web: automated
---

# Penanda Masa Garansi Kolom Warranty Expiry: Expired, Expires Soon, Batas 30 Hari, dan Tanpa Pengaruh pada Sort, Filter, Search, Download

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Full Sensitive (Pre-setup #50) `fullSensitive_automated_{namaCompany}@qwertysystem.net` (Manage Asset Master Data: R; Group Role View asset value dan Manage purchase pada group `Head Office` dan `Region Jawa`; Global Role Manage accounting; lisensi FA-7 aktif), client CatMain (Pre-setup #20), password `Spectra.env.FA_FS_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_FS_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup #20: node `Furniture` (Code `FURN`, leaf).
- Data milik spec (di-seed hook `before` lewat API; dibersihkan hook `after`; kemampuan seed disediakan tim FE/BE), client CatMain, node `Laptop`: aset `Garansi Jauh {runId}-148` dengan Warranty Expiry relatif hari ini + 365 hari menurut Time Zone General Settings client (dipakai sebagai tanggal garansi jauh pada TC-FA-CAT-694 Expected d, menggantikan tanggal absolut).
- Data Pre-setup #58 (CatMain, node `Furniture`, aset `Office Chair - 1` sampai `Office Chair - 5`, seed API): Warranty Expiry relatif terhadap hari ini menurut Time Zone General Settings client: `Office Chair - 1` kemarin, `Office Chair - 2` hari ini, `Office Chair - 3` hari ini + 30 hari, `Office Chair - 4` hari ini + 31 hari, `Office Chair - 5` hari ini + 10 hari. Tanggal diisi ulang lewat seed API pada awal tiap run; disediakan tim FE.
- Kemampuan teknis: membaca isi berkas unduhan XLSX (tanggal asli, informasi warna, tooltip); disediakan tim FE.
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- State yang diubah spec: konfigurasi Setup Column tersimpan di browser. Kemampuan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dipakai sebagai langkah penghubung bila TC berikutnya membutuhkan kolom bawaan dan sebagai pemulihan di hook `after`; disediakan tim FE (butir hook suite). Spec ini tidak mengubah data Pre-setup.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik elipsis (⋯) pada baris `Furniture` > `Detail`

### TC-FA-CAT-694: Penanda masa garansi lewat, hari ini, dan jauh

2. Klik header Actions (⋯) > `Setup Column...`, centang `Warranty Expiry`, lalu klik `[Save]`
3. Hover tanggal `Office Chair - 1` (kemarin)
4. Verifikasi sel memakai kelas warna danger dan tooltip `Warranty expired`
5. Hover tanggal `Office Chair - 2` (hari ini)
6. Verifikasi sel memakai kelas warna warning dan tooltip `Warranty expires soon` (pada tanggal habis garansi masih berlaku, bukan expired)
7. Verifikasi tanggal tampil penuh pada kedua sel
8. Klik icon close (✕) pada Popup Detail
9. Pilih node `Electronics` di Sidebar Category Tree
10. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
11. Ketik Search `Garansi Jauh {runId}-148`, tekan Enter
12. Verifikasi sel Warranty Expiry `Garansi Jauh {runId}-148` (hari ini + 365) tampil normal tanpa warna dan tanpa tooltip penanda garansi
13. Klik `(←)` pada kotak Search

### TC-FA-CAT-695: Batas warning garansi hari ke-30 inklusif dan hari ke-31 normal

14. Klik icon close (✕) pada Popup Detail
15. Pilih node `All Categories` di Sidebar Category Tree
16. Klik elipsis (⋯) pada baris `Furniture` > `Detail`
17. Hover tanggal `Office Chair - 3` (hari ini + 30)
18. Verifikasi sel tampil warning dengan tooltip `Warranty expires soon`
19. Hover tanggal `Office Chair - 4` (hari ini + 31)
20. Verifikasi sel tampil normal tanpa tooltip penanda garansi
21. Verifikasi ambang 30 hari tetap (angka tetap, bukan setting)

### TC-FA-CAT-697: Penanda tidak mempengaruhi Sort, Filter, Search, dan Download

22. Klik header Warranty Expiry satu kali
23. Verifikasi urutan Oldest First: `Office Chair - 1`, `Office Chair - 2`, `Office Chair - 5`, `Office Chair - 3`, `Office Chair - 4` tanpa dipengaruhi warna
24. Klik header Warranty Expiry satu kali lagi
25. Klik header Warranty Expiry satu kali lagi
26. Klik icon Filter, pilih rentang Warranty Expiry dari kemarin sampai hari ini (mencakup `Office Chair - 1` dan `Office Chair - 2`), lalu klik `[Apply]`
27. Verifikasi Filter rentang hanya menyisakan `Office Chair - 1` dan `Office Chair - 2`
28. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
29. Ketik Search tanggal `Office Chair - 2`, tekan Enter
30. Verifikasi tidak ada hasil karena Data Type Date tidak dicari lewat Search
31. Klik `(←)` pada kotak Search
32. Klik Download > `Download as XLSX`
33. Buka berkas `Category-Assets.xlsx`
34. Verifikasi berkas menulis tanggal asli mengikuti General Settings tanpa informasi warna maupun tooltip

## Notes

- Mode: FE+BE. Langkah penghubung (S-03, S-09): menutup Popup Detail, memilih node, `[Clear Field]` + `[Apply]`, dan `(←)` pada Search. Search pada langkah 11 menemukan aset garansi jauh milik spec pada tabel Popup Detail `Laptop` (R-16). Kode warna spesifik tidak diasersi, hanya kelas danger, warning, dan normal (TC-FA-CAT-694 Expected e).
- Dua klik header Warranty Expiry tambahan pada TC-FA-CAT-697 mengembalikan urutan ke Netral (langkah penghubung; Newest First tidak diasersi oleh TC).
- Temuan untuk QA:
  - TC-FA-CAT-697 langkah 5 "Search tanggal `Office Chair - 2`" ambigu (nama aset atau tanggal); spec mengikuti Expected c (Search tanggal tidak menemukan hasil) dengan mengetik teks sesuai TC.
  - TC-FA-CAT-694 menyebut hover tiap tanggal tetapi `Laptop Dell - 1` hanya diamati tanpa hover pada langkah 5; spec memverifikasi tampil normal.
  - Pre-setup #55 menulis Warranty Expiry `Laptop Dell - 1` 2027-03-15 (absolut; TC-FA-CAT-694 Expected d dan TC-FA-CAT-695 Expected c) sehingga akan menjadi expired setelah tanggal itu. Spec memakai aset milik spec dengan tanggal relatif (hari ini + 365); TC dan Pre-setup #55 perlu diubah menjadi tanggal relatif.
  - TC-FA-CAT-697 Expected b menyebut rentang yang "mencakup" dua aset tanpa tanggal literal karena tanggal relatif hari ini.
