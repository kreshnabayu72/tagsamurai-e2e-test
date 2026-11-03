---
id: TC-FA-SU-E2E-084-kunci-transaction-role-bagi-aktor-ber-scope-grup-dan-target-tier
title: "Kunci Transaction Role bagi Aktor Ber-scope Grup dan Target Tier"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-271
  - TC-FA-SU-273
  - TC-FA-SU-1060
coverage:
  web: automated
---

# Kunci Transaction Role bagi Aktor Ber-scope Grup dan Target Tier

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal: Manage user & role Group (Update, Finance & Accounting) Sinta Dewi (Pre-setup #6), email disediakan tim FE (tidak tertulis di Pre-setup TC), kredensial `Spectra.env.FA_MURGR_UPD_PASSWORD`. Login di hook `before` spec ini (akun pertama spec); halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun kedua (ganti akun eksplisit): Manage global user & role (Update) Qori Akbar (Pre-setup #4), email disediakan tim FE (tidak tertulis di Pre-setup TC), kredensial `Spectra.env.FA_MURG_UPD_PASSWORD`.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21), penugasan (Pre-setup #23), dan Transaction Role (Pre-setup #39).
- Pengguna target: Yuda Pratama (7 baris Transaction Role contoh PRD; baris Missing × Approver pada Branch Surabaya, General Affairs, dan Logistics Warehouse berada di luar scope Sinta Dewi) untuk TC-FA-SU-271; Lina Marlina (Total Control dengan Transaction Role) dan Citra Lestari (Read Only) untuk TC-FA-SU-273 dan 1060.
- Kemampuan teknis: klien HTTP dengan token sesi aktor untuk permintaan langsung (TC-FA-SU-273, disediakan tim FE/BE).
- State global yang diubah: tidak ada; semua aksi ditolak atau hanya dibaca.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-271: Baris Transaction Role memuat grup di luar scope aktor ber-scope grup: checkbox dan Remove Disabled dengan tooltip

1. Buka Detail Yuda Pratama > Tab Role > Sub-tab Transaction Role lalu hover checkbox pada baris Missing × Approver
2. Verifikasi checkbox baris Missing × Approver Disabled dengan tooltip "You don't have permission to edit."
3. Klik `⋯` pada baris Missing × Approver lalu hover `Remove`
4. Verifikasi aksi `Remove` baris Missing × Approver Disabled dengan tooltip "You don't have permission to edit."
5. Klik Select All
6. Verifikasi Select All tidak memilih baris yang memuat grup di luar scope
7. Verifikasi `[Bulk Remove]` tidak mencakup baris tersebut
8. Klik `[Assign Group]` pada baris Missing × Approver
9. Verifikasi grup di luar scope yang ter-assign (Branch Surabaya, General Affairs, Logistics Warehouse) tercentang dan Disabled dengan tooltip "You don't have permission to edit."
10. Klik `[✕]` pada popup Assign Group dan klik Unselect All

### TC-FA-SU-273: Target Total Control atau Read Only bagi aktor Manage user & role: Remove dan checkbox Disabled dengan tooltip tier

11. Ganti akun: logout lalu login sebagai Manage global user & role (Update) Qori Akbar
12. Buka Detail Lina Marlina > Tab Role > Sub-tab Transaction Role lalu klik `⋯` pada satu baris dan hover `Remove`
13. Verifikasi aksi `Remove` baris Transaction Role Lina Marlina Disabled dengan tooltip "You don't have permission to edit."
14. Hover checkbox baris yang sama
15. Verifikasi checkbox baris Transaction Role Lina Marlina Disabled dengan tooltip "You don't have permission to edit."
16. Kirim permintaan langsung ke API assign Transaction Role untuk Lina Marlina memakai klien HTTP hingga respons diterima
17. Verifikasi respons permintaan langsung ditolak server dengan status 403

### TC-FA-SU-1060: Target Total Control dan Read Only bagi aktor Manage global user & role: [+ Assign] dan [Assign Group] Disabled dengan tooltip S-15

18. Hover `[+ Assign]` pada Detail Lina Marlina > Tab Role > Sub-tab Transaction Role
19. Verifikasi tombol `[+ Assign]` tampil (Show) tetapi Disabled dengan tooltip "You don't have permission to edit."
20. Hover `[Assign Group]` pada satu baris
21. Verifikasi `[Assign Group]` Disabled dengan tooltip "You don't have permission to edit."
22. Hover checkbox pada baris yang sama
23. Verifikasi checkbox baris Disabled dengan tooltip "You don't have permission to edit."
24. Verifikasi tidak ada baris terpilih dan `[Bulk Remove]` tidak dapat dipicu
25. Buka Detail Citra Lestari > Tab Role > Sub-tab Transaction Role lalu hover `[+ Assign]`
26. Verifikasi tombol `[+ Assign]` tampil tetapi Disabled dengan tooltip "You don't have permission to edit."

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Spec ditulis per blok role karena ganti akun menuntut langkah eksplisit (bagian 3a, `[KEPUTUSAN 2026-10-30]`); judulnya tanpa kata Positif atau Negatif.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 10.
- `P-5` butir b: permintaan langsung ke API pada TC-FA-SU-273 (kelas a) adalah satu TC objek-uji ringan tanpa harness eksternal; asersinya hanya status respons 403 (bagian 8b butir 1). Perilaku FE untuk respons itu tidak diasersi.
- Temuan untuk QA:
  - TC-FA-SU-273 butir b menyebut "assign atau remove" ditolak 403, tetapi langkah 4 hanya mengirim permintaan assign; spec mengasersi permintaan assign saja.
  - TC-FA-SU-271 menyebut "baris yang memuat ≥1 grup di luar scope" tanpa menyebut baris mana yang dipakai; spec memakai baris Missing × Approver Yuda Pratama sebagai baris terkunci.
