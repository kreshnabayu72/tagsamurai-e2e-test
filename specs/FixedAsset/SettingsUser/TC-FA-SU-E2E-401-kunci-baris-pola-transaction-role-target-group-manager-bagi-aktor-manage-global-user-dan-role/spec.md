---
id: TC-FA-SU-E2E-401-kunci-baris-pola-transaction-role-target-group-manager-bagi-aktor-manage-global-user-dan-role
title: "Kunci Baris Pola Transaction Role Target Group Manager bagi Aktor Manage Global User & Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1089
coverage:
  web: automated
---

# Kunci Baris Pola Transaction Role Target Group Manager bagi Aktor Manage Global User & Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Manage global user & role (Update) Qori Akbar (Pre-setup #4, entity-wide; Global Role Manage global user & role ON, Read dan Update); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA), disediakan tim FE; kredensial `Spectra.env.FA_MURG_UPD_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21), penugasan (Pre-setup #23), dan varian Group Manager `FaUserGM` (Pre-setup #48). Hook `before` memastikan fixture Pre-setup #48 sesuai kondisi awal lewat seed API (kemampuan disediakan tim BE/FE).
- Pengguna target: Putri Anggraeni (Pre-setup #48): Group Manager Finance & Accounting (turunan: Accounts Payable) dengan baris pola Group Manager, ditambah baris non-pola Disposal × Staff (IT Infrastructure) dan Damaged × Monitoring & Report (Branch Surabaya) yang berada di luar subtree penugasan Group Manager.
- Data uji: tanpa data yang dibuat atau diubah; spec hanya membaca dan tidak menekan `[Bulk Remove]`.
- Kemampuan teknis: tidak ada tambahan.
- State global yang diubah: tidak ada; tidak butuh pemulihan.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1089 (aktor Qori Akbar, butir a dan c): Target Group Manager bagi aktor selain Default User dan Total Control: Remove dan checkbox baris pola Disabled (S-16), baris di luar subtree tidak terkunci

1. Ketik Search `Putri Anggraeni`, tekan Enter, lalu klik Name `Putri Anggraeni`
2. Klik Tab Role lalu Sub-tab Transaction Role
3. Ketik Search `Transfer`, tekan Enter
4. Verifikasi tabel menampilkan baris Transfer × Approver
5. Klik `⋯` pada baris Transfer × Approver lalu arahkan kursor ke row action `Remove`
6. Verifikasi row action `Remove` baris Transfer × Approver Disabled dengan tooltip "You don't have permission to edit."
7. Arahkan kursor ke checkbox pada baris Transfer × Approver
8. Verifikasi checkbox baris Transfer × Approver Disabled dengan tooltip "You don't have permission to edit."
9. Klik checkbox header (Select All)
10. Verifikasi Select All tidak memilih baris pola yang terkunci
11. Verifikasi `[Bulk Remove]` tidak dapat dipicu dari baris tersebut
12. Ganti isi kotak search dengan `Disposal`, tekan Enter
13. Verifikasi tabel menampilkan baris Disposal × Staff (IT Infrastructure)
14. Klik `⋯` pada baris Disposal × Staff (IT Infrastructure) lalu arahkan kursor ke row action `Remove`
15. Verifikasi row action `Remove` baris Disposal × Staff (IT Infrastructure) Enabled
16. Verifikasi checkbox baris Disposal × Staff (IT Infrastructure) Enabled
17. Tekan `Esc` untuk menutup menu `⋯`
18. Ganti isi kotak search dengan `Damaged`, tekan Enter
19. Verifikasi tabel menampilkan baris Damaged × Monitoring & Report (Branch Surabaya)
20. Klik `⋯` pada baris Damaged × Monitoring & Report (Branch Surabaya) lalu arahkan kursor ke row action `Remove`
21. Verifikasi row action `Remove` baris Damaged × Monitoring & Report (Branch Surabaya) Enabled
22. Verifikasi checkbox baris Damaged × Monitoring & Report (Branch Surabaya) Enabled
23. Tekan `Esc` untuk menutup menu `⋯`
24. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Pembagian TC lintas spec (S-05, bagian 8): TC-FA-SU-1089 dibagi per aktor; butir a dan c (Qori Akbar) di spec ini, butir a, b, dan d (Sinta Dewi) di spec 389. Kedua spec memakai aktor berbeda dan tidak saling bergantung. Butir e dirujuk TC ke TC-FA-SU-1090 dan tidak punya langkah pada kedua spec.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 3, 12, 17, 18, 23 dan 24. Search pada langkah 1 dan 3 adalah langkah penghubung untuk menemukan baris target (R-16, R-23); Search `Transfer`, `Disposal`, dan `Damaged` mempersempit tabel agar baris yang diuji teramati tanpa menelusuri halaman, sehingga Select All (langkah 9) berlaku atas hasil Search. Langkah 17 dan 23 menutup menu `⋯` tanpa memilih aksi. Langkah 24 membersihkan Search (S-09).
- Langkah 4 adalah `Verifikasi` anchor positif (baris target tampil) sebelum asersi Select All (langkah 10, 11); Select All tidak mengubah state data.
- Spec membaca saja; seleksi baris tidak terbentuk karena baris pola terkunci (S-09).
- Temuan untuk QA:
  - TC-FA-SU-1089 langkah 5 ("ulangi langkah 2 sampai 3 pada baris pola dan pada baris Disposal × Staff dan Damaged × Monitoring & Report") tidak menyebut apakah Select All diulang pada baris non-pola; spec mengasersi Select All hanya pada baris pola (langkah 9 sampai 11) dan hanya `Remove` dan checkbox pada baris non-pola (Expected butir c).
  - TC-FA-SU-1089 Expected butir b (`[Assign Group]` pada baris pola dan node popup) tidak menyebut aktor; TC hanya mengulang langkah 2 sampai 3 untuk Qori Akbar sehingga butir b diasersi pada Sinta Dewi (spec 389).
  - TC-FA-SU-1089 menyebut row action `Remove`, sedangkan PRD D-10 dan D-05c memakai istilah `Revoke` untuk pencabutan penugasan pada dialog Auto-Revert; spec memakai `Remove` sesuai TC. Mohon dikonfirmasi label row action yang dimaksud (`[Remove]` atau `[Revoke]`).
  - TC-FA-SU-1089 langkah 5 menyebut Qori Akbar (Manage global user & role, Update) tetapi suite.md dan Pre-setup TC tidak memuat email akunnya; spec menandainya "disediakan tim FE".
  - TC-FA-SU-1089 Expected butir c mengasersi checkbox Enabled pada baris non-pola tetapi tidak menyebut cara membaca state checkbox tanpa mengklik; spec mengasersi state Enabled tanpa mengubah seleksi.
