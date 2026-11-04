---
id: TC-FA-LIC-E2E-114-konkurensi-registrasi-arrival-transfer-dan-aksi-manage
title: "Konkurensi Pemeriksaan Kuota Grup: Dua Registrasi, Registrasi dengan Arrival Transfer, dan Aksi Manage"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LIC-606
  - TC-FA-LIC-607
  - TC-FA-LIC-622
  - TC-FA-LIC-608
coverage:
  web: automated
---

# Konkurensi Pemeriksaan Kuota Grup: Dua Registrasi, Registrasi dengan Arrival Transfer, dan Aksi Manage

## Prerequisites

- Mode: FE+BE.
- Akun sesi A (aktor hook `before`): Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid (`License allocation per group` ON), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun sesi B: Total Control kedua (Pre-setup #22) `totalControlSecond_automated_{namaCompany}@qwertysystem.net` pada client yang sama, password dari `Spectra.env.FA_TC2_PASSWORD`. Sesi B dibuka sebagai konteks browser kedua di langkah 1 (hasil di sesi B diasersi) dan ditutup di langkah akhir. Nama env `FA_TC_PASSWORD` dan `FA_TC2_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup dan penyetel state): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup yang diubah spec: hierarki dan kuota #12, draf aset siap Submit dan aset Active untuk Transfer #20, aset Unmanaged untuk aksi Manage #28. Pemulihan oleh fixture BE pemulih (disediakan tim FE/BE) di hook `before` dan `after` serta di awal tiap blok TC (pengecualian S-06: alokasi grup dan aset Pre-setup tidak dapat dimiliki spec, suite berjalan serial). Efek yang dicatat: Used dan Reserved grup, status aset, dan Last Updated berubah.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak dikarang):
  - Fixture BE penyetel state: approval OFF atau ON; `Divisi IT` Allocated 100 dengan Used by This Group 99 (Remaining 1); `Gudang A` Used 99 (Remaining 1, Allocated 100); satu draf aset siap Submit per sesi di grup target; satu aset Active di `Divisi IT` yang ditransfer ke `Gudang A` berstatus In Transfer Process; satu aset Unmanaged di `Divisi IT`.
  - Aksi Manage atas aset Unmanaged mengikuti PRD modul aset (pemicu disediakan tim FE).
  - `Spectra.intercept()` hanya mengamati respons pemeriksaan kuota (tanpa mengubah respons) pada TC-FA-LIC-607 dan TC-FA-LIC-608.
  - "Hampir bersamaan" berarti sesi yang ditentukan TC bertindak lebih dulu hingga hasilnya tersimpan, sesi lain segera sesudahnya; urutan commit dikendalikan per blok (TC-FA-LIC-606, 607, dan 608: sesi A lebih dulu; TC-FA-LIC-622: sesi B lebih dulu).
- Konteks kedua adalah objek uji kelas c; spec ini tidak memakai `P-2` atau `P-7`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka konteks browser B, login sebagai Total Control kedua (#22), buka License > Allocation Quota

### TC-FA-LIC-606: Dua registrasi tanpa approval bersamaan ke grup dengan satu sisa slot

2. Pulihkan Pre-setup #12 dan #20 lewat fixture BE: approval OFF, `Divisi IT` Allocated 100 dengan Used by This Group 99 (Remaining 1), satu draf aset siap Submit di `Divisi IT` per sesi
3. Sesi A dan B: buka draf aset masing-masing di `Divisi IT`
4. Sesi A: klik `[Submit]` hingga hasilnya tersimpan
5. Sesi B: klik `[Submit]`
6. Verifikasi Submit sesi A berhasil
7. Verifikasi Submit sesi B ditolak `QUOTA_EXCEEDED` dengan pesan `Group quota exceeded. Available slots: 0. Please contact administrator to increase quota.`
8. Verifikasi aset dari Submit yang ditolak tetap berstatus `Draft`
9. Sesi A: buka License > Allocation Quota, klik node `Divisi IT`
10. Verifikasi Used by This Group `100`
11. Verifikasi Remaining `0`
12. Verifikasi Used by This Group tidak melampaui Allocated Quota `100`

### TC-FA-LIC-607: Submit for Approval (Reserved) lebih dulu dari Arrival transfer

13. Pulihkan Pre-setup #12 dan #20 lewat fixture BE: approval ON, `Gudang A` Used 99 (Remaining 1), draf aset siap Submit di `Gudang A`, satu aset Active ditransfer dari `Divisi IT` ke `Gudang A` berstatus In Transfer Process
14. Sesi A: siapkan Submit for Approval draf aset di `Gudang A`; sesi B: siapkan Confirm Receipt pada Arrival transfer ke `Gudang A`
15. Pasang intercept pengamat pada respons pemeriksaan kuota
16. Sesi A: klik `[Submit for Approval]`
17. Verifikasi draf aset sesi A berstatus Waiting for Approval
18. Sesi B: klik `[Confirm Receipt]`
19. Verifikasi pemeriksaan kuota Confirm Receipt memperoleh `QUOTA_EXCEEDED` dengan sisa slot 0
20. Lepas intercept
21. Verifikasi transaksi transfer tetap In Transfer Process
22. Verifikasi aset transfer tetap di `Divisi IT`
23. Sesi A: buka License > Allocation Quota, klik node `Gudang A`
24. Verifikasi `Gudang A`: Used by This Group `99`, Reserved by This Group `1`, Remaining `0`
25. Verifikasi Used by This Group ditambah Reserved by This Group `Gudang A` tidak melampaui Allocated Quota `100`

### TC-FA-LIC-622: Arrival transfer lebih dulu dari Submit for Approval

26. Pulihkan Pre-setup #12 dan #20 lewat fixture BE (urutan sama dengan langkah 13)
27. Sesi A: siapkan Submit for Approval draf aset di `Gudang A`; sesi B: siapkan Confirm Receipt pada Arrival transfer ke `Gudang A`
28. Sesi B: klik `[Confirm Receipt]`
29. Verifikasi Confirm Receipt berhasil: aset transfer tiba di `Gudang A`
30. Sesi A: klik `[Submit for Approval]`
31. Verifikasi Submit for Approval ditolak `QUOTA_EXCEEDED` (V-FALIC-06) dengan pesan `Group quota exceeded. Available slots: 0. Please contact administrator to increase quota.`
32. Verifikasi draf aset sesi A tidak menjadi Waiting for Approval
33. Sesi A: buka License > Allocation Quota, klik node `Gudang A`
34. Verifikasi `Gudang A`: Used by This Group `100`, Reserved by This Group `0`, Remaining `0`
35. Verifikasi Used by This Group ditambah Reserved by This Group `Gudang A` tidak melampaui Allocated Quota `100`

### TC-FA-LIC-608: Aksi Manage bersamaan dengan registrasi tanpa approval ke grup dengan satu sisa slot

36. Pulihkan Pre-setup #12, #20, dan #28 lewat fixture BE: approval OFF, `Divisi IT` Allocated 100 dengan Used by This Group 99 (Remaining 1), satu aset Unmanaged di `Divisi IT`, satu draf aset siap Submit di `Divisi IT`
37. Sesi A: siapkan aksi Manage atas satu aset Unmanaged di `Divisi IT` sesuai PRD modul aset; sesi B: siapkan Submit draf aset di `Divisi IT`
38. Pasang intercept pengamat pada respons pemeriksaan kuota
39. Sesi A: jalankan aksi Manage hingga hasilnya tersimpan
40. Sesi B: klik `[Submit]`
41. Verifikasi tepat satu permintaan memperoleh `OK` dari pemeriksaan kuota
42. Verifikasi permintaan lain memperoleh `QUOTA_EXCEEDED` dengan sisa slot 0 (`Group quota exceeded. Available slots: 0. Please contact administrator to increase quota.`)
43. Lepas intercept
44. Sesi A: buka License > Allocation Quota, klik node `Divisi IT`
45. Verifikasi Used by This Group ditambah Reserved by This Group `Divisi IT` tidak melampaui Allocated Quota `100` (Remaining tidak negatif)
46. Tutup konteks browser B dan hapus sesi login-nya

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 dan 46 membuka dan menutup konteks B (S-09); langkah 2, 13, 26, dan 36 memulihkan Pre-setup antar blok; langkah 20 dan 43 melepas intercept segera setelah pengamatan selesai (S-09).
- TC-FA-LIC-607 (Submit for Approval lebih dulu) dan TC-FA-LIC-622 (Arrival transfer lebih dulu) adalah dua urutan commit dari skenario yang sama; fixture pemulih pada langkah 26 memulihkan state di antara keduanya.
- Spec di atas 35 langkah (46 langkah): alasan dipertahankan, seluruh blok adalah satu kelas harness (dua sesi paralel pada pemeriksaan kuota grup) dan berdiri sendiri; tiap blok dimulai dari pemulihan state lewat fixture BE sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-LIC-606, 607, 622, dan 608 berlabel Manual Only (dua sesi paralel) dan memakai frasa "hampir bersamaan"; spec mengendalikan urutan commit sesuai langkah TC.
  - TC-FA-LIC-607 butir b menyebut "copy penolakan dimiliki modul transfer"; spec mengasersi penolakan `QUOTA_EXCEEDED` sisa slot 0 pada respons pemeriksaan kuota tanpa teks pesan.
  - TC-FA-LIC-607 tidak menyebut tombol `[Submit for Approval]` dan `[Confirm Receipt]` secara literal ("Submit for Approval", "Confirm Receipt"); spec memakai label itu dari TC dan label tombol dimiliki modul registrasi dan transfer.
  - TC-FA-LIC-608 langkah 1 dan 2 bergantung pada aksi Manage yang belum ditulis di PRD modul aset (pemicu "sesuai PRD asset/"); asersi hanya pada nilai yang diturunkan dari PRD License.
