---
id: TC-FA-FATR-E2E-034-gating-mts-read
title: "Gating Manage transaction settings (Read)"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [§2#r1, §2#r7, §4.3#r5, §4.8#r1, §4.8#r2, §4.8#r3, §4.8#r4, §4.8#r5, §4.8#r6, §4.8#r7, §4.8#r8, §4.8#r12, §4.8#p2, §9.4.2#r23, §9.11#r1, §9.2#b159]
smoke: []
dependsOn: []
trace:
  §2#r1: [4, 7, 9]
  §2#r7: [2, 7, 12, 17, 18]
  §4.3#r5: [12, 13, 14, 15]
  §4.8#r1: [2, 4]
  §4.8#r2: [5, 7]
  §4.8#r3: 9
  §4.8#r4: 12
  §4.8#r5: [13, 15]
  §4.8#r6: 16
  §4.8#r7: 17
  §4.8#r8: 18
  §4.8#r12: [23, 29, 30, 31, 32]
  §4.8#p2: [20, 25]
  §9.4.2#r23: [18, 20]
  §9.11#r1: [12, 16, 17]
  §9.2#b159: [23, 25]
anchor: [27, 28]
coverage:
  web: automated
---
# Gating Manage transaction settings (Read)

## Prerequisites
- Aktor: pemegang Global Role Manage transaction settings (Read) `Rani Wulandari {runId}`.
- Layar awal: Fixed Asset > Settings > Transaction Settings.
- Data:
  - DU-034-1: User `Rani Wulandari {runId}`, Global Role Manage transaction settings hanya Read (tanpa Update), bukan Total Control, tanpa Group Role Manage asset & TAG, ada di entitas aktor.
  - DU-034-2: Category leaf `Truk Angkut {runId}` di bawah Category induk `Armada {runId}`.
  - DU-034-3: pada tab Borrow Category `Truk Angkut {runId}`, field `Max duration` bernilai sendiri `12` dan field `Max extensions` Inherit, dibuat oleh aktor lain.
  - DU-034-4: Group `Proyek Cikarang {runId}`, ada di entitas aktor.
  - DU-034-5: Asset Name `Backhoe Loader {runId}`, aktif.
  - DU-034-6: override pada tab Borrow Category `Truk Angkut {runId}` dengan Scope `Asset Name`, Target `Backhoe Loader {runId}`, Overridden `Max duration (10 days)`, dibuat oleh aktor lain.
  - DU-034-7: override pada tab Borrow Category `Truk Angkut {runId}` dengan Scope `Group`, Target `Proyek Cikarang {runId}`, Overridden `Max duration (30 days)`, dibuat oleh aktor lain.
- Kondisi:
  - Akun `Rani Wulandari {runId}` aktif dan dapat dipakai masuk.

## Test Steps

### Pemegang Manage transaction settings (Read) melihat halaman dan header
1. Ketik Search Sidebar Category Tree `Truk Angkut {runId}`, tekan Enter
2. Verifikasi Sidebar Category Tree menampilkan `All categories` dan Category `Truk Angkut {runId}`
3. Klik Category `Truk Angkut {runId}`
4. Verifikasi tab `Borrow`, `Assign`, `Transfer`, dan `Disposal` tampil
5. Verifikasi tombol `[Export rules]` tampil dan aktif
6. Klik `[Export rules]`
7. Verifikasi berkas aturan terunduh langsung tanpa dialog
8. Klik ikon `Changelog` pada header halaman
9. Verifikasi dialog `Changelog: Transaction Settings` tampil
10. Klik `✕` pada dialog Changelog

### Kontrol field disabled dan tombol Set own value serta Reset to inherit tidak dirender
11. Klik tab `Borrow`
12. Verifikasi kontrol field `Max duration` disabled dengan nilai `12`
13. Verifikasi tombol `[Reset to inherit]` tidak dirender pada field `Max duration`
14. Verifikasi field `Max extensions` menampilkan teks `Inherit` beserta sumbernya
15. Verifikasi tombol `[Set own value]` tidak dirender pada field `Max extensions`
16. Verifikasi tombol `[Reset to Default]` tampil dan disabled
17. Verifikasi tombol `[Save]` tampil dan disabled

### Tombol + Override disabled dengan alasan
18. Verifikasi tombol `[+ Override]` tampil dan disabled
19. Arahkan kursor ke tombol `[+ Override]`
20. Verifikasi alasan `You don't have permission to add overrides.` tersampaikan pada tombol `[+ Override]` yang disabled

### Delete override baris disabled dengan alasan dan seleksi bulk tidak tersedia
21. Ketik Search tabel Overrides `{runId}`, tekan Enter
22. Klik menu `⋯` pada baris `Backhoe Loader {runId}`
23. Verifikasi item `Delete` disabled untuk baris override dengan Scope `Asset Name`
24. Arahkan kursor ke item `Delete`
25. Verifikasi alasan `This override is outside your scope.` tersampaikan pada item `Delete` yang disabled
26. Tekan Esc untuk menutup menu baris
27. Verifikasi baris dengan Scope `Asset Name` dan Target `Backhoe Loader {runId}` tampil di tabel Overrides
28. Verifikasi baris dengan Scope `Group` dan Target `Proyek Cikarang {runId}` tampil di tabel Overrides
29. Verifikasi checkbox seleksi pada baris `Backhoe Loader {runId}` tidak dirender[^drift-1]
30. Verifikasi checkbox seleksi pada baris `Proyek Cikarang {runId}` tidak dirender[^drift-1]
31. Verifikasi checkbox pemilih semua baris pada header tabel Overrides tidak dirender[^drift-1]
32. Verifikasi tombol aksi bulk tidak tampil pada toolbar tabel Overrides[^drift-1]

[^drift-1]: Drift PRD vs foundation. PRD §4.8 (sel Delete baris dan bulk) dan §4.1 DO-15: aktor tanpa hak tulis dapat mencentang baris lalu aksi bulk `Delete` disabled dengan tooltip tersendiri. foundation `functions/entity-isolation.md` §18.4 Aturan kolom 3: kolom checkbox seleksi Hidden dan bar aksi bulk Hidden total untuk aktor tanpa hak tulis sama sekali, sehingga baris tidak bisa dicentang. Diasersi: foundation, karena checkbox seleksi dan bar aksi bulk tabel adalah pola bersama (SB-4).
