---
id: TC-FA-FAAL-E2E-026-filter-position-division-note-dan-opsi-dropdown
title: "Filter Tab Session: Position, Division, Note, dan Opsi Dropdown"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-77
  - TC-FA-FAAL-78
coverage:
  web: automated
---

# Filter Tab Session: Position, Division, Note, dan Opsi Dropdown

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (butir "Env var" di `suite.md`); password tidak ditulis di spec atau fixture.
- Data: Tab Session SS-01 sampai SS-11 (Pre-setup #11), seperti tabel di bawah Spec hanya membaca dan tidak mengubah data.
- Hook `after` spec ini mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan data Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

| Baris | User (nama lengkap) | Employee ID | Position | Division | Note | Tanggal (Asia/Jakarta) |
|---|---|---|---|---|---|---|
| SS-01 | John Doe | EMP001 | Staff | Marketing | Session started | 14/07/26 08:05 |
| SS-02 | John Doe | EMP001 | Staff | Marketing | Session ended | 14/07/26 09:30 |
| SS-03 | Siti Nurbaya (tampil `Siti N`) | EMP002 | Manager | Finance | Concurrent limit reached | 14/07/26 10:00 |
| SS-04 | Mike Tan | EMP003 | Staff | Operations | Logged out by admin | 14/07/26 14:00 |
| SS-05 | Jane Smith | kosong | kosong | Finance | Session started | 15/07/26 08:00 |
| SS-06 | Budi Santoso (tampil `Budi S`) | EMP004 | Supervisor | Operations | Session started | 15/07/26 09:00 |
| SS-07 | Dewi Lestari | EMP005 | Staff | Marketing | Session started | 15/07/26 10:00 |
| SS-08 | Hendra Pratama (pengguna pertama) | EMP006 | Staff | Marketing | Session started | 15/07/26 11:00 |
| SS-09 | Hendra Pratama (pengguna kedua) | EMP007 | Manager | Finance | Session started | 15/07/26 12:00 |
| SS-10 | John Dalton | EMP008 | Staff | Operations | Session started | 16/07/26 08:00 |
| SS-11 | John Davis | EMP009 | Supervisor | Finance | Session ended | 16/07/26 09:00 |

## Test Steps

### TC-FA-FAAL-77: Filter Position, Division, dan Note Tab Session menyaring baris

1. Klik icon Filter
2. Pilih `Supervisor` pada field Position
3. Klik `[Apply]`
4. Verifikasi SS-06 dan SS-11 tampil
5. Klik `[Clear Field]`
6. Klik `[Apply]`
7. Pilih `Finance` pada field Division
8. Klik `[Apply]`
9. Verifikasi SS-03, SS-05, SS-09, dan SS-11 tampil
10. Klik `[Clear Field]`
11. Klik `[Apply]`
12. Pilih `Concurrent limit reached` pada field Note
13. Klik `[Apply]`
14. Verifikasi hanya SS-03 tampil
15. Klik `[Clear Field]`
16. Klik `[Apply]`

### TC-FA-FAAL-78: Opsi dropdown filter Position, Division, dan Note berasal dari data tabel

17. Buka dropdown Position
18. Verifikasi dropdown Position berisi tepat `Manager`, `Staff`, `Supervisor` (tanpa opsi untuk nilai kosong)
19. Tutup dropdown Position
20. Buka dropdown Division
21. Verifikasi dropdown Division berisi tepat `Finance`, `Marketing`, `Operations`
22. Tutup dropdown Division
23. Buka dropdown Note
24. Verifikasi dropdown Note berisi tepat `Concurrent limit reached`, `Logged out by admin`, `Session ended`, `Session started`
25. Tutup dropdown Note

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): langkah 5, 6, 10, 11, 15, 16, 19, 22, 25 (mengosongkan field dan menerapkannya setelah tiap keyword, menutup dropdown).
- Temuan untuk QA:
  - TC sumber tidak menyatakan apakah Filter Panel tetap terbuka setelah `[Apply]`. Spec mengikuti pola TC-FA-FAAL-77 (`[Clear Field]` dan `[Apply]` berurutan tanpa membuka ulang panel).
