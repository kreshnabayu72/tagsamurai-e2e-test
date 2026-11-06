---
id: TC-FA-SU-E2E-394-remove-baris-pola-transaction-role-target-group-manager-dialog-auto-revert-cancel-lalu-konfirmasi
title: "Remove Baris Pola Transaction Role Target Group Manager: Dialog Auto-Revert, Cancel lalu Konfirmasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1090
coverage:
  web: automated
---

# Remove Baris Pola Transaction Role Target Group Manager: Dialog Auto-Revert, Cancel lalu Konfirmasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan penugasan (Pre-setup #23).
- Pengguna target: Putri Anggraeni (Pre-setup #48 `FaUserGM`): Group Manager Finance & Accounting (turunan Accounts Payable) dengan baris pola Group Manager pada kedua node, ditambah penugasan non-pola Group Role Manage user & role pada Finance & Accounting (Read dan Update), Transaction Role Disposal x Staff pada IT Infrastructure, dan Damaged x Monitoring & Report pada Branch Surabaya. Email akun ini tidak tertulis di Pre-setup TC; target hanya dibuka lewat Search nama.
- Data uji: baris yang di-Remove: Transfer x Approver (Accounts Payable dan Finance & Accounting).
- Kemampuan teknis (disediakan tim FE/BE): seed API untuk memulihkan Putri Anggraeni ke Pre-setup #48 (di hook `before`, pada langkah penghubung akhir, dan di hook `after`); pembacaan jumlah entri Tab Changelog target, Tab System Log aktor, dan Activity Log sebelum aksi sebagai baseline (bagian 8b butir 10); jalur navigasi ke Tab System Log aktor dan Activity Log (tidak disebut TC). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: status Group Manager dan seluruh baris pola serta penugasan Putri Anggraeni; dipulihkan ke Pre-setup #48 lewat seed API pada langkah 35 dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1090: Remove satu baris pola Transaction Role target Group Manager: dialog Auto-Revert D-05c varian Role Transaksi, Cancel tanpa perubahan, dan konfirmasi melepas GM dengan baris pola dipertahankan

1. Catat jumlah entri Tab Changelog Putri Anggraeni, Tab System Log aktor, dan Activity Log sebagai baseline
2. Ketik Search `Putri Anggraeni`, tekan Enter, lalu klik Name `Putri Anggraeni`
3. Klik Tab Role lalu Sub-tab Transaction Role
4. Verifikasi banner Group Manager tampil di Sub-tab Transaction Role
5. Klik ⋯ pada baris Transfer x Approver lalu klik `Remove`
6. Verifikasi dialog tampil dengan Title `Remove Group Manager` (varian Role Transaksi), Body bullet `• Putri Anggraeni`, kalimat `This change will remove Group Manager status for this group.`, `Their other role assignments will remain as they are.` dan `Are you sure you want to remove it?`, serta tombol `[Cancel]` (Text, Contrast) dan `[Remove]`
7. Verifikasi dialog `Remove Transaction Role` (D-07) maupun `Change Transaction Role` (D-06) tidak tampil
8. Klik `[Cancel]` pada dialog
9. Verifikasi tidak ada toast
10. Verifikasi dialog tertutup
11. Verifikasi baris Transfer x Approver tetap ada
12. Verifikasi banner Group Manager tetap tampil di Sub-tab Transaction Role
13. Klik Tab Changelog
14. Verifikasi jumlah entri Tab Changelog Putri Anggraeni sama dengan baseline
15. Klik Tab Role lalu Sub-tab Transaction Role
16. Klik ⋯ pada baris Transfer x Approver lalu klik `Remove`
17. Verifikasi dialog dengan Title `Remove Group Manager` tampil
18. Klik `[Remove]` pada dialog
19. Verifikasi toast gabungan sukses Remove Transaction Role disertai klausa auto-revert Group Manager tampil
20. Verifikasi hanya satu toast yang tampil, bukan toast terpisah
21. Verifikasi banner Group Manager hilang di Sub-tab Transaction Role
22. Verifikasi baris non-pola Disposal x Staff (IT Infrastructure) dan Damaged x Monitoring & Report (Branch Surabaya) tetap ada
23. Verifikasi baris Transfer x Approver terhapus oleh aksi Remove aktor sendiri
24. Verifikasi seluruh baris pola Group Manager Transaction Role lain (Asset Admin dan Approver pada seluruh Jenis Transaksi untuk Accounts Payable dan Finance & Accounting) tetap tersimpan sebagai baris biasa
25. Klik Sub-tab Group Role
26. Verifikasi banner Group Manager hilang di Sub-tab Group Role
27. Verifikasi baris non-pola Manage user & role pada Finance & Accounting tetap ada
28. Verifikasi seluruh baris pola Group Manager Group Role (Group Role katalog selain Manage user & role pada Finance & Accounting dan Accounts Payable) tetap tersimpan sebagai baris biasa
29. Klik Tab Changelog Putri Anggraeni lalu muat ulang sampai entri tampil
30. Verifikasi entri `Auto-Revert` dengan Object `Group Manager` tercatat (selisih baseline) di Tab Changelog Putri Anggraeni
31. Buka Tab System Log aktor
32. Verifikasi entri `Auto-Revert` dengan Object `Group Manager` tercatat (selisih baseline) di Tab System Log aktor
33. Buka Activity Log
34. Verifikasi entri `Auto-Revert` dengan Object `Group Manager` tercatat (selisih baseline) di Activity Log
35. Pulihkan Putri Anggraeni ke Pre-setup #48 lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan: Cancel (langkah 5 sampai 14) lebih dulu, lalu konfirmasi `[Remove]` yang mengubah state (S-09, S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 3, 13, 15, 25, 29, 31, 33 dan 35. Search `Putri Anggraeni` pada langkah 2 adalah langkah penghubung untuk menemukan baris target (R-16, R-23). Baseline log mengikuti S-12; pemulihan lewat seed API memulihkan Pre-setup #48 (S-06, S-09).
- Anchor 8b butir 2: `Verifikasi` banner Group Manager tampil (langkah 4, tidak tertulis di Expected TC) menjadi anchor bagi banner hilang (langkah 21, 26); dialog tampil (langkah 6) menjadi anchor bagi asersi tidak ada toast dan dialog D-07 atau D-06 tidak tampil (langkah 7, 9). Baris pola Group Manager tidak lagi diasersi sebagai absence: baris Transfer x Approver terhapus oleh aksi aktor (langkah 23), baris pola lain tetap tersimpan (langkah 24, 28), dan baris non-pola tetap ada (langkah 22, 27).
- Klausa "dalam transaksi atomik yang sama" (Expected d) tidak teramati terpisah lewat UI; keadaan akhir lengkap diasersi pada langkah 21 sampai 28 dan atomisitas tidak punya langkah observasi.
- Tidak adanya entri `Remove (via Group Manager)` per baris pola pada surface mana pun (Expected e) dirujuk ke TC-FA-SU-1098 dan tidak diasersi di spec ini (spec 403).
- Pembagian TC lintas spec: TC-FA-SU-1091 (Bulk Remove target Group Manager) ada di spec 405.
- Surface log untuk "tanpa entri log" setelah `[Cancel]` (langkah 14) adalah Tab Changelog target; Expected TC tidak menyebut surface.
- Temuan untuk QA:
  - Copy dialog D-05c varian Role Transaksi dan tombol `[Remove]` bertanda "copy usulan, perlu persetujuan PM" (TC-FA-SU-1090 butir a; `D-05` `settings-role-permission` Open Item #7d). Spec memakai teks apa adanya; PRD DO-12 menyebut tombol `[Revoke]` pada dialog D-10 (jalur Edit Home Group) sedangkan DO-02 memakai `[Remove]` untuk D-05; mohon dikonfirmasi label D-05c.
  - Toast gabungan (butir c, T-06b dengan T-17/T-18 klausa auto-revert Group Manager) tidak ditulis literal di TC maupun PRD; spec mengasersi toast gabungan secara longgar (sukses Remove Transaction Role disertai klausa auto-revert) tanpa teks persis.
  - Teks banner Group Manager untuk Putri Anggraeni tidak tertulis di TC; spec hanya mengasersi banner Group Manager tampil atau hilang. Spec 386 (TC-FA-SU-1074) masih menyatakan banner Group Manager tidak tampil di Sub-tab Transaction Role, sedangkan TC-FA-SU-1090 mengasersi banner tampil di sub-tab itu.
  - TC-FA-SU-1090 ACC menyebut `#20` (id Client `FaUserMain`, bukan nomor akun); aktor diambil dari langkah "Login sebagai Ahmad Dahlan (Default User)". Mohon dikonfirmasi.
  - Post Condition notifikasi in-app view-only ke Putri Anggraeni tidak punya langkah observasi di TC dan tidak diasersi; Putri Anggraeni juga tidak punya nama env password di `suite.md`.
  - TC menyebut Expected e "entri `Auto-Revert` tercatat" tanpa surface; spec membaca tiga surface (Tab Changelog target, Tab System Log aktor, Activity Log) dari Post Condition b. Belum jelas apakah baris pemicu (aksi `Edit` atau `Remove` baris Transfer x Approver) ikut dicatat sebagai entri tersendiri sebelum `Auto-Revert`; TC hanya menyebut "Auto-Revert", sehingga spec tidak mengasersi entri baris pemicu.
  - Jalur navigasi ke Tab System Log aktor dan Activity Log tidak disebut TC (langkah 31, 33).
