---
id: TC-FA-LBL-E2E-113-drawer-kolom-asset-value-commercial-dan-fiscal-company-depreciation-bagian-2-2
title: "Drawer Kolom Asset Value Commercial dan Fiscal (Company Depreciation) (bagian 2/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-591
  - TC-FA-LBL-593
coverage:
  web: automated
---

# Drawer Kolom Asset Value Commercial dan Fiscal (Company Depreciation) (bagian 2/2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control `Company Depreciation` (Pre-setup #53, pengguna `Total Control Dep`), `Fixture.assetLabeling.akun.totalControlDepreciation`, `Spectra.env.FA_TC_DEPRECIATION_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Akun aktor: Dep-Value (`Company Depreciation`; Read Manage Asset Master Data; Group Role View asset value pada `Dep HQ`) (Pre-setup #54), `Fixture.assetLabeling.akun.depValue`, `Spectra.env.FA_DEPVALUE_PASSWORD`. Dipakai pada langkah Ganti akun.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup `Company Depreciation` (#53), hanya dibaca dan dirujuk lewat `Fixture.assetLabeling.depreciation`: General Settings currency `Rp` (ribuan titik, desimal koma, 2 desimal); Group `Dep HQ` dan `Dep Other` (terpisah); dua buku Asset Value tetap `Commercial` dan `Fiscal`; label `Dep Label` pada aset Active `Dep Asset - 81` (Group `Dep HQ`; Commercial `Straight Line` 60 months bernilai 1000000; Fiscal `Straight Line` 48 months bernilai 500000), `Dep Asset - 82` (Group `Dep HQ`; Asset Class `Not Depreciated`, harga perolehan 250000, sehingga Commercial 250000 dan Fiscal 250000), dan `Dep Asset - 83` (Group `Dep Other`; Commercial 300000; Fiscal 100000).
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlDepreciation` (email akun Total Control `Company Depreciation`), `Fixture.assetLabeling.akun.depValue` (email akun Dep-Value), dan `Fixture.assetLabeling.depreciation` (data Pre-setup #53).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4).
- State global: konfigurasi kolom Setup Column Drawer Tagged Asset (preferensi browser) diubah dan dipulihkan oleh langkah spec; hook `after` spec ini menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4). Kemampuan menghapus preferensi itu disediakan tim FE. Tidak ada state global lain yang diubah.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah (Last Updated tidak berubah).
- Env var: `Spectra.env.FA_TC_DEPRECIATION_PASSWORD`, `Spectra.env.FA_DEPVALUE_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-LBL-593: Sort, Filter, dan Search kolom Asset Value bekerja independen per kolom (Commercial dan Fiscal)

1. Klik chip `Dep Label` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, lalu klik `[Save]`
3. Klik header `Asset Value (Commercial)` satu kali
4. Verifikasi urutan klik 1 Commercial (numerik naik): `Dep Asset - 82` (250.000), `Dep Asset - 83` (300.000), `Dep Asset - 81` (1.000.000)
5. Klik header `Asset Value (Commercial)` dua kali lagi (klik ketiga)
6. Verifikasi urutan klik 3 Commercial kembali ke default Name A-Z
7. Klik header `Asset Value (Fiscal)` satu kali
8. Verifikasi urutan klik 1 Fiscal: `Dep Asset - 83` (100.000), `Dep Asset - 82` (250.000), `Dep Asset - 81` (500.000)
9. Klik header `Asset Value (Fiscal)` kedua kali
10. Verifikasi urutan klik 2 Fiscal: `Dep Asset - 81`, `Dep Asset - 82`, `Dep Asset - 83`
11. Klik header `Asset Value (Fiscal)` ketiga kali
12. Verifikasi urutan klik 3 Fiscal kembali ke default Name A-Z
13. Klik icon Filter di toolbar Drawer dan baca daftar field
14. Verifikasi Filter Panel memuat field `Asset Value (Commercial)` dan `Asset Value (Fiscal)` (Min/Max)
15. Isi `Asset Value (Fiscal)` Min `400.000` dan Max `600.000`, lalu klik `[Apply]`
16. Verifikasi hanya `Dep Asset - 81` tampil
17. Buka panel Filter lagi, klik `[Clear Field]`
18. Klik icon Search di toolbar Drawer, ketik `Rp 100.000,00`, tekan Enter
19. Verifikasi hanya `Dep Asset - 83` tampil (nilai tampil kolom Fiscal)
20. Klik `(←)` pada kotak Search
21. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, lalu klik `[Save]`
22. Tutup Drawer Tagged Asset

### TC-FA-LBL-591: Gerbang No access berlaku di kedua kolom Asset Value

23. Ganti akun: Logout, login sebagai Dep-Value `Fixture.assetLabeling.akun.depValue` (`Spectra.env.FA_DEPVALUE_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab Labels
24. Klik chip `Dep Label` di kolom Label
25. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, lalu klik `[Save]`
26. Verifikasi `Asset Value (Commercial)`: `Dep Asset - 81` dan `Dep Asset - 82` bernilai
27. Verifikasi `Asset Value (Commercial)`: `Dep Asset - 83` (`Dep Other`) `No access`
28. Verifikasi `Asset Value (Fiscal)`: `Dep Asset - 81` dan `Dep Asset - 82` bernilai (`Dep Asset - 82` Not Depreciated menampilkan harga perolehan `Rp 250.000,00`)
29. Verifikasi `Asset Value (Fiscal)`: `Dep Asset - 83` `No access`
30. Verifikasi nilai asli `Dep Asset - 83` (300000 dan 100000) tidak tampil di kedua kolom
31. Hover sel `No access` pada `Dep Asset - 83`
32. Verifikasi sel `No access` tidak menampilkan metode maupun masa manfaat
33. Verifikasi tooltip sel `No access` hanya `Requires View asset value access in this group.`
34. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, lalu klik `[Save]`
35. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Penyimpangan urutan (bagian 3): TC-FA-LBL-593 (akun Total Control `Company Depreciation`, login di hook `before`) ditaruh sebelum TC-FA-LBL-591 supaya Ganti akun ke Dep-Value hanya sekali dan berada di akhir; Ganti akun tertulis eksplisit pada langkah pembuka TC-FA-LBL-591.
- Langkah penghubung (S-03): `[Clear Field]` sesudah Filter, `Klik (←) pada kotak Search`, Pemulihan kolom Asset Value ke Hidden, dan tutup Drawer memulihkan keadaan awal blok berikutnya (S-09).
- Pembagian TC lintas spec: TC-FA-LBL-589, 590, 592 (struktur dan nilai kolom Asset Value) ada di spec 112.
- Temuan untuk QA:
  - TC-FA-LBL-593 Langkah Uji 3 menulis "Klik header Asset Value (Commercial) satu kali lalu tiga kali"; spec memakai klik 1 lalu dua klik lagi hingga klik ketiga (Netral) sesuai Expected a, yang tidak menyebut klik 2 Commercial.
  - TC-FA-LBL-593 Expected d dan e tidak menyebut apakah filter dibersihkan sebelum Search; spec mengikuti Langkah Uji TC 7 (`[Clear Field]` lalu Search).
