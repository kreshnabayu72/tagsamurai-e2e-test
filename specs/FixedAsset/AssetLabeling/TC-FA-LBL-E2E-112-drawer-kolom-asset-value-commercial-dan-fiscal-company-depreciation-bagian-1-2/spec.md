---
id: TC-FA-LBL-E2E-112-drawer-kolom-asset-value-commercial-dan-fiscal-company-depreciation-bagian-1-2
title: "Drawer Kolom Asset Value Commercial dan Fiscal (Company Depreciation) (bagian 1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-589
  - TC-FA-LBL-590
  - TC-FA-LBL-592
coverage:
  web: automated
---

# Drawer Kolom Asset Value Commercial dan Fiscal (Company Depreciation) (bagian 1/2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control `Company Depreciation` (Pre-setup #53, pengguna `Total Control Dep`), `Fixture.assetLabeling.akun.totalControlDepreciation`, `Spectra.env.FA_TC_DEPRECIATION_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Akun aktor: Total Control `Company Depreciation Baru` (Pre-setup #55, salinan `Company Depreciation` dengan label `Dep Label` juga pada `Dep Asset - 84` (Group `Dep HQ`; Tax Method kosong; harga perolehan 400000)), `Fixture.assetLabeling.akun.totalControlDepreciationBaru`, `Spectra.env.FA_TC_DEPRECIATIONBARU_PASSWORD`. Dipakai pada langkah Ganti akun (lihat tabel akun di bawah); email akun tertulis di fixture.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup `Company Depreciation` (#53), hanya dibaca dan dirujuk lewat `Fixture.assetLabeling.depreciation`: General Settings currency `Rp` (ribuan titik, desimal koma, 2 desimal); Group `Dep HQ` dan `Dep Other` (terpisah); dua buku Asset Value tetap `Commercial` dan `Fiscal`; label `Dep Label` pada aset Active `Dep Asset - 81` (Group `Dep HQ`; Commercial `Straight Line` 60 months bernilai 1000000; Fiscal `Straight Line` 48 months bernilai 500000), `Dep Asset - 82` (Group `Dep HQ`; Asset Class `Not Depreciated`, harga perolehan 250000, sehingga Commercial 250000 dan Fiscal 250000), dan `Dep Asset - 83` (Group `Dep Other`; Commercial 300000; Fiscal 100000).
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlDepreciation` (email akun Total Control `Company Depreciation`), `Fixture.assetLabeling.akun.totalControlDepreciationBaru` (email akun Total Control `Company Depreciation Baru`), dan `Fixture.assetLabeling.depreciation` (data Pre-setup #53 dan #55).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4).
- State global: konfigurasi kolom Setup Column Drawer Tagged Asset (preferensi browser) diubah dan dipulihkan oleh langkah spec; hook `after` spec ini menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4). Kemampuan menghapus preferensi itu disediakan tim FE. Tidak ada state global lain yang diubah.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah (Last Updated tidak berubah).
- Env var: `Spectra.env.FA_TC_DEPRECIATION_PASSWORD`, `Spectra.env.FA_TC_DEPRECIATIONBARU_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-LBL-589: Kolom Asset Value: dua kolom tetap, Commercial lalu Fiscal, default Hidden

1. Klik chip `Dep Label` di kolom Label
2. Verifikasi kolom Asset Value tidak tampil di header tabel Drawer
3. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`
4. Verifikasi `Asset Value (Commercial)` dan `Asset Value (Fiscal)` muncul sebagai dua kolom terpisah
5. Verifikasi kedua kolom Asset Value tidak tercentang
6. Verifikasi urutan `Asset Value (Commercial)` lalu `Asset Value (Fiscal)` pada posisi antara `Last Scanned` dan `Warranty Expiry`
7. Verifikasi tidak ada kolom Asset Value lain
8. Tutup Setup Column dengan `[✕]`
9. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, lalu klik `[Save]`
10. Verifikasi kedua kolom tampil berurutan Commercial lalu Fiscal pada posisi itu
11. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, lalu klik `[Save]`
12. Tutup Drawer Tagged Asset

### TC-FA-LBL-590: Kolom Asset Value: nilai buku terkini tiap kolom dan harga perolehan untuk Not Depreciated

13. Klik chip `Dep Label` di kolom Label
14. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, lalu klik `[Save]`
15. Verifikasi `Asset Value (Commercial)`: `Dep Asset - 81` `Rp 1.000.000,00`, `Dep Asset - 82` `Rp 250.000,00`, `Dep Asset - 83` `Rp 300.000,00`
16. Verifikasi `Asset Value (Fiscal)`: `Dep Asset - 81` `Rp 500.000,00`, `Dep Asset - 82` `Rp 250.000,00` (Not Depreciated menampilkan harga perolehan, bukan `—`), `Dep Asset - 83` `Rp 100.000,00`
17. Verifikasi nilai di kedua kolom memakai currency 2 desimal
18. Verifikasi nilai di kedua kolom rata kanan
19. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, lalu klik `[Save]`
20. Tutup Drawer Tagged Asset

### TC-FA-LBL-592: Tooltip sel Asset Value menampilkan metode dan masa manfaat; Tax Method kosong menampilkan harga perolehan

21. Ganti akun: Logout, login sebagai Total Control `Company Depreciation Baru` `Fixture.assetLabeling.akun.totalControlDepreciationBaru` (`Spectra.env.FA_TC_DEPRECIATIONBARU_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab Labels
22. Klik chip `Dep Label` di kolom Label
23. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, lalu klik `[Save]`
24. Hover sel `Asset Value (Commercial)` pada `Dep Asset - 81`
25. Verifikasi tooltip sel Commercial `Dep Asset - 81` `Straight Line · 60 months`
26. Hover sel `Asset Value (Fiscal)` pada `Dep Asset - 81`
27. Verifikasi tooltip sel Fiscal `Dep Asset - 81` `Straight Line · 48 months`
28. Verifikasi sel `Asset Value (Fiscal)` pada `Dep Asset - 84` menampilkan `Rp 400.000,00` (bukan `—`)
29. Verifikasi metode tidak menjadi kolom tersendiri dan kolom Asset Value tetap dua (`Asset Value (Commercial)` dan `Asset Value (Fiscal)`)
30. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, lalu klik `[Save]`
31. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Ganti akun: langkah pembuka TC-FA-LBL-592 berganti ke Total Control `Company Depreciation Baru` karena TC itu memakai salinan company (Pre-setup #55); akun pertama (Pre-setup #53) login di hook `before`.
- Langkah penghubung (S-03): langkah Pemulihan kolom Asset Value ke Hidden dan tutup Drawer memulihkan keadaan awal blok berikutnya (S-09); TC-FA-LBL-590 dan TC-FA-LBL-592 mencentang ulang kedua kolom sesuai langkah TC.
- Pembagian TC lintas spec: TC-FA-LBL-591 dan TC-FA-LBL-593 (Asset Value gerbang No access dan Sort, Filter, Search) ada di spec 113.
- Temuan untuk QA:
  - TC-FA-LBL-589 Expected a menyebut "kolom Asset Value tidak tampil" tanpa nama kolom; spec memverifikasi dua kolom `Asset Value (Commercial)` dan `Asset Value (Fiscal)` tidak tampil (Expected b dan data TC).
