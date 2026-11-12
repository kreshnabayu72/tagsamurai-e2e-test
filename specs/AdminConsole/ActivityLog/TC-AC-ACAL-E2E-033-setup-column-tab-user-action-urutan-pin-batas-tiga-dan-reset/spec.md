---
id: TC-AC-ACAL-E2E-033-setup-column-tab-user-action-urutan-pin-batas-tiga-dan-reset
title: "Setup Column Tab User Action: Urutan, Pin, Batas Tiga Kolom, dan Reset"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-107
  - TC-AC-ACAL-108
  - TC-AC-ACAL-109
coverage:
  web: automated
---

# Setup Column Tab User Action: Urutan, Pin, Batas Tiga Kolom, dan Reset

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; `{namaCompany}` ditetapkan tim FE), password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Activity Log (lihat suite.md).
- Data Pre-setup dan Data Dinamis: tidak ada seeding. Tabel Tab User Action cukup memuat entri User Action apa pun; spec hanya mengamati kolom dan kontrol Setup Column.
- Data uji TC-AC-ACAL-107 dan TC-AC-ACAL-108 (delapan kolom, satu per iterasi; urutan default tab User Action):

  | No | Kolom |
  |---|---|
  | 1 | `Date` |
  | 2 | `Action` |
  | 3 | `Object` |
  | 4 | `Name` |
  | 5 | `Field` |
  | 6 | `Old Value` |
  | 7 | `New Value` |
  | 8 | `Modified By` |

- Pilihan spec (TC tidak menyebutkan sasaran): pada TC-AC-ACAL-107 tiap kolom digeser ke posisi terakhir; pada TC-AC-ACAL-108 tiga kolom yang di-pin adalah tiga kolom pertama pada urutan tersimpan (`Modified By`, `Date`, `Action`), kolom keempat adalah `Object`, dan kolom yang di-unpin sesudah Save adalah `Action`.
- Lebar viewport untuk TC-AC-ACAL-108: tabel dapat digulir horizontal. Nilai lebar ditetapkan tim FE (contoh 1024 px) dan diatur di langkah 22; viewport dipulihkan di langkah 28.
- Kemampuan teknis (disediakan tim FE): drag and drop baris kolom di Popup Setup Column; hover icon Pin untuk membaca tooltip; mengatur viewport; menggulir tabel secara horizontal dan membaca kolom yang membeku; muat ulang halaman (F5) pada konteks browser yang sama supaya preferensi kolom di browser tetap ada; menghapus preferensi kolom tab User Action di browser.
- State global yang diubah: preferensi kolom tab User Action (urutan dan pin, disimpan di browser, bukan lewat API). TC-AC-ACAL-109 mengembalikannya ke default (langkah 29 sampai 35); hook `after` menghapus preferensi kolom di browser (didaftarkan di `suite.md`) bila spec gagal sebelum langkah itu. Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

1. Buka Admin Console > Activity Log > User Action

### TC-AC-ACAL-107: Geser urutan kolom

2. Klik header `⋯`, klik `Setup Column...`
3. Untuk setiap baris tabel Data uji TC-AC-ACAL-107 dan TC-AC-ACAL-108 (langkah 3 sampai 4): drag kolom ke posisi terakhir
4. Verifikasi kolom yang digeser berpindah ke posisi baru pada preview (tidak ada kolom terkunci)
5. Drag kolom terakhir (`Modified By`) ke posisi pertama
6. Verifikasi urutan preview berubah menjadi `Modified By | Date | Action | Object | Name | Field | Old Value | New Value`
7. Klik `[Save]`
8. Verifikasi urutan tabel berubah menjadi `Modified By | Date | Action | Object | Name | Field | Old Value | New Value`
9. Muat ulang halaman (F5)
10. Verifikasi urutan baru tetap (`Modified By` kolom pertama tabel)

### TC-AC-ACAL-108: Pin dan unpin kolom serta batas tiga kolom beku

