---
id: TC-AC-RP-E2E-065-toggle-require-approval-manage-user-and-role
title: "Toggle Require Approval oleh Aktor Manage user and role (Update)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-440
  - TC-AC-RP-441
coverage:
  web: automated
---

# Toggle Require Approval oleh Aktor Manage user and role (Update)

## Prerequisites

- Mode: FE+BE (penahanan respons lewat intercept di atas backend nyata untuk TC-AC-RP-440).
- Akun aktor: Manage user and role dengan Update `manageUserRoleU_automated_{namaCompany}@qwertysystem.net` (nama tampil `Hendra Wijaya`), password `Spectra.env.AC_RP_MUR_U_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_RP_MUR_U_PASSWORD` harus terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group `Region Jawa` dengan anak `Jakarta`; `Sumatera`), #17 (toggle `Manage allocation` `Region Jawa` ON, `Sumatera` OFF tersimpan, group lain tanpa nilai; `Manage wallet & pricing` seluruh group OFF).
- Data Dinamis: spec ini tidak membuat Data Dinamis; target aksi adalah toggle Pre-setup. Nilai bersuffix `+{runId}-065` tidak dipakai karena tidak ada data yang dibuat spec.
- Kemampuan teknis (Pre-setup #23): penundaan respons simpan toggle lewat intercept (TC-AC-RP-440) agar state sementara toggle "disabled selama proses" dapat diasersi sebelum respons dilepas.
- Perubahan Pre-setup: toggle `Manage allocation` `Sumatera` (ON) dan `Manage wallet & pricing` `Region Jawa` (ON). Pemulihan ke nilai awal memakai kemampuan reset baseline automation yang disediakan tim FE/BE, dijalankan di hook `before` dan `after`. Efek: Changelog Role Detail menerima entri perubahan toggle; Last Updated berubah.
- Suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip `guided_tooltip_seen_role-permission`: mengikuti pernyataan di Hook suite `suite.md`.

## Test Steps

### TC-AC-RP-440: Manage user and role (Update) mengubah toggle Require Approval for Allocation

1. Klik tab `System`
2. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
3. Klik node `Sumatera`
4. Tahan respons simpan toggle (intercept penundaan respons)
5. Klik toggle "Require Approval for Allocation"
6. Verifikasi toggle `Sumatera` berubah ke ON langsung
7. Verifikasi toggle disabled selama proses
8. Lepas tahanan respons
9. Verifikasi toast "Success, permissions have been updated."
10. Klik node `Region Jawa`
11. Verifikasi toggle `Region Jawa` tetap ON
12. Klik node `Jakarta`
13. Verifikasi toggle `Jakarta` tetap OFF
14. Klik node `Sumatera`
15. Verifikasi nilai `Sumatera` ON tersimpan

### TC-AC-RP-441: Manage user and role (Update) mengubah toggle Require Approval for Wallet Allocation

16. Buka halaman `Settings > Role & Permission`
17. Klik tab `System`
18. Pada section Group Role, klik `⋯` pada baris `Manage wallet & pricing` lalu klik `Detail`
19. Klik node `Region Jawa`
20. Klik toggle "Require Approval for Wallet Allocation"
21. Verifikasi toggle ON
22. Verifikasi toast "Success, permissions have been updated."
23. Buka halaman `Settings > Role & Permission`
24. Klik tab `System`
25. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
26. Klik node `Region Jawa`
27. Verifikasi toggle `Manage allocation` tidak berubah (tetap ON)

## Notes

- Mode: FE+BE (penahanan respons). Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Tanda "→" pada kolom Langkah Uji TC tidak diasersi.
- Langkah penghubung (S-03): langkah 4 dan 8 (tahan dan lepas respons), 14 (kembali ke node `Sumatera` sebagai langkah observasi nilai tersimpan), 16 sampai 19 dan 23 sampai 26 (navigasi ke Role Detail).
- Asersi state sementara (bagian 8b butir 5 dan 11): langkah 6 dan 7 ditulis sebelum respons dilepas (langkah 8); toast (langkah 9) sesudah respons dilepas.
- Temuan untuk QA:
  - TC-AC-RP-440 Expected "nilai `Sumatera` ON tersimpan" tidak punya langkah observasi di TC; spec mengamatinya dengan kembali ke node `Sumatera` (langkah 14 dan 15), bukan muat ulang halaman.
  - TC-AC-RP-440 Expected "disabled selama proses" adalah state sementara yang tidak teramati tanpa penundaan respons; TC tidak menyebut cara menahan respons. Spec memakai penundaan respons (Pre-setup #23).
  - TC-AC-RP-441 Expected "toggle `Manage allocation` tidak berubah" tidak menyebut group; spec memeriksa `Region Jawa` (nilai awal ON).
  - Mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD (S-13).
