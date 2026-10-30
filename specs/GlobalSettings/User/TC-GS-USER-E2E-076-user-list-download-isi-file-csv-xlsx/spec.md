---
id: TC-GS-USER-E2E-076-user-list-download-isi-file-csv-xlsx
title: "User List: Download CSV/XLSX (Menu, Isi Berkas Seluruh Baris, Cakupan Search, Kolom Hidden, Nilai Kosong, Access/Active, dan Nilai Phone)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-453
  - TC-GS-USER-454
  - TC-GS-USER-455
  - TC-GS-USER-456
  - TC-GS-USER-457
  - TC-GS-USER-461
  - TC-GS-USER-1079
coverage:
  web: automated
---

# User List: Download CSV/XLSX (Menu, Isi Berkas Seluruh Baris, Cakupan Search, Kolom Hidden, Nilai Kosong, Access/Active, dan Nilai Phone)

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Pre-setup.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 1 dan 10-22 serta Custom Field aktif No. 24, hanya dibaca): Default User `Hendra Gunawan` (Active, Access `Fixed Asset`, `Global Settings`, `Supply Asset`), `Dewi Lestari`, dan user Pre-setup lain di tabel Login User (sedikitnya 20 baris, sehingga dengan SA dan SB lebih dari 10 baris dan halaman 1 tidak memuat SA dan SB).
- Data Dinamis, di-seed lewat API di hook `before`. Kemampuan seeding user lewat API disediakan tim FE/BE (endpoint tidak disebut di TC dan PRD). Field wajib yang bukan objek uji: Access sesuai tabel, Division sesuai tabel, dan Custom Field `Emergency Phone` (Required, Tabel Pre-setup No. 24) dengan Country Code `🇮🇩 +62` dan Number `81234567890`.
  - SA: First Name `Zulkifli`, Last Name `Hakim {runId}-076`, Email `zulkiflihakim+{runId}-076@qwertysystem.net`, Division `Finance`, Access `Fixed Asset`, tanpa Position dan tanpa Employee ID (nilai kosong ditulis `-`), Emergency Phone `🇮🇩 +62` `81234567890`. Name diawali `Z` sehingga urutan default Name A-Z menaruhnya di halaman terakhir.
  - SB: First Name `Yolanda`, Last Name `Putri {runId}-076`, Email `yolandaputri+{runId}-076@qwertysystem.net`, Position `Supervisor`, Division `Logistics`, Access `Fixed Asset`, Employee ID `EMP-0761-{runId}`.
  - Seeding minimal (S-11): SA untuk nilai kosong, nilai Phone, dan baris yang tidak tampil di halaman 1; SB sebagai baris pembanding hasil search (TC-GS-USER-455) dan baris di luar halaman 1.
  - Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus SA dan SB lewat API; hapus berkas unduhan.
- Kemampuan teknis (kelas binary buffer, prinsip 13f konvensi): menangkap berkas unduhan browser (event download) ke direktori bersih per unduhan supaya nama berkas yang sama (`User.csv`) tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV dan XLSX (nama kolom, jumlah baris, nilai sel).
- State yang diubah dan dipulihkan: kolom `Division` di-hide lalu dicentang kembali di TC-GS-USER-456; kolom `Emergency Phone` dicentang lewat Setup Column (langkah 44) dan dipulihkan lewat `[Reset to Default]` dan `[Save]` (langkah 55 sampai 58); Search ditutup di langkah 26. Hook `after` sebagai cadangan mengembalikan konfigurasi kolom ke default (penghapusan preferensi kolom User List di browser; mekanisme disediakan tim FE/BE).
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List (sub-tab Login User).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-USER-453: Download CSV seluruh data tanpa toast sukses

1. Verifikasi halaman 1 tabel (10 baris per halaman) tidak memuat baris `Zulkifli Hakim {runId}-076` dan `Yolanda Putri {runId}-076`
2. Klik icon Download
3. Verifikasi Overlay menampilkan opsi `Download as CSV` dan `Download as XLSX`
4. Klik `Download as CSV`
5. Verifikasi file `User.csv` terunduh
6. Buka isi file `User.csv` yang diunduh
7. Verifikasi file memuat baris `Zulkifli Hakim {runId}-076` dan `Yolanda Putri {runId}-076` yang tidak tampil di halaman 1 tabel (tidak dibatasi halaman)
8. Verifikasi jumlah baris data di file lebih dari 10
9. Verifikasi tidak ada toast sukses

