---
id: TC-FA-SU-E2E-107-kolom-curated-user-list-urutan-setelah-last-updated-dan-kolom-tag-pada-plan-starter
title: "Kolom Curated User List: Urutan Setelah Last Updated dan Kolom TAG pada Plan Starter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-366
coverage:
  web: automated
---

# Kolom Curated User List: Urutan Setelah Last Updated dan Kolom TAG pada Plan Starter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Data Pre-setup tambahan: Custom Field (#31, termasuk Shift) dan plan Enterprise Client `FaUserMain` (#32).
- Preferensi kolom User List (Setup Column) dihapus di browser pada hook `before` dan `after` spec ini (kemampuan disediakan tim FE, bagian 4 konvensi), bukan lewat `[Reset to Default]`.

## Test Steps

### TC-FA-SU-366: Urutan kolom curated setelah Last Updated

1. Verifikasi urutan kolom default: `Active`, `Name`, `Email`, `Role`, `Home Group`, `Position`, `Division`, `Employee ID`, `Modified By`, `Last Updated`
2. Verifikasi kolom curated `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, dan `Shift` default tersembunyi
3. Klik header kolom Actions (⋯)
4. Klik `Setup Column...`
5. Centang `Activation Status` dan `Temporary User`, klik `[Save]`
6. Verifikasi kolom `Activation Status` dan `Temporary User` tampil setelah `Last Updated`
7. Klik header kolom Actions (⋯), klik `Setup Column...`
8. Verifikasi daftar Setup Column memuat `TAG` dan `Shift` sesuai gating plan Enterprise dan Custom Field aktif
9. Klik `[✕]` pada Setup Column

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 7 (membuka Setup Column) dan 9 (menutup Setup Column).
- TC-FA-SU-367 (kolom dan field TAG pada plan Starter) dipindah ke spec `TC-FA-SU-E2E-377` (kelas h, state tenant) karena mengubah plan; spec ini hanya membaca dan tidak mengubah plan Client `FaUserMain`.
- Temuan untuk QA (S-15): TC-FA-SU-366 langkah 3 menyuruh mencentang kolom curated lewat header kolom Actions (⋯), sedangkan TC-FA-SU-350 menyatakan kolom curated hanya ada di Setup Column; spec memakai Setup Column.
