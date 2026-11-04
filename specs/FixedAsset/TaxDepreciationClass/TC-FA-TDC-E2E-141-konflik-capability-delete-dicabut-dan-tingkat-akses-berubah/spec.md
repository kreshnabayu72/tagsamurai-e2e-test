---
id: TC-FA-TDC-E2E-141-konflik-capability-delete-dicabut-dan-tingkat-akses-berubah
title: "Konflik Capability: Delete Dicabut dari Manage accounting dan Tingkat Akses User Berubah Saat User Sedang Login"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-774
  - TC-FA-TDC-775
  - TC-FA-TDC-776
coverage:
  web: automated
---

# Konflik Capability: Delete Dicabut dari Manage accounting dan Tingkat Akses User Berubah Saat User Sedang Login

## Prerequisites

- Mode: FE+BE.
- Akun pengubah (sesi A): Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Akun pengamat blok TC-FA-TDC-774 (sesi Siti): Siti Rahmawati, pemegang capability Manage accounting. Email tidak tertulis di TC dan disediakan tim FE; password lewat `Spectra.env.FA_SITI_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Sesi Siti adalah konteks browser kedua yang hasilnya diasersi; login eksplisit di langkah 1.
- Akun pengamat blok TC-FA-TDC-775 dan TC-FA-TDC-776 (sesi Budi): Budi Santoso, awalnya Total Control. Email tidak tertulis di TC dan disediakan tim FE; password lewat `Spectra.env.FA_BUDI_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Sesi Budi adalah konteks browser kedua yang hasilnya diasersi; login eksplisit di langkah 15.
- Login sesi A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk perubahan capability role, tingkat akses user, dan class), flag Guided Tooltip disetel true oleh hook suite (untuk semua akun aktor), hook `beforeEach` mengonfirmasi `beforeunload`.
- State yang diubah: capability Manage accounting milik Siti Rahmawati (Read dan Delete di awal, dicabut Delete pada TC-FA-TDC-774) dan tingkat akses Budi Santoso (Total Control, menjadi Read Only pada TC-FA-TDC-775, kembali ke Total Control pada TC-FA-TDC-776); capability Siti dipulihkan ke Read dan Delete dengan langkah eksplisit (langkah 14), tingkat akses Budi kembali ke Total Control lewat langkah 28 dan 29, dan hook `after` memulihkan keduanya sebagai cadangan (Siti Read dan Delete, Budi Total Control).
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus atau dipulihkan di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nb4` | `NB-4` | Class Name `Bukan bangunan – Kelompok 4`, Active, Used By 0 |
| `sitiReadDelete` | Siti Rahmawati | memegang Manage accounting dengan Read dan Delete sebelum langkah 1 |
| `budiTotalControl` | Budi Santoso | Total Control, sedang login di sesi lain sebelum langkah 15 |

- Blok TC-FA-TDC-775 dan TC-FA-TDC-776 berjalan berurutan menurut rantai state tingkat akses Budi (Total Control lalu Read Only lalu Total Control).
- Suite berjalan serial (`parallel: false`) karena capability role dan tingkat akses user adalah state global.

## Test Steps

### TC-FA-TDC-774: Delete yang dicabut dari Manage accounting menyembunyikan row action Delete dan checkbox

1. Buka konteks browser kedua (sesi Siti), login sebagai Siti Rahmawati dengan `Spectra.env.FA_SITI_PASSWORD`, lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
2. Sesi A: buka Settings > Role & Permission
3. Sesi A: buka Detail Role "Manage accounting"
4. Sesi A: hapus centang Delete milik Siti Rahmawati
5. Sesi A: klik `[Save]`
6. Sesi A: Tunggu aksi selesai
7. Sesi Siti: muat ulang tab Tax Depreciation Class
8. Sesi Siti: ketik Search `NB-4`, tekan Enter
9. Verifikasi sesi Siti: baris `NB-4` tampil di tabel
10. Verifikasi sesi Siti: tombol ⋯ per baris tidak tampil
11. Verifikasi sesi Siti: kolom checkbox dan Bulk Action Bar tidak tampil
12. Sesi Siti: klik `(←)` pada kotak Search
13. Tutup konteks browser sesi Siti
14. Sesi A: pulihkan capability Manage accounting milik Siti Rahmawati ke Read dan Delete lewat seeding API

### TC-FA-TDC-775: Tingkat akses user diubah menjadi Read Only membuat tab Tax Depreciation Class hanya dapat dibaca

15. Buka konteks browser kedua (sesi Budi), login sebagai Budi Santoso dengan `Spectra.env.FA_BUDI_PASSWORD`, lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
16. Sesi A: buka Global Settings > User
17. Sesi A: buka Detail user Budi Santoso
18. Sesi A: ubah tingkat akses menjadi Read Only
19. Sesi A: klik `[Save]`
20. Sesi A: Tunggu aksi selesai
21. Sesi Budi: muat ulang tab Tax Depreciation Class
22. Sesi Budi: ketik Search `NB-4`, tekan Enter
23. Verifikasi sesi Budi: Search, Filter, Download, dan Changelog tetap tampil
24. Verifikasi sesi Budi: tombol `+ Class` tidak tampil
25. Sesi Budi: arahkan kursor ke toggle `Active` baris `NB-4`
26. Verifikasi sesi Budi: toggle `Active` baris `NB-4` tampil Disabled dengan tooltip `You don't have permission to edit.`
27. Verifikasi sesi Budi: kolom checkbox, Bulk Action Bar, dan tombol ⋯ per baris tidak tampil