### TC-GS-USER-457: Nilai kosong ditulis `-` di file export

10. Buka baris `Zulkifli Hakim {runId}-076` di isi file `User.csv` yang diunduh pada langkah 4
11. Verifikasi sel kosong ditulis `-`: kolom Position dan kolom Employee ID baris `Zulkifli Hakim {runId}-076` bernilai `-`

### TC-GS-USER-461: Export Access multi-badge dipisah koma dan Active ditulis teks

12. Buka baris Default User (`Hendra Gunawan`) di isi file `User.csv` yang diunduh pada langkah 4
13. Verifikasi kolom Access: `Fixed Asset, Global Settings, Supply Asset`
14. Verifikasi kolom Active: `Active`
15. Verifikasi foto avatar tidak ikut di file: header file tidak memuat kolom foto atau avatar

### TC-GS-USER-454: Download XLSX

16. Klik icon Download
17. Klik `Download as XLSX`
18. Verifikasi file `User.xlsx` terunduh

### TC-GS-USER-455: Download mengikuti Search/Filter aktif

19. Klik icon Search, ketik `Zulkifli Hakim`, tekan Enter
20. Verifikasi baris `Zulkifli Hakim {runId}-076` tampil di tabel hasil search
21. Klik icon Download
22. Klik `Download as CSV`
23. Buka isi file `User.csv` yang diunduh
24. Verifikasi file memuat baris `Zulkifli Hakim {runId}-076` (hasil search)
25. Verifikasi file hanya berisi baris hasil search: baris `Yolanda Putri {runId}-076` dan baris `Dewi Lestari` tidak ada di file
26. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### TC-GS-USER-456: Download mengecualikan kolom hidden lalu menyertakan lagi setelah unhide

27. Klik header kolom Column Visibility (⋯)
28. Hilangkan centang `Division`
29. Tekan Esc untuk menutup Overlay Column Visibility
30. Verifikasi kolom `Division` tidak tampil di tabel
31. Klik icon Download
32. Klik `Download as CSV`
33. Buka isi file `User.csv` yang diunduh
34. Verifikasi file memuat kolom `Name` dan `Email`
35. Verifikasi file pertama tanpa kolom `Division`
36. Verifikasi tidak ada toast peringatan
37. Klik header kolom Column Visibility (⋯)
38. Centang `Division`
39. Tekan Esc untuk menutup Overlay Column Visibility
40. Klik icon Download
41. Klik `Download as CSV`
42. Buka isi file `User.csv` yang diunduh
43. Verifikasi file kedua memuat kolom `Division`

### TC-GS-USER-1079: Download CSV memuat nilai Phone sebagai [+CountryCode] [Number]

44. Klik header kolom Column Visibility (⋯)
45. Klik `Setup Column...`
46. Centang `Emergency Phone`
47. Klik `[Save]`
48. Klik icon Download
49. Klik `Download as CSV`
50. Verifikasi file `User.csv` terunduh
51. Buka isi file `User.csv` yang diunduh
52. Verifikasi file memuat kolom `Emergency Phone`
53. Verifikasi baris `Zulkifli Hakim {runId}-076`: sel Emergency Phone `+62 81234567890` (satu spasi)
54. Verifikasi sel Emergency Phone baris `Zulkifli Hakim {runId}-076` tidak tertulis tanpa spasi (`+6281234567890`)

### Pemulihan state

