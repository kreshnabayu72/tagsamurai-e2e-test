---
id: TC-FA-TDC-E2E-035-suspended-create-edit-cancel-version-dan-restore-ditolak-toast-baku
title: "Entitas Suspended: Create, Edit, Cancel Scheduled Version, dan Restore Default Classes Ditolak dengan Toast Baku"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-884
  - TC-FA-TDC-885
  - TC-FA-TDC-886
  - TC-FA-TDC-887
coverage:
  web: automated
---

# Entitas Suspended: Create, Edit, Cancel Scheduled Version, dan Restore Default Classes Ditolak dengan Toast Baku

## Prerequisites

- Mode: FE+BE.
- Aktor: Total Control pada company uji khusus automation berstatus Suspended. Akun, email, dan company tidak tertulis di TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan tim FE).
- Login di hook `before` spec ini sebagai Total Control pada company Suspended; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data uji (di-seed fixture BE di hook `before`, dipulihkan di hook `after`; kunci di `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada dan disediakan tim FE): 7 class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) pada satu halaman; tidak ada class dengan Class Code NB-9; NB-4 dengan Class Name `Bukan bangunan – Kelompok 4`; BLD-NP memiliki versi Scheduled mulai Jan 2027 yang tahun pajaknya belum dimulai. Nilai form Create (TC-FA-TDC-884): Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Code `NB-9`, Class Name `Kelompok 9 uji`, Asset Type `Non-building`, Useful Life `10`, Allowed Methods `Straight Line`. Nilai Class Name baru NB-4 (TC-FA-TDC-885): `Kelompok 4 diubah`.
- Status entitas Suspended dibentuk fixture BE dan tidak diubah spec ini; kemampuan itu disediakan tim FE/BE. Blok TC-FA-TDC-887 membutuhkan tabel tanpa class (semua status); spec mengosongkan tabel lewat fixture BE (langkah 37) dan hook `after` memulihkan dataset.
- Kemampuan baca jumlah entri log (Changelog, System Log, dan Activity Log) lewat fixture BE, disediakan tim FE/BE; baseline dibaca tepat sebelum aksi tiap TC (8b.10, S-12).
- Kemampuan browser: dialog `beforeunload` ditangani hook suite `beforeEach` (jaring pengaman form dirty).
- State global: tidak ada yang diubah bila penolakan berfungsi; hook `after` memulihkan dataset class dan sesi.
- Rujukan suite: `suite.md` (hook `before`, `beforeEach`, `after`; seed dan pemulihan lewat API).

## Test Steps

### TC-FA-TDC-884: Create ditolak

1. Catat baseline jumlah entri Changelog, System Log, dan Activity Log modul Tax Depreciation Class
2. Klik `+ Class`, isi Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Code `NB-9`, Class Name `Kelompok 9 uji`, Asset Type `Non-building`, Useful Life `10`, Allowed Methods `Straight Line`
3. Klik `[Submit]`
4. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." tampil
5. Verifikasi toast tampil di kanan bawah
6. Verifikasi halaman tetap berada di tab Tax Depreciation Class tanpa pengalihan
7. Tutup Drawer dengan `[×]`
8. Verifikasi dialog `Unsaved Changes` tampil
9. Klik `[Leave]`
10. Tutup toast error
11. Verifikasi tabel memuat sedikitnya satu baris class lain
12. Verifikasi class NB-9 tidak ada di tabel
13. Verifikasi jumlah entri Changelog, System Log, dan Activity Log modul sama dengan baseline

### TC-FA-TDC-885: Edit Class Name ditolak

14. Catat baseline jumlah entri Changelog, System Log, dan Activity Log untuk NB-4
15. Klik Class Code NB-4
16. Ubah Class Name menjadi `Kelompok 4 diubah`
17. Klik `[Save]`
18. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." tampil
19. Verifikasi toast tampil di kanan bawah
20. Verifikasi halaman tetap berada di tab Tax Depreciation Class tanpa pengalihan
21. Kembalikan Class Name ke `Bukan bangunan – Kelompok 4`
22. Tutup Drawer dengan `[×]`
23. Tutup toast error
24. Verifikasi Class Name NB-4 pada tabel tetap `Bukan bangunan – Kelompok 4`
25. Verifikasi jumlah entri Changelog, System Log, dan Activity Log untuk NB-4 sama dengan baseline

### TC-FA-TDC-886: Cancel Scheduled Version ditolak

26. Catat baseline jumlah entri Changelog, System Log, dan Activity Log untuk BLD-NP
27. Klik Class Code BLD-NP
28. Klik `[Cancel scheduled version]` pada Alert
29. Klik `[Cancel version]` pada dialog
30. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." tampil
31. Verifikasi toast tampil di kanan bawah
32. Verifikasi halaman tetap berada di tab Tax Depreciation Class tanpa pengalihan
33. Verifikasi Alert versi Scheduled BLD-NP masih tampil pada Drawer (versi tetap Scheduled)
34. Tutup Drawer dengan `[×]`
35. Tutup toast error
36. Verifikasi jumlah entri Changelog, System Log, dan Activity Log untuk BLD-NP sama dengan baseline

### TC-FA-TDC-887: Restore default classes ditolak

37. Kosongkan seluruh Tax Depreciation Class (semua status) lewat fixture BE hingga tersimpan
38. Buka Settings > Accounting > Tax Depreciation Class
39. Catat baseline jumlah entri Changelog, System Log, dan Activity Log modul Tax Depreciation Class
40. Klik `Restore default classes` di Empty State
41. Klik `[Restore]` pada dialog
42. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." tampil
43. Verifikasi toast tampil di kanan bawah
44. Verifikasi halaman tetap berada di tab Tax Depreciation Class tanpa pengalihan
45. Verifikasi tabel tetap kosong
46. Verifikasi jumlah entri Changelog, System Log, dan Activity Log modul sama dengan baseline

## Notes

- Langkah penghubung (S-03): langkah 10, 23, dan 35 menutup toast error sebelum toast identik diasersi lagi (R-12); langkah 21 mengembalikan field Drawer yang dirty ke nilai tersimpan sebelum Drawer ditutup (S-09); langkah 37 dan 38 membentuk tabel kosong untuk TC-FA-TDC-887 lewat fixture BE; langkah 7 sampai 9 menutup form Create yang dirty secara deterministik (S-08). Baris target ditemukan tanpa Search karena tabel memuat 7 baris pada satu halaman (dinyatakan di Prerequisites).
- S-05 dan prinsip 13g (pengecualian kelas h): asersi "tidak ada entri log baru" (langkah 13, 25, 36, dan 46) ditulis di spec ini sebagai `Verifikasi` selisih jumlah entri terhadap baseline per surface log (Changelog, System Log, Activity Log); toast error adalah anchor positif bahwa server sudah merespons (8b.2). `Verifikasi` log diletakkan setelah penutupan Drawer karena asersi tabel baru teramati sesudahnya (8b.5).
- Langkah 6, 20, 32, dan 44: TC tidak menyebut cara mengamati "tanpa pengalihan"; spec mengamati bahwa tab Tax Depreciation Class tetap tampil (pada langkah 32 Drawer terbuka di atas tab).
- Alasan spec melewati sekitar 35 langkah (46 langkah): seluruh blok satu kelas harness (h, write-lockdown Suspended) dengan asersi penolakan yang sama; tiap blok berdiri sendiri (dataset dan baseline sendiri) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok TC-FA-TDC-887 diletakkan terakhir karena membutuhkan tabel kosong.
- Temuan untuk QA:
  - TC tidak menyebut akun, email, dan company Total Control untuk status Suspended.
  - TC-FA-TDC-884 sampai 887 menyebut "entri log baru" tanpa menyebut surface log; spec memakai tiga surface log modul.
  - TC-FA-TDC-884 dan 885 tidak menyebut keadaan Drawer setelah penolakan; spec mengasumsikan Drawer tetap terbuka dengan input dipertahankan. TC-FA-TDC-886 tidak menyebut cara mengamati "versi tetap Scheduled"; spec memakai Alert versi Scheduled pada Drawer (sama dengan TC-FA-TDC-766).
  - TC memakai class seed literal (NB-4, BLD-NP) sebagai target aksi tulis yang ditolak; spec memakai dataset company khusus automation yang dipulihkan fixture karena modul ini tidak memiliki butir Lampiran A untuk nama literal.
