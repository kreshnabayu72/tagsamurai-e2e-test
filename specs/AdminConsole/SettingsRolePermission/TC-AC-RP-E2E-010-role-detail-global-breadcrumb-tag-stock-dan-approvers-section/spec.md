---
id: TC-AC-RP-E2E-010-role-detail-global-breadcrumb-tag-stock-dan-approvers-section
title: "Role Detail Global Role: Breadcrumb, Manage TAG stock Principal, dan Approvers Section"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-39
  - TC-AC-RP-41
  - TC-AC-RP-42
  - TC-AC-RP-43
  - TC-AC-RP-45
coverage:
  web: automated
---

# Role Detail Global Role: Breadcrumb, Manage TAG stock Principal, dan Approvers Section

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: Tabel Data Uji Pre-setup #11 (tree group Principal), #13, #15, dan #17 (Approvers `Manage TAG stock` = `Sarah Kimura`; `Manage hardware stock` kosong). Berkas fixture Pre-setup modul belum ada dan disediakan tim FE.
- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada data Dinamis, seeding, atau suffix `{runId}`. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-39: Breadcrumb System pada Role Detail kembali ke Tab System

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage language` lalu klik `Detail`
3. Klik segmen "System" pada Breadcrumb
4. Verifikasi halaman Role & Permission tampil dengan Tab System aktif

### TC-AC-RP-41: Detail Manage TAG stock entitas Principal tetap grid CRUD penuh

5. Pada section Global Role, klik `⋯` pada baris `Manage TAG stock` lalu klik `Detail`
6. Perhatikan header tabel
7. Verifikasi tabel memiliki kolom C, R, U, D seperti role Global lain
8. Verifikasi kolom D berisi checkbox

### TC-AC-RP-42: Approvers Section tampil di atas tabel Detail Manage TAG stock (Principal)

9. Susuri section di atas tabel user assignments
10. Verifikasi section "Approvers — Duplicate Identifier" berada di atas tabel user assignments
11. Verifikasi toolbar section Approvers berisi ikon Search, ikon Filter, dan tombol "+ Assign"
12. Verifikasi tidak ada ikon Download pada toolbar section Approvers
13. Verifikasi tabel Approvers berkolom Checkbox, Name, Position, Division, Actions
14. Verifikasi tabel Approvers menampilkan 1 baris `Sarah Kimura`
15. Verifikasi tidak ada kolom Type pada tabel Approvers

### TC-AC-RP-43: Approvers Section identik pada Detail Manage hardware stock

16. Klik segmen "System" pada Breadcrumb untuk kembali ke Tab System
17. Pada section Global Role, klik `⋯` pada baris `Manage hardware stock` lalu klik `Detail`
18. Perhatikan section di atas tabel
19. Verifikasi section "Approvers — Duplicate Identifier" tampil dengan toolbar ikon Search, ikon Filter, dan tombol "+ Assign" yang sama
20. Verifikasi tabel Approvers berkolom Checkbox, Name, Position, Division, Actions
21. Verifikasi tabel Approvers kosong menampilkan empty state dengan Title "No approvers yet" dan Description "Assign an approver to review requests for this role."

### TC-AC-RP-45: Role Global lain tidak memiliki Approvers Section

22. Klik segmen "System" pada Breadcrumb untuk kembali ke Tab System
23. Pada section Global Role, klik `⋯` pada baris `Manage language` lalu klik `Detail`
24. Cari section Approvers
25. Verifikasi halaman Role Detail `Manage language` tampil dengan tabel user assignments
26. Verifikasi tidak ada section Approvers maupun Approval Settings di Detail `Manage language`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Seluruh TC spec ini TC FE; spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan: TC-AC-RP-41 dan TC-AC-RP-42 memakai halaman Role Detail `Manage TAG stock` yang sama, sehingga TC-AC-RP-42 tidak membuka halaman ulang; TC-AC-RP-40 (varian Distributor) ada di spec 011.
- Langkah penghubung tanpa awalan Verifikasi (S-03): "Perhatikan header tabel", "Susuri section di atas tabel user assignments", "Perhatikan section di atas tabel", dan "Cari section Approvers" mengikuti Langkah Uji TC sumber sebagai prasyarat asersi; klik segmen "System" pada Breadcrumb mengembalikan Tab System sebelum membuka Detail role lain (S-09).
- Verifikasi halaman Role Detail `Manage language` tampil dengan tabel user assignments (langkah sebelum asersi absence terakhir) adalah anchor positif absence section Approvers dan Approval Settings (8b butir 2).
- Verifikasi tabel Approvers berkolom Checkbox, Name, Position, Division, Actions pada TC-AC-RP-43 berasal dari klausa "toolbar dan kolom yang sama" Expected TC.
- Temuan untuk QA:
  - TC-AC-RP-43 Expected menyebut "toolbar dan kolom yang sama" tanpa menyebut ulang ikon dan kolomnya; spec menyalin daftar dari TC-AC-RP-42.
  - Judul section "Approvers — Duplicate Identifier" pada TC-AC-RP-42 dan TC-AC-RP-43 tampak seperti teks placeholder; asersi memakai teks TC persis.
