---
id: TC-FA-SU-E2E-360-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-1
title: "Resilience Baca: Empty State, Loading, dan Error Load Surface Tabel (Bagian 1)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-406
  - TC-FA-SU-440
coverage:
  web: automated
---

# Resilience Baca: Empty State, Loading, dan Error Load Surface Tabel (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Kelas harness: b (fault injection pada pembacaan data, resilience baca). Data Pre-setup: Client `FaUserMain` (#20), Transaction Role (#39), Responsibilities (#24). Pengguna tanpa data pada surface Detail: Hana Kusuma (Pending Activation) dari Client `FaUserMain`.
- Kemampuan teknis: `Spectra.intercept()` atas respons HTTP data surface di atas backend nyata (ditahan lambat, lalu respons 500); intercept dilepas oleh langkah `Lepas intercept` dan hook `after` melepasnya lagi sebagai cadangan, sehingga spec lain tidak terpengaruh. Keyword Search tanpa hasil `zzzz` dipilih spec. Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pelepasan intercept.

## Test Steps

### TC-FA-SU-406: Empty state, hasil pencarian kosong, loading, dan error load Sub-tab Transaction Role

1. Buka Detail Hana Kusuma > Tab Role > Sub-tab Transaction Role
2. Verifikasi data kosong sungguhan menampilkan ilustrasi 100x100 dengan Title `No transaction role yet` dan Description `Transaction roles assigned to this user will appear here.`
3. Ketik Search `zzzz`, tekan Enter
4. Verifikasi Search tanpa hasil menampilkan Title `No results found` dan Description `Try adjusting your search or filter.`
5. Atur intercept respons data Sub-tab Transaction Role menjadi lambat (ditahan)
6. Buka ulang Detail Hana Kusuma > Tab Role > Sub-tab Transaction Role
7. Verifikasi saat memuat, skeleton 5 baris sesuai kolom aktual tampil
8. Ganti intercept respons data Sub-tab Transaction Role menjadi 500
9. Buka ulang Detail Hana Kusuma > Tab Role > Sub-tab Transaction Role
10. Verifikasi fetch gagal menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
11. Verifikasi tampilan fetch gagal bukan empty state
12. Lepas intercept respons data Sub-tab Transaction Role
13. Klik `[Try Again]`
14. Verifikasi `[Try Again]` memuat ulang data: pesan `Unable to load this data.` tidak lagi tampil

### TC-FA-SU-440: Empty state, hasil pencarian kosong, loading, dan error load Sub-tab Borrowed Assets

15. Buka Detail Hana Kusuma > Tab Responsibilities > Sub-tab Borrowed Assets
16. Verifikasi data kosong sungguhan menampilkan ilustrasi 100x100 dengan Title `No borrowed assets` dan Description `This user has no borrowed assets currently.`
17. Ketik Search `zzzz`, tekan Enter
18. Verifikasi Search tanpa hasil menampilkan Title `No results found` dan Description `Try adjusting your search or filter.`
19. Atur intercept respons data Sub-tab Borrowed Assets menjadi lambat (ditahan)
20. Buka ulang Detail Hana Kusuma > Tab Responsibilities > Sub-tab Borrowed Assets
21. Verifikasi saat memuat, skeleton 5 baris sesuai kolom aktual tampil
22. Ganti intercept respons data Sub-tab Borrowed Assets menjadi 500
23. Buka ulang Detail Hana Kusuma > Tab Responsibilities > Sub-tab Borrowed Assets
24. Verifikasi fetch gagal menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
25. Verifikasi tampilan fetch gagal bukan empty state
26. Lepas intercept respons data Sub-tab Borrowed Assets
27. Klik `[Try Again]`
28. Verifikasi `[Try Again]` memuat ulang data: pesan `Unable to load this data.` tidak lagi tampil

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; tiap TC memakai surface-nya sendiri sehingga kegagalan satu blok tidak mengubah state blok lain.
- Mode FE+BE: kegagalan dipaksa dengan `Spectra.intercept()` parsial di atas backend nyata (bagian 6 konvensi), bukan seluruh API di-mock. Kelas b (resilience) dikumpulkan per jenis aksi baca atau unduh; kelas lain tidak ada di spec ini.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): membuka ulang surface sebelum tiap kondisi lambat dan 500 (supaya permintaan data dikirim ulang dan Search tidak terbawa), serta mengatur, mengganti, dan melepas intercept (pemicu, bukan objek asersi).
- Pembagian TC lintas spec:
  - TC-FA-SU-440: format dan nama berkas TC-FA-SU-435 di spec 147, transformasi data TC-FA-SU-437 di spec 370, Download gagal TC-FA-SU-438 di spec 366.
- Pemetaan butir Expected: butir a, b, c, dan d TC masing-masing menjadi satu `Verifikasi` (butir d dipecah per klausa: tampilan fetch gagal beserta `[Try Again]`, bukan empty state, dan `[Try Again]` memuat ulang data).
- Temuan untuk QA (S-15):
  - TC-FA-SU-406: precondition b menyebut halaman target Yuda Pratama, sedangkan Langkah Uji 1 membuka pengguna tanpa data (Hana Kusuma); spec mengikuti Langkah Uji 1.
  - TC-FA-SU-440: precondition b menyebut halaman target Budi Santoso, sedangkan Langkah Uji 1 membuka pengguna tanpa data (Hana Kusuma); spec mengikuti Langkah Uji 1.
  - TC-FA-SU-406: Pre-setup #39 tidak mencantumkan Transaction Role untuk Hana Kusuma, sehingga "tanpa data" disimpulkan dari ketiadaannya.
  - Keyword Search tanpa hasil, cara melambatkan respons, dan jeda tahan tidak diberi nilai oleh TC; spec memakai `zzzz` dan intercept ditahan sampai kondisi `Verifikasi` selesai. Butir b menyebut "Search atau Filter" tanpa hasil, sedangkan Langkah Uji hanya memakai keyword (Search); Filter tanpa hasil tidak dijalankan.
  - Hasil akhir `[Try Again]` (butir d, "memuat ulang data") tidak dinyatakan TC; spec mengasersi pesan `Unable to load this data.` tidak lagi tampil setelah intercept dilepas. Langkah Uji "Ulangi" ditafsirkan sebagai membuka ulang surface (Search tidak terbawa) karena TC tidak menyatakan apakah keyword Search bertahan setelah muat ulang.
