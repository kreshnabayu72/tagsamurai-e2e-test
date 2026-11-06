---
id: TC-FA-SU-E2E-389-kunci-baris-pola-transaction-role-target-group-manager-bagi-aktor-manage-user-dan-role-group
title: "Kunci Baris Pola Transaction Role Target Group Manager bagi Aktor Manage User & Role Group"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1089
coverage:
  web: automated
---

# Kunci Baris Pola Transaction Role Target Group Manager bagi Aktor Manage User & Role Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Manage user & role Group (Update) Sinta Dewi (Pre-setup #6, scope Finance & Accounting); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA), disediakan tim FE; kredensial `Spectra.env.FA_MURGR_UPD_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21), penugasan (Pre-setup #23), dan varian Group Manager `FaUserGM` (Pre-setup #48). Hook `before` memastikan fixture Pre-setup #48 sesuai kondisi awal lewat seed API (kemampuan disediakan tim BE/FE).
- Pengguna target: Putri Anggraeni (Pre-setup #48): Group Manager Finance & Accounting (turunan: Accounts Payable) dengan baris pola Group Manager (Transaction Role Asset Admin dan Approver pada sembilan Jenis Transaksi), ditambah baris non-pola Disposal × Staff (IT Infrastructure) dan Damaged × Monitoring & Report (Branch Surabaya) yang berada di luar scope Sinta Dewi.
- Data uji: tanpa data yang dibuat atau diubah; spec hanya membaca dan tidak menekan `[Bulk Remove]`.
- Kemampuan teknis: tidak ada tambahan.
- State global yang diubah: tidak ada; tidak butuh pemulihan.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1089 (aktor Sinta Dewi, butir a, b, d): Target Group Manager bagi aktor selain Default User dan Total Control: Remove dan checkbox baris pola Disabled (S-16), popup Assign Group menonaktifkan node subtree, baris di luar subtree tidak terkunci

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
12. Verifikasi `[Assign Group]` pada baris Transfer × Approver Enabled
13. Klik `[Assign Group]` pada baris Transfer × Approver
14. Arahkan kursor ke node Finance & Accounting
15. Verifikasi node Finance & Accounting di popup Assign Group Transaction Role Disabled dengan tooltip "You don't have permission to edit."
16. Arahkan kursor ke node Accounts Payable
17. Verifikasi node Accounts Payable di popup Assign Group Transaction Role Disabled dengan tooltip "You don't have permission to edit."
18. Klik `[✕]` untuk menutup popup Assign Group Transaction Role
19. Ganti isi kotak search dengan `Disposal`, tekan Enter
20. Verifikasi tabel menampilkan baris Disposal × Staff (IT Infrastructure)
21. Verifikasi row action `Remove` baris Disposal × Staff (IT Infrastructure) Disabled
22. Verifikasi checkbox baris Disposal × Staff (IT Infrastructure) Disabled
23. Ganti isi kotak search dengan `Damaged`, tekan Enter
24. Verifikasi tabel menampilkan baris Damaged × Monitoring & Report (Branch Surabaya)
25. Verifikasi row action `Remove` baris Damaged × Monitoring & Report (Branch Surabaya) Disabled
26. Verifikasi checkbox baris Damaged × Monitoring & Report (Branch Surabaya) Disabled
27. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. TC-FA-SU-1089 dibagi per aktor: butir a, b, dan d (Sinta Dewi) di spec ini; butir a dan c (Qori Akbar) di spec 401. Pembagian TC lintas spec (S-05, bagian 8): kedua spec memuat `sourceTc` TC-FA-SU-1089, memakai aktor berbeda, dan tidak saling bergantung. Butir e (Default User dan Total Control tidak terkunci pada baris pola) dirujuk TC ke TC-FA-SU-1090 dan tidak punya langkah pada kedua spec (lihat Temuan untuk QA).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 3, 18, 19, 23 dan 27. Search pada langkah 1 dan 3 adalah langkah penghubung untuk menemukan baris target (R-16, R-23); Search `Transfer`, `Disposal`, dan `Damaged` mempersempit tabel agar baris yang diuji teramati tanpa menelusuri halaman, sehingga Select All (langkah 9) berlaku atas hasil Search. Langkah 18 menutup popup tanpa perubahan. Langkah 27 membersihkan Search (S-09).
- Langkah 4, 20, dan 24 adalah `Verifikasi` anchor positif (baris target tampil) sebelum asersi Select All (langkah 10, 11) dan sebelum asersi baris di luar scope; Select All tidak mengubah state data.
- Spec membaca saja; seleksi baris tidak terbentuk karena baris terkunci, sehingga tidak ada seleksi yang perlu dibersihkan (S-09).
- Temuan untuk QA:
  - TC-FA-SU-1089 Expected butir e ("Default User dan Total Control tidak terkunci pada baris pola") tidak punya langkah di TC ini (dirujuk ke TC-FA-SU-1090); spec tidak mengasersinya.
  - TC-FA-SU-1089 Expected butir d ("Disabled karena scope aktor (S-38), bukan karena kunci Group Manager") tidak menyebut tooltip atau cara membedakan penyebabnya; spec hanya mengasersi Disabled pada baris di luar scope (langkah 21, 22, 25, 26) tanpa membedakan penyebab.
  - TC-FA-SU-1089 Expected butir a ("`[Bulk Remove]` tidak dapat dipicu dari baris tersebut") tidak menyebut apakah tombol tidak tampil atau Disabled; spec mengasersi tidak dapat dipicu tanpa menyebut bentuknya.
  - TC-FA-SU-1089 menyebut row action `Remove`, sedangkan PRD D-10 dan D-05c memakai istilah `Revoke` untuk pencabutan penugasan pada dialog Auto-Revert; spec memakai `Remove` sesuai TC. Mohon dikonfirmasi label row action yang dimaksud (`[Remove]` atau `[Revoke]`).
  - TC-FA-SU-1089 langkah 1 menyebut Sinta Dewi tetapi suite.md dan Pre-setup TC tidak memuat email akunnya; spec menandainya "disediakan tim FE".
  - TC-FA-SU-1089 tidak menyebut Search untuk menemukan baris pola atau halaman Pagination; tabel dapat memuat lebih dari satu halaman sehingga spec menambahkan Search sebagai langkah penghubung (langkah 3, 19, 23).
