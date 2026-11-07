---
id: TC-FA-SU-E2E-364-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-5
title: "Resilience Baca: Empty State, Loading, dan Error Load Surface Tabel (Bagian 5)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-764
  - TC-FA-SU-795
coverage:
  web: automated
---

# Resilience Baca: Empty State, Loading, dan Error Load Surface Tabel (Bagian 5)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Kelas harness: b (fault injection pada pembacaan data, resilience baca). Data Pre-setup: Client `FaUserMain` (#20), System Log (#28), Transaction Admin Log (#29). Pengguna tanpa data pada surface Detail: Hana Kusuma (Pending Activation) dari Client `FaUserMain`.
- Kemampuan teknis: `Spectra.intercept()` atas respons HTTP data surface di atas backend nyata (ditahan lambat, lalu respons 500); intercept dilepas oleh langkah `Lepas intercept` dan hook `after` melepasnya lagi sebagai cadangan, sehingga spec lain tidak terpengaruh. Keyword Search tanpa hasil `zzzz` dipilih spec. Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pelepasan intercept.

## Test Steps

### TC-FA-SU-764: Empty state, hasil pencarian kosong, loading, dan error load Tab System Log

1. Ketik Search `Hana Kusuma`, tekan Enter, lalu buka Detail Hana Kusuma > Tab System Log
2. Verifikasi data kosong sungguhan menampilkan ilustrasi 100x100 dengan Title `No system logs recorded` dan Description `Security and audit trail records will appear here.`
3. Ketik Search `zzzz`, tekan Enter
4. Verifikasi Search tanpa hasil menampilkan Title `No results found` dan Description `Try adjusting your search or filter.`
5. Atur intercept respons data Tab System Log menjadi lambat (ditahan)
6. Buka ulang Detail Hana Kusuma > Tab System Log
7. Verifikasi saat memuat, skeleton 5 baris sesuai kolom aktual tampil
8. Ganti intercept respons data Tab System Log menjadi 500
9. Buka ulang Detail Hana Kusuma > Tab System Log
10. Verifikasi fetch gagal menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
11. Verifikasi tampilan fetch gagal bukan empty state
12. Lepas intercept respons data Tab System Log
13. Klik `[Try Again]`
14. Verifikasi `[Try Again]` memuat ulang data: pesan `Unable to load this data.` tidak lagi tampil

### TC-FA-SU-795: Empty state, hasil pencarian kosong, loading, dan error load Tab Transaction Admin Log sub-tab Borrowing & Assignment

15. Buka Detail Hana Kusuma > Tab Transaction Admin Log > Sub-tab Borrowing & Assignment
16. Verifikasi data kosong sungguhan menampilkan ilustrasi 100x100 dengan Title `No transaction log yet` dan Description `Transactions this user has processed as PIC will appear here.`
17. Ketik Search `zzzz`, tekan Enter
18. Verifikasi Search tanpa hasil menampilkan Title `No results found` dan Description `Try adjusting your search or filter.`
19. Atur intercept respons data Tab Transaction Admin Log sub-tab Borrowing & Assignment menjadi lambat (ditahan)
20. Buka ulang Detail Hana Kusuma > Tab Transaction Admin Log > Sub-tab Borrowing & Assignment
21. Verifikasi saat memuat, skeleton 5 baris sesuai kolom aktual tampil
22. Ganti intercept respons data Tab Transaction Admin Log sub-tab Borrowing & Assignment menjadi 500
23. Buka ulang Detail Hana Kusuma > Tab Transaction Admin Log > Sub-tab Borrowing & Assignment
24. Verifikasi fetch gagal menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
25. Verifikasi tampilan fetch gagal bukan empty state
26. Lepas intercept respons data Tab Transaction Admin Log sub-tab Borrowing & Assignment
27. Klik `[Try Again]`
28. Verifikasi `[Try Again]` memuat ulang data: pesan `Unable to load this data.` tidak lagi tampil

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; tiap TC memakai surface-nya sendiri sehingga kegagalan satu blok tidak mengubah state blok lain.
- Mode FE+BE: kegagalan dipaksa dengan `Spectra.intercept()` parsial di atas backend nyata (bagian 6 konvensi), bukan seluruh API di-mock. Kelas b (resilience) dikumpulkan per jenis aksi baca atau unduh; kelas lain tidak ada di spec ini.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): membuka ulang surface sebelum tiap kondisi lambat dan 500 (supaya permintaan data dikirim ulang dan Search tidak terbawa), serta mengatur, mengganti, dan melepas intercept (pemicu, bukan objek asersi).
- Langkah penghubung tambahan (S-03): Search nama `Hana Kusuma` di User List supaya baris target tidak bergantung posisi halaman (langkah 1, 8b butir 13, R-16).
- Pembagian TC lintas spec:
  - TC-FA-SU-764: format dan nama berkas TC-FA-SU-759 di spec 250, transformasi data TC-FA-SU-761 di spec 373, Download gagal TC-FA-SU-762 di spec 368.
  - TC-FA-SU-795: format dan nama berkas TC-FA-SU-790 di spec 262, transformasi data TC-FA-SU-792 di spec 373, Download gagal TC-FA-SU-793 di spec 368.
- Pemetaan butir Expected: butir a, b, c, dan d TC masing-masing menjadi satu `Verifikasi` (butir d dipecah per klausa: tampilan fetch gagal beserta `[Try Again]`, bukan empty state, dan `[Try Again]` memuat ulang data).
- Temuan untuk QA (S-15):
  - TC-FA-SU-764: precondition b menyebut halaman target Budi Santoso, sedangkan Langkah Uji 1 membuka pengguna tanpa data (Hana Kusuma); spec mengikuti Langkah Uji 1.
  - TC-FA-SU-795: precondition b menyebut halaman target Budi Santoso, sedangkan Langkah Uji 1 membuka pengguna tanpa data (Hana Kusuma); spec mengikuti Langkah Uji 1.
  - TC-FA-SU-764: Pre-setup #28 hanya mencantumkan System Log Budi Santoso (Hana Kusuma muncul sebagai target pada baris itu, bukan sebagai pemilik log); TC tidak menyatakan Tab System Log Hana Kusuma kosong.
  - TC-FA-SU-795: Pre-setup #29 hanya mencantumkan Transaction Admin Log Budi Santoso; Hana Kusuma kosong hanya tersirat.
  - Keyword Search tanpa hasil, cara melambatkan respons, dan jeda tahan tidak diberi nilai oleh TC; spec memakai `zzzz` dan intercept ditahan sampai kondisi `Verifikasi` selesai. Butir b menyebut "Search atau Filter" tanpa hasil, sedangkan Langkah Uji hanya memakai keyword (Search); Filter tanpa hasil tidak dijalankan.
  - Hasil akhir `[Try Again]` (butir d, "memuat ulang data") tidak dinyatakan TC; spec mengasersi pesan `Unable to load this data.` tidak lagi tampil setelah intercept dilepas. Langkah Uji "Ulangi" ditafsirkan sebagai membuka ulang surface (Search tidak terbawa) karena TC tidak menyatakan apakah keyword Search bertahan setelah muat ulang.
