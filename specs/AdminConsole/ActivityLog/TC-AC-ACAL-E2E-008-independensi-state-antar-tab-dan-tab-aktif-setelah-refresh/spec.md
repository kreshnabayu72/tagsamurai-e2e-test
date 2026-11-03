---
id: TC-AC-ACAL-E2E-008-independensi-state-antar-tab-dan-tab-aktif-setelah-refresh
title: "Independensi State Antar Tab dan Tab Aktif Setelah Refresh"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-112
  - TC-AC-ACAL-115
coverage:
  web: automated
---

# Independensi State Antar Tab dan Tab Aktif Setelah Refresh

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; kredensial `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Email akun memuat placeholder `{namaCompany}` seperti di Pre-setup TC (lihat Temuan untuk QA).
- Data Log yang di-seed di hook `before` (volume Pre-setup No 11; kemampuan seeding log disediakan tim FE/BE; lihat Temuan untuk QA):
  - Tab Session: sedikitnya 30 entri milik `John Doe` (EMP001, Position `Staff`, Division `Marketing`; nama literal menurut Lampiran A-3 (S-12) karena Search `John` bergantung pada nama; seeding idempotent, dilewati bila sudah ada, dan tidak dihapus), sehingga Search `John` dengan Filter Division `Marketing` memberi lebih dari 25 hasil (cukup untuk Rows per page `25`; halaman 2 tab Session tidak diasersi).
  - Tab User Action: sedikitnya 30 entri dengan Object `Partner`, Action `Suspend`, Name `Partner ActLog {runId}-008` dan sejenisnya sehingga Search `Partner` memberi lebih dari 10 hasil (halaman 2 pada 10 baris per halaman).
  - Seeding idempotent (dilewati bila sudah ada), tidak dihapus (audit trail permanen).
- Kemampuan teknis (disediakan tim FE): refresh halaman (F5); logout tidak dipakai di spec ini.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- State global: tidak ada yang diubah.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACAL-112: Search, Filter, Sort, halaman tiap tab independen dan dipertahankan saat pindah tab

1. Ketik Search `John`, tekan Enter
2. Klik icon Filter, pilih Division `Marketing`, klik `[Apply]`
3. Klik sort User sekali (User ↑)
4. Ganti Rows per page ke `25`
5. Verifikasi tab Session: sedikitnya satu baris tampil
6. Verifikasi tab Session tersaring: setiap baris memuat `John` dan Division `Marketing`
7. Klik tab "User Action"
8. Verifikasi tab User Action: kotak Search kosong
9. Verifikasi tab User Action: tanpa Filter dari tab Session
10. Verifikasi tab User Action: tanpa Sort dari tab Session
11. Ketik Search `Partner`, tekan Enter
12. Pindah ke halaman 2
13. Verifikasi tab User Action: sedikitnya satu baris tampil
14. Verifikasi tab User Action tersaring: setiap baris memuat `Partner`
15. Verifikasi tab User Action: halaman 2 aktif
16. Klik tab "Session"
17. Verifikasi tab Session: kotak Search masih berisi `John`
18. Verifikasi tab Session: Filter Division `Marketing` masih aktif
19. Verifikasi tab Session: Sort User ↑ masih aktif
20. Verifikasi tab Session: Rows per page masih `25`
21. Klik tab "User Action"
22. Verifikasi tab User Action: kotak Search masih berisi `Partner`
23. Verifikasi tab User Action: halaman 2 masih aktif

### TC-AC-ACAL-115: Tab aktif setelah refresh (F5)

24. Klik tab "User Action"
25. Tekan F5
26. Verifikasi tab User Action tetap aktif setelah refresh (tidak kembali ke Session)

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-112, 115). Tidak ada TC hanya-BE di spec ini.
- Langkah "Verifikasi ... sedikitnya satu baris tampil" pada TC-112 (langkah 5 dan 13) adalah pembanding sebelum asersi universal "setiap baris ..." (bagian 8b butir 2); Expected TC tidak memuatnya.
- Langkah penghubung (S-03): langkah 24 (klik tab "User Action") memenuhi precondition TC-115 "berada di Admin Console > Activity Log > User Action"; tab itu sudah aktif dari langkah 21, sehingga klik ini tidak mengubah state dan dipertahankan karena precondition TC mensyaratkannya.
- Temuan untuk QA:
  - TC-112 Expected a menyebut "Tab Session tersaring" tanpa merinci; spec mengasersi setiap baris memuat `John` dan Division `Marketing`.
  - TC-112 Expected c ("halaman 2") tidak menyebut jumlah baris; spec mengasersi halaman 2 aktif dan hasil tersaring `Partner`.
  - TC-112 langkah 3 mensyaratkan lebih dari 10 hasil Search `Partner`; precondition TC ("Data >= 30 entri per tab") tidak menyebut komposisi data, sehingga komposisi seed ditetapkan di Prerequisites.
  - Mekanisme seeding entri log tidak didefinisikan di TC, PRD, atau LLD yang dibaca; kemampuan itu diminta dari tim FE/BE.
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD` (akun `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`), terdaftar di `.env.example` dan `spectra.config.ts`.
