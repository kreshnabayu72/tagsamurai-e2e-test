---
id: TC-AC-RP-E2E-009-screening-role-detail-global-role
title: "Screening Role Detail Global Role: Header, Kolom, Baris CRUD, Kolom R Disabled, dan Sel Tidak Berlaku"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-34
  - TC-AC-RP-35
  - TC-AC-RP-36
  - TC-AC-RP-37
coverage:
  web: automated
---

# Screening Role Detail Global Role: Header, Kolom, Baris CRUD, Kolom R Disabled, dan Sel Tidak Berlaku

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: Tabel Data Uji Pre-setup #11 (tree group Principal), #13 (pemegang Total Control `Bambang Hartono`, `Budi Santoso`, `John Doe`, `Rina Wijaya`, `Sarah Kim`, `Siti Nurhaliza`; Read Only `Dewi Anggraini`, `Lisa Wong`), dan #15 (penugasan individual `Manage device master data`: `John Dohan` C/R/U, `Jane Smith` R, `Hendra Wijaya` R, `Fajar Nugroho` R, `Maya Putri` R; `Manage hardware stock`: `Alex Tan` C/R). Berkas fixture Pre-setup modul belum ada dan disediakan tim FE.
- Spec read-only: checkbox R yang diklik pada TC-AC-RP-36 Disabled sehingga tidak mengubah data; tidak ada data Dinamis, seeding, atau suffix `{runId}`. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-34: Screening Role Detail Global Role

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
3. Susuri halaman dari atas ke bawah
4. Verifikasi Breadcrumb "Settings > Role & Permission > System > Detail"
5. Verifikasi Page Header menampilkan Title "Manage device master data"
6. Verifikasi Page Header menampilkan deskripsi "This role allows the user to manage device categories, device names, and hardware SKUs through the Device Master Data menu."
7. Verifikasi Toolbar: Search, Filter, Download, Changelog, "+ Assign"
8. Verifikasi tabel berkolom: Checkbox (kolom pertama), Name, Position, Division, C, R, U, D, Actions `⋯`
9. Verifikasi tidak ada Sidebar Group Tree dan tidak ada kolom Group

### TC-AC-RP-35: Isi baris Role Detail Manage device master data

10. Pilih 25 baris per halaman
11. Verifikasi tabel menampilkan 13 baris berurutan Name A-Z
12. Verifikasi baris `John Dohan`: C ☑, R ☑ disabled, U ☑, D ☐
13. Verifikasi baris `Jane Smith`, `Hendra Wijaya`, `Fajar Nugroho`, dan `Maya Putri` hanya R ☑ disabled
14. Verifikasi baris Total Control (`Budi Santoso`, `John Doe`, `Rina Wijaya`, `Sarah Kim`) C/R/U/D ☑
15. Verifikasi baris Read Only (`Dewi Anggraini`, `Lisa Wong`) hanya R ☑
16. Verifikasi baris `Bambang Hartono` (Default User) dan `Siti Nurhaliza` (diri sendiri) tetap tampil

### TC-AC-RP-36: Kolom R selalu checked disabled dengan tooltip

17. Hover checkbox R baris `John Dohan`
18. Verifikasi checkbox R checked dan disabled
19. Verifikasi tooltip "Read access is required and can only be removed by removing the role." tampil
20. Klik checkbox R tersebut
21. Verifikasi klik tidak mengubah nilai: checkbox R tetap checked
22. Verifikasi tidak ada toast yang tampil

### TC-AC-RP-37: Sel CRUD tidak berlaku tampil sebagai teks tanpa checkbox

23. Klik segmen "System" pada Breadcrumb untuk kembali ke Tab System
24. Pada section Global Role, klik `⋯` pada baris `Manage hardware stock` lalu klik `Detail`
25. Perhatikan kolom U baris `Alex Tan`
26. Verifikasi kolom U pada semua baris tanpa checkbox dan menampilkan teks "—" yang tidak dapat diklik
27. Verifikasi baris `Alex Tan`: C ☑, R ☑ disabled, D ☐

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Seluruh TC spec ini TC FE; spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03): langkah 3 (susur halaman sebagai prasyarat asersi), langkah 10 (memilih 25 baris per halaman agar seluruh 13 baris teramati, S-14), dan langkah 23 (kembali ke Tab System lewat Breadcrumb sebelum membuka Detail role lain). Langkah "Perhatikan kolom U" mengikuti Langkah Uji TC-AC-RP-37.
- Pembagian TC lintas spec: TC-AC-RP-38 (deskripsi Global Role untuk 10 role) ada di spec 120; ia memakai halaman Role Detail yang sama tetapi berulang per role sehingga berdiri sendiri.
- Verifikasi baris `Alex Tan` pada TC-AC-RP-37 dilakukan di Role Detail Principal `Manage hardware stock`, bukan varian Distributor (spec 011).
- Temuan untuk QA:
  - TC-AC-RP-35 menyebut "13 baris" sebagai hasil gabungan Total Control, Read Only, Default User, diri sendiri, dan penugasan individual; jumlah 13 bergantung data Pre-setup #13 dan #15 yang tidak dijumlahkan di TC.
  - TC-AC-RP-36 tidak menyatakan keadaan fokus atau hover setelah klik; asersi memakai nilai checkbox tetap checked dan tidak ada toast.
