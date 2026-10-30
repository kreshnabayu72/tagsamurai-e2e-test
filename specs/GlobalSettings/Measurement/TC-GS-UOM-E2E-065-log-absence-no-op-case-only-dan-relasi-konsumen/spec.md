---
id: TC-GS-UOM-E2E-065-log-absence-no-op-case-only-dan-relasi-konsumen
title: "Tidak Ada Pencatatan Log: Edit No-Op, Case-Only, dan Perubahan Relasi dari Produk Konsumen"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UOM-217
  - TC-GS-UOM-218
  - TC-GS-UOM-225
  - TC-GS-UOM-330
  - TC-GS-UOM-220
  - TC-GS-UOM-267
coverage:
  web: automated
---

# Tidak Ada Pencatatan Log: Edit No-Op, Case-Only, dan Perubahan Relasi dari Produk Konsumen

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > Master Reference > Measurement.
- Pelaku pemicu (hanya lewat sesi API, tanpa login UI): Admin FAMS Client A, `famsAdmin_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.FA_ADMIN_PASSWORD`. Email akun ini tidak tertulis di Pre-setup TC Measurement (lihat Temuan untuk QA); fixture disediakan tim FE. Admin FAMS berhak membuat dan mengubah Asset Name FAMS.
- Environment variable: `GS_TC_PASSWORD`, `FA_ADMIN_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel `seen` oleh hook suite (lihat `suite.md`, bagian Hook suite).
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi), di-seed lewat API di hook `before`, milik spec ini; tiap TC punya unit dan baseline sendiri (kelas g):

  | Unit | Symbol | Keadaan | Dipakai TC |
  |---|---|---|---|
  | `Ton {runId}-065` | `t` | bebas relasi | 217 (Edit No-Op) |
  | `Roll {runId}-065` | `roll` | bebas relasi | 218 (Edit case-only) |
  | `Kelvin {runId}-065` | `K` | bebas relasi sampai Asset Name `Cable Roll {runId}-065` dibuat Admin FAMS pada langkah 9 | 225 |
  | `Cask {runId}-065` | `csk` | dipakai Asset Name FAMS `Grain Scoop {runId}-065` (di-seed lewat API) | 330 |
  | `Keg {runId}-065` | `keg` | bebas relasi | 330 |
  | `Liter {runId}-065` | `L` | bebas relasi | 220 dan 267 (terhapus Bulk Delete) |
  | `Pack {runId}-065` | `pk` | bebas relasi | 220 dan 267 (terhapus Bulk Delete) |
  | `Box {runId}-065` | `box` | dipakai Asset Name FAMS `Box Item {runId}-065` (di-seed lewat API) | 220 dan 267 (dilewati) |

- Nilai field wajib lain Asset Name FAMS yang dibuat atau di-seed lewat API (`Cable Roll`, `Grain Scoop`, `Box Item`): Category (kategori daun) dan TAG Type (minimal 1 opsi). Fixture `fixtures/measurement.json` belum ada; tim FE menyediakannya:

  | Kunci fixture | Field | Nilai |
  |---|---|---|
  | `assetName.category` | Category | disediakan tim FE |
  | `assetName.tagType` | TAG Type | disediakan tim FE |

  Field Measurement Asset Name diisi unit yang dirujuk langkah.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Asset Name `Cable Roll`, `Grain Scoop`, dan `Box Item` bersuffix `{runId}-065` bila ada, lalu semua unit bersuffix `{runId}-065` bila masih ada (Asset Name dihapus sebelum unitnya); pulihkan page size tabel Measurement ke 10.
- Kemampuan teknis: sesi API aktor (lihat `suite.md`, bagian Hook suite) untuk Admin FAMS membuat dan mengubah Asset Name FAMS; akses Total Control ke Detail User Sari Dewi > Tab System Log dan Global Settings > Activity Log.
- Baseline log (S-12): jumlah entri tiap unit milik spec pada Changelog, System Log aktor, dan Activity Log dicatat sebelum aksi pemicu pertama (langkah 1 sampai 3); pembanding Last Updated Kelvin, Cask, dan Keg dicatat pada langkah 4. Total entri tidak diasersi sebagai angka absolut.
- Tidak ada state global yang diubah.
- TC-GS-UOM-217, 218, 225, 330, 220, 267: login sebagai Total Control dan berada di Global Settings > Master Reference > Measurement.

## Test Steps

### Baseline

1. Buka Changelog, ketik Search `{runId}-065`, tekan Enter, catat jumlah entri tiap unit milik spec (Ton, Roll, Kelvin, Cask, Keg, Liter, Pack, Box) sebagai baseline Changelog, lalu tutup Changelog
2. Buka Global Settings > User > Detail Sari Dewi > Tab System Log, ketik Search `{runId}-065`, tekan Enter, catat jumlah entri tiap unit milik spec sebagai baseline System Log
3. Buka Global Settings > Activity Log, pilih tab `User Action`, ketik Search `{runId}-065`, tekan Enter, catat jumlah entri tiap unit milik spec sebagai baseline Activity Log
4. Buka Global Settings > Master Reference > Measurement, ketik Search `{runId}-065`, tekan Enter, catat Last Updated `Kelvin {runId}-065`, `Cask {runId}-065`, dan `Keg {runId}-065`

### TC-GS-UOM-217: Edit No-Op tidak mencatat entri di seluruh surface (aksi)

5. Klik `⋯` pada baris `Ton {runId}-065` > Edit, klik [Save] tanpa mengubah apa pun
6. Verifikasi toast netral: "No changes to save."

### TC-GS-UOM-218: Edit case-only tidak mencatat entri (aksi)

7. Klik `⋯` pada baris `Roll {runId}-065` > Edit, ubah Unit Name menjadi `ROLL {runId}-065` dan Symbol menjadi `ROLL`, klik [Save]
8. Verifikasi toast netral: "No changes to save."

### TC-GS-UOM-225: Perubahan relasi dari produk konsumen tidak mengubah Last Updated dan tidak dicatat

9. [Admin FAMS, sesi API] Buat Asset Name `Cable Roll {runId}-065` dengan Measurement `Kelvin {runId}-065` hingga tersimpan
10. Muat ulang halaman Measurement, ketik Search `Kelvin {runId}-065`, tekan Enter, klik teks `Kelvin {runId}-065`
11. Verifikasi Item Type List Detail Kelvin memuat `Cable Roll {runId}-065` (Fixed Asset)
12. Tutup Unit Detail
13. Verifikasi Last Updated `Kelvin {runId}-065` tidak berubah dari langkah 4

### TC-GS-UOM-330: Mengubah Measurement Asset Name di FAMS memindahkan Item Type tanpa mengubah Last Updated

14. [Admin FAMS, sesi API] Ubah Measurement Asset Name `Grain Scoop {runId}-065` dari `Cask {runId}-065` menjadi `Keg {runId}-065` hingga tersimpan
15. Muat ulang halaman Measurement, ketik Search `Cask {runId}-065`, tekan Enter, klik teks `Cask {runId}-065`
16. Verifikasi Item Type List Detail Cask menampilkan Title `No item types linked`
17. Tutup Unit Detail, ganti isi kotak search dengan `Keg {runId}-065`, tekan Enter, klik teks `Keg {runId}-065`
18. Verifikasi Item Type List Detail Keg memuat `Grain Scoop {runId}-065`
19. Tutup Unit Detail, ganti isi kotak search dengan `{runId}-065`, tekan Enter
20. Verifikasi Last Updated `Cask {runId}-065` tidak berubah dari langkah 4
21. Verifikasi Last Updated `Keg {runId}-065` tidak berubah dari langkah 4

### TC-GS-UOM-220 dan TC-GS-UOM-267: Bulk Delete campuran (aksi)

22. Centang baris `Liter {runId}-065`, `Pack {runId}-065`, dan `Box {runId}-065`
23. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
24. Klik [Continue] pada dialog Bulk Delete campuran
25. Verifikasi toast: "Success, unit has been deleted. Some items were skipped."

### Pemeriksaan ulang Changelog

26. Buka Changelog, ketik Search `{runId}-065`, tekan Enter
27. Verifikasi Changelog memuat baris Action `Delete` untuk `Liter {runId}-065` dan `Pack {runId}-065` (anchor positif)
28. Verifikasi Changelog: jumlah entri `Ton {runId}-065` tidak bertambah dari langkah 1 (TC-GS-UOM-217)
29. Verifikasi Changelog: jumlah entri `Roll {runId}-065` tidak bertambah dari langkah 1 (TC-GS-UOM-218)
30. Verifikasi Changelog: jumlah entri `Kelvin {runId}-065` tidak bertambah dari langkah 1 (TC-GS-UOM-225)
31. Verifikasi Changelog: jumlah entri `Cask {runId}-065` tidak bertambah dari langkah 1 (TC-GS-UOM-330)
32. Verifikasi Changelog: jumlah entri `Keg {runId}-065` tidak bertambah dari langkah 1 (TC-GS-UOM-330)
33. Verifikasi Changelog: tidak ada baris Delete untuk `Box {runId}-065` dan jumlah entrinya tidak bertambah dari langkah 1 (TC-GS-UOM-220)

### Pemeriksaan ulang System Log

34. Tutup Changelog, buka Global Settings > User > Detail Sari Dewi > Tab System Log, ketik Search `{runId}-065`, tekan Enter
35. Verifikasi System Log memuat baris Delete untuk `Liter {runId}-065` dan `Pack {runId}-065` (anchor positif)
36. Verifikasi System Log: jumlah entri `Ton {runId}-065` tidak bertambah dari langkah 2
37. Verifikasi System Log: jumlah entri `Roll {runId}-065` tidak bertambah dari langkah 2
38. Verifikasi System Log: tidak ada baris Delete untuk `Box {runId}-065` dan jumlah entrinya tidak bertambah dari langkah 2 (TC-GS-UOM-267)

### Pemeriksaan ulang Activity Log

39. Buka Global Settings > Activity Log, pilih tab `User Action`, ketik Search `{runId}-065`, tekan Enter
40. Verifikasi Activity Log memuat baris Delete untuk `Liter {runId}-065` dan `Pack {runId}-065` (anchor positif)
41. Verifikasi Activity Log: jumlah entri `Ton {runId}-065` tidak bertambah dari langkah 3
42. Verifikasi Activity Log: jumlah entri `Roll {runId}-065` tidak bertambah dari langkah 3
43. Verifikasi Activity Log: tidak ada baris Delete untuk `Box {runId}-065` dan jumlah entrinya tidak bertambah dari langkah 3 (TC-GS-UOM-267)

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Kelas g (asersi absence) untuk aksi UI tunggal dan pemicu perubahan relasi dari produk konsumen oleh Admin FAMS lewat sesi API.
- Pembagian TC lintas spec: TC-GS-UOM-73 dan 74 (aksi Edit No-Op dan case-only, toast `No changes to save.`) di spec 027; TC-GS-UOM-217 dan 218 (asersi tidak ada entri di tiga surface) di spec ini dengan aksi dan baseline sendiri (S-05). TC-GS-UOM-217 bergantung TC-GS-UOM-73 (kolom Dependensi), sehingga spec ini mengulang aksi No-Op Ton dengan unit milik spec. TC-GS-UOM-220 dan 267 terbelah: presence (baris Delete Liter dan Pack) di spec `TC-GS-UOM-E2E-064-log-bulk-delete-dan-aktor-non-total-control`, absence (tidak ada entri `Box`) di spec ini dengan Bulk Delete campuran dan baseline sendiri; id keduanya ada di `sourceTc` kedua spec (S-05). TC-GS-UOM-225 dan 330 (relasi dari produk konsumen: Last Updated tidak berubah, tidak ada entri Changelog) di spec ini; isi Item Type List yang diasersi ikut di spec ini. TC-GS-UOM-390 (Last Updated Meter tidak berubah saat relasi bertambah dan berkurang) di spec 058.
- Anchor absence (butir 2 bagian 8b): toast netral `No changes to save.` (langkah 6 dan 8) menjadi anchor untuk absence entri Ton dan Roll; baris Delete `Liter` dan `Pack` di surface yang sama (langkah 27, 35, 40) menjadi anchor untuk absence entri Box; Item Type List Detail (langkah 11, 16, 18) menjadi anchor untuk absence entri Kelvin, Cask, dan Keg. Asersi memakai baseline jumlah entri (langkah 1 sampai 3), bukan posisi baris teratas.
- Langkah penghubung: langkah 1 sampai 4 (baseline), langkah 10, 15 (muat ulang Tab Measurement dan membuka Detail; sesuai Langkah Uji TC-GS-UOM-225 dan 330), langkah 12, 17, 19 (menutup Unit Detail dan Search unit berikutnya), langkah 22 (centang baris hasil Search `{runId}-065` yang memuat delapan unit milik spec), langkah 34 dan 39 (navigasi ke System Log dan Activity Log); langkah 3 dan 39 juga memilih tab `User Action` pada Activity Log.
- Sumber memakai Ton, Roll, Kelvin (D-05), Cask (D-24), Keg (D-25), dan Liter, Pack, Box Pre-setup secara literal; spec memakai unit milik spec bersuffix `{runId}-065` (S-06, S-12) dan Asset Name FAMS milik spec (`Cable Roll`, `Grain Scoop`, `Box Item`).
- Spec memuat 43 langkah (melewati batas 35 langkah); seluruhnya satu kelas harness (absence log) dengan satu set data, dan blok pemeriksaan ulang tiga surface adalah blok baca-log berpola yang tidak dihitung ke batas (konvensi bagian 3, prinsip 13). Blok aksi dan pemeriksaan ulang dikumpulkan di akhir supaya tiap surface dibuka sekali; tiap TC punya unit dan baseline sendiri.
- Temuan untuk QA:
  - Akun Admin FAMS tidak ada di Pre-setup TC Measurement; spec memakai Admin FAMS Client A yang disediakan tim FE (S-13). TC-GS-UOM-225 dan 330 menyebut "Di FAMS" tanpa menyebut pelaku; spec memakai sesi API Admin FAMS.
  - TC-GS-UOM-217 Expected "Tidak ada entri baru untuk Ton di ketiga surface" bergantung TC-GS-UOM-73; Last Updated Ton tidak diasersi di spec ini karena bukan Expected TC-GS-UOM-217.
  - TC-GS-UOM-330 menyebut "Asset Name Grain Scoop memakai Keg" sebagai Post Condition tanpa langkah observasi; tidak diasersi.
  - TC-GS-UOM-217, 218, dan 267 menyebut Activity Log tanpa menyebut tab; log mutasi Measurement ada di tab `User Action` (`global-settings/activity-log/PRD/activity-log.md` §4.1.2), sehingga langkah 3 dan 39 memilih tab `User Action` sebelum Search. Isi `Verifikasi` langkah 41 sampai 43 dan baseline langkah 3 tidak berubah.
