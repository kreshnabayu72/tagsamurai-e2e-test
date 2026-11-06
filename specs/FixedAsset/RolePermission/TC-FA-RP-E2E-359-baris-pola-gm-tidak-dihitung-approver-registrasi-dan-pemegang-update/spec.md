---
id: TC-FA-RP-E2E-359-baris-pola-gm-tidak-dihitung-approver-registrasi-dan-pemegang-update
title: "Baris pola GM (Approver dan Manage asset & TAG Update) tidak dihitung: GM nonaktif tidak membuka prasyarat aktivasi registrasi dan Damaged"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-1202
coverage:
  web: automated
---

# Baris pola GM (Approver dan Manage asset & TAG Update) tidak dihitung: GM nonaktif tidak membuka prasyarat aktivasi registrasi dan Damaged

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada `Company Isolated` (Pre-setup #35). Email tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE, password `Spectra.env.FA_ISOLATED_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, bagian "Hook suite".
- Data Pre-setup (dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas belum ada, disediakan tim FE): #18 (struktur group, `Helpdesk` di bawah `IT Infrastructure`) dan #35 (`Company Isolated`: struktur group sama dengan #18; tanpa Group Manager; `Helpdesk` tanpa Approver manual dan tanpa pemegang Update `Manage asset & TAG`; Require Approval transaksi OFF di semua node; baris Approver pola Total Control tidak dihitung; Pandu Wijaya mencakup `Helpdesk` dari ancestor `IT Infrastructure` hanya pada sub-tab `Disposal`, sehingga sub-tab `Damaged` yang tanpa Approver manual di node mana pun, termasuk ancestor, dipakai untuk langkah Transaction Role).
- Kondisi awal yang di-seed di hook `before` (precondition TC, dipakai sebagai precondition, tidak diasersi): Kevin Susanto ditugaskan Group Manager di `Helpdesk` pada `Company Isolated` (baris pola GM tertulis, termasuk `Manage asset & TAG` Update dan Approver), lalu Status Kevin Susanto dinonaktifkan. `Helpdesk` tanpa pemegang Update lain dan tanpa Group Manager lain; sub-tab `Damaged` tanpa Approver manual yang mencakup. Seeding lewat kemampuan seeding API yang disediakan tim FE/BE (tanpa endpoint karangan).
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): Kevin Susanto dipulihkan ke state Pre-setup #35 (Active, tanpa penugasan Group Manager dan tanpa baris pola GM di `Helpdesk`), dan toggle `Require Approval for Registration` pada Detail Role `Manage asset & TAG` serta `Require Approval for Damaged` pada `Helpdesk` tetap OFF (dikembalikan ke OFF bila ternyata berubah). Dijamin fixture backend yang disediakan tim FE/BE. Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_ISOLATED_TC_PASSWORD` dan `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1202: baris pola GM tidak dihitung sebagai approver terdaftar atau pemegang Update

1. Buka Fixed Asset > Settings > Role & Permission > System dan klik Role Name `Manage asset & TAG` pada section Group Role
2. Klik node `Helpdesk` di Sidebar Group Tree
3. Aktifkan toggle `Require Approval for Registration`
4. Verifikasi dialog blok severity warning tampil dengan Title `Cannot Require Approval`, Body `Grant Update access on Manage asset & TAG to at least one user in this group, or assign a Group Manager to it, before enabling approval.`, dan satu tombol `[OK]`
5. Klik `[OK]`
6. Verifikasi toggle `Require Approval for Registration` kembali OFF
7. Buka Fixed Asset > Settings > Role & Permission > Transaction Role
8. Klik node `Helpdesk` di Sidebar Group Tree
9. Klik sub-tab `Damaged`
10. Aktifkan toggle `Require Approval for Damaged`
11. Verifikasi dialog blok `Cannot Require Approval` tampil
12. Verifikasi toggle `Require Approval for Damaged` kembali OFF
13. Klik `[OK]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 13 langkah.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): membuka Detail Role, klik node, membuka tab Transaction Role dan sub-tab (langkah 1, 2, 7 sampai 9); langkah 13 menutup dialog blok sebagai langkah penghubung (TC tidak menyebut cara menutup dialog langkah 5; hasil toggle langkah 12 diamati sebelum dialog ditutup).
- Pembagian TC lintas spec: TC-FA-RP-1202 hanya ada di spec ini. Post Condition TC ("Kevin Susanto dipulihkan ke state Pre-setup #35 oleh automation baseline") tidak punya langkah observasi di TC dan tidak diasersi; pemulihan ada di hook `after` (Prerequisites).
- Temuan untuk QA:
  - Akun login Total Control `Company Isolated` tidak tertulis di Pre-setup TC (#35 hanya menyebut "Total Control tersedia"); akun disediakan tim FE.
  - TC-FA-RP-1202 Precondition d menugaskan Kevin Susanto Group Manager di `Helpdesk` pada `Company Isolated` (lalu dinonaktifkan), sedangkan Pre-setup #35 menyebut `Company Isolated` tanpa Group Manager dan Pre-setup #13 dan #43 menyebut Kevin Susanto Group Manager hanya di `Data Center`; Pre-setup #38 menyebut Kevin Susanto di `Data Center` dan `Helpdesk` pada Company Alpha. Keberadaan user Kevin Susanto pada `Company Isolated` dan state seed-nya tidak ditetapkan di Tabel Data Uji; spec men-seed kondisi precondition d dan hal ini perlu rekonsiliasi.
  - Copy dialog `Cannot Require Approval` beserta Body pada langkah 4 bertanda `copy usulan, PRD 12 #7` pada kolom Sumber PRD (D-11); spec menyalin teks TC persis dan bergantung pada persetujuan PM.
  - TC-FA-RP-1202 Expected c hanya menyebut Title dialog `Cannot Require Approval` untuk `Damaged` tanpa Body dan tanpa tombol; spec mengasersi Title saja (langkah 11). Tidak ada rujukan cara menutup dialog.
  - TC-FA-RP-1202 mensyaratkan Kevin Susanto Inactive tetapi tidak menyebut cara menonaktifkannya; spec men-seed lewat seeding API.
