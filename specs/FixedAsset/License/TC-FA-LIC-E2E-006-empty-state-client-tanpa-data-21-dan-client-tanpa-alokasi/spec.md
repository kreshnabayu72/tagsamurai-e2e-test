---
id: TC-FA-LIC-E2E-006-empty-state-client-tanpa-data-21-dan-client-tanpa-alokasi
title: "Empty State Client Tanpa Data dan Client Tanpa Alokasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-18
  - TC-FA-LIC-30
  - TC-FA-LIC-38
  - TC-FA-LIC-58
  - TC-FA-LIC-68
  - TC-FA-LIC-540
  - TC-FA-LIC-542
  - TC-FA-LIC-543
  - TC-FA-LIC-584
coverage:
  web: automated
---

# Empty State Client Tanpa Data dan Client Tanpa Alokasi

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control client baru Pre-setup #21 `newClient_automated_{namaCompany}@qwertysystem.net` (plan Paid, tanpa sesi aktif, tanpa grup/data; kredensial `Spectra.env.FA_NEWCLIENT_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > License dibuka hook `beforeEach` suite.
- Akun aktor kedua (ganti akun eksplisit di langkah 18 sampai 20): Total Control client Paid tanpa alokasi Pre-setup #23 `totalControlNoAlloc_automated_{namaCompany}@qwertysystem.net` (Subscription ada, tanpa alokasi Asset License maupun addon, tanpa aset Unmanaged, Active, maupun Waiting for Approval; kredensial `Spectra.env.FA_NOALLOC_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite (Total Control Pre-setup #1).
- State yang diubah spec dan dipulihkan: plan client #21 disetel Paid dengan `License allocation per group` ON lewat fixture BE (TC-FA-LIC-58 meminta "Pre-setup #21 diubah plan Paid"); hook `after` memulihkan plan dan toggle ke keadaan awal. Fixture BE penyetel plan dan kemampuan membuat client #21 tanpa sesi aktif disediakan tim FE/BE.
- Data: tidak ada data yang dibuat; client #21 dan #23 hanya dibaca. Berkas `fixtures/` untuk Pre-setup License (`Fixture.fixedAssetLicense.*`) belum ada; disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip seen, sesi API aktor, fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### Client #21: Subscription History (TC-FA-LIC-30)

1. Setel plan client #21 ke Paid dengan `License allocation per group` ON lewat fixture BE
2. Muat ulang halaman License
3. Verifikasi sub-tab `Subscription History`: ilustrasi empty state dengan Title `No subscription history yet` dan Description `Subscription terms for this product will appear here.`

### Client #21: Allocation Quota tanpa grup (TC-FA-LIC-58)

4. Klik Tab `Allocation Quota`
5. Verifikasi Section 2 `Level 1 Groups Quota`: ilustrasi empty state dengan Title `No groups yet` dan Description `Groups will appear here once created.`

### Client #21: Concurrent User tanpa sesi (TC-FA-LIC-68)

6. Klik Tab `Concurrent User`
7. Verifikasi ilustrasi empty state dengan Title `No active sessions` dan Description `There are currently no active user sessions.`

### Client #21: Changelog Allocation Quota tanpa entri (TC-FA-LIC-540)

8. Klik Tab `Allocation Quota`
9. Klik ikon Changelog pada toolbar Section 2
10. Verifikasi modal `Changelog: Allocation Quota` terbuka
11. Verifikasi modal: ilustrasi empty state dengan Title `No changelog yet` dan Description `Activities and changes will appear here.`
12. Tutup modal `Changelog: Allocation Quota` dengan `[×]`

### Client #21: Changelog Concurrent User tanpa entri (TC-FA-LIC-584)

13. Klik Tab `Concurrent User`
14. Klik ikon Changelog pada toolbar
15. Verifikasi modal `Changelog: Concurrent User` terbuka
16. Verifikasi modal: ilustrasi empty state dengan Title `No changelog yet` dan Description `Activities and changes will appear here.`
17. Tutup modal `Changelog: Concurrent User` dengan `[×]`

### Client #23: License Summary dan Allocation History tanpa alokasi (TC-FA-LIC-18, 542, 38, 543)

18. Ganti akun: Logout
19. Login sebagai Total Control client Paid tanpa alokasi Pre-setup #23 (`Spectra.env.FA_NOALLOC_TC_PASSWORD`)
20. Klik menu License pada sidebar
21. Verifikasi baris `Unmanaged` kolom `Asset` tampil dengan nilai `0`
22. Verifikasi baris `Total`, `Used`, `Reserved`, dan `Remaining` kolom `Asset` bernilai `0` (bukan `—` dan bukan `Not Available`)
23. Verifikasi baris `Unmanaged` kolom `Asset` bernilai `0`
24. Verifikasi kolom addon `Not Available` pada baris `Total`
25. Verifikasi kolom addon `—` pada baris lainnya
26. Klik sub-tab `Subscription History`
27. Verifikasi Subscription History berisi baris
28. Klik sub-tab `Allocation History`
29. Verifikasi Allocation History: ilustrasi empty state dengan Title `No allocation history yet` dan Description `Asset license and add-on quota allocations will appear here.`
30. Klik Tab `Allocation Quota`
31. Verifikasi Section 1 `All License` node `All Groups`: baris `Total`, `Used`, `Reserved`, dan `Remaining` kolom `Asset` bernilai `0`

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-18, 30, 38, 58, 68, 540, 542, 543, 584). Tidak ada TC hanya-BE di spec ini.
- Urutan TC diubah dari urutan nomor agar semua blok client #21 berurutan sebelum satu kali ganti akun ke #23 (S-07).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 1 dan 2 (menyetel plan Paid, TC-58), langkah 12 dan 17 (menutup modal Changelog), langkah 18 sampai 20 (ganti akun dan membuka License), langkah 26 (klik sub-tab `Subscription History` sebagai langkah TC-38), serta klik tab pada langkah 4, 6, 8, 13, 30.
- Langkah 21 (TC-18) dan langkah 23 (TC-542 butir b) mengasersi baris `Unmanaged` kolom `Asset` bernilai `0` karena masing-masing TC memiliki Expected sendiri.
- Temuan untuk QA:
  - TC-58 menyebut "Pre-setup #21 diubah plan Paid", sedangkan Pre-setup #21 sudah berplan Paid dan TC-30 memakai client yang sama dengan Subscription History tampil; spec hanya memastikan plan Paid dengan `License allocation per group` ON lewat fixture BE.
  - TC-68 Precondition kontradiktif ("tanpa sesi aktif selain milik aktor tidak berlaku: gunakan client dengan nol sesi") karena aktor yang login memiliki sesi web sendiri; spec memakai client #21 dan mengasumsikan fixture tabel sesi client ini kosong tanpa menghitung sesi UI aktor. Langkah TC "setelah semua sesi berakhir" tidak ditulis sebagai langkah.
  - TC-540 dan TC-584 mensyaratkan client tanpa entri Changelog; spec mengasumsikan client #21 tidak pernah diubah sehingga entri Changelog Allocation Quota dan Concurrent User kosong; TC tidak menyatakan apakah penyetelan plan pada langkah 1 mencatat entri Changelog.
