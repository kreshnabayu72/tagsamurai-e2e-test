---
id: TC-FA-RP-E2E-011-screening-popup-assign-dan-mekanik-table-user-picker-dasar-1
title: "Screening popup Assign dan mekanik Table User Picker dasar (1/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-35
  - TC-FA-RP-36
  - TC-FA-RP-37
  - TC-FA-RP-38
coverage:
  web: automated
---

# Screening popup Assign dan mekanik Table User Picker dasar (1/3)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #15 dan #16 (pool pengguna sebagai kandidat popup Assign), #18 (pohon group; `Data Center` dan `Rack A1` dipakai preview scope). Spec hanya membaca dan membatalkan popup; tidak mengubah data.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama group, dan nama pengguna ditambahkan tim FE.
- Kemampuan teknis: tidak ada tambahan. Spec tidak mengubah state global.

## Test Steps

### TC-FA-RP-35: Screening popup Assign Total Control (3 zona)

1. Klik `[+ Assign]` di Tab `Total Control`
2. Verifikasi Modal Dialog size lg berjudul `Assign Total Control`
3. Verifikasi tombol `(✕)` tampil di header
4. Verifikasi toolbar `Search | Filter` dengan placeholder Search `Search name, email, position...`
5. Verifikasi kolom `Name (sortable) | Email (sortable) | Position (sortable) | Division (sortable) | Status (sortable) | Column Visibility (⋯)`
6. Verifikasi Checkbox per baris dan header Select All tampil
7. Verifikasi counter bar tidak tampil sebelum ada seleksi
8. Verifikasi `[Cancel]` (Text, Contrast) dan `[Assign]` (primary, enabled) tampil di footer
9. Verifikasi pagination tampil di footer
10. Verifikasi sedikitnya satu baris kandidat tampil
11. Verifikasi aktor sendiri (Siti Rahmawati) dan Default User tidak ada di daftar
12. Klik `[✕]` untuk menutup popup

### TC-FA-RP-36: Screening popup Assign Read Only

13. Klik Tab `Read Only`, lalu klik `[+ Assign]`
14. Verifikasi Modal Dialog size lg berjudul `Assign Read Only`
15. Verifikasi struktur toolbar, kolom, dan footer sama dengan popup Assign Total Control
16. Verifikasi sedikitnya satu baris kandidat tampil
17. Verifikasi aktor sendiri, Default User, Total Control, dan Read Only tidak ada di daftar
18. Klik `[✕]` untuk menutup popup

### TC-FA-RP-37: Screening popup Assign Group Manager (field Group, preview scope)

19. Klik Tab `Group Manager`, klik node `All Groups` di Sidebar Group Tree, lalu klik `[+ Assign]`
20. Verifikasi Modal berjudul `Assign Group Manager`
21. Verifikasi field Group berlabel `Group` (TreeSelect single-select, placeholder `Select group`) kosong karena Sidebar pada `All Groups`
22. Pilih group `Data Center` pada field Group
23. Verifikasi preview scope menampilkan `Data Center` dan `Rack A1` (node terpilih beserta descendant)
24. Verifikasi footer `[Cancel]` dan `[Assign]` tampil
25. Klik `[✕]` untuk menutup popup

### TC-FA-RP-38: Screening popup Assign User, Global Role (tanpa field Group)

26. Klik Tab `System`, buka Detail Role `Manage Open API`, lalu klik `[+ Assign]`
27. Verifikasi Modal berjudul `Assign User — Manage Open API`
28. Verifikasi popup tanpa field Group dan tanpa preview scope
29. Verifikasi struktur toolbar, kolom, dan footer sama dengan popup Assign lain
30. Klik `[✕]` untuk menutup popup

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-35, 36, 37, 38). TC-FA-RP-39 sampai 42 ada di spec `TC-FA-RP-E2E-012-screening-popup-assign-dan-mekanik-table-user-picker-dasar-2`.
- Langkah penghubung (tanpa awalan `Verifikasi`): klik tab, buka Detail Role, pilih group pada field Group (precondition expected b TC-FA-RP-37), dan menutup popup dengan `[✕]` (popup tanpa seleksi tertutup tanpa dialog `Unsaved Changes`, sesuai TC-FA-RP-44).
- Absence daftar kandidat (aktor sendiri, Default User, Total Control, Read Only): didahului `Verifikasi` sedikitnya satu baris kandidat tampil pada popup yang sama (8b butir 2).
- Pola header PRD yang disebut TC-FA-RP-38 expected c (`Assign User — [Role Name]`) dicakup oleh `Verifikasi` judul modal pada Role `Manage Open API`.
- Temuan untuk QA:
  - TC-FA-RP-37 expected a menyebut field Group "kosong karena Sidebar pada `All Groups`"; precondition d menyatakan Sidebar pada `All Groups` tanpa langkah memilihnya; spec mengklik node `All Groups` pada langkah pembuka.
  - Post Condition TC-FA-RP-35, 36, 37, dan 38 tidak memberi langkah observasi tambahan; tidak diasersi.
