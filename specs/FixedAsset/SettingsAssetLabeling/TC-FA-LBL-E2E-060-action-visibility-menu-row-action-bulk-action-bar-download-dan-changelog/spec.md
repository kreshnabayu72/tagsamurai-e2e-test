---
id: TC-FA-LBL-E2E-060-action-visibility-menu-row-action-bulk-action-bar-download-dan-changelog
title: "Action Visibility: menu row action, Bulk Action Bar, Download, dan Changelog"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:konsolidasi-action-visibility-matrix/edit--menu-row-action
  - FALB:konsolidasi-action-visibility-matrix/edit--menu-row-action~2
  - FALB:konsolidasi-action-visibility-matrix/delete-single--menu-row-action
  - FALB:konsolidasi-action-visibility-matrix/delete-single--menu-row-action~2
  - FALB:konsolidasi-action-visibility-matrix/delete-bulk
  - FALB:konsolidasi-action-visibility-matrix/download
  - FALB:konsolidasi-action-visibility-matrix/changelog
  - FALB:global-table-rules/bulk-actions
coverage:
  web: automated
---

# Action Visibility: menu row action, Bulk Action Bar, Download, dan Changelog

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite. Ganti akun eksplisit ke Read Only (`DU-02`), env `FA_RO_EMAIL` dan `FA_RO_PASSWORD` (langkah 43). Hook `after` mengembalikan sesi ke `DU-01`.
- Data uji `DU-71` (Label bersih, label dipakai aset, dan Default Label untuk uji visibilitas aksi), bersuffix `{runId}-060`, dibuat lewat sesi API di hook `before` dan dihapus di hook `after` (aset, Asset Name, lalu label): label `Act-{runId}-060-01` bersih (Total Asset 0 dan bukan Default Label), label `-02` dipakai aset (Total Asset lebih dari 0), dan label `-03` dijadikan Default Label oleh Asset Name seed. Satu Search `DU-71` menampilkan ketiganya.
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label, aset, dan Asset Name, disediakan tim FE/BE.
- State global: tidak ada yang diubah; semua dialog konfirmasi dibatalkan atau ditutup dengan `[OK]`, tidak ada label yang dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `DU-71`, tekan Enter
2. Verifikasi tiga baris label milik `DU-71` tampil pada Labels List

### FALB:konsolidasi-action-visibility-matrix/edit--menu-row-action: Edit pada menu row action bagi pemegang Permission Update

3. Klik `[⋯]` pada baris label bersih `-01` milik `DU-71`
4. Verifikasi aksi `Edit` tampil dan Enabled pada menu `[⋯]`
5. Klik `Edit`
6. Verifikasi Modal Edit Label tampil dengan judul `Edit Label`
7. Klik `[✕]` pada header Modal Edit Label

### FALB:konsolidasi-action-visibility-matrix/delete-single--menu-row-action: Delete single pada label bersih membuka D-01

8. Klik `[⋯]` pada baris label bersih `-01` milik `DU-71`
9. Verifikasi aksi `Delete` tampil dan Enabled dengan severity Danger pada menu `[⋯]`
10. Klik `Delete`
11. Verifikasi dialog `Delete Label` tampil dengan nama label `-01`, teks `Are you sure you want to delete it? This action cannot be undone.`, serta tombol `[Cancel]` dan `[Delete]`
12. Klik `[Cancel]`

### FALB:konsolidasi-action-visibility-matrix/delete-single--menu-row-action~2: Delete single pada label dipakai atau Default Label membuka D-02 tanpa mutasi

13. Klik `[⋯]` pada baris label dipakai aset `-02` milik `DU-71`
14. Verifikasi aksi `Delete` tampil dan Enabled dengan severity Danger pada menu `[⋯]`
15. Klik `Delete`
16. Verifikasi dialog `Cannot Delete Label` tampil dengan nama label `-02`, baris hitungan aset sesuai nilai Total Asset baris itu, teks `Remove it from those assets and Default Label lists before deleting it.`, dan tombol `[OK]`
17. Klik `[OK]`
18. Klik `[⋯]` pada baris label Default Label `-03` milik `DU-71`, lalu klik `Delete`
19. Verifikasi dialog `Cannot Delete Label` tampil dengan nama label `-03`, baris hitungan Default Label sesuai jumlah Asset Name yang memakai label itu, teks `Remove it from those assets and Default Label lists before deleting it.`, dan tombol `[OK]`
20. Klik `[OK]`
21. Verifikasi ketiga baris label milik `DU-71` masih tampil pada Labels List

### FALB:konsolidasi-action-visibility-matrix/delete-bulk: Delete bulk pada Bulk Action Bar

