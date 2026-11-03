---
id: TC-FA-SU-E2E-362-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-3
title: "Resilience Baca: Empty State, Loading, dan Error Load Surface Tabel (Bagian 3)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-574
  - TC-FA-SU-606
coverage:
  web: automated
---

# Resilience Baca: Empty State, Loading, dan Error Load Surface Tabel (Bagian 3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Kelas harness: b (fault injection pada pembacaan data, resilience baca). Data Pre-setup: Client `FaUserMain` (#20), Non-Login User (#26), Changelog (#27). Pengguna milik spec (dibuat lewat seed API di hook `before`, dihapus di hook `after`; pengguna Pre-setup bersama tidak dipakai, S-06; disediakan tim FE): `Hana Kusuma {runId}-362`, email `hana.kusuma+{runId}-362@qwertysystem.net`, Pending Activation, tanpa Non-Login User yang diwakili dan tanpa riwayat Changelog (tidak ada aksi ke pengguna ini sebelum spec berjalan). Entri Changelog pengguna ini tidak ditulis spec lain karena namanya bersuffix unik per spec.
- Kemampuan teknis: `Spectra.intercept()` atas respons HTTP data surface di atas backend nyata (ditahan lambat, lalu respons 500); intercept dilepas oleh langkah `Lepas intercept` dan hook `after` melepasnya lagi sebagai cadangan, sehingga spec lain tidak terpengaruh. Keyword Search tanpa hasil `zzzz` dipilih spec. Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend selain seed dan hapus pengguna milik spec; tidak ada cleanup lain selain pelepasan intercept.

## Test Steps

### TC-FA-SU-574: Empty state, hasil pencarian kosong, loading, dan error load Tab Non-Login User

1. Ketik Search `Hana Kusuma {runId}-362`, tekan Enter, klik nama Hana Kusuma {runId}-362, lalu buka Tab Non-Login User
2. Verifikasi data kosong sungguhan menampilkan ilustrasi 100x100 dengan Title `No non-login users represented` dan Description `This user does not represent any non-login users.`
3. Ketik Search `zzzz`, tekan Enter
4. Verifikasi Search tanpa hasil menampilkan Title `No results found` dan Description `Try adjusting your search or filter.`
5. Atur intercept respons data Tab Non-Login User menjadi lambat (ditahan)
6. Buka ulang Detail Hana Kusuma {runId}-362 > Tab Non-Login User
7. Verifikasi saat memuat, skeleton 5 baris sesuai kolom aktual tampil
8. Ganti intercept respons data Tab Non-Login User menjadi 500
9. Buka ulang Detail Hana Kusuma {runId}-362 > Tab Non-Login User
10. Verifikasi fetch gagal menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
11. Verifikasi tampilan fetch gagal bukan empty state
12. Lepas intercept respons data Tab Non-Login User
13. Klik `[Try Again]`
14. Verifikasi `[Try Again]` memuat ulang data: pesan `Unable to load this data.` tidak lagi tampil

### TC-FA-SU-606: Empty state, hasil pencarian kosong, loading, dan error load Tab Changelog

15. Buka Detail Hana Kusuma {runId}-362 > Tab Changelog
16. Verifikasi data kosong sungguhan menampilkan ilustrasi 100x100 dengan Title `No changelog yet` dan Description `Activities and changes will appear here.`
17. Ketik Search `zzzz`, tekan Enter
18. Verifikasi Search tanpa hasil menampilkan Title `No results found` dan Description `Try adjusting your search or filter.`
19. Atur intercept respons data Tab Changelog menjadi lambat (ditahan)
20. Buka ulang Detail Hana Kusuma {runId}-362 > Tab Changelog
21. Verifikasi saat memuat, skeleton 5 baris sesuai kolom aktual tampil
22. Ganti intercept respons data Tab Changelog menjadi 500
23. Buka ulang Detail Hana Kusuma {runId}-362 > Tab Changelog
24. Verifikasi fetch gagal menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
25. Verifikasi tampilan fetch gagal bukan empty state
26. Lepas intercept respons data Tab Changelog
27. Klik `[Try Again]`
28. Verifikasi `[Try Again]` memuat ulang data: pesan `Unable to load this data.` tidak lagi tampil

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; tiap TC memakai surface-nya sendiri sehingga kegagalan satu blok tidak mengubah state blok lain.
- Mode FE+BE: kegagalan dipaksa dengan `Spectra.intercept()` parsial di atas backend nyata (bagian 6 konvensi), bukan seluruh API di-mock. Kelas b (resilience) dikumpulkan per jenis aksi baca atau unduh; kelas lain tidak ada di spec ini.
- Langkah 1 menggabungkan Search baris target dengan klik nama dan pembukaan Tab Non-Login User (R-16).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): membuka ulang surface sebelum tiap kondisi lambat dan 500 (supaya permintaan data dikirim ulang dan Search tidak terbawa), serta mengatur, mengganti, dan melepas intercept (pemicu, bukan objek asersi).
- Pembagian TC lintas spec:
  - TC-FA-SU-574: format dan nama berkas TC-FA-SU-569 di spec 191, transformasi data TC-FA-SU-571 di spec 371, Download gagal TC-FA-SU-572 di spec 367.
  - TC-FA-SU-606: format dan nama berkas TC-FA-SU-601 di spec 201, transformasi data TC-FA-SU-603 di spec 372, Download gagal TC-FA-SU-604 di spec 367.
- Pemetaan butir Expected: butir a, b, c, dan d TC masing-masing menjadi satu `Verifikasi` (butir d dipecah per klausa: tampilan fetch gagal beserta `[Try Again]`, bukan empty state, dan `[Try Again]` memuat ulang data).
- Temuan untuk QA (S-15):
  - TC-FA-SU-574: precondition b menyebut halaman target Budi Santoso, sedangkan Langkah Uji 1 membuka pengguna tanpa data (Hana Kusuma); spec mengikuti Langkah Uji 1 dengan pengguna milik spec.
  - TC-FA-SU-606: precondition b menyebut halaman target Budi Santoso, sedangkan Langkah Uji 1 membuka pengguna tanpa data (Hana Kusuma); spec mengikuti Langkah Uji 1.
  - TC-FA-SU-574: Pre-setup #26 hanya mencantumkan Non-Login User milik Budi Santoso; spec memakai pengguna milik spec `Hana Kusuma {runId}-362` yang dibuat tanpa Non-Login User (S-06).
  - TC-FA-SU-606: Pre-setup #27 hanya mencantumkan riwayat Budi Santoso; TC tidak menyatakan bahwa Tab Changelog pengguna tanpa data kosong; spec memakai `Hana Kusuma {runId}-362` milik spec yang dibuat Pending Activation tanpa riwayat, sehingga tidak bergantung pada urutan run spec lain.
  - Keyword Search tanpa hasil, cara melambatkan respons, dan jeda tahan tidak diberi nilai oleh TC; spec memakai `zzzz` dan intercept ditahan sampai kondisi `Verifikasi` selesai. Butir b menyebut "Search atau Filter" tanpa hasil, sedangkan Langkah Uji hanya memakai keyword (Search); Filter tanpa hasil tidak dijalankan.
  - Hasil akhir `[Try Again]` (butir d, "memuat ulang data") tidak dinyatakan TC; spec mengasersi pesan `Unable to load this data.` tidak lagi tampil setelah intercept dilepas. Langkah Uji "Ulangi" ditafsirkan sebagai membuka ulang surface (Search tidak terbawa) karena TC tidak menyatakan apakah keyword Search bertahan setelah muat ulang.
