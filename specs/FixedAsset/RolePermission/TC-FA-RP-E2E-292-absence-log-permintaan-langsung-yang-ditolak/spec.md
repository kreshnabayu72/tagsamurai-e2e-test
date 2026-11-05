---
id: TC-FA-RP-E2E-292-absence-log-permintaan-langsung-yang-ditolak
title: "Absence log: permintaan langsung yang ditolak"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-913
  - TC-FA-RP-957
  - TC-FA-RP-961
  - TC-FA-RP-983
  - TC-FA-RP-1098
coverage:
  web: automated
---

# Absence log: permintaan langsung yang ditolak

## Prerequisites

- Mode: FE+BE.
- Akun aktor 1: Read Only Dewi Anggraini (Pre-setup #4), `readOnly_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_RO_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Seluruh langkah spec ini adalah request langsung ke server lewat sesi API aktor (bagian 8b butir 1), sehingga UI tidak dipakai langkah.
- Akun aktor sesi API berikutnya (ganti akun eksplisit pada langkah 5, 10, dan 19): Total Control pada `Company Isolated` (Pre-setup #35), akun disediakan tim FE (email tidak tertulis di Pre-setup TC; lihat Temuan untuk QA), `Spectra.env.FA_ISOLATED_TC_PASSWORD`; Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`; Total Control pada `Client Suspended` (Pre-setup #25), akun disediakan tim FE (email tidak tertulis di Pre-setup TC; lihat Temuan untuk QA), `Spectra.env.FA_SUSPENDED_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Env var yang dipakai: `FA_RO_PASSWORD`, `FA_ISOLATED_TC_PASSWORD`, `FA_TC_PASSWORD`, `FA_SUSPENDED_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #15 (Ahmad Fauzi pada `Manage accounting`), #17 (Indra Kusuma tanpa Home Group), #18, #19, #20 (Approval Scope `Transfer` pada `IT Infrastructure` bernilai `Both`), #25 (`Client Suspended`), dan #35 (`Company Isolated`: `Helpdesk` sub-tab `Damaged` tanpa Approver yang mencakup dan tanpa Group Manager, Require Approval `Damaged` Off; Pandu Wijaya mencakup `Helpdesk` hanya pada sub-tab `Disposal`). Disiapkan lewat seeding di hook `before`.
- Kemampuan teknis: klien HTTP untuk request langsung ke server dan sesi API tiap aktor (disediakan tim FE/BE; tanpa endpoint karangan). Kemampuan teknis: kemampuan baca jumlah entri (disediakan tim FE/BE, tanpa endpoint karangan, bagian 8b butir 10) untuk Changelog surface terkait, System Log aktor, dan Activity Log; baseline dicatat per TC sebelum aksi pemicu dan asersi memakai perbandingan dengan baseline, bukan angka absolut (S-12).
- State global: status `Client Suspended` tidak diubah; spec tidak mengubah data karena semua request ditolak.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status tenant) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis kecuali dinyatakan lain. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-RP-913: Read Only mengedit CRUD ditolak server, tidak ada entri log

1. Catat baseline jumlah entri Changelog Detail Role `Manage accounting`, System Log Dewi Anggraini, dan Activity Log lewat kemampuan baca jumlah entri
2. Kirim request langsung ke server (bukan lewat UI) dengan sesi API Read Only untuk mengubah Create baris Ahmad Fauzi pada `Manage accounting`
3. Verifikasi respons status `403` dengan pesan `You don't have permission to do this.`
4. Verifikasi jumlah entri Changelog Detail Role `Manage accounting`, System Log Dewi Anggraini, dan Activity Log sama dengan baseline (tidak ada entri log baru)

### TC-FA-RP-957: Mengaktifkan Require Approval tanpa prasyarat ditolak server, tidak ada entri log

5. Ganti akun: gunakan sesi API Total Control pada `Company Isolated` dengan `Spectra.env.FA_ISOLATED_TC_PASSWORD`
6. Catat baseline jumlah entri Changelog Transaction Role, System Log Total Control `Company Isolated`, dan Activity Log lewat kemampuan baca jumlah entri
7. Kirim request langsung ke server (bukan lewat UI) untuk mengaktifkan Require Approval `Damaged` pada node `Helpdesk` tanpa Approver yang mencakup dan Group Manager (sub-tab `Damaged`)
8. Verifikasi respons status `422`
9. Verifikasi jumlah entri Changelog Transaction Role, System Log Total Control `Company Isolated`, dan Activity Log sama dengan baseline (tidak ada entri log baru)

### TC-FA-RP-961: Radio aturan persetujuan di luar enum ditolak validasi skema, tidak ada entri log

10. Ganti akun: gunakan sesi API Total Control Siti Rahmawati dengan `Spectra.env.FA_TC_PASSWORD`
11. Catat baseline jumlah entri Changelog Transaction Role, System Log Siti Rahmawati, dan Activity Log lewat kemampuan baca jumlah entri
12. Kirim request langsung ke server (bukan lewat UI) untuk menyimpan aturan persetujuan `Disposal` dengan nilai `majority`
13. Verifikasi respons status `422`
14. Verifikasi jumlah entri Changelog Transaction Role, System Log Siti Rahmawati, dan Activity Log sama dengan baseline (tidak ada entri log baru)

### TC-FA-RP-1098: Radio Approval Scope di luar enum ditolak validasi skema, tidak ada entri log

15. Catat baseline jumlah entri Changelog Transaction Role, System Log Siti Rahmawati, dan Activity Log lewat kemampuan baca jumlah entri
16. Kirim request langsung ke server (bukan lewat UI) untuk menyimpan Approval Scope `Transfer` pada `IT Infrastructure` dengan nilai `sideways`
17. Verifikasi respons status `422`
18. Verifikasi jumlah entri Changelog Transaction Role, System Log Siti Rahmawati, dan Activity Log sama dengan baseline (tidak ada entri log baru)

### TC-FA-RP-983: Client Suspended menolak permintaan langsung Set Home Group constraint, tidak ada entri log

19. Ganti akun: gunakan sesi API Total Control pada `Client Suspended` dengan `Spectra.env.FA_SUSPENDED_TC_PASSWORD`
20. Catat baseline jumlah entri Changelog User milik Indra Kusuma, System Log Total Control `Client Suspended`, dan Activity Log lewat kemampuan baca jumlah entri
21. Kirim request langsung ke server (bukan lewat UI) untuk menetapkan Home Group constraint `Data Center` pada Indra Kusuma pada `Client Suspended`
22. Verifikasi respons status `403` dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
23. Verifikasi jumlah entri Changelog User milik Indra Kusuma, System Log Total Control `Client Suspended`, dan Activity Log sama dengan baseline (tidak ada entri log baru)

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-913, 957, 961, 983, 1098).
- Kelas g (absence log): tiap TC punya aksi pemicu nyata, baseline sendiri (S-12), dan anchor positif sebelum asersi absence (bagian 8b butir 2). Pemicu adalah permintaan langsung ke server yang ditolak (`P-5` butir a); spec kelas a dan spec state tenant hanya mengasersi status respons dan state data (bagian 8b butir 1, S-05).
- Pembagian TC lintas spec: klausa "tidak ada entri log" TC-FA-RP-913, 957, 961, 983, dan 1098 diasersi di spec ini dengan aksi nyata dan baseline sendiri. Presence TC-FA-RP-983 ada di spec 279; spec lain mengasersi status respons dan state data untuk TC-FA-RP-913, 957, 961, dan 1098. Id TC tetap di `sourceTc` spec asal dan spec ini (S-05).
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): ganti akun sesi API (langkah 5, 10, 19); pencatatan baseline jumlah entri.
- Urutan TC: TC-FA-RP-913 (Read Only login di hook `before`), TC-FA-RP-957 (`Company Isolated`), TC-FA-RP-961 dan TC-FA-RP-1098 (Total Control Siti Rahmawati), lalu TC-FA-RP-983 (`Client Suspended`) agar tiap akun hanya diganti satu kali.
- Temuan untuk QA:
  - Akun Total Control `Company Isolated` (Pre-setup #35) dan `Client Suspended` (Pre-setup #25) tidak tertulis di Pre-setup #1 sampai #11; email dan password disediakan tim FE (S-11).
  - Expected "tidak ada entri log" pada TC-FA-RP-913, 957, 961, 983, dan 1098 tidak menyebut surface; spec membandingkan Changelog surface terkait (Transaction Role, Detail Role, atau `Changelog: User`), System Log aktor, dan Activity Log terhadap baseline. TC-FA-RP-983 tidak menyebut surface log Home Group constraint; spec memakai `Changelog: User` milik Indra Kusuma.
  - TC-FA-RP-961 tidak menyebut node target aturan persetujuan `Disposal` dan TC-FA-RP-957 memakai `Helpdesk` pada `Company Isolated` (Pre-setup #35) walau Precondition juga memuat #15 dan #18; spec memakai `Disposal` pada node `IT Infrastructure` untuk TC-FA-RP-961 sebagai dugaan dan tidak mengasersi node pada langkah.
