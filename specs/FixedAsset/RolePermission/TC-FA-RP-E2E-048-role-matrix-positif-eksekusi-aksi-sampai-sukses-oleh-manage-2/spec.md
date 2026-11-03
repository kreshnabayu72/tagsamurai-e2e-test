---
id: TC-FA-RP-E2E-048-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-manage-2
title: "Role Matrix Positif: eksekusi aksi sampai sukses oleh Manage global user & role (Update) (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-167
  - TC-FA-RP-168
  - TC-FA-RP-169
  - TC-FA-RP-170
coverage:
  web: automated
---

# Role Matrix Positif: eksekusi aksi sampai sukses oleh Manage global user & role (Update) (2/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage global user & role (Update) (Hendra Wijaya); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (fixture baru, belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-FA-RP-167 sampai TC-FA-RP-170 | Manage global user & role (Update) | Manage dengan Update | Hendra Wijaya (Pre-setup #6) | `murGlobal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GLOBAL_PASSWORD` |

- Data Pre-setup yang dibaca dan diubah: pool pengguna #15 (Budi Santoso), pohon group #18, dan seed Role Transaksi #19 pada `IT Infrastructure` sub-tab `Disposal` (Putri Wulandari sebagai Staff, Pandu Wijaya sebagai Approver, Require Approval OFF). Budi Santoso, Budi Setiawan, dan Ahmad Fauzi tidak memegang role yang disentuh pada awal spec (seed hook `before`). Hook `after` memulihkan Require Approval ke OFF dan aturan OR, mengembalikan Putri Wulandari ke Staff, dan menghapus penugasan Budi Santoso (pengecualian S-06 2026-10-30: pemulihan dijamin fixture backend yang disediakan tim FE/BE dan dinyatakan di `suite.md`, Hook suite, Pre-setup bersama).
- State global yang diubah: Require Approval `Disposal` pada `IT Infrastructure` dan penugasan Role Transaksi (dipulihkan hook `after`).

## Test Steps

1. Klik Tab Transaction Role
2. Klik node `IT Infrastructure` di Sidebar Group Tree
3. Klik sub-tab `Disposal`

### TC-FA-RP-167: Assign Role Transaksi sampai sukses

4. Klik `[+ Assign]` pada section Asset Admin
5. Pilih Budi Santoso pada popup Assign
6. Klik `[Assign]`
7. Verifikasi Toast sukses `Success, Asset Admin has been assigned.`
8. Verifikasi Baris Budi Santoso masuk section Asset Admin

### TC-FA-RP-168: Remove Role Transaksi sampai sukses

9. Klik `⋯` pada baris Putri Wulandari (Staff)
10. Klik `Remove`
11. Verifikasi Dialog `Remove Staff` tampil dengan bullet `Putri W` dan `This user will no longer be assigned to this role for IT Infrastructure.`
12. Klik `[Remove]` pada dialog
13. Verifikasi Toast sukses `Success, Staff has been removed.`

### TC-FA-RP-169: Toggle Require Approval ON sampai sukses

14. Aktifkan toggle `Require Approval for Disposal`
15. Verifikasi Toast sukses `Success, permissions have been updated.`
16. Verifikasi Toggle `Require Approval for Disposal` ON
17. Verifikasi Radio `Any approver (OR)` terpilih tampil

### TC-FA-RP-170: Ubah radio aturan ke AND sampai sukses

18. Pilih radio `All approvers (AND)`
19. Verifikasi Toast sukses `Success, approval rule has been updated.`
20. Verifikasi Radio `All approvers (AND)` terpilih

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik tab (langkah 1); klik tab, node, dan sub-tab untuk membuka tabel Role Transaksi (langkah 1, 2 dan 3).
- Urutan TC mengikuti nomor TC; toggle ON dari TC-FA-RP-169 dipakai sebagai kondisi awal TC-FA-RP-170 dalam spec yang sama, sehingga TC tersebut dijalankan berurutan dan tidak berdiri sendiri.
- Pembagian TC lintas spec: TC-FA-RP-163 sampai TC-FA-RP-166 ada di spec 047.
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - TC-FA-RP-167 Expected tidak menyebut jumlah baris atau urutan section; spec hanya mengasersi baris Budi Santoso masuk section Asset Admin.
  - TC-FA-RP-169 Langkah Uji memilih `Require Approval for Disposal` ON tanpa menyebut prasyarat aktivasi; Approver Pandu Wijaya dari Pre-setup #19 sudah ada.
  - TC-FA-RP-170 Precondition menyebut toggle ON; spec mengandalkan hasil langkah TC-FA-RP-169 pada spec yang sama (toggle ON dibangun langkah sebelumnya) dan state akhir dipulihkan hook `after`.
  - Post Condition TC tidak memuat langkah observasi sehingga tidak diasersi.
