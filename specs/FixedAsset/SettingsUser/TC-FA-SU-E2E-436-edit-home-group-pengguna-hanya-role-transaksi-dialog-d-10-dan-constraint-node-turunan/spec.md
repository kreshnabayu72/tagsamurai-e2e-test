---
id: TC-FA-SU-E2E-436-edit-home-group-pengguna-hanya-role-transaksi-dialog-d-10-dan-constraint-node-turunan
title: "Edit Home Group Pengguna dengan Hanya Role Transaksi: Dialog D-10, Pencabutan Approver, dan Constraint ke Node Turunan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1126
  - TC-FA-SU-1127
coverage:
  web: automated
---

# Edit Home Group Pengguna dengan Hanya Role Transaksi: Dialog D-10, Pencabutan Approver, dan Constraint ke Node Turunan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23), Transaction Role (#39), dan varian `FaUserHGT` (#51; kebutuhan tim FE, seed disediakan tim FE/BE sebelum eksekusi). Pengguna target: Mira Anggraini (Home Group Finance & Accounting): hanya Transaction Role Disposal × Staff dan Borrowing & Assignment × Approver pada Finance & Accounting, tanpa Group Role, ditambah Global Role Manage asset master data. Nama pengguna dan grup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan baca state BE (disediakan tim FE/BE, tanpa endpoint karangan; TC tidak memberi cara cek): jumlah entri `Edit Home Group` dan `Remove` pada Tab Changelog Mira Anggraini, modal Changelog User > Transaction Role, Tab System Log aktor, dan Activity Log, serta jumlah notifikasi in-app Mira Anggraini. Dibaca sebelum aksi (baseline, S-12) dan sesudah aksi; asersi hanya memakai selisih karena audit trail dan notifikasi bersifat permanen. Jendela absence notifikasi: "Tunggu 5 detik tanpa memuat ulang halaman" (pilihan spec, bukan nilai TC).
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan Role Transaksi Mira Anggraini ke Pre-setup #51. Seed dijalankan di hook `before`, sebagai langkah penghubung (langkah 16 dan 30), dan di hook `after` (cadangan). Efek pada Pre-setup: Home Group, Transaction Role, Last Updated, dan Modified By Mira Anggraini berubah; entri log permanen `Edit Home Group` bertambah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Catat daftar Global Role dan Transaction Role Mira Anggraini sebagai baseline

### TC-FA-SU-1126: Dialog D-10 dengan bullet Role Transaksi

2. Ketik Search `Mira Anggraini`, tekan Enter
3. Klik ⋯ pada baris Mira Anggraini lalu klik `Edit Home Group`
4. Klik node IT Infrastructure lalu klik `[Select]`
5. Verifikasi dialog Title `Role Outside Constraint Will Be Revoked` dengan dua bullet `• Staff — Disposal — Finance & Accounting` dan `• Approver — Borrowing & Assignment — Finance & Accounting`, kalimat `Setting the Home Group constraint to IT Infrastructure for Mira Anggraini will revoke these assignments outside this group.` dan `Are you sure you want to revoke them?`
6. Verifikasi tombol `[Cancel]` (Text, Contrast) dan `[Revoke]` (filled danger) tampil
7. Verifikasi dialog tidak memuat bullet Group Role maupun `Group Manager`
8. Klik `[Revoke]`
9. Verifikasi toast "Success, home group has been updated." tampil
10. Verifikasi tidak ada dialog Remove Last Approver (D-09)
11. Klik Name `Mira Anggraini`, klik Tab Role lalu Sub-tab Transaction Role
12. Verifikasi Sub-tab Transaction Role tidak lagi memuat baris Disposal × Staff dan Borrowing & Assignment × Approver
13. Klik Sub-tab Global Role
14. Verifikasi Global Role Mira Anggraini (Manage asset master data) tidak berubah dibanding baseline langkah 1
15. Kembali ke User List lewat Breadcrumb
16. Pulihkan Home Group dan Role Transaksi Mira Anggraini ke Pre-setup #51 lewat seed API

### TC-FA-SU-1127: Constraint ke node turunan

