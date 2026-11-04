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
- Akun sesi B: Total Control kedua (Pre-setup #22) `totalControlSecond_automated_{namaCompany}@qwertysystem.net` pada client yang sama, password dari `Spectra.env.FA_TC2_PASSWORD`. Sesi B dibuka sebagai konteks browser kedua di langkah 1 (hasil di sesi B diasersi) dan ditutup di langkah akhir (langkah 47). Nama env `FA_TC_PASSWORD` dan `FA_TC2_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
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
3. Sesi A: siapkan registrasi massal 40 aset ke Divisi IT tanpa klik `[Submit]`
4. Sesi B: klik node `Kantor Pusat`, klik `[Edit]` pada `Divisi IT`, isi `70` tanpa klik `[Save]`
5. Sesi A: klik `[Submit]` registrasi massal 40 aset hingga registrasi tersimpan
6. Verifikasi registrasi massal 40 aset berhasil
7. Sesi A: buka License > Allocation Quota dan klik node `Kantor Pusat`
8. Verifikasi Used by This Group Divisi IT `100`
9. Verifikasi Remaining Divisi IT `0`
10. Sesi B: klik `[Save]`
11. Verifikasi Edit sesi B ditolak V-FALIC-01 dengan pesan inline `Cannot set quota below used, reserved, and subgroup-allocated quota (100).`
12. Verifikasi modal sesi B tetap terbuka
13. Verifikasi input `70` dipertahankan pada modal sesi B
14. Verifikasi Allocated Quota Divisi IT tetap `100`
15. Verifikasi tidak ada toast sukses untuk sesi B
16. Verifikasi tidak ada dialog konflik versi
17. Sesi B: klik `[×]` pada modal
18. Verifikasi pada sesi B dialog `Unsaved Changes` tampil
19. Sesi B: klik `[Leave]`

### TC-FA-LIC-459: Remove Allocation bersamaan dengan registrasi ke grup yang sama

20. Pulihkan Pre-setup #12 lewat fixture BE (Divisi IT Allocated 100 dengan Used 60) dan siapkan 1 draf aset siap Submit di Divisi IT
21. Sesi A: klik node `Kantor Pusat`
22. Catat Remaining Kantor Pusat (`200`, baseline TC-FA-LIC-459)
23. Sesi A: klik `[Edit]` pada `Divisi IT`, klik `[Clear Field]`; sesi B: buka draf aset di Divisi IT
24. Sesi A: klik `[Save]`
25. Tunggu aksi selesai
26. Sesi B: klik `[Submit]`
27. Verifikasi Remove Allocation `Divisi IT` berhasil: `Divisi IT` menampilkan `Not Allocated`
28. Verifikasi registrasi 1 aset berhasil
29. Verifikasi tidak ada duplikasi atau kehilangan Used: Used by This Group Divisi IT `61`
30. Sesi A: klik node `Kantor Pusat`
31. Verifikasi Remaining Kantor Pusat `239` (naik ke `240` karena alokasi `Divisi IT` dilepas, lalu berkurang 1 karena registrasi memakai Remaining Kantor Pusat)

### TC-FA-LIC-616: Edit dua grup level 1 bersamaan memperebutkan pool organisasi

32. Pulihkan Pre-setup #12 lewat fixture BE (Unallocated Pool 200)
33. Sesi A: klik node `All Groups`, klik `[Edit]` pada `Produksi` (1500); sesi B: klik node `All Groups`, klik `[Edit]` pada `Cabang Medan` (1000)
34. Sesi A: isi `1600` (naik 100); sesi B: isi `1150` (naik 150)
35. Sesi A: klik `[Save]`
36. Tunggu aksi selesai
37. Sesi B: klik `[Save]`
38. Verifikasi sesi A berhasil: Produksi `1600` dan sisa pool organisasi `100`
39. Verifikasi sesi B ditolak V-FALIC-03 `Total allocated quota exceeds organization total limit (1,100).` karena dievaluasi ulang terhadap sisa pool terbaru
40. Verifikasi modal B tetap terbuka dengan input `1150` dipertahankan
41. Verifikasi tidak ada dialog konflik versi
42. Buka License > Allocation Quota pada node All Groups, periksa Allocated Quota kedua grup
43. Verifikasi Allocated Quota Cabang Medan tetap `1000`
44. Sesi B: klik `[×]` pada modal
45. Verifikasi pada sesi B dialog `Unsaved Changes` tampil
46. Sesi B: klik `[Leave]`
47. Tutup konteks browser B dan hapus sesi login-nya

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 dan 47 membuka dan menutup konteks B (S-09); langkah 2, 20, dan 32 memulihkan Pre-setup antar blok; langkah 17 sampai 19 dan 44 sampai 46 menutup form dirty (S-08); langkah 21 dan 30 memilih node `Kantor Pusat` dan langkah 22 mencatat baseline Remaining Kantor Pusat.
- Asersi di luar Expected TC (S-03; 8b.8): langkah 25 dan 36 "Tunggu aksi selesai" (tanpa `Verifikasi`) memastikan `[Save]` sesi A selesai sebelum sesi B bertindak pada TC-FA-LIC-459 dan TC-FA-LIC-616; TC tidak menyebut langkah tunggu, tetapi tanpa itu hasil bergantung pada balapan.
- Tiap blok dimulai dari pemulihan Pre-setup #12 lewat fixture BE sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. TC-FA-LIC-152, 158, 456, dan 458 ada di spec `TC-FA-LIC-E2E-113`.
- Temuan untuk QA:
  - TC-FA-LIC-457, 459, dan 616 berlabel Manual Only (dua sesi paralel); spec menjalankannya dengan urutan commit yang dikendalikan (sesi A lebih dulu, sesi B segera sesudahnya) dan kemampuan dua sesi dicatat di Prerequisites.
  - TC-FA-LIC-457 menetapkan satu urutan (registrasi massal 40 aset lebih dulu, lalu Save sesi B ditolak V-FALIC-01 `(100)`); spec mengikutinya tanpa urutan kedua.
  - TC-FA-LIC-459 butir a ("tidak ada duplikasi atau kehilangan Used") tidak menyebut nilai; spec mengasersi Used `61` (60 + 1) dari Pre-setup.
  - TC-FA-LIC-459 butir a ("setelah Remove registrasi memakai Remaining Kantor Pusat") tidak menyebut nilai; spec mengasersi Remaining Kantor Pusat `239` dari baseline `200` (Pre-setup #12): Remove Allocation `Divisi IT` menaikkannya ke `240` (nilai yang sama dengan Remaining Kantor Pusat setelah Remove pada spec E2E-118) dan satu registrasi menguranginya 1.
- Alasan di atas 35 langkah (47 langkah): semua blok satu topik (konkurensi dua sesi registrasi aset dan Remove) dan berdiri sendiri; langkah di atas 35 berasal dari pencatatan baseline dan ganti akun eksplisit; kegagalan satu blok tidak membuat blok lain kehilangan makna.
