---
id: TC-FA-SU-E2E-068-detail-group-assignment-dan-group-dihapus-di-settings-groups
title: "Detail Group Assignment dan Group Dihapus di Settings Groups"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-224
  - TC-FA-SU-225
coverage:
  web: automated
---

# Detail Group Assignment dan Group Dihapus di Settings Groups

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal: Read Only Citra Lestari (Pre-setup #3) `readOnly_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_RO_PASSWORD`. Login di hook `before` spec ini (akun pertama spec); halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun kedua (ganti akun eksplisit): Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21), penugasan (Pre-setup #23), dan Transaction Role (Pre-setup #39).
- Pengguna target: Ahmad Dahlan (Default User), Lina Marlina (Total Control), Citra Lestari (Read Only, akun sendiri) untuk TC-FA-SU-224; Rudi Hartono dan Doni Prasetyo (Home Group Logistics Warehouse) dengan Group Role, Group Manager, dan Transaction Role pada Logistics Warehouse untuk TC-FA-SU-225, disediakan lewat seed API karena Pre-setup #23 dan #39 tidak memuat penugasan itu untuk keduanya (lihat Temuan untuk QA); 
- Data uji: grup Logistics Warehouse yang dihapus di Settings > Groups.
- Kemampuan teknis: seed API untuk menyetel dan memulihkan penugasan Rudi Hartono dan Doni Prasetyo serta grup Logistics Warehouse; pembacaan jumlah entri Tab Changelog, jumlah notifikasi in-app, dan Role Count sebelum aksi sebagai baseline (disediakan tim FE/BE, bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: grup Logistics Warehouse (dihapus) beserta penugasannya dan Home Group Rudi Hartono serta Doni Prasetyo; dipulihkan ke Pre-setup #21, #23, dan #39 lewat seed API pada langkah penghubung dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-224: Detail Group Assignment tersedia untuk semua aktor yang bisa membuka Tab Role termasuk target terkunci

1. Buka Detail Ahmad Dahlan > Tab Role > Sub-tab Group Role
2. Verifikasi `[Detail]` Enabled bagi Read Only pada target Default User
3. Buka Detail Lina Marlina > Tab Role > Sub-tab Group Role
4. Verifikasi `[Detail]` tetap tersedia (Enabled) pada target Total Control
5. Buka Detail Citra Lestari > Tab Role > Sub-tab Group Role
6. Verifikasi `[Detail]` tetap tersedia (Enabled) pada target Read Only dan akun sendiri
7. Klik `[Detail]` pada satu baris Group Role Citra Lestari
8. Verifikasi Detail Group Assignment terbuka
9. Tutup Detail Group Assignment

### TC-FA-SU-225: Group dihapus di Settings > Groups: Group Role, Group Manager, dan Transaction Role pada grup itu terhapus, role tanpa grup, dan Home Group kosong silent

10. Ganti akun: logout lalu login sebagai Total Control Lina Marlina
11. Setel Group Role, Group Manager, dan Transaction Role pada Logistics Warehouse untuk Rudi Hartono dan Doni Prasetyo lewat seed API
12. Catat jumlah entri Object `Group Role`, `Transaction Role`, dan `Group Manager (Group Deleted)` serta entri Home Group Rudi Hartono dan Doni Prasetyo pada Tab Changelog, jumlah notifikasi in-app keduanya, dan Role Count keduanya sebagai baseline
13. Hapus grup Logistics Warehouse di Settings > Groups lewat sesi API hingga grup terhapus
14. Buka Detail Rudi Hartono > Tab Role
15. Verifikasi penugasan Group Role pada Logistics Warehouse hilang dan role yang kehilangan seluruh grup tampil Group `—` dan tidak aktif
16. Buka Detail Doni Prasetyo > Tab Role
17. Verifikasi penugasan Group Role pada Logistics Warehouse hilang dan role yang kehilangan seluruh grup tampil Group `—` dan tidak aktif
18. Buka User List
19. Verifikasi Role Count Rudi Hartono dan Doni Prasetyo tidak lagi menghitung role yang kehilangan seluruh grup
20. Buka Tab Changelog dan Search `Hartono`, tekan Enter, lalu muat ulang sampai entri tampil
21. Verifikasi entri `Remove` per assignment yang terlepas (Object `Group Role`, `Transaction Role`, dan `Group Manager (Group Deleted)`) bertambah dibanding baseline pada Tab Changelog
22. Verifikasi Modified By entri itu adalah admin yang menghapus grup (`Lina M`)
23. Verifikasi grup Logistics Warehouse tidak lagi tampil di Sidebar Group Tree (penghapusan grup tidak diblokir)
24. Verifikasi Home Group Rudi Hartono dan Doni Prasetyo kosong di User List
25. Verifikasi jumlah entri Home Group Rudi Hartono dan Doni Prasetyo pada Tab Changelog sama dengan baseline (tanpa entri log)
26. Verifikasi jumlah notifikasi in-app Rudi Hartono dan Doni Prasetyo sama dengan baseline (tanpa notifikasi)
27. Pulihkan grup Logistics Warehouse, penugasan, dan Home Group Rudi Hartono serta Doni Prasetyo lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 9, 11, 12 dan 27. Baseline mengikuti S-12; pemulihan lewat seed API memulihkan Pre-setup #21, #23, dan #39 (S-06, S-09).
- Langkah pola baca-log: langkah 20 sampai 22. Search `Hartono` pada langkah itu adalah langkah penghubung untuk menemukan baris target (R-16). Langkah pertama TC-FA-SU-225 mengganti akun ke Total Control (ganti akun eksplisit, S-07).
- TC-FA-SU-226 dan 227 (Group Role Wawan Setiawan: sinkronisasi dan tanpa switch) ada di spec 088.
- TC-FA-SU-225: klausa "tanpa entri log dan tanpa notifikasi" pada Home Group ditulis sebagai asersi jumlah dengan baseline (bagian 3 prinsip 13 butir g, S-12).
- Jumlah langkah 27: 24 langkah di luar blok baca-log berpola (3 langkah, tidak dihitung pada smell bagian 3 prinsip 13), seluruhnya satu kelas harness.
- Temuan untuk QA:
  - TC-FA-SU-224 butir a menyebut `[Detail]` Enabled bagi Read Only, Manage user & role, dan Group Manager, tetapi langkah hanya memakai Read Only; spec hanya mengasersi Read Only. TC juga tidak menyebut isi Detail Group Assignment; spec mengasersi bahwa Detail terbuka.
  - TC-FA-SU-225 memakai Rudi Hartono dan Doni Prasetyo sebagai pemilik Group Role, Group Manager, dan Transaction Role pada Logistics Warehouse, tetapi Pre-setup #23 dan #39 tidak memuat penugasan itu untuk keduanya; spec menyetelnya lewat seed API. TC-FA-SU-225 tidak menyebut Expected Role Count baseline dan notifikasi; spec memakai baseline.
