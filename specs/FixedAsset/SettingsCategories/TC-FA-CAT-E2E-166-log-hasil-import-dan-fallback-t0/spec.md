---
id: TC-FA-CAT-E2E-166-log-hasil-import-dan-fallback-t0
title: "Log Kategori Hasil Import (Tab Category dan Create Missing Categories), Parity Edit dan Delete Record Hasil Import, serta Log Marked as Excess dari Fallback T-0 oleh System"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-474
  - TC-FA-CAT-475
  - TC-FA-CAT-476
  - TC-FA-CAT-469
coverage:
  web: automated
---

# Log Kategori Hasil Import (Tab Category dan Create Missing Categories), Parity Edit dan Delete Record Hasil Import, serta Log Marked as Excess dari Fallback T-0 oleh System

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor kedua: Total Control (Pre-setup #1) pada client CatPreT0 (Pre-setup #32) untuk TC-FA-CAT-469, password dari `Spectra.env.FA_TC_PASSWORD`. Login lewat langkah Ganti akun eksplisit (langkah 25). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #38 (CatMain): kategori `Import Cat` (Code `IMP1`) dan `Import Cat Child` dibuat lewat Import Tab Category oleh Import Data, kategori `Missing Cat` dibuat lewat `[Create Missing Categories]` dari Tab Asset Name. Record hasil Import tidak dapat dimiliki spec lewat seed biasa; langkah 13 sampai 24 (TC-FA-CAT-476) mengubah dan menghapus `Import Cat` beserta `Import Cat Child`. Pemulihan ke keadaan awal lewat fixture backend yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` (S-06, pengecualian 2026-10-30). Efek: Last Updated dan entri Changelog bertambah; suite berjalan serial. Identitas user pelaku Import tidak tertulis di Pre-setup #38 (lihat Temuan untuk QA).
- Data Pre-setup #32 (CatPreT0, plan Professional dengan downgrade terjadwal ke Starter, T-0 belum tiba, cap plan aktif 100 dan cap plan baru 5, 8 kategori usable `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy`): jumlah node yang menjadi Excess pada Fallback T-0 tanpa seleksi adalah 3 (8 kategori dikurangi cap baru 5).
- Kemampuan teknis untuk langkah 27 sampai 29 (TC-FA-CAT-469, kelas time-travel T-0 sebagai pemicu): mengatur jam server dan jam browser secara absolut ke T-0 (dibaca dari downgrade terjadwal lewat seed API) tanpa seleksi Wizard, lalu memulihkan keduanya ke waktu nyata sebelum surface log dibuka (S-09); pemicu Fallback T-0 dan pemulihan lewat fixture backend yang disediakan tim FE/BE tanpa endpoint karangan, dijalankan juga di hook `before` dan `after`. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: membuka Modal Changelog (filter Category Name atau Action), Detail User aktor > Tab System Log, dan Activity Log serta mencari baris berdasarkan nama kategori; membaca daftar user client CatPreT0 yang relevan untuk langkah 34. Mekanisme pencarian tidak diuraikan TC dan disediakan tim FE/BE tanpa endpoint karangan. Kolom Modified By diasersi berformat `[First Name] [Last Initial]`.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-474: Log kategori hasil Import Tab Category, aktor penjalan Import pada tiga surface

1. Buka Modal Changelog dan cari baris Category Name `Import Cat`
2. Verifikasi Changelog memuat baris Action `Create`, Field `Category Name`, Old Value `—`, New Value `Import Cat`, dengan Modified By user pelaku Import
3. Tutup Modal Changelog, buka Detail User aktor pelaku Import > Tab System Log, dan cari baris Name `Import Cat`
4. Verifikasi System Log aktor memuat baris yang sama dengan Object `Categories` dan Name `Import Cat`
5. Buka Activity Log dan cari baris `Import Cat`
6. Verifikasi Activity Log memuat baris yang sama

### TC-FA-CAT-475: Log kategori hasil Create Missing Categories dari Tab Asset Name

7. Buka Modal Changelog dan cari baris Category Name `Missing Cat`
8. Verifikasi Changelog memuat baris Action `Create`, Field `Category Name`, Old Value `—`, New Value `Missing Cat`, dengan Modified By aktor yang menjalankan
9. Tutup Modal Changelog, buka Detail User aktor > Tab System Log, dan cari baris Name `Missing Cat`
10. Verifikasi System Log aktor memuat baris yang sama
11. Buka Activity Log dan cari baris `Missing Cat`
12. Verifikasi Activity Log memuat baris yang sama

### TC-FA-CAT-476: Record hasil Import berperilaku identik dengan Create manual pada Edit dan Delete

13. Klik elipsis (⋯) pada baris `Import Cat` > `Edit`
14. Ubah Category Name menjadi `Import Cat Edited`, lalu klik `[Save]`
15. Verifikasi toast `Success, category has been updated.`
16. Buka Modal Changelog dan cari baris Category Name `Import Cat Edited`
17. Verifikasi Changelog memuat baris Action `Edit`, Field `Category Name`, Old Value `Import Cat`, New Value `Import Cat Edited`
18. Tutup Modal Changelog
19. Klik elipsis (⋯) pada baris `Import Cat Edited` > `Delete`
20. Verifikasi dialog D-08 tampil
21. Klik `[Delete]` pada dialog D-08
22. Buka Modal Changelog dan cari baris Action `Delete` dengan Category Name berawalan `Import Cat Edited`
23. Verifikasi Changelog memuat dua baris Delete: `Import Cat Edited` dan `Import Cat Edited › Import Cat Child` (satu baris per node)
24. Tutup Modal Changelog

### TC-FA-CAT-469: Log Marked as Excess dari Fallback T-0, System pada Changelog dan Activity Log tanpa System Log

25. Ganti akun: logout, login sebagai Total Control pada client CatPreT0 (Pre-setup #32) dengan `Spectra.env.FA_TC_PASSWORD`, lalu buka Fixed Asset > Settings > Categories
26. Catat baseline: jumlah baris Changelog dan Activity Log Action `Marked as Excess (Category Consolidation)` serta jumlah baris System Log Object `Categories` pada Detail User tiap user relevan client CatPreT0
27. Atur jam server dan jam browser ke T-0 secara absolut tanpa menyimpan seleksi Wizard, sehingga Fallback T-0 berjalan
28. Muat ulang halaman tiap 5 detik sampai kategori ber-badge `Excess` tampil pada tabel (batas 2 menit)
29. Pulihkan jam server dan jam browser ke waktu nyata
30. Buka Modal Changelog dan filter Action `Marked as Excess (Category Consolidation)`
31. Verifikasi Changelog memuat tiga baris baru dari baseline dengan Action `Marked as Excess (Category Consolidation)` dan Modified By `System`, satu per node Excess
32. Tutup Modal Changelog, buka Activity Log, dan filter Action `Marked as Excess (Category Consolidation)`
33. Verifikasi Activity Log memuat tiga baris baru dari baseline dengan Action `Marked as Excess (Category Consolidation)` dan Modified By `System`, satu per node Excess
34. Buka Detail User semua user relevan client CatPreT0 > Tab System Log
35. Verifikasi jumlah baris System Log Object `Categories` pada tiap user relevan sama dengan baseline langkah 26 (tidak ada baris karena tidak ada user aktor)

## Notes

- Spec melewati sekitar 35 langkah (35 langkah nominal, TC-FA-CAT-474 dan 475 sama-sama pola baca-log). Alasan: empat blok TC satu kelas (pencatatan log kategori) yang berdiri sendiri; 17 langkah di antaranya adalah blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) yang tidak dihitung terhadap ambang (prinsip 13 bagian 3).
- P-1: asersi "tidak ada baris System Log" pada TC-FA-CAT-469 butir b berada di spec ini sebagai asersi jumlah dengan baseline (langkah 26 dan 35) karena konteksnya (time-travel T-0 dan Fallback yang baru dibangun) tidak dapat dibentuk ulang di spec absence tanpa biaya; anchor positifnya adalah baris Changelog dan Activity Log (langkah 31 dan 33).
- Langkah penghubung (S-03, S-09, R-16): membuka surface dan mencari entri (langkah 1, 3, 5, 7, 9, 11, 16, 18, 22, 24, 30, 32, 34), langkah 26 (baseline), langkah 27 sampai 29 (pemicu T-0, polling, dan pemulihan jam), langkah 28 mengikuti idiom polling bagian 6.
- Urutan: TC-FA-CAT-474 dan 475 (hanya baca) mendahului TC-FA-CAT-476 yang mengubah dan menghapus record hasil Import; TC-FA-CAT-469 di akhir karena ganti akun dan time-travel (S-10).
- Langkah 20 dan 21: TC-FA-CAT-476 menulis "Delete family menampilkan dialog D-08" sehingga spec menghapus `Import Cat Edited` beserta `Import Cat Child` dalam satu aksi.
- Langkah 31 dan 33: jumlah tiga node Excess diturunkan dari Pre-setup #32 (8 kategori usable, cap baru 5); TC-FA-CAT-469 hanya menyebut "per node Excess".
- Temuan untuk QA:
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan, termasuk untuk client CatPreT0.
  - TC-FA-CAT-474 menyebut "user pelaku Import" dan "aktor yang menjalankan Import" tanpa identitas; Pre-setup #38 hanya menyebut "Import Data" sehingga akun dan email pelaku Import tidak tertulis (disediakan tim FE).
  - TC-FA-CAT-476 langkah 2 ("Hapus `Import Cat Child` lalu `Import Cat Edited`") menghapus anak terlebih dahulu, sehingga dialog D-08 untuk keluarga (Expected) tidak akan muncul pada penghapusan induk berikutnya; spec menghapus induk beserta anak dalam satu aksi agar sesuai Expected.
  - TC-FA-CAT-476 Expected "log Edit" tidak menyebut kolomnya; spec memverifikasi baris Edit Field `Category Name`.
  - TC-FA-CAT-469 Expected b ("Tidak ada baris di System Log user mana pun") tidak menyebut daftar user relevan dan baseline; spec memakai daftar user relevan yang disediakan tim FE/BE dan baseline langkah 26. TC-FA-CAT-469 tidak menyebut cara membuat "T-0 tiba tanpa seleksi"; kemampuan time-travel T-0 disediakan tim FE/BE.
