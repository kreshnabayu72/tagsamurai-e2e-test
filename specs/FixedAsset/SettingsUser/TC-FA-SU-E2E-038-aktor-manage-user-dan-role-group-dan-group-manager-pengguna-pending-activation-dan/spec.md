---
id: TC-FA-SU-E2E-038-aktor-manage-user-dan-role-group-dan-group-manager-pengguna-pending-activation-dan
title: "Aktor Manage user & role Group dan Group Manager, Pengguna Pending Activation, dan Resolusi Approver"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-131
  - TC-FA-SU-132
  - TC-FA-SU-133
coverage:
  web: automated
---

# Aktor Manage user & role Group dan Group Manager, Pengguna Pending Activation, dan Resolusi Approver

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Lina Marlina`), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip `seen`, sesi API aktor, pemulihan) mengikuti `suite.md`.
- Akun ganti akun (langkah eksplisit, hook `after` memulihkan sesi ke Total Control default suite):

  | Role yang diuji | Akun | Password |
  |---|---|---|
  | Manage user & role Group (Update), Group Role pada Finance & Accounting | Pre-setup #6, `Sinta Dewi`; email tidak tertulis di Pre-setup TC, disediakan tim FE | `Spectra.env.FA_MURGR_UPD_PASSWORD` |
  | Group Manager (IT Infrastructure dan Accounts Payable) | Pre-setup #9, `Oscar Pranata`; email tidak tertulis di Pre-setup TC, disediakan tim FE | `Spectra.env.FA_GM_PASSWORD` |

  Nama env `FA_MURGR_UPD_PASSWORD` dan `FA_GM_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup #21 (Finance & Accounting, IT Infrastructure, Branch Surabaya, dan lainnya), Responsibilities #25 (approver permohonan Waiting for Approval) dan Transaction Role #39 sebagai pola data. Target aksi tulis memakai pengguna milik spec (S-06).
- Pengguna milik spec (seed API di hook `before`, dihapus di hook `after`; dirujuk lewat `Fixture.fa-settings-user.<kunci>`, fixture belum ada dan disediakan tim FE). Email `<alias>+{runId}-038@qwertysystem.net` dengan alias huruf kecil:
  - `Hana Kusuma {runId}-038`: Active, Pending Activation (TC-FA-SU-132).
  - `Eka Wulandari {runId}-038`: Active, Transaction Role Approver, approver permohonan Waiting for Approval (TC-FA-SU-133).
  - `Gita Permata {runId}-038`: Active, Home Group Finance & Accounting (dalam scope Sinta Dewi; TC-FA-SU-131).
  - `Indra Wijaya {runId}-038`: Active, Home Group IT Infrastructure (dalam scope Oscar Pranata, di luar scope Sinta Dewi; TC-FA-SU-131).
- Kemampuan teknis: seed penugasan Transaction Role Approver dan permohonan Waiting for Approval untuk pengguna milik spec disediakan tim FE/BE; jalur navigasi picker approver dan antrean Waiting for Approval di modul transaksi disediakan tim FE (lihat Temuan untuk QA).
- State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-132: Pengguna Pending Activation dapat di-Activate dan di-Deactivate

1. Ketik Search `Hana Kusuma {runId}-038`, tekan Enter
2. Verifikasi sakelar Active baris `Hana Kusuma {runId}-038` Enabled
3. Klik sakelar Active pada baris `Hana Kusuma {runId}-038`
4. Klik `[Deactivate]`
5. Verifikasi sakelar Active baris `Hana Kusuma {runId}-038` berpindah ke OFF
6. Verifikasi badge `Pending Activation` tetap tampil
7. Klik sakelar Active pada baris `Hana Kusuma {runId}-038`
8. Klik `[Activate]`
9. Verifikasi sakelar Active baris `Hana Kusuma {runId}-038` berpindah ke ON
10. Verifikasi Activation Status `Hana Kusuma {runId}-038` tetap `Pending Activation`

### TC-FA-SU-133: Pengguna nonaktif disaring dari resolusi approver tanpa menghapus baris penugasan

11. Ganti isi kotak search dengan `Eka Wulandari {runId}-038`, tekan Enter
12. Klik sakelar Active pada baris `Eka Wulandari {runId}-038`
13. Klik `[Deactivate]`
14. Tunggu aksi selesai (sakelar Active baris `Eka Wulandari {runId}-038` berstatus OFF)
15. Buka picker approver pada modul transaksi
16. Verifikasi picker approver pada modul transaksi termuat dengan daftar approver eligible tampil
17. Verifikasi `Eka Wulandari {runId}-038` tidak muncul sebagai approver eligible pada picker transaksi FAMS
18. Buka antrean Waiting for Approval pada modul transaksi
19. Verifikasi antrean Waiting for Approval pada modul transaksi termuat dengan daftar permohonan tampil
20. Verifikasi `Eka Wulandari {runId}-038` tidak muncul sebagai approver eligible pada antrean Waiting for Approval
21. Buka Settings > User lewat sidebar, ganti isi kotak search dengan `Eka Wulandari {runId}-038`, tekan Enter
22. Buka Detail `Eka Wulandari {runId}-038` > Tab Role > Sub-tab Transaction Role
23. Verifikasi baris penugasan Transaction Role Approver `Eka Wulandari {runId}-038` tetap ada
24. Klik sakelar Active di header Detail
25. Klik `[Activate]`
26. Tunggu aksi selesai (header Detail `Eka Wulandari {runId}-038` berstatus Active)
27. Buka picker approver pada modul transaksi
28. Verifikasi `Eka Wulandari {runId}-038` muncul kembali sebagai approver eligible

