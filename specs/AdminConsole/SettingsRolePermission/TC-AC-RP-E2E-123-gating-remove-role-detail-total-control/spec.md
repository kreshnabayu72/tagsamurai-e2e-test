---
id: TC-AC-RP-E2E-123-gating-remove-role-detail-total-control
title: "Gating Remove Role Detail untuk Aktor Total Control: Diri Sendiri dan Dialog Auto-revert"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-117
  - TC-AC-RP-118
coverage:
  web: automated
---

# Gating Remove Role Detail untuk Aktor Total Control: Diri Sendiri dan Dialog Auto-revert

## Prerequisites

- Mode: FE+BE. Spec hanya mengamati state, tooltip, dan dialog; dialog konfirmasi `Remove` dibatalkan dengan `[Cancel]` sehingga tidak ada perubahan state server.
- Akun aktor: Total Control Principal `Siti Nurhaliza`, `totalControlRP_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman `Settings > Role & Permission` dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Nama env `AC_RP_TC_PASSWORD` baru dan perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Data Pre-setup (identitas dirujuk lewat fixture `acRolePermission`, belum ada, dibuat pada tahap script): #1 (`Siti Nurhaliza`), #11 (tree group Principal: `Region Jawa`), #13 (Total Control `Rina Wijaya`, tampil `Rina W` pada dialog), #15 (Group Role `Manage distributor` untuk baris `Rina Wijaya` pada `Region Jawa`; Role Global `Manage device master data`).
- Data Dinamis: tidak ada; spec tidak membuat data sehingga tidak ada seeding, suffix `+{runId}-123`, maupun cleanup.
- Flag Guided Tooltip halaman ini, pemulihan baseline, dan sesi API aktor mengikuti pernyataan di `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-117: Remove dan checkbox baris diri sendiri Disabled

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
3. Hover checkbox multi-select baris `Siti Nurhaliza`
4. Verifikasi checkbox multi-select baris `Siti Nurhaliza` Disabled dengan tooltip "You can't manage your own account from here."
5. Klik `⋯` baris `Siti Nurhaliza`
6. Hover aksi `Remove`
7. Verifikasi aksi `Remove` baris `Siti Nurhaliza` Disabled dengan tooltip "You can't manage your own account from here."
8. Tutup overlay `⋯` dengan Esc

### TC-AC-RP-118: Total Control: Remove baris TC/RO/GM-target enabled dan memicu dialog auto-revert

9. Buka halaman `Settings > Role & Permission`
10. Klik tab `System`
11. Pada section Group Role, klik `⋯` pada baris `Manage distributor` lalu klik `Detail`
12. Klik node `Region Jawa`
13. Klik `⋯` baris `Rina Wijaya`
14. Verifikasi aksi `Remove` baris `Rina Wijaya` enabled
15. Klik `Remove`
16. Verifikasi dialog yang tampil adalah dialog auto-revert Total Control dengan Title "Remove Total Control" (bukan dialog "Remove Role")
17. Verifikasi dialog memuat Title "Remove Total Control", body "These users will lose Total Control access:" dengan bullet • Rina W, teks "Are you sure you want to remove it?" (tanpa kata "edit"), serta tombol `[Cancel]` dan `[Remove]`
18. Klik `[Cancel]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pembagian TC lintas spec: TC-AC-RP-115, 116, dan 119 (aktor Manage user and role) ada di spec 032.
- Langkah penghubung (S-03, S-08): langkah 8 (menutup overlay `⋯`), langkah 9 (membuka halaman kembali dari Role Detail Global menuju Group Role), dan langkah 18 (`[Cancel]` pada dialog konfirmasi agar tidak ada yang dihapus). Langkah 1 dan 10 membuka Tab System yang dibutuhkan langkah berikutnya (S-14).
- Hover pada langkah 3 dan 6 mendahului asersi tooltip (bagian 8b butir 5).
- Dialog konfirmasi pada langkah 17 diasersi sebagai satu elemen karena judul, isi, dan tombolnya disebut utuh dalam Expected TC-AC-RP-118 (S-01).
- Temuan untuk QA:
  - TC-AC-RP-118 tidak menyatakan penutupan dialog setelah Expected; spec menambah `[Cancel]` sebagai langkah penghubung agar baris `Rina Wijaya` tidak terhapus (Post Condition TC bernilai "-").
  - TC-AC-RP-117 Expected tidak membedakan state `Disabled` tooltip untuk checkbox dan `Remove` secara terpisah; spec mengasersi keduanya sesuai kalimat TC dengan hover masing-masing.
