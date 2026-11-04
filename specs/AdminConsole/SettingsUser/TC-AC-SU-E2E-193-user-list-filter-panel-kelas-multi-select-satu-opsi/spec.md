---
id: TC-AC-SU-E2E-193-user-list-filter-panel-kelas-multi-select-satu-opsi
title: "User List Filter Panel: Filter Kelas Multi-Select Satu Opsi per Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-274
coverage:
  web: automated
---

# User List Filter Panel: Filter Kelas Multi-Select Satu Opsi per Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-193`): `John Doe {runId}-193` (Active, Activated, Position `HR Business Partner`, Division `Finance`, Modified By `Budi Santoso {runId}-193`, Temporary User `No`), `Jane Smith {runId}-193` (Inactive, Activated, Position `Finance Manager`, Division `Finance`, Modified By `Budi Hartono {runId}-193`), `Sarah Lee {runId}-193` (Inactive, Pending Activation, Division `IT Operations`), `Budi Santoso {runId}-193` (Inactive, Pending Email Confirmation), `Mike Tan {runId}-193` (Active, Pending Activation, Division `IT Operations`), `Andi Wijaya {runId}-193` (Active, Activated, Temporary User `Yes`).
- Tabel filter TC-274 (parameter langkah 3 sampai 6):
| No | Field | Opsi | Baris yang tampil | Baris pembanding yang tidak tampil |
|---|---|---|---|---|
| 1 | Status | `Inactive` | `Jane Smith {runId}-193`, `Sarah Lee {runId}-193`, `Budi Santoso {runId}-193` | `John Doe {runId}-193` |
| 2 | Position | `Finance Manager` | `Jane Smith {runId}-193` | `John Doe {runId}-193` |
| 3 | Division | `IT Operations` | `Sarah Lee {runId}-193`, `Mike Tan {runId}-193` | `John Doe {runId}-193` |
| 4 | Modified By | `Budi Hartono {runId}-193` | `Jane Smith {runId}-193` | `John Doe {runId}-193` |
| 5 | Activation Status | `Pending Activation` | `Mike Tan {runId}-193`, `Sarah Lee {runId}-193` | `John Doe {runId}-193` |
| 6 | Temporary User | `Yes` | `Andi Wijaya {runId}-193` | `John Doe {runId}-193` |
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.

## Test Steps

### TC-AC-SU-274: Filter kelas multi-select satu opsi (Status, Position, Division, Modified By, Activation Status, Temporary User)

1. Klik icon Search
2. Klik icon Filter
3. Pilih opsi pada kolom "Opsi" untuk field pada kolom "Field" tabel filter TC-274, klik `[Apply]`
4. Ganti isi kotak search dengan `{runId}-193`, tekan Enter
5. Verifikasi baris pada kolom "Baris yang tampil" tabel filter TC-274 tampil di tabel
6. Verifikasi baris pada kolom "Baris pembanding" tabel filter TC-274 tidak tampil
7. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

## Notes

- Langkah 2 sampai 7 diulang untuk tiap baris tabel filter TC-274 (8b butir 7); langkah 1 (buka kotak Search) dijalankan sekali; parameter ada di Prerequisites; `[Apply]` menutup Filter Panel, sehingga langkah 7 diawali `Klik icon Filter` dan langkah 2 membukanya lagi di iterasi berikutnya.
- Langkah penghubung (S-03): langkah 4 (Search `{runId}-193` sesudah Apply agar asersi baris tidak bergantung halaman dan baris Pre-setup; isi kotak search sama di tiap iterasi).
- TC-272 dan TC-273 (Filter Panel) ada di spec 077.
- Alasan di atas ±35 langkah (ekspansi): satu TC berisi enam field dengan langkah identik, berdiri sendiri.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-193` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
