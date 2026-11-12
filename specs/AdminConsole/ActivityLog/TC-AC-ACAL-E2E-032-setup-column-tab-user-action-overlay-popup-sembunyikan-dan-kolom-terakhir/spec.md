---
id: TC-AC-ACAL-E2E-032-setup-column-tab-user-action-overlay-popup-sembunyikan-dan-kolom-terakhir
title: "Setup Column Tab User Action: Overlay, Popup, Sembunyikan, Cancel, dan Kolom Terakhir"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-104
  - TC-AC-ACAL-105
  - TC-AC-ACAL-106
  - TC-AC-ACAL-110
  - TC-AC-ACAL-111
coverage:
  web: automated
---

# Setup Column Tab User Action: Overlay, Popup, Sembunyikan, Cancel, dan Kolom Terakhir

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; `{namaCompany}` ditetapkan tim FE), password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Langkah login di `## Test Steps` (langkah 46) hanya untuk login ulang akun yang sama pada TC-AC-ACAL-106.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Activity Log (lihat suite.md).
- Data Pre-setup dan Data Dinamis: tidak ada seeding. Tabel Tab User Action cukup memuat entri User Action apa pun; spec hanya mengamati kolom dan kontrol Setup Column.
- Data uji TC-AC-ACAL-106 dan TC-AC-ACAL-111 (tujuh kolom yang di-uncheck satu per satu; kolom terakhir `Modified By` tidak di-uncheck):

  | No | Kolom |
  |---|---|
  | 1 | `Date` |
  | 2 | `Action` |
  | 3 | `Object` |
  | 4 | `Name` |
  | 5 | `Field` |
  | 6 | `Old Value` |
  | 7 | `New Value` |

- Urutan kolom default tab User Action: `Date | Action | Object | Name | Field | Old Value | New Value | Modified By`.
- Pilihan spec (TC tidak menyebutkan kolomnya): kolom yang di-uncheck pada TC-AC-ACAL-110 adalah `Name`, dan kolom yang digeser adalah `Date` ke posisi terakhir.
- Kemampuan teknis (disediakan tim FE): drag and drop baris kolom di Popup Setup Column; hover checkbox dan icon Pin untuk membaca tooltip; muat ulang halaman (F5) pada konteks browser yang sama supaya preferensi kolom di browser tetap ada; logout dan login ulang akun yang sama; menghapus preferensi kolom tab User Action di browser.
- State global yang diubah: preferensi kolom tab User Action (disimpan di browser, bukan lewat API). Pemulihan: langkah 50 sampai 52 mengembalikan kolom `Field` dan hook `after` menghapus preferensi kolom di browser (didaftarkan di `suite.md`; bukan `[Reset to Default]`, yang diuji di spec lain). Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

1. Buka Admin Console > Activity Log > User Action

### TC-AC-ACAL-104: Screening Overlay Column Visibility

2. Klik header `⋯`
3. Verifikasi Overlay Column Visibility memuat daftar kolom berurutan `Date | Action | Object | Name | Field | Old Value | New Value | Modified By`
4. Verifikasi setiap kolom pada overlay memiliki checkbox checked dan enabled
5. Verifikasi setiap kolom pada overlay memiliki drag handle
6. Verifikasi item `Setup Column...` tampil di bagian bawah overlay
7. Tutup Overlay Column Visibility

### TC-AC-ACAL-105: Screening Popup Setup Column

