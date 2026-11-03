---
id: TC-FA-RP-E2E-105-require-approval-transaction-role-toggle-radio-aturan-dan-2
title: "Require Approval Transaction Role: toggle, radio aturan, dan pewarisan nilai (2/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-348
  - TC-FA-RP-349
  - TC-FA-RP-355
  - TC-FA-RP-360
coverage:
  web: automated
---

# Require Approval Transaction Role: toggle, radio aturan, dan pewarisan nilai (2/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya. Pelaku kedua yang hanya memicu state (penugasan Approver, penghapusan group) memakai sesi API Total Control kedua; kemampuan sesi API disediakan tim BE/FE.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #18 (pohon group Company Alpha, termasuk `Dock 1`), #19 (Require Approval OFF di semua node; Approver Pandu Wijaya hanya pada `IT Infrastructure`).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: menghapus group lewat sesi API (disediakan tim FE/BE tanpa endpoint karangan).
- State yang diubah dan pemulihannya: Require Approval dan penugasan Approver sub-tab `Disposal` dan `Damaged` pada `IT Infrastructure`, `Data Center`, dan `Helpdesk`; group `Dock 1` dihapus oleh TC-FA-RP-355 dan dipulihkan sesuai aturan pemulihan fixture destruktif pada TC. Hook `after` memulihkan Pre-setup #18 dan #19 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Klik Tab `Transaction Role`

### TC-FA-RP-348: Require Approval per node, nilai tidak diwariskan antar sibling

2. Tugaskan Approver Pandu Wijaya pada node `Data Center` sub-tab `Disposal` lewat sesi API hingga tersimpan
3. Klik node `Data Center` pada Sidebar Group Tree
4. Klik sub-tab `Disposal`
5. Aktifkan toggle `Require Approval for Disposal`
6. Klik node `Helpdesk` pada Sidebar Group Tree
7. Klik sub-tab `Disposal`
8. Verifikasi toggle `Require Approval for Disposal` node `Helpdesk` OFF

### TC-FA-RP-349: Nilai Require Approval independen antar sub-tab pada node yang sama

9. Klik node `IT Infrastructure` pada Sidebar Group Tree
10. Klik sub-tab `Disposal`
11. Aktifkan toggle `Require Approval for Disposal` (precondition TC: toggle ON, tidak diasersi)
12. Klik sub-tab `Damaged`
13. Verifikasi toggle `Require Approval for Damaged` OFF pada node yang sama

### TC-FA-RP-360: Sebelum node dipilih, toggle, radio, tabel role, dan `[+ Assign]` Hidden

14. Klik node `All Groups` pada Sidebar Group Tree
15. Klik sub-tab `Disposal`
16. Verifikasi card prompt `Select a group from the sidebar to view and manage its approval settings.` tampil
17. Verifikasi toggle, radio, section role, dan `[+ Assign]` tidak tampil

### TC-FA-RP-355: Toggle pada node yang dihapus sesi lain

18. Klik node `Dock 1` pada Sidebar Group Tree
19. Klik sub-tab `Disposal`
20. Hapus group `Dock 1` lewat sesi API hingga terhapus
21. Aktifkan toggle `Require Approval for Disposal`
22. Verifikasi toast netral `This group is no longer available.`
23. Verifikasi Sidebar Group Tree di-refresh sehingga node `Dock 1` tidak lagi tampil
24. Verifikasi toggle kembali ke posisi semula (OFF)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah menjadi 348, 349, 360, 355: TC-FA-RP-355 menghapus group sehingga diletakkan di akhir (aksi yang menghapus data).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 7 (klik sub-tab sesudah pindah node), langkah 11 (mengaktifkan toggle sebagai precondition TC-FA-RP-349). TC-FA-RP-348 menyebut "setelah menugaskan Approver Pandu Wijaya pada node itu" sehingga penugasan dijalankan lewat sesi API (langkah 2) dan dipakai sebagai precondition TC, tidak diasersi.
- Pembagian TC lintas spec: TC-FA-RP-350 (dua sesi UI Total Control yang diasersi, kelas c) ada di spec 296. Pada TC-FA-RP-355 Sesi 2 hanya menghapus group dan memakai sesi API.
- Post Condition TC-FA-RP-355 ("Group `Dock 1` dipulihkan sesuai aturan pemulihan fixture destruktif") tidak punya langkah observasi di TC sehingga tidak diasersi; pemulihan dilakukan hook `after`.
- Temuan untuk QA:
  - TC-FA-RP-355 butir b menyebut "Sidebar Group Tree di-refresh" tanpa indikator yang teramati; spec mengasersi node `Dock 1` tidak lagi tampil (langkah 23).
  - TC-FA-RP-349 menulis "dengan toggle ON" sebagai kondisi node dan sub-tab tanpa menyebut cara menyiapkannya; spec mengaktifkan toggle lewat UI (langkah 11).
