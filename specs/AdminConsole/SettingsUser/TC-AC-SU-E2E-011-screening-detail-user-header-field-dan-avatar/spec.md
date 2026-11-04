---
id: TC-AC-SU-E2E-011-screening-detail-user-header-field-dan-avatar
title: "Screening Detail User: Tiga Zona Header, Body, dan Avatar Read-only dengan atau tanpa Foto"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-37
  - TC-AC-SU-40
coverage:
  web: automated
---

# Screening Detail User: Tiga Zona Header, Body, dan Avatar Read-only dengan atau tanpa Foto

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-37, 40 | `John Doe` | `John Doe {runId}-011` | `johndoe+{runId}-011@qwertysystem.net` | Activated, Active, tanpa foto; Employee ID `EMP-001-{runId}-011`, Position `Finance Manager`, Division `Finance`, bukan Temporary User, TAG `—`; Custom Field aktif Pre-setup (`Office Location`, `Shift`, `Join Date`) tidak diubah; tanpa Responsibility (label tab `Responsibilities (0)`) |
| TC-AC-SU-40 | `Rina Putri` | `Rina Putri {runId}-011` | `rinaputri+{runId}-011@qwertysystem.net` | punya foto profil di Global Settings |

- Custom Field Pre-setup (#10) aktif sehingga accordion `Custom Field` tampil; spec tidak mengubahnya. Foto profil `Rina Putri` di-seed lewat Fixture BE.
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-37: Screening halaman Detail User 3 zona

1. Ketik Search `John Doe {runId}-011`, tekan Enter
2. Klik Name `John Doe {runId}-011`
3. Verifikasi Header: Breadcrumb `Settings > User > Detail`
4. Verifikasi Header: segmen `Settings` dan `Detail` berupa label statis
5. Verifikasi Header: segmen `User` dapat diklik
6. Verifikasi Header: avatar read-only
7. Verifikasi Header: Full Name `John Doe {runId}-011`
8. Verifikasi Header: badge `Active` (success)
9. Verifikasi Header: Employee ID `EMP-001-{runId}-011` sebagai subtitle muted di bawah Full Name
10. Verifikasi Header: Switch Active berlabel `Active`
11. Verifikasi Header: tidak ada tombol Resend (bukan Pending)
12. Verifikasi Body: General Information berupa grid 4 kolom
13. Verifikasi Body: Baris 1 General Information `Email | User Type | Position | Division`
14. Verifikasi Body: Baris 2 General Information berisi `TAG`
15. Verifikasi Body: field Temporary Until hidden
16. Verifikasi Body: accordion `Custom Field` collapsed
17. Verifikasi Body: Tab `Role (aktif) | Responsibilities (0) | Changelog | System Log | User Log`
18. Verifikasi Body: Sub-tab `Global Role (aktif) | Group Role`
19. Verifikasi tidak ada aksi Edit Profile, Delete, atau edit foto

### TC-AC-SU-40: Avatar Detail User read-only dengan dan tanpa foto

20. Hover avatar `John Doe {runId}-011` pada Detail yang sedang terbuka
21. Verifikasi avatar `John Doe {runId}-011` berupa lingkaran initials `JD`
22. Verifikasi hover avatar `John Doe {runId}-011` tidak menampilkan overlay edit/delete
23. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
24. Ganti isi kotak search dengan `Rina Putri {runId}-011`, tekan Enter
25. Klik Name `Rina Putri {runId}-011`
26. Hover avatar `Rina Putri {runId}-011`
27. Verifikasi avatar `Rina Putri {runId}-011` berupa lingkaran berisi foto
28. Verifikasi hover avatar `Rina Putri {runId}-011` tidak menampilkan overlay edit/delete
29. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
30. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16; berlaku juga untuk Search sesudahnya), langkah 23 dan 29 (kembali ke daftar), langkah 30 (reset Search). Layar awal dibuka hook `beforeEach` suite.
- Detail `John Doe {runId}-011` dipakai bersama oleh TC-AC-SU-37 dan butir John Doe TC-AC-SU-40 (kunjungan yang sama, tanpa membuka ulang): langkah "Buka Detail `John Doe`" TC-AC-SU-40 dipenuhi oleh Detail yang sudah terbuka dari TC-AC-SU-37 supaya halaman yang sama tidak dibuka dua kali.
- Temuan untuk QA:
  - TC-AC-SU-37: nilai Employee ID `EMP-001` dipakai sebagai `EMP-001-{runId}-011` (bersuffix); Position `Finance Manager` dan Division `Finance` adalah nilai master data yang tidak ada di Tabel Pre-setup, disediakan tim FE/BE.
  - TC-AC-SU-37 menyebut "≥1 Custom Field aktif" dan Tab `Responsibilities (N)` tanpa nilai N; spec men-seed `John Doe {runId}-011` tanpa Responsibility sehingga N = 0 diturunkan dari seeding dan label diasersi `Responsibilities (0)`.
  - TC-AC-SU-40: foto profil `Rina Putri` "di Global Settings" di-seed lewat Fixture BE (mekanisme tidak disebut TC).
  - Nama user TC (`John Doe`, `Rina Putri`) dipakai sebagai nama bersuffix `{runId}-011` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
