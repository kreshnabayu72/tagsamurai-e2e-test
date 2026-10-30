---
id: TC-GS-ROLE-E2E-021-aksesibilitas-keyboard-checkbox-detail-dan-focus-trap-dialog
title: "Aksesibilitas Keyboard: Checkbox Detail, Tooltip Saat Fokus, dan Focus Trap Dialog Remove"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-47
  - TC-GS-ROLE-48
coverage:
  web: automated
---

# Aksesibilitas Keyboard: Checkbox Detail, Tooltip Saat Fokus, dan Focus Trap Dialog Remove

## Prerequisites

- Mode: FE+BE.
- Akun: Ahmad Fauzi (Total Control), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD` (Pre-setup #1). Login dan navigasi dilakukan sekali di hook `before`. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup: Doni Pratama (Staff, IT; baris Manage TAG dengan Read checked dan Update unchecked, Pre-setup #10); Budi Santoso (Default User, Pre-setup #2); Dewi Lestari (Total Control, Inactive, Pre-setup #3).
- Spec mengubah satu data Pre-setup: Update baris Manage TAG milik Doni Pratama menjadi checked (langkah 12). Hook `after` memulihkan Update Doni Pratama ke unchecked lewat sesi API aktor Total Control (jalan walau spec gagal di tengah). Efek samping lain dari perubahan itu (entri Changelog Detail dan nilai Last Updated) tidak dipulihkan. TC-GS-ROLE-48 tidak mengubah data: dialog Remove baris Dewi Lestari ditutup dengan Esc.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: membuka Global Settings > Role & Permission > Tab Total Control.
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: menekan Tab, Space, dan Esc; membaca elemen yang sedang fokus; membaca tooltip yang tampil saat fokus pada checkbox disabled.

## Test Steps

### TC-GS-ROLE-48: Dialog konfirmasi Remove: focus trapped dan Esc menutup

1. Buka overlay (⋯) baris Dewi Lestari
2. Klik Remove
3. Verifikasi dialog konfirmasi tampil dengan tombol `[Cancel]` dan `[Remove]`
4. Tekan Tab berulang sampai fokus melewati elemen terakhir dialog
5. Verifikasi fokus berputar di dalam dialog (hanya berpindah antara `[Cancel]` dan `[Remove]`) dan tidak keluar dari dialog
6. Tekan Esc
7. Verifikasi dialog tertutup
8. Verifikasi tidak ada toast
9. Verifikasi baris Dewi Lestari tetap ada di Tab Total Control

### TC-GS-ROLE-47: Checkbox Detail operable keyboard dan tooltip saat fokus

10. Buka Detail "Manage TAG"
11. Tekan Tab sampai fokus di checkbox Update baris Doni Pratama, tekan Space
12. Verifikasi checkbox Update baris Doni Pratama checked
13. Verifikasi toast sukses `Success, permissions have been updated.`
14. Tekan Tab sampai fokus di checkbox Update baris Budi Santoso
15. Verifikasi checkbox Update baris Budi Santoso disabled menerima fokus
16. Verifikasi tooltip `Default User cannot be modified.` tampil saat fokus

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah: TC-GS-ROLE-48 dijalankan lebih dulu karena dimulai dari layar awal (Tab Total Control) dan tidak mengubah data, sedangkan TC-GS-ROLE-47 mengubah Update Doni Pratama dan pindah ke Detail sehingga ditaruh terakhir (tidak ada langkah navigasi tambahan).
- Langkah 4 dan 11 (Tab berulang dan Tab sampai fokus) adalah aksi keyboard; jumlah penekanan Tab ditentukan skrip sampai kondisi tercapai.
- Pembagian TC lintas spec: TC-GS-ROLE-41, 42, 43 ada di spec 019; TC-GS-ROLE-44, 45, 46 ada di spec 020; TC-GS-ROLE-77 (accessibility Popup Assign) ada di spec 023.
- Temuan untuk QA:
  - TC-GS-ROLE-48 langkah 1 ("Klik Remove pada baris Dewi Lestari") tidak menyebut overlay; spec membuka overlay `(⋯)` mengikuti TC-GS-ROLE-42.
  - TC-GS-ROLE-48 Expected b ("tanpa perubahan") tidak menyebut bukti selain baris Dewi Lestari tetap ada; spec menambah `Verifikasi` tidak ada toast (langkah 8) sebagai bukti tidak ada aksi yang dikirim.
  - TC-GS-ROLE-47 Expected a tidak menyebut efek lanjutan pada Changelog Detail; entri yang tercipta tidak dipulihkan.
  - TC-GS-ROLE-47 menyebut Update Doni Pratama unchecked sebagai precondition tetapi Doni Pratama adalah data Pre-setup bersama (Tabel Data Uji Pre-setup #10); TC tidak menyatakan pemulihannya.