### TC-FA-TDC-776: Tingkat akses user diubah dari Read Only menjadi Total Control membuka seluruh aksi

28. Sesi A: ubah tingkat akses Budi Santoso dari Read Only menjadi Total Control pada Detail user
29. Sesi A: klik `[Save]`
30. Sesi A: Tunggu aksi selesai
31. Sesi Budi: muat ulang tab Tax Depreciation Class
32. Sesi Budi: ganti isi kotak search dengan `NB-4`, tekan Enter
33. Verifikasi sesi Budi: tombol `+ Class` tampil
34. Verifikasi sesi Budi: toggle `Active` baris `NB-4` Enabled
35. Sesi Budi: klik tombol ⋯ baris `NB-4`
36. Verifikasi sesi Budi: menu baris memuat `Edit` dan `Delete`
37. Sesi Budi: tekan Esc untuk menutup menu baris
38. Verifikasi sesi Budi: kolom checkbox tampil
39. Sesi Budi: centang checkbox baris `NB-4`
40. Verifikasi sesi Budi: Bulk Action Bar tampil
41. Sesi Budi: klik `Unselect All` pada Bulk Action Bar
42. Sesi Budi: klik `(←)` pada kotak Search
43. Tutup konteks browser sesi Budi

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Rantai state (P-3, user berurutan): tingkat akses Budi berubah di sesi A dari Total Control ke Read Only (langkah 18) lalu kembali ke Total Control (langkah 28); TC-FA-TDC-775 dan TC-FA-TDC-776 dijalankan dalam urutan itu agar precondition TC-FA-TDC-776 (Read Only) terpenuhi tanpa seeding ulang. Bila dijalankan terpisah, TC-FA-TDC-776 perlu seeding tingkat akses sendiri.
- Langkah penghubung (S-03): langkah 2 sampai 3 dan 16 sampai 17 (membuka modul Role & Permission dan Global Settings > User; langkah 28 memakai Detail user yang masih terbuka), langkah 8, 22, dan 32 (Search agar baris target ada di halaman teramati; R-16, 8b.13), langkah 12, 13, 37, 41, 42, dan 43 (membersihkan Search, seleksi, menu, dan menutup konteks kedua; S-09).
- Langkah 7, 21, dan 31: muat ulang tab sesuai langkah TC; Search, Filter, Sort, dan halaman dipertahankan sesudah F5 (8b.9), sehingga langkah 8 dan 22 (Search pertama tiap sesi pengamat) menulis "ketik Search" dan langkah 32 menulis "ganti isi kotak search".
- Langkah 6, 20, dan 30 ("Tunggu aksi selesai", tanpa Verifikasi) menunggu `[Save]` perubahan hak akses selesai sebelum sesi pengamat memuat ulang (8b.8, S-03). Langkah 14 memulihkan capability Siti secara eksplisit (S-09, S-03); hook `after` hanya cadangan.
- Langkah 10, 11, 24, 27 (absence): baris `NB-4` yang tampil (langkah 9) untuk langkah 10 dan 11, Search, Filter, Download, dan Changelog yang tampil (langkah 23) untuk langkah 24, dan toggle yang tampil Disabled (langkah 26) untuk langkah 27 menjadi anchor positif pada halaman yang sama (8b.2).
- Alasan spec melewati sekitar 35 langkah (43 langkah): ketiga blok adalah kelas c pada perubahan hak akses saat user lain login. Blok TC-FA-TDC-775 dan TC-FA-TDC-776 tersambung oleh rantai state tingkat akses Budi (langkah 18 ke langkah 28); blok TC-FA-TDC-774 memakai user dan capability lain (Siti) sehingga terpisah dari rantai itu. Langkah berulang per blok adalah membuka sesi, mengubah hak akses, memuat ulang, dan Search, serta `Verifikasi` per klausa (S-01).
- Temuan untuk QA:
  - Email akun Total Control sesi A, Siti Rahmawati, dan Budi Santoso tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code `NB-4` ditulis literal tanpa suffix `{runId}-<NNN>` (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini. Ketiga TC hanya membaca toggle dan menu `NB-4`; tidak ada aksi tulis atas `NB-4`.
  - TC-FA-TDC-775 Expected d ("Search, Filter, Download, dan Changelog tetap tampil") disatukan dalam satu butir; spec memakai satu `Verifikasi` karena daftar ikon disebut utuh (S-01).
  - TC-FA-TDC-774 dan TC-FA-TDC-776 tidak menyebut cara membuka Detail user atau Detail Role; spec memakai jalur Settings > Role & Permission dan Global Settings > User seperti precondition TC.
  - TC-FA-TDC-776 Expected d ("Kolom checkbox dan Bulk Action Bar tampil") membutuhkan seleksi agar Bulk Action Bar tampil; spec menambah langkah centang `NB-4` (langkah 39, S-03).
  - Kolom Automation TC-FA-TDC-774, TC-FA-TDC-775, dan TC-FA-TDC-776 memuat `Automatable`; TC ini masuk spec kelas c karena sesi Siti dan sesi Budi adalah konteks kedua yang diasersi.
