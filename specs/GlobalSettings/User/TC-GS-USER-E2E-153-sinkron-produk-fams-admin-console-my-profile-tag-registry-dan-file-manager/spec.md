---
id: TC-GS-USER-E2E-153-sinkron-produk-fams-admin-console-my-profile-tag-registry-dan-file-manager
title: "Sinkron ke Fixed Asset, Admin Console, My Profile, All Tags, dan File Manager"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-958
  - TC-GS-USER-959
  - TC-GS-USER-960
  - TC-GS-USER-961
  - TC-GS-USER-962
  - TC-GS-USER-963
  - TC-GS-USER-964
coverage:
  web: automated
---

# Sinkron ke Fixed Asset, Admin Console, My Profile, All Tags, dan File Manager

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun yang diuji (spec memakai tiga akun dan berganti akun secara eksplisit):

  | Urutan | Peran dalam spec | Email | Environment variable password |
  |---|---|---|---|
  | 1 | Total Control Client A (Siti Nurhaliza), Tabel Data Uji Pre-setup No. 2 | `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `GS_TC_PASSWORD` |
  | 2 | Dewi Lestari (user uji milik spec, hanya untuk TC-GS-USER-962) | `dewilestari+{runId}-153@qwertysystem.net` | `USER_PASSWORD` |
  | 3 | Total Control entitas Principal (disediakan tim FE, tidak ada di Tabel Pre-setup) | akun disediakan tim FE | `GS_PRINCIPAL_TC_PASSWORD` |

  Login akun 1 di hook `before` lalu membuka Global Settings > User > User List (sub-tab Login User); hook `after` mengembalikan sesi ke akun default suite (akun 1). Akun 1 memiliki akses ke Fixed Asset (Borrow dan Settings > User), Global Settings > All Tags, dan File Manager; Tabel Pre-setup tidak menyebutnya, disediakan tim FE. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `USER_PASSWORD`, `GS_PRINCIPAL_TC_PASSWORD`.
- Data Pre-setup dibaca saja: Division `Finance` (No. 23) untuk Create user; TAG `TAG-USR-0001` (No. 25, user, aktif, bebas) dipasangkan ke `Wahyu Hidayat {runId}-153` pada TC-GS-USER-963 lalu dilepas oleh hook `after` lewat API (efek: riwayat pairing TAG `TAG-USR-0001` bertambah; status kembali bebas; S-06).
- Data Dinamis (suffix per run dan nomor spec), di-seed lewat API di hook `before` (nilai field wajib lain user mengikuti fixture `fixtures/user.json` yang belum ada, disediakan tim FE):
  - Entitas Client A, oleh sesi API akun 1:
    - Login User `Dewi Lestari {runId}-153`, email `dewilestari+{runId}-153@qwertysystem.net`, Activated, Active, Access `Fixed Asset` dan `Global Settings`, tanpa foto, password `Spectra.env.USER_PASSWORD` (setara Dewi Lestari Tabel Pre-setup No. 12; target TC-GS-USER-958, 962, 964).
    - Login User `Wahyu Hidayat {runId}-153`, email `wahyuhidayat+{runId}-153@qwertysystem.net`, Activated, Active, Access `Fixed Asset` (pembanding aktif pada pilihan peminjam dan approver TC-GS-USER-958; target pairing TAG TC-GS-USER-963 karena Dewi sudah Deactivate di TC-GS-USER-958 saat blok itu berjalan).
    - Transaksi Borrow lama atas nama `Dewi Lestari {runId}-153` (kemampuan seeding transaksi Fixed Asset lewat API, disediakan tim FE/BE).
  - Entitas Principal, oleh sesi API akun 3: Login User `Rizal Akbar {runId}-153` (email `rizalakbar+{runId}-153@qwertysystem.net`, Staff, Access `Admin Console`, Active; target TC-GS-USER-960) dan Login User `Rizal Pratama {runId}-153` (email `rizalpratama+{runId}-153@qwertysystem.net`, Staff, Access `Admin Console`, Active, toggle per-produk Admin Console ON; target TC-GS-USER-961).
  - Berkas foto uji `Fixture.user.photoUji` (gambar valid; fixture belum ada, disediakan tim FE).
  - Input uji: email baru Dewi `dewilestari.baru+{runId}-153@qwertysystem.net` (TC-GS-USER-962).
  - Dibuat spec lewat UI: Login User `Hana Pertiwi {runId}-153` (First Name `Hana`, Last Name `Pertiwi {runId}-153`, Division `Finance`, email `hanapertiwi+{runId}-153@qwertysystem.net`, Access `Fixed Asset`) pada TC-GS-USER-959.
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak memberi cara): simulasi scan `TAG-USR-0001` pada RFID reader untuk pairing dari Detail (TC-GS-USER-963; precondition "RFID reader tersambung"); polling sinkron asinkron Admin Console (muat ulang dan Search berulang dengan batas waktu tunggu); seeding transaksi Borrow dan seeding user pada entitas Principal lewat sesi API akun 3.
- Cleanup (hook `after`, tidak berasumsi seeding atau langkah berhasil penuh): lepas pairing `TAG-USR-0001` bila terpasang; hapus lewat API transaksi Borrow seed, Login User `dewilestari+{runId}-153@qwertysystem.net` (atau email baru `dewilestari.baru+{runId}-153@qwertysystem.net`), `wahyuhidayat+{runId}-153@qwertysystem.net`, `hanapertiwi+{runId}-153@qwertysystem.net` pada Client A, dan `rizalakbar+{runId}-153@qwertysystem.net`, `rizalpratama+{runId}-153@qwertysystem.net` pada Principal; hapus berkas foto uji milik Dewi bila tersisa; kembalikan sesi ke akun 1.
- Tidak ada state global yang diubah.

## Test Steps

### TC-GS-USER-959: Create user dengan Access Fixed Asset muncul di Fixed Asset > Settings > User sebagai User Basic

1. Buka Global Settings > User > Tab User List
2. Klik `[+ User]`, isi First Name `Hana`, Last Name `Pertiwi {runId}-153`, Division `Finance`, Email `hanapertiwi+{runId}-153@qwertysystem.net`, centang Access `Fixed Asset`, klik `[Submit]`
3. Tunggu aksi selesai
4. Buka Fixed Asset > Settings > User
5. Klik icon Search, ketik `Hana Pertiwi {runId}-153`, tekan Enter
6. Verifikasi `Hana Pertiwi {runId}-153` tampil di daftar user Fixed Asset
7. Verifikasi role `Hana Pertiwi {runId}-153` adalah `User Basic`

### TC-GS-USER-964: Ganti foto memperbarui avatar di User List dan File Manager

8. Buka Global Settings > User > Tab User List, klik icon Search, ketik `Dewi Lestari {runId}-153`, tekan Enter
9. Klik Name `Dewi Lestari {runId}-153`
10. Hover avatar di Detail, pilih opsi upload foto, pilih berkas `Fixture.user.photoUji`
11. Tunggu aksi selesai
12. Kembali ke User List dengan klik Back
13. Verifikasi avatar baris `Dewi Lestari {runId}-153` menampilkan foto baru (gambar, bukan inisial)
14. Buka Global Settings > File Manager, klik icon Search, ketik nama berkas `Fixture.user.photoUji`, tekan Enter
15. Verifikasi File Manager memuat file baru milik `Dewi Lestari {runId}-153`

### TC-GS-USER-962: Banner Pending Email Change tampil read-only di My Profile target

16. Buka Global Settings > User > Tab User List, klik icon Search, ketik `Dewi Lestari {runId}-153`, tekan Enter
17. Klik `⋯` pada baris `Dewi Lestari {runId}-153` > Edit, ubah Email ke `dewilestari.baru+{runId}-153@qwertysystem.net`, klik `[Save]`
18. Tunggu aksi selesai
19. Ganti akun: logout, lalu login sebagai Dewi Lestari (`dewilestari+{runId}-153@qwertysystem.net`) dengan `Spectra.env.USER_PASSWORD`, lalu buka Global Settings > My Profile
20. Verifikasi banner Pending Email Change tampil di My Profile
21. Verifikasi banner Pending Email Change tidak memuat tombol `Resend`
22. Verifikasi banner Pending Email Change tidak memuat tombol `Cancel`
23. Ganti akun: logout, lalu login sebagai Total Control Client A (`totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`) dengan `Spectra.env.GS_TC_PASSWORD`

### TC-GS-USER-958: Deactivate user menghilangkan user dari pilihan peminjam dan approver FAMS

24. Buka Global Settings > User > Tab User List, klik icon Search, ketik `Dewi Lestari {runId}-153`, tekan Enter
25. Matikan switch Active baris `Dewi Lestari {runId}-153`, klik `[Deactivate]` pada dialog
26. Tunggu aksi selesai
27. Buka Fixed Asset > Borrow > Create
28. Isi pencarian pilihan peminjam dengan `{runId}-153`
29. Verifikasi `Wahyu Hidayat {runId}-153` tersedia sebagai pilihan peminjam
30. Verifikasi `Dewi Lestari {runId}-153` tidak tersedia sebagai pilihan peminjam
31. Isi pencarian pilihan approver dengan `{runId}-153`
32. Verifikasi `Wahyu Hidayat {runId}-153` tersedia sebagai pilihan approver
33. Verifikasi `Dewi Lestari {runId}-153` tidak tersedia sebagai pilihan approver
34. Buka Fixed Asset > Borrow, klik icon Search, ketik `Dewi Lestari {runId}-153`, tekan Enter
35. Verifikasi transaksi lama `Dewi Lestari {runId}-153` tetap tampil

### TC-GS-USER-960 dan TC-GS-USER-961: Sinkron ke Admin Console (entitas Principal)

36. Ganti akun: logout, lalu login sebagai Total Control Principal (akun disediakan tim FE) dengan `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`, lalu buka Global Settings > User > Tab User List
37. Klik icon Search, ketik `Rizal Akbar {runId}-153`, tekan Enter
38. Klik `⋯` pada baris `Rizal Akbar {runId}-153` > Edit, hapus centang Access `Admin Console`, klik `[Save]`
39. Tunggu aksi selesai
40. Ganti isi kotak search dengan `Rizal Pratama {runId}-153`, tekan Enter
41. Matikan switch Active baris `Rizal Pratama {runId}-153`, klik `[Deactivate]` pada dialog
42. Tunggu aksi selesai
43. Buka Admin Console > Settings > User, klik icon Search, ketik `{runId}-153`, tekan Enter
44. Tunggu proses sinkron selesai: muat ulang Admin Console > Settings > User dan ulangi Search `{runId}-153` sampai baris `Rizal Akbar {runId}-153` tidak lagi tampil (batas waktu tunggu disediakan tim FE)
45. Verifikasi `Rizal Pratama {runId}-153` tampil di daftar user Admin Console
46. Verifikasi toggle per-produk baris `Rizal Pratama {runId}-153` tampil
47. Verifikasi toggle per-produk baris `Rizal Pratama {runId}-153` disabled
48. Verifikasi toggle per-produk baris `Rizal Pratama {runId}-153` berada pada posisi terakhir (ON)
49. Verifikasi `Rizal Akbar {runId}-153` tidak tampil di daftar user Admin Console

### TC-GS-USER-963: Pair TAG dari Detail terlihat di All Tags

50. Ganti akun: logout, lalu login sebagai Total Control Client A (`totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`) dengan `Spectra.env.GS_TC_PASSWORD`
51. Buka Global Settings > User > Tab User List, klik icon Search, ketik `Wahyu Hidayat {runId}-153`, tekan Enter
52. Klik Name `Wahyu Hidayat {runId}-153`
53. Klik aksi Pair TAG di Detail, lalu simulasikan scan `TAG-USR-0001` pada RFID reader
54. Tunggu aksi selesai
55. Buka Global Settings > All Tags, klik icon Search, ketik `TAG-USR-0001`, tekan Enter
56. Verifikasi status `TAG-USR-0001` terpasang ke `Wahyu Hidayat {runId}-153`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Sinkron ke modul lain (Fixed Asset, Admin Console, My Profile, All Tags, File Manager); satu TC (TC-GS-USER-963) memakai simulator scan RFID sebagai kelas harness hardware dan diletakkan di akhir spec.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-GS-USER-959 (membuat user) dan TC-GS-USER-964 (ganti foto) lebih dulu, TC-GS-USER-962 (butuh Dewi tetap Active untuk login) sebelum TC-GS-USER-958 yang menonaktifkan Dewi, dan TC-GS-USER-960 dan 961 membutuhkan ganti akun ke entitas Principal; tiga akun dipakai berurutan dengan ganti akun eksplisit (langkah 19, 23, 36, 50). TC-GS-USER-963 (pairing TAG lewat simulator scan RFID, langkah 53) dipindah ke akhir spec (langkah 50 sampai 56) supaya kegagalan simulator tidak menutupi blok lain (konvensi bagian 3, pemisah nyata hardware berisiko). Pemisahan blok simulator scan (konvensi bagian 3, pemisah nyata hardware berisiko): objek uji TC-GS-USER-963 adalah sinkron Pair TAG ke All Tags, bukan perangkat scan; blok non-hardware lebih dulu, langkah 50 memulihkan akun Client A, dan target pairing diganti ke `Wahyu Hidayat {runId}-153` karena Dewi sudah di-Deactivate pada langkah 25. TC-GS-USER-960 dan 961 diamati pada satu kunjungan Admin Console > Settings > User (langkah 43 sampai 49): aksi keduanya dijalankan lebih dulu pada user berbeda (`Rizal Akbar`, `Rizal Pratama`), dan `Rizal Pratama` yang tampil menjadi anchor positif bagi asersi `Rizal Akbar` tidak tampil.
- Spec melewati sekitar 35 langkah (56 langkah). Alasan: tujuh TC memakai satu tema (sinkron aksi User ke modul lain) dan sebagian besar langkah adalah aksi pada layar User ditambah pembacaan di modul tujuan dengan Search dan `Verifikasi` per klausa (S-01) yang tidak dapat digabung; state Dewi dibangun berurutan antar blok (foto, email pending, lalu Deactivate), sehingga memecahnya mengulang seeding user, pairing TAG, dan ganti akun.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 4, 8, 14, 16, 24, 27, 34, 43, 51, 55 (membuka layar dan Search); langkah 3, 11, 18, 26, 39, 42, 54 (menunggu aksi selesai); langkah 12 (Back ke User List); langkah 19, 23, 36, 50 (ganti akun); langkah 28 dan 31 (pencarian pada pilihan peminjam dan approver); langkah 44 (menunggu proses sinkron asinkron). Langkah 44 berhenti saat `Rizal Akbar` tidak lagi tampil atau saat batas waktu tunggu habis; kondisi berhenti itu bukan asersi, asersinya langkah 49.
- Asersi absence (langkah 30, 33, 49) didahului `Verifikasi` pembanding pada surface yang sama (langkah 29, 32, 45; bagian 8b butir 2).
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-USER-958: Expected b ("Transaksi lama Dewi tetap tampil") tidak menyebut transaksi, lokasi daftar, dan cara membuatnya; spec memakai transaksi Borrow seed dan Search di Fixed Asset > Borrow. TC juga tidak menyebut cara mencari di "pilihan peminjam/approver"; spec memakai pencarian di masing-masing pilihan.
  - TC-GS-USER-959: TC tidak menyebut field wajib selain Access; spec memakai First Name, Last Name, Division, dan Email.
  - TC-GS-USER-960: TC tidak menyebut apakah Remove Access memunculkan dialog konfirmasi untuk `Admin Console`; spec tidak memuat dialog itu (user seed tanpa aset atau approval) dan memakai penantian polling untuk "proses sinkron" tanpa durasi.
  - TC-GS-USER-961: "posisi terakhir" tidak menyebut nilainya; spec men-seed toggle per-produk ON dan mengasersi ON.
  - TC-GS-USER-962: TC tidak menyebut teks banner di My Profile (NC-10 hanya mendefinisikan teks pada Identity Detail); spec mengasersi keberadaan banner dan ketiadaan tombol `Resend` dan `Cancel`. TC tidak menyebut kapan sesi Dewi dibuat; spec login sebagai Dewi dengan email lama (email baru masih pending).
  - TC-GS-USER-963: kolom Automation bernilai Manual Only dan precondition "RFID reader tersambung"; spec memasukkannya (bagian 2 konvensi) dengan simulasi scan yang disediakan tim FE. TC tidak menyebut aksi Pair dari Detail (label tombol).
  - TC-GS-USER-964: TC tidak menyebut berkas foto, apakah ada langkah simpan sesudah upload, dan kolom File Manager yang menunjukkan kepemilikan Dewi; spec mengasersi file dengan nama berkas uji milik Dewi.
  - TC-GS-USER-958 sampai 964: akun Total Control tidak tercatat memiliki akses Fixed Asset, All Tags, dan File Manager di Tabel Pre-setup; disediakan tim FE.
