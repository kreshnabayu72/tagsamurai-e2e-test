---
id: TC-FA-SU-E2E-435-edit-home-group-mencabut-group-role-dan-role-transaksi-di-luar-constraint-silent
title: "Edit Home Group Mencabut Group Role dan Role Transaksi di Luar Constraint (Silent)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1125
coverage:
  web: automated
---

# Edit Home Group Mencabut Group Role dan Role Transaksi di Luar Constraint (Silent)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23), dan varian `FaUserHGT` (#51; kebutuhan tim FE, seed disediakan tim FE/BE sebelum eksekusi). Pengguna target: Gita Permata (Home Group Finance & Accounting): Group Role Manage group pada Finance & Accounting; Transaction Role Disposal × Asset Admin (Finance & Accounting), Disposal × Approver (Accounts Payable), dan Damaged × Staff (IT Infrastructure). Nama pengguna, grup, dan baris penugasan dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan seluruh penugasan Gita Permata ke kondisi Pre-setup #51 (aksi spec ini mencabut seluruh penugasan di luar constraint). Seed dijalankan di hook `before`, sebagai langkah penghubung terakhir (langkah 12), dan di hook `after` (cadangan). Efek pada Pre-setup: Home Group, Group Role, Transaction Role, Last Updated, dan Modified By Gita Permata berubah; entri log permanen `Edit Home Group` bertambah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1125: Butir a dan b

1. Ketik Search `Gita Permata`, tekan Enter
2. Klik ⋯ pada baris Gita Permata lalu klik `Edit Home Group`
3. Klik node IT Infrastructure lalu klik `[Select]`
4. Klik `[Revoke]` pada dialog `Role Outside Constraint Will Be Revoked`
5. Verifikasi toast "Success, home group has been updated." tampil
6. Verifikasi Home Group Gita Permata menjadi IT Infrastructure
7. Klik Name `Gita Permata`, klik Tab Role lalu Sub-tab Group Role
8. Verifikasi Sub-tab Group Role tidak memuat grup Finance & Accounting pada baris Manage group
9. Klik Sub-tab Transaction Role
10. Verifikasi baris Damaged × Staff (IT Infrastructure) tetap ada pada Sub-tab Transaction Role
11. Verifikasi Sub-tab Transaction Role tidak memuat baris Disposal × Asset Admin dan Disposal × Approver
12. Pulihkan Home Group dan seluruh penugasan Gita Permata ke Pre-setup #51 lewat seed API

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pembagian TC lintas spec (S-05): TC-FA-SU-1125 butir a dan b diasersi di spec ini; butir c (satu entri `Edit Home Group` per surface log, tanpa entri `Remove`), d (modal Changelog User > Group Role dan > Transaction Role), dan e (tanpa notifikasi in-app untuk Gita Permata) diasersi di spec E2E-432. Spec ini tidak membaca log maupun notifikasi.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (Search untuk menemukan baris target, R-16 dan R-23; kotak Search masih berisi nilainya sehingga Klik Name pada langkah 7 tidak diawali Search ulang), langkah 7 (buka Detail, Tab Role, dan Sub-tab), langkah 9, dan langkah 12 (pemulihan).
- Langkah 4 mengklik `[Revoke]` tanpa `Verifikasi` dialog karena Expected TC-FA-SU-1125 tidak memuat dialog; isi dialog `Role Outside Constraint Will Be Revoked` diasersi di TC-FA-SU-290.
- Anchor asersi absence (bagian 8b butir 2): toast hasil server pada langkah 5 menjadi anchor bahwa Edit selesai dan daftar sudah diperbarui untuk langkah 8 dan 11; baris Damaged × Staff pada langkah 10 menjadi anchor surface Sub-tab Transaction Role untuk langkah 11.
- Temuan untuk QA (S-15):
  - Post Condition a TC-FA-SU-1125 berisi hal yang sama dengan Expected b sehingga tidak diasersi terpisah.
  - Sub-tab Group Role Gita Permata tidak punya Group Role lain di Pre-setup #51, sehingga sub-tab dapat kosong setelah pencabutan; tabel kosong tidak punya baris pembanding sebagai anchor selain toast langkah 5.
  - Seed `FaUserHGT` (#51) belum ada sebagai fixture; disediakan tim FE/BE sebelum eksekusi.
