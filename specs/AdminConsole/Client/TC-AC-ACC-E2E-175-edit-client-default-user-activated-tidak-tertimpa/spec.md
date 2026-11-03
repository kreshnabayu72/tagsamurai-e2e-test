---
id: TC-AC-ACC-E2E-175-edit-client-default-user-activated-tidak-tertimpa
title: "Edit Client dengan Default User Activated: Section Default User Tidak Tampil dan Nilai Tidak Tertimpa"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-800
coverage:
  web: automated
---

# Edit Client dengan Default User Activated: Section Default User Tidak Tampil dan Nilai Tidak Tertimpa

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Active-Full (Manage active client: C/R/U/D, exact-match Area Jakarta dan Cabang Menteng), A-15 | `activeFullJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD` |

- Env var `AC_CLIENT_ACTIVE_FULL_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`.
- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data milik spec (kelas Dipulihkan pada TC, ditiru bersuffix): Client "PT Uji Tabel Detail {runId}-175" di-seed hook `before` lewat Fixture BE (disediakan tim FE/BE) dengan atribut C-DTL-1 (Tabel A3): Active, Managed By Partner CV Mitra Sejati, Group Area Jakarta, Fax kosong, Default User Activated (Name Rini Hartono, Email `rini.hartono+{runId}-175@ptujitabeldetail.test`, Division Operations, Position Operations Head; master Division dan Position memuat "Operations", "Logistics", "Operations Head", "Logistics Manager"). Hook `after` menghapus Client dan Default User milik spec ini lewat API tanpa mengandaikan seed berhasil penuh.
- Alasan data bersuffix: spec mengubah Fax (aksi tulis) sehingga tidak memakai fixture Pre-setup bersama (S-06); nama literal "PT Uji Tabel Detail" pada TC diganti nama bersuffix (S-12).
- Suite berjalan serial (`parallel: false`); spec tidak mengubah state global.

## Test Steps

### TC-AC-ACC-800: Edit Client yang Default User-nya Activated tidak menampilkan section Default User dan tidak menimpa nilai Default User

1. Ketik Search `PT Uji Tabel Detail {runId}-175`, tekan Enter
2. Klik Company Name "PT Uji Tabel Detail {runId}-175" untuk membuka Detail
3. Verifikasi Section "Default User" menampilkan Name "Rini Hartono"
4. Verifikasi Section "Default User" menampilkan Email "rini.hartono+{runId}-175@ptujitabeldetail.test"
5. Verifikasi Section "Default User" menampilkan Division "Operations"
6. Verifikasi Section "Default User" menampilkan Position "Operations Head"
7. Verifikasi Section "Default User" menampilkan badge "Activated"
8. Klik `[Edit]`
9. Verifikasi popup "Edit Client" tidak memuat Section Default User
10. Ubah Fax menjadi `0215550123`
11. Klik `[Save]`
12. Verifikasi toast "Success, client has been updated."
13. Verifikasi Detail menampilkan Fax `0215550123`
14. Verifikasi Name "Rini Hartono", Email "rini.hartono+{runId}-175@ptujitabeldetail.test", Division "Operations", dan Position "Operations Head" Default User tetap seperti sebelum Edit

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Pemulihan Fax ke kosong (Post Condition TC-800) dipenuhi hook `after` yang menghapus Client milik spec; spec tidak menulis langkah pemulihan karena data dibuang.
- Temuan untuk QA (S-15): TC-800 menyebut fixture C-DTL-1 "PT Uji Tabel Detail" sebagai target aksi tulis (kelas Dipulihkan) dan Tabel A3 menyatakan TC-800 tidak boleh berjalan bersamaan dengan TC-238; spec menghindari bentrokan itu dengan Client bersuffix milik sendiri. Mekanisme seeding salinan fixture adalah kemampuan "disediakan tim FE/BE" tanpa endpoint karangan (S-13).
