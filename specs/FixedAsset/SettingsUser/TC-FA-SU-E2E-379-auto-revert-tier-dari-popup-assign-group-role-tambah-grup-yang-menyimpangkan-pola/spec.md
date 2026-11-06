---
id: TC-FA-SU-E2E-379-auto-revert-tier-dari-popup-assign-group-role-tambah-grup-yang-menyimpangkan-pola
title: "Auto-Revert Tier dari Popup Assign Group Role: Tambah Grup yang Menyimpangkan Pola"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-1078
coverage:
  web: automated
---

# Auto-Revert Tier dari Popup Assign Group Role: Tambah Grup yang Menyimpangkan Pola

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21, termasuk General Affairs) dan penugasan (Pre-setup #23).
- Pengguna target: Lina Marlina, Total Control (Pre-setup #1 dan #23), dan Citra Lestari, Read Only (Pre-setup #3 dan #23).
- Data uji: grup `General Affairs` ditambahkan lewat `[+ Assign Group]` pada popup Assign Group Role dengan centang default (Read saja).
- Kemampuan teknis (disediakan tim FE/BE): fixture seed backend yang mengeluarkan baris `General Affairs` pada role `Manage files` Lina Marlina dan Citra Lestari dari pola tanpa memicu auto-revert (belum ada baris Pre-setup khusus; role `Manage files` adalah asumsi spec karena TC tidak menyebut role terpilih, lihat Notes); seed API untuk memulihkan penugasan keduanya ke Pre-setup #23; pembacaan jumlah entri Tab Changelog target, Tab System Log aktor, dan Activity Log sebelum aksi sebagai baseline (bagian 8b butir 10); jalur navigasi ke Tab System Log aktor dan Activity Log (tidak disebut TC). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: tier dan baris Group Role Manage files x General Affairs milik Lina Marlina dan Citra Lestari; dipulihkan ke Pre-setup #23 lewat seed API pada langkah penghubung dan di hook `after`. Suite berjalan serial.
- Target tanpa Home Group (Pre-setup #50, `FaUserNoHG`; Catatan TC: TC penugasan Tab Role Section 3d, 3e, 4c, 8, dan 9 yang memilih node bebas dijalankan pada varian tanpa Home Group, FI-32), diterapkan per target: Home Group Lina Marlina (IT Infrastructure pada Pre-setup #43) dikosongkan lewat seed API di hook `before` supaya node General Affairs (langkah 8) tidak Disabled oleh gate Home Group constraint; Home Group Lina Marlina dipulihkan ke IT Infrastructure di hook `after`. Seed per target disediakan tim FE/BE.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1078: Assign Group (tambah grup) pada target Total Control yang menyimpangkan pola: dialog Auto-Revert D-05a; pada target Read Only dengan default Read saja tidak menyimpang

1. Keluarkan baris Manage files x General Affairs milik Lina Marlina dan Citra Lestari dari pola lewat seed backend tanpa auto-revert
2. Catat jumlah entri Tab Changelog Lina Marlina dan Citra Lestari, Tab System Log aktor, dan Activity Log sebagai baseline
3. Ketik Search `Lina Marlina`, tekan Enter, lalu klik Name `Lina Marlina`
4. Klik Tab Role lalu Sub-tab Group Role
5. Verifikasi banner `This user has Total Control access.` tampil di Sub-tab Group Role
6. Buka popup Assign Group Role Manage files
7. Klik `[+ Assign Group]`
8. Centang General Affairs lalu klik `[Select]`
9. Klik `[Save]` tanpa mengubah centang default (Read saja)
10. Verifikasi dialog Auto-Revert D-05a dengan Title `Remove Total Control` tampil, bukan toast assigned langsung
11. Klik `[Remove]`
12. Verifikasi General Affairs tersimpan pada Manage files Lina Marlina
13. Verifikasi banner `This user has Total Control access.` hilang di Sub-tab Group Role
14. Verifikasi baris Group Role role lain milik Lina Marlina tidak berubah
15. Buka Tab Changelog, Search `Lina Marlina`, tekan Enter, lalu muat ulang sampai entri tampil
16. Verifikasi entri `Assign` Object `Group Role` dan entri `Auto-Revert` tercatat satu kali (selisih baseline) di Tab Changelog Lina Marlina
17. Buka Tab System Log aktor
18. Verifikasi entri `Assign` dan entri `Auto-Revert` tercatat satu kali (selisih baseline) di Tab System Log aktor
19. Buka Activity Log
20. Verifikasi entri `Assign` dan entri `Auto-Revert` tercatat satu kali (selisih baseline) di Activity Log
21. Pulihkan penugasan Lina Marlina ke Pre-setup #23 lewat seed API
22. Kembali ke daftar User lewat Breadcrumb
23. Ganti isi kotak search dengan `Citra Lestari`, tekan Enter, lalu klik Name `Citra Lestari`
24. Klik Tab Role lalu Sub-tab Group Role
25. Verifikasi banner `This user has Read Only access.` tampil di Sub-tab Group Role
26. Buka popup Assign Group Role Manage files
27. Klik `[+ Assign Group]`
28. Centang General Affairs lalu klik `[Select]`
29. Klik `[Save]` tanpa mengubah centang default (Read saja)
30. Verifikasi toast "Success, group role has been assigned."
31. Verifikasi tidak ada dialog Auto-Revert
32. Verifikasi banner `This user has Read Only access.` tetap tampil
33. Buka Tab Changelog, Search `Citra Lestari`, tekan Enter, lalu muat ulang sampai entri tampil
34. Verifikasi entri `Assign` Object `Group Role` tercatat satu kali (selisih baseline) di Tab Changelog Citra Lestari
35. Buka Tab System Log aktor
36. Verifikasi entri `Assign` tercatat satu kali (selisih baseline) di Tab System Log aktor
37. Buka Activity Log
38. Verifikasi entri `Assign` tercatat satu kali (selisih baseline) di Activity Log
39. Pulihkan penugasan Citra Lestari ke Pre-setup #23 lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 3, 15, 17, 19, 21, 22, 23, 33, 35, 37 dan 39. Search pada langkah 3, 15, 23 dan 33 adalah langkah penghubung untuk menemukan baris target (R-16, R-23). Baseline log mengikuti S-12; pemulihan lewat seed API memulihkan Pre-setup #23 (S-06, S-09).
- Langkah pola baca-log: langkah 15 sampai 20 dan 33 sampai 38.
- Asersi "tidak ada entri `Auto-Revert` untuk Citra Lestari" (Post Condition TC) tidak ditulis di spec ini; rujukan S-05: asersi absence log hanya di spec absence (kelas g). Spec ini mengasersi tidak adanya dialog Auto-Revert (langkah 31) setelah toast sukses sebagai anchor (8b butir 2).
- Alasan di atas sekitar 35 langkah (blok baca-log berpola tidak dihitung menurut bagian 3 prinsip 13, Smell): satu TC (satu spec per TC, C2) yang mencakup dua target berurutan (Lina Marlina lalu Citra Lestari), tanpa kelas harness; Expected memuat tiga butir bermajemuk dan tiga surface log per target yang dibaca satu per satu (S-01).
- TC-FA-SU-1079 (Cancel dialog Auto-Revert dari popup) ada di spec 384.
- Pre-setup #50 diterapkan hanya pada Lina Marlina (bukan seluruh 25 pengguna): pemilih Group Role dan Role Transaksi men-Disabled node di luar Home Group constraint target (FI-32, tooltip S-45) dan permintaan langsung di luar constraint ditolak `422`, sedangkan TC ini memilih General Affairs (langkah 8); Home Group Lina Marlina dipulihkan di hook `after`. Mohon dikonfirmasi bila #50 harus diterapkan penuh.
- Temuan untuk QA:
  - TC-FA-SU-1078 langkah 2 ("pada role yang belum memuat grup General Affairs (fixture, lihat Data Uji)") tidak menyebut role terpilih dan belum ada baris Pre-setup untuk fixture; spec memakai `Manage files` (konsisten dengan TC-FA-SU-1076, 1077 dan 1079) dan menuliskan fixture sebagai kebutuhan tim BE di `## Prerequisites`. Mohon ditambahkan baris Pre-setup khusus atau penyebutan role.
  - TC-FA-SU-1078 Post Condition menyebut entri `Assign` dan `Auto-Revert` (hanya Lina) tercatat pada tiga surface log tanpa menyebut Field, Old Value, dan New Value entri `Assign`; spec hanya mengasersi Object `Group Role` dan jumlah entri.
