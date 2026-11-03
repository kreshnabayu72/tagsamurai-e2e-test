---
id: TC-FA-LIC-E2E-010-screening-sub-tab-subscription-history-kolom-isi-baris
title: "Screening Sub-Tab Subscription History: Kolom, Isi Baris, Status, Empty State, dan Loading"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-24
  - TC-FA-LIC-25
  - TC-FA-LIC-26
  - TC-FA-LIC-27
  - TC-FA-LIC-28
  - TC-FA-LIC-31
  - TC-FA-LIC-527
coverage:
  web: automated
---

# Screening Sub-Tab Subscription History: Kolom, Isi Baris, Status, Empty State, dan Loading

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (client PT Sejahtera, plan Professional (Paid), `License allocation per group` ON; General Settings `dd/MM/yy`; kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > License (Tab All License, sub-tab `Subscription History`) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #13: empat term Subscription (SUBS-20270101-00001 Pending, SUBS-20260101-00001 Active, SUBS-20250101-00001 Renewed, SUBS-20241201-00001 Converted), data kuota #12. Nilai dibaca dari `Fixture.fixedAssetLicense.*`; berkas fixture belum ada, disediakan tim FE.
- State yang diubah spec dan dipulihkan: tiga term berstatus Waiting for Approval, Rejected, dan Canceled (TC-FA-LIC-26), lima term berstatus Expired, Grace, Archive, Purge, dan Deleted (TC-FA-LIC-27), dan satu term plan custom `Growth — Custom` (TC-FA-LIC-28) ditambahkan lewat fixture BE pada client ini; bahasa UI diganti pada langkah 34. Hook `after` menghapus term tambahan, memulihkan Pre-setup #13, dan memulihkan bahasa UI. Fixture BE penyetel dan pemulih disediakan tim FE/BE.
- Kemampuan teknis: intercept jaringan yang menunda respons data riwayat 3 detik (TC-FA-LIC-527), dilepas segera sesudah pengamatan (langkah 20); bahasa UI lain yang didukung aplikasi tersedia untuk TC-FA-LIC-28.
- Hook dan kemampuan suite (flag Guided Tooltip seen, sesi API aktor, fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-LIC-24: Screening sub-tab Subscription History

1. Verifikasi Sub-Tab: `Subscription History` (aktif) | `Allocation History`
2. Verifikasi Title `Subscription History` dengan Subtitle `Record of subscription terms for this product.`
3. Verifikasi Toolbar: `Search | Filter | Download`
4. Verifikasi Kolom: `Subscription ID (sortable) | Plan (sortable) | Type (sortable) | Status (sortable) | Start Date (sortable) | End Date (sortable) | Plan Owner (sortable) | Column Visibility (⋯) (unsortable)`
5. Verifikasi kolom Actions kosong tanpa menu `⋯` per baris (tidak ada row action)
6. Verifikasi Footer: paginasi default 10 per halaman

### TC-FA-LIC-25: Isi baris Subscription History

7. Verifikasi urutan dari atas: SUBS-20270101-00001 (Pending), SUBS-20260101-00001 (Active), SUBS-20250101-00001 (Renewed), SUBS-20241201-00001 (Converted)
8. Verifikasi SUBS-20270101-00001: Plan `Professional`, Type `Paid` (teks biasa tanpa badge), Start Date 01/01/27, End Date 31/12/27, Plan Owner `PT Maju Bersama (Distributor)`
9. Verifikasi Status: SUBS-20270101-00001 `Pending` severity warning, SUBS-20260101-00001 `Active` severity success, SUBS-20250101-00001 `Renewed` severity primary
10. Verifikasi SUBS-20241201-00001: Plan `Enterprise`, Type `Trial` badge severity primary, Plan Owner `PT ABC (Principal)`
11. Verifikasi SUBS-20241201-00001: Status `Converted` severity primary
12. Verifikasi tanggal tampil mengikuti General Settings (`dd/MM/yy`)

### TC-FA-LIC-31: Empty state hasil Search kosong

13. Ketik Search `zzzz`, tekan Enter
14. Verifikasi ilustrasi empty state dengan Title `No results found` dan Description `Try adjusting your search or filter.`
15. Klik `(←)` pada kotak Search

### TC-FA-LIC-527: Skeleton loader saat memuat

16. Tunda respons data riwayat selama 3 detik lewat intercept jaringan
17. Muat ulang halaman License (F5), lalu buka sub-tab `Subscription History`
18. Verifikasi tabel Subscription History menampilkan skeleton loader selama memuat
19. Verifikasi setelah respons diterima skeleton diganti baris data (empat term)
20. Lepas intercept jaringan

### TC-FA-LIC-26: Hanya term yang sudah disetujui

21. Tambah term berstatus Waiting for Approval, Rejected, dan Canceled lewat fixture BE, lalu muat ulang halaman License
22. Verifikasi term Pre-setup #13 tetap tampil di tabel: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001, SUBS-20241201-00001
23. Verifikasi term berstatus Waiting for Approval, Rejected, dan Canceled tidak tampil di tabel
24. Buka Filter Panel
25. Buka opsi field Status
26. Verifikasi opsi filter Status memuat `Pending`, `Active`, `Renewed`, `Converted`
27. Verifikasi opsi filter Status tidak memuat Waiting for Approval, Rejected, dan Canceled

### TC-FA-LIC-27: Status Expired, Grace, Archive, Purge, dan Deleted

28. Tambah term berstatus Expired, Grace, Archive, Purge, dan Deleted lewat fixture BE, lalu muat ulang halaman License
29. Verifikasi kolom Status kelima baris tampil apa adanya dengan badge sesuai enum `license-allocation-subscription.md` §4.1.1
30. Verifikasi status dan tanggal tiap baris sama dengan data pada fixture (tanpa perhitungan ulang status atau tanggal)

### TC-FA-LIC-28: Plan custom memakai badge Custom

31. Tambah satu term dengan plan custom `Growth — Custom` lewat fixture BE, lalu muat ulang halaman License
32. Verifikasi nama plan custom `Growth — Custom` tampil verbatim beserta badge `Custom`
33. Verifikasi nama plan bawaan (`Professional`, `Enterprise`) tampil tanpa badge `Custom`
34. Ganti bahasa UI ke bahasa lain yang didukung
35. Verifikasi nama plan bawaan mengikuti terjemahan UI
36. Verifikasi nama plan custom tetap `Growth — Custom` (tidak diterjemahkan) dengan badge `Custom`
37. Pulihkan bahasa UI semula

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-24, 25, 26, 27, 28, 31, 527). Tidak ada TC hanya-BE di spec ini. TC-FA-LIC-22 dan TC-FA-LIC-32 (kegagalan memuat) tidak ada di spec ini.
- Urutan TC diubah dari urutan nomor: blok baca (TC-24, 25, 31, 527) di awal dan blok yang menambah term lewat fixture (TC-26, 27, 28) di akhir (S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 15 (menutup input Search dengan `(←)`), langkah 20 (melepas intercept), langkah 37 (memulihkan bahasa UI), serta muat ulang halaman License pada langkah 21, 28, 31. Pada langkah 17 sub-tab `Subscription History` dibuka sesudah muat ulang agar tampilan sama dengan langkah TC.
- Asersi pembanding di luar Expected TC (S-03): langkah 22 (term Pre-setup #13 tetap tampil) dan langkah 26 (opsi filter Status `Pending`, `Active`, `Renewed`, `Converted`) mendahului asersi absence pada langkah 23 dan 27 sebagai data pembanding pada surface yang sama. Opsi pada langkah 26 diturunkan dari status keempat term Pre-setup #13, karena TC-FA-LIC-26 butir b menulis opsi filter Status hanya memuat status yang tampil di tabel.
- Temuan untuk QA:
  - TC-28 langkah 2 menyebut "bahasa lain yang didukung" tanpa menyebut bahasa; Expected c tidak menyebut terjemahan nama plan bawaan. Langkah 35 mengasersi bahwa nama plan bawaan "mengikuti terjemahan UI" sesuai TC tanpa teks terjemahan konkret.
  - TC-27 butir b ("Tidak ada perhitungan ulang status atau tanggal oleh modul ini") tidak dapat diamati langsung di UI; langkah 30 membandingkan nilai UI dengan data fixture.
  - TC-26 dan TC-27 tidak menyebut apakah term fixture tambahan dihapus sesudah TC; pemulihan dilakukan oleh hook `after`.
- Alasan di atas sekitar 35 langkah (37 langkah): semua blok satu topik (sub-tab Subscription History) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah di atas 35 hanya dua `Verifikasi` pembanding absence dan langkah penghubung fixture serta muat ulang.
