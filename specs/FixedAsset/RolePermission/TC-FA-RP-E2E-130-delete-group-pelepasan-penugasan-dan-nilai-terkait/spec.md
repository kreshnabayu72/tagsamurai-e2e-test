---
id: TC-FA-RP-E2E-130-delete-group-pelepasan-penugasan-dan-nilai-terkait
title: "Delete Group: pelepasan penugasan dan nilai terkait"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-448
  - TC-FA-RP-449
  - TC-FA-RP-469
  - TC-FA-RP-470
coverage:
  web: automated
---

# Delete Group: pelepasan penugasan dan nilai terkait

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun kedua untuk TC 449: Kevin Susanto (Pre-setup #13; email data pengguna `kevinsusanto@qwertysystem.net`; password disediakan tim FE, nama env belum tertulis di sumber; lihat Temuan untuk QA).
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (hanya dibaca, tidak dihapus atau diubah spec ini): #18 (pohon Group; `IT Infrastructure` menjadi induk subtree milik spec), #43 (Fajar Nugroho Group Manager di `IT Infrastructure`, pembanding positif langkah 4), #19 (Role Transaksi pada `IT Infrastructure`), #39 (baris Citra Lestari `Manage files` di `Head Office`, pembanding absence).
- Data Dinamis milik spec (S-06, S-12; pola spec 129): subtree group `Zona Uji {runId}-130` di bawah `IT Infrastructure` dengan anak `Rak Uji {runId}-130`, di-seed lewat seeding API di hook `before`: Kevin Susanto (Pre-setup #13, Group Manager) di `Zona Uji {runId}-130`; Budi Santoso `Manage files` di `Rak Uji {runId}-130`; satu user kolam #15 sebagai Asset Admin pada `Zona Uji {runId}-130` sub-tab `Disposal` dengan Require Approval ON (TC 448 tidak menyebut nama user; pilihan tim FE); Home Group Gunawan Halim (Pre-setup #17) diatur ke `Zona Uji {runId}-130`. Subtree dan penugasannya di-seed ulang lewat seeding API sebagai langkah penghubung sesudah tiap blok TC yang menghapusnya (langkah 12, 20, 31). Hook `after` menghapus subtree itu bila masih ada dan memulihkan Home Group Gunawan Halim ke `Data Center` (Pre-setup #17). Group Pre-setup bersama (`Data Center`, `Rack A1`, #18 dan #43) tidak dihapus spec ini.
- Kemampuan teknis: seeding API dan penghapusan subtree milik spec; kemampuan membaca jumlah entri Changelog Tab Transaction Role (baseline, S-12) disediakan tim FE/BE.

## Test Steps

### Delete Group melepas penugasan dan nilai terkait (TC 448)

1. Buka Fixed Asset > Settings > Groups, hapus group `Zona Uji {runId}-130` lewat row action Delete, lalu klik `[Delete]` pada dialog `Delete Group`.
2. Tunggu aksi selesai (group `Zona Uji {runId}-130` hilang dari daftar Group).
3. Buka Fixed Asset > Settings > Role & Permission > Group Manager.
4. Verifikasi sedikitnya satu baris tampil di Tab Group Manager (baris Fajar Nugroho di `IT Infrastructure`).
5. Verifikasi baris Kevin Susanto di `Zona Uji {runId}-130` hilang dari Tab Group Manager.
6. Buka Detail Role `Manage files` dan klik `All Groups`.
7. Verifikasi baris Citra Lestari di `Head Office` tampil pada `Manage files`.
8. Verifikasi baris Budi Santoso di `Rak Uji {runId}-130` hilang dari `Manage files`.
9. Buka Tab Transaction Role dan perhatikan Sidebar Group Tree.
10. Verifikasi node `IT Infrastructure` tampil di Sidebar Group Tree.
11. Verifikasi node `Zona Uji {runId}-130` dan `Rak Uji {runId}-130` tidak ada lagi di Sidebar Group Tree beserta penugasan Role Transaksi dan nilai persetujuannya.
12. Seed ulang subtree milik spec (Prerequisites, Data Dinamis) beserta penugasannya lewat seeding API hingga tersimpan.

### Delete Group tidak mengirim notifikasi ke pemegang penugasan (TC 449)

13. Buka Fixed Asset > Settings > Groups, hapus group `Zona Uji {runId}-130`, lalu klik `[Delete]`.
14. Tunggu aksi selesai (group `Zona Uji {runId}-130` hilang dari daftar Group).
15. Ganti akun: logout, lalu login sebagai Kevin Susanto.
16. Buka daftar notifikasi.
17. Verifikasi daftar notifikasi terbuka.
18. Verifikasi tidak ada notifikasi tentang pelepasan Group Manager di `Zona Uji {runId}-130`.
19. Ganti akun: logout, lalu login sebagai Total Control Siti Rahmawati.
20. Seed ulang subtree milik spec (Prerequisites, Data Dinamis) beserta penugasannya lewat seeding API hingga tersimpan.

### Delete Group tidak mencatat nilai Require Approval (TC 469)

21. Siapkan Require Approval ON di `Zona Uji {runId}-130` sub-tab `Disposal` lewat seeding API hingga tersimpan.
22. Buka Tab Transaction Role, klik node `IT Infrastructure`, lalu sub-tab `Disposal`.
23. Buka Changelog dari ikon di baris sub-tab `Disposal`, catat jumlah entri sebagai baseline, lalu tutup modal Changelog.
24. Buka Fixed Asset > Settings > Groups, hapus group `Zona Uji {runId}-130`, lalu klik `[Delete]`.
25. Tunggu aksi selesai (group `Zona Uji {runId}-130` hilang dari daftar Group).
26. Buka Tab Transaction Role, klik node `IT Infrastructure`, lalu sub-tab `Disposal`.
27. Buka Changelog dari ikon di baris sub-tab `Disposal`.
28. Verifikasi modal Changelog memuat sedikitnya satu entri.
29. Verifikasi jumlah entri sama dengan baseline (tidak ada entri untuk nilai Require Approval yang ikut hilang).
30. Tutup modal Changelog.
31. Seed ulang subtree milik spec (Prerequisites, Data Dinamis) beserta penugasannya lewat seeding API hingga tersimpan.

### Delete Group menghapus Home Group secara silent (TC 470)

32. Buka Fixed Asset > Settings > Groups, hapus group `Zona Uji {runId}-130`, lalu klik `[Delete]`.
33. Tunggu aksi selesai (group `Zona Uji {runId}-130` hilang dari daftar Group).
34. Buka Settings > User > Detail Gunawan Halim.
35. Verifikasi Home Group Gunawan Halim kosong.

## Notes

- Spec ini memuat 35 langkah. Keempat blok berkelas fungsional sama dan memakai subtree group milik spec (S-06): tiap blok menghapus subtree itu dan blok berikutnya menyiapkannya lewat seed ulang (langkah 12, 20, 31), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna dan group Pre-setup bersama tidak ikut terhapus. Pemulihan akhir (Home Group Gunawan Halim ke `Data Center`) ada di hook `after`, bukan langkah.
- P-1 (state berat): TC 469 punya Expected absence log ("Changelog tidak memuat entri untuk nilai Require Approval yang ikut hilang") yang bergantung pada state berat hasil Delete Group (cascade nilai Require Approval) yang dibangun langkah sebelumnya di spec ini; asersi absence tetap di sini dengan baseline (langkah 23) dan pembanding positif (langkah 28), bukan di spec absence.
- Langkah penghubung (S-03): 2, 3, 6, 9, 12, 14, 16, 20 sampai 27, 30 sampai 34; langkah 4, 7, 10, dan 17 adalah pembanding positif untuk asersi absence sesudahnya (8b butir 2 dan 11).
- Pemicu penghapusan subtree milik spec lewat UI Settings > Groups dan akun Kevin Susanto pada langkah 15 adalah ganti akun eksplisit dalam satu browser (berurutan, bukan konteks kedua simultan).
- Temuan untuk QA:
  - TC 448, 449, 469, dan 470 menamai group `Data Center` dan `Rack A1` (Pre-setup #18, dipakai bersama spec lain); spec memakai subtree milik spec bersuffix (Prerequisites) dan menulis nama subtree itu pada langkah dan Expected supaya tidak menghapus group Pre-setup bersama (S-06). Perilaku yang diasersi sama dengan TC.
  - TC 448 precondition c tidak menyebut user Asset Admin pada group yang dihapus; spec memakai satu user kolam #15 pilihan tim FE.
  - TC 448 Post Condition a (entri `Remove (Group Deleted)` per penugasan dan tidak ada notifikasi) dan Post Condition TC 449 serta TC 470 untuk log tidak punya langkah observasi di TC dan tidak diasersi.
  - TC 470 Expected "tanpa entri log dan tanpa notifikasi" tidak menyebut surface log maupun akun pengamat notifikasi Gunawan Halim dan tidak punya langkah observasi; hanya klausa Home Group kosong yang diasersi sampai QA menetapkan surface.
  - TC 469 precondition menyebut Pre-setup #24 (`Company Changelog`), sedangkan TC lain di blok ini memakai Company Alpha (#18, #19); spec berjalan pada Company Alpha dan memakai baseline jumlah entri Changelog (bukan data #24).
  - TC 449 butuh login Kevin Susanto, tetapi email dan nama env passwordnya tidak ada di Pre-setup TC maupun `suite.md`; didaftarkan tim FE.
  - TC 469 punya klausa absence log; TC 470 punya klausa "tanpa entri log". Keduanya tidak punya spec absence tersendiri, sehingga TC 469 ditangani dengan P-1 di atas dan TC 470 dengan catatan di butir sebelumnya.
