---
id: TC-GS-UOM-E2E-066-sync-fams-form-dan-agregasi
title: "Sinkronisasi Unit ke Fixed Asset: Opsi Dropdown Asset Name, Rename, Stale Reference, dan Hapus Referensi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-226
  - TC-GS-UOM-228
  - TC-GS-UOM-229
  - TC-GS-UOM-230
  - TC-GS-UOM-231
  - TC-GS-UOM-269
coverage:
  web: automated
---

# Sinkronisasi Unit ke Fixed Asset: Opsi Dropdown Asset Name, Rename, Stale Reference, dan Hapus Referensi

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > Master Reference > Measurement. Akun yang sama membuka FAMS > Settings > Asset Master (lintas modul); akses Total Control ke FAMS diasumsikan (lihat Temuan untuk QA).
- Pelaku pemicu (hanya lewat sesi API, tanpa login UI):

  | Peran dalam spec | Role | Email | Environment variable password |
  |---|---|---|---|
  | Admin lain (rename dan hapus unit) | Total Control Client A kedua | `totalControlSecond_automated_qaTeam1@qwertysystem.net` | `GS_TC2_PASSWORD` |
  | Admin FAMS (buat dan hapus Asset Name FAMS) | Admin FAMS Client A | `famsAdmin_automated_qaTeam1@qwertysystem.net` | `FA_ADMIN_PASSWORD` |

  Kedua akun tidak tertulis di Pre-setup TC Measurement (lihat Temuan untuk QA); fixture disediakan tim FE.
