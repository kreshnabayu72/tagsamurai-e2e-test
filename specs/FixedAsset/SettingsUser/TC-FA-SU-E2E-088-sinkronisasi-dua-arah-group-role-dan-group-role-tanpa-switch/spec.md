---
id: TC-FA-SU-E2E-088-sinkronisasi-dua-arah-group-role-dan-group-role-tanpa-switch
title: "Sinkronisasi Dua Arah Group Role dan Group Role Tanpa Switch"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-226
  - TC-FA-SU-227
coverage:
  web: automated
---

# Sinkronisasi Dua Arah Group Role dan Group Role Tanpa Switch

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan penugasan (Pre-setup #23).
- Pengguna target: Wawan Setiawan; Group Role `Manage files` pada IT Infrastructure dan Branch Surabaya, `Manage asset & TAG` dan `Manage user & role` tanpa grup; Role Count awal 7 roles (Pre-setup #43).
- Data uji: grup General Affairs ditambahkan dan Branch Surabaya dihapus pada `Manage files` (TC-FA-SU-226); satu grup disimpan pada `Manage asset & TAG` dan flag aktif dikirim untuk `Manage user & role` (TC-FA-SU-227).
- Kemampuan teknis: seed API untuk memulihkan penugasan Group Role Wawan Setiawan (disediakan tim FE/BE); klien HTTP dengan token sesi aktor untuk permintaan langsung (TC-FA-SU-227, disediakan tim FE/BE); pembacaan state data role Wawan Setiawan lewat fixture BE; pembacaan Role Count sebelum aksi sebagai baseline (disediakan tim FE/BE, bagian 8b butir 10).
- State global yang diubah: penugasan Group Role `Manage files` dan `Manage asset & TAG` milik Wawan Setiawan; dipulihkan ke Pre-setup #23 lewat seed API pada langkah penghubung dan di hook `after`.
- Target tanpa Home Group (Pre-setup #50, `FaUserNoHG`; Catatan TC: TC penugasan Tab Role Section 3d, 3e, 4c, 8, dan 9 yang memilih node bebas dijalankan pada varian tanpa Home Group, FI-32), diterapkan per target: Home Group Wawan Setiawan (Finance & Accounting pada Pre-setup #43) dikosongkan lewat seed API di hook `before` supaya node General Affairs (langkah 2) dan grup yang disimpan pada Manage asset & TAG (langkah 14) tidak Disabled oleh gate Home Group constraint; Home Group Wawan Setiawan dipulihkan ke Finance & Accounting di hook `after`. Seed per target disediakan tim FE/BE.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-226: Sinkronisasi dua arah Group Role: perubahan di Detail User tampil di Role & Permission dan sebaliknya

1. Ketik Search `Wawan Setiawan`, tekan Enter
2. Tambah General Affairs ke Manage files Wawan Setiawan di Detail User
3. Tunggu aksi selesai: penambahan General Affairs pada langkah 2 tersimpan dan popup tertutup
4. Buka Settings > Role & Permission > Tab System > Detail Role Manage files
5. Verifikasi penugasan General Affairs pada Manage files Wawan Setiawan tampil di Detail Role Manage files
6. Hapus Branch Surabaya dari penugasan Wawan Setiawan pada Detail Role Manage files
7. Tunggu aksi selesai: penghapusan Branch Surabaya pada langkah 6 selesai
8. Buka Settings > User lewat sidebar, ganti isi kotak search dengan `Wawan Setiawan`, tekan Enter
9. Buka Detail Wawan Setiawan > Tab Role > Sub-tab Group Role
10. Verifikasi perubahan dari Role & Permission (Branch Surabaya dihapus) tampil di Sub-tab Group Role Wawan Setiawan tanpa reload manual
11. Pulihkan penugasan Manage files Wawan Setiawan ke Pre-setup #23 lewat seed API

### TC-FA-SU-227: Group Role tanpa switch: aktif hanya saat punya minimal satu grup dan server tidak menerima flag aktif

12. Kembali ke User List, ganti isi kotak search dengan `Wawan Setiawan`, tekan Enter
13. Catat Role Count Wawan Setiawan di User List sebagai baseline
14. Buka Detail Wawan Setiawan > Tab Role > Sub-tab Group Role lalu simpan satu grup pada Manage asset & TAG lewat popup Assign Group Role
15. Tunggu aksi selesai: penyimpanan grup pada langkah 14 selesai dan popup tertutup
16. Buka User List
17. Ganti isi kotak search dengan `Wawan Setiawan`, tekan Enter
18. Verifikasi role Manage asset & TAG aktif dan Role Count Wawan Setiawan bertambah dibanding baseline
19. Kirim permintaan langsung ke API memakai klien HTTP dengan flag aktif untuk role Manage user & role Wawan Setiawan yang tanpa grup hingga respons diterima
20. Verifikasi (state data lewat fixture BE) role Manage user & role Wawan Setiawan tetap tidak aktif
21. Pulihkan penugasan Manage asset & TAG Wawan Setiawan ke Pre-setup #23 lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 11, 13 dan 21; langkah 3, 7, dan 15 menunggu aksi tulis selesai sebelum berpindah surface (bagian 8b butir 8); langkah 1, 8, 12, dan 17 adalah Search nama Wawan Setiawan sebelum membuka Detail atau membaca baris Role Count, karena User List memuat 3 halaman (R-16, bagian 8b butir 9 dan 13). Baseline mengikuti S-12; pemulihan lewat seed API memulihkan Pre-setup #23 (S-09).
- `P-5` butir b: TC-FA-SU-227 (kelas a, permintaan langsung dengan flag aktif) adalah satu TC objek-uji ringan kelas a tanpa harness eksternal; permintaan langsung hanya mengasersi state data (bagian 8b butir 1).
- TC-FA-SU-224 dan 225 ada di spec 068.
- Pre-setup #50 diterapkan hanya pada Wawan Setiawan (bukan seluruh 25 pengguna): pemilih Group Role dan Role Transaksi men-Disabled node di luar Home Group constraint target (FI-32, tooltip S-45) dan permintaan langsung di luar constraint ditolak `422`, sedangkan TC ini memilih General Affairs (langkah 2) dan grup yang disimpan pada Manage asset & TAG (langkah 14); Home Group Wawan Setiawan dipulihkan di hook `after`. Mohon dikonfirmasi bila #50 harus diterapkan penuh.
- Temuan untuk QA:
  - TC-FA-SU-226 langkah 4 menyebut Sub-tab Group Role "Eka" sedangkan Expected b menyebut Wawan, dan langkah 3 menghapus Branch Surabaya sedangkan Expected b menyebut "penugasan yang ditambah dari Role & Permission"; spec memakai Wawan Setiawan dan mengasersi penghapusan Branch Surabaya.
  - TC-FA-SU-227 tidak menyebut role "lain tanpa grup" yang dikirimi flag aktif; spec memakai Manage user & role.
  - Post Condition TC-FA-SU-226 (penugasan sama pada Settings > User dan Role & Permission) dan TC-FA-SU-227 (state role) dicakup oleh Expected di atas.