17. Catat jumlah entri `Edit Home Group` dan `Remove` pada Tab Changelog Mira Anggraini, modal Changelog User > Transaction Role, Tab System Log aktor, dan Activity Log, serta jumlah notifikasi in-app Mira Anggraini sebagai baseline
18. Klik ⋯ pada baris Mira Anggraini lalu klik `Edit Home Group`
19. Klik node Accounts Payable lalu klik `[Select]`
20. Verifikasi dialog `Role Outside Constraint Will Be Revoked` mendaftar `• Staff — Disposal — Finance & Accounting` dan `• Approver — Borrowing & Assignment — Finance & Accounting`
21. Klik `[Revoke]`
22. Verifikasi toast "Success, home group has been updated." tampil
23. Klik Name `Mira Anggraini`, klik Tab Role lalu Sub-tab Transaction Role
24. Verifikasi Sub-tab Transaction Role tidak lagi memuat baris Disposal × Staff dan Borrowing & Assignment × Approver
25. Baca jumlah entri `Edit Home Group` dan `Remove` pada Tab Changelog Mira Anggraini, modal Changelog User > Transaction Role, Tab System Log aktor, dan Activity Log
26. Verifikasi jumlah entri `Edit Home Group` bertambah 1 dibanding baseline langkah 17 pada Tab Changelog Mira Anggraini, Tab System Log aktor, dan Activity Log
27. Verifikasi jumlah entri `Remove` sama dengan baseline langkah 17 pada Tab Changelog Mira Anggraini, modal Changelog User > Transaction Role, Tab System Log aktor, dan Activity Log
28. Tunggu 5 detik tanpa memuat ulang halaman
29. Verifikasi jumlah notifikasi in-app Mira Anggraini sama dengan baseline langkah 17
30. Pulihkan Home Group dan Role Transaksi Mira Anggraini ke Pre-setup #51 lewat seed API

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 dan 17 (baseline), 2 (Search untuk menemukan baris target, R-16 dan R-23; kotak Search masih berisi nilainya sehingga Klik Name pada langkah 11 dan 23 tidak diawali Search ulang), 11, 13, 15, 23, 25, 28, serta 16 dan 30 (pemulihan). Sesudah kembali ke User List (langkah 15) kotak Search mempertahankan `Mira Anggraini` sehingga langkah 18 tidak mengetik Search ulang.
- Anchor asersi absence (bagian 8b butir 2): dialog pada langkah 5 untuk langkah 7; toast hasil server pada langkah 9 untuk langkah 10 dan 12; toast pada langkah 22 untuk langkah 24; `Verifikasi` selisih entri `Edit Home Group` pada langkah 26 untuk langkah 27. Langkah 26 tidak ada di Expected TC-FA-SU-1127 dan ditambahkan hanya sebagai anchor positif (S-03); jumlah notifikasi pada langkah 29 dibandingkan dengan baseline karena seed bersih tidak menggantikan baseline (bagian 8b butir 10).
- Asersi tidak adanya entri log dan notifikasi (TC-FA-SU-1127 butir c) memakai selisih jumlah terhadap baseline pada pemicu yang sama (bagian 8b butir 10 dan S-12), bukan asersi kelas g.
- Langkah 10: TC-FA-SU-1126 butir c menulis "tanpa dialog Remove Last Approver (D-09)"; spec mengasersi sesudah toast pada langkah 9.
- Temuan untuk QA (S-15):
  - Copy dialog `Role Outside Constraint Will Be Revoked` pada TC-FA-SU-1126 ditandai "copy usulan — perlu persetujuan PM"; asersi memakai literal TC dan perlu diubah bila PM mengganti copy.
  - Global Role Manage asset master data Mira Anggraini adalah asumsi TC (tidak ditetapkan PRD); langkah 14 hanya mengasersi "tidak berubah" terhadap baseline langkah 1, bukan nilai role tertentu.
  - Post Condition b TC-FA-SU-1126 (satu entri `Edit Home Group` pada Tab Changelog target, Tab System Log aktor, dan Activity Log; tanpa entri log atau notifikasi untuk pencabutan Role Transaksi) tidak punya Expected padanan atau langkah observasi di TC sehingga tidak diasersi pada TC itu (S-01); pembacaan log dan notifikasi dilakukan pada TC-FA-SU-1127 sesuai butir c.
  - TC-FA-SU-1127 butir c tidak menyebut surface log dan notifikasi; spec memakai Tab Changelog, modal Changelog User > Transaction Role, Tab System Log aktor, Activity Log, dan jumlah notifikasi Mira Anggraini (cara baca disediakan tim FE/BE).
  - Seed `FaUserHGT` (#51) belum ada sebagai fixture; disediakan tim FE/BE sebelum eksekusi.