11. Klik header `⋯`, klik `Setup Column...`
12. Untuk setiap baris tabel Data uji TC-AC-ACAL-107 dan TC-AC-ACAL-108 (langkah 12 sampai 15): klik icon Pin kolom
13. Verifikasi icon Pin kolom aktif
14. Klik icon Pin kolom lagi
15. Verifikasi icon Pin kolom nonaktif
16. Pin kolom `Modified By`, `Date`, dan `Action`
17. Verifikasi tiga kolom `Modified By`, `Date`, dan `Action` ter-pin
18. Arahkan kursor ke icon Pin kolom keempat (`Object`)
19. Verifikasi icon Pin kolom `Object` disabled dan tetap tampil
20. Verifikasi tooltip icon Pin `Maximum 3 columns can be pinned at once. Unpin another column first.`
21. Klik `[Save]`
22. Atur lebar viewport sehingga tabel dapat digulir horizontal
23. Gulir tabel secara horizontal
24. Verifikasi kolom ter-pin (`Modified By`, `Date`, `Action`) tetap di kiri saat tabel digulir
25. Klik header `⋯`, klik `Setup Column...`, unpin kolom `Action`, klik `[Save]`
26. Gulir tabel secara horizontal
27. Verifikasi kolom `Action` yang di-unpin ikut bergeser saat tabel digulir
28. Pulihkan lebar viewport ke ukuran awal

### TC-AC-ACAL-109: Reset to Default

29. Klik header `⋯`, klik `Setup Column...`
30. Klik `[Reset to Default]`
31. Verifikasi preview kembali ke default: kolom `Date | Action | Object | Name | Field | Old Value | New Value | Modified By` visible dengan urutan itu
32. Verifikasi preview tanpa kolom ter-pin
33. Klik `[Save]`
34. Muat ulang halaman (F5)
35. Verifikasi tabel tetap default: kolom `Date | Action | Object | Name | Field | Old Value | New Value | Modified By` berurutan dan tanpa kolom ter-pin

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (bagian 4b, Tab User Action). Seluruh TC sumber spec ini dikerjakan di sini.
- Urutan TC di dalam spec: TC-AC-ACAL-107, 108, lalu 109. TC-AC-ACAL-109 berprecondition "konfigurasi kolom sudah diubah dan tersimpan", yang dipenuhi oleh TC-AC-ACAL-107 dan 108 pada spec yang sama; Reset to Default sekaligus memulihkan state spec.
- Langkah penghubung (aksi tanpa `Verifikasi`): pengaturan dan pemulihan viewport (langkah 22 dan 28), menggulir tabel (langkah 23 dan 26), dan membuka ulang Popup Setup Column (langkah 25). `[Save]` Setup Column adalah aksi sisi klien tanpa langkah "Tunggu aksi selesai".
- Langkah 3 sampai 4 dan 12 sampai 15 berulang untuk setiap baris tabel Data uji (delapan iterasi, bagian 8b butir 7).
- Spec memiliki 35 langkah nominal dan 77 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Setup Column Tab User Action pada akun yang sama tanpa seeding), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan ekspansi berasal dari perulangan per kolom data tanpa langkah bersyarat.
- Temuan untuk QA:
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD`, yang sudah terdaftar di `.env.example` dan `spectra.config.ts`.
  - TC-AC-ACAL-107 menyatakan "drag tiap kolom ke posisi lain" tanpa posisi tujuan; TC-AC-ACAL-108 tidak menyebut kolom yang di-pin, kolom keempat, dan kolom yang di-unpin. Spec memilih sasaran seperti pada Prerequisites (pilihan spec).
  - TC-AC-ACAL-108 langkah 4 (Save, scroll) dan langkah 5 (unpin, Save) dipetakan ke Expected d dan e menurut urutan langkah; TC tidak menyatakan pemetaan itu eksplisit.
  - TC tidak menyebut lebar viewport agar tabel dapat digulir horizontal; nilai ditetapkan tim FE.
