---
id: TC-FA-SU-E2E-077-transaction-role-save-identik-guard-server-turun-tangga-grup-dihapus-edit-bersamaan
title: "Transaction Role: Save Identik, Guard Server Turun Tangga, Grup Dihapus, Edit Bersamaan, dan Sebagian Grup Identik"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-253
  - TC-FA-SU-254
  - TC-FA-SU-256
  - TC-FA-SU-278
  - TC-FA-SU-280
coverage:
  web: automated
---

# Transaction Role: Save Identik, Guard Server Turun Tangga, Grup Dihapus, Edit Bersamaan, dan Sebagian Grup Identik

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Pelaku kedua (Admin B, Pre-setup #13): sesi API yang memicu perubahan state tanpa konteks UI kedua (R-20); akun disediakan tim FE. Sesi API memakai token yang tidak dihitung sebagai sesi web (`suite.md`). Admin B menyimpan assignment atau menghapus grup hingga tersimpan.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan Transaction Role (Pre-setup #39) untuk TC-FA-SU-253, 256, 278, dan 280; tenant `FaUserTR` (Pre-setup #44, varian `FaUserMain`) untuk TC-FA-SU-254. Perpindahan tenant ke `FaUserTR` dengan akun aktor yang sama adalah kemampuan "disediakan tim FE" (TC tidak menyebut caranya, lihat Temuan untuk QA).
- Pengguna target: Mira Anggraini pada `FaUserMain` (Disposal × Staff dan Borrowing & Assignment × Approver pada Finance & Accounting); Nanda Pratama pada `FaUserTR` (Disposal × Monitoring & Report, Transfer × Asset Admin, Transfer × Monitoring & Report, dan Transfer × Approver, seluruhnya pada Finance & Accounting).
- Data uji: Damaged × Monitoring & Report pada Finance & Accounting (TC-FA-SU-253); Transfer × Asset Admin pada Logistics Warehouse, grup yang dihapus Admin B (TC-FA-SU-256); Disposal pada Finance & Accounting dengan Asset Admin lalu Monitoring & Report (TC-FA-SU-278); Disposal × Staff pada Branch Surabaya (identik) dan IT Infrastructure (baru) (TC-FA-SU-280); Disposal × Staff pada Finance & Accounting untuk Nanda Pratama (TC-FA-SU-254).
- Kemampuan teknis: seed API untuk memulihkan Transaction Role Mira Anggraini dan Nanda Pratama serta grup Logistics Warehouse beserta penugasannya (Pre-setup #21, #39, #44; disediakan tim FE/BE); pembacaan jumlah entri Tab Changelog target sebelum aksi sebagai baseline (disediakan tim FE/BE, bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: Transaction Role Mira Anggraini dan Nanda Pratama serta grup Logistics Warehouse (dihapus); dipulihkan lewat seed API di hook `after`. Suite berjalan serial.
- Target tanpa Home Group (Pre-setup #50, `FaUserNoHG`; Catatan TC: TC penugasan Tab Role Section 3d, 3e, 4c, 8, dan 9 yang memilih node bebas dijalankan pada varian tanpa Home Group, FI-32), diterapkan per target: Home Group Mira Anggraini (Finance & Accounting pada Pre-setup #43) dikosongkan lewat seed API di hook `before` supaya node Logistics Warehouse (langkah 10), Branch Surabaya (penugasan Admin B langkah 29, juga dipilih pada langkah 31), dan IT Infrastructure (langkah 31) tidak Disabled oleh gate Home Group constraint dan penugasan Admin B lewat sesi API tidak ditolak `422`; Home Group Mira Anggraini dipulihkan ke Finance & Accounting di hook `after`. Seed per target disediakan tim FE/BE.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-253: Save identik dengan assignment existing: toast No-Op dan tanpa entri log

1. Ketik Search `Mira Anggraini`, tekan Enter, lalu buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role, klik `[+ Assign]`, lalu isi Group Finance & Accounting, Transaction Damaged, dan Role Monitoring & Report
2. Admin B menyimpan Damaged × Monitoring & Report untuk Finance & Accounting pada Mira Anggraini lewat sesi API hingga assignment tersimpan
3. Catat jumlah entri `Assign` Object `Transaction Role` Mira Anggraini pada Tab Changelog sebagai baseline dibaca setelah entri `Assign` Field `Damaged — Finance & Accounting — Monitoring & Report` milik Admin B tampil (sesudah assignment Admin B; dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit)
4. Klik `[Submit]` pada sesi A
5. Verifikasi toast "No changes to save."
6. Verifikasi tidak ada toast error
7. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang
8. Verifikasi jumlah entri `Assign` Object `Transaction Role` Mira Anggraini pada Tab Changelog sama dengan baseline

### TC-FA-SU-256: Grup dihapus sebelum Save modal: toast stale, Group stale dibersihkan, dan modal tetap terbuka

9. Catat jumlah entri Object `Transaction Role` Mira Anggraini pada Tab Changelog sebagai baseline
10. Kembali ke User List, ganti isi kotak search dengan `Mira Anggraini`, tekan Enter, lalu buka ulang Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role, klik `[+ Assign]`, lalu pilih Group Logistics Warehouse, Transaction Transfer, dan Role Asset Admin
11. Admin B menghapus grup Logistics Warehouse di Settings > Groups lewat sesi API hingga grup terhapus
12. Klik `[Submit]`
13. Verifikasi toast "Error, failed to assign Asset Admin. One or more selected groups no longer exist. Please select another."
14. Verifikasi Group stale Logistics Warehouse dihapus dari pilihan (tombol Group berlabel `Select Group`)
15. Verifikasi modal tetap terbuka
16. Klik `[✕]` pada modal
17. Verifikasi dialog `Unsaved Changes`
18. Klik `[Leave]`
19. Verifikasi tidak ada baris Transfer × Asset Admin baru pada tabel Mira Anggraini
20. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang
21. Verifikasi jumlah entri Object `Transaction Role` Mira Anggraini pada Tab Changelog sama dengan baseline

### TC-FA-SU-278: Edit bersamaan Transaction Role mengikuti last-write-wins

22. Kembali ke User List, ganti isi kotak search dengan `Mira Anggraini`, tekan Enter, lalu buka ulang Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role, klik `[+ Assign]`, lalu isi Group Finance & Accounting, Transaction Disposal, dan Role Asset Admin
23. Klik `[Submit]` pada sesi A
24. Tunggu aksi selesai (modal tertutup) sebelum sesi berpindah
25. Admin B menyimpan Disposal × Monitoring & Report untuk Finance & Accounting pada Mira Anggraini lewat sesi API, dengan konfirmasi turun tangga, hingga assignment tersimpan
26. Muat ulang Sub-tab Transaction Role Mira Anggraini
27. Verifikasi role Disposal pada Finance & Accounting mengikuti permintaan yang terakhir diterima (Monitoring & Report)
28. Verifikasi tidak ada dialog konflik versi

### TC-FA-SU-280: Save dengan sebagian Group identik: baris identik dilewati tanpa keterangan tambahan pada toast

29. Admin B menambahkan Disposal × Staff pada Branch Surabaya untuk Mira Anggraini lewat sesi API hingga assignment tersimpan
30. Catat jumlah entri `Assign` Object `Transaction Role` Mira Anggraini pada Tab Changelog sebagai baseline dibaca setelah entri `Assign` Field `Disposal — Branch Surabaya — Staff` milik Admin B tampil (sesudah assignment Admin B; dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit)
31. Pada tampilan sesi A yang belum dimuat ulang, klik `[+ Assign]`, pilih Group Branch Surabaya dan IT Infrastructure, Transaction Disposal, dan Role Staff, lalu klik `[Submit]`
32. Verifikasi toast "Success, Staff has been assigned." tanpa kata skipped atau keterangan baris identik
33. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang sampai entri tampil
34. Verifikasi satu entri `Assign` untuk Group baru IT Infrastructure (Disposal — IT Infrastructure — Staff) bertambah dibanding baseline pada Tab Changelog
35. Verifikasi tidak ada entri `Assign` untuk Branch Surabaya (jumlah entri baru tepat satu) pada Tab Changelog

### TC-FA-SU-254: Guard server menolak Save turun tangga tanpa konfirmasi: dialog konteks dan tabel di-refresh

36. Pindah ke tenant `FaUserTR` dengan akun aktor yang sama
37. Ketik Search `Nanda Pratama`, tekan Enter, lalu buka Detail Nanda Pratama > Tab Role > Sub-tab Transaction Role, klik `[+ Assign]`, lalu isi Group Finance & Accounting, Transaction Disposal, dan Role Staff
38. Admin B mengubah Disposal Finance & Accounting Nanda Pratama menjadi Asset Admin lewat sesi API hingga perubahan tersimpan
39. Klik `[Submit]` pada sesi A
40. Verifikasi dialog Title `User Updated` dengan Body `This user was changed by someone else. Please review.` dan tombol `[OK]`
41. Klik `[OK]`
42. Verifikasi tabel di-refresh: Disposal pada Finance & Accounting Nanda Pratama menampilkan Asset Admin
43. Verifikasi Save Staff ditolak seluruhnya: tidak ada baris Disposal × Staff pada Finance & Accounting

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-FA-SU-253, 256, 278, 280, lalu 254, supaya perpindahan tenant ke `FaUserTR` terjadi satu kali di akhir (TC-FA-SU-254 memakai `FaUserTR`, sisanya `FaUserMain`).
- Pelaku kedua (Admin B) dipicu lewat sesi API dan bukan konteks UI kedua, sehingga tidak memakai `P-2` (bagian 3 prinsip 13, `[KEPUTUSAN 2026-10-30]`). Sesi A adalah sesi UI aktor (Total Control).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 3, 9, 16 sampai 18, 24, 30 dan 36. Baseline log dicatat sesudah aksi Admin B karena aksi itu menambah entri sendiri, dan baseline menunggu entri Admin B tampil karena entri log muncul eventual (S-12, bagian 6); penutupan modal dirty mengikuti S-08.
- Langkah pola baca-log: langkah 7, 8, 20, 21 dan 33 sampai 35. Search `Mira Anggraini` pada langkah itu adalah langkah penghubung untuk menemukan baris target (R-16).
- Klausa "tidak ada entri log" pada TC-FA-SU-253 dan 256 (aksi yang tidak mengubah data atau gagal) ditulis sebagai asersi jumlah dengan baseline di spec fungsional (bagian 3 prinsip 13 butir g, S-12); toast menjadi anchor positif.
- Jumlah langkah 43, di atas smell 35 langkah: 36 langkah di luar blok baca-log berpola (7 langkah, tidak dihitung pada smell bagian 3 prinsip 13); seluruh blok satu topik (konflik dua pelaku pada Save Transaction Role Mira Anggraini dan Nanda Pratama) dan satu pola pelaku kedua lewat sesi API; tiap TC memakai baris Transaction Role yang berbeda sehingga tidak saling mengandalkan hasil TC lain.
- Pre-setup #50 diterapkan hanya pada Mira Anggraini (bukan seluruh 25 pengguna): pemilih Group Role dan Role Transaksi men-Disabled node di luar Home Group constraint target (FI-32, tooltip S-45) dan permintaan langsung di luar constraint ditolak `422`, sedangkan TC ini memilih Logistics Warehouse (langkah 10), Branch Surabaya (penugasan Admin B langkah 29, juga dipilih pada langkah 31), dan IT Infrastructure (langkah 31); Home Group Mira Anggraini dipulihkan di hook `after`. Mohon dikonfirmasi bila #50 harus diterapkan penuh.
- Search nama pengguna target pada User List digabung dalam langkah buka Detail (langkah 1, 10, 22 dan 37): langkah penghubung untuk menemukan baris target karena User List memuat 25 pengguna pada 3 halaman (R-16, bagian 8b butir 13); langkah 10 dan 22 mengganti isi kotak search yang masih berisi nama sebelumnya (bagian 8b butir 9).
- Temuan untuk QA:
  - TC-FA-SU-253, 254, 256, 278, dan 280 menyebut "Sesi A dan B" yang membuka modal atau tampilan basi; spec menjadikan sesi UI aktor sebagai sesi A dan Admin B sebagai sesi API, sehingga "B membuka modal" tidak ditulis.
  - TC-FA-SU-278 menyebut sesi B "konfirmasi dialog turun tangga"; spec menulisnya sebagai penyimpanan lewat sesi API dengan konfirmasi turun tangga tanpa mengarang endpoint. TC-FA-SU-278 tidak menyebut pengguna target; spec memakai Mira Anggraini.
  - TC-FA-SU-254 langkah 4 ("Klik `[OK]`") ditulis setelah Verifikasi dialog; TC tidak menyebut pengguna di luar Nanda Pratama untuk guard server pada `FaUserMain`.
  - TC-FA-SU-254 butir a ("server menolak seluruh Save tanpa perubahan") tidak punya cara observasi langsung selain state tabel; spec mengasersi tidak ada baris Disposal × Staff pada Finance & Accounting.
  - Post Condition TC-FA-SU-253, 254, 256, 278, dan 280 tidak punya langkah observasi di TC selain yang diasersi di atas dan tidak diasersi lagi.