8. Klik header `⋯`, klik `Setup Column...`
9. Verifikasi header Popup Setup Column memuat title `Setup Column`
10. Verifikasi deskripsi header `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
11. Verifikasi tombol `✕` tampil di header
12. Verifikasi body memuat daftar kolom berurutan `Date | Action | Object | Name | Field | Old Value | New Value | Modified By`
13. Verifikasi setiap kolom pada body memiliki checkbox checked
14. Verifikasi setiap kolom pada body memiliki drag handle
15. Verifikasi setiap kolom pada body memiliki icon Pin
16. Verifikasi preview tabel tampil
17. Verifikasi footer memuat `[Reset to Default]` dan `[Save]`
18. Verifikasi footer tidak memuat `[Cancel]`

### TC-AC-ACAL-110: Tutup Popup Setup Column membuang perubahan

19. Klik `✕` untuk menutup Popup Setup Column
20. Klik header `⋯`, klik `Setup Column...`
21. Uncheck kolom `Name` di popup, klik `✕`
22. Verifikasi Popup Setup Column tertutup
23. Verifikasi tabel tetap berada pada konfigurasi tersimpan terakhir (kolom `Name` tetap tampil)
24. Klik header `⋯`, klik `Setup Column...`
25. Drag kolom `Date` ke posisi terakhir, tekan `Esc`
26. Verifikasi Popup Setup Column tertutup
27. Verifikasi urutan kolom tabel tidak berubah (kolom `Date` tetap pertama)

### TC-AC-ACAL-111: Guard satu kolom terakhir tidak dapat di-uncheck

28. Klik header `⋯`
29. Untuk setiap baris tabel Data uji TC-AC-ACAL-106 dan TC-AC-ACAL-111 (langkah 29): hilangkan centang kolom di Overlay Column Visibility
30. Arahkan kursor ke checkbox kolom tersisa `Modified By`
31. Verifikasi checkbox kolom tersisa tetap tampil tetapi disabled
32. Verifikasi tooltip `At least one column must remain visible.`
33. Untuk setiap baris tabel Data uji TC-AC-ACAL-106 dan TC-AC-ACAL-111 (langkah 33): ceklis kembali kolom di Overlay Column Visibility
34. Tutup Overlay Column Visibility

### TC-AC-ACAL-106: Unceklis dan ceklis kolom di Popup Setup Column

35. Klik header `⋯`, klik `Setup Column...`
36. Untuk setiap baris tabel Data uji TC-AC-ACAL-106 dan TC-AC-ACAL-111 (langkah 36 sampai 37): uncheck kolom di popup
37. Verifikasi preview tabel menghilangkan kolom yang di-uncheck
38. Untuk setiap baris tabel Data uji TC-AC-ACAL-106 dan TC-AC-ACAL-111 (langkah 38 sampai 39): ceklis kembali kolom di popup
39. Verifikasi preview tabel menampilkan kembali kolom yang diceklis
40. Uncheck kolom `Field` di popup, klik `[Save]`
41. Verifikasi tabel tanpa kolom `Field`
42. Muat ulang halaman (F5)
43. Verifikasi kolom `Date` dan `Action` tampil pada tabel
44. Verifikasi kolom `Field` tetap tersembunyi
45. Logout dari akun aktor
46. Login kembali dengan akun aktor yang sama (password `Spectra.env.AC_TC_PASSWORD`)
47. Buka Admin Console > Activity Log > User Action
48. Verifikasi kolom `Date` dan `Action` tampil pada tabel
49. Verifikasi kolom `Field` tetap tersembunyi setelah logout-login

### Pemulihan state

50. Klik header `⋯`, klik `Setup Column...`
51. Ceklis kolom `Field`
52. Klik `[Save]`

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (bagian 4b, Tab User Action). Seluruh TC sumber spec ini dikerjakan di sini.
- Urutan TC di dalam spec: TC-AC-ACAL-104, 105, 110, 111, lalu 106. TC-AC-ACAL-106 menyimpan konfigurasi kolom dan memuat login ulang sehingga ditaruh paling akhir; TC-AC-ACAL-110 dan 111 membutuhkan konfigurasi bawaan.
- Tombol tutup Popup Setup Column ditulis `✕` mengikuti TC-AC-ACAL-105 dan 110 (langkah 11, 19, 21).
- Langkah penghubung (aksi tanpa `Verifikasi`): penutupan overlay dan popup (langkah 7 dan 19), pemulihan kolom di overlay (langkah 33), dan pemulihan konfigurasi kolom `Field` (langkah 50 sampai 52, `[Save]` Setup Column adalah aksi sisi klien sehingga tanpa langkah "Tunggu aksi selesai"). Langkah 43 dan 48 adalah anchor positif (kolom lain tampil) untuk asersi absence kolom `Field` sesudah muat ulang dan login ulang.
- Langkah 29, 33, 36 sampai 37, dan 38 sampai 39 berulang untuk setiap baris tabel Data uji (tujuh iterasi, bagian 8b butir 7).
- Spec memiliki 52 langkah nominal dan 88 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Setup Column Tab User Action pada akun yang sama tanpa seeding), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan ekspansi berasal dari perulangan per kolom data tanpa langkah bersyarat.
- Temuan untuk QA:
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD`, yang sudah terdaftar di `.env.example` dan `spectra.config.ts`.
  - TC-AC-ACAL-110 tidak menyebut kolom yang di-uncheck dan di-drag; spec memilih `Name` dan `Date` (pilihan spec).
  - TC-AC-ACAL-111 tidak menyebut kolom yang tersisa; spec menyisakan kolom terakhir `Modified By`, konsisten dengan TC-AC-ACAL-106 ("kecuali satu kolom terakhir").
  - TC-AC-ACAL-106 Expected a menyebut "tiap kolom yang di-uncheck" tanpa menyebut kolom yang tersisa pada langkah terakhir; kolom `Modified By` tetap tercentang.
  - TC-AC-ACAL-111 langkah 1 meng-uncheck kolom di Overlay Column Visibility, tetapi TC tidak menyatakan apakah perubahan overlay tersimpan di browser; spec memulihkannya dengan ceklis ulang (langkah 33).
