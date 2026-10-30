---
id: TC-GS-ACTLOG-E2E-024-setup-column-tab-session-overlay-popup-sembunyikan-cancel-kolom-terakhir
title: "Setup Column Tab Session: Overlay, Popup, Sembunyikan, Cancel, Kolom Terakhir"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-93
  - TC-GS-ACTLOG-94
  - TC-GS-ACTLOG-95
  - TC-GS-ACTLOG-96
  - TC-GS-ACTLOG-102
  - TC-GS-ACTLOG-103
coverage:
  web: automated
---

# Setup Column Tab Session: Overlay, Popup, Sembunyikan, Cancel, Kolom Terakhir

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan sekali di hook `before`, lalu halaman awal Global Settings > Activity Log > Session. Environment variable: `GS_TC_PASSWORD`.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Data Pre-setup dan Data Dinamis: tidak ada seeding. Tabel Tab Session memuat baris Login akun aktor dari hook `before` dan log lain entitas.
- Preferensi kolom tab Session (visibilitas, urutan, pin) tersimpan di cache browser (TC-GS-ACTLOG-95 butir b), bukan lewat API, sehingga tidak ada endpoint yang dipakai untuknya. "Muat ulang halaman (F5)" dilakukan pada konteks browser yang sama supaya cache tetap ada.
- Data uji TC-GS-ACTLOG-96 (sepuluh kolom, satu per iterasi):

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
  | 10 | `Device / Browser` |

- Kemampuan teknis: membuka overlay `Column Visibility (⋯)` dan popup Setup Column; menekan `Esc`; hover pada checkbox untuk membaca tooltip; memuat ulang halaman pada konteks browser yang sama.
- State global yang dipulihkan (di langkah 22, 51, dan hook `after` yang tetap jalan walau spec gagal di tengah): konfigurasi kolom tab Session dikembalikan ke default (sepuluh kolom tampil berurutan seperti pada Data uji TC-GS-ACTLOG-96, tanpa pin) lewat `[Reset to Default]` atau penghapusan key cache tab Session. Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

1. Buka Global Settings > Activity Log > Session

### TC-GS-ACTLOG-93: Screening Overlay Column Visibility

2. Klik header kolom `Column Visibility (⋯)`
3. Verifikasi overlay memuat 10 kolom berurutan: `Date`, `User`, `Employee ID`, `Position`, `Division`, `Activity`, `Status`, `Note`, `IP Address`, `Device / Browser`
4. Verifikasi tiap kolom di overlay memiliki checkbox tercentang dan aktif
5. Verifikasi tiap kolom di overlay memiliki drag handle
6. Verifikasi item `Setup Column...` tampil di bagian bawah overlay

### TC-GS-ACTLOG-94: Screening Popup Setup Column

7. Klik item `Setup Column...`
8. Verifikasi header popup memuat judul `Setup Column`
9. Verifikasi header popup memuat tombol tutup `(X)`
10. Verifikasi body popup memuat 10 baris kolom berurutan: `Date`, `User`, `Employee ID`, `Position`, `Division`, `Activity`, `Status`, `Note`, `IP Address`, `Device / Browser`
11. Verifikasi tiap baris kolom memiliki checkbox tercentang dan aktif
12. Verifikasi tiap baris kolom memiliki drag handle
13. Verifikasi tiap baris kolom memiliki icon Pin
14. Verifikasi tabel di balik popup siap menampilkan pratinjau
15. Verifikasi footer popup memuat tombol `[Reset to Default]` dan `[Save]`
16. Klik `(X)` untuk menutup popup

### TC-GS-ACTLOG-95: Overlay Column Visibility langsung menerapkan perubahan tanpa Save

17. Klik header `Column Visibility (⋯)`, lalu hilangkan centang kolom `Employee ID`
18. Verifikasi kolom `Employee ID` langsung hilang dari tabel
19. Verifikasi overlay tidak memiliki tombol Save
20. Muat ulang halaman (F5)
21. Verifikasi kolom `Employee ID` tetap tersembunyi setelah F5 (tersimpan di cache browser)
22. Klik header `Column Visibility (⋯)`, lalu centang kembali kolom `Employee ID`
23. Tutup overlay `Column Visibility (⋯)` dengan menekan `Esc`

### TC-GS-ACTLOG-96: Sembunyikan dan tampilkan kolom lewat Popup Setup Column