### TC-FA-SU-131: Aktor Manage user & role Group dan Group Manager mengubah status dalam scope

29. Ganti akun: Logout
30. Login sebagai Sinta Dewi (Manage user & role Group (Update)) dengan `Spectra.env.FA_MURGR_UPD_PASSWORD`
31. Buka Settings > User lewat sidebar
32. Ketik Search `Gita Permata {runId}-038`, tekan Enter
33. Verifikasi sakelar Active baris `Gita Permata {runId}-038` Enabled
34. Klik sakelar Active pada baris `Gita Permata {runId}-038`
35. Klik `[Deactivate]`
36. Verifikasi toast "Success, user has been deactivated." tampil
37. Ganti isi kotak search dengan `Indra Wijaya {runId}-038`, tekan Enter
38. Verifikasi baris `Indra Wijaya {runId}-038` (di luar scope) tidak tampil dengan empty state `No results found`
39. Ganti akun: Logout
40. Login sebagai Oscar Pranata (Group Manager IT Infrastructure) dengan `Spectra.env.FA_GM_PASSWORD`
41. Buka Settings > User lewat sidebar
42. Ketik Search `Indra Wijaya {runId}-038`, tekan Enter
43. Verifikasi sakelar Active baris `Indra Wijaya {runId}-038` Enabled
44. Klik sakelar Active pada baris `Indra Wijaya {runId}-038`
45. Klik `[Deactivate]`
46. Verifikasi toast "Success, user has been deactivated." tampil

## Notes

- Alasan di atas 35 langkah (46): spec dengan Step ganti akun eksplisit (menurut bagian 3 konvensi, bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras); setiap blok memakai pengguna milik spec sendiri. Aksi dengan akun Total Control ditulis lebih dulu, blok ganti akun di akhir.
- Langkah penghubung (S-03): langkah 1, 32, dan 42 (Search untuk menemukan baris target, R-16), langkah 11 dan 37 (mengganti isi kotak search yang masih berisi nama sebelumnya, bagian 8b butir 9), langkah 21 (kembali ke Settings > User sesudah langkah 15 sampai 20 di modul transaksi dan mengganti isi kotak search, R-16, bagian 8b butir 9), langkah 29, 30, 39, dan 40 (ganti akun, S-07), langkah 31 dan 41 (membuka Settings > User lewat sidebar sesudah ganti akun, S-14), langkah 14 dan 26 (menunggu aksi `[Deactivate]` atau `[Activate]` selesai sebelum berpindah ke picker transaksi, bagian 8b butir 8).
- Pembagian TC lintas spec: TC-FA-SU-125 sampai TC-FA-SU-130 (permintaan paksa ditolak server) ada di spec kelas a.
- Temuan untuk QA:
  - TC-FA-SU-131 Expected butir b ("sakelar pengguna di luar scope tidak tampil karena barisnya disembunyikan") tidak menyebut pengguna mana; spec memakai `Indra Wijaya {runId}-038` yang berada di IT Infrastructure (di luar scope Finance & Accounting) dan asersi memakai empty state `No results found` hasil Search dengan toast sukses langkah 36 sebagai anchor. Expected butir a diasersi untuk Sinta Dewi dan Oscar Pranata; TC langkah 3 tidak merinci Expected untuk Oscar Pranata sehingga toast dan sakelar Enabled diasersi ulang untuk Indra Wijaya.
  - Email Sinta Dewi dan Oscar Pranata tidak tertulis di Pre-setup TC; nama env password diusulkan.
  - TC-FA-SU-133 menyebut "picker approver pada modul transaksi" dan "antrean Waiting for Approval" tanpa jalur navigasi atau modul transaksi mana; jalur navigasinya ditentukan di Page Object. Langkah TC hanya memberi langkah untuk picker; langkah 18 sampai 20 dibuat untuk antrean karena Expected butir a menyebutnya. Asersi absence approver pada picker (langkah 17) dan antrean (langkah 20) masing-masing didahului Verifikasi bahwa picker atau antrean termuat (langkah 16 dan 19) sebagai anchor positif (bagian 8b butir 2).
  - Post Condition TC-FA-SU-131 butir a dan b, TC-FA-SU-132 butir b, dan TC-FA-SU-133 butir a tidak punya langkah observasi di TC (status aktif, entri log pada tiga surface) dan tidak diasersi, kecuali yang sudah menjadi Expected padanan.
  - Teks toast Deactivate pada TC-FA-SU-131 dikutip persis dari TC itu; Activation Status `Pending Activation` pada TC-FA-SU-132 diasersi sebagai badge dan nilai Activation Status.
  - Target TC (Gita Permata, Hana Kusuma, Eka Wulandari, Indra Wijaya) adalah pengguna Pre-setup bersama; spec memakai pengguna milik spec dengan suffix (S-06).
