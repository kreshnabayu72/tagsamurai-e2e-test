---
id: TC-FA-LIC-E2E-113-konkurensi-dua-sesi-total-control-edit-remove
title: "Konkurensi Dua Sesi Total Control: Edit dan Remove Allocation Bersamaan"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LIC-152
  - TC-FA-LIC-158
  - TC-FA-LIC-456
  - TC-FA-LIC-458
coverage:
  web: automated
---

# Konkurensi Dua Sesi Total Control: Edit dan Remove Allocation Bersamaan

## Prerequisites

- Mode: FE+BE.
- Akun sesi A (aktor hook `before`): Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid (`License allocation per group` ON), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun sesi B: Total Control kedua (Pre-setup #22) `totalControlSecond_automated_{namaCompany}@qwertysystem.net` pada client yang sama, password dari `Spectra.env.FA_TC2_PASSWORD`. Sesi B dibuka sebagai konteks browser kedua di langkah 1 (hasil di sesi B diasersi) dan ditutup di langkah akhir (langkah 38); pada TC-FA-LIC-152 sesi B hanya memicu perubahan state sehingga memakai sesi API aktor. Nama env `FA_TC_PASSWORD` dan `FA_TC2_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup dan penyetel state): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup yang diubah spec: hierarki dan kuota #12 (Kantor Pusat dengan Divisi Logistik 500 (Gudang A), Divisi IT 100 dengan Used 60, Divisi Keuangan belum beralokasi, Remaining Kantor Pusat 200; Produksi 1500, Cabang Medan 1000, Unallocated Pool 200 dengan Total Asset Capacity 5000 dan Total Allocated 4800). Pemulihan oleh fixture BE pemulih (disediakan tim FE/BE) di hook `before` dan `after` serta di awal tiap blok TC (pengecualian S-06: alokasi grup Pre-setup bernama literal tidak dapat dimiliki spec, suite berjalan serial). Efek yang dicatat: Last Updated alokasi yang diedit dan entri baru di Changelog Allocation Quota, System Log, dan Activity Log bertambah permanen.
- Kemampuan teknis:
  - Dua sesi paralel (konteks browser B dan sesi API aktor B) pada client yang sama.
  - Fixture BE penyetel state: Gudang A tanpa alokasi dengan Used 100 (TC-FA-LIC-152).
  - "Hampir bersamaan" berarti sesi A menekan `[Save]` atau `[Submit]` lebih dulu, sesi B segera sesudahnya; urutan commit dikendalikan per blok.
- Pemicu dan konteks kedua adalah objek uji kelas c; spec ini tidak memakai `P-2` atau `P-7`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka konteks browser B, login sebagai Total Control kedua (#22), buka License > Allocation Quota

### TC-FA-LIC-152: Parent di-Remove oleh aktor lain saat modal Edit child terbuka

2. Pulihkan Pre-setup #12 lewat fixture BE (Gudang A tanpa alokasi dengan Used 100, Divisi Logistik beralokasi 500 tanpa child beralokasi)
3. Sesi A: klik node `Divisi Logistik`, klik `[Edit]` pada `Gudang A`, tanpa Save
4. Sesi B (API akun #22): hapus alokasi Divisi Logistik (kosongkan field, Save) hingga alokasi tersimpan
5. Tunggu aksi selesai
6. Sesi A: isi `120` (di atas Minimum Quota 100 dan di bawah Maximum Quota 150), klik `[Save]`
7. Verifikasi dialog blok `Cannot Edit Allocation` / `Allocate quota to the parent group first.` / `[OK]`
8. Verifikasi modal Edit tetap terbuka dengan input `120` dipertahankan
9. Klik `[OK]`
10. Verifikasi daftar di-refresh dan server menolak tanpa mengubah data: `Gudang A` tetap `Not Allocated`
11. Klik `[×]` pada modal
12. Verifikasi dialog `Unsaved Changes` tampil
13. Klik `[Leave]`

### TC-FA-LIC-158: Edit Allocation dua aktor bersamaan pada grup yang sama: last-write-wins

14. Pulihkan Pre-setup #12 lewat fixture BE
15. Sesi A dan B: klik node `Kantor Pusat`, klik `[Edit]` pada `Divisi Logistik` (modal Edit terbuka di kedua sesi)
16. Sesi A: isi `600`, klik `[Save]`
17. Sesi B: isi `650`, klik `[Save]`
18. Verifikasi pada sesi B Save diterima (tidak ada penolakan Minimum Quota atau Maximum Quota)
19. Verifikasi Allocated Quota `Divisi Logistik` `650` (Save terakhir menimpa)
20. Verifikasi tidak ada dialog konflik versi

### TC-FA-LIC-456: Edit sibling bersamaan memperebutkan Remaining parent: pihak kalah ditolak V-FALIC-02

21. Pulihkan Pre-setup #12 lewat fixture BE (Remaining Kantor Pusat 200)
22. Sesi A: klik node `Kantor Pusat`, klik `[Edit]` pada `Divisi IT` (100); sesi B: klik node `Kantor Pusat`, klik `[Edit]` pada `Divisi Keuangan` (belum beralokasi)
23. Sesi A: isi `250` (naik 150); sesi B: isi `100`
24. Sesi A: klik `[Save]`
25. Sesi B: klik `[Save]`
26. Verifikasi sesi A berhasil: Remaining Kantor Pusat `50`
27. Verifikasi sesi B ditolak V-FALIC-02 `Allocated quota exceeds the maximum allowed for this group (50).` karena dievaluasi ulang terhadap Remaining terbaru
28. Verifikasi tidak ada dialog konflik versi
29. Sesi B: klik `[×]` pada modal
30. Sesi B: verifikasi dialog `Unsaved Changes` tampil
31. Sesi B: klik `[Leave]`

### TC-FA-LIC-458: Parent turun bersamaan dengan child naik: dikunci per parent beralokasi

32. Pulihkan Pre-setup #12 lewat fixture BE
33. Sesi A: klik node `All Groups`, klik `[Edit]` pada `Kantor Pusat`, isi `1300`; sesi B: klik node `Kantor Pusat`, klik `[Edit]` pada `Divisi IT`, isi `150`
34. Sesi A: klik `[Save]`
35. Sesi B: klik `[Save]`
36. Verifikasi pihak yang kalah menerima V-FALIC-01 atau V-FALIC-02 (V-FALIC-03 bila yang kalah Edit grup level 1)
37. Verifikasi Allocated Quota Kantor Pusat tidak di bawah Allocated to Subgroups terbaru
38. Tutup konteks browser B dan hapus sesi login-nya

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 dan 38 membuka dan menutup konteks B (S-09); langkah 2, 14, 21, dan 32 memulihkan Pre-setup antar blok; langkah 5 menunggu aksi sesi B selesai sebelum sesi A menyimpan (bagian 8b butir 8); langkah 11 dan 29 menutup form dirty (S-08).
- Tiap blok dimulai dari pemulihan Pre-setup #12 lewat fixture BE sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. TC-FA-LIC-457, 459, dan 616 ada di spec `TC-FA-LIC-E2E-168`.
- Temuan untuk QA:
  - TC-FA-LIC-152, 158, 456, dan 458 berlabel Manual Only (dua sesi paralel); spec menjalankannya dengan urutan commit yang dikendalikan (sesi A lebih dulu, sesi B segera sesudahnya) dan kemampuan dua sesi dicatat di Prerequisites.
  - TC-FA-LIC-152 butir c ("daftar di-refresh") tidak menyebut isi daftar; spec mengasersi Gudang A tetap `Not Allocated` sebagai bukti data tidak berubah.
  - TC-FA-LIC-158 butir b ("Minimum dan Maximum Quota dievaluasi ulang saat submit") tidak dapat diamati dari UI selain Save sesi B diterima; spec mengasersi tidak ada penolakan.
  - TC-FA-LIC-458 butir a tidak menyebut nilai awal Kantor Pusat dan menulis pihak kalah dengan beberapa kemungkinan pesan; spec mengasersi kemungkinan itu sebagai satu klausa (langkah 36).
  - TC-FA-LIC-456 menyebut "hampir bersamaan"; spec mengurutkan Save sesi A lalu sesi B.
- Alasan di atas 35 langkah (38 langkah): semua blok satu topik (konkurensi dua sesi Edit dan Remove) dan berdiri sendiri; langkah di atas 35 berasal dari ganti akun eksplisit antar sesi; kegagalan satu blok tidak membuat blok lain kehilangan makna.