24. Untuk setiap baris tabel Data uji TC-GS-ACTLOG-96 (langkah 24 sampai 33): buka Popup Setup Column (klik header `Column Visibility (⋯)`, klik `Setup Column...`), lalu hilangkan centang kolom
25. Verifikasi kolom hilang dari tabel di balik popup sebelum `[Save]`
26. Klik `[Save]`
27. Verifikasi kolom tersembunyi di tabel setelah `[Save]`
28. Muat ulang halaman (F5)
29. Verifikasi kolom tetap tersembunyi setelah F5
30. Buka kembali Popup Setup Column
31. Centang kolom
32. Klik `[Save]`
33. Verifikasi kolom tampil di tabel

### TC-GS-ACTLOG-102: Esc dan tombol tutup (X) membatalkan perubahan Popup Setup Column

34. Buka Popup Setup Column, lalu hilangkan centang kolom `User`
35. Tutup popup dengan menekan `Esc`
36. Verifikasi popup tertutup
37. Verifikasi kolom `User` tetap tampil di tabel
38. Buka Popup Setup Column, lalu hilangkan centang kolom `User`
39. Klik `(X)`
40. Verifikasi popup tertutup
41. Verifikasi kolom `User` tetap tampil di tabel

### TC-GS-ACTLOG-103: Kolom terakhir yang tampil tidak dapat disembunyikan

42. Buka Popup Setup Column, hilangkan centang sembilan kolom selain `User`, lalu klik `[Save]`
43. Tunggu aksi selesai
44. Buka Popup Setup Column
45. Coba hilangkan centang kolom `User`, lalu arahkan kursor ke checkbox
46. Verifikasi checkbox kolom `User` nonaktif (disabled)
47. Verifikasi centang kolom `User` tidak dapat dihilangkan
48. Verifikasi tooltip `At least one column must remain visible.`
49. Centang kolom `Date`
50. Verifikasi checkbox kolom `User` kembali aktif

### Pemulihan state akhir

51. Klik `[Reset to Default]`
52. Klik `[Save]`
53. Tunggu aksi selesai

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md` (bagian Setup Column Tab Session). Semua TC sumber spec ini dikerjakan di sini; TC-GS-ACTLOG-97 dan 98 (bergantung pada TC-GS-ACTLOG-94) ada di spec 025, serta TC-GS-ACTLOG-99, 100, dan 101 di spec 026 (TC-GS-ACTLOG-101 bergantung pada TC-GS-ACTLOG-96).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 dan 16 (membuka dan menutup popup untuk TC-GS-ACTLOG-94), langkah 22 (memulihkan visibilitas `Employee ID` setelah TC-GS-ACTLOG-95), langkah 23 (menutup overlay sebelum popup dibuka pada langkah 24), langkah 42 (membentuk precondition TC-GS-ACTLOG-103 "kolom selain `User` sudah disembunyikan"), langkah 43 dan 53 (menunggu `[Save]` selesai karena hasilnya tidak diasersi langsung, 8b butir 8), dan langkah 51 sampai 53 (memulihkan konfigurasi kolom di akhir spec; hook `after` sebagai cadangan). Langkah 24 membuka popup di tiap iterasi karena `[Save]` menutup popup; TC hanya menulis pembukaan popup sekali.
- Langkah 24 sampai 33 berulang untuk setiap baris tabel Data uji TC-GS-ACTLOG-96 di Prerequisites.
- Spec memiliki 53 langkah nominal dan 143 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas harness (Setup Column Tab Session pada akun dan tabel yang sama), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan sebagian besar langkah adalah `Verifikasi` hasil pemecahan klausa Expected (S-01) serta satu iterasi sepuluh kolom TC-GS-ACTLOG-96.
- Temuan untuk QA:
  - TC-GS-ACTLOG-94 Expected butir c menulis footer popup `[Cancel]`, `[Reset to Default]`, `[Save]`, dan TC-GS-ACTLOG-102 menulis judul dan langkah klik `[Cancel]`. Modal Setup Column tidak punya `[Cancel]` (prd-conventions.md §9.3 bagian Apply timing dan §24.1); spec mengasersi footer `[Reset to Default]` dan `[Save]`, serta membatalkan perubahan lewat `Esc` (langkah 35) dan `(X)` (langkah 39).
  - TC-GS-ACTLOG-96 menulis siklus hilangkan centang sampai centang kembali per kolom tanpa menyatakan apakah popup tertutup setelah `[Save]`; spec membuka popup di tiap iterasi (langkah 24 dan langkah "Buka kembali Popup Setup Column").
  - TC-GS-ACTLOG-96 mengasersi "setelah [Save] dan F5 kolom tetap tersembunyi" dalam satu butir; spec memisahkannya menjadi asersi setelah `[Save]` dan setelah F5.
  - TC dan PRD tidak menentukan penutupan overlay `Column Visibility (⋯)` setelah centang kolom; spec menutupnya dengan `Esc` (langkah 23).
