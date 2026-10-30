---
id: TC-GS-FILEMGR-E2E-052-download-tabel-utama-isi-file-csv-xlsx
title: "Download Tabel Utama dan Export Lintas Surface: Isi File CSV dan XLSX, Nama File, dan Kolom Tersembunyi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-190
  - TC-GS-FILEMGR-191
  - TC-GS-FILEMGR-192
  - TC-GS-FILEMGR-193
  - TC-GS-FILEMGR-194
  - TC-GS-FILEMGR-195
  - TC-GS-FILEMGR-198
  - TC-GS-FILEMGR-199
coverage:
  web: automated
---

# Download Tabel Utama dan Export Lintas Surface: Isi File CSV dan XLSX, Nama File, dan Kolom Tersembunyi

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sinta Maharani (Tabel A1 TC) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Tabel A2 (33 file aktif, ukuran halaman 10), Tabel A3 (16 baris Recycle Bin, retensi 30 hari, Deleted Date relatif terhadap waktu uji), dan Tabel A4 (14 entri Changelog). Dataset disiapkan lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme dan endpoint seeding tidak didefinisikan di TC, lihat Temuan untuk QA). Nama file literal sesuai tabel karena isi file export dan hasil Search bergantung pada nama (pengecualian setara S-12: seeding idempotent, suite serial). Spec hanya membaca data; tidak ada aksi tulis ke data dan tidak ada data dinamis.
- General Settings: Date Format `dd/MM/yy` dan Time Format `HH:mm` (default) saat spec dimulai; hook `before` memastikan nilai itu. Langkah 58 mengubahnya sementara ke `M/d/yy` dan `hh:mm a`; langkah 62 memulihkan, dan hook `after` memulihkan sebagai cadangan. Halaman General Settings milik modul lain; selektornya disediakan tim FE.
- Tabel "Surface yang diuji" (parameter langkah 26 sampai 40):

| Surface | Pembuka | Nama file CSV | Nama file XLSX |
|---|---|---|---|
| Tabel utama | tanpa aksi (layar File Manager) | `File-Manager-List.csv` | `File-Manager-List.xlsx` |
| Recycle Bin | klik tombol Recycle Bin di toolbar | `File-Manager-Recycle-Bin.csv` | `File-Manager-Recycle-Bin.xlsx` |
| Changelog | klik ikon Changelog di toolbar | `Changelog-File-Manager.csv` | `Changelog-File-Manager.xlsx` |

- Suite serial (`parallel: false`): dataset (33 file aktif, 16 baris Recycle Bin, 14 entri Changelog) dan format tanggal General Settings adalah state global.
- Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > File Manager.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): format tanggal General Settings, konfigurasi kolom tabel utama (semua kolom tampil), dan berkas unduhan dihapus.
- Kemampuan teknis (kelas binary buffer, prinsip 13f): menangkap berkas unduhan browser (event download) ke direktori bersih per unduhan supaya nama berkas yang sama tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV (BOM, pemisah, header, jumlah baris) dan XLSX (nama sheet, nilai dan tipe sel).

## Test Steps

### TC-GS-FILEMGR-190: Download tabel utama tanpa Search atau Filter mengekspor seluruh baris

1. Klik ikon Download di toolbar tabel utama, lalu klik `Download as CSV`
2. Verifikasi tidak ada toast sukses
3. Verifikasi file terunduh
4. Verifikasi file CSV memuat 33 baris data (seluruh dataset, bukan hanya halaman aktif)
5. Verifikasi header file CSV memuat kolom yang tampil: `File Name`, `File Format`, `User Name`, `Size`, `Uploaded By`, `Upload Date`

### TC-GS-FILEMGR-191: Download tabel utama saat Search aktif hanya mengekspor baris yang cocok

