---
id: TC-FA-SU-E2E-406-save-campuran-modal-assign-transaction-role-target-group-manager-dialog-turun-tangga-lalu-auto-revert
title: "Save Campuran Modal Assign Transaction Role Target Group Manager: Dialog Turun Tangga lalu Auto-Revert"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-1093
coverage:
  web: automated
---

# Save Campuran Modal Assign Transaction Role Target Group Manager: Dialog Turun Tangga lalu Auto-Revert

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan penugasan (Pre-setup #23). Putri Anggraeni ber-Home Group Finance & Accounting (Pre-setup #43/#48), sehingga IT Infrastructure di luar constraint dan Disabled di pemilih Group (tooltip S-45); sesuai Catatan TC (Home Group constraint FI-32), target tanpa Home Group memakai seed `FaUserNoHG` (Pre-setup #50), diterapkan per target: hanya Home Group Putri Anggraeni yang dikosongkan lewat seed API di hook `before`; penugasan lain tidak berubah. Seed `FaUserNoHG` wajib disediakan tim FE/BE sebelum eksekusi.
- Pengguna target: Putri Anggraeni (Pre-setup #48 `FaUserGM`): Group Manager Finance & Accounting (turunan Accounts Payable) dengan baris pola Group Manager pada kedua node, ditambah penugasan non-pola Group Role Manage user & role pada Finance & Accounting (Read dan Update), Transaction Role Disposal x Staff pada IT Infrastructure, dan Damaged x Monitoring & Report pada Branch Surabaya. Email akun ini tidak tertulis di Pre-setup TC; target hanya dibuka lewat Search nama.
- Data uji: Disposal: Finance & Accounting (Asset Admin pola ke Monitoring & Report) dan IT Infrastructure (Staff non-pola ke Monitoring & Report). Langkah berulang 5 sampai 7, 15 sampai 17 dan 27 sampai 29 memakai parameter yang sama: Group Finance & Accounting dan IT Infrastructure, Transaction Disposal, Role Monitoring & Report.
- Kemampuan teknis (disediakan tim FE/BE): seed API untuk memulihkan Putri Anggraeni ke Pre-setup #48 (pada langkah penghubung akhir dan di hook `after`) dan, di hook `before`, mengosongkan Home Group Putri Anggraeni (Pre-setup #50 per target); pembacaan jumlah entri Tab Changelog target sebelum aksi sebagai baseline (bagian 8b butir 10).
- State global yang diubah: status Group Manager, seluruh baris pola, penugasan, dan Home Group (dikosongkan di hook `before`) Putri Anggraeni; dipulihkan ke Pre-setup #48 (termasuk Home Group Finance & Accounting) lewat seed API pada langkah 39 dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1093: Save campuran pada target Group Manager: dialog D-06 untuk grup di luar subtree lebih dulu, lalu D-05c untuk grup dalam subtree, dan Cancel di salah satunya membatalkan seluruh Save

1. Catat jumlah entri Tab Changelog Putri Anggraeni sebagai baseline
2. Ketik Search `Putri Anggraeni`, tekan Enter, lalu klik Name `Putri Anggraeni`
3. Klik Tab Role lalu Sub-tab Transaction Role
4. Verifikasi banner Group Manager tampil di Sub-tab Transaction Role
5. Klik `[+ Assign]`
6. Pilih Group Finance & Accounting dan IT Infrastructure, Transaction Disposal, Role Monitoring & Report
7. Klik `[Submit]`
8. Verifikasi dialog pertama D-06 dengan Title `Change Transaction Role` tampil mendaftar `• IT Infrastructure (currently Staff)`
9. Verifikasi dialog pertama tidak mendaftar Finance & Accounting
10. Verifikasi tombol `[Cancel]` dan `[Change]` tampil
11. Klik `[Cancel]` pada dialog pertama
12. Verifikasi dialog tertutup dan dialog kedua D-05c tidak tampil
13. Verifikasi kedua grup tidak berubah: Disposal x Asset Admin (Finance & Accounting) dan Disposal x Staff (IT Infrastructure) tetap ada, tanpa baris Disposal x Monitoring & Report
14. Verifikasi banner Group Manager tetap tampil di Sub-tab Transaction Role
15. Klik Tab Role lalu Sub-tab Transaction Role lalu klik `[+ Assign]`
16. Pilih Group Finance & Accounting dan IT Infrastructure, Transaction Disposal, Role Monitoring & Report
17. Klik `[Submit]`
18. Klik `[Change]` pada dialog pertama
19. Verifikasi dialog kedua D-05c varian Role Transaksi dengan Title `Remove Group Manager` tampil
20. Verifikasi dialog pertama D-06 sudah tertutup, sehingga kedua dialog tidak digabung
21. Klik `[Cancel]` pada dialog kedua
22. Verifikasi dialog tertutup
23. Verifikasi kedua grup tidak berubah: Disposal x Asset Admin (Finance & Accounting) dan Disposal x Staff (IT Infrastructure) tetap ada, tanpa baris Disposal x Monitoring & Report
24. Verifikasi banner Group Manager tetap tampil di Sub-tab Transaction Role
25. Klik Tab Changelog
26. Verifikasi jumlah entri Tab Changelog Putri Anggraeni sama dengan baseline
27. Klik Tab Role lalu Sub-tab Transaction Role lalu klik `[+ Assign]`
28. Pilih Group Finance & Accounting dan IT Infrastructure, Transaction Disposal, Role Monitoring & Report
29. Klik `[Submit]`
30. Klik `[Change]` pada dialog pertama
31. Verifikasi dialog kedua D-05c dengan Title `Remove Group Manager` tampil
32. Klik `[Remove]` pada dialog kedua
33. Verifikasi kedua penugasan Disposal x Monitoring & Report pada Finance & Accounting dan IT Infrastructure tersimpan dan tetap ada
34. Verifikasi banner Group Manager hilang di Sub-tab Transaction Role
35. Verifikasi seluruh baris pola Group Manager Transaction Role (Asset Admin dan Approver pada seluruh Jenis Transaksi untuk Accounts Payable dan Finance & Accounting, selain Disposal x Asset Admin pada Finance & Accounting yang digantikan penugasan Monitoring & Report) tetap tersimpan sebagai baris biasa
36. Klik Sub-tab Group Role
37. Verifikasi baris non-pola Manage user & role pada Finance & Accounting tetap ada
38. Verifikasi seluruh baris pola Group Manager Group Role (Group Role katalog selain Manage user & role pada Finance & Accounting dan Accounts Payable) tetap tersimpan sebagai baris biasa
39. Pulihkan Putri Anggraeni ke Pre-setup #48 lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan mengikuti TC: `[Cancel]` pada dialog pertama (langkah 5 sampai 14), `[Cancel]` pada dialog kedua (langkah 15 sampai 26), lalu konfirmasi kedua dialog yang mengubah state (S-09, S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 3, 15, 25, 27, 36 dan 39. Search `Putri Anggraeni` pada langkah 2 adalah langkah penghubung untuk menemukan baris target (R-16, R-23). Baseline log mengikuti S-12; pemulihan lewat seed API memulihkan Pre-setup #48 (S-06, S-09).
- Anchor 8b butir 2: banner Group Manager tampil (langkah 4, tidak tertulis di Expected TC) menjadi anchor bagi banner hilang (langkah 34); dialog pertama tampil (langkah 8) menjadi anchor bagi dialog kedua tidak tampil (langkah 12); baris Disposal x Asset Admin dan Disposal x Staff tetap ada (langkah 13, 23) menjadi anchor bagi tidak ada baris Disposal x Monitoring & Report; baris non-pola tetap ada (langkah 33, 37) berdampingan dengan baris pola yang tetap tersimpan (langkah 35, 38), tidak lagi diasersi sebagai absence.
- Alasan di atas sekitar 35 langkah (39): satu TC dengan tiga eksekusi `[Submit]` pada modal Assign yang sama sesuai langkah 5 dan 6 TC (Cancel pada dialog pertama, Cancel pada dialog kedua, konfirmasi keduanya), tanpa kelas harness; blok berulang ada pada langkah 5 sampai 7, 15 sampai 17 dan 27 sampai 29 dengan parameter di Prerequisites tanpa langkah bersyarat. Pemecahan menyisakan eksekusi yang tidak bermakna sendiri.
- Cancel pada dialog pertama (langkah 11) dan dialog kedua (langkah 21) dibaca terhadap satu baseline log (langkah 1); pembacaan Tab Changelog pada langkah 25 dan 26 mencakup kedua pembatalan.
- Klausa "dalam transaksi atomik yang sama" tidak teramati terpisah lewat UI; keadaan akhir lengkap diasersi pada langkah 33 sampai 38.
- Pembagian TC lintas spec: TC-FA-SU-1092 (turun tangga via modal Assign) ada di spec 395.
- Temuan untuk QA:
  - TC-FA-SU-1093 Precondition tidak menyebut Pre-setup #50 sedangkan Putri Anggraeni ber-Home Group, sehingga IT Infrastructure akan Disabled (S-45) dan penugasan ditolak 422 V-09; spec mengikuti Catatan TC (Home Group constraint FI-32) dan memakai seed `FaUserNoHG` (Pre-setup #50) per target, bukan seluruh 25 pengguna. Mohon dikonfirmasi bila #50 harus diterapkan penuh atau Precondition TC diperbarui.
  - Copy dialog D-05c varian Role Transaksi dan tombol `[Remove]` bertanda "copy usulan, perlu persetujuan PM" (`D-05` `settings-role-permission` Open Item #7d); TC-FA-SU-1093 butir b tidak menulis teks dialog kedua, sehingga spec hanya mengasersi Title `Remove Group Manager` dan varian Role Transaksi. PRD DO-12 menyebut tombol `[Revoke]` pada dialog D-10 (jalur Edit Home Group) sedangkan DO-02 memakai `[Remove]` untuk D-05; mohon dikonfirmasi label D-05c.
  - Teks banner Group Manager untuk Putri Anggraeni tidak tertulis di TC; spec hanya mengasersi banner tampil atau hilang. Spec 386 (TC-FA-SU-1074) masih menyatakan banner Group Manager tidak tampil di Sub-tab Transaction Role.
  - TC-FA-SU-1093 ACC menyebut `#20` (id Client `FaUserMain`, bukan nomor akun); aktor diambil dari langkah "Login sebagai Ahmad Dahlan (Default User)". Mohon dikonfirmasi.
  - TC-FA-SU-1093 tidak menyebut apakah modal Assign tetap terbuka setelah `[Cancel]` pada dialog; spec membuka modal lagi lewat `[+ Assign]` (langkah 15, 27) mengikuti "Ulangi langkah 2 sampai 3".
  - Expected c "tanpa entri log" tidak menyebut surface; spec membaca Tab Changelog target. Toast hasil konfirmasi tidak disebut di Expected d dan tidak diasersi. Post Condition (Putri tidak lagi Group Manager) diasersi lewat Expected d.
