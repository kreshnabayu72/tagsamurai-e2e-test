---
id: TC-GS-TAG-E2E-078-download-registri-isi-file-nama-kolom-dan-hasil-nol
title: "Download Registri: Isi File CSV/XLSX Mengikuti Search/Filter/Tab, Nama File, Kolom Tampil, Transformasi Sel, dan Hasil Nol"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-239
  - TC-GS-TAG-240
  - TC-GS-TAG-241
  - TC-GS-TAG-242
  - TC-GS-TAG-244
coverage:
  web: automated
---

# Download Registri: Isi File CSV/XLSX Mengikuti Search/Filter/Tab, Nama File, Kolom Tampil, Transformasi Sel, dan Hasil Nol

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sari Dewi (Pre-setup TC, Client A) `totalControl_automated_qaTeam1@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Seed Registri A Client A (DD-01 sampai DD-30; 30 baris, 4 Paired dan 26 Not Paired; Tabel Data Uji Dinamis TC). Di-seed dan direset idempotent lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme tidak didefinisikan di TC, Q-4). Identifier TAG bersifat tetap dan tanpa sufiks `{runId}` (`suite.md`, S-12). Spec hanya membaca data; hitungan baris file (30, 24, 4) valid hanya bila Seed Registri A utuh dan suite berjalan serial.
- General Settings: Date Format `dd/MM/yy`, 24-hour, Asia/Jakarta (default Client A); spec ini tidak mengubahnya (Last Scanned DD-01 pada file XLSX = `16/09/26 14:30`).
- Suite serial (`parallel: false`).
- Flag Guided Tooltip registri (`guided_tooltip_seen_gs-tag-registry`) disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): filter dan Search registri dikosongkan, visibilitas kolom dikembalikan ke default lewat `[Reset to Default]` Setup Column, dan berkas unduhan dihapus.
- Kemampuan teknis (kelas binary buffer, prinsip 13f): menangkap berkas unduhan browser (event download) ke direktori bersih per unduhan supaya nama berkas yang sama tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV (header, jumlah baris data) dan XLSX (nilai sel baris DD-01 dan DD-05). Kegagalan unduhan (5xx) ada di spec `TC-GS-TAG-E2E-079-download-registri-gagal` dan unduhan lebih dari 5.000 baris di spec `TC-GS-TAG-E2E-080-download-registri-lebih-5000-baris`.

## Test Steps

### TC-GS-TAG-239: Download mengikuti Search, Filter, dan tab aktif

1. Klik ikon Download di toolbar, lalu klik `Download as CSV` (tanpa Search dan Filter)
2. Verifikasi file CSV memuat 30 baris data (seluruh dataset, bukan hanya 10 baris halaman)
3. Verifikasi nama file `All-TAGs.csv`
4. Klik ikon Filter untuk membuka panel
5. Pilih `Source` = Official
6. Klik `Apply`
7. Klik ikon Filter untuk menutup panel
8. Klik ikon Download, lalu klik `Download as CSV`
9. Verifikasi file CSV memuat 24 baris data
10. Klik Tab Paired
11. Klik ikon Download, lalu klik `Download as CSV`
12. Verifikasi file CSV memuat 4 baris data
13. Verifikasi nama file `Paired-TAGs.csv`
14. Klik Tab All
15. Klik ikon Filter untuk membuka panel
16. Klik `Clear Field`, lalu klik `Apply`
17. Klik ikon Filter untuk menutup panel

### TC-GS-TAG-240: Nama file dan ekstensi mengikuti pilihan format dan tab

18. Klik ikon Download, lalu klik `Download as XLSX` (Tab All)
19. Verifikasi tidak ada toast sukses
20. Verifikasi nama file `All-TAGs.xlsx`
21. Klik Tab Paired
22. Klik ikon Download, lalu klik `Download as XLSX`
23. Verifikasi tidak ada toast sukses
24. Verifikasi nama file `Paired-TAGs.xlsx`
25. Klik Tab Not Paired
26. Klik ikon Download, lalu klik `Download as CSV`
27. Verifikasi tidak ada toast sukses
28. Verifikasi nama file `Not-Paired-TAGs.csv`
29. Klik Tab All

### TC-GS-TAG-241: Download hanya memuat kolom yang sedang tampil

30. Sembunyikan kolom `SKU` dan `Brand` lewat overlay Column Visibility (⋯), lalu tutup overlay
31. Klik ikon Download, lalu klik `Download as CSV`
32. Verifikasi tidak ada toast peringatan
33. Verifikasi header file CSV pertama memuat kolom yang tampil (mis. `Code`)
34. Verifikasi header file CSV pertama tidak memuat kolom `SKU` dan `Brand`
35. Tampilkan kembali kolom `SKU` lewat overlay Column Visibility (⋯), lalu tutup overlay
36. Klik ikon Download, lalu klik `Download as CSV`
37. Verifikasi tidak ada toast peringatan
38. Verifikasi header file CSV kedua memuat kolom `SKU`
39. Tampilkan kembali kolom `Brand` lewat overlay Column Visibility (⋯), lalu tutup overlay

### TC-GS-TAG-242: Transformasi sel export

40. Tampilkan kolom `Last Scanned In` lewat overlay Column Visibility (⋯), lalu tutup overlay
41. Klik ikon Download, lalu klik `Download as XLSX`
42. Buka file XLSX dan baca baris DD-01 dan DD-05
43. Verifikasi kolom TAG Type berisi label `RFID` (DD-01) dan `QR` (DD-05), bukan nama ikon
44. Verifikasi kolom Status baris DD-01 berisi teks `Paired`
45. Verifikasi kolom Brand baris DD-01 berisi teks `Zebra`
46. Verifikasi kolom Last Scanned In baris DD-01 berisi label `Fixed Asset` (tanpa warna)
47. Verifikasi kolom Last Scanned baris DD-01 mengikuti format General Settings (`16/09/26 14:30`)
48. Verifikasi kolom Device Name baris DD-05 berisi `-` (hyphen tunggal)
49. Verifikasi kolom Brand baris DD-05 berisi `-` (hyphen tunggal)
50. Sembunyikan kembali kolom `Last Scanned In` lewat overlay Column Visibility (⋯), lalu tutup overlay

### TC-GS-TAG-244: Download hasil nol baris berisi hanya header

51. Ketik Search `ZZZ-NOTFOUND`, tekan Enter
52. Verifikasi `No results found` tampil
53. Verifikasi tombol Download aktif
54. Klik ikon Download, lalu klik `Download as CSV`
55. Verifikasi tidak ada toast
56. Verifikasi file terunduh
57. Verifikasi file CSV hanya memuat baris header kolom yang tampil
58. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber dipertahankan (239, 240, 241, 242, 244). Spec tidak menghapus data; state yang diubah (filter, visibilitas kolom) dipulihkan di dalam spec dan di hook `after`.
- Panjang spec: 58 langkah, di atas sekitar 35 langkah. Alasan dipertahankan: seluruh blok satu kelas (binary buffer: isi dan nama file export registri, prinsip 13f) pada satu dataset (Seed Registri A); tidak ada kegagalan server di spec ini (itu spec 079); setiap blok memakai unduhannya sendiri dan memulihkan state yang diubah (langkah 14 sampai 17, 29, 39, 50, 58) sehingga berdiri sendiri. Kemampuan menangkap dan membaca berkas dibutuhkan semua blok sehingga kegagalannya memengaruhi seluruh blok, tetapi kegagalan asersi isi satu blok tidak menutup blok lain. Pemisahan tidak dilakukan karena dataset, akun, dan harness sama.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 14 sampai 17 (mengosongkan filter dan kembali ke Tab All), langkah 29 (kembali ke Tab All), langkah 30, 35, 39 (menyembunyikan dan menampilkan kembali kolom, bagian dari langkah TC-GS-TAG-241), langkah 40 (menampilkan Last Scanned In, precondition TC-GS-TAG-242 butir d), langkah 42 (membaca berkas), langkah 50 (memulihkan visibilitas kolom), langkah 58 (mengosongkan Search).
- Absence toast (langkah 19, 23, 27, 32, 37, 55) diletakkan segera setelah pemicu unduhan dan sebelum asersi berkas; berkas terunduh (nama berkas atau langkah 56) menjadi anchor positif yang menyusul (bagian 8b butir 11).
- Asersi tambahan di luar Expected TC (S-03): langkah 33 (anchor positif bahwa header file pertama termuat sebelum absence `SKU` dan `Brand` pada langkah 34, bagian 8b butir 2); langkah 52 (empty state `No results found` sebagai anchor positif bahwa Search diproses sebelum asersi file hasil nol).
- Hitungan baris file (30, 24, 4) diturunkan dari Seed Registri A; baris data tidak termasuk header.
- Asersi nama file `All-TAGs.csv` (Tab All, CSV) berada di langkah 3 pada blok TC-GS-TAG-239 dan menjadi cakupan pasangan format dan tab Tab All untuk TC-GS-TAG-240.
- Temuan untuk QA:
  - TC-GS-TAG-239 langkah 2 menyetel `Source` = Official di Tab All lalu pindah ke Tab Paired tanpa menyebut apakah filter Tab All ikut terbawa; per TC-GS-TAG-218 filter independen per tab, sehingga Tab Paired tanpa filter dan hasilnya 4 baris. Spec mengikuti Expected (4 baris).
  - TC-GS-TAG-240 tidak menyebut keadaan filter saat unduhan; spec mengosongkan filter di langkah 15 sampai 17 supaya nama file dan tab yang diuji tidak bercampur dengan filter blok sebelumnya.
  - TC-GS-TAG-242 hanya menyebut "format General Settings" untuk Last Scanned; spec memakai format default `dd/MM/yy HH:mm` dan nilai `16/09/26 14:30` dari Seed Registri A. TC tidak menyebut nama sheet atau tipe sel XLSX.
  - TC-GS-TAG-244 tidak menyebut format unduhan; spec memakai CSV seperti Langkah TC.
  - Hitungan baris bergantung pada Seed Registri A utuh dan suite serial (Q-4).
