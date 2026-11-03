---
id: TC-FA-FAAM-E2E-098-bulk-delete-dialog-homogen-campuran-blok-dan-cancel
title: "Bulk Delete: Dialog Homogen, Campuran, Blok Semua In-Use, Seleksi Satu Baris, dan Cancel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-283
  - TC-FA-FAAM-285
  - TC-FA-FAAM-287
  - TC-FA-FAAM-288
  - TC-FA-FAAM-289
  - TC-FA-FAAM-672
coverage:
  web: automated
---

# Bulk Delete: Dialog Homogen, Campuran, Blok Semua In-Use, Seleksi Satu Baris, dan Cancel

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; seed API per TC mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Dinamis (suffix `{runId}-098`, seed di hook `before`, cleanup di hook `after`); tidak ada record yang dihapus aksi spec karena semua dialog dibatalkan atau ditolak guard in-use:
  - `Bulk Clean A {runId}-098` dan `Bulk Clean B {runId}-098`: salinan Pre-setup #13c (Total Asset 0).
  - `Bulk Used X {runId}-098` (Total Asset 3) dan `Bulk Used Y {runId}-098` (Total Asset 1): salinan Pre-setup #14o yang dirujuk aset aktif lewat seeding.
  - Search `{runId}-098` menampilkan keempat baris dalam satu halaman.
- Kemampuan teknis (disediakan tim BE/FE): membaca jumlah entri Changelog tanpa mengubahnya (baseline N0, dicatat sebelum aksi pertama).
- State global: tidak ada yang diubah spec ini.

## Test Steps

1. Catat jumlah entri Changelog sebagai N0 lewat kemampuan baca
2. Ketik Search `{runId}-098`, tekan Enter

### TC-FA-FAAM-283: Bulk Delete semua bersih menampilkan dialog homogen

3. Centang baris `Bulk Clean A {runId}-098`, `Bulk Clean B {runId}-098`
4. Klik `Bulk Action` lalu `Delete`
5. Verifikasi dialog `Delete Asset Names` dengan bullet `Bulk Clean A {runId}-098` dan `Bulk Clean B {runId}-098` (A→Z, scrollable) dan teks `Are you sure you want to delete them? This action cannot be undone.` serta tombol `[Cancel]` dan `[Delete]` tampil
6. Klik `[Cancel]`
7. Klik icon `×`

### TC-FA-FAAM-285: Bulk Delete campuran menampilkan dialog dua kelompok

8. Centang baris `Bulk Clean A {runId}-098`, `Bulk Clean B {runId}-098`, `Bulk Used X {runId}-098`
9. Klik `Bulk Action` lalu `Delete`
10. Verifikasi dialog `Delete Asset Names` berisi `The following will be deleted:` dengan bullet `Bulk Clean A {runId}-098`, `Bulk Clean B {runId}-098`, lalu `The following are used by assets and will be skipped:` dengan bullet `Bulk Used X {runId}-098`, lalu `Are you sure you want to continue? This action cannot be undone.` serta tombol `[Cancel]` dan `[Continue]` (merah) tampil

### TC-FA-FAAM-672: Cancel pada dialog Bulk Delete campuran tidak menghapus apa pun dan mempertahankan seleksi

11. Klik `[Cancel]` pada dialog `Delete Asset Names`
12. Verifikasi dialog tertutup
13. Verifikasi ketiga baris tetap tercentang
14. Verifikasi bar bulk tetap tampil
15. Verifikasi ketiga baris `Bulk Clean A {runId}-098`, `Bulk Clean B {runId}-098`, `Bulk Used X {runId}-098` masih tampil di List (tidak ada Asset Name terhapus)
16. Buka Changelog dan baca entri teratas
17. Verifikasi jumlah entri Changelog sama dengan N0 (tidak ada entri baru)
18. Tutup Changelog
19. Klik icon `×`

### TC-FA-FAAM-287: Bulk Delete semua in-use menampilkan dialog blok

20. Centang baris `Bulk Used X {runId}-098`, `Bulk Used Y {runId}-098`
21. Klik `Bulk Action` lalu `Delete`
22. Verifikasi dialog `Cannot Delete Asset Names` dengan bullet `Bulk Used X {runId}-098` dan `Bulk Used Y {runId}-098` dan teks `These asset names are used by assets and cannot be deleted.` serta tombol `[OK]` tampil
23. Klik `[OK]`
24. Verifikasi seleksi dan bar dipertahankan: bar bulk tampil dengan teks `2 asset names selected` dan kedua baris tetap tercentang
25. Verifikasi kedua baris `Bulk Used X {runId}-098` dan `Bulk Used Y {runId}-098` masih tampil di List (tanpa mutasi)
26. Baca jumlah entri Changelog lewat kemampuan baca
27. Verifikasi jumlah entri Changelog sama dengan N0 (tanpa log)
28. Klik icon `×`

### TC-FA-FAAM-288: Bulk dengan seleksi 1 baris memakai dialog single

29. Centang baris `Bulk Clean A {runId}-098`
30. Klik `Bulk Action` lalu `Delete`
31. Verifikasi dialog `Delete Asset Name` (bentuk tunggal) dengan teks `Are you sure you want to delete it? This action cannot be undone.` tampil
32. Klik `[Cancel]`
33. Klik icon `×`

### TC-FA-FAAM-289: Bulk dengan seleksi 1 baris in-use memakai dialog blok single

34. Centang baris `Bulk Used Y {runId}-098`
35. Klik `Bulk Action` lalu `Delete`
36. Verifikasi dialog `Cannot Delete Asset Name` dengan teks `This asset name is used by 1 asset and cannot be deleted.` tampil
37. Klik `[OK]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (R-16, langkah 2), menutup dialog dengan `[Cancel]` atau `[OK]` (langkah 6, 23, 32, 37), membatalkan seleksi antar TC (langkah 7, 19, 28, 33; S-09), membuka dan menutup Changelog (langkah 16, 18), serta baseline Changelog (langkah 1, 26; S-12).
- Langkah pembuka TC-FA-FAAM-672 (centang tiga baris, `Bulk Action` lalu `Delete`) identik dengan langkah 8 dan 9 milik TC-FA-FAAM-285 sehingga dialog yang sama dari langkah 10 dipakai; langkah 11 sampai 19 adalah sisa langkah TC-FA-FAAM-672.
- Urutan TC di dalam spec mengikuti kebutuhan state: dialog homogen, lalu campuran dan Cancel, lalu blok, lalu satu baris. Tidak ada aksi yang menghapus data sehingga tidak ada aksi penghapus di akhir.
- Dialog pada langkah 5, 10, 22, 31, dan 36 ditulis sebagai satu `Verifikasi` karena judul, isi, dan tombol disebut utuh pada Expected TC (S-01, dialog konfirmasi satu elemen).
- Alasan melewati sekitar 35 langkah (37 langkah): seluruh blok berbagi satu topik (dialog Bulk Delete), satu dataset (empat Asset Name dengan Search `{runId}-098`), tidak mengubah data, dan tidak ada blok yang kehilangan makna bila blok lain gagal; setiap Expected dialog tetap diasersi per klausa (S-01).
- Temuan untuk QA:
  - TC-FA-FAAM-287 Expected c ("tanpa mutasi, tanpa log") tidak punya langkah observasi di TC; spec mengamatinya lewat baris yang tetap tampil dan jumlah entri Changelog terhadap baseline N0.
  - TC-FA-FAAM-283 menyebut bullet "A→Z, scrollable" tanpa jumlah bullet yang memicu scroll; hanya urutan A→Z dengan dua bullet yang diasersi, scroll tidak diuji.
