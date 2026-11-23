---
id: TC-FA-SU-E2E-476-tab-transaction-admin-log-assignment-format-assignee-dan-hover-pic-saat-tindakan
title: "Tab Transaction Admin Log Sub-tab Assignment: Format Assignee dan Hover PIC Saat Tindakan"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1189
coverage:
  web: automated
---

# Tab Transaction Admin Log Sub-tab Assignment: Format Assignee dan Hover PIC Saat Tindakan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Assignment berisi 4 baris: `ASG-20260720-0071` (Activity `Handed over`, Assignee Employee `Rina W`), `ASG-20260719-0070` (Activity `Approved`, Assignee Division `General Affairs` dengan PIC saat tindakan Budi Santoso), `ASG-20260717-0069` (Activity `Requested`), dan `ASG-20260715-0068` (Activity `Rejected`) sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan seed API (disediakan tim BE/FE): mengganti PIC Division `General Affairs` menjadi Hana Kusuma setelah tanggal tindakan `19/07/26` dan memulihkannya ke Pre-setup #29 (PIC Budi Santoso) di hook `after`. Efek pada Pre-setup: PIC Division `General Affairs` berubah sementara; spec tidak mengubah data lain.
- Kemampuan teknis (disediakan tim FE): membaca teks tooltip hover pada sel tabel.
- State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1189: Format Assignee dan hover PIC Division mengikuti PIC saat tindakan (Budi Santoso)

1. Ganti PIC Division `General Affairs` menjadi Hana Kusuma lewat sesi API hingga perubahan tersimpan
2. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Assignment
3. Verifikasi Assignee baris `ASG-20260720-0071` menampilkan `Rina W` dengan ikon User
4. Hover nilai Assignee baris `ASG-20260720-0071`
5. Verifikasi hover menampilkan nama lengkap `Rina Wijaya`
6. Verifikasi Assignee baris `ASG-20260719-0070` menampilkan `General Affairs` dengan ikon Division
7. Hover nilai Assignee baris `ASG-20260719-0070`
8. Verifikasi hover menampilkan `PIC: Budi Santoso`
9. Verifikasi hover tidak menampilkan `PIC: Hana Kusuma`
10. Verifikasi Activity keempat baris berurutan `Handed over`, `Approved`, `Requested`, `Rejected`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (memicu state lewat sesi API, R-20), langkah 2 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), dan hover pada langkah 4 dan 7.
- Klausa absence (langkah 9, `PIC: Hana Kusuma` tidak tampil) didahului `Verifikasi` positif `PIC: Budi Santoso` pada langkah 8 sebagai anchor pada surface yang sama (8b.2).
- Temuan untuk QA (S-15): (1) TC-FA-SU-1189 tidak menyebut cara mengganti PIC Division; spec memicunya lewat seed API (R-20) dan memulihkannya di hook `after`. (2) Format `Rina W` dan tooltip `PIC: [Full Name]` bersumber dari `assignment.md` §4.1; TC tidak menyebut tooltip kosong `No active PIC` sehingga tidak diasersi.
