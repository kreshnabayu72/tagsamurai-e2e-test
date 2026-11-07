---
id: TC-FA-SU-E2E-363-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-4
title: "Resilience Baca: Empty State, Loading, dan Error Load Surface Tabel (Bagian 4)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-670
  - TC-FA-SU-702
coverage:
  web: automated
---

# Resilience Baca: Empty State, Loading, dan Error Load Surface Tabel (Bagian 4)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Kelas harness: b (fault injection pada pembacaan data, resilience baca). Data Pre-setup: Client `FaUserMain` (#20), Changelog (#27). Pengguna tanpa data pada surface Detail: Hana Kusuma (Pending Activation) dari Client `FaUserMain`.
- Kemampuan teknis: `Spectra.intercept()` atas respons HTTP data surface di atas backend nyata (ditahan lambat, lalu respons 500); intercept dilepas oleh langkah `Lepas intercept` dan hook `after` melepasnya lagi sebagai cadangan, sehingga spec lain tidak terpengaruh. Keyword Search tanpa hasil `zzzz` dipilih spec. Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pelepasan intercept.

## Test Steps

### TC-FA-SU-670: Empty state, hasil pencarian kosong, loading, dan error load Modal Changelog User > Group Role

1. Ketik Search `Hana Kusuma`, tekan Enter, lalu buka Detail Hana Kusuma > Tab Role > Sub-tab Group Role > icon Changelog
2. Verifikasi data kosong sungguhan menampilkan ilustrasi 100x100 dengan Title `No changelog yet` dan Description `Activities and changes will appear here.`
3. Ketik Search `zzzz`, tekan Enter
4. Verifikasi Search tanpa hasil menampilkan Title `No results found` dan Description `Try adjusting your search or filter.`
5. Tutup modal Changelog
6. Atur intercept respons data Modal Changelog User > Group Role menjadi lambat (ditahan)
7. Buka ulang Detail Hana Kusuma > Tab Role > Sub-tab Group Role > icon Changelog
8. Verifikasi saat memuat, skeleton 5 baris sesuai kolom aktual tampil
9. Tutup modal Changelog
10. Ganti intercept respons data Modal Changelog User > Group Role menjadi 500
11. Buka ulang Detail Hana Kusuma > Tab Role > Sub-tab Group Role > icon Changelog
12. Verifikasi fetch gagal menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
13. Verifikasi tampilan fetch gagal bukan empty state
14. Lepas intercept respons data Modal Changelog User > Group Role
15. Klik `[Try Again]`
16. Verifikasi `[Try Again]` memuat ulang data: pesan `Unable to load this data.` tidak lagi tampil
17. Tutup modal Changelog

### TC-FA-SU-702: Empty state, hasil pencarian kosong, loading, dan error load Modal Changelog User > Transaction Role

18. Buka Detail Hana Kusuma > Tab Role > Sub-tab Transaction Role > icon Changelog
19. Verifikasi data kosong sungguhan menampilkan ilustrasi 100x100 dengan Title `No changelog yet` dan Description `Activities and changes will appear here.`
20. Ketik Search `zzzz`, tekan Enter
21. Verifikasi Search tanpa hasil menampilkan Title `No results found` dan Description `Try adjusting your search or filter.`
22. Tutup modal Changelog
23. Atur intercept respons data Modal Changelog User > Transaction Role menjadi lambat (ditahan)
24. Buka ulang Detail Hana Kusuma > Tab Role > Sub-tab Transaction Role > icon Changelog
25. Verifikasi saat memuat, skeleton 5 baris sesuai kolom aktual tampil
26. Tutup modal Changelog
27. Ganti intercept respons data Modal Changelog User > Transaction Role menjadi 500
28. Buka ulang Detail Hana Kusuma > Tab Role > Sub-tab Transaction Role > icon Changelog
29. Verifikasi fetch gagal menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
30. Verifikasi tampilan fetch gagal bukan empty state
31. Lepas intercept respons data Modal Changelog User > Transaction Role
32. Klik `[Try Again]`
33. Verifikasi `[Try Again]` memuat ulang data: pesan `Unable to load this data.` tidak lagi tampil
34. Tutup modal Changelog

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; tiap TC memakai surface-nya sendiri sehingga kegagalan satu blok tidak mengubah state blok lain.
- Mode FE+BE: kegagalan dipaksa dengan `Spectra.intercept()` parsial di atas backend nyata (bagian 6 konvensi), bukan seluruh API di-mock. Kelas b (resilience) dikumpulkan per jenis aksi baca atau unduh; kelas lain tidak ada di spec ini.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): membuka ulang surface sebelum tiap kondisi lambat dan 500 (supaya permintaan data dikirim ulang dan Search tidak terbawa), serta mengatur, mengganti, dan melepas intercept (pemicu, bukan objek asersi), serta menutup modal Changelog.
- Langkah penghubung tambahan (S-03): Search nama `Hana Kusuma` di User List supaya baris target tidak bergantung posisi halaman (langkah 1, 8b butir 13, R-16).
- Pembagian TC lintas spec:
  - TC-FA-SU-670: format dan nama berkas TC-FA-SU-665 di spec 221, transformasi data TC-FA-SU-667 di spec 372, Download gagal TC-FA-SU-668 di spec 367.
  - TC-FA-SU-702: format dan nama berkas TC-FA-SU-697 di spec 229, transformasi data TC-FA-SU-699 di spec 372, Download gagal TC-FA-SU-700 di spec 367.
- Pemetaan butir Expected: butir a, b, c, dan d TC masing-masing menjadi satu `Verifikasi` (butir d dipecah per klausa: tampilan fetch gagal beserta `[Try Again]`, bukan empty state, dan `[Try Again]` memuat ulang data).
- Temuan untuk QA (S-15):
  - TC-FA-SU-670: precondition b menyebut halaman target Budi Santoso, sedangkan Langkah Uji 1 membuka pengguna tanpa data (Hana Kusuma); spec mengikuti Langkah Uji 1.
  - TC-FA-SU-702: precondition b menyebut halaman target Budi Santoso, sedangkan Langkah Uji 1 membuka pengguna tanpa data (Hana Kusuma); spec mengikuti Langkah Uji 1.
  - TC-FA-SU-670: Pre-setup #27 hanya mencantumkan riwayat modal Role milik Budi Santoso; Hana Kusuma kosong hanya tersirat.
  - TC-FA-SU-702: Pre-setup #27 hanya mencantumkan riwayat modal Role milik Budi Santoso; Hana Kusuma kosong hanya tersirat.
  - Keyword Search tanpa hasil, cara melambatkan respons, dan jeda tahan tidak diberi nilai oleh TC; spec memakai `zzzz` dan intercept ditahan sampai kondisi `Verifikasi` selesai. Butir b menyebut "Search atau Filter" tanpa hasil, sedangkan Langkah Uji hanya memakai keyword (Search); Filter tanpa hasil tidak dijalankan.
  - Hasil akhir `[Try Again]` (butir d, "memuat ulang data") tidak dinyatakan TC; spec mengasersi pesan `Unable to load this data.` tidak lagi tampil setelah intercept dilepas. Langkah Uji "Ulangi" ditafsirkan sebagai membuka ulang surface (Search tidak terbawa) karena TC tidak menyatakan apakah keyword Search bertahan setelah muat ulang.
