---
id: TC-FA-TDC-E2E-140-konflik-capability-diubah-saat-user-lain-login
title: "Konflik Capability: Update dan Delete pada Manage accounting Diberikan atau Dicabut Saat User Lain Sedang Login"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-771
  - TC-FA-TDC-772
  - TC-FA-TDC-773
sourceRules: ["§4.8#r14", "§4.8#r13", "§4.8#r15", "ST-29", "FATDC-LOGIC-08i", "§4.8#r12", "FATDC-LOGIC-14b", "§4.8#r17"]
smoke: []
dependsOn: []
trace:
  "§4.8#r14": 9
  "§4.8#r13": [11, 30]
  "§4.8#r15": [12, 29]
  "ST-29": 20
  "FATDC-LOGIC-08i": 21
  "§4.8#r12": 22
  "FATDC-LOGIC-14b": 33
  "§4.8#r17": 34
coverage:
  web: automated
---

# Konflik Capability: Update dan Delete pada Manage accounting Diberikan atau Dicabut Saat User Lain Sedang Login

## Prerequisites

- Mode: FE+BE.
- Akun pengubah (sesi A): Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Akun pengamat (sesi Siti): Siti Rahmawati, pemegang capability Manage accounting. Email tidak tertulis di TC dan disediakan tim FE; password lewat `Spectra.env.FA_SITI_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Sesi Siti adalah konteks browser kedua yang hasilnya diasersi; login eksplisit di langkah 1.
- Login sesi A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk perubahan capability role dan class), flag Guided Tooltip disetel true oleh hook suite (untuk kedua akun), hook `beforeEach` mengonfirmasi `beforeunload`.
- State yang diubah: capability Manage accounting milik Siti Rahmawati (dimulai dengan Read saja; diberi Update pada TC-FA-TDC-771, dicabut pada TC-FA-TDC-772, diberi Delete pada TC-FA-TDC-773); dipulihkan ke Read saja dengan langkah eksplisit (langkah 37) dan di hook `after` sebagai cadangan.
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus atau dipulihkan di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nb4` | `NB-4` | Class Name `Bukan bangunan – Kelompok 4`, Active, Used By 0 |
| `sitiRead` | Siti Rahmawati | memegang Manage accounting dengan Read saja sebelum langkah 1 |

- Ketiga blok berjalan berurutan menurut rantai state capability: Read saja (TC-FA-TDC-771) lalu Read dan Update (TC-FA-TDC-772) lalu Read saja (TC-FA-TDC-773).
- Suite berjalan serial (`parallel: false`) karena capability role adalah state global.

## Test Steps

### TC-FA-TDC-771: Update yang diberikan pada Manage accounting mengaktifkan toggle Active dan Edit tanpa login ulang

1. Buka konteks browser kedua (sesi Siti), login sebagai Siti Rahmawati dengan `Spectra.env.FA_SITI_PASSWORD`, lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
2. Sesi A: buka Settings > Role & Permission
3. Sesi A: buka Detail Role "Manage accounting"
4. Sesi A: centang Update milik Siti Rahmawati
5. Sesi A: klik `[Save]`
6. Sesi A: Tunggu aksi selesai
7. Sesi Siti: muat ulang tab Tax Depreciation Class
8. Sesi Siti: ketik Search `NB-4`, tekan Enter
9. Verifikasi sesi Siti: toggle `Active` baris `NB-4` Enabled
10. Sesi Siti: klik tombol ⋯ baris `NB-4`
11. Verifikasi sesi Siti: menu baris memuat `Edit`
12. Verifikasi sesi Siti: menu baris tidak memuat `Delete`
13. Sesi Siti: tekan Esc untuk menutup menu baris

### TC-FA-TDC-772: Update yang dicabut dari Manage accounting menonaktifkan toggle Active

14. Sesi A: hapus centang Update milik Siti Rahmawati pada Detail Role "Manage accounting"
15. Sesi A: klik `[Save]`
16. Sesi A: Tunggu aksi selesai
17. Sesi Siti: muat ulang tab Tax Depreciation Class
18. Sesi Siti: ganti isi kotak search dengan `NB-4`, tekan Enter
19. Sesi Siti: arahkan kursor ke toggle `Active` baris `NB-4`
20. Verifikasi sesi Siti: toggle `Active` baris `NB-4` tetap tampil namun Disabled
21. Verifikasi sesi Siti: tooltip toggle berisi `You don't have permission to edit.`
22. Verifikasi sesi Siti: tombol ⋯ per baris tidak tampil

### TC-FA-TDC-773: Delete yang diberikan pada Manage accounting menampilkan row action Delete dan Bulk Delete

