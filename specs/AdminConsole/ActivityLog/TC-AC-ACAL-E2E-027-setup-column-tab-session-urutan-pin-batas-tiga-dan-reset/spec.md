---
id: TC-AC-ACAL-E2E-027-setup-column-tab-session-urutan-pin-batas-tiga-dan-reset
title: "Setup Column Tab Session: Urutan, Pin, Batas Tiga Kolom, dan Reset"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-83
  - TC-AC-ACAL-84
  - TC-AC-ACAL-85
coverage:
  web: automated
---

# Setup Column Tab Session: Urutan, Pin, Batas Tiga Kolom, dan Reset

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; `{namaCompany}` ditetapkan tim FE), password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Activity Log (lihat suite.md).
- Data Pre-setup dan Data Dinamis: tidak ada seeding. Tabel Tab Session cukup memuat entri sesi akun aktor dan entri lain; spec hanya mengamati kolom dan kontrol Setup Column.
- Data uji TC-AC-ACAL-83 dan TC-AC-ACAL-84 (sepuluh kolom, satu per iterasi; urutan default tab Session):

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

- Pilihan spec (TC tidak menyebutkan sasaran): pada TC-AC-ACAL-83 tiap kolom digeser ke posisi terakhir; pada TC-AC-ACAL-84 tiga kolom yang di-pin adalah tiga kolom pertama pada urutan tersimpan (`Device / Browser`, `Date`, `User`), kolom keempat adalah `Employee ID`, dan kolom yang di-unpin sesudah Save adalah `User`.
- Lebar viewport untuk TC-AC-ACAL-84: tabel dapat digulir horizontal. Nilai lebar ditetapkan tim FE (contoh 1024 px) dan diatur di langkah 21; viewport dipulihkan di langkah 27.
- Kemampuan teknis (disediakan tim FE): drag and drop baris kolom di Popup Setup Column; hover icon Pin untuk membaca tooltip; mengatur viewport; menggulir tabel secara horizontal dan membaca kolom yang membeku; muat ulang halaman (F5) pada konteks browser yang sama supaya preferensi kolom di browser tetap ada; menghapus preferensi kolom tab Session di browser.
- State global yang diubah: preferensi kolom tab Session (urutan dan pin, disimpan di browser, bukan lewat API). TC-AC-ACAL-85 mengembalikannya ke default (langkah 28 sampai 34); hook `after` menghapus preferensi kolom di browser (didaftarkan di `suite.md`) bila spec gagal sebelum langkah itu. Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-AC-ACAL-83: Geser urutan kolom

1. Klik header `⋯`, klik `Setup Column...`
2. Untuk setiap baris tabel Data uji TC-AC-ACAL-83 dan TC-AC-ACAL-84 (langkah 2 sampai 3): drag kolom ke posisi terakhir
3. Verifikasi kolom yang digeser berpindah ke posisi baru pada preview (tidak ada kolom terkunci)
4. Drag kolom terakhir (`Device / Browser`) ke posisi pertama
5. Verifikasi urutan preview berubah menjadi `Device / Browser | Date | User | Employee ID | Position | Division | Activity | Status | Note | IP Address`
6. Klik `[Save]`
7. Verifikasi urutan tabel berubah menjadi `Device / Browser | Date | User | Employee ID | Position | Division | Activity | Status | Note | IP Address`
8. Muat ulang halaman (F5)
9. Verifikasi urutan baru tetap (`Device / Browser` kolom pertama tabel)

### TC-AC-ACAL-84: Pin dan unpin kolom serta batas tiga kolom beku

10. Klik header `⋯`, klik `Setup Column...`
11. Untuk setiap baris tabel Data uji TC-AC-ACAL-83 dan TC-AC-ACAL-84 (langkah 11 sampai 14): klik icon Pin kolom
12. Verifikasi icon Pin kolom aktif
13. Klik icon Pin kolom lagi
14. Verifikasi icon Pin kolom nonaktif
15. Pin kolom `Device / Browser`, `Date`, dan `User`
16. Verifikasi tiga kolom `Device / Browser`, `Date`, dan `User` ter-pin
17. Arahkan kursor ke icon Pin kolom keempat (`Employee ID`)
18. Verifikasi icon Pin kolom `Employee ID` disabled dan tetap tampil
19. Verifikasi tooltip icon Pin `Maximum 3 columns can be pinned at once. Unpin another column first.`
20. Klik `[Save]`
21. Atur lebar viewport sehingga tabel dapat digulir horizontal
22. Gulir tabel secara horizontal
23. Verifikasi kolom ter-pin (`Device / Browser`, `Date`, `User`) tetap di kiri saat tabel digulir
24. Klik header `⋯`, klik `Setup Column...`, unpin kolom `User`, klik `[Save]`
25. Gulir tabel secara horizontal
26. Verifikasi kolom `User` yang di-unpin ikut bergeser saat tabel digulir
27. Pulihkan lebar viewport ke ukuran awal

### TC-AC-ACAL-85: Reset to Default

28. Klik header `⋯`, klik `Setup Column...`
29. Klik `[Reset to Default]`
30. Verifikasi preview kembali ke default: kolom `Date | User | Employee ID | Position | Division | Activity | Status | Note | IP Address | Device / Browser` visible dengan urutan itu
31. Verifikasi preview tanpa kolom ter-pin
32. Klik `[Save]`
33. Muat ulang halaman (F5)
34. Verifikasi tabel tetap default: kolom `Date | User | Employee ID | Position | Division | Activity | Status | Note | IP Address | Device / Browser` berurutan dan tanpa kolom ter-pin

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (bagian 4a, Tab Session). Seluruh TC sumber spec ini dikerjakan di sini.
- Urutan TC di dalam spec: TC-AC-ACAL-83, 84, lalu 85. TC-AC-ACAL-85 berprecondition "konfigurasi kolom sudah diubah dan tersimpan", yang dipenuhi oleh TC-AC-ACAL-83 dan 84 pada spec yang sama; Reset to Default sekaligus memulihkan state spec.
- Langkah penghubung (aksi tanpa `Verifikasi`): pengaturan dan pemulihan viewport (langkah 21 dan 27), menggulir tabel (langkah 22 dan 25), dan membuka ulang Popup Setup Column (langkah 24). `[Save]` Setup Column adalah aksi sisi klien tanpa langkah "Tunggu aksi selesai".
- Langkah 2 sampai 3 dan 11 sampai 14 berulang untuk setiap baris tabel Data uji (sepuluh iterasi, bagian 8b butir 7).
- Spec memiliki 34 langkah nominal dan 88 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Setup Column Tab Session pada akun yang sama tanpa seeding), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan ekspansi berasal dari perulangan per kolom data tanpa langkah bersyarat.
- Temuan untuk QA:
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD`, yang sudah terdaftar di `.env.example` dan `spectra.config.ts`.
  - TC-AC-ACAL-83 menyatakan "drag tiap kolom ke posisi lain" tanpa posisi tujuan; TC-AC-ACAL-84 tidak menyebut kolom yang di-pin, kolom keempat, dan kolom yang di-unpin. Spec memilih sasaran seperti pada Prerequisites (pilihan spec).
  - TC-AC-ACAL-84 langkah 4 (Save, scroll) dan langkah 5 (unpin, Save) dipetakan ke Expected d dan e menurut urutan langkah; TC tidak menyatakan pemetaan itu eksplisit.
  - TC tidak menyebut lebar viewport agar tabel dapat digulir horizontal; nilai ditetapkan tim FE.
