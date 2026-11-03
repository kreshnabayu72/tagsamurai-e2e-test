---
id: TC-FA-SU-E2E-375-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-7
title: "Resilience Baca: Empty State, Loading, dan Error Load Surface Tabel (Bagian 7)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-365
  - TC-FA-SU-734
coverage:
  web: automated
---

# Resilience Baca: Empty State, Loading, dan Error Load Surface Tabel (Bagian 7)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Kelas harness: b (fault injection pada pembacaan data, resilience baca). Data Pre-setup: Client `FaUserMain` (#20), Changelog (#27). Surface User List memakai seluruh populasi 25 pengguna Client tanpa pengguna khusus.
- Kemampuan teknis: `Spectra.intercept()` atas respons HTTP data surface di atas backend nyata (ditahan lambat, lalu respons 500); intercept dilepas oleh langkah `Lepas intercept` dan hook `after` melepasnya lagi sebagai cadangan, sehingga spec lain tidak terpengaruh. Keyword Search tanpa hasil `zzzz` dipilih spec. Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pelepasan intercept.

## Test Steps

### TC-FA-SU-365: Empty state, hasil pencarian kosong, loading, dan error load User List

1. Verifikasi tabel User List tidak kosong: sedikitnya satu baris tampil (Default User selalu memiliki akses FAMS)
2. Ketik Search `zzzz`, tekan Enter
3. Verifikasi Search tanpa hasil menampilkan Title `No results found` dan Description `Try adjusting your search or filter.`
4. Atur intercept respons data User List menjadi lambat (ditahan)
5. Buka ulang halaman Fixed Asset > Settings > User
6. Verifikasi saat memuat, skeleton 5 baris sesuai kolom aktual tampil
7. Ganti intercept respons data User List menjadi 500
8. Buka ulang halaman Fixed Asset > Settings > User
9. Verifikasi fetch gagal menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
10. Verifikasi tampilan fetch gagal bukan empty state
11. Lepas intercept respons data User List
12. Klik `[Try Again]`
13. Verifikasi `[Try Again]` memuat ulang data: pesan `Unable to load this data.` tidak lagi tampil

### TC-FA-SU-734: Empty state, hasil pencarian kosong, loading, dan error load Modal Combined Changelog: User

14. Klik icon Changelog di halaman User List
15. Verifikasi data kosong sungguhan menampilkan ilustrasi 100x100 dengan Title `No changelog yet` dan Description `Activities and changes will appear here.`
16. Ketik Search `zzzz`, tekan Enter
17. Verifikasi Search tanpa hasil menampilkan Title `No results found` dan Description `Try adjusting your search or filter.`
18. Tutup modal Changelog
19. Atur intercept respons data Modal Combined Changelog: User menjadi lambat (ditahan)
20. Klik ulang icon Changelog di halaman User List
21. Verifikasi saat memuat, skeleton 5 baris sesuai kolom aktual tampil
22. Tutup modal Changelog
23. Ganti intercept respons data Modal Combined Changelog: User menjadi 500
24. Klik ulang icon Changelog di halaman User List
25. Verifikasi fetch gagal menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
26. Verifikasi tampilan fetch gagal bukan empty state
27. Lepas intercept respons data Modal Combined Changelog: User
28. Klik `[Try Again]`
29. Verifikasi `[Try Again]` memuat ulang data: pesan `Unable to load this data.` tidak lagi tampil
30. Tutup modal Changelog

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; tiap TC memakai surface-nya sendiri sehingga kegagalan satu blok tidak mengubah state blok lain.
- Mode FE+BE: kegagalan dipaksa dengan `Spectra.intercept()` parsial di atas backend nyata (bagian 6 konvensi), bukan seluruh API di-mock. Kelas b (resilience) dikumpulkan per jenis aksi baca atau unduh; kelas lain tidak ada di spec ini.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): membuka ulang surface sebelum tiap kondisi lambat dan 500 (supaya permintaan data dikirim ulang dan Search tidak terbawa), serta mengatur, mengganti, dan melepas intercept (pemicu, bukan objek asersi), serta menutup modal Changelog.
- Pembagian TC lintas spec:
  - TC-FA-SU-365: format dan nama berkas TC-FA-SU-360 di spec 127, transformasi data TC-FA-SU-362 di spec 370, Download gagal TC-FA-SU-363 di spec 366.
  - TC-FA-SU-734: format dan nama berkas TC-FA-SU-729 di spec 240, transformasi data TC-FA-SU-731 di spec 373, Download gagal TC-FA-SU-732 di spec 368.
- Pemetaan butir Expected: butir a, b, c, dan d TC masing-masing menjadi satu `Verifikasi` (butir d dipecah per klausa: tampilan fetch gagal beserta `[Try Again]`, bukan empty state, dan `[Try Again]` memuat ulang data).
- Temuan untuk QA (S-15):
  - TC-FA-SU-365: butir a ("tabel tidak pernah genuinely empty ... kondisi kosong hanya muncul dari Search atau Filter tanpa hasil") berupa pernyataan keadaan; spec membuktikannya dengan `Verifikasi` sedikitnya satu baris tampil sebelum Search dan dengan `Verifikasi` empty state `No results found` sesudah Search tanpa hasil.
  - TC-FA-SU-734: langkah uji membuka Modal Combined Changelog "pada pengguna tanpa data (Hana Kusuma)", padahal modal ini memuat riwayat seluruh pengguna Client dan Pre-setup #27 menyediakan 6 baris Combined Changelog; kondisi data kosong sungguhan (butir a) tidak dapat terbentuk dari Pre-setup. Spec mengikuti TC; butir a perlu keputusan QA (Client tanpa riwayat atau respons kosong yang di-intercept).
  - Keyword Search tanpa hasil, cara melambatkan respons, dan jeda tahan tidak diberi nilai oleh TC; spec memakai `zzzz` dan intercept ditahan sampai kondisi `Verifikasi` selesai. Butir b menyebut "Search atau Filter" tanpa hasil, sedangkan Langkah Uji hanya memakai keyword (Search); Filter tanpa hasil tidak dijalankan.
  - Hasil akhir `[Try Again]` (butir d, "memuat ulang data") tidak dinyatakan TC; spec mengasersi pesan `Unable to load this data.` tidak lagi tampil setelah intercept dilepas. Langkah Uji "Ulangi" ditafsirkan sebagai membuka ulang surface (Search tidak terbawa) karena TC tidak menyatakan apakah keyword Search bertahan setelah muat ulang.