23. Sesi A: centang Delete milik Siti Rahmawati pada Detail Role "Manage accounting"
24. Sesi A: klik `[Save]`
25. Sesi A: Tunggu aksi selesai
26. Sesi Siti: muat ulang tab Tax Depreciation Class
27. Sesi Siti: ganti isi kotak search dengan `NB-4`, tekan Enter
28. Sesi Siti: klik tombol ⋯ baris `NB-4`
29. Verifikasi sesi Siti: menu baris memuat `Delete`
30. Verifikasi sesi Siti: menu baris tidak memuat `Edit`
31. Sesi Siti: tekan Esc untuk menutup menu baris
32. Sesi Siti: centang checkbox baris `NB-4`
33. Verifikasi sesi Siti: Bulk Action Bar memuat `Delete`
34. Verifikasi sesi Siti: Bulk Action Bar tidak memuat `Activate` maupun `Deactivate`
35. Sesi Siti: klik `Unselect All` pada Bulk Action Bar
36. Sesi Siti: klik `(←)` pada kotak Search
37. Sesi A: pulihkan capability Manage accounting milik Siti Rahmawati ke Read saja lewat seeding API
38. Tutup konteks browser sesi Siti

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Rantai state: capability Siti berubah di sesi A dari Read saja ke Read dan Update (langkah 4), kembali ke Read saja (langkah 14), lalu Read dan Delete (langkah 23); ketiga TC dijalankan dalam urutan itu agar precondition tiap TC terpenuhi tanpa seeding ulang di antara blok (P-3, user berurutan; alur tergantung urutan itu dicatat di Temuan untuk QA).
- Spec ini 38 langkah, di atas ~35 langkah: tiga TC kelas c berantai lewat capability Siti (Read saja, Read dan Update, Read dan Delete) pada baris yang sama, sehingga memecahnya berarti menyeed ulang capability dan membuka ulang sesi kedua. Langkah penghubung dan pemulihan di antaranya adalah langkah 35 sampai 38 dan langkah Search, serta tiga langkah "Tunggu aksi selesai" (langkah 6, 16, dan 25) menunggu `[Save]` capability selesai (8b.8).
- Langkah penghubung (S-03): langkah 2 dan 3 (membuka modul Role & Permission dan Detail Role; langkah 14 dan 23 memakai Detail Role yang masih terbuka), langkah 8, 18, dan 27 (Search agar baris target ada di halaman teramati; R-16, 8b.13), langkah 13 dan 31 (menutup menu baris), langkah 35 dan 36 (membersihkan seleksi dan Search; S-09), langkah 37 dan 38 (memulihkan capability dan menutup konteks sesi Siti).
- Langkah 7, 17, dan 26: muat ulang tab sesuai langkah TC; Search, Filter, Sort, dan halaman dipertahankan sesudah F5 (8b.9), sehingga langkah 8 (Search pertama sesi Siti) menulis "ketik Search" dan langkah 18 dan 27 menulis "ganti isi kotak search".
- Langkah 6, 16, dan 25 ("Tunggu aksi selesai", tanpa Verifikasi) menunggu `[Save]` perubahan capability selesai sebelum sesi Siti memuat ulang (8b.8, S-03).
- Langkah 22 (absence ⋯ tidak tampil): toggle langkah 20 yang tampil pada baris yang sama menjadi anchor positif (8b.2). Langkah 12, 30, dan 34 (menu atau bar tidak memuat aksi tertentu): aksi lain yang tampil pada menu atau bar yang sama (langkah 11, 29, dan 33) menjadi anchor positif.
- Temuan untuk QA:
  - Email akun Total Control sesi A dan akun Siti Rahmawati tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code `NB-4` ditulis literal tanpa suffix `{runId}-<NNN>` (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini. TC-FA-TDC-771 sampai TC-FA-TDC-773 hanya membaca atau mengubah toggle baris `NB-4`; spec tidak menjalankan aksi tulis atas `NB-4`.
  - TC-FA-TDC-772 dan TC-FA-TDC-773 memiliki precondition capability yang berbeda dari akhir blok sebelumnya hanya karena rantai urutan (Read dan Update lalu Read saja); bila dijalankan terpisah, TC masing-masing perlu seeding capability sendiri.
  - TC-FA-TDC-771 langkah 3 menyebut "klik tombol ⋯ baris NB-4 dan toggle Active"; spec mengasersi toggle Enabled (langkah 9) tanpa mengklik toggle karena TC tidak memberi Expected perubahan status.
  - TC-FA-TDC-773 langkah 3 menyebut "centang checkbox baris NB-4" pada user yang baru mendapat Delete; spec memakai aksi yang sama (langkah 32).
  - Kolom Automation TC-FA-TDC-771, TC-FA-TDC-772, dan TC-FA-TDC-773 memuat `Automatable`; TC ini masuk spec kelas c karena sesi Siti adalah konteks kedua yang diasersi.