6. Ketik Search `staff-photo`, tekan Enter
7. Klik ikon Download, lalu klik `Download as CSV`
8. Verifikasi file CSV memuat 25 baris data (`staff-photo-01.jpg` s.d. `staff-photo-25.jpg`)
9. Verifikasi file CSV tidak memuat baris `budi-avatar.jpg` atau file lain di luar hasil Search
10. Klik ikon panah (←) pada kotak Search

### TC-GS-FILEMGR-192: Kolom yang disembunyikan tidak ikut diekspor dan ikut lagi setelah ditampilkan kembali

11. Sembunyikan kolom `Uploaded By` lewat overlay Column Visibility (⋯)
12. Klik ikon Download, lalu klik `Download as CSV`
13. Verifikasi tidak ada toast peringatan
14. Verifikasi header file CSV pertama tidak memuat `Uploaded By`
15. Tampilkan kembali kolom `Uploaded By` lewat overlay Column Visibility (⋯)
16. Klik ikon Download, lalu klik `Download as CSV`
17. Verifikasi header file CSV kedua memuat `Uploaded By`

### TC-GS-FILEMGR-195: Download dengan hasil Search nol baris tetap menghasilkan file berisi header saja

18. Ketik Search `zzzxyz-tidak-ada`, tekan Enter
19. Verifikasi tombol Download tetap aktif
20. Klik ikon Download, lalu klik `Download as CSV`
21. Verifikasi tidak ada toast
22. Verifikasi file terunduh
23. Verifikasi file CSV hanya memuat baris header kolom yang tampil
24. Klik ikon panah (←) pada kotak Search

### TC-GS-FILEMGR-193, 194: Ekstensi, encoding, nama file, dan sheet export CSV dan XLSX pada tiga surface

25. Untuk setiap surface pada tabel Prerequisites, lakukan langkah 26 sampai 40
26. Buka surface sesuai kolom Pembuka
27. Klik ikon Download di toolbar surface itu
28. Verifikasi overlay Download memuat dua opsi `Download as CSV` dan `Download as XLSX`
29. Klik `Download as CSV`
30. Verifikasi tidak ada toast sukses
31. Verifikasi file berekstensi `.csv`
32. Verifikasi file CSV berpemisah koma
33. Verifikasi file CSV ber-encoding UTF-8 dengan BOM
34. Verifikasi nama file CSV sesuai kolom "Nama file CSV", tanpa timestamp
35. Klik ikon Download, lalu klik `Download as XLSX`
36. Verifikasi tidak ada toast sukses
37. Verifikasi file berekstensi `.xlsx`
38. Verifikasi nama file XLSX sesuai kolom "Nama file XLSX", tanpa timestamp
39. Verifikasi file XLSX memuat satu sheet bernama `Sheet1`
40. Tutup modal surface bila surface berupa modal

### TC-GS-FILEMGR-199: Nama dasar file export tabel utama dan Recycle Bin tanpa timestamp

41. Klik ikon Download di toolbar tabel utama, lalu klik `Download as CSV`
42. Klik ikon Download, lalu klik `Download as CSV` sekali lagi
43. Verifikasi kedua unduhan bernama dasar `File-Manager-List` tanpa tanggal atau jam
44. Klik tombol Recycle Bin di toolbar
45. Klik ikon Download, lalu klik `Download as CSV`
46. Klik ikon Download, lalu klik `Download as CSV` sekali lagi
47. Verifikasi kedua unduhan bernama dasar `File-Manager-Recycle-Bin` tanpa tanggal atau jam
48. Tutup modal Recycle Bin

### TC-GS-FILEMGR-198: Isi sel file export XLSX untuk Size, tanggal, dan Auto-Purge In

