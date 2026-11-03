---
id: TC-FA-RP-E2E-001-screening-tab-total-control-read-only-group-manager-system-1
title: "Screening Tab Total Control, Read Only, Group Manager, System, dan loading state (1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1
  - TC-FA-RP-2
  - TC-FA-RP-4
  - TC-FA-RP-5
  - TC-FA-RP-6
coverage:
  web: automated
---

# Screening Tab Total Control, Read Only, Group Manager, System, dan loading state (1/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env, didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #12 (baris Maya Anggraeni di Tab Read Only), #15 dan #16 (pool pengguna; kandidat dan baris Tab Total Control), #18 (pohon group `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`, `Helpdesk`, `Logistics Warehouse` > `Dock 1`), #43 (seed Group Manager: Fajar Nugroho di `IT Infrastructure`, Kevin Susanto di `Data Center`, Lina Marlina di `Head Office`). Baris Default User (Admin Utama, Modified By `System`) berasal dari data tabel Tab Total Control Pre-setup #36.
- Data Dinamis: penugasan Group Manager Kevin Susanto di `Helpdesk` (precondition TC-FA-RP-6). Dibuat lewat sesi API aktor pada langkah 34 dan dicabut kembali di hook `after`.
- Fixture `Fixture.fixedAssetRolePermission` (`fixtures/fixedAssetRolePermission.json`) belum ada; kunci akun, nama group, dan nama pengguna yang dipakai spec ini ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor (login API dengan token yang tidak dihitung sebagai sesi web, lihat `suite.md`); hover untuk membaca tooltip dan path badge.
- Pemulihan: penugasan Kevin Susanto di `Helpdesk` dicabut di hook `after`; Pre-setup bersama lain tidak diubah spec ini.

## Test Steps

### TC-FA-RP-1: Screening Tab Total Control saat pertama dibuka (3 zona)

1. Verifikasi Breadcrumb tampil `Settings > Role & Permission > Total Control` pada halaman yang dibuka hook `beforeEach`
2. Verifikasi Tab tampil berurutan `Total Control (aktif) | Read Only | Group Manager | Transaction Role | System`
3. Verifikasi Table Tools tampil `Search | Filter | Download | Changelog | [+ Assign]`
4. Verifikasi deskripsi statis di bawah tab `Total Control applies to Fixed Asset only — it does not grant access to other TAG Samurai products.`
5. Verifikasi kolom tabel `Name (sortable) | Position (sortable) | Division (sortable) | Status (sortable) | Modified By (sortable) | Last Updated (sortable) | Column Visibility (⋯) (unsortable — header klik = buka overlay Column Visibility → CTA [Setup Column] di dalamnya, body per baris = row action menu)`
6. Verifikasi baris Default User dengan Modified By `System` dan baris Total Control lain tampil
7. Verifikasi tidak ada kolom Checkbox
8. Verifikasi pagination default 10 data per halaman
9. Verifikasi Bulk Action Bar tidak ada di tab ini

### TC-FA-RP-2: Breadcrumb Tab Total Control, segmen aktif bukan link

10. Verifikasi Breadcrumb tampil persis `Settings > Role & Permission > Total Control`
11. Verifikasi Breadcrumb berada di luar card halaman
12. Verifikasi tidak ada judul halaman besar
13. Klik segmen terakhir `Total Control` pada Breadcrumb
14. Verifikasi segmen terakhir `Total Control` adalah tab aktif dan bukan link
15. Verifikasi klik tidak memindahkan halaman (Tab `Total Control` tetap aktif)

### TC-FA-RP-4: Screening Tab Read Only saat dibuka (3 zona)

16. Klik Tab `Read Only`
17. Verifikasi Breadcrumb tampil `Settings > Role & Permission > Read Only`
18. Verifikasi Tab tampil berurutan `Total Control | Read Only (aktif) | Group Manager | Transaction Role | System`
19. Verifikasi Table Tools tampil `Search | Filter | Download | Changelog | [+ Assign]`
20. Verifikasi deskripsi statis `Read Only applies to Fixed Asset only — it does not grant access to other TAG Samurai products.`
21. Verifikasi kolom tabel `Name (sortable) | Position (sortable) | Division (sortable) | Status (sortable) | Modified By (sortable) | Last Updated (sortable) | Column Visibility (⋯) (unsortable — header klik = buka overlay Column Visibility → CTA [Setup Column] di dalamnya, body per baris = row action menu)`
22. Verifikasi baris Maya Anggraeni (Read Only) tampil
23. Verifikasi tidak ada kolom Checkbox
24. Verifikasi pagination default 10 data per halaman