22. Centang checkbox baris label bersih `-01` milik `DU-71`
23. Verifikasi Bulk Action Bar tampil dengan aksi `Delete` Enabled dengan severity Danger
24. Klik `Delete` pada Bulk Action Bar
25. Verifikasi dialog `Delete Label` untuk label `-01` tampil (seleksi satu baris memakai dialog tunggal)
26. Klik `[Cancel]`
27. Centang checkbox baris label dipakai aset `-02` milik `DU-71`
28. Klik `Delete` pada Bulk Action Bar
29. Verifikasi dialog `Delete Labels` tampil dengan daftar `The following will be deleted:` berisi `-01`, daftar `The following are in use and will be skipped:` berisi `-02`, teks `Are you sure you want to continue? This action cannot be undone.`, serta tombol `[Cancel]` dan `[Continue]`
30. Klik `[Cancel]`
31. Hilangkan centang baris `-01` dan centang baris Default Label `-03` milik `DU-71`
32. Klik `Delete` pada Bulk Action Bar
33. Verifikasi dialog `Cannot Delete Labels` tampil dengan daftar `-02` dan `-03` serta teks `These labels are in use and cannot be deleted.` dan tombol `[OK]`
34. Klik `[OK]`
35. Hilangkan centang baris `-02` dan `-03` milik `DU-71`

### FALB:konsolidasi-action-visibility-matrix/download: Download pada toolbar tabel selalu Enabled

36. Klik Download pada toolbar tabel
37. Verifikasi opsi `Download as CSV` dan `Download as XLSX` tampil dan Enabled
38. Klik Download pada toolbar tabel untuk menutup menu Download

### FALB:konsolidasi-action-visibility-matrix/changelog: Changelog pada toolbar tabel selalu Enabled

39. Klik ikon Changelog pada toolbar tabel
40. Verifikasi Modal Changelog: Labels tampil dengan judul `Changelog: Labels`
41. Klik `[✕]` pada header Modal Changelog
42. Verifikasi ikon Changelog tampil pada toolbar tabel

### FALB:konsolidasi-action-visibility-matrix/edit--menu-row-action~2: Edit Hidden bagi Read Only

43. Ganti akun ke Read Only: logout, login dengan akun `DU-02`, lalu buka Fixed Asset > Settings > Asset Master > tab Labels
44. Ketik Search `DU-71`, tekan Enter
45. Verifikasi tiga baris label milik `DU-71` tampil pada Labels List
46. Klik `[⋯]` pada baris label bersih `-01` milik `DU-71`
47. Verifikasi aksi `Detail` tampil pada menu `[⋯]`
48. Verifikasi aksi `Edit` tidak tampil pada menu `[⋯]`

### FALB:global-table-rules/bulk-actions: Seleksi massal checkbox hanya bagi pemegang Permission Delete

49. Verifikasi checkbox baris dan checkbox Select All tidak tampil pada Labels List
50. Verifikasi Bulk Action Bar tidak tampil

## Notes

- Langkah penghubung (S-03): Search `DU-71` (langkah 1 dan 44) menemukan ketiga baris target di Labels List yang dapat memuat lebih dari satu halaman (R-16); klik `[⋯]` membuka menu baris; langkah 7, 12, 17, 20, 26, 30, 34, 35, 38, dan 41 menutup menu, dialog, atau modal serta membersihkan seleksi sebelum blok berikutnya (S-09); langkah 43 adalah langkah ganti akun eksplisit tanpa `Verifikasi` karena akun pertama login di hook `before`.
- Anchor absence: langkah 45 (baris label `DU-71` tampil) dan langkah 47 (`Detail` tampil; PRD §2.1 dan §4.7 View Tagged Assets) mendahului asersi `Edit`, checkbox, dan Bulk Action Bar tidak tampil (langkah 48 sampai 50); sisi pemegang Permission Delete bagi `FALB:global-table-rules/bulk-actions` (checkbox dan Bulk Action Bar tampil bagi `DU-01`) diasersi pada langkah 22 sampai 23.
- Pembagian klausa lintas spec: Download dan Changelog "Selalu berlaku" bagi Read Only diasersi sebagai anchor tampil di spec 059 (langkah 3, 13, 21, 29); spec ini mengasersi Enabled dan efek klik untuk `DU-01`. Isi dan nama berkas Download dimiliki spec 054, 035, 050, dan 067.
- Keterbatasan data: `DU-71` hanya menyediakan satu label bersih, sehingga klausa "semua bersih `D-03`" pada `FALB:konsolidasi-action-visibility-matrix/delete-bulk` tidak diasersi di spec ini; klausa dialog campuran `D-04` dan semua dipakai `D-05` serta seleksi satu baris (`D-01`) diasersi di langkah 25 sampai 34. Tidak ada eksekusi hapus, sehingga tidak ada mutasi data.
- Alasan spec melewati 35 langkah: seluruh blok satu kelas harness (Role Matrix tampilan aksi) dengan data `DU-71` yang sama dan dibaca saja; tiap blok berdiri sendiri karena semua dialog dibatalkan atau ditutup dan seleksi dibersihkan di akhir blok (langkah 12, 17, 20, 26, 30, 34, dan 35), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