- Environment variable: `GS_TC_PASSWORD`, `GS_TC2_PASSWORD`, `FA_ADMIN_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel `seen` oleh hook suite (lihat `suite.md`, bagian Hook suite).
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi), milik spec ini:
  - `Carton {runId}-066` / `ctn` (D-16): dibuat spec lewat UI pada TC-GS-UOM-226; di-rename Admin lain menjadi `Carton Pack {runId}-066` pada TC-GS-UOM-229.
  - `Yard {runId}-066` / `yd` (bebas relasi, di-seed lewat API; dihapus spec lewat UI pada TC-GS-UOM-230, setara dependensi TC-GS-UOM-147).
  - `Quart {runId}-066` / `qt` (bebas relasi, di-seed lewat API; dihapus Admin lain pada TC-GS-UOM-231, setara dependensi TC-GS-UOM-56).
  - `Dozen {runId}-066` / `dz`: di-seed lewat API; dipakai Asset Name FAMS `Egg Tray {runId}-066` dan item Supply `Egg Carton {runId}-066` (pengganti Dozen Pre-setup); di-rename spec menjadi `Dozen Pack {runId}-066` pada TC-GS-UOM-228. Referensi Supply (SAMS) disediakan tim FE lewat fixture backend (NC-09).
  - `Kelvin {runId}-066` / `K` (D-05): di-seed lewat API; dipakai Asset Name FAMS `Cable Roll {runId}-066`; dihapus spec lewat UI pada TC-GS-UOM-269.
  - Asset Name FAMS milik spec: `Egg Tray {runId}-066`, `Cable Roll {runId}-066`, serta `Carton Item {runId}-066` (dibuat lewat form FAMS pada TC-GS-UOM-229) dan `Quart Item {runId}-066` (tidak jadi tersimpan pada TC-GS-UOM-231).
- Nilai field wajib lain Asset Name FAMS yang dibuat lewat form UI atau API: Category (kategori daun) dan TAG Type (minimal 1 opsi). Fixture `fixtures/measurement.json` belum ada; tim FE menyediakannya:

  | Kunci fixture | Field | Nilai |
  |---|---|---|
  | `assetName.category` | Category | disediakan tim FE |
  | `assetName.tagType` | TAG Type | disediakan tim FE |
  | `supplyItem.*` | Item Supply `Egg Carton` yang memakai Measurement | disediakan tim FE |

- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Asset Name FAMS `Carton Item`, `Egg Tray`, `Cable Roll`, `Quart Item` bersuffix `{runId}-066` dan item Supply `Egg Carton {runId}-066` bila ada, lalu semua unit bersuffix `{runId}-066` (nama yang masih ada: `Carton` atau `Carton Pack`, `Yard`, `Quart`, `Dozen` atau `Dozen Pack`, `Kelvin`) bila masih ada (Asset Name dihapus sebelum unitnya).
- Kemampuan teknis: sesi API aktor (lihat `suite.md`, bagian Hook suite) untuk Admin lain (Edit dan Delete Measurement) dan Admin FAMS (membuat dan menghapus Asset Name FAMS); akses ke form Create Asset Name FAMS (FAMS > Settings > Asset Master) dan field dropdown Measurement.
- Tidak ada state global yang diubah.
- TC-GS-UOM-226, 228, 229, 230, 231, 269: login sebagai Total Control dan berada di Global Settings > Master Reference > Measurement.

## Test Steps

### TC-GS-UOM-226: Unit baru muncul di dropdown Measurement form Asset Name FAMS

1. Klik [+ Unit], isi Unit Name `Carton {runId}-066` dan Symbol `ctn`, klik [Submit]
2. Tunggu aksi selesai (form tertutup)
3. Buka FAMS > Settings > Asset Master > Create Asset Name
4. Buka dropdown Measurement
5. Verifikasi opsi `Carton {runId}-066` tersedia

### TC-GS-UOM-229: Form konsumen yang memilih unit yang di-rename tetap sukses Submit

6. Pilih opsi `Carton {runId}-066` pada field Measurement, isi Asset Name `Carton Item {runId}-066` dan field wajib lain dari fixture
7. [Admin lain, sesi API] Ubah Unit Name `Carton {runId}-066` menjadi `Carton Pack {runId}-066` hingga tersimpan
8. Klik [Submit] pada form Create Asset Name FAMS
9. Verifikasi Submit sukses (bukan error stale reference)
10. Buka FAMS > Settings > Asset Master, buka Asset Name `Carton Item {runId}-066`
11. Verifikasi Asset Name `Carton Item {runId}-066` tersimpan dengan Measurement `Carton Pack {runId}-066`

### TC-GS-UOM-231: Form Asset Name dengan unit terpilih yang dihapus admin lain menampilkan error field dan auto-clear

12. Buka FAMS > Settings > Asset Master > Create Asset Name, pilih `Quart {runId}-066` pada field Measurement, isi Asset Name `Quart Item {runId}-066` dan field wajib lain dari fixture
13. [Admin lain, sesi API] Hapus `Quart {runId}-066` hingga tersimpan
14. Klik [Submit] pada form Create Asset Name FAMS
15. Verifikasi error field Measurement: `This measurement no longer exists. Please select another.`
16. Verifikasi field Measurement dikosongkan
17. Buka dropdown Measurement
18. Verifikasi opsi `Carton Pack {runId}-066` tersedia di dropdown (anchor positif)
19. Verifikasi opsi di-refresh sehingga `Quart {runId}-066` tidak ada di dropdown Measurement
20. Verifikasi input valid lain (Asset Name `Quart Item {runId}-066`) tetap terisi
21. Klik `✕` pada form Create Asset Name
22. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
23. Klik `[Leave]`

### TC-GS-UOM-230: Unit yang dihapus hilang dari dropdown konsumen

24. Buka Global Settings > Master Reference > Measurement, ketik Search `Yard {runId}-066`, tekan Enter, klik `⋯` pada baris tersebut > Delete, klik [Delete] pada dialog
25. Verifikasi toast sukses: "Success, unit has been deleted."
26. Buka FAMS > Settings > Asset Master > Create Asset Name, buka dropdown Measurement
27. Verifikasi opsi `Carton Pack {runId}-066` tersedia di dropdown (anchor positif)
28. Verifikasi opsi `Yard {runId}-066` tidak ada di dropdown
29. Klik `✕` pada form Create Asset Name (form tidak berisi perubahan)

### TC-GS-UOM-228: Rename unit tercermin di FAMS Asset Master tanpa mengubah relasi

30. Buka Global Settings > Master Reference > Measurement, ketik Search `Dozen {runId}-066`, tekan Enter, klik `⋯` pada baris tersebut > Edit, ubah Unit Name menjadi `Dozen Pack {runId}-066`, klik [Save]
31. Tunggu aksi selesai (modal tertutup)
32. Buka FAMS > Settings > Asset Master, buka Asset Name `Egg Tray {runId}-066`
33. Verifikasi Measurement Egg Tray tampil `Dozen Pack {runId}-066`
34. Buka Global Settings > Master Reference > Measurement, ketik Search `Dozen Pack {runId}-066`, tekan Enter, klik teks `Dozen Pack {runId}-066`
35. Verifikasi Item Type List Detail `Dozen Pack {runId}-066` memuat `Egg Carton {runId}-066`
36. Verifikasi Item Type List Detail `Dozen Pack {runId}-066` memuat `Egg Tray {runId}-066`
37. Tutup Unit Detail

### TC-GS-UOM-269: Penghapusan referensi di FAMS membuat unit bebas relasi dan dapat dihapus

38. [Admin FAMS, sesi API] Hapus Asset Name `Cable Roll {runId}-066` hingga tersimpan
39. Muat ulang halaman Measurement, ketik Search `Kelvin {runId}-066`, tekan Enter, klik teks `Kelvin {runId}-066`
40. Verifikasi Item Type List Detail Kelvin menampilkan Title `No item types linked`
41. Tutup Unit Detail, klik `⋯` pada baris `Kelvin {runId}-066` > Delete
42. Verifikasi dialog `Delete Unit` tampil (bukan `Cannot Delete Data`)
43. Klik [Delete] pada dialog
44. Verifikasi toast sukses: "Success, unit has been deleted."
45. Verifikasi `Kelvin {runId}-066` hilang dari tabel

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Kelas harness: lintas modul (Fixed Asset sebagai konsumen); pelaku kedua (Admin lain, Admin FAMS) hanya memicu perubahan state lewat sesi API.
- Urutan TC di spec berbeda dari urutan sumber: 226 (pembuatan unit dan opsi dropdown), 229 (memakai unit yang sama dan form yang sama), 231 (stale reference), 230 (hapus unit), 228 (rename), lalu 269 (Delete, paling akhir; prinsip 5). TC-GS-UOM-226 dan 229 berbagi form Create Asset Name yang dibuka sekali (langkah 3 sampai 9, lalu langkah 10 dan 11 membuka dan membaca Asset Name yang tersimpan). Form dibuka tiga kali (langkah 3, 12, 26) dan ditutup tiga kali (Submit sukses menutup form pada langkah 8; `✕` pada langkah 21 dan 29).
- Dependensi dijalankan sebagai langkah atau seeding di spec ini: TC-GS-UOM-226 (langkah 1 sampai 5), TC-GS-UOM-147 dan 56 (seeding `Yard` dan `Quart`; pembuatannya bukan objek uji), TC-GS-UOM-225 (seeding `Kelvin` dan Asset Name `Cable Roll`).
- Sumber memakai nama literal (Carton, Yard, Quart, Dozen, Kelvin, Egg Tray, Cable Roll); spec memakai nama bersuffix `{runId}-066` (S-12) dan unit milik spec sebagai pengganti baris Pre-setup `Dozen` (S-06).
- Langkah penghubung: langkah 2 (menunggu Create selesai sebelum pindah ke FAMS), langkah 10 (membuka Asset Name `Carton Item {runId}-066` yang baru tersimpan di FAMS supaya Measurement-nya teramati; aksi tanpa `Verifikasi`), langkah 17 (membuka dropdown Measurement untuk mengamati opsi sesudah error stale reference), langkah 21 sampai 23 (menutup form Create Asset Name dirty lewat `✕`, dialog `Unsaved Changes`, dan `[Leave]`; S-08), langkah 24, 30, 34, dan 39 (Search baris target pada tabel Measurement), langkah 29 (menutup form bersih), langkah 31 (menunggu aksi selesai sebelum pindah ke FAMS), langkah 37 dan 41 (menutup Unit Detail).
- Langkah 27 (opsi `Carton Pack` tersedia) menjadi anchor positif bagi absence `Yard` pada langkah 28 (bagian 8b butir 2). Langkah 18 (opsi `Carton Pack` tersedia) menjadi anchor positif bagi absence `Quart` pada langkah 19; error pada langkah 15 tidak dipakai sebagai anchor isi dropdown.
- Langkah 6 dan 12 mengisi field wajib lain Asset Name FAMS dari fixture karena Submit tidak dapat dikirim tanpa field itu (S-11); TC hanya menyebut "isi field lain" pada TC-GS-UOM-231.
- Spec ini di atas batas 35 langkah (45): seluruhnya satu kelas harness (sinkronisasi lintas modul ke Fixed Asset) dengan satu dataset unit milik spec; memecahnya mengulang seeding Asset Name yang sama.
- Temuan untuk QA:
  - TC-GS-UOM-226, 228, 229, 230, 231, 269 mempunyai precondition aktor Total Control yang membuka modul FAMS (Asset Master); TC tidak menyatakan apakah akun Total Control Global Settings memiliki akses FAMS. Spec mengasumsikannya.
  - Akun Admin lain dan Admin FAMS tidak ada di Pre-setup TC Measurement (S-13); fixture Supply (item `Egg Carton`) disediakan tim FE.
  - TC-GS-UOM-229 tidak menyebut Asset Name yang disubmit, Post Condition tidak ada; spec memakai `Carton Item {runId}-066` dan mengasersi Measurement hasilnya sesuai Expected b.
  - TC-GS-UOM-228 dan 269 tidak punya Post Condition di luar Expected; Post Condition "Dozen menjadi Dozen Pack" dan "Kelvin terhapus" dicakup langkah 33 dan 45.
  - TC-GS-UOM-229 Expected b ("Asset Name tersimpan dengan Measurement yang sama (tampil `Carton Pack`)") tidak memberi langkah menuju layar tempat Asset Name dan Measurement-nya terlihat; spec menambah langkah 10 (membuka Asset Name di FAMS > Settings > Asset Master) sebagai langkah penghubung supaya langkah 11 dapat diamati.
