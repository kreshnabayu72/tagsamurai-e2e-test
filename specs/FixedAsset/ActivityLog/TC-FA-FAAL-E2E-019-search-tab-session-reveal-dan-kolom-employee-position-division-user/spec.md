---
id: TC-FA-FAAL-E2E-019-search-tab-session-reveal-dan-kolom-employee-position-division-user
title: "Search Tab Session: Reveal Input dan Kolom Employee ID, Position, Division, serta User"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-57
  - TC-FA-FAAL-59
  - TC-FA-FAAL-60
coverage:
  web: automated
---

# Search Tab Session: Reveal Input dan Kolom Employee ID, Position, Division, serta User

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (butir "Env var" di `suite.md`); password tidak ditulis di spec atau fixture.
- Data: Tab Session SS-01 sampai SS-11 (Pre-setup #11), seperti tabel di bawah; spec hanya membaca dan tidak mengubah data. Search dikosongkan antar-kasus oleh langkah spec.
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

### TC-FA-FAAL-57: Search Tab Session: reveal input, autofocus, dan placeholder

1. Klik icon Search
2. Verifikasi input Search terbuka
3. Verifikasi kursor langsung fokus di dalam input Search
4. Verifikasi placeholder input Search `Search user, employee ID, or note...`
5. Klik `(←)` pada kotak Search

### TC-FA-FAAL-59: Search kolom Employee ID, Position, dan Division Tab Session: substring dan case-insensitive

6. Ketik Search `P007`, tekan Enter
7. Verifikasi hanya SS-09 (EMP007) tampil
8. Kosongkan isi kotak search, tekan Enter
9. Ketik Search `p007`, tekan Enter
10. Verifikasi hanya SS-09 (EMP007) tampil
11. Kosongkan isi kotak search, tekan Enter
12. Ketik Search `superv`, tekan Enter
13. Verifikasi SS-06 dan SS-11 tampil
14. Kosongkan isi kotak search, tekan Enter
15. Ketik Search `SUPERV`, tekan Enter
16. Verifikasi SS-06 dan SS-11 tampil
17. Kosongkan isi kotak search, tekan Enter
18. Ketik Search `inanc`, tekan Enter
19. Verifikasi SS-03, SS-05, SS-09, dan SS-11 tampil
20. Kosongkan isi kotak search, tekan Enter
21. Ketik Search `INANC`, tekan Enter
22. Verifikasi SS-03, SS-05, SS-09, dan SS-11 tampil
23. Klik `(←)` pada kotak Search

### TC-FA-FAAL-60: Search kolom User Tab Session mencocokkan nama lengkap

24. Ketik Search `Santoso`, tekan Enter
25. Verifikasi SS-06 tampil sebagai `Budi S` (nama singkat tidak mengandung kata Santoso)
26. Kosongkan isi kotak search, tekan Enter
27. Ketik Search `santoso`, tekan Enter
28. Verifikasi SS-06 tampil sebagai `Budi S` (nama singkat tidak mengandung kata Santoso)
29. Kosongkan isi kotak search, tekan Enter
30. Ketik Search `Nurbaya`, tekan Enter
31. Verifikasi SS-03 tampil sebagai `Siti N`
32. Kosongkan isi kotak search, tekan Enter
33. Ketik Search `John`, tekan Enter
34. Verifikasi SS-01, SS-02, SS-10, dan SS-11 tampil
35. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): langkah 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35 (mengosongkan atau menutup kotak Search sebelum kasus atau keyword berikutnya). Penutupan lewat `(←)` mereset tabel.
- TC-FA-FAAL-58 (siklus Enter, Clear, dan Collapse) ada di spec 067.
- Search yang mencocokkan baris ditulis "Ketik Search `X`, tekan Enter" (bagian 8b butir 9); TC-FA-FAAL-57 memakai "Klik icon Search" eksplisit karena menguji reveal input.
- Temuan untuk QA:
  - TC-FA-FAAL-57 Expected a ("terbuka dengan kursor langsung fokus") memuat dua klausa; spec memecahnya menjadi dua `Verifikasi` (S-01).
  - TC-FA-FAAL-59 dan TC-FA-FAAL-60 menyebut hasil dua keyword (`P007` dan `p007`, `Santoso` dan `santoso`) dalam satu butir Expected; spec mengasersi hasil tiap keyword.
