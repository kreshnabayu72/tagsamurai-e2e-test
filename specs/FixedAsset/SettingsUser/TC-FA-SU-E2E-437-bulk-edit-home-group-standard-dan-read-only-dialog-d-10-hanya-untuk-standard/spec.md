---
id: TC-FA-SU-E2E-437-bulk-edit-home-group-standard-dan-read-only-dialog-d-10-hanya-untuk-standard
title: "Bulk Edit Home Group Pengguna Standard dan Read Only: Dialog D-10 Hanya untuk Standard dan Baris Pola Read Only Tetap"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-1128
coverage:
  web: automated
---

# Bulk Edit Home Group Pengguna Standard dan Read Only: Dialog D-10 Hanya untuk Standard dan Baris Pola Read Only Tetap

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23), dan varian `FaUserHGT` (#51; kebutuhan tim FE, seed disediakan tim FE/BE sebelum eksekusi). Pengguna target: Gita Permata (Standard, Home Group Finance & Accounting): Group Role Manage group pada Finance & Accounting; Transaction Role Disposal × Asset Admin (Finance & Accounting), Disposal × Approver (Accounts Payable), dan Damaged × Staff (IT Infrastructure); Citra Lestari (Read Only, Home Group General Affairs): baris pola Group Role (Read di semua group) dan baris pola Transaction Role Monitoring & Report di semua group. Kedua baris diasumsikan berada pada halaman User List yang sama (dicentang tanpa Search). Nama pengguna, grup, dan baris penugasan dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan baca state BE (disediakan tim FE/BE, tanpa endpoint karangan; TC tidak memberi cara cek): jumlah entri `Edit Home Group` dan `Remove` pada Tab Changelog Gita Permata, Tab Changelog Citra Lestari, Tab System Log aktor, dan Activity Log, serta jumlah notifikasi in-app Gita Permata dan Citra Lestari. Dibaca sebelum aksi (baseline, S-12) dan sesudah aksi; asersi hanya memakai selisih karena audit trail dan notifikasi bersifat permanen. Jendela absence notifikasi: "Tunggu 5 detik tanpa memuat ulang halaman" (pilihan spec, bukan nilai TC).
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan seluruh penugasan Gita Permata dan Citra Lestari ke Pre-setup #51. Seed dijalankan di hook `before`, sebagai langkah penghubung terakhir (langkah 28), dan di hook `after` (cadangan). Efek pada Pre-setup: Home Group, Group Role, Transaction Role, Last Updated, dan Modified By Gita Permata serta Home Group Citra Lestari berubah; entri log permanen `Edit Home Group` bertambah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Catat jumlah entri `Edit Home Group` dan `Remove` pada Tab Changelog Gita Permata, Tab Changelog Citra Lestari, Tab System Log aktor, dan Activity Log, jumlah notifikasi in-app Gita Permata dan Citra Lestari, serta daftar baris pola Group Role dan Transaction Role Citra Lestari sebagai baseline
2. Centang Gita Permata dan Citra Lestari
3. Klik Bulk Action > `Edit Home Group`, klik node IT Infrastructure, lalu klik `[Select]`
4. Verifikasi dialog `Role Outside Constraint Will Be Revoked` tampil untuk Gita Permata
5. Verifikasi dialog memuat tiga bullet `• Manage group — Finance & Accounting`, `• Asset Admin — Disposal — Finance & Accounting`, dan `• Approver — Disposal — Accounts Payable`
6. Klik `[Revoke]`
7. Verifikasi tidak ada dialog untuk Citra Lestari
8. Verifikasi toast "Success, home group has been updated." tampil tanpa varian "Some items were skipped."
9. Verifikasi Home Group Gita Permata dan Citra Lestari menjadi IT Infrastructure
10. Ketik Search `Citra Lestari`, tekan Enter
11. Klik Name `Citra Lestari`, klik Tab Role lalu Sub-tab Group Role
12. Verifikasi baris pola Group Role (Read di semua group) Citra Lestari tetap utuh sama dengan baseline langkah 1
13. Verifikasi banner Read Only tetap tampil
14. Klik Sub-tab Transaction Role
15. Verifikasi baris pola Transaction Role Monitoring & Report di semua group Citra Lestari tetap utuh sama dengan baseline langkah 1
16. Kembali ke User List lewat Breadcrumb, lalu ganti isi kotak search dengan `Gita Permata`, tekan Enter
17. Klik Name `Gita Permata`, klik Tab Role lalu Sub-tab Group Role
18. Verifikasi Sub-tab Group Role tidak memuat grup Finance & Accounting pada baris Manage group
19. Klik Sub-tab Transaction Role
20. Verifikasi baris Damaged × Staff (IT Infrastructure) tetap ada pada Sub-tab Transaction Role
21. Verifikasi Sub-tab Transaction Role tidak memuat baris Disposal × Asset Admin dan Disposal × Approver
22. Baca jumlah entri `Edit Home Group` dan `Remove` pada Tab Changelog Gita Permata, Tab Changelog Citra Lestari, Tab System Log aktor, dan Activity Log
23. Verifikasi jumlah entri `Edit Home Group` bertambah 1 per pengguna dibanding baseline langkah 1 pada Tab Changelog Gita Permata dan Tab Changelog Citra Lestari, dan bertambah 2 pada Tab System Log aktor dan Activity Log
24. Verifikasi jumlah entri `Remove` sama dengan baseline langkah 1 pada Tab Changelog Gita Permata, Tab Changelog Citra Lestari, Tab System Log aktor, dan Activity Log
25. Tunggu 5 detik tanpa memuat ulang halaman
26. Verifikasi jumlah notifikasi in-app Gita Permata dan Citra Lestari sama dengan baseline langkah 1
27. Kembali ke User List lewat Breadcrumb
28. Pulihkan Home Group dan seluruh penugasan Gita Permata dan Citra Lestari ke Pre-setup #51 lewat seed API

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (baseline), 10 (Search untuk menemukan baris target, R-16 dan R-23; kotak Search masih berisi nilainya sehingga Klik Name pada langkah 11 tidak diawali Search ulang), 11, 14, 16 (kembali ke User List dan ganti isi kotak search, butir 9), 17, 19, 22, 25, 27, dan 28 (pemulihan). Langkah 2 mencentang tanpa Search mengikuti spec Bulk Edit Home Group lain di suite.
- Anchor asersi absence (bagian 8b butir 2): dialog Gita Permata pada langkah 4 untuk langkah 7; toast hasil server pada langkah 8 untuk langkah 18 dan 21; baris Damaged × Staff pada langkah 20 untuk langkah 21; `Verifikasi` selisih entri `Edit Home Group` pada langkah 23 untuk langkah 24.
- Asersi tidak adanya entri `Remove` dan notifikasi (Expected e) memakai selisih jumlah terhadap baseline pada pemicu yang sama (bagian 8b butir 10 dan S-12), bukan asersi kelas g. Modal Changelog User per sub-tab tidak dibaca di spec ini (pembacaannya ada di spec E2E-432 untuk TC-FA-SU-1125 butir d).
- Langkah 8: Expected b menulis "tanpa varian skipped"; spec mengasersi teks toast persis tanpa kalimat "Some items were skipped." dalam satu `Verifikasi` (satu elemen toast).
- Urutan TC: TC-FA-SU-1128 langkah 4 (Detail Citra Lestari lebih dulu) dan langkah 5 (Detail Gita Permata) diikuti; baca log (Expected e) ditempatkan setelah seluruh Detail dibuka.
- Temuan untuk QA (S-15):
  - Letak banner Read Only tidak disebut TC; spec mengasersinya setelah Sub-tab Group Role Citra Lestari dibuka.
  - Expected e menyebut surface log secara umum; spec memakai Tab Changelog target (Gita Permata dan Citra Lestari), Tab System Log aktor, dan Activity Log (dua entri `Edit Home Group`, satu per pengguna). Notifikasi dibaca lewat kemampuan baca BE yang disediakan tim FE/BE.
  - Kedua pengguna dicentang tanpa Search dan diasumsikan berada pada halaman yang sama.
  - Seed `FaUserHGT` (#51) belum ada sebagai fixture; disediakan tim FE/BE sebelum eksekusi.
