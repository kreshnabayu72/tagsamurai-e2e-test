---
id: TC-AC-RP-E2E-081-role-detail-sort-dan-column-visibility
title: "Role Detail: Sort kolom dan kolom CRUD tidak di Column Visibility"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-279
  - TC-AC-RP-280
  - TC-AC-RP-281
  - TC-AC-RP-282
  - TC-AC-RP-283
coverage:
  web: automated
---

# Role Detail: Sort kolom dan kolom CRUD tidak di Column Visibility

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD` (nama env baru, perlu didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini: mengikuti pernyataan hook suite di `suite.md`.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role, kolom) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script).
- Spec ini tidak menulis data Pre-setup; tidak ada record bersuffix `+{runId}-NNN` yang dibuat.
- Role Detail Global Role `Manage device master data` memuat sedikitnya dua nilai distinct pada kolom Name, Position, dan Division; Role Detail Group Role `Manage distributor` memuat penugasan pada lebih dari satu group (Pre-setup #11, #15).

## Test Steps

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`

### TC-AC-RP-279: Sort Role Detail kolom Name

3. Klik header Name sekali
4. Verifikasi urutan Name A-Z
5. Klik header Name kedua kali
6. Verifikasi urutan Name Z-A
7. Klik header Name ketiga kali
8. Verifikasi urutan kembali netral ke Name A-Z
9. Verifikasi kolom C/R/U/D tidak memiliki ikon sort

### TC-AC-RP-280: Sort Role Detail kolom Position

10. Klik header Position sekali
11. Verifikasi urutan Position A-Z
12. Klik header Position kedua kali
13. Verifikasi urutan Position Z-A
14. Klik header Position ketiga kali
15. Verifikasi urutan kembali netral ke Name A-Z
16. Verifikasi kolom C/R/U/D tidak memiliki ikon sort

### TC-AC-RP-281: Sort Role Detail kolom Division

17. Klik header Division sekali
18. Verifikasi urutan Division A-Z
19. Klik header Division kedua kali
20. Verifikasi urutan Division Z-A
21. Klik header Division ketiga kali
22. Verifikasi urutan kembali netral ke Name A-Z
23. Verifikasi kolom C/R/U/D tidak memiliki ikon sort

### TC-AC-RP-283: Kolom CRUD tidak tercantum di Column Visibility

24. Buka Column Visibility
25. Verifikasi daftar memuat Name, Position, Division, dan kolom curated
26. Verifikasi kolom C/R/U/D, Checkbox, dan Actions tidak tercantum sehingga tidak dapat disembunyikan, di-drag, atau di-pin
27. Tutup Column Visibility dengan `✕` atau `Esc`

### TC-AC-RP-282: Sort Role Detail Group Role kolom Group

28. Klik segmen "System" pada Breadcrumb
29. Pada section Group Role, klik `⋯` pada baris `Manage distributor` lalu klik `Detail`
30. Klik header Group sekali
31. Verifikasi baris berurutan berdasarkan nama group A-Z

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec fungsional tanpa kelas harness khusus.
- Langkah 1 dan langkah sesudahnya membuka Role Detail `Manage device master data` sekali untuk TC-AC-RP-279 sampai 281 dan 283 (langkah buka halaman TC berikutnya tidak diulang); klik ketiga tiap siklus sort mengembalikan urutan bawaan (S-09).
- Penyimpangan urutan: TC-AC-RP-283 dijalankan sebelum TC-AC-RP-282 karena memakai Role Detail yang sama dengan TC-AC-RP-279 sampai 281; TC-AC-RP-282 membutuhkan Role Detail Group Role.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 27 menutup Column Visibility; langkah 28 kembali ke Tab System (S-09).
- Verifikasi "tidak dapat disembunyikan, di-drag, atau di-pin" pada TC-AC-RP-283 ditulis satu Verifikasi bersama tidak tercantum karena tidak teramati terpisah dari ketiadaan di daftar (S-03).
- Temuan untuk QA: Column Visibility pada TC-AC-RP-283 tidak menyebut `[Save]`; Expected TC-AC-RP-279 sampai 281 sama (siklus sort dan tanpa ikon sort kolom C/R/U/D).
