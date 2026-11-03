---
id: TC-AC-SU-E2E-205-tab-system-log-filter-panel-or-dalam-field-dan-antar-field
title: "Tab System Log: Filter Panel, OR di dalam Satu Field dan AND antar Field"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-417
coverage:
  web: automated
---

# Tab System Log: Filter Panel, OR di dalam Satu Field dan AND antar Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE): user `Jane Smith {runId}-205` (email `janesmith+{runId}-205@qwertysystem.net`) sebagai aktor dengan 5 entri System Log:

| Entri | Action | Object | Name | Field |
|---|---|---|---|---|
| M1 | Deactivate | User | John Doe {runId}-205 | Status |
| M2 | Resend Activation Email | User | Sarah Lee {runId}-205 | Activation Email |
| M3 | Assign | Total Control | Rina Putri {runId}-205 | Access Level |
| M4 | Edit | Global Role | Jane Smith {runId}-205 | Manage group — Update |
| M5 | Assign | Global Role | John Doe {runId}-205 | Access Level |

- Kemampuan teknis: kemampuan seed entri System Log disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

1. Cari `Jane Smith {runId}-205` di Search pada User List, tekan Enter, lalu buka Detail user tersebut
2. Klik tab `System Log`

### TC-AC-SU-417: OR di dalam satu field, AND antar field

3. Klik icon Filter
4. Pilih `Assign` dan `Edit` di field `Action`
5. Klik `[Apply]`
6. Verifikasi sedikitnya satu baris tampil
7. Verifikasi setiap baris yang tampil memiliki Action `Assign` atau `Edit`
8. Klik icon Filter
9. Tambah `Global Role` di field `Object`
10. Klik `[Apply]`
11. Verifikasi sedikitnya satu baris tampil
12. Verifikasi setiap baris yang tampil memiliki Action `Assign` atau `Edit` dan Object `Global Role`
13. Klik icon Filter
14. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah pembuka yang mencari user target lewat Search pada User List lalu membuka Detail adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji. `[Clear Field]` lalu `[Apply]` mengosongkan Filter (S-09).
- Pembagian TC Filter Panel Tab System Log: TC-AC-SU-414 dan 415 di spec 116, TC-AC-SU-416 di spec 204, TC-AC-SU-417 di spec ini.
- Temuan untuk QA:
  - Perilaku Filter Panel setelah `[Apply]` (tetap terbuka atau menutup) tidak dinyatakan di TC. Spec mengasumsikan panel menutup setelah Apply dan membukanya lagi dengan klik icon Filter.
  - Cara men-seed entri System Log (Date, Action, Object, Name, Field, Old Value, New Value, aktor, termasuk snapshot full path untuk Object `Group`) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
