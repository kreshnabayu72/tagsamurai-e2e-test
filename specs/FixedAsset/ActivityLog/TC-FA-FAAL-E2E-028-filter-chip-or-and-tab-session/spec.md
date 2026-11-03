---
id: TC-FA-FAAL-E2E-028-filter-chip-or-and-tab-session
title: "Filter Tab Session: Logika OR, Chip, dan Hapus Chip"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-84
  - TC-FA-FAAL-85
  - TC-FA-FAAL-86
  - TC-FA-FAAL-87
coverage:
  web: automated
---

# Filter Tab Session: Logika OR, Chip, dan Hapus Chip

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (butir "Env var" di `suite.md`); password tidak ditulis di spec atau fixture.
- Data: Tab Session SS-01 sampai SS-11 (Pre-setup #11), seperti tabel di bawah. Spec hanya membaca dan tidak mengubah data.
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

### TC-FA-FAAL-84: Dua opsi dalam satu field filter memakai logika OR

1. Klik icon Filter
2. Pilih `Finance` dan `Marketing` pada field Division
3. Klik `[Apply]`
4. Verifikasi delapan baris tampil: SS-01, SS-02, SS-03, SS-05, SS-07, SS-08, SS-09, SS-11
5. Verifikasi baris Operations (SS-04, SS-06, SS-10) tidak tampil

### TC-FA-FAAL-85: Chip opsi terpilih tampil di dalam field filter

6. Klik `[Clear Field]`
7. Buka dropdown Division
8. Centang `Finance`
9. Verifikasi satu chip `Finance` tampil di dalam field Division
10. Centang `Marketing`
11. Verifikasi chip kedua `Marketing` tampil di samping chip `Finance` (tidak menggantikan)

### TC-FA-FAAL-86: Hapus chip lewat tombol silang menghapus centang opsi

12. Tutup dropdown Division
13. Klik `(✕)` pada chip `Finance` tanpa membuka dropdown
14. Verifikasi chip `Finance` hilang
15. Verifikasi chip `Marketing` tetap ada
16. Buka dropdown Division
17. Verifikasi checkbox `Finance` di dalam dropdown tidak tercentang
18. Verifikasi checkbox `Marketing` di dalam dropdown tercentang
19. Tutup dropdown Division
20. Klik `[Apply]`
21. Verifikasi hanya SS-01, SS-02, SS-07, SS-08 tampil

### TC-FA-FAAL-87: Hapus centang di dalam dropdown menghapus chip

22. Klik `[Clear Field]`
23. Buka dropdown Division
24. Centang `Finance`
25. Centang `Marketing`
26. Hilangkan centang `Marketing` dari dalam dropdown
27. Tutup dropdown Division
28. Verifikasi chip `Marketing` hilang dari field Division
29. Verifikasi chip `Finance` tetap ada

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): langkah 6, 12, 19, 22, 27 (mengosongkan field sebelum TC berikutnya, menutup dropdown). `[Clear Field]` tanpa `[Apply]` dipakai bila TC berikutnya tidak mengasersi tabel; `[Apply]` TC-FA-FAAL-86 menimpa filter sebelumnya.
- Langkah 1 TC-FA-FAAL-85, 86, dan 87 ("Klik icon Filter") dipenuhi Filter Panel yang sudah terbuka dari TC-FA-FAAL-84.
- Temuan untuk QA:
  - TC sumber tidak menyatakan apakah Filter Panel tetap terbuka setelah `[Apply]`. Spec mengikuti pola TC-FA-FAAL-77 (`[Clear Field]` dan `[Apply]` berurutan tanpa membuka ulang panel).
  - TC-FA-FAAL-86 langkah 1 ("pilih Finance dan Marketing") dipenuhi state akhir TC-FA-FAAL-85 (kedua chip sudah ada); spec tidak mengulang pemilihan agar centang tidak terbalik.
