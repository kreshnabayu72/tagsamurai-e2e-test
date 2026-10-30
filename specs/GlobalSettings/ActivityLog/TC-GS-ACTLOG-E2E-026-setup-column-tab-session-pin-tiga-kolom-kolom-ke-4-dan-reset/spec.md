---
id: TC-GS-ACTLOG-E2E-026-setup-column-tab-session-pin-tiga-kolom-kolom-ke-4-dan-reset
title: "Setup Column Tab Session: Pin Tiga Kolom, Kolom Ke-4, dan Reset"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-99
  - TC-GS-ACTLOG-100
  - TC-GS-ACTLOG-101
coverage:
  web: automated
---

# Setup Column Tab Session: Pin Tiga Kolom, Kolom Ke-4, dan Reset

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan sekali di hook `before`, lalu halaman awal Global Settings > Activity Log > Session. Environment variable: `GS_TC_PASSWORD`.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Data Pre-setup dan Data Dinamis: tidak ada seeding. Tabel Tab Session memuat baris Login akun aktor dari hook `before` dan log lain entitas.
- Preferensi kolom tab Session (visibilitas, urutan, pin) tersimpan di cache browser (TC-GS-ACTLOG-95 butir b), bukan lewat API, sehingga tidak ada endpoint yang dipakai untuknya. "Muat ulang halaman (F5)" dilakukan pada konteks browser yang sama supaya cache tetap ada.
- Lebar viewport: tabel dapat digulir horizontal. Nilai lebar ditetapkan tim FE (contoh 1024 px) dan diatur di langkah 2; viewport dipulihkan di langkah 36.
- Kemampuan teknis: drag and drop baris kolom di Popup Setup Column; mengatur viewport; menggulir tabel secara horizontal dan membaca kolom yang membeku; hover pada icon Pin untuk membaca tooltip; memuat ulang halaman pada konteks browser yang sama.
- State global yang dipulihkan (di langkah 12 sampai 15, 32, 36, dan hook `after` yang tetap jalan walau spec gagal di tengah): konfigurasi kolom tab Session dikembalikan ke default (sepuluh kolom tampil berurutan `Date`, `User`, `Employee ID`, `Position`, `Division`, `Activity`, `Status`, `Note`, `IP Address`, `Device / Browser`, tanpa pin) lewat `[Reset to Default]` atau penghapusan key cache tab Session; viewport dikembalikan ke ukuran awal. Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

1. Buka Global Settings > Activity Log > Session
2. Atur lebar viewport sehingga tabel dapat digulir horizontal

### TC-GS-ACTLOG-99: Pin tiga kolom sekaligus dan urutan kolom beku

3. Buka Popup Setup Column (klik header `Column Visibility (⋯)`, klik `Setup Column...`)
4. Klik icon Pin pada kolom `Date`, `User`, dan `Employee ID`
5. Seret kolom `Employee ID` ke atas `Date` di antara kolom beku
6. Klik `[Save]`
7. Gulir tabel ke kanan
8. Verifikasi ketiga kolom (`Employee ID`, `Date`, `User`) membeku di sisi kiri
9. Verifikasi urutan kolom beku dari kiri: `Employee ID`, `Date`, `User`
10. Verifikasi kolom lain tergulir
11. Verifikasi kolom `Column Visibility (⋯)` tetap di sisi kanan

### Pemulihan state antar TC

12. Buka Popup Setup Column
13. Klik `[Reset to Default]`
14. Klik `[Save]`
15. Tunggu aksi selesai

### TC-GS-ACTLOG-100: Pin kolom ke-4 ditolak saat tiga kolom sudah beku

16. Buka Popup Setup Column
17. Klik icon Pin pada kolom `Date`, `User`, dan `Employee ID`
18. Arahkan kursor ke icon Pin pada kolom `Position`
19. Verifikasi icon Pin kolom `Position` nonaktif (disabled)
20. Verifikasi icon Pin kolom `Position` tidak dapat diklik
21. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.` muncul saat hover
22. Verifikasi kolom `Position` tidak membeku
23. Klik icon Pin kolom `Date` untuk melepas pin
24. Verifikasi icon Pin kolom `Position` aktif kembali

### Pemulihan state antar TC

25. Tutup popup dengan `(X)` (perubahan pin belum disimpan sehingga dibuang)

### TC-GS-ACTLOG-101: Reset to Default di Popup Setup Column

26. Buka Popup Setup Column, hilangkan centang kolom `User`, klik icon Pin pada kolom `Date`, lalu klik `[Save]`
27. Tunggu aksi selesai
28. Buka Popup Setup Column
29. Klik `[Reset to Default]`
30. Verifikasi tabel di balik popup kembali ke susunan default: kolom `Date`, `User`, `Employee ID`, `Position`, `Division`, `Activity`, `Status`, `Note`, `IP Address`, `Device / Browser` tampil berurutan
31. Verifikasi tabel di balik popup tanpa kolom beku
32. Klik `[Save]`
33. Tunggu aksi selesai
34. Muat ulang halaman (F5)
35. Verifikasi susunan default tetap berlaku setelah F5

### Pemulihan state akhir

36. Kembalikan lebar viewport ke ukuran awal

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md` (bagian Setup Column Tab Session). Semua TC sumber spec ini dikerjakan di sini; TC-GS-ACTLOG-98 (prasyarat TC-GS-ACTLOG-99) ada di spec 025 dan TC-GS-ACTLOG-96 (prasyarat TC-GS-ACTLOG-101) ada di spec 024.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2 (mengatur viewport untuk precondition TC-GS-ACTLOG-99 sampai 100), langkah 12 sampai 15 (mengembalikan konfigurasi tersimpan ke default setelah TC-GS-ACTLOG-99, karena pin yang tersimpan akan terlepas oleh klik icon Pin pada langkah sesudah 16), langkah 25 (menutup popup tanpa menyimpan), langkah 26 (membentuk precondition TC-GS-ACTLOG-101 "kolom `User` disembunyikan, kolom `Date` di-pin"), langkah 15, 27, dan 33 (menunggu `[Save]` selesai karena hasilnya tidak diasersi langsung, 8b butir 8), dan langkah 36 (memulihkan viewport; hook `after` sebagai cadangan).
- Spec memiliki 36 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu kelas harness (Setup Column Tab Session pada akun dan tabel yang sama), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan sebagian besar langkah adalah `Verifikasi` hasil pemecahan klausa Expected (S-01) serta langkah pemulihan antar TC.
- Temuan untuk QA:
  - TC-GS-ACTLOG-99 dan 100 tidak menyebut lebar viewport yang membuat tabel dapat digulir horizontal; nilai ditetapkan tim FE di Prerequisites.
