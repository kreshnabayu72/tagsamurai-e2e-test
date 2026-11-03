---
id: TC-AC-SU-E2E-204-tab-system-log-filter-panel-satu-opsi-per-field
title: "Tab System Log: Filter Panel, Filter Satu Opsi per Field Multi-select"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-416
coverage:
  web: automated
---

# Tab System Log: Filter Panel, Filter Satu Opsi per Field Multi-select

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE): user `Jane Smith {runId}-204` (email `janesmith+{runId}-204@qwertysystem.net`) sebagai aktor dengan 5 entri System Log:

| Entri | Action | Object | Name | Field |
|---|---|---|---|---|
| M1 | Deactivate | User | John Doe {runId}-204 | Status |
| M2 | Resend Activation Email | User | Sarah Lee {runId}-204 | Activation Email |
| M3 | Assign | Total Control | Rina Putri {runId}-204 | Access Level |
| M4 | Edit | Global Role | Jane Smith {runId}-204 | Manage group — Update |
| M5 | Assign | Global Role | John Doe {runId}-204 | Access Level |

| Filter satu opsi | Opsi dipilih |
|---|---|
| Action | Assign |
| Object | User |
| Name | John Doe {runId}-204 |
| Field | Status |

- Kemampuan teknis: kemampuan seed entri System Log disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

1. Cari `Jane Smith {runId}-204` di Search pada User List, tekan Enter, lalu buka Detail user tersebut
2. Klik tab `System Log`

### TC-AC-SU-416: Filter field multi-select, satu opsi per field

3. Klik icon Filter
4. Pilih opsi pada kolom 'Opsi dipilih' di field pada baris tabel 'Filter satu opsi'
5. Klik `[Apply]`
6. Verifikasi sedikitnya satu baris tampil
7. Verifikasi setiap baris yang tampil memiliki nilai field itu sama dengan opsi yang dipilih
8. Verifikasi icon Filter menampilkan badge titik
9. Klik icon Filter
10. Klik `[Clear Field]`, lalu klik `[Apply]`
11. Verifikasi tabel kembali menampilkan semua baris (jumlah baris sama dengan sebelum Filter)
12. Verifikasi badge titik pada icon Filter hilang

## Notes

- Langkah pembuka yang mencari user target lewat Search pada User List lalu membuka Detail adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- Langkah berulang per baris tabel: langkah 3 sampai 12 (tabel 'Filter satu opsi', 4 field). `[Clear Field]` lalu `[Apply]` mengosongkan Filter (S-09); membuka-menutup Filter Panel adalah langkah penghubung.
- Ukuran spec: 12 langkah nominal, sekitar 42 dengan ekspansi blok berulang (2 + 10 x 4), di atas smell sekitar 35 langkah. Spec memuat satu TC (TC-AC-SU-416) dengan satu pola yang diulang untuk empat field; TC tidak dibelah antar spec, dan tiap iterasi field berdiri sendiri karena Filter dikosongkan di akhir iterasi.
- Pembagian TC Filter Panel Tab System Log: TC-AC-SU-414 dan 415 di spec 116, TC-AC-SU-416 di spec ini, TC-AC-SU-417 di spec 205.
- Temuan untuk QA:
  - TC-416 meminta `[Clear Field]` + `[Apply]` tanpa menyatakan apakah dilakukan pada panel yang dibuka ulang; spec membuka ulang panel.
  - Perilaku Filter Panel setelah `[Apply]` (tetap terbuka atau menutup) tidak dinyatakan di TC. Spec mengasumsikan panel menutup setelah Apply dan membukanya lagi dengan klik icon Filter.
  - Cara men-seed entri System Log (Date, Action, Object, Name, Field, Old Value, New Value, aktor, termasuk snapshot full path untuk Object `Group`) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
