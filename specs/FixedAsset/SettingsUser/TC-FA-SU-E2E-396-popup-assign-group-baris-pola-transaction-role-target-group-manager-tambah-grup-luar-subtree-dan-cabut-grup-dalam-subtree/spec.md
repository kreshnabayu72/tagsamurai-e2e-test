---
id: TC-FA-SU-E2E-396-popup-assign-group-baris-pola-transaction-role-target-group-manager-tambah-grup-luar-subtree-dan-cabut-grup-dalam-subtree
title: "Popup Assign Group Baris Pola Transaction Role Target Group Manager: Tambah Grup di Luar Subtree dan Cabut Grup dalam Subtree"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-1094
coverage:
  web: automated
---

# Popup Assign Group Baris Pola Transaction Role Target Group Manager: Tambah Grup di Luar Subtree dan Cabut Grup dalam Subtree

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan penugasan (Pre-setup #23). Putri Anggraeni ber-Home Group Finance & Accounting (Pre-setup #43/#48), sehingga Branch Surabaya di luar constraint dan Disabled di pemilih Group (tooltip S-45); sesuai Catatan TC (Home Group constraint FI-32), target tanpa Home Group memakai seed `FaUserNoHG` (Pre-setup #50), diterapkan per target: hanya Home Group Putri Anggraeni yang dikosongkan lewat seed API di hook `before`; penugasan lain tidak berubah. Seed `FaUserNoHG` wajib disediakan tim FE/BE sebelum eksekusi.
- Pengguna target: Putri Anggraeni (Pre-setup #48 `FaUserGM`): Group Manager Finance & Accounting (turunan Accounts Payable) dengan baris pola Group Manager pada kedua node, ditambah penugasan non-pola Group Role Manage user & role pada Finance & Accounting (Read dan Update), Transaction Role Disposal x Staff pada IT Infrastructure, dan Damaged x Monitoring & Report pada Branch Surabaya. Email akun ini tidak tertulis di Pre-setup TC; target hanya dibuka lewat Search nama.
- Data uji: baris Transfer x Approver; Branch Surabaya (di luar subtree) ditambah, Accounts Payable (dalam subtree) dicabut.
- Kemampuan teknis (disediakan tim FE/BE): seed API untuk memulihkan Putri Anggraeni ke Pre-setup #48 (pada langkah penghubung akhir dan di hook `after`) dan, di hook `before`, mengosongkan Home Group Putri Anggraeni (Pre-setup #50 per target).
- State global yang diubah: status Group Manager, seluruh baris pola, penugasan, dan Home Group (dikosongkan di hook `before`) Putri Anggraeni; dipulihkan ke Pre-setup #48 (termasuk Home Group Finance & Accounting) lewat seed API pada langkah 32 dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1094: Assign Group pada baris pola Transaction Role target Group Manager: tambah grup di luar subtree tanpa dialog, cabut grup dalam subtree memicu D-05c

1. Ketik Search `Putri Anggraeni`, tekan Enter, lalu klik Name `Putri Anggraeni`
2. Klik Tab Role lalu Sub-tab Transaction Role
3. Verifikasi banner Group Manager tampil di Sub-tab Transaction Role
4. Klik `[Assign Group]` pada baris Transfer x Approver
5. Centang Branch Surabaya
6. Klik `[Save]`
7. Verifikasi toast assigned tampil
8. Verifikasi dialog Auto-Revert tidak tampil
9. Verifikasi kolom Group baris Transfer x Approver menjadi `Accounts Payable, Branch Surabaya +1 more`
10. Verifikasi banner Group Manager tetap tampil di Sub-tab Transaction Role
11. Verifikasi baris pola Transfer x Approver dan Disposal x Asset Admin tetap ada
12. Klik `[Assign Group]` pada baris Transfer x Approver
13. Hapus centang Accounts Payable
14. Klik `[Save]`
15. Verifikasi dialog D-05c varian Role Transaksi dengan Title `Remove Group Manager` tampil
16. Verifikasi dialog `Remove Transaction Role` (D-07) tidak tampil
17. Klik `[Cancel]`
18. Verifikasi popup Assign Group tampil kembali dengan isi tidak berubah
19. Tunggu toast lama hilang otomatis (toast assigned langkah 7)
20. Klik `[Save]`
21. Verifikasi dialog dengan Title `Remove Group Manager` tampil
22. Klik `[Remove]`
23. Verifikasi toast gabungan sukses Remove Transaction Role disertai klausa auto-revert Group Manager tampil
24. Verifikasi hanya satu toast yang tampil, bukan toast terpisah
25. Verifikasi banner Group Manager hilang di Sub-tab Transaction Role
26. Verifikasi penugasan Transfer x Approver pada Branch Surabaya (langkah 5) tetap ada
27. Verifikasi seluruh baris pola Group Manager Transaction Role lain (Asset Admin dan Approver pada Accounts Payable dan Finance & Accounting) tetap tersimpan sebagai baris biasa; pencabutan Accounts Payable pada Transfer x Approver berasal dari aksi aktor sendiri
28. Klik Sub-tab Group Role
29. Verifikasi baris non-pola Manage user & role pada Finance & Accounting tetap ada
30. Verifikasi seluruh baris pola Group Manager Group Role (Group Role katalog selain Manage user & role pada Finance & Accounting dan Accounts Payable) tetap tersimpan sebagai baris biasa
31. Verifikasi banner Group Manager hilang di Sub-tab Group Role
32. Pulihkan Putri Anggraeni ke Pre-setup #48 lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan: tambah grup di luar subtree tanpa dialog (langkah 4 sampai 11), `[Cancel]` pada dialog (langkah 12 sampai 18), lalu konfirmasi `[Remove]` yang mengubah state (S-09, S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 19, 28 dan 32. Search `Putri Anggraeni` pada langkah 1 adalah langkah penghubung untuk menemukan baris target (R-16, R-23). Langkah 19 menunggu toast lama hilang sebelum hitungan toast pada langkah 24 (R-12). Pemulihan lewat seed API memulihkan Pre-setup #48 (S-06, S-09).
- Anchor 8b butir 2: banner Group Manager tampil (langkah 3, tidak tertulis di Expected TC) menjadi anchor bagi banner hilang (langkah 25, 31); toast assigned (langkah 7) menjadi anchor bagi dialog Auto-Revert tidak tampil (langkah 8); dialog D-05c tampil (langkah 15) menjadi anchor bagi dialog D-07 tidak tampil (langkah 16); baris non-pola dan penugasan Branch Surabaya tetap ada (langkah 26, 29) berdampingan dengan baris pola yang tetap tersimpan (langkah 27, 30), tidak lagi diasersi sebagai absence.
- Klausa "dalam transaksi atomik yang sama" tidak teramati terpisah lewat UI; keadaan akhir lengkap diasersi pada langkah 25 sampai 31.
- Post Condition b TC-FA-SU-1094 (entri `Assign` Branch Surabaya dan entri `Auto-Revert` di tiga surface log) tidak punya langkah observasi di TC dan tidak diasersi di spec ini; entri `Auto-Revert` diasersi pada spec 394 (TC-FA-SU-1090).
- Temuan untuk QA:
  - TC-FA-SU-1094 Precondition tidak menyebut Pre-setup #50 sedangkan Putri Anggraeni ber-Home Group, sehingga Branch Surabaya akan Disabled (S-45) dan penugasan ditolak 422 V-09; spec mengikuti Catatan TC (Home Group constraint FI-32) dan memakai seed `FaUserNoHG` (Pre-setup #50) per target, bukan seluruh 25 pengguna. Mohon dikonfirmasi bila #50 harus diterapkan penuh atau Precondition TC diperbarui.
  - Copy dialog D-05c varian Role Transaksi dan tombol `[Remove]` bertanda "copy usulan, perlu persetujuan PM" (`D-05` `settings-role-permission` Open Item #7d); TC-FA-SU-1094 tidak menulis teks dialog, sehingga spec hanya mengasersi Title `Remove Group Manager` dan varian Role Transaksi. PRD DO-12 menyebut tombol `[Revoke]` pada dialog D-10 (jalur Edit Home Group) sedangkan DO-02 memakai `[Remove]` untuk D-05; mohon dikonfirmasi label D-05c.
  - Teks toast assigned (butir a) dan toast gabungan (butir c, klausa auto-revert Group Manager, copy usulan) tidak ditulis literal di TC maupun PRD; spec mengasersi keduanya secara longgar tanpa teks persis.
  - Teks banner Group Manager untuk Putri Anggraeni tidak tertulis di TC; spec hanya mengasersi banner tampil atau hilang. Spec 386 (TC-FA-SU-1074) masih menyatakan banner Group Manager tidak tampil di Sub-tab Transaction Role.
  - TC-FA-SU-1094 ACC menyebut `#20` (id Client `FaUserMain`, bukan nomor akun); aktor diambil dari langkah "Login sebagai Ahmad Dahlan (Default User)". Mohon dikonfirmasi.
  - Expected b "`[Cancel]` mengembalikan popup dengan isi utuh tanpa menyimpan" tidak menjelaskan keadaan centang di popup (centang Accounts Payable tetap terhapus atau kembali); spec hanya mengasersi popup tampil kembali dengan isi tidak berubah (langkah 18).
  - Expected c menyebut "seluruh baris pola GM lain tetap tersimpan" yang mencakup Group Role; spec membaca Sub-tab Group Role (langkah 28 sampai 31) dengan banner Group Manager di sub-tab itu sebagai pembanding.
