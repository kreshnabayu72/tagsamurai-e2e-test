---
id: TC-FA-GRP-E2E-073-delete-tanpa-warning-user-tc-ro-du-home-group-non-aktif-dan-transaction-role-approver
title: "Delete Group: User TC/RO/Default User Saja, Home Group, User Non-Aktif/Temporary, dan Transaction Role Approver Memicu Dialog Konfirmasi Normal"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-225
  - TC-FA-GRP-226
  - TC-FA-GRP-980
  - TC-FA-GRP-1059
coverage:
  web: automated
---

# Delete Group: User TC/RO/Default User Saja, Home Group, User Non-Aktif/Temporary, dan Transaction Role Approver Memicu Dialog Konfirmasi Normal

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control (Pre-setup No 1: `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed lewat API di `before`, tanpa aset aktif): `Del Only TC` (tanpa user Group Role atau Group Manager di node; user Total Control, Read Only, dan Default User client tidak dihitung); `Del Home` (hanya dipakai sebagai Home Group `User Home 1`, tanpa role); `Del Inactive` dengan `User Inactive 1` (Activation Status non-aktif, ber-Group Role di node) dan `User Temp 1` (Temporary User, Temporary Until sudah lewat, ber-Group Role di node); `Del Approver Only` dengan `User Approver 1` (Transaction Role approver Transfer di node, tanpa Group Role atau Group Manager). Email user `<nama>+{runId}-073@qwertysystem.net`.
- Kemampuan teknis (disediakan tim FE/BE): seeding user non-aktif dan Temporary User yang Temporary Until-nya sudah lewat serta Transaction Role approver; tidak ada endpoint karangan.
- Cleanup di `after`: hapus sisa data milik spec lewat API.

## Test Steps

### TC-FA-GRP-225: User TC/RO/Default User saja tidak memicu warning

1. Buka elipsis `⋯` baris `Del Only TC`, pilih `Delete`
2. Verifikasi dialog konfirmasi normal dengan isi "Are you sure you want to delete it? This action cannot be undone."
3. Klik [Cancel]

### TC-FA-GRP-226: Home Group user tidak memicu warning

4. Buka elipsis `⋯` baris `Del Home`, pilih `Delete`
5. Verifikasi dialog konfirmasi normal dengan isi "Are you sure you want to delete it? This action cannot be undone."
6. Klik [Cancel]

### TC-FA-GRP-1059: Transaction Role approver tidak memicu warning

7. Buka elipsis `⋯` baris `Del Approver Only`, pilih `Delete`
8. Verifikasi dialog dengan title "Delete Group", bullet `Del Approver Only`, isi "Are you sure you want to delete it? This action cannot be undone.", tombol [Cancel] dan [Delete]
9. Klik [Cancel]

### TC-FA-GRP-980: User non-aktif dan Temporary User tetap dihitung

10. Buka elipsis `⋯` baris `Del Inactive`, pilih `Delete`
11. Verifikasi dialog warning dengan isi "This group has users assigned — deleting it will remove their group roles. This action cannot be undone. Are you sure you want to delete it?" (`User Inactive 1` dan `User Temp 1` tetap dihitung)
12. Klik [Delete] pada dialog
13. Verifikasi toast sukses "Success, group has been deleted."
14. Buka Settings > Role & Permission, pilih `User Inactive 1`
15. Verifikasi assignment Group Role `User Inactive 1` terlepas
16. Buka Settings > Role & Permission, pilih `User Temp 1`
17. Verifikasi assignment Group Role `User Temp 1` terlepas

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 3, 6, 9, 14, 16: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Urutan: dialog konfirmasi yang hanya dibaca dan dibatalkan lebih dulu, Delete yang menghapus data (TC-980) paling akhir (S-10).
- Temuan untuk QA:
  - TC-225 dan TC-226 hanya menyebut "dialog konfirmasi normal" di kolom Expected; spec mengasersi isi "Are you sure you want to delete it? This action cannot be undone." dan tidak menambah asersi title atau tombol.
  - TC-980 Post Condition (entri pencabutan Group Role A dan B di log Role & Permission dan Changelog: User) tidak punya langkah observasi; tidak diasersi (S-01).
