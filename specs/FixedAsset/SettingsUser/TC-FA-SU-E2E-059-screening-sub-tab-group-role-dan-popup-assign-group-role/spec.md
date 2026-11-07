---
id: TC-FA-SU-E2E-059-screening-sub-tab-group-role-dan-popup-assign-group-role
title: "Screening Sub-tab Group Role dan Popup Assign Group Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-192
  - TC-FA-SU-193
  - TC-FA-SU-194
  - TC-FA-SU-195
coverage:
  web: automated
---

# Screening Sub-tab Group Role dan Popup Assign Group Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20, 25 pengguna) dengan pohon grup (Pre-setup #21) dan penugasan (Pre-setup #23).
- Pengguna target: Wawan Setiawan (Group Role `Manage files` pada IT Infrastructure dan Branch Surabaya, `Manage asset & TAG` tanpa grup; Pre-setup #23) dan Nanda Pratama (Pre-setup #11: Group Role `Manage user & role` pada Finance & Accounting, Global Role `Manage global user & role` OFF).
- Data uji: Wawan Setiawan pada `Manage files`: IT Infrastructure dengan Read dan Delete tercentang, Branch Surabaya dengan Read tercentang dan Delete tidak tercentang (TC-FA-SU-194).
- Kemampuan teknis: seed API untuk memulihkan switch Global Role `Manage global user & role` Nanda Pratama ke OFF (disediakan tim FE/BE, dipakai di `after` dan sebagai langkah penghubung).
- State global yang diubah: switch Global Role `Manage global user & role` Nanda Pratama (TC-FA-SU-193); dipulihkan ke OFF pada langkah penghubung sesudah asersi dan di hook `after`.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-192: Screening Sub-tab Group Role: kolom, baris katalog tetap, dan aksi per baris

1. Ketik Search `Wawan Setiawan`, tekan Enter
2. Buka Detail Wawan Setiawan > Tab Role > Sub-tab Group Role
3. Verifikasi kolom `Role Name | Group | Actions` dengan header kolom Actions (⋯)
4. Verifikasi TableTools hanya berisi ikon Changelog
5. Verifikasi seluruh baris katalog Group Role tampil berurut Role Name A-Z termasuk role tanpa grup (Group `—`)
6. Verifikasi tiap baris punya aksi `[Detail]` dan `[Assign Group]` Enabled, termasuk baris dengan 0 grup
7. Verifikasi tidak ada switch aktif/nonaktif pada baris Group Role
8. Verifikasi role aktif bila dan hanya bila punya ≥1 grup

### TC-FA-SU-193: Baris Group Role Manage user & role tidak dirender selama Global Role Manage global user & role aktif

9. Kembali ke User List, ganti isi kotak search dengan `Nanda Pratama`, tekan Enter
10. Buka Detail Nanda Pratama > Tab Role > Sub-tab Global Role lalu nyalakan Global Role `Manage global user & role`
11. Klik Sub-tab Group Role Nanda Pratama
12. Verifikasi baris katalog Group Role lain tetap tampil
13. Verifikasi baris Group Role `Manage user & role` tidak tampil sehingga `[Detail]` dan `[Assign Group]`-nya tidak ada
14. Matikan kembali Global Role `Manage global user & role` Nanda Pratama lewat seed API (pemulihan)
15. Tunggu aksi selesai: permintaan seed API pemulihan selesai

### TC-FA-SU-194: Screening popup Assign Group Role: header, toolbar, tabel dinamis per role, dan footer

16. Kembali ke User List, ganti isi kotak search dengan `Wawan Setiawan`, tekan Enter
17. Buka Detail Wawan Setiawan > Tab Role > Sub-tab Group Role
18. Klik `[Assign Group]` pada baris Manage files
19. Verifikasi header `Assign Group Role — Manage files` dengan close `[✕]`
20. Verifikasi toolbar berisi kolom pencarian dengan placeholder `Search groups...` dan tombol `[+ Assign Group]`
21. Verifikasi tabel berkolom Group | Read | Delete | Remove (kolom sesuai kapabilitas role: Manage files hanya Read dan Delete)
22. Verifikasi baris IT Infrastructure: Read tercentang Disabled, Delete tercentang, dan ikon hapus tampil
23. Verifikasi baris Branch Surabaya: Read tercentang Disabled dan Delete tidak tercentang
24. Verifikasi footer `[Clear Field]` (Text, Primary) di kiri dan `[Save]` (Success) di kanan
25. Verifikasi kolom C/R/U/D tidak masuk Column Visibility (selalu permanen)
26. Klik `[✕]` untuk menutup popup

### TC-FA-SU-195: Empty state popup Assign Group Role saat tabel 0 baris

27. Klik `[Assign Group]` pada baris Manage asset & TAG yang belum punya grup
28. Verifikasi popup `Assign Group Role` terbuka kosong dengan ilustrasi, Title `No groups assigned yet`, dan Description `Click [+ Assign Group] to add a group.`
29. Klik `[✕]` untuk menutup popup tanpa Save
30. Verifikasi kolom Group baris Manage asset & TAG tetap `—` dan role tetap tidak aktif

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 14, 15, dan 26. Langkah 15 menunggu pemulihan seed API selesai sebelum berpindah surface (bagian 8b butir 8). Langkah pemulihan Global Role Nanda Pratama memulihkan state yang diubah TC-FA-SU-193; penutupan popup tanpa perubahan mengakhiri TC-FA-SU-194 sebelum popup lain dibuka.
- Langkah penghubung Search (R-16, S-03; bagian 8b butir 9 dan 13): langkah 1, 9, dan 16 mencari baris target dengan nama persis sebelum aksi pada baris itu, tanpa `Verifikasi`; tabel User List dapat memuat lebih dari satu halaman (25 pengguna, 3 halaman).
- Pada TC-FA-SU-193, `Verifikasi` baris katalog lain tampil ditulis sebelum `Verifikasi` absence baris `Manage user & role` (anchor positif, bagian 8b butir 2); urutan butir a dan b Expected TC ditukar.
- Temuan untuk QA:
  - TC-FA-SU-194 butir d (kolom C/R/U/D tidak masuk Column Visibility) tidak menyebut cara membuka Column Visibility pada popup; spec mengasersi sesuai teks TC.
  - TC-FA-SU-192 butir d ("role aktif bila dan hanya bila punya ≥1 grup") tidak menyebut elemen yang menandai role aktif; spec mengasersi sesuai teks TC.
  - TC-FA-SU-193 menyalakan Global Role lewat UI Sub-tab Global Role tetapi tidak menyebut tab asalnya; spec memakai Tab Role > Sub-tab Global Role.
