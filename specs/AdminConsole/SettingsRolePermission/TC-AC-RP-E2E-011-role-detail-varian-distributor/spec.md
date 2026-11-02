---
id: TC-AC-RP-E2E-011-role-detail-varian-distributor
title: "Role Detail Varian Entitas Distributor: Manage TAG stock, Manage hardware stock, dan Tanpa Approvers Section"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-40
  - TC-AC-RP-44
  - TC-AC-RP-430
coverage:
  web: automated
---

# Role Detail Varian Entitas Distributor: Manage TAG stock, Manage hardware stock, dan Tanpa Approvers Section

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor `totalControlDistRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Gilang Ramadhan`, entitas `Distributor Nusantara`), password dari `Spectra.env.AC_RP_DIST_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza, `AC_RP_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: Tabel Data Uji Pre-setup #19 (`Distributor Nusantara` dengan Total Control `Gilang Ramadhan`, yang memegang `Manage TAG stock` melalui tingkat akses itu; user Standard `Bayu Santoso` belum memegang peran apa pun). Berkas fixture Pre-setup modul belum ada dan disediakan tim FE.
- Spec read-only: aksi `Remove` dan "+ Assign" tidak dijalankan (hanya keberadaannya diamati); tidak ada data Dinamis, seeding, atau suffix `{runId}`. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_DIST_TC_PASSWORD` adalah nama baru dan `AC_RP_TC_PASSWORD` dipakai hook `after`; keduanya harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-40: Varian Detail Manage TAG stock entitas Distributor tanpa kolom CRUD

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage TAG stock` lalu klik `Detail`
3. Perhatikan header tabel dan keterangan halaman
4. Verifikasi tabel tidak memiliki kolom C, R, U, D sama sekali
5. Verifikasi kolom data tabel adalah Name, Position, Division
6. Verifikasi teks statis di bawah deskripsi role memuat "TAG stock access is managed as a whole."
7. Verifikasi tombol "+ Assign" dan checkbox bulk tersedia
8. Klik `⋯` pada baris pertama tabel
9. Verifikasi overlay row action memuat `Remove`
10. Tutup overlay row action

### TC-AC-RP-44: Approvers Section tidak tampil pada Distributor dan Partner

11. Klik segmen "System" pada Breadcrumb untuk kembali ke Tab System
12. Pada section Global Role, klik `⋯` pada baris `Manage hardware stock` lalu klik `Detail`
13. Cari section "Approvers — Duplicate Identifier"
14. Verifikasi halaman Role Detail `Manage hardware stock` menampilkan toolbar dan tabel user assignments
15. Verifikasi section Approvers tidak tampil

### TC-AC-RP-430: Varian Detail Manage hardware stock entitas Distributor tanpa kolom CRUD

16. Perhatikan header tabel dan keterangan halaman
17. Verifikasi tabel tidak memiliki kolom C, R, U, D sama sekali
18. Verifikasi kolom data tabel adalah Name, Position, Division
19. Verifikasi teks statis di bawah deskripsi role memuat "Hardware stock access is managed as a whole."
20. Verifikasi tombol "+ Assign" dan checkbox bulk tersedia
21. Klik `⋯` pada baris pertama tabel
22. Verifikasi overlay row action memuat `Remove`
23. Tutup overlay row action

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Seluruh TC spec ini TC FE; spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan: TC-AC-RP-430 ditaruh sesudah TC-AC-RP-44 karena keduanya memakai halaman Role Detail `Manage hardware stock` yang sama (S-10, tanpa buka halaman ulang). Pada TC-AC-RP-44 bagian "Distributor dan Partner" hanya varian Distributor yang diuji; tidak ada akun Partner pada Langkah Uji TC.
- Langkah penghubung tanpa awalan Verifikasi (S-03): "Perhatikan header tabel dan keterangan halaman" dan "Cari section ..." mengikuti Langkah Uji TC sumber; menutup overlay pada langkah 10 dan 23; klik segmen "System" pada Breadcrumb mengembalikan Tab System sebelum membuka Detail role lain (S-09).
- Verifikasi halaman Role Detail `Manage hardware stock` menampilkan toolbar dan tabel user assignments adalah klausa Expected TC-AC-RP-44 ("halaman langsung menampilkan toolbar dan tabel") dan sekaligus anchor positif untuk absence section Approvers (8b butir 2).
- Temuan untuk QA:
  - TC-AC-RP-40 dan TC-AC-RP-430 Expected c ("row action `⋯` → `Remove`") tidak menyebut baris mana yang diklik; spec memakai baris pertama tabel. Akun `Gilang Ramadhan` sendiri bisa menjadi baris pertama dan aksi `Remove` pada baris diri sendiri bisa Disabled; keadaan "tersedia" tidak dibedakan antara enabled dan Disabled di TC.
  - TC-AC-RP-44 menyebut "Distributor dan Partner" pada Skenario tetapi Precondition dan Langkah Uji hanya entitas Distributor; varian Partner tidak diuji di TC ini.
  - Pre-setup #19 tidak merinci isi tabel Role Detail Distributor selain `Gilang Ramadhan` dan `Bayu Santoso`; baris pertama tidak dapat diturunkan dari TC.
