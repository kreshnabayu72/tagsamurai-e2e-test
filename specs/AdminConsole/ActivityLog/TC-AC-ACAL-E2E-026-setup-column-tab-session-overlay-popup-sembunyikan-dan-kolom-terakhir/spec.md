---
id: TC-AC-ACAL-E2E-026-setup-column-tab-session-overlay-popup-sembunyikan-dan-kolom-terakhir
title: "Setup Column Tab Session: Overlay, Popup, Sembunyikan, Cancel, dan Kolom Terakhir"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-80
  - TC-AC-ACAL-81
  - TC-AC-ACAL-82
  - TC-AC-ACAL-86
  - TC-AC-ACAL-87
coverage:
  web: automated
---

# Setup Column Tab Session: Overlay, Popup, Sembunyikan, Cancel, dan Kolom Terakhir

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; `{namaCompany}` ditetapkan tim FE), password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Langkah login di `## Test Steps` (langkah 45) hanya untuk login ulang akun yang sama pada TC-AC-ACAL-82.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Activity Log (lihat suite.md).
- Data Pre-setup dan Data Dinamis: tidak ada seeding. Tabel Tab Session cukup memuat entri sesi akun aktor dan entri lain; spec hanya mengamati kolom dan kontrol Setup Column.
- Data uji TC-AC-ACAL-82 dan TC-AC-ACAL-87 (sembilan kolom yang di-uncheck satu per satu; kolom terakhir `Device / Browser` tidak di-uncheck):

  | No | Kolom |
  |---|---|
  | 1 | `Date` |
  | 2 | `User` |
  | 3 | `Employee ID` |
  | 4 | `Position` |
  | 5 | `Division` |
  | 6 | `Activity` |
  | 7 | `Status` |
  | 8 | `Note` |
  | 9 | `IP Address` |

- Urutan kolom default tab Session: `Date | User | Employee ID | Position | Division | Activity | Status | Note | IP Address | Device / Browser`.
- Pilihan spec (TC tidak menyebutkan kolomnya): kolom yang di-uncheck pada TC-AC-ACAL-86 adalah `Note`, dan kolom yang digeser adalah `Date` ke posisi terakhir.
- Kemampuan teknis (disediakan tim FE): drag and drop baris kolom di Popup Setup Column; hover checkbox dan icon Pin untuk membaca tooltip; muat ulang halaman (F5) pada konteks browser yang sama supaya preferensi kolom di browser tetap ada; logout dan login ulang akun yang sama; menghapus preferensi kolom tab Session di browser.
- State global yang diubah: preferensi kolom tab Session (disimpan di browser, bukan lewat API). Pemulihan: langkah 49 sampai 51 mengembalikan kolom `Note` dan hook `after` menghapus preferensi kolom di browser (didaftarkan di `suite.md`; bukan `[Reset to Default]`, yang diuji di spec lain). Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-AC-ACAL-80: Screening Overlay Column Visibility

1. Klik header `⋯`
2. Verifikasi Overlay Column Visibility memuat daftar kolom berurutan `Date | User | Employee ID | Position | Division | Activity | Status | Note | IP Address | Device / Browser`
3. Verifikasi setiap kolom pada overlay memiliki checkbox checked dan enabled
4. Verifikasi setiap kolom pada overlay memiliki drag handle
5. Verifikasi item `Setup Column...` tampil di bagian bawah overlay
6. Tutup Overlay Column Visibility

### TC-AC-ACAL-81: Screening Popup Setup Column

