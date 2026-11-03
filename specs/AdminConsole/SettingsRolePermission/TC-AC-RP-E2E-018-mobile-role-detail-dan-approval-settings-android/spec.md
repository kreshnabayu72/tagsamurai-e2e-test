---
id: TC-AC-RP-E2E-018-mobile-role-detail-dan-approval-settings-android
title: "Mobile Android: Role Detail Global (Checkbox Inline, Long Press) dan Approval Settings"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-73
  - TC-AC-RP-74
  - TC-AC-RP-75
coverage:
  mobile: automated
---

# Mobile Android: Role Detail Global (Checkbox Inline, Long Press) dan Approval Settings

## Prerequisites

- Mode: FE+BE. Platform: aplikasi native Android (PRD §4.6). Spec hanya mengamati dan memilih card secara lokal; tidak ada checkbox CRUD yang diubah dan tidak ada perubahan state server.
- Perangkat atau emulator Android dengan aplikasi native TAG Samurai Admin Console terpasang (Tabel Data Uji Pre-setup #22), serta kemampuan tap, long press, dan mengetuk elemen UI. Perangkat dipakai bersama sehingga suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Principal `Siti Nurhaliza`, `totalControlRP_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_RP_TC_PASSWORD`. Login di aplikasi Android dilakukan di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Nama env `AC_RP_TC_PASSWORD` baru dan perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Data Pre-setup (identitas dirujuk lewat fixture `acRolePermission`, belum ada, dibuat pada tahap script): #11 (tree group Principal: `Region Jawa`), #12 (user Standard `John Dohan`, `Maya Putri`, `Alex Tan`), #15 (penugasan `Manage device master data` John Dohan C/R/U dan Maya Putri R; `Manage hardware stock` Alex Tan C/R), #17 (toggle `Manage allocation` `Region Jawa` ON; Approvers `Dewi Anggraini` dan `Dewi Anggreni`).
- Data Dinamis: tidak ada; spec tidak membuat atau mengubah data sehingga tidak ada seeding, suffix `+{runId}-018`, maupun cleanup.
- Hook suite web (`beforeEach` pembuka halaman) berlaku untuk sesi browser; pada sesi aplikasi Android halaman dibuka lewat langkah spec ini, dan flag Guided Tooltip `guided_tooltip_seen_role-permission` untuk akun aktor disetel `true` oleh hook `before` suite (kemampuan disediakan tim FE/BE).

## Test Steps

### TC-AC-RP-73: Role Detail Global mobile dengan checkbox CRUD inline dan long press

1. Buka halaman `Settings > Role & Permission` di aplikasi Android
2. Klik tab `System`
3. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
4. Verifikasi header memuat Breadcrumb (sama dengan web), nama role, dan deskripsi role
5. Verifikasi header tidak memuat Back link terpisah
6. Verifikasi card `John Dohan` memuat nama dalam format komponen user (ikon user + "John D") dan `[⋯]`
7. Verifikasi card `John Dohan` memuat "Position · Division"
8. Verifikasi card `John Dohan` memuat baris "C [☑] R [☑] U [☑] D [○]" dengan R checked disabled
9. Long press card `John Dohan`
10. Verifikasi checkbox muncul pada seluruh card (mode checkbox aktif)
11. Verifikasi card `John Dohan` langsung tercentang
12. Verifikasi Floating Bottom Bulk Bar tampil di bawah dengan `[✕]`, counter "1 Selected", `[Select All]`, dan aksi `[Remove]` (danger) langsung
13. Verifikasi Floating Bottom Bulk Bar tidak memakai dropdown `Bulk Action`
14. Ketuk card `Maya Putri`
15. Verifikasi card `Maya Putri` tercentang
16. Verifikasi counter menjadi "2 Selected"
17. Ketuk `[✕]` pada Floating Bottom Bulk Bar
18. Verifikasi seluruh seleksi dibatalkan
19. Verifikasi mode checkbox berhenti (checkbox tidak tampil pada card)
20. Verifikasi Floating Bottom Bulk Bar hilang

### TC-AC-RP-74: Kolom CRUD yang tidak berlaku tampil "—" tanpa checkbox

21. Buka halaman `Settings > Role & Permission` di aplikasi Android
22. Klik tab `System`
23. Pada section Global Role, klik `⋯` pada baris `Manage hardware stock` lalu klik `Detail`
24. Verifikasi baris checkbox card `Alex Tan` memuat C, R, dan D sebagai checkbox
25. Verifikasi U pada baris checkbox card `Alex Tan` tanpa checkbox dan tampil "—"

### TC-AC-RP-75: Approval Settings mobile mengikuti chip Group

26. Buka halaman `Settings > Role & Permission` di aplikasi Android
27. Klik tab `System`
28. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
29. Verifikasi chip "All Groups" menampilkan card prompt "Select a group from the sidebar to view and manage its approvers."
30. Verifikasi "+ Assign" Approvers tidak tampil pada chip "All Groups"
31. Pilih `Region Jawa` pada chip Group
32. Verifikasi Toggle Card "Require Approval for Allocation" bernilai ON pada chip `Region Jawa`
33. Verifikasi sub-section "Approvers — Region Jawa" tampil dengan "+ Assign"

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (S-03): langkah 21 dan 26 (membuka halaman kembali dari Role Detail sebelum TC berikutnya, tanpa asersi) beserta klik tab `System` di langkah 22 dan 27. Langkah 1 membuka halaman secara eksplisit karena hook `beforeEach` suite membuka halaman pada sesi web; spec ini berjalan di aplikasi Android.
- Langkah 20 sampai 33 tidak mengandalkan state seleksi TC-AC-RP-73: membuka halaman kembali (langkah 21) mengakhiri mode checkbox (S-09).
- Langkah 30 (absence "+ Assign") didahului langkah 29 yang membuktikan card prompt pada permukaan yang sama sudah tampil (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-RP-73 Expected c menulis "bukan dropdown `Bulk Action`" sebagai klausa pembeda; spec mengasersi absence dropdown itu (langkah 13) dengan Floating Bottom Bulk Bar pada langkah 12 sebagai anchor.
  - TC-AC-RP-73 Expected b menulis "R checked disabled" sebagai bagian nilai baris "C [☑] R [☑] U [☑] D [○]"; spec menjadikannya satu klausa nilai baris card (langkah 8).
  - Post Condition TC-AC-RP-73 sampai 75 bernilai "-" sehingga tidak ada yang diasersi.
