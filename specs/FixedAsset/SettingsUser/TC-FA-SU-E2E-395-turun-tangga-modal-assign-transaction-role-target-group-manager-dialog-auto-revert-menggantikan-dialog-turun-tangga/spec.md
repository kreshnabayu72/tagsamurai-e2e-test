---
id: TC-FA-SU-E2E-395-turun-tangga-modal-assign-transaction-role-target-group-manager-dialog-auto-revert-menggantikan-dialog-turun-tangga
title: "Turun Tangga Modal Assign Transaction Role Target Group Manager: Dialog Auto-Revert Menggantikan Dialog Turun Tangga"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-1092
coverage:
  web: automated
---

# Turun Tangga Modal Assign Transaction Role Target Group Manager: Dialog Auto-Revert Menggantikan Dialog Turun Tangga

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan penugasan (Pre-setup #23).
- Pengguna target: Putri Anggraeni (Pre-setup #48 `FaUserGM`): Group Manager Finance & Accounting (turunan Accounts Payable) dengan baris pola Group Manager pada kedua node, ditambah penugasan non-pola Group Role Manage user & role pada Finance & Accounting (Read dan Update), Transaction Role Disposal x Staff pada IT Infrastructure, dan Damaged x Monitoring & Report pada Branch Surabaya. Email akun ini tidak tertulis di Pre-setup TC; target hanya dibuka lewat Search nama.
- Data uji: Disposal pada Finance & Accounting: Asset Admin (pola) ke Monitoring & Report. Langkah berulang 5 sampai 7 dan 16 sampai 18 memakai parameter yang sama: Group Finance & Accounting, Transaction Disposal, Role Monitoring & Report.
- Kemampuan teknis (disediakan tim FE/BE): seed API untuk memulihkan Putri Anggraeni ke Pre-setup #48 (di hook `before`, pada langkah penghubung akhir, dan di hook `after`); pembacaan jumlah entri Tab Changelog target sebelum aksi sebagai baseline (bagian 8b butir 10).
- State global yang diubah: status Group Manager dan seluruh baris pola serta penugasan Putri Anggraeni; dipulihkan ke Pre-setup #48 lewat seed API pada langkah 30 dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1092: Turun tangga pada grup dalam subtree penugasan GM dari modal Assign: dialog D-05c menggantikan dialog turun tangga D-06, Cancel membatalkan, dan baris yang baru ditugaskan tidak ikut dicabut

1. Catat jumlah entri Tab Changelog Putri Anggraeni sebagai baseline
2. Ketik Search `Putri Anggraeni`, tekan Enter, lalu klik Name `Putri Anggraeni`
3. Klik Tab Role lalu Sub-tab Transaction Role
4. Verifikasi banner Group Manager tampil di Sub-tab Transaction Role
5. Klik `[+ Assign]`
6. Pilih Group Finance & Accounting, Transaction Disposal, Role Monitoring & Report
7. Klik `[Submit]`
8. Verifikasi dialog tampil dengan Title `Remove Group Manager` (varian Role Transaksi), Body bullet `• Putri Anggraeni`, kalimat `This change will remove Group Manager status for this group.`, `Their other role assignments will remain as they are.` dan `Are you sure you want to remove it?`, serta tombol `[Cancel]` (Text, Contrast) dan `[Remove]`
9. Verifikasi dialog `Remove Transaction Role` (D-07) maupun `Change Transaction Role` (D-06) tidak tampil
10. Verifikasi tidak ada dialog kedua
11. Klik `[Cancel]`
12. Verifikasi banner Group Manager tetap tampil di Sub-tab Transaction Role
13. Verifikasi tidak ada penugasan tersimpan: baris Disposal x Monitoring & Report pada Finance & Accounting tidak ada
14. Klik Tab Changelog
15. Verifikasi jumlah entri Tab Changelog Putri Anggraeni sama dengan baseline
16. Klik Tab Role lalu Sub-tab Transaction Role lalu klik `[+ Assign]`
17. Pilih Group Finance & Accounting, Transaction Disposal, Role Monitoring & Report
18. Klik `[Submit]`
19. Verifikasi dialog dengan Title `Remove Group Manager` tampil
20. Klik `[Remove]` pada dialog
21. Verifikasi toast gabungan sukses Remove Transaction Role disertai klausa auto-revert Group Manager tampil
22. Verifikasi hanya satu toast yang tampil, bukan toast terpisah
23. Verifikasi penugasan Disposal x Monitoring & Report pada Finance & Accounting tersimpan sebagai baris non-pola dan tidak ikut dicabut
24. Verifikasi banner Group Manager hilang di Sub-tab Transaction Role
25. Verifikasi baris non-pola Disposal x Staff (IT Infrastructure) dan Damaged x Monitoring & Report (Branch Surabaya) tetap ada
26. Verifikasi baris pola Group Manager Transaction Role lain (Asset Admin dan Approver pada Accounts Payable dan Finance & Accounting, selain Disposal x Asset Admin pada Finance & Accounting yang digantikan penugasan Monitoring & Report) tetap tersimpan sebagai baris biasa
27. Klik Sub-tab Group Role
28. Verifikasi baris non-pola Manage user & role pada Finance & Accounting tetap ada
29. Verifikasi seluruh baris pola Group Manager Group Role (Group Role katalog selain Manage user & role pada Finance & Accounting dan Accounts Payable) tetap tersimpan sebagai baris biasa
30. Pulihkan Putri Anggraeni ke Pre-setup #48 lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan: `[Cancel]` (langkah 5 sampai 15) lebih dulu, lalu `[Remove]` yang mengubah state (S-09, S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 3, 14, 16, 27 dan 30. Search `Putri Anggraeni` pada langkah 2 adalah langkah penghubung untuk menemukan baris target (R-16, R-23). Baseline log mengikuti S-12; pemulihan lewat seed API memulihkan Pre-setup #48 (S-06, S-09).
- Anchor 8b butir 2: banner Group Manager tampil (langkah 4, tidak tertulis di Expected TC) menjadi anchor bagi banner hilang (langkah 24); dialog D-05c tampil (langkah 8) menjadi anchor bagi dialog D-07 atau D-06 tidak tampil dan tidak ada dialog kedua (langkah 9, 10); baris non-pola tetap ada (langkah 25, 28) berdampingan dengan baris pola yang tetap tersimpan (langkah 26, 29), tidak lagi diasersi sebagai absence; banner tampil (langkah 12) menjadi anchor bagi baris Disposal x Monitoring & Report tidak ada (langkah 13).
- Klausa "dalam transaksi atomik yang sama" tidak teramati terpisah lewat UI; keadaan akhir lengkap diasersi pada langkah 24 sampai 29.
- Pembagian TC lintas spec: TC-FA-SU-1093 (Save campuran target Group Manager) ada di spec 406. Post Condition b TC-FA-SU-1092 (pasangan entri penggantian tangga dan entri `Auto-Revert` di tiga surface log, notifikasi in-app) tidak punya langkah observasi di TC dan tidak diasersi; entri `Auto-Revert` diasersi pada spec 394 (TC-FA-SU-1090).
- Temuan untuk QA:
  - Copy dialog D-05c varian Role Transaksi dan tombol `[Remove]` bertanda "copy usulan, perlu persetujuan PM" (TC-FA-SU-1092 butir a; `D-05` `settings-role-permission` Open Item #7d). Spec memakai teks apa adanya; PRD DO-12 menyebut tombol `[Revoke]` pada dialog D-10 (jalur Edit Home Group) sedangkan DO-02 memakai `[Remove]` untuk D-05; mohon dikonfirmasi label D-05c.
  - Toast gabungan (butir c, klausa auto-revert Group Manager, copy usulan) tidak ditulis literal di TC maupun PRD; spec mengasersi toast gabungan secara longgar tanpa teks persis.
  - Teks banner Group Manager untuk Putri Anggraeni tidak tertulis di TC; spec hanya mengasersi banner tampil atau hilang. Spec 386 (TC-FA-SU-1074) masih menyatakan banner Group Manager tidak tampil di Sub-tab Transaction Role.
  - TC-FA-SU-1092 ACC menyebut `#20` (id Client `FaUserMain`, bukan nomor akun); aktor diambil dari langkah "Login sebagai Ahmad Dahlan (Default User)". Mohon dikonfirmasi.
  - TC-FA-SU-1092 Expected b "tanpa entri log" tidak menyebut surface; spec membaca Tab Changelog target (langkah 14 dan 15). Notifikasi in-app ke Putri Anggraeni (Post Condition b) tidak diasersi, dan Putri Anggraeni tidak punya nama env password di `suite.md`.
  - TC-FA-SU-1092 Expected c menyebut "baris pola GM lain tetap tersimpan" tanpa daftar baris; spec mengasersi himpunan baris pola Transaction Role dan Group Role menurut Pre-setup #48.
