---
id: TC-AC-SU-E2E-116-tab-system-log-filter-panel-screening-opsi-dan-kombinasi
title: "Tab System Log: Filter Panel (Screening dan Isi Opsi Dropdown)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-414
  - TC-AC-SU-415
coverage:
  web: automated
---

# Tab System Log: Filter Panel (Screening dan Isi Opsi Dropdown)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE): user `Jane Smith {runId}-116` (email `janesmith+{runId}-116@qwertysystem.net`) sebagai aktor dengan 5 entri System Log:

| Entri | Action | Object | Name | Field |
|---|---|---|---|---|
| M1 | Deactivate | User | John Doe {runId}-116 | Status |
| M2 | Resend Activation Email | User | Sarah Lee {runId}-116 | Activation Email |
| M3 | Assign | Total Control | Rina Putri {runId}-116 | Access Level |
| M4 | Edit | Global Role | Jane Smith {runId}-116 | Manage group — Update |
| M5 | Assign | Global Role | John Doe {runId}-116 | Access Level |

| Opsi dropdown | Opsi yang tampil (nilai DISTINCT seeding) |
|---|---|
| Action | Deactivate, Resend Activation Email, Assign, Edit |
| Object | User, Total Control, Global Role |
| Name | John Doe {runId}-116, Sarah Lee {runId}-116, Rina Putri {runId}-116, Jane Smith {runId}-116 |
| Field | Status, Activation Email, Access Level, Manage group — Update |

- Kemampuan teknis: kemampuan seed entri System Log disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-414: Screening Filter Panel Tab System Log

1. Cari `Jane Smith {runId}-116` di Search pada User List, tekan Enter, lalu buka Detail user tersebut
2. Klik tab `System Log`
3. Hover icon Filter
4. Verifikasi tooltip `Filter` tampil
5. Klik icon Filter
6. Verifikasi Filter Panel terbuka di bawah toolbar
7. Verifikasi field Filter Panel berurutan `Date`, `Action`, `Object`, `Name`, `Field`
8. Verifikasi field `Date` berupa date range picker dengan placeholder `Select date`
9. Verifikasi field `Action` berupa multi-select searchable dengan placeholder `All actions`
10. Verifikasi field `Object` berupa multi-select searchable dengan placeholder `All objects`
11. Verifikasi field `Name` berupa multi-select searchable dengan placeholder `All names`
12. Verifikasi field `Field` berupa multi-select searchable dengan placeholder `All fields`
13. Verifikasi footer panel menampilkan link `[Clear Field]` di kiri dan `[Apply]` di kanan

### TC-AC-SU-415: Isi opsi dropdown Filter Tab System Log

14. Buka dropdown field pada baris tabel 'Opsi dropdown'
15. Verifikasi opsi dropdown sama dengan nilai DISTINCT pada kolom 'Opsi yang tampil' baris tabel itu
16. Verifikasi jumlah opsi sama dengan jumlah nilai DISTINCT itu (tidak ada opsi di luar daftar)
17. Tutup dropdown
18. Klik icon Filter untuk menutup Filter Panel

## Notes

- Langkah pembuka yang mencari user target lewat Search pada User List lalu membuka Detail adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- Langkah berulang per baris tabel: langkah 14 sampai 17 (tabel 'Opsi dropdown', 4 field; 13 langkah nominal + 4 x 4 + 1 = sekitar 30 dengan ekspansi). Menutup dropdown dan membuka-menutup Filter Panel adalah langkah penghubung.
- Pembagian TC Filter Panel Tab System Log: TC-AC-SU-414 dan 415 di spec ini, TC-AC-SU-416 di spec 204, TC-AC-SU-417 di spec 205.
- Temuan untuk QA:
  - TC-415 'nilai yang tidak ada di baris tabel tidak muncul' tidak menyebut contoh nilai; spec mengasersi jumlah opsi sama dengan jumlah nilai DISTINCT.
  - TC-415 memuat `Jane Smith` sebagai nilai Name pada System Log milik Jane Smith sendiri (entri tentang dirinya); spec memakai `Jane Smith {runId}-116` sebagai Name pada entri M4.
  - Cara men-seed entri System Log (Date, Action, Object, Name, Field, Old Value, New Value, aktor, termasuk snapshot full path untuk Object `Group`) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