55. Klik header kolom Column Visibility (⋯)
56. Klik `Setup Column...`
57. Klik `[Reset to Default]`
58. Klik `[Save]`

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Kelas harness binary buffer (prinsip 13f): isi berkas CSV dan XLSX dipisah dari kegagalan ekspor (spec 069) dan dari volume lebih dari 5.000 baris (spec 077).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 453, 457, 461 (berkas `User.csv` seluruh data, semua kolom default), 454, 455, 456, lalu 1079 di akhir. Urutan di `tc-user.md`: 453 sampai 457, 461, 1079. TC-GS-USER-457 dan 461 membaca berkas `User.csv` hasil unduhan TC-GS-USER-453 (langkah 4) tanpa unduh ulang: state tabel ketiganya identik (tanpa Search dan Filter, semua kolom default, seluruh baris), sehingga langkah "Download CSV" TC-GS-USER-457 dan 461 dipenuhi unduhan itu. TC-GS-USER-1079 ditaruh paling akhir karena menampilkan kolom lewat Setup Column.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6 dan semua langkah `Buka isi file` (membaca isi berkas unduhan; blok baca berpola), `Klik icon panah (←)` (langkah 26), pencentangan kembali `Division`, penutupan Overlay Column Visibility lewat Esc, serta langkah 55 sampai 58 (memulihkan konfigurasi kolom).
- Asersi tambahan (S-03): TC-GS-USER-453 memuat `Verifikasi` bahwa halaman 1 tidak memuat SA dan SB dan `Verifikasi` jumlah baris di file lebih dari 10, sebagai anchor bahwa berkas memuat baris di luar halaman tampil; TC-GS-USER-455 memuat `Verifikasi` baris SA tampil di tabel hasil search dan di file, sebagai anchor ketiadaan baris lain; TC-GS-USER-456 memuat `Verifikasi` kolom `Name` dan `Email` ada di file pertama, sebagai anchor ketiadaan kolom `Division`.
- Pembagian TC lintas spec: TC-GS-USER-460 dan 1055 sampai 1060 (Download gagal, toast error) diverifikasi di spec 069; TC-GS-USER-462 (lebih dari 5.000 baris) di spec 077; Search di spec 071; Filter Panel di spec 072; Setup Column di spec 075.
- Spec melewati sekitar 35 langkah (58 langkah) karena tujuh TC Download memakai dataset dan layar yang sama dan satu kelas harness (binary buffer). Blok 453, 454, 455, 456, dan 1079 mengunduh berkas sendiri; blok 457 dan 461 membaca berkas hasil unduhan blok 453. Langkah membaca isi berkas termasuk blok baca berpola.
- Temuan untuk QA:
  - TC-GS-USER-453: TC menyebut berkas berisi "semua baris" tanpa menyebut jumlah; spec mengasersi berkas memuat baris di luar halaman 1 (SA dan SB) dan jumlah baris lebih dari 10, karena tabel Login User memuat sedikitnya 20 baris Pre-setup.
  - TC-GS-USER-454: TC hanya menyebut berkas `User.xlsx` terunduh; isi berkas XLSX tidak diasersi.
  - TC-GS-USER-455 dan 456: TC tidak menyebut keyword dan kolom yang di-hide; spec memakai `Zulkifli Hakim` (Search) dan `Division` (kolom hidden).
  - TC-GS-USER-457: TC tidak menyebut baris yang berisi sel kosong; spec memakai SA (tanpa Position dan Employee ID).
  - TC-GS-USER-461: kolom Access Default User `Fixed Asset, Global Settings, Supply Asset` bergantung pada subscription client dan akses Default User (Tabel Pre-setup No. 1 dan 26); TC tidak menyebut kondisi itu.
  - TC-GS-USER-453, 454, 455, 456, 457, 461, 1079: cara menangkap berkas unduhan dan membaca isinya tidak disebut di TC; kemampuan itu disediakan tim FE (Prerequisites).
  - TC-GS-USER-1079: Pre-setup No. 12 menyebut Emergency Phone `Dewi Lestari` kosong, sedangkan TC menyebut tersimpan `+62 81234567890`. Spec memakai SA dengan nilai itu.
  - TC-GS-USER-1079: TC menyebut menu `[Setup Column]` dan header `Actions (⋯)`, sedangkan TC-GS-USER-441 dan 442 menyebut `Setup Column...` dan `Column Visibility (⋯)`. Spec memakai `Setup Column...` dan `Column Visibility (⋯)`.
  - TC-GS-USER-453: Expected TC menulis opsi `Download as CSV` / `Download as XLSX`, berbeda dari tabel Division (`Download CSV`); spec mengikuti TC User.
