---
id: TC-FA-LIC-E2E-168-konkurensi-dua-sesi-registrasi-aset-remove-dan-pool-organisasi
title: "Konkurensi Dua Sesi Total Control: Registrasi Aset, Remove Allocation, dan Pool Organisasi"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LIC-457
  - TC-FA-LIC-459
  - TC-FA-LIC-616
coverage:
  web: automated
---

# Konkurensi Dua Sesi Total Control: Registrasi Aset, Remove Allocation, dan Pool Organisasi

## Prerequisites

- Mode: FE+BE.
- Akun sesi A (aktor hook `before`): Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid (`License allocation per group` ON), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun sesi B: Total Control kedua (Pre-setup #22) `totalControlSecond_automated_{namaCompany}@qwertysystem.net` pada client yang sama, password dari `Spectra.env.FA_TC2_PASSWORD`. Sesi B dibuka sebagai konteks browser kedua di langkah 1 (hasil di sesi B diasersi) dan ditutup di langkah akhir (langkah 36). Nama env `FA_TC_PASSWORD` dan `FA_TC2_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup dan penyetel state): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup yang diubah spec: hierarki dan kuota #12 (Kantor Pusat dengan Divisi Logistik 500 (Gudang A), Divisi IT 100 dengan Used 60, Divisi Keuangan belum beralokasi, Remaining Kantor Pusat 200; Produksi 1500, Cabang Medan 1000, Unallocated Pool 200 dengan Total Asset Capacity 5000 dan Total Allocated 4800). Pemulihan oleh fixture BE pemulih (disediakan tim FE/BE) di hook `before` dan `after` serta di awal tiap blok TC (pengecualian S-06: alokasi grup Pre-setup bernama literal tidak dapat dimiliki spec, suite berjalan serial). Efek yang dicatat: Last Updated alokasi yang diedit dan entri baru di Changelog Allocation Quota, System Log, dan Activity Log bertambah permanen.
- Kemampuan teknis:
  - Dua sesi paralel (konteks browser B dan sesi API aktor B) pada client yang sama.
  - Fixture BE penyetel state: Divisi IT Allocated 100 dengan Used 60 (TC-FA-LIC-457 dan 459), 40 draf aset siap Submit di Divisi IT, dan 1 draf aset siap Submit di Divisi IT; draf disubmit lewat jalur registrasi aset modul terkait (disediakan tim FE; endpoint tidak dikarang).
  - "Hampir bersamaan" berarti sesi A menekan `[Save]` atau `[Submit]` lebih dulu, sesi B segera sesudahnya; urutan commit dikendalikan per blok.
- Pemicu dan konteks kedua adalah objek uji kelas c; spec ini tidak memakai `P-2` atau `P-7`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka konteks browser B, login sebagai Total Control kedua (#22), buka License > Allocation Quota

### TC-FA-LIC-457: Registrasi aset bersamaan dengan Edit Allocation: yang kalah dievaluasi ulang

2. Pulihkan Pre-setup #12 lewat fixture BE (Divisi IT Allocated 100 dengan Used 60, Remaining 40) dan siapkan 40 draf aset siap Submit di Divisi IT
3. Sesi B: klik node `Kantor Pusat`, klik `[Edit]` pada `Divisi IT`, isi `100` (tanpa perubahan), lalu isi `70`
4. Sesi A: submit 40 aset massal ke Divisi IT hingga registrasi tersimpan
5. Sesi B: klik `[Save]`
6. Verifikasi registrasi lebih dulu: Used by This Group Divisi IT `100`
7. Verifikasi Edit ke `70` ditolak V-FALIC-01 dengan nilai minimum `(100)`
8. Sesi B: klik `[×]` pada modal, verifikasi dialog `Unsaved Changes`, klik `[Leave]`
9. Pulihkan Pre-setup #12 lewat fixture BE (Divisi IT Allocated 100 dengan Used 60) dan siapkan 40 draf aset siap Submit di Divisi IT
10. Sesi B: klik `[Edit]` pada `Divisi IT`, isi `70`, klik `[Save]` hingga Edit tersimpan
11. Sesi A: submit 40 aset massal ke Divisi IT
12. Verifikasi Edit lebih dulu: registrasi ditolak `QUOTA_EXCEEDED` dengan sisa slot terbaru `10`

### TC-FA-LIC-459: Remove Allocation bersamaan dengan registrasi ke grup yang sama

13. Pulihkan Pre-setup #12 lewat fixture BE (Divisi IT Allocated 100 dengan Used 60) dan siapkan 1 draf aset siap Submit di Divisi IT
14. Sesi A: klik node `Kantor Pusat`
15. Catat Remaining Kantor Pusat (`200`, baseline TC-FA-LIC-459)
16. Sesi A: klik `[Edit]` pada `Divisi IT`, klik `[Clear Field]`; sesi B: buka draf aset di Divisi IT
17. Sesi A: klik `[Save]`
18. Sesi B: klik `[Submit]`
19. Verifikasi Remove Allocation `Divisi IT` berhasil: `Divisi IT` menampilkan `Not Allocated`
20. Verifikasi registrasi 1 aset berhasil
21. Verifikasi tidak ada duplikasi atau kehilangan Used: Used by This Group Divisi IT `61`
22. Sesi A: klik node `Kantor Pusat`
23. Verifikasi Remaining Kantor Pusat `239` (naik ke `240` karena alokasi `Divisi IT` dilepas, lalu berkurang 1 karena registrasi memakai Remaining Kantor Pusat)

### TC-FA-LIC-616: Edit dua grup level 1 bersamaan memperebutkan pool organisasi

24. Pulihkan Pre-setup #12 lewat fixture BE (Unallocated Pool 200)
25. Sesi A: klik node `All Groups`, klik `[Edit]` pada `Produksi` (1500); sesi B: klik node `All Groups`, klik `[Edit]` pada `Cabang Medan` (1000)
26. Sesi A: isi `1600` (naik 100); sesi B: isi `1150` (naik 150)
27. Sesi A: klik `[Save]`
28. Sesi B: klik `[Save]`
29. Verifikasi sesi A berhasil: Produksi `1600` dan sisa pool organisasi `100`
30. Verifikasi sesi B ditolak V-FALIC-03 `Total allocated quota exceeds organization total limit (1,100).` karena dievaluasi ulang terhadap sisa pool terbaru
31. Verifikasi modal B tetap terbuka dengan input `1150` dipertahankan
32. Verifikasi tidak ada dialog konflik versi
33. Buka License > Allocation Quota pada node All Groups, periksa Allocated Quota kedua grup
34. Verifikasi Allocated Quota Cabang Medan tetap `1000`
35. Sesi B: klik `[×]` pada modal, verifikasi dialog `Unsaved Changes`, klik `[Leave]`
36. Tutup konteks browser B dan hapus sesi login-nya

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 dan 36 membuka dan menutup konteks B (S-09); langkah 2, 9, 13, dan 24 memulihkan Pre-setup antar blok; langkah 8 dan 35 menutup form dirty (S-08); langkah 14 dan 22 memilih node `Kantor Pusat` dan langkah 15 mencatat baseline Remaining Kantor Pusat.
- Tiap blok dimulai dari pemulihan Pre-setup #12 lewat fixture BE sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. TC-FA-LIC-152, 158, 456, dan 458 ada di spec `TC-FA-LIC-E2E-113`.
- Temuan untuk QA:
  - TC-FA-LIC-457, 459, dan 616 berlabel Manual Only (dua sesi paralel); spec menjalankannya dengan urutan commit yang dikendalikan (sesi A lebih dulu, sesi B segera sesudahnya) dan kemampuan dua sesi dicatat di Prerequisites.
  - TC-FA-LIC-457 butir a menulis dua hasil bersyarat ("bila registrasi lebih dulu ... bila Edit lebih dulu ..."); spec menjalankan kedua urutan dengan pemulihan di antaranya (langkah 2 sampai 8 dan 9 sampai 12) dan tidak mengasersi nilai pesan V-FALIC-01 selain `(100)`. Sisa slot `10` pada langkah 12 dihitung dari Edit ke `70` dikurangi Used 60.
  - TC-FA-LIC-459 butir a ("tidak ada duplikasi atau kehilangan Used") tidak menyebut nilai; spec mengasersi Used `61` (60 + 1) dari Pre-setup.
  - TC-FA-LIC-616 menyebut "hampir bersamaan"; spec mengurutkan Save sesi A lalu sesi B.
  - TC-FA-LIC-459 butir a ("setelah Remove registrasi memakai Remaining Kantor Pusat") tidak menyebut nilai; spec mengasersi Remaining Kantor Pusat `239` dari baseline `200` (Pre-setup #12): Remove Allocation `Divisi IT` menaikkannya ke `240` (nilai yang sama dengan Remaining Kantor Pusat setelah Remove pada spec E2E-118) dan satu registrasi menguranginya 1.
- Alasan di atas 35 langkah (36 langkah): semua blok satu topik (konkurensi dua sesi registrasi aset dan Remove) dan berdiri sendiri; langkah di atas 35 berasal dari pencatatan baseline dan ganti akun eksplisit; kegagalan satu blok tidak membuat blok lain kehilangan makna.
