---
id: TC-AC-SU-E2E-015-aktor-default-user-tanpa-aksi-create-edit-delete
title: "Aktor Default User: Tanpa Aksi Create, Edit, atau Delete serta Switch dan Checkbox Baris Default User Disabled"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-50
  - TC-AC-SU-58
  - TC-AC-SU-114
coverage:
  web: automated
---

# Aktor Default User: Tanpa Aksi Create, Edit, atau Delete serta Switch dan Checkbox Baris Default User Disabled

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User (Pre-setup #1) `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DU_PASSWORD`.
- Login di hook `before` spec ini sebagai Default User; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-50 | `John Doe` | `John Doe {runId}-015` | `johndoe+{runId}-015@qwertysystem.net` | Activated, Active |
| TC-AC-SU-58 | `Dewi Lestari` | `Dewi Lestari {runId}-015` | `dewilestari+{runId}-015@qwertysystem.net` | Total Control |
| TC-AC-SU-58 | `Andi Wijaya` | `Andi Wijaya {runId}-015` | `andiwijaya+{runId}-015@qwertysystem.net` | Read Only |
| TC-AC-SU-58 | `Rudi Hartono` | `Rudi Hartono {runId}-015` | `rudihartono+{runId}-015@qwertysystem.net` | tanpa role (kosong) |

- Baris Default User sendiri (aktor sekaligus Default User) dicari lewat Search atas email Pre-setup #1 dan tidak diubah.
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-50: Tidak ada aksi Create, Edit identitas, atau Delete user

1. Ketik Search `John Doe {runId}-015`, tekan Enter
2. Amati toolbar dan row action
3. Verifikasi Table Tools `Search | Filter | Download | Changelog` tampil
4. Verifikasi toolbar tanpa tombol `[+ User]`/Create
5. Klik (⋯) baris `John Doe {runId}-015`
6. Verifikasi row action berisi `Detail`
7. Verifikasi row action tanpa `Edit` dan `Delete`
8. Tutup menu row action dengan Esc
9. Klik Name `John Doe {runId}-015`
10. Verifikasi General Information tampil
11. Verifikasi Detail tanpa `Edit Profile` dan `Delete User`
12. Verifikasi seluruh field General Information read-only
13. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User

### TC-AC-SU-58: Switch Active per target, aktor Default User

14. Ganti isi kotak search dengan `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
15. Hover switch baris Default User sendiri
16. Verifikasi switch baris Default User sendiri tampil namun disabled
17. Verifikasi tooltip `Default User cannot be modified.` (prioritas Default User di atas self)

### TC-AC-SU-114: Aktor Default User, baris dirinya tetap Disabled

18. Hover checkbox baris Default User (aktor sendiri)
19. Verifikasi checkbox tampil namun disabled
20. Verifikasi tooltip `Default User cannot be modified.` (prioritas Default User > self)
21. Klik checkbox baris Default User
22. Verifikasi checkbox tetap tampil namun disabled

### TC-AC-SU-58: Switch Active per target (lanjutan, target lain)

23. Ganti isi kotak search dengan `{runId}-015`, tekan Enter
24. Verifikasi switch Active baris `Dewi Lestari {runId}-015` enabled
25. Verifikasi switch Active baris `Andi Wijaya {runId}-015` enabled
26. Verifikasi switch Active baris `Rudi Hartono {runId}-015` enabled
27. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16; berlaku juga untuk semua Search sesudahnya, termasuk 14 dan 23), langkah 8 (tutup menu), langkah 13 (kembali ke daftar), langkah 27 (reset Search).
- Perubahan urutan TC (S-05): blok TC-AC-SU-58 dipecah di dua tempat dan TC-AC-SU-114 disisipkan di antaranya karena baris Default User sendiri dicari lewat email, sedangkan target lain dicari lewat suffix; urutan: 50, 58 (Default User sendiri), 114, 58 (target lain). Subjudul memetakan langkah ke id TC.
- Temuan untuk QA:
  - TC-AC-SU-58: target `Dewi Lestari`, `Andi Wijaya`, dan `Rudi Hartono` di-seed sebagai user milik spec bersuffix; baris Default User dicari lewat email Pre-setup #1.
  - TC-AC-SU-114: TC tidak menyebut hasil klik checkbox yang disabled selain tetap visible dan disabled; spec mengasersi keduanya sesudah klik.
  - Nama user TC (`John Doe`, `Dewi Lestari`, `Andi Wijaya`, `Rudi Hartono`) dipakai sebagai nama bersuffix `{runId}-015` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
