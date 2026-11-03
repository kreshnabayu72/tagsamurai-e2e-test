---
id: TC-FA-CAID-E2E-062-resilience-save-5xx-koneksi-terputus-dan-download-gagal
title: "Resilience B: Save 5xx, Koneksi Terputus, Respons Detik ke-59, dan Download Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAID-316
  - TC-FA-CAID-319
  - TC-FA-CAID-340
  - TC-FA-CAID-155
  - TC-FA-CAID-226
coverage:
  web: automated
---

# Resilience B: Save 5xx, Koneksi Terputus, Respons Detik ke-59, dan Download Gagal

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata dan asersi state backend, bagian 6 konvensi; bukan `Mode: mock` karena sebagian asersi membaca state server).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun aktor: Total Control Company Alpha (Pre-setup No 1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Hook suite (`suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id` disetel `seen`; konfigurasi Company Alpha baseline B1 (Pre-setup No 10) dan aset A1 sampai A5 (Pre-setup No 11) dipulihkan lewat seed API sesi aktor; layar awal Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka di `beforeEach`. Suite berjalan serial (`parallel: false`).
- Nilai data dirujuk lewat `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Data Pre-setup: konfigurasi Company Alpha baseline B1 (Pre-setup No 10: Master Switch ON, Separator `/ (Slash)`, segmen Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company) dan aset Pre-setup No 11: A1 Active `JKT/LAP/T490/0926/1`, A2 Draft `JKT/LAP/T490/0926/2`, A3 Waiting for Approval `JKT/LAP/T490/0000/3`, A4 Disposed `JKT/LAP/T490/0926/4`, A5 Deleted (tidak tampil di UI).
- Master data Code List Company Alpha (Pre-setup No 28): Groups `Head Office` (HO), `Head Office > Floor 1` (F1), `Head Office > Floor 2` (F2), `Jakarta Office` (JKT), `Surabaya Branch` (SBY, Excess), `Warehouse` (WH); Categories `IT Equipment` (ITE), `IT Equipment > Laptop` (LAP), `Old Equipment` (OLD, Locked), `Printer` (PRN); Asset Names `Dell, Latitude 14"` (DL14), `LaserJet Pro` (LJP), `ThinkPad T490` (T490); Divisions `Finance` (FIN), `Human Resources` (HR), `Operations` (OPS); Accounts Active `Computer Equipment` (1210) dan `Office Furniture` (1220). Di-seed di hook `before` lewat sesi API aktor (kemampuan disediakan tim FE) (dipakai TC-FA-CAID-155). Data Pre-setup No 15 (`Company Changelog`, entri seed L1 sampai L7; entri log audit lain tidak dihapus dan tidak diasersi) dan Pre-setup No 27 (General Settings baseline) dipakai sebagai precondition TC-FA-CAID-226, tidak diasersi; di-seed lewat API di hook `before` pada Company aktor (kemampuan disediakan tim FE/BE).
- Alat uji (Pre-setup No 26): penyunting request/respons pada sesi otomasi (`Spectra.intercept()`), pemutus jaringan, dan penunda respons. Kebutuhan intercept, dipasang dan dilepas lewat langkah eksplisit; nama endpoint konkret ditentukan tim FE di tahap script (tidak dikarang di spec): respons download Code List jawab 5xx (TC-FA-CAID-155); respons download Changelog jawab 5xx (TC-FA-CAID-226); respons Save jawab 5xx (TC-FA-CAID-316); jaringan sesi diputus lalu dipulihkan (TC-FA-CAID-319); respons Save ditahan 59 detik lewat `Spectra.intercept()` (TC-FA-CAID-340). Pengecualian timeout klien bagian 6 konvensi: batas tunggu klien tidak dapat digeser dengan jam, nilai tahanan ditulis eksplisit (59 detik, waktu nyata), jeda nyata di atas ±30 detik hanya sah di blok TC-FA-CAID-340, dan asersi absence toast mengikuti bagian 8b butir 11 (sesudah `Lepas tahanan respons` dan `Verifikasi` toast sukses).
- Kemampuan membaca jumlah entri Changelog Custom Asset ID sebelum aksi sebagai baseline N disediakan tim FE/BE (bagian 8b butir 10); jumlah entri tidak diasersi sebagai angka absolut (S-12). Surface log yang diperiksa adalah Modal Changelog: Custom Asset ID, karena TC menyebut "entri log" tanpa menyebut surface.
- Kemampuan membaca berkas hasil unduhan (nama berkas) disediakan tim FE. Jeda 5 detik untuk mengamati bahwa toast error tetap tampil (persisten sampai di-dismiss) adalah pilihan spec, bukan nilai TC.
- Data Dinamis: tidak ada. State global: konfigurasi Company Alpha menjadi Separator `- (Dash)` pada TC-FA-CAID-316, 319, dan 340 (Asset ID A1 sampai A3 ikut berubah lewat Retroactive Mass Update); dipulihkan ke baseline B1 lewat seed API sesi aktor di antara TC dan di hook `after`. Entri log yang bertambah tidak dihapus. Hook `after` juga melepas semua intercept dan memulihkan koneksi jaringan.

## Test Steps

### TC-FA-CAID-155: Download Code List sukses tanpa toast, gagal dengan toast error

1. Klik tautan `[View Code List]`
2. Klik icon Download, pilih `Download as CSV` pada tab `Group Codes`
3. Verifikasi download berhasil tidak menampilkan toast apa pun
4. Verifikasi berkas `Code-List-Group-Codes.csv` terunduh
5. Pasang intercept pada respons download Code List: jawab 5xx
6. Klik icon Download, pilih `Download as CSV` pada tab `Group Codes`
7. Verifikasi Toast error `Error, failed to download Code-List-Group-Codes.` tampil
8. Tunggu 5 detik tanpa menutup toast
9. Verifikasi toast error masih tampil (bertahan sampai di-dismiss)
10. Tutup toast error (dismiss)
11. Lepas intercept respons download Code List

### TC-FA-CAID-226: Download Changelog sukses tanpa toast, gagal dengan toast error

12. Klik `[✕]` pada header Modal View Code List
13. Klik tombol `[Changelog]` pada header kartu untuk membuka Modal Changelog
14. Klik icon Download, pilih `Download as CSV`
15. Verifikasi download berhasil tidak menampilkan toast
16. Verifikasi berkas `Changelog-Custom-Asset-ID.csv` terunduh
17. Pasang intercept pada respons download Changelog: jawab 5xx
18. Klik icon Download, pilih `Download as CSV`
19. Verifikasi Toast error `Error, failed to download Changelog-Custom-Asset-ID.` tampil
20. Tunggu 5 detik tanpa menutup toast
21. Verifikasi toast error masih tampil (bertahan sampai di-dismiss)
22. Tutup toast error (dismiss)
23. Lepas intercept respons download Changelog
24. Klik `[✕]` pada header Modal Changelog

### TC-FA-CAID-316: Save gagal 5xx

25. Catat jumlah entri Changelog Custom Asset ID sebagai baseline N
26. Pilih Separator `- (Dash)`
27. Pasang intercept pada respons Save: jawab 5xx
28. Klik `[Save]`
29. Verifikasi Toast error `Error, failed to save configuration.` tampil tanpa tombol aksi
30. Verifikasi form tetap terbuka dengan Separator `- (Dash)`
31. Verifikasi tombol `[Save]` aktif kembali
32. Buka Fixed Asset > Assets > All Assets lewat sidebar
33. Verifikasi dialog berjudul `Unsaved Changes` tampil
34. Verifikasi body dialog `You have unsaved changes. Are you sure you want to leave?`
35. Verifikasi tombol `[Cancel]` dan `[Leave]`
36. Klik `[Leave]`
37. Verifikasi Asset ID A1 sampai A4 tidak berubah (`JKT/LAP/T490/0926/1`, `JKT/LAP/T490/0926/2`, `JKT/LAP/T490/0000/3`, `JKT/LAP/T490/0926/4`)
38. Kembali ke Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu klik tombol `[Changelog]` pada header kartu
39. Verifikasi jumlah entri Changelog sama dengan baseline N (tidak ada entri baru)
40. Klik `[✕]` pada header Modal Changelog
41. Pilih Separator `- (Dash)` kembali
42. Lepas intercept respons Save
43. Klik `[Save]`
44. Verifikasi Toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
45. Buka Fixed Asset > Assets > All Assets
46. Verifikasi Asset ID A1 menjadi `JKT-LAP-T490-0926-1`
47. Pulihkan konfigurasi Company Alpha dan aset A1 sampai A5 ke baseline B1 lewat seed API sesi aktor, lalu muat ulang tab Custom Asset ID

### TC-FA-CAID-319: Save saat koneksi terputus

48. Pilih Separator `- (Dash)`
49. Putuskan koneksi jaringan pada sesi
50. Klik `[Save]`
51. Verifikasi Toast `Connection problem. Please try again.` tampil tanpa tombol aksi
52. Verifikasi form tetap terbuka dengan Separator `- (Dash)`
53. Verifikasi tombol `[Save]` aktif kembali
54. Pulihkan koneksi jaringan pada sesi
55. Klik `[Save]`
56. Verifikasi Toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
57. Buka Fixed Asset > Assets > All Assets
58. Verifikasi Asset ID A1 menjadi `JKT-LAP-T490-0926-1`
59. Pulihkan konfigurasi Company Alpha dan aset A1 sampai A5 ke baseline B1 lewat seed API sesi aktor, lalu muat ulang tab Custom Asset ID

### TC-FA-CAID-340: Respons Save pada detik ke-59

60. Pilih Separator `- (Dash)`
61. Tahan respons Save selama 59 detik lewat intercept, lalu klik `[Save]`
62. Lepas tahanan respons Save (respons tiba setelah 59 detik)
63. Verifikasi Toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
64. Verifikasi Toast `Connection problem. Please try again.` tidak tampil
65. Buka Fixed Asset > Assets > All Assets
66. Verifikasi Asset ID A1 menjadi `JKT-LAP-T490-0926-1`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. 66 langkah, di atas 35 langkah. Alasan: seluruh blok satu kelas harness (fault injection, bagian 3 prinsip 13b) dengan baseline B1 yang sama, tiap blok berdiri sendiri dan dipulihkan ke B1 lewat langkah penghubung (langkah 47 dan 59), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah panjang berasal dari blok Save yang masing-masing memverifikasi Asset ID di All Assets, dan dua blok download yang masing-masing memasang intercept.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC: TC-FA-CAID-155 dan 226 (download, tanpa mutasi), lalu 316, 319, dan 340 (Save). TC-FA-CAID-340 berakhir dengan konfigurasi Dash sehingga ditaruh paling akhir; `beforeEach` suite spec berikutnya memulihkan B1.
- Langkah penghubung (tanpa `Verifikasi`): pemasangan dan pelepasan intercept (dilepas segera setelah pemicu selesai, S-09), `[✕]` pada Modal View Code List dan Modal Changelog, "Tunggu 5 detik tanpa menutup toast" dan "Tutup toast error" (jendela pengamatan toast persisten), langkah 41 (memilih ulang Separator `- (Dash)` karena pilihan form dibuang saat `[Leave]`; langkah TC-FA-CAID-316), serta langkah 47 dan 59 (memulihkan baseline B1 antar TC, S-09).
- Pada TC-FA-CAID-316 membuka All Assets (langkah 32) saat form masih dirty memunculkan dialog `Unsaved Changes` (D-01, NC-02), diasersi pada langkah 33 sampai 35 dan dikonfirmasi `[Leave]` secara deterministik (S-08). Karena pilihan form dibuang, retry Save didahului memilih ulang Separator `- (Dash)` (langkah 41), sesuai langkah TC.
- Asersi absence "download berhasil tidak menampilkan toast" (langkah 3 dan 15) diletakkan tepat di bawah langkah pemicu (langkah 2 dan 14) dan sebelum `Verifikasi` berkas terunduh (langkah 4 dan 16): pemicu menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas (bagian 8b butir 11; `Verifikasi` berkas ditambahkan spec dan dicatat di sini, S-03). Asersi "toast `Connection problem` tidak tampil" pada TC-FA-CAID-340 (langkah 64) ditulis sesudah `Lepas tahanan respons` (langkah 62) dan `Verifikasi` toast sukses (langkah 63) yang menjadi anchor positif (pengecualian respons ditahan, bagian 8b butir 11).
- Pembagian TC lintas spec: TC-FA-CAID-12, 159, 230, 317, dan 321 ada di spec 061; TC-FA-CAID-318, 320, dan 332 ada di spec 063.
- Temuan untuk QA:
  - TC-FA-CAID-316 b menyebut "tidak ada entri log" tanpa menyebut surface; spec memeriksa jumlah entri Modal Changelog terhadap baseline N.
  - TC-FA-CAID-155 dan 226 menyebut "bertahan sampai di-dismiss" tanpa menyebut durasi pengamatan; spec memakai jeda 5 detik.
