---
id: TC-FA-FAAM-E2E-094-delete-single-race-dan-record-sudah-terhapus-single-dan-bulk
title: "Delete: Aset Baru Antar Dialog dan Konfirmasi, serta Record Sudah Terhapus oleh Sesi Lain (Single dan Bulk)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAM-268
  - TC-FA-FAAM-269
  - TC-FA-FAAM-290
coverage:
  web: automated
---

# Delete: Aset Baru Antar Dialog dan Konfirmasi, serta Record Sudah Terhapus oleh Sesi Lain (Single dan Bulk)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; seed API per TC dan sesi API aktor mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Pelaku kedua ("sesi lain" pada TC): sesi API akun Total Control yang sama (login API, token tidak dihitung sebagai sesi web), disediakan tim BE/FE. Pelaku kedua hanya memicu perubahan state (mendaftarkan aset, menghapus Asset Name); tidak ada konteks UI kedua yang diasersi.
- Data Dinamis (suffix `{runId}-094`, seed di hook `before`, cleanup di hook `after` untuk yang tersisa):
  - `Warehouse Pallet 268 {runId}-094`: salinan Pre-setup #13 (Total Asset 0); satu aset didaftarkan pelaku kedua pada TC-FA-FAAM-268 sehingga Total Asset menjadi 1.
  - `Warehouse Pallet 269 {runId}-094`: salinan Pre-setup #13 (Total Asset 0); dihapus pelaku kedua pada TC-FA-FAAM-269.
  - `Bulk Clean A 290 {runId}-094` dan `Bulk Clean B 290 {runId}-094`: salinan Pre-setup #13c (Total Asset 0); `Bulk Clean B 290 {runId}-094` dihapus pelaku kedua dan `Bulk Clean A 290 {runId}-094` dihapus aksi UI pada TC-FA-FAAM-290.
- Kemampuan teknis (disediakan tim BE/FE): membaca jumlah entri Changelog tanpa mengubahnya (baseline N sesudah penghapusan oleh pelaku kedua, dicatat sebelum klik `[Delete]` UI).
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-268: Aset baru terdaftar antara dialog dan konfirmasi, re-check atomik menolak Delete

1. Ketik Search `Warehouse Pallet 268 {runId}-094`, tekan Enter
2. Klik `⋯` baris `Warehouse Pallet 268 {runId}-094` lalu `Delete`
3. Pelaku kedua lewat sesi API mendaftarkan satu aset ke `Warehouse Pallet 268 {runId}-094` hingga tersimpan
4. Klik `[Delete]` pada dialog
5. Verifikasi dialog blok `Cannot Delete Asset Name` dengan teks `This asset name is used by 1 asset and cannot be deleted.` tampil
6. Verifikasi tidak ada toast tambahan
7. Klik `[OK]`
8. Verifikasi baris `Warehouse Pallet 268 {runId}-094` tetap ada

### TC-FA-FAAM-269: Delete record yang sudah tidak ada dianggap sukses idempotent

9. Ganti isi kotak search dengan `Warehouse Pallet 269 {runId}-094`, tekan Enter
10. Klik `⋯` baris `Warehouse Pallet 269 {runId}-094` lalu `Delete`
11. Pelaku kedua lewat sesi API menghapus `Warehouse Pallet 269 {runId}-094` hingga terhapus
12. Catat jumlah entri Changelog sebagai N2 lewat kemampuan baca
13. Klik `[Delete]` pada dialog
14. Verifikasi toast sukses `Success, asset name has been deleted.` tampil
15. Verifikasi baris `Warehouse Pallet 269 {runId}-094` hilang
16. Buka Changelog
17. Verifikasi jumlah entri Changelog sama dengan N2 (tidak ada entri log baru dari klik ini)
18. Tutup Changelog

### TC-FA-FAAM-290: Item sudah terhapus saat bulk diproses dihitung terhapus tanpa baris log

19. Ganti isi kotak search dengan `290 {runId}-094`, tekan Enter
20. Centang baris `Bulk Clean A 290 {runId}-094`, `Bulk Clean B 290 {runId}-094`
21. Klik `Bulk Action` lalu `Delete`
22. Pelaku kedua lewat sesi API menghapus `Bulk Clean B 290 {runId}-094` hingga terhapus
23. Catat jumlah entri Changelog sebagai N3 lewat kemampuan baca
24. Klik `[Delete]` pada dialog
25. Verifikasi toast `Success, asset name has been deleted.` tampil
26. Buka Changelog dan baca entri teratas
27. Verifikasi entri teratas Changelog: Action `Delete`, Field `Asset Name`, Old `Bulk Clean A 290 {runId}-094`
28. Verifikasi jumlah entri Changelog sama dengan N3 + 1 (hanya satu baris Delete dari batch ini)
29. Tutup Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (R-16, langkah 1, 9, 19; Search `290 {runId}-094` pada langkah 19 menampilkan kedua baris salinan TC-FA-FAAM-290), `[OK]` menutup dialog blok (langkah 7), baseline Changelog (langkah 12, 23, S-12), dan membuka serta menutup Changelog (langkah 16, 18, 26, 29).
- Langkah pelaku kedua (langkah 3, 11, 22) ditulis "... hingga ... tersimpan" atau "hingga terhapus" (R-20). Pelaku kedua memakai sesi API sehingga spec ini bukan kelas multi-konteks.
- Baseline N2 dan N3 dicatat sesudah penghapusan oleh pelaku kedua agar entri Delete milik pelaku kedua tidak terhitung sebagai entri klik UI.
- Temuan untuk QA:
  - TC-FA-FAAM-268, TC-FA-FAAM-269, dan TC-FA-FAAM-290 berlabel Automation "Manual Only — (d) dua sesi paralel", tetapi langkah pelaku keduanya hanya memicu perubahan state; spec memakai sesi API (bagian 3 prinsip 13, pelaku kedua sesi API).
  - TC-FA-FAAM-268 Expected b "tanpa mutasi" tidak punya langkah observasi di TC; spec mengamatinya lewat baris tetap ada setelah `[OK]`.
  - TC-FA-FAAM-290 Expected b menyebut "baris Delete untuk `Bulk Clean A 290` dari batch ini"; entri Delete `Bulk Clean B 290` milik pelaku kedua tetap ada di Changelog dan dikecualikan lewat baseline N3.
