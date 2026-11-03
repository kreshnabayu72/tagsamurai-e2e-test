---
id: TC-FA-SU-E2E-121-tabel-user-list-filter-dan-kontrol-filter-bagian-2
title: "Tabel User List: Filter dan Kontrol Filter (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-343
  - TC-FA-SU-344
  - TC-FA-SU-345
coverage:
  web: automated
---

# Tabel User List: Filter dan Kontrol Filter (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Spec ini hanya membaca data Pre-setup dan tidak mengubahnya; suite berjalan serial (`parallel: false`).
- Tabel `Filter FK`:

| Field | Nilai | Opsi | Hasil |
|---|---|---|---|
| Home Group | `Branch Surabaya` | `Branch Surabaya`, `Finance & Accounting`, `General Affairs`, `IT Infrastructure`, `Logistics Warehouse` | `Eka Wulandari`, `Fajar Nugroho`, `Lukman Hakim`, `Umar Faruq` (4 baris) |
| Position | `Accountant` | `Accountant`, `AP Staff`, `Branch Admin`, `Branch Staff`, `Finance Auditor`, `Finance Lead`, `Finance Manager`, `Finance Staff` | `Gita Permata` (1 baris) |
| Division | `Finance & Accounting` | `Finance & Accounting`, `General Affairs`, `Information Technology`, `Logistics`, `Operations` | `Budi Santoso`, `Gita Permata`, `Mira Anggraini`, `Nanda Pratama`, `Putri Anggraeni`, `Sinta Dewi` (7 baris) |
| Modified By | `Ahmad D` | `Ahmad D`, `Budi S`, `System` | `Budi Santoso`, `Citra Lestari`, `Eka Wulandari`, `Gita Permata`, `Hana Kusuma`, `Lina Marlina` (17 baris) |

- Tabel `Filter Date`:

| Field | Rentang | Hasil |
|---|---|---|
| Last Updated | 10/06/26 sampai 15/07/26 | `Ahmad Dahlan`, `Budi Santoso` (2 baris) |
| Temporary Until | 31/12/26 sampai 31/12/26 | `Fajar Nugroho` (1 baris) |


## Test Steps

1. Klik icon Filter

### TC-FA-SU-343: Filter kelas fk

2. Untuk setiap baris tabel `Filter FK` di Prerequisites (langkah 3 sampai 9):
3. Buka dropdown <Field>
4. Verifikasi opsi dropdown <Field> = DISTINCT data tabel (<Opsi>)
5. Centang <Nilai>
6. Klik `[Apply]`
7. Verifikasi memilih <Nilai> menyisakan <Hasil>
8. Verifikasi chip <Nilai> tampil di dalam field <Field>
9. Klik `[Clear Field]` pada field <Field> lalu `[Apply]`

### TC-FA-SU-344: Filter kelas date

10. Untuk setiap baris tabel `Filter Date` di Prerequisites (langkah 11 sampai 14):
11. Pilih rentang <Rentang> pada <Field>
12. Klik `[Apply]`
13. Verifikasi rentang inklusif <Rentang> pada <Field> menyisakan <Hasil>
14. Klik `[Clear Field]` pada field <Field> lalu `[Apply]`

### TC-FA-SU-345: Filter kelas cf Shift

15. Buka dropdown Shift
16. Verifikasi opsi dropdown Shift = DISTINCT data tabel (`Morning`, `Night`)
17. Centang `Morning`
18. Klik `[Apply]`
19. Verifikasi memilih `Morning` menyisakan `Ahmad Dahlan`, `Budi Santoso`, `Doni Prasetyo`, `Fajar Nugroho`, `Gita Permata`, `Lina Marlina` (13 baris)
20. Verifikasi chip `Morning` tampil di dalam field Shift
21. Klik `[Clear Field]` pada field Shift lalu `[Apply]`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1 (membuka panel Filter) dan 21 (membersihkan Filter, S-09).
- Langkah yang diulang: langkah 3 sampai 9 (empat field) dan langkah 11 sampai 14 (dua field tanggal), parameter pada tabel Prerequisites. Panel Filter tetap terbuka antar blok.
- Temuan untuk QA (S-15): (1) Daftar nama pada Expected TC berupa baris teratas hasil (kurang dari jumlah baris yang disebut atau dari ukuran halaman); spec mengasersi daftar nama itu dan jumlah baris sebagaimana tertulis.
- Alasan di atas sekitar 35 langkah (ekspansi perulangan dihitung): seluruh blok berkelas fungsional yang sama pada halaman, akun, dan dataset Pre-setup #20 yang sama tanpa mengubah data; langkah berulang per kolom atau field berpola identik (langkah 3 sampai 9, langkah 11 sampai 14) dan kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna; bagian 3 konvensi menetapkan Setup Column, Bulk Action Bar, dan Search, Filter, Sort tetap satu spec selama dataset dan harness sama, sedangkan pemecahan hanya menambah login, hook, dan pembukaan halaman.