7. Klik header `⋯`, klik `Setup Column...`
8. Verifikasi header Popup Setup Column memuat title `Setup Column`
9. Verifikasi deskripsi header `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
10. Verifikasi tombol `✕` tampil di header
11. Verifikasi body memuat daftar kolom berurutan `Date | User | Employee ID | Position | Division | Activity | Status | Note | IP Address | Device / Browser`
12. Verifikasi setiap kolom pada body memiliki checkbox checked
13. Verifikasi setiap kolom pada body memiliki drag handle
14. Verifikasi setiap kolom pada body memiliki icon Pin
15. Verifikasi preview tabel tampil
16. Verifikasi footer memuat `[Reset to Default]` dan `[Save]`
17. Verifikasi footer tidak memuat `[Cancel]`

### TC-AC-ACAL-86: Tutup Popup Setup Column membuang perubahan

18. Klik `✕` untuk menutup Popup Setup Column
19. Klik header `⋯`, klik `Setup Column...`
20. Uncheck kolom `Note` di popup, klik `✕`
21. Verifikasi Popup Setup Column tertutup
22. Verifikasi tabel tetap berada pada konfigurasi tersimpan terakhir (kolom `Note` tetap tampil)
23. Klik header `⋯`, klik `Setup Column...`
24. Drag kolom `Date` ke posisi terakhir, tekan `Esc`
25. Verifikasi Popup Setup Column tertutup
26. Verifikasi urutan kolom tabel tidak berubah (kolom `Date` tetap pertama)

### TC-AC-ACAL-87: Guard satu kolom terakhir tidak dapat di-uncheck

27. Klik header `⋯`
28. Untuk setiap baris tabel Data uji TC-AC-ACAL-82 dan TC-AC-ACAL-87 (langkah 28): hilangkan centang kolom di Overlay Column Visibility
29. Arahkan kursor ke checkbox kolom tersisa `Device / Browser`
30. Verifikasi checkbox kolom tersisa tetap tampil tetapi disabled
31. Verifikasi tooltip `At least one column must remain visible.`
32. Untuk setiap baris tabel Data uji TC-AC-ACAL-82 dan TC-AC-ACAL-87 (langkah 32): ceklis kembali kolom di Overlay Column Visibility
33. Tutup Overlay Column Visibility

### TC-AC-ACAL-82: Unceklis dan ceklis kolom di Popup Setup Column

34. Klik header `⋯`, klik `Setup Column...`
35. Untuk setiap baris tabel Data uji TC-AC-ACAL-82 dan TC-AC-ACAL-87 (langkah 35 sampai 36): uncheck kolom di popup
36. Verifikasi preview tabel menghilangkan kolom yang di-uncheck
37. Untuk setiap baris tabel Data uji TC-AC-ACAL-82 dan TC-AC-ACAL-87 (langkah 37 sampai 38): ceklis kembali kolom di popup
38. Verifikasi preview tabel menampilkan kembali kolom yang diceklis
39. Uncheck kolom `Note` di popup, klik `[Save]`
40. Verifikasi tabel tanpa kolom `Note`
41. Muat ulang halaman (F5)
42. Verifikasi kolom `Date` dan `User` tampil pada tabel
43. Verifikasi kolom `Note` tetap tersembunyi
44. Logout dari akun aktor
45. Login kembali dengan akun aktor yang sama (password `Spectra.env.AC_TC_PASSWORD`)
46. Buka Admin Console > Activity Log > Session
47. Verifikasi kolom `Date` dan `User` tampil pada tabel
48. Verifikasi kolom `Note` tetap tersembunyi setelah logout-login

### Pemulihan state

49. Klik header `⋯`, klik `Setup Column...`
50. Ceklis kolom `Note`
51. Klik `[Save]`

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (bagian 4a, Tab Session). Seluruh TC sumber spec ini dikerjakan di sini.
- Urutan TC di dalam spec: TC-AC-ACAL-80, 81, 86, 87, lalu 82. TC-AC-ACAL-82 menyimpan konfigurasi kolom dan memuat login ulang sehingga ditaruh paling akhir; TC-AC-ACAL-86 dan 87 membutuhkan konfigurasi bawaan.
- Langkah penghubung (aksi tanpa `Verifikasi`): penutupan overlay dan popup (langkah 6 dan 18), pemulihan kolom di overlay (langkah 32), dan pemulihan konfigurasi kolom `Note` (langkah 49 sampai 51, `[Save]` Setup Column adalah aksi sisi klien sehingga tanpa langkah "Tunggu aksi selesai"). Langkah 42 dan 47 adalah anchor positif (kolom lain tampil) untuk asersi absence kolom `Note` sesudah muat ulang dan login ulang.
- Langkah 28, 32, 35 sampai 36, dan 37 sampai 38 berulang untuk setiap baris tabel Data uji (sembilan iterasi, bagian 8b butir 7).
- Spec memiliki 51 langkah nominal dan 99 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Setup Column Tab Session pada akun yang sama tanpa seeding), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan ekspansi berasal dari perulangan per kolom data tanpa langkah bersyarat.
- Temuan untuk QA:
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD`, yang sudah terdaftar di `.env.example` dan `spectra.config.ts`.
  - TC-AC-ACAL-86 tidak menyebut kolom yang di-uncheck dan di-drag; spec memilih `Note` dan `Date` (pilihan spec).
  - TC-AC-ACAL-87 tidak menyebut kolom yang tersisa; spec menyisakan kolom terakhir `Device / Browser`, konsisten dengan TC-AC-ACAL-82 ("kecuali satu kolom terakhir").
  - TC-AC-ACAL-82 Expected a menyebut "tiap kolom yang di-uncheck" tanpa menyebut kolom yang tersisa pada langkah terakhir; kolom `Device / Browser` tetap tercentang.
  - TC-AC-ACAL-87 langkah 1 meng-uncheck kolom di Overlay Column Visibility, tetapi TC tidak menyatakan apakah perubahan overlay tersimpan di browser; spec memulihkannya dengan ceklis ulang (langkah 32).
