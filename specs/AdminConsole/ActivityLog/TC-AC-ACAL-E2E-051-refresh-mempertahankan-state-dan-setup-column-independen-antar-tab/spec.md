---
id: TC-AC-ACAL-E2E-051-refresh-mempertahankan-state-dan-setup-column-independen-antar-tab
title: "Refresh Mempertahankan State dan Setup Column Independen Antar Tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-114
  - TC-AC-ACAL-120
coverage:
  web: automated
---

# Refresh Mempertahankan State dan Setup Column Independen Antar Tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; kredensial `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Email akun memuat placeholder `{namaCompany}` seperti di Pre-setup TC (lihat Temuan untuk QA).
- Data Log yang di-seed di hook `before` (volume Pre-setup No 11; kemampuan seeding log disediakan tim FE/BE; lihat Temuan untuk QA):
  - Tab Session: sedikitnya 30 entri milik `John Doe` (EMP001, Position `Staff`, Division `Marketing`; nama literal menurut Lampiran A-3 (S-12) karena Search `John` bergantung pada nama; seeding idempotent, tidak dihapus), sehingga Search `John` dengan Filter Position `Staff` memberi lebih dari 25 hasil (halaman 2 pada 25 baris per halaman).
  - Seeding tidak dihapus (audit trail permanen).
- Kemampuan teknis (disediakan tim FE): refresh halaman (F5). Pemulihan konfigurasi kolom: hook `after` suite menghapus preferensi Setup Column di browser (lihat suite.md); spec ini memuat langkah pemulihan eksplisit untuk kolom `Note` dan `Field`.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- State global yang diubah: preferensi kolom Setup Column tab Session dan tab User Action di browser (dipulihkan lewat langkah penghubung dan hook suite `after`).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACAL-114: Refresh (F5) mempertahankan Search, Filter, Sort, halaman, dan page size

1. Ketik Search `John`, tekan Enter
2. Klik icon Filter, pilih Position `Staff`, klik `[Apply]`
3. Klik sort Date sekali (Date ↑)
4. Ganti Rows per page ke `25`
5. Pindah ke halaman 2
6. Tekan F5
7. Verifikasi tab Session: kotak Search masih berisi `John`
8. Verifikasi tab Session: Filter Position `Staff` masih aktif
9. Verifikasi tab Session: Sort Date ↑ masih aktif
10. Verifikasi tab Session: halaman 2 masih aktif
11. Verifikasi tab Session: Rows per page masih `25`

### TC-AC-ACAL-120: Konfigurasi Setup Column Tab Session dan Tab User Action independen

12. Klik menu Activity Log di sidebar Admin Console
13. Klik header `⋯` tab Session
14. Hapus centang `Note` pada Overlay Column Visibility
15. Verifikasi tab Session: kolom `Note` hilang
16. Tutup Overlay Column Visibility dengan `Esc`
17. Klik tab "User Action"
18. Verifikasi tab User Action: kolom `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value`, `Description`, dan `Modified By` tampil
19. Klik header `⋯` tab User Action
20. Hapus centang `Field` pada Overlay Column Visibility
21. Verifikasi tab User Action: kolom `Field` hilang
22. Tutup Overlay Column Visibility dengan `Esc`
23. Klik tab "Session"
24. Verifikasi tab Session: kolom `Note` tetap hilang
25. Verifikasi tab Session: kolom `Date`, `User`, `Employee ID`, `Position`, `Division`, `Activity`, `Status`, `IP Address`, dan `Device / Browser` tampil
26. Klik header `⋯` tab Session
27. Centang kembali `Note` pada Overlay Column Visibility
28. Tutup Overlay Column Visibility dengan `Esc`
29. Klik tab "User Action"
30. Klik header `⋯` tab User Action
31. Centang kembali `Field` pada Overlay Column Visibility
32. Tutup Overlay Column Visibility dengan `Esc`

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-114, 120). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 12 (klik ulang menu mereset state tab sebelum TC-120), langkah 16 dan 22 (tutup Overlay Column Visibility dengan `Esc`), dan langkah 26 sampai 32 (memulihkan kolom `Note` dan `Field`; pemulihan state yang diubah spec, S-09, dengan hook `after` suite sebagai cadangan).
- Temuan untuk QA:
  - TC-120 hanya menyebut "hide kolom Note" tanpa menyebut jalurnya (Overlay Column Visibility atau Popup Setup Column dengan `[Save]`); spec memakai Overlay Column Visibility.
  - Mekanisme seeding entri log tidak didefinisikan di TC, PRD, atau LLD yang dibaca; kemampuan itu diminta dari tim FE/BE.
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD` (akun `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`), terdaftar di `.env.example` dan `spectra.config.ts`.