49. Klik ikon Download di toolbar tabel utama, lalu klik `Download as XLSX`
50. Verifikasi sel Size baris `budi-avatar.jpg` bernilai angka `2516582` bertipe number (bukan teks `2.4 MB`)
51. Verifikasi sel Upload Date baris `budi-avatar.jpg` bernilai `02/09/26 14:30`
52. Klik tombol Recycle Bin di toolbar
53. Klik ikon Download, lalu klik `Download as XLSX`
54. Verifikasi sel Size baris `old-avatar.png` bernilai `2097152` bertipe number
55. Verifikasi sel Deleted Date baris `old-avatar.png` mengikuti pola `dd/MM/yy HH:mm`
56. Verifikasi sel Auto-Purge In baris `old-avatar.png` bernilai `29` bertipe number
57. Tutup modal Recycle Bin
58. Ubah General Settings ke Date Format `M/d/yy` dan Time Format `hh:mm a`
59. Buka layar Global Settings > File Manager
60. Klik ikon Download di toolbar tabel utama, lalu klik `Download as XLSX`
61. Verifikasi sel Upload Date baris `budi-avatar.jpg` bernilai `9/2/26 02:30 PM`
62. Ubah General Settings kembali ke Date Format `dd/MM/yy` dan Time Format `HH:mm`

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: 190, 191, 192, 195, 193 dan 194 (digabung), 199, 198. TC yang mengubah state global (TC-GS-FILEMGR-198, format tanggal General Settings) di akhir dan dipulihkan pada langkah 62.
- Panjang spec: 62 langkah tertulis (sekitar 92 langkah setelah ekspansi tiga surface pada langkah 26 sampai 40), di atas sekitar 35 langkah. Alasan dipertahankan: seluruh blok satu kelas (binary buffer: isi dan nama file export, prinsip 13f), tidak ada kegagalan server di spec ini (itu spec `TC-GS-FILEMGR-E2E-016-resilience-download-gagal`), setiap blok memakai unduhan sendiri dan berdiri sendiri, dan langkah berulang pada tiga surface memakai parameter di tabel Prerequisites tanpa langkah bersyarat (bagian 8b butir 7). Kemampuan teknis menangkap dan membaca berkas dibutuhkan semua blok sehingga kegagalannya memengaruhi seluruh blok, tetapi kegagalan asersi isi satu blok tidak menutup blok lain.
- TC-GS-FILEMGR-193 dan 194 dijalankan per surface dalam satu iterasi (CSV lalu XLSX) agar tiap surface hanya dibuka sekali; Expected TC-GS-FILEMGR-193 butir a (dua opsi Download) diasersi sekali per iterasi di langkah 28.
- Absence toast (langkah 2, 13, 21, 30, 36) diletakkan segera setelah pemicu unduhan dan sebelum asersi berkas; berkas terunduh (langkah 3, 22, 31, 37) menjadi anchor positif yang menyusul.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 10 dan 24 (mengosongkan Search), langkah 15 (menampilkan kembali kolom), langkah 40, 48, dan 57 (menutup modal), langkah 59 (membuka layar File Manager setelah mengubah General Settings), langkah 62 (memulihkan format tanggal).
- Nama berkas yang sama pada TC-GS-FILEMGR-199 (dua unduhan berturut-turut) dan antar langkah dibaca dari direktori bersih per unduhan (kemampuan teknis di Prerequisites).
- Temuan untuk QA:
  - Skenario TC-GS-FILEMGR-191 menyebut "Search dan Filter aktif", tetapi Langkah Uji hanya memuat Search; spec mengikuti langkah TC (Search saja). Perlu konfirmasi apakah Filter harus ikut diterapkan.
  - Mekanisme dan endpoint seeding Tabel A2, A3, dan A4 tidak didefinisikan di TC (Q-4); hitungan baris dan isi file mengasumsikan dataset di-seed ulang per spec dan suite serial (Q-7).
  - Nilai sel `29` Auto-Purge In (langkah 56) dan Deleted Date relatif adalah nilai turunan dari retensi 30 hari dan waktu uji (Q-14); `old-avatar.png` (sekarang − 1 hari) stabil terhadap job auto-purge.
  - Langkah 58 dan 62 memakai halaman General Settings (modul lain) yang langkahnya tidak didefinisikan di TC ini (Q-9); selektor disediakan tim FE.
