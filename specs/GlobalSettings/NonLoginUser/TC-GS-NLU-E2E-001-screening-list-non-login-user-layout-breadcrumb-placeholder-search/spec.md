---
id: TC-GS-NLU-E2E-001-screening-list-non-login-user-layout-breadcrumb-placeholder-search
title: "Screening List Non-Login User: layout, breadcrumb, placeholder Search, tab, dan Login User tidak tampil"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-1
  - TC-GS-NLU-2
  - TC-GS-NLU-3
  - TC-GS-NLU-4
  - TC-GS-NLU-5
coverage:
  web: automated
---

# Screening List Non-Login User: layout, breadcrumb, placeholder Search, tab, dan Login User tidak tampil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza, Default User entitas), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` untuk akun aktor sudah diset true oleh hook suite `before` (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: Non-Login User Budi Kurniawan, Siti Rahayu, Rina Marlina (No. 11) dan pool Login User Represented By (No. 10: Ahmad Fauzi, Andi Wijaya, Mike Tan) hanya dibaca. Default User Siti Nurhaliza (No. 1) dipakai sebagai kata kunci Search TC-GS-NLU-5.
- Spec hanya membaca: tidak membuat, mengubah, atau menghapus data, dan tidak mengubah state global. Search yang dipakai dipulihkan lewat langkah penghubung.
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.
- Suite berjalan serial (`parallel: false`).
- Env var yang dipakai terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-GS-NLU-1: Screening sub-tab Non-Login User oleh Total Control

1. Verifikasi Breadcrumb `User > User List > Non-Login User` tampil
2. Verifikasi tidak ada Page Title Header
3. Verifikasi Tab `User List (aktif) | Position | Division | Custom Field` tampil
4. Verifikasi Sub-tab `Login User | Non-Login User (aktif)` tampil
5. Verifikasi Table Tools (rata kanan) menampilkan `Search | Filter | Download | Changelog | [+ Non-Login User]`
6. Verifikasi kolom tabel: `Checkbox (bulk) | Active (sortable) | Name (sortable) | Position (sortable) | Division (sortable) | Employee ID (sortable) | Represented By (sortable) | Last Update (sortable) | Column Visibility (⋯) (unsortable)`
7. Verifikasi baris tampil terurut Name A-Z
8. Verifikasi footer menampilkan pagination default 10 per halaman

### TC-GS-NLU-2: Breadcrumb halaman User List mengikuti sub-tab aktif

9. Klik sub-tab `Login User`
10. Verifikasi Breadcrumb `User > User List > Login User`
11. Klik sub-tab `Non-Login User`
12. Verifikasi Breadcrumb `User > User List > Non-Login User`

### TC-GS-NLU-3: Placeholder Search pada sub-tab Non-Login User

13. Klik icon Search di Table Tools
14. Verifikasi Search input melebar
15. Verifikasi kursor otomatis fokus di dalam Search input
16. Verifikasi Placeholder `"Search name, position, division, employee ID, represented by..."`
17. Klik `(←)` pada kotak Search untuk menutup input

### TC-GS-NLU-4: Sub-tab Non-Login User tidak mempengaruhi isi sub-tab Login User

18. Klik sub-tab `Login User`
19. Verifikasi sub-tab `Login User` aktif
20. Verifikasi tabel menampilkan sedikitnya satu baris
21. Verifikasi tabel hanya memuat Login User: baris Budi Kurniawan, Siti Rahayu, dan Rina Marlina tidak tampil
22. Klik sub-tab `Non-Login User`
23. Verifikasi sub-tab `Non-Login User` aktif
24. Verifikasi tabel menampilkan sedikitnya satu baris
25. Verifikasi tabel hanya memuat Non-Login User: baris Login User Ahmad Fauzi, Andi Wijaya, dan Mike Tan tidak tampil

### TC-GS-NLU-5: Login User termasuk Default User tidak muncul di tabel Non-Login User

26. Klik icon Search, ketik Search `Siti Nurhaliza`, tekan Enter
27. Verifikasi tabel menampilkan empty state `"No results found"` untuk kata kunci `Siti Nurhaliza`
28. Verifikasi Default User `Siti Nurhaliza` tidak tampil sebagai baris di tabel
29. Ganti isi kotak search dengan `Mike Tan`, tekan Enter
30. Verifikasi tabel menampilkan empty state `"No results found"` untuk kata kunci `Mike Tan`
31. Klik `(←)` pada kotak Search untuk mengosongkan Search

## Notes

- Langkah penghubung (S-03): langkah 17, 31 (menutup atau mengosongkan kotak Search sebelum TC berikutnya, S-09).
- Langkah 1 dan 2 TC-GS-NLU-1 (klik menu `User` di sidebar, klik sub-tab `Non-Login User`) sudah dipenuhi hook `beforeEach` suite yang membuka halaman awal; spec tidak mengulangnya.
- Temuan untuk QA:
  - TC-GS-NLU-1 Expected b.i menyebut perilaku header kolom `Column Visibility (⋯)` (klik membuka overlay Column Visibility dengan CTA `[Setup Column]`), tetapi langkah TC hanya "Amati". Spec hanya mengasersi daftar kolom dan sifat unsortable; perilaku klik tidak diasersi.
  - TC-GS-NLU-4 Expected a dan b ("hanya memuat Login User" / "hanya memuat Non-Login User") tidak menyebut cara membedakan. Spec mengasersi absence nama Pre-setup pada halaman pertama yang teramati (didahului pembanding "sedikitnya satu baris"); baris di halaman lain tidak diperiksa. Keadaan awal sort sub-tab Login User tidak disebut TC.
  - TC-GS-NLU-5 Expected b ("Default User tidak pernah tampil di sub-tab ini") adalah kesimpulan dari butir a; ditulis sebagai satu Verifikasi pada kata kunci `Siti Nurhaliza`.
- Lampiran A konvensi tidak memuat butir untuk modul Non-Login User; tidak ada pengecualian khusus modul yang dipakai.
