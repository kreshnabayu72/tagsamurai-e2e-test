---
id: TC-FA-FAAL-E2E-080-search-trim-spasi-kedua-tab
title: "Search Men-trim Spasi Awal dan Akhir Query di Kedua Tab"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAL-68
coverage:
  web: automated
---

# Search Men-trim Spasi Awal dan Akhir Query di Kedua Tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (butir "Env var" di `suite.md`); password tidak ditulis di spec atau fixture.
- Data: Tab Session SS-01 sampai SS-11 (Pre-setup #11), seperti tabel di bawah; Tab User Action UA-01 sampai UA-15 (Pre-setup #12), baris dipakai UA-01 (Name `Budi Santoso`). Spec hanya membaca dan tidak mengubah data.
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

### TC-FA-FAAL-68: Search men-trim spasi awal dan akhir query di kedua tab

1. Klik icon Filter
2. Pilih tanggal mulai `14/07/26` dan tanggal akhir `16/07/26` pada field Date
3. Klik `[Apply]`
4. Ketik Search `  Budi  ` (spasi di awal dan akhir), tekan Enter
5. Verifikasi hanya SS-06 tampil
6. Verifikasi isi input Search tetap `  Budi  ` (sama dengan yang diketik)
7. Klik `✕` pada Search
8. Ketik Search `  ` (hanya spasi), tekan Enter
9. Verifikasi query hanya spasi diperlakukan sebagai kosong: tabel kembali menampilkan 11 baris dengan teks pagination `Showing 1–10 of 11 entries`
10. Klik `(←)` pada kotak Search
11. Klik tab User Action
12. Klik icon Filter
13. Pilih tanggal mulai `18/06/26` dan tanggal akhir `18/06/26` pada field Date
14. Klik `[Apply]`
15. Ketik Search `  Santoso  `, tekan Enter
16. Verifikasi hanya UA-01 tampil

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- TC-FA-FAAL-65 sampai 67 ada di spec 021.
- Langkah penghubung (S-03): langkah 1 sampai 3 dan 12 sampai 14 (menerapkan Filter Date Jendela Seed pada tiap tab sesuai precondition d TC-FA-FAAL-68), langkah 7 dan 10 (mengosongkan atau menutup kotak Search).
- TC-FA-FAAL-68 mencantumkan TC-FA-FAAL-58 sebagai dependensi; langkah TC-FA-FAAL-68 mandiri atas data Pre-setup #11 dan #12, sedangkan siklus Search TC-FA-FAAL-58 ada di spec 067 dan tidak diulang.
- Temuan untuk QA:
  - Pre-setup #11 menyebut tepat 11 baris Tab Session (dan #12 tepat 15 baris Tab User Action) tanpa menyatakan bahwa login aktor (dan spec lain pada client yang sama) menambah baris `Session started` pada log permanen. Asersi hitungan (`Showing 1–10 of 11 entries`) hanya benar bila data Pre-setup berada di client yang terisolasi dari login lain; spec mengikuti TC.
  - TC-FA-FAAL-68 langkah 2 memakai "Kosongkan input" sebelum mengetik query spasi; spec menulis "Klik `✕` pada Search" sebagai langkah penghubung yang mengosongkan kotak sebelum "Ketik Search ..., tekan Enter" (bagian 8b butir 9).
  - TC-FA-FAAL-68 tidak menyebut jumlah baris untuk kasus query hanya spasi selain "11 baris kembali tampil"; spec memakai teks pagination `Showing 1–10 of 11 entries`.
