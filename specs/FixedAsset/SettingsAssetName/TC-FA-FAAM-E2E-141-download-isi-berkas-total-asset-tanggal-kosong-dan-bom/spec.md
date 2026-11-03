---
id: TC-FA-FAAM-E2E-141-download-isi-berkas-total-asset-tanggal-kosong-dan-bom
title: "Download List: Isi Berkas Total Asset, Modified By, Last Updated, Nilai Kosong, BOM-Kutip CSV, dan Last Updated CSV Tab Total Assets"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-451
  - TC-FA-FAAM-452
  - TC-FA-FAAM-453
  - TC-FA-FAAM-454
  - TC-FA-FAAM-460
  - TC-FA-FAAM-846
coverage:
  web: automated
---

# Download List: Isi Berkas Total Asset, Modified By, Last Updated, Nilai Kosong, BOM-Kutip CSV, dan Last Updated CSV Tab Total Assets

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`). Baris yang dirujuk: `Dell Latitude` (Pre-setup #10, Modified By `Sarah Johnson`), `Warehouse Pallet` (Pre-setup #13, Default Addon `—`, Total Asset 0), dan Asset Name `Comma, "Quote" Item` (Pre-setup #15e, hanya dibaca).
- Date Format dan Time Format General Settings dibaca dari pengaturan client sebelum langkah; format itulah yang diharapkan pada sel Last Updated (TC-FA-FAAM-453). Akun Total Control memiliki akses ke Global Settings > General Settings. Nilai awal Date Format dibaca hook `before` dan dipulihkan di hook `after`.
- Data uji TC-FA-FAAM-846: nilai baru Date Format yang berbeda dari nilai awal disediakan tim FE (TC tidak menyebut nilainya). `Dell Latitude` Total Asset 42 (Pre-setup #10) hanya dibaca.
- Kemampuan teknis: mengunduh berkas dari browser dan membaca isi berkas XLSX atau CSV (sel, encoding, nama sheet) lewat pembaca berkas; disediakan tim FE/BE. Pembukaan Global Settings > General Settings.
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global yang diubah: Date Format General Settings client utama (hanya TC-FA-FAAM-846). Dipulihkan oleh langkah 31 dan 32 serta hook `after` (tetap jalan walau spec gagal di tengah). Suite berjalan serial (`parallel: false`).
- Cleanup (hook `after`): pulihkan Date Format ke nilai awal; hapus berkas unduhan.

## Test Steps

### Unduh berkas XLSX
1. Klik icon Download lalu `Download as XLSX`
2. Buka berkas `Asset-Names.xlsx`
### TC-FA-FAAM-451: Download List kelas Total Asset (angka asli)
3. Lihat sel Total Asset
4. Verifikasi sel Total Asset berupa angka (number) tanpa pemisah ribuan
5. Verifikasi sel Total Asset baris `Warehouse Pallet` tetap `0`
### TC-FA-FAAM-452: Download List kelas Modified By
6. Lihat sel Modified By baris `Dell Latitude`
7. Verifikasi sel Modified By berisi nama lengkap user `Sarah Johnson`
### TC-FA-FAAM-453: Download List kelas Last Updated (format General Settings)
8. Lihat sel Last Updated baris `Dell Latitude`
9. Verifikasi tanggal dan jam pada sel Last Updated mengikuti Date Format dan Time Format General Settings
### TC-FA-FAAM-454: Download List kelas nilai kosong
10. Lihat sel Default Addon baris `Warehouse Pallet`
11. Verifikasi sel Default Addon baris `Warehouse Pallet` berisi `-` (hyphen tunggal), bukan kosong, bukan em dash
### TC-FA-FAAM-460: CSV berencoding UTF-8 BOM dan nilai berkoma dibungkus kutip
12. Verifikasi berkas XLSX berisi satu sheet `Sheet1`
13. Klik icon Download lalu `Download as CSV`
14. Buka berkas `Asset-Names.csv`
15. Verifikasi encoding berkas CSV UTF-8 dengan BOM
16. Verifikasi nilai berkoma dan berkutip pada baris `Comma, "Quote" Item` dibungkus tanda kutip ganda
17. Verifikasi tanda kutip dalam nilai digandakan
### TC-FA-FAAM-846: Download CSV Tab Total Assets kolom Last Updated (Date Format baru General Settings)
18. Buka Global Settings > General Settings
19. Ubah Date Format ke nilai baru yang berbeda dari nilai awal
20. Klik `[Save]`
21. Buka Fixed Asset > Settings > Asset Master > Asset Name
22. Ketik Search `Dell Latitude`, tekan Enter
23. Klik nama `Dell Latitude` lalu klik tab `Total Assets (42)`
24. Klik Download lalu pilih CSV
25. Buka berkas CSV yang terunduh
26. Lihat kolom Last Updated
27. Verifikasi berkas CSV memuat sedikitnya satu baris data pada kolom Last Updated
28. Verifikasi setiap sel kolom Last Updated di berkas CSV memakai Date Format baru dari General Settings
29. Tutup Popup Detail
30. Buka Global Settings > General Settings
31. Pulihkan Date Format ke nilai awal
32. Klik `[Save]`

## Notes

- Satu berkas XLSX diunduh sekali dan dipakai oleh TC-FA-FAAM-451 sampai 454 serta klausa sheet TC-FA-FAAM-460; berkas CSV diunduh terpisah untuk klausa encoding dan kutip TC-FA-FAAM-460.
- Langkah "Lihat" adalah langkah penghubung (aksi tanpa `Verifikasi`) yang mengarahkan pembacaan sel.
- Modified By pada berkas diasersi nama lengkap sesuai Expected TC-FA-FAAM-452 (berkas memuat nama penuh, bukan format `[First Name] [Last Initial]` tabel; R-14).
- Spec ini hanya mengasersi isi sel dan encoding berkas (kelas f). Langkah 28 hanya tentang format Last Updated pada berkas CSV Tab Total Assets; langkah 27 menjadi anchor bahwa berkas memuat baris data sebelum asersi universal "setiap sel".
- Langkah penghubung tanpa `Verifikasi` pada blok TC-FA-FAAM-846: langkah 18, 21, 30 (navigasi), langkah 19, 20, 31, 32 (mengubah dan memulihkan state global; hook `after` sebagai cadangan; S-09), langkah 22 (Search), langkah 23 sampai 26 (membuka tab, mengunduh, dan membaca berkas), dan langkah 29 (menutup Popup Detail).
- Pembagian TC lintas spec: format tanggal Last Updated pada tabel Tab Total Assets (TC-FA-FAAM-608) ada di spec 225.
- Temuan untuk QA: Expected TC-FA-FAAM-453 tidak menyebut nilai Date Format dan Time Format yang diharapkan; spec membandingkan dengan format General Settings client. Nama literal `Comma, "Quote" Item` pada Pre-setup #15e dipakai apa adanya (baca saja). TC-FA-FAAM-846 tidak menyebut nilai Date Format baru, nama berkas CSV, dan label tombol Download pada tab Total Assets; spec memakai "nilai baru" yang disediakan tim FE dan menulis "Klik Download lalu pilih CSV".
