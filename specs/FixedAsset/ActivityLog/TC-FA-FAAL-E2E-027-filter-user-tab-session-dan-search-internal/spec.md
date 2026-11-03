---
id: TC-FA-FAAL-E2E-027-filter-user-tab-session-dan-search-internal
title: "Filter User Tab Session: Opsi per Nama Lengkap, Dua Pengguna Bernama Sama, dan Search Internal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-81
  - TC-FA-FAAL-82
  - TC-FA-FAAL-83
coverage:
  web: automated
---

# Filter User Tab Session: Opsi per Nama Lengkap, Dua Pengguna Bernama Sama, dan Search Internal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (butir "Env var" di `suite.md`); password tidak ditulis di spec atau fixture.
- Data: Tab Session SS-01 sampai SS-11 (Pre-setup #11), seperti tabel di bawah; SS-08 dan SS-09 berasal dari dua pengguna berbeda yang bernama `Hendra Pratama`. Spec hanya membaca dan tidak mengubah data.
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

### TC-FA-FAAL-81: Opsi filter User Tab Session: satu opsi per nama lengkap

1. Klik icon Filter
2. Buka dropdown User
3. Verifikasi opsi berlabel nama lengkap: `Budi Santoso`, `Dewi Lestari`, `Hendra Pratama`, `Jane Smith`, `John Dalton`, `John Davis`, `John Doe`, `Mike Tan`, `Siti Nurbaya` (sembilan opsi)
4. Verifikasi `Hendra Pratama` muncul sebagai satu opsi walau SS-08 dan SS-09 berasal dari dua pengguna berbeda
5. Tutup dropdown User

### TC-FA-FAAL-82: Filter User Tab Session menyaring baris, termasuk dua pengguna bernama sama

6. Pilih `Hendra Pratama` pada field User
7. Klik `[Apply]`
8. Verifikasi SS-08 dan SS-09 tampil
9. Klik `[Clear Field]`
10. Klik `[Apply]`
11. Pilih `John Doe` pada field User
12. Klik `[Apply]`
13. Verifikasi SS-01 dan SS-02 tampil
14. Klik `[Clear Field]`
15. Klik `[Apply]`

### TC-FA-FAAL-83: Search internal dropdown filter User

16. Buka dropdown User
17. Ketik `jo` pada kotak cari di dalam dropdown
18. Verifikasi hanya `John Dalton`, `John Davis`, `John Doe` tampil sebagai opsi
19. Ganti isi kotak cari dalam dropdown dengan `JO`
20. Verifikasi opsi yang tampil sama dengan hasil `jo`: hanya `John Dalton`, `John Davis`, `John Doe`
21. Ganti isi kotak cari dalam dropdown dengan `zzz`
22. Verifikasi teks `No results found` tampil tanpa ilustrasi

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): langkah 5, 9, 10, 14, 15 (menutup dropdown, mengosongkan field User dan menerapkannya).
- Temuan untuk QA:
  - TC sumber tidak menyatakan apakah Filter Panel tetap terbuka setelah `[Apply]`. Spec mengikuti pola TC-FA-FAAL-77 (`[Clear Field]` dan `[Apply]` berurutan tanpa membuka ulang panel).
  - TC-FA-FAAL-81 dan TC-FA-FAAL-82 tidak menyebut dasar penggabungan dua pengguna bernama sama menjadi satu opsi filter (nama lengkap); spec hanya mengasersi hasil yang disebut Expected.
