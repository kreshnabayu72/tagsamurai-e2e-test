---
id: TC-FA-FAAL-E2E-086-filter-tab-session-state-dropdown-position-loading-kosong-tanpa-hasil
title: "Filter Tab Session: State Loading, Sumber Kosong, dan Tanpa Hasil pada Dropdown Position"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-80
coverage:
  web: automated
---

# Filter Tab Session: State Loading, Sumber Kosong, dan Tanpa Hasil pada Dropdown Position

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (butir "Env var" di `suite.md`); password tidak ditulis di spec atau fixture.
- Data: Tab Session SS-01 sampai SS-11 (Pre-setup #11), seperti tabel di bawah; client tanpa riwayat sesi dan tanpa log aksi FAMS (Pre-setup #13) untuk langkah 10. Akun Total Control client itu tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE. Spec hanya membaca dan tidak mengubah data.
- Kemampuan teknis: `Spectra.intercept()` menunda respons opsi dropdown Position (langkah 2) dan melepasnya (langkah 5). Endpoint opsi dropdown tidak tertulis di TC; disediakan tim FE (S-13). Intercept dilepas dan dipulihkan di hook `after` bila spec gagal di tengah.
- Hook `after` spec ini mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan data Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

Tabel Data Tab Session berikut adalah precondition TC-FA-FAAL-80 dan tidak diasersi di spec ini:

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

### TC-FA-FAAL-80: State loading, sumber kosong, dan tanpa hasil pada dropdown filter

1. Klik icon Filter
2. Tunda respons opsi dropdown Position lewat intercept jaringan
3. Buka dropdown Position
4. Verifikasi dropdown Position menampilkan skeleton atau spinner mini selama penundaan
5. Lepas penundaan respons opsi dropdown Position
6. Ketik `zzz` pada kotak cari di dalam dropdown Position
7. Verifikasi teks `No results found` tampil tanpa ilustrasi
8. Tutup dropdown Position
9. Ganti akun: Logout dari akun Total Control
10. Login sebagai Total Control pada client tanpa riwayat sesi (Pre-setup #13)
11. Buka Fixed Asset > Reports & Logs > Activity Log pada client tersebut
12. Klik icon Filter
13. Buka dropdown Position
14. Verifikasi dropdown Position menampilkan teks `No options available`

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): langkah 1, 5, 8, 9, 10, 11 (membuka Filter Panel, melepas intercept, menutup dropdown, ganti akun, dan membuka layar untuk akun client #13). Ganti akun pada langkah 10 bersifat eksplisit (S-07).
- Intercept pada TC-FA-FAAL-80 hanya menahan respons untuk mengamati state UI (skeleton atau spinner mini); ini bukan kelas b (bagian 3 prinsip 13).
- Temuan untuk QA:
  - TC-FA-FAAL-80 tidak menyebut akun dan client untuk Pre-setup #13; spec mengasumsikan akun Total Control client itu disediakan tim FE.
  - TC-FA-FAAL-80 tidak menyebut endpoint opsi dropdown yang ditunda; kebutuhan intercept ditulis tanpa endpoint (S-13).
