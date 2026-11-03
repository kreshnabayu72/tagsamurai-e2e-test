---
id: TC-FA-FAAL-E2E-023-filter-date-tab-session
title: "Filter Date Tab Session: Screening Panel, Satu Hari, dan Rentang"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-70
  - TC-FA-FAAL-71
  - TC-FA-FAAL-72
coverage:
  web: automated
---

# Filter Date Tab Session: Screening Panel, Satu Hari, dan Rentang

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (butir "Env var" di `suite.md`); password tidak ditulis di spec atau fixture.
- Data: Tab Session SS-01 sampai SS-11 (Pre-setup #11), seperti tabel di bawah. Spec hanya membaca dan tidak mengubah data.
- Filter Panel diasumsikan tetap terbuka setelah `[Apply]` (lihat Temuan untuk QA).
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

### TC-FA-FAAL-70: Screening Filter Panel Tab Session

1. Klik icon Filter
2. Verifikasi panel tampil di bawah Toolbar
3. Verifikasi icon Filter berubah gelap
4. Verifikasi field berurutan dari kiri ke kanan sesuai urutan kolom tabel: `Date`, `User`, `Position`, `Division`, `Note`
5. Verifikasi field `Date` berupa date range picker dengan placeholder `Select date`
6. Verifikasi field `User` berupa multi-select searchable dengan placeholder `All users`
7. Verifikasi field `Position` berupa multi-select searchable dengan placeholder `All positions`
8. Verifikasi field `Division` berupa multi-select searchable dengan placeholder `All divisions`
9. Verifikasi field `Note` berupa multi-select searchable dengan placeholder `All notes`
10. Verifikasi tidak ada nilai ter-pilih pada kelima field
11. Verifikasi empat field berada pada baris pertama dan satu field pada baris kedua
12. Verifikasi tombol `[Clear Field]` di kiri dan `[Apply]` di kanan
13. Verifikasi tidak ada field Employee ID, Activity, Status, IP Address, maupun Device/Browser

### TC-FA-FAAL-71: Filter Date satu hari di Tab Session

14. Pilih tanggal mulai `14/07/26` dan tanggal akhir `14/07/26` pada field Date
15. Klik `[Apply]`
16. Verifikasi hanya SS-01, SS-02, SS-03, dan SS-04 tampil
17. Verifikasi icon Filter menampilkan badge titik
18. Klik `[Clear Field]`
19. Klik `[Apply]`

### TC-FA-FAAL-72: Filter Date rentang Start berbeda dari End di Tab Session

20. Pilih tanggal mulai `14/07/26` dan tanggal akhir `15/07/26` pada field Date
21. Klik `[Apply]`
22. Verifikasi SS-01 sampai SS-09 tampil (sembilan baris)
23. Verifikasi SS-10 dan SS-11 tidak tampil

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): langkah 18, 19 (mengosongkan field Date dan menerapkannya sebelum TC-FA-FAAL-72).
- Langkah 1 TC-FA-FAAL-71 dan TC-FA-FAAL-72 ("Klik icon Filter") dipenuhi panel yang sudah terbuka dari TC-FA-FAAL-70 dan tidak diulang agar icon Filter tidak menutup panel.
- Temuan untuk QA:
  - TC sumber tidak menyatakan apakah Filter Panel tetap terbuka setelah `[Apply]`. Spec mengikuti pola TC-FA-FAAL-77 (`[Clear Field]` dan `[Apply]` berurutan tanpa membuka ulang panel).
  - TC-FA-FAAL-70 Expected b menggabungkan urutan, tipe kontrol, placeholder, dan keadaan tanpa nilai; spec memecahnya per field (tipe kontrol dan placeholder satu klausa, S-01).
