---
id: TC-AC-SU-E2E-077-user-list-filter-panel-screening-dan-isi-opsi
title: "User List Filter Panel: Screening dan Isi Opsi Dropdown dari Data Tabel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-272
  - TC-AC-SU-273
coverage:
  web: automated
---

# User List Filter Panel: Screening dan Isi Opsi Dropdown dari Data Tabel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-077`): `John Doe {runId}-077` (Active, Activated, Position `HR Business Partner`, Division `Finance`, role aktif `Manage group`), `Jane Smith {runId}-077` (Inactive, Pending Email Confirmation, Position `Finance Manager`, Division `IT Operations`, Modified By `Budi Hartono {runId}-077`), `Mike Tan {runId}-077` (Active, Pending Activation, Temporary User `Yes`), `Rina Putri {runId}-077` (Total Control), `Andi Wijaya {runId}-077` (Read Only). Global Role `Manage presetup` tidak aktif di user mana pun milik spec; Position `Legal Counsel` ada di master Global Settings (Pre-setup) tanpa user milik spec.
- Custom Field Pre-setup `Shift` (Dropdown) berstatus Active (Pre-setup #10).
- Tabel opsi dropdown TC-273 (parameter langkah 11 sampai 12):
| No | Field | Opsi yang harus ada |
|---|---|---|
| 1 | Status | `Active`, `Inactive` |
| 2 | Role | `Manage group`, `Total Control`, `Read Only` |
| 3 | Position | `HR Business Partner`, `Finance Manager` |
| 4 | Division | `Finance`, `IT Operations` |
| 5 | Modified By | `Budi Hartono {runId}-077` |
| 6 | Activation Status | `Activated`, `Pending Activation`, `Pending Email Confirmation` |
| 7 | Temporary User | `Yes`, `No` |
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.
- Pemulihan Setup Column: preferensi kolom yang disimpan spec ini dihapus di hook `after` dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.

## Test Steps

### TC-AC-SU-272: Screening Filter Panel User List

1. Hover icon Filter
2. Verifikasi tooltip `Filter` tampil
3. Klik `⋯` pada header Actions
4. Klik `[Setup Column]`
5. Centang seluruh kolom curated (`Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, dan Custom Field aktif) pada Setup Column
6. Klik `[Save]`
7. Klik icon Filter
8. Verifikasi Filter Panel muncul di bawah toolbar
9. Verifikasi field: `Status` (multi-select searchable, placeholder `All statuses`) | `Role` (`All roles`) | `Position` (`All positions`) | `Division` (`All divisions`) | `Modified By` (`All users`) | `Last Updated` (date range, `Select date`) | `Activation Status` (`All statuses`) | `Temporary User` (`All options`) | `Temporary Until` (date range, `Select date`) | `Shift` (Custom Field Dropdown aktif)
10. Verifikasi kontrol `[Clear Field]` (link) dan `[Apply]` (button)

### TC-AC-SU-273: Isi opsi dropdown filter populate DISTINCT dari data tabel

11. Buka dropdown pada kolom "Field" tabel opsi dropdown TC-273
12. Verifikasi dropdown memuat opsi pada kolom "Opsi yang harus ada"
13. Buka dropdown `Role`
14. Verifikasi dropdown `Role` tidak memuat opsi `Manage presetup` (tanpa user aktif)
15. Buka dropdown `Position`
16. Verifikasi dropdown `Position` tidak memuat opsi `Legal Counsel` (tanpa user)

## Notes

- Langkah penghubung (S-03): Setup Column pada TC-272 menampilkan seluruh kolom curated sebelum Filter Panel dibuka mengikuti Langkah TC; konfigurasi kolom dipulihkan hook `after`.
- Langkah 11 sampai 12 diulang untuk tiap baris tabel opsi dropdown TC-273 (8b butir 7). Opsi yang tidak boleh ada (`Manage presetup`, `Legal Counsel`) diasersi pada langkah terpisah sesudah pengulangan.
- TC-274 (filter kelas multi-select satu opsi) ada di spec 193.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-077` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-273 Expected "hanya Role/Position/Division/Modified By yang dimiliki user DS-UL" tidak dapat diasersi sebagai himpunan penuh karena opsi DISTINCT juga memuat nilai dari baris Pre-setup; spec mengasersi opsi milik spec ada dan opsi tanpa user (`Legal Counsel`, `Manage presetup`) tidak ada.
