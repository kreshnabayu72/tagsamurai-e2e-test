---
id: TC-AC-ACAL-E2E-050-klik-ulang-menu-activity-log-mereset-kedua-tab-ke-default
title: "Klik Ulang Menu Activity Log Mereset Kedua Tab ke Default"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-113
coverage:
  web: automated
---

# Klik Ulang Menu Activity Log Mereset Kedua Tab ke Default

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; kredensial `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Email akun memuat placeholder `{namaCompany}` seperti di Pre-setup TC (lihat Temuan untuk QA).
- Data Log yang di-seed di hook `before` (kemampuan seeding log disediakan tim FE/BE; lihat Temuan untuk QA):
  - Tab Session: sedikitnya satu entri milik `John Doe` (EMP001, Division `Marketing`; nama literal menurut Lampiran A-3 (S-12) karena Search `John` bergantung pada nama; seeding idempotent, tidak dihapus).
  - Tab User Action: sedikitnya satu entri dengan Object `Partner`, Action `Suspend`, Name `Partner ActLog {runId}-050`.
  - Seeding tidak dihapus (audit trail permanen).
  - Pembanding sort default: tiap tab memuat sedikitnya dua baris dengan nilai Date berbeda; seeding dua entri dengan Date berbeda per tab ditetapkan tim FE.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- State global: tidak ada yang diubah.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACAL-113: Klik ulang menu Activity Log di sidebar mereset kedua tab ke default

1. Ketik Search `John`, tekan Enter
2. Klik icon Filter, pilih Division `Marketing`, klik `[Apply]`
3. Klik sort User sekali (User ↑)
4. Klik tab "User Action"
5. Ketik Search `Partner`, tekan Enter
6. Klik icon Filter, pilih Action `Suspend`, klik `[Apply]`
7. Klik sort Name sekali
8. Klik menu Activity Log di sidebar Admin Console
9. Verifikasi tab Session aktif
10. Verifikasi tab Session: tanpa Search
11. Verifikasi tab Session: tanpa Filter
12. Verifikasi tab Session: sedikitnya dua baris tampil
13. Verifikasi tab Session: sort default
14. Verifikasi tab Session: halaman 1
15. Verifikasi tab Session: Rows per page `10`
16. Klik tab "User Action"
17. Verifikasi tab User Action: tanpa Search
18. Verifikasi tab User Action: tanpa Filter
19. Verifikasi tab User Action: sedikitnya dua baris tampil
20. Verifikasi tab User Action: sort default
21. Verifikasi tab User Action: halaman 1
22. Verifikasi tab User Action: Rows per page `10`

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-113). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 sampai 5 (membentuk Search, Filter, dan Sort aktif pada kedua tab sebagai precondition TC-113; Search `John`, Filter Division `Marketing`, dan sort User pada tab Session, lalu Search `Partner` pada tab User Action), langkah 6 dan 7 (Filter dan Sort tab User Action, karena precondition TC-113 mensyaratkan kedua tab memiliki Search, Filter, dan Sort aktif).
- Asersi tambahan di luar Expected TC (S-03): langkah 12 dan 19 (`Verifikasi` sedikitnya dua baris tampil) adalah data pembanding (anchor) untuk asersi sort default pada langkah 13 dan 20; Expected TC-113 tidak memuatnya.
- Temuan untuk QA:
  - TC-113 precondition mensyaratkan Search, Filter, dan Sort aktif pada kedua tab tanpa merinci nilainya; nilai Search `John`, Division `Marketing`, sort User, Search `Partner`, Action `Suspend`, dan sort Name dipilih spec.
  - TC-113 Expected "sort default" tidak mendefinisikan indikator sort default; spec mengasersi sort default secara umum.
  - Mekanisme seeding entri log tidak didefinisikan di TC, PRD, atau LLD yang dibaca; kemampuan itu diminta dari tim FE/BE.
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD` (akun `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`), terdaftar di `.env.example` dan `spectra.config.ts`.
