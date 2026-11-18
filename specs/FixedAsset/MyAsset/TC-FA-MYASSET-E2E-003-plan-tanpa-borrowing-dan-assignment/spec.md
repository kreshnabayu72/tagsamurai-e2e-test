---
id: TC-FA-MYASSET-E2E-003-plan-tanpa-borrowing-dan-assignment
title: "Item My Asset menurut level plan tanpa baris berjalan: disembunyikan dan URL ditolak bila Borrowing dan Assignment None, tetap tampil bila hanya salah satu None"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§9.10#p1"]
smoke: []
dependsOn: []
trace:
  "§9.10#p1": [3, 6, 9, 12, 13, 16, 19, 20]
anchor: [2, 5, 11, 18]
coverage:
  web: automated
---

# Item My Asset menurut level plan tanpa baris berjalan: disembunyikan dan URL ditolak bila Borrowing dan Assignment None, tetap tampil bila hanya salah satu None

## Prerequisites
- Aktor: Borrower di entitas khusus dengan plan Borrowing `None` dan Assignment `None`; juga pengguna di entitas khusus dengan Borrowing `None` dan Assignment `Basic`, dan pengguna di entitas khusus dengan Borrowing `Basic` dan Assignment `None`. Ketiga entitas ini tidak dipakai spec lain.
- Layar awal: halaman FAMS yang memuat navbar.
- Data:
  - DU-003-1: Entitas `Entitas Level None {runId}` dengan Borrowing level `None` dan Assignment level `None`; Borrowing dan Assignment tidak tersedia pada plan itu.
  - DU-003-2: User `Hendra Saputra {runId}`, Borrower aktif di entitas DU-003-1, tanpa pinjaman berjalan dan tanpa penugasan berjalan.
  - DU-003-3: Entitas `Entitas Borrowing None {runId}` dengan Borrowing level `None` dan Assignment level `Basic`; Borrowing tidak tersedia dan Assignment tersedia pada plan itu.
  - DU-003-4: User `Rina Wijaya {runId}`, Borrower aktif di entitas DU-003-3, tanpa pinjaman berjalan dan tanpa penugasan berjalan.
  - DU-003-5: Entitas `Entitas Assignment None {runId}` dengan Borrowing level `Basic` dan Assignment level `None`; Borrowing tersedia dan Assignment tidak tersedia pada plan itu.
  - DU-003-6: User `Maya Anggraini {runId}`, Borrower aktif di entitas DU-003-5, tanpa pinjaman berjalan dan tanpa penugasan berjalan.
- Kondisi:
  - Borrowing dan Assignment sama-sama None pada plan entitas aktor.
  - `Hendra Saputra {runId}` tidak punya pinjaman maupun penugasan berjalan.
  - Borrowing `None` dan Assignment `Basic` pada plan entitas `Rina Wijaya {runId}`; ia tidak punya pinjaman maupun penugasan berjalan.
  - Borrowing `Basic` dan Assignment `None` pada plan entitas `Maya Anggraini {runId}`; ia tidak punya pinjaman maupun penugasan berjalan.
  - Akun `Rina Wijaya {runId}` dan `Maya Anggraini {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Item My Asset disembunyikan di menu profil saat Borrowing dan Assignment None tanpa pinjaman dan penugasan berjalan
1. Klik avatar di navbar
2. Verifikasi menu profil memuat item akun lain
3. Verifikasi tidak ada item `My Asset` di menu profil

### Akses langsung ke URL My Asset ditolak saat Borrowing dan Assignment None tanpa pinjaman dan penugasan berjalan
4. Buka halaman My Asset lewat alamat langsung
5. Verifikasi navbar tampil
6. Verifikasi akses ke halaman My Asset ditolak, tidak ada tab `Task`, `Borrowed`, `Assigned`, dan `History`

### Item My Asset tetap tampil dan URL tidak ditolak saat hanya Borrowing None dan Assignment tersedia tanpa pinjaman berjalan
7. Masuk sebagai `Rina Wijaya {runId}`
8. Klik avatar di navbar
9. Verifikasi item `My Asset` tampil di menu profil
10. Buka halaman My Asset lewat alamat langsung
11. Verifikasi halaman My Asset terbuka pada tab awal `Task` bagi `Rina Wijaya {runId}`
12. Verifikasi tab `Assigned` dan `History` tampil
13. Verifikasi tab `Borrowed` tidak tampil

### Item My Asset tetap tampil dan URL tidak ditolak saat hanya Assignment None dan Borrowing tersedia tanpa penugasan berjalan
14. Masuk sebagai `Maya Anggraini {runId}`
15. Klik avatar di navbar
16. Verifikasi item `My Asset` tampil di menu profil
17. Buka halaman My Asset lewat alamat langsung
18. Verifikasi halaman My Asset terbuka pada tab awal `Task` bagi `Maya Anggraini {runId}`
19. Verifikasi tab `Borrowed` dan `History` tampil
20. Verifikasi tab `Assigned` tidak tampil