### TC-FA-RP-5: Screening Tab Group Manager saat dibuka (3 zona dan Sidebar Group Tree)

25. Klik Tab `Group Manager`
26. Verifikasi Breadcrumb tampil `Settings > Role & Permission > Group Manager`
27. Verifikasi Tab tampil berurutan `Total Control | Read Only | Group Manager (aktif) | Transaction Role | System`
28. Verifikasi Table Tools tampil `Search | Filter | Download | Changelog | [+ Assign]`
29. Verifikasi kolom tabel `Name (sortable) | Group (sortable) | Position (sortable) | Division (sortable) | Status (sortable) | Modified By (sortable) | Last Updated (sortable) | Column Visibility (⋯) (unsortable — header klik = buka overlay Column Visibility → CTA [Setup Column] di dalamnya, body per baris = row action menu)`
30. Verifikasi tiga baris penugasan Group Manager tampil: Fajar Nugroho di `IT Infrastructure`, Kevin Susanto di `Data Center`, Lina Marlina di `Head Office`
31. Verifikasi tidak ada kolom Checkbox
32. Verifikasi pagination default 10 data per halaman
33. Verifikasi panel kanan menampilkan Sidebar Group Tree dengan node `All Groups` aktif

### TC-FA-RP-6: Kolom Group Tab Group Manager, badge dan hover path penuh

34. Lewat sesi API aktor, tugaskan Kevin Susanto sebagai Group Manager di `Helpdesk` hingga tersimpan, lalu muat ulang Tab `Group Manager`
35. Verifikasi Kevin Susanto tampil sebagai dua baris, satu per kombinasi user dan group (`Data Center` dan `Helpdesk`)
36. Verifikasi kolom Group menampilkan badge nama group penugasan langsung, bukan seluruh descendant
37. Arahkan kursor ke badge Group `Data Center` pada baris Kevin Susanto
38. Verifikasi hover badge `Data Center` menampilkan path penuh `Head Office > IT Infrastructure > Data Center`

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-1, 2, 4, 5, 6). Ada satu pemicu API (langkah 34); sesi API aktor memakai pernyataan di `suite.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): klik Tab `Read Only` dan `Group Manager`, klik segmen Breadcrumb, hover badge, serta langkah 34 yang menyiapkan precondition TC-FA-RP-6 (Kevin Susanto juga Group Manager di `Helpdesk`) dan memuat ulang tab. Halaman awal TC-FA-RP-1 dibuka hook `beforeEach` suite, padanan langkah 1 TC-FA-RP-1.
- Alasan di atas sekitar 35 langkah (38 langkah): seluruh blok satu topik (screening tab dan Breadcrumb pada halaman yang sama), kelas fungsional yang sama, dan tiap blok baca-saja kecuali satu pemicu API di blok terakhir; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-RP-1 precondition c ("belum pernah membuka halaman Role & Permission pada sesi ini") tidak dapat dijamin: hook `beforeEach` suite membuka halaman sebelum langkah pertama. Tampilan yang diasersi sama dengan hasil membuka menu dari sidebar.
  - TC-FA-RP-5 mengharapkan tiga baris penugasan (Pre-setup #43), sedangkan data tabel Tab Group Manager Pre-setup #38 berisi enam baris (termasuk Kevin Susanto di `Helpdesk`, Dimas Pranata di `Rack A1`, dan Cahyo Aji). Spec mengasersi tiga baris yang disebut TC-FA-RP-5 dan menyiapkan Kevin Susanto di `Helpdesk` hanya pada langkah 34; QA mengonfirmasi data Pre-setup yang berlaku untuk TC-FA-RP-5.
  - TC-FA-RP-1 menyatakan pagination default 10 data per halaman; dengan Pre-setup #36 (9 baris) tabel tidak berganti halaman, sehingga hanya ukuran halaman default yang dapat diamati.
  - Post Condition TC-FA-RP-6 tidak memberi langkah observasi tambahan; tidak diasersi.
