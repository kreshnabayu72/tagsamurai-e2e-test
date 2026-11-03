---
id: TC-FA-LIC-E2E-114-konkurensi-registrasi-arrival-transfer-dan-aksi-manage
title: "Konkurensi Pemeriksaan Kuota Grup: Dua Registrasi, Registrasi dengan Arrival Transfer, dan Aksi Manage"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LIC-606
  - TC-FA-LIC-607
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
  - `Spectra.intercept()` hanya mengamati respons pemeriksaan kuota (tanpa mengubah respons) pada TC-FA-LIC-608.
  - "Hampir bersamaan" berarti sesi A bertindak lebih dulu hingga tersimpan, sesi B segera sesudahnya; urutan commit dikendalikan per blok.
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
11. Verifikasi Remaining `0` dan Used tidak melampaui Allocated Quota `100`

### TC-FA-LIC-607: Registrasi dengan approval (Reserved) bersamaan dengan Arrival transfer

12. Pulihkan Pre-setup #12 dan #20 lewat fixture BE: approval ON, `Gudang A` Used 99 (Remaining 1), draf aset siap Submit di `Gudang A`, satu aset Active ditransfer dari `Divisi IT` ke `Gudang A` berstatus In Transfer Process
13. Sesi A: siapkan Submit for Approval draf aset di `Gudang A`; sesi B: siapkan Confirm Receipt pada Arrival transfer ke `Gudang A`
14. Sesi A: klik `[Submit for Approval]` hingga hasilnya tersimpan
15. Sesi B: klik `[Confirm Receipt]`
16. Sesi A: buka License > Allocation Quota, klik node `Gudang A`
17. Verifikasi Submit for Approval lebih dulu: Reserved by This Group `Gudang A` `1`, Used `99`, Remaining `0`
18. Verifikasi Arrival ditolak `QUOTA_EXCEEDED` dan aset transfer tetap di `Divisi IT`
19. Verifikasi Used by This Group ditambah Reserved by This Group `Gudang A` tidak melampaui Allocated Quota `100`
20. Pulihkan Pre-setup #12 dan #20 lewat fixture BE (urutan sama dengan langkah 12)
21. Sesi B: klik `[Confirm Receipt]` hingga hasilnya tersimpan
22. Sesi A: klik `[Submit for Approval]`
23. Sesi A: buka License > Allocation Quota, klik node `Gudang A`
24. Verifikasi Arrival lebih dulu: Used by This Group `100`, Remaining `0`
25. Verifikasi Submit ditolak `Group quota exceeded. Available slots: 0. Please contact administrator to increase quota.`
26. Verifikasi Used by This Group ditambah Reserved by This Group `Gudang A` tidak melampaui Allocated Quota `100`

### TC-FA-LIC-608: Aksi Manage bersamaan dengan registrasi tanpa approval ke grup dengan satu sisa slot

27. Pulihkan Pre-setup #12, #20, dan #28 lewat fixture BE: approval OFF, `Divisi IT` Allocated 100 dengan Used by This Group 99 (Remaining 1), satu aset Unmanaged di `Divisi IT`, satu draf aset siap Submit di `Divisi IT`
28. Sesi A: siapkan aksi Manage atas satu aset Unmanaged di `Divisi IT` sesuai PRD modul aset; sesi B: siapkan Submit draf aset di `Divisi IT`
29. Pasang intercept pengamat pada respons pemeriksaan kuota
30. Sesi A: jalankan aksi Manage hingga hasilnya tersimpan
31. Sesi B: klik `[Submit]`
32. Verifikasi tepat satu permintaan memperoleh `OK` dari pemeriksaan kuota
33. Verifikasi permintaan lain memperoleh `QUOTA_EXCEEDED` dengan sisa slot 0 (`Group quota exceeded. Available slots: 0. Please contact administrator to increase quota.`)
34. Lepas intercept
35. Sesi A: buka License > Allocation Quota, klik node `Divisi IT`
36. Verifikasi Used by This Group ditambah Reserved by This Group `Divisi IT` tidak melampaui Allocated Quota `100` (Remaining tidak negatif)
37. Tutup konteks browser B dan hapus sesi login-nya

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 dan 37 membuka dan menutup konteks B (S-09); langkah 2, 12, 20, dan 27 memulihkan Pre-setup antar blok; langkah 34 melepas intercept segera setelah pengamatan selesai (S-09).
- TC-FA-LIC-607 butir b menulis dua hasil bersyarat; spec menjalankan kedua urutan commit dengan pemulihan di antaranya (langkah 12 sampai 19 dan 20 sampai 26).
- Spec di atas 35 langkah (37 langkah): alasan dipertahankan, seluruh blok adalah satu kelas harness (dua sesi paralel pada pemeriksaan kuota grup) dan berdiri sendiri; tiap blok dimulai dari pemulihan state lewat fixture BE sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-LIC-606, 607, dan 608 berlabel Manual Only (dua sesi paralel) dan memakai frasa "hampir bersamaan"; spec mengendalikan urutan commit (sesi A lebih dulu, sesi B sesudahnya).
  - TC-FA-LIC-607 butir b menyebut "copy penolakan dimiliki modul transfer"; spec mengasersi Arrival ditolak `QUOTA_EXCEEDED` tanpa teks pesan.
  - TC-FA-LIC-607 tidak menyebut tombol `[Submit for Approval]` dan `[Confirm Receipt]` secara literal ("Submit for Approval", "Confirm Receipt"); spec memakai label itu dari TC dan label tombol dimiliki modul registrasi dan transfer.
  - TC-FA-LIC-608 langkah 1 dan 2 bergantung pada aksi Manage yang belum ditulis di PRD modul aset (pemicu "sesuai PRD asset/"); asersi hanya pada nilai yang diturunkan dari PRD License.
