---
id: TC-FA-SU-E2E-061-hapus-grup-ubah-checkbox-crud-save-campuran-dan-save-tanpa-perubahan
title: "Hapus Grup, Ubah Checkbox CRUD, Save Campuran, dan Save Tanpa Perubahan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-200
  - TC-FA-SU-201
  - TC-FA-SU-202
  - TC-FA-SU-203
coverage:
  web: automated
---

# Hapus Grup, Ubah Checkbox CRUD, Save Campuran, dan Save Tanpa Perubahan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan penugasan (Pre-setup #23).
- Pengguna target: Wawan Setiawan tanpa Home Group (Pre-setup #50 `FaUserNoHG`, varian `FaUserMain` dengan Home Group dikosongkan); Group Role `Manage files` pada IT Infrastructure (Read dan Delete tercentang) dan Branch Surabaya (Read tercentang, Delete tidak tercentang).
- Data uji: grup yang dihapus Branch Surabaya (TC-FA-SU-200); permission Delete pada Branch Surabaya diubah dari Inactive menjadi Active (TC-FA-SU-201); grup yang ditambahkan General Affairs (TC-FA-SU-202).
- Kemampuan teknis: seed API untuk memulihkan penugasan Group Role `Manage files` Wawan Setiawan ke Pre-setup #23 (disediakan tim FE/BE); pembacaan jumlah entri tiga permukaan log (Tab Changelog target, Tab System Log aktor, Activity Log) sebelum aksi sebagai baseline (disediakan tim FE/BE, bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: penugasan Group Role `Manage files` milik Wawan Setiawan; dipulihkan ke Pre-setup #23 lewat seed API pada langkah penghubung antar TC dan di hook `after`. Last Updated Wawan Setiawan berubah dan tidak dipulihkan.
- Target tanpa Home Group (Pre-setup #50, `FaUserNoHG`; Catatan TC: TC penugasan Tab Role yang memilih node bebas dijalankan pada varian tanpa Home Group, FI-32), diterapkan per target: Home Group Wawan Setiawan (Finance & Accounting pada Pre-setup #43) dikosongkan lewat seed API di hook `before` supaya node di luar constraint tidak Disabled oleh gate Home Group; Home Group Wawan Setiawan dipulihkan ke Finance & Accounting di hook `after`. Seed per target disediakan tim FE/BE.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-200: Hapus grup dari popup menunggu Save: perubahan lokal sampai Save lalu toast updated dan log Remove

1. Catat jumlah entri `Remove` Object `Group Role` Wawan Setiawan pada Tab Changelog sebagai baseline
2. Ketik Search `Wawan Setiawan`, tekan Enter
3. Buka Detail Wawan Setiawan > Tab Role > Sub-tab Group Role
4. Buka popup Assign Group Role Manage files
5. Klik ikon hapus pada Branch Surabaya
6. Verifikasi baris Branch Surabaya hilang dari tabel popup
7. Klik `[✕]` pada popup
8. Verifikasi dialog `Unsaved Changes`
9. Klik `[Leave]`
10. Buka ulang popup Assign Group Role Manage files
11. Verifikasi baris Branch Surabaya masih tampil di tabel popup (tidak ada perubahan tersimpan sebelum `[Save]`)
12. Klik ikon hapus pada Branch Surabaya lalu klik `[Save]`
13. Verifikasi toast "Success, group role has been updated."
14. Verifikasi Branch Surabaya hilang dari kolom Group baris Manage files
15. Buka Tab Changelog, Search `Wawan Setiawan`, tekan Enter, lalu muat ulang sampai entri tampil
16. Verifikasi entri `Remove` / Object `Group Role` / Field `Manage files — Branch Surabaya` / Old Value `Assigned` / New Value `—` bertambah satu dibanding baseline pada Tab Changelog

### TC-FA-SU-201: Ubah checkbox CRUD di popup lalu Save: toast updated dan log Edit per permission dan grup

17. Pulihkan penugasan Manage files Wawan Setiawan ke Pre-setup #23 lewat seed API
18. Catat jumlah entri `Edit` Object `Group Role` Wawan Setiawan pada Tab Changelog sebagai baseline
19. Kembali ke User List, ganti isi kotak search dengan `Wawan Setiawan`, tekan Enter
20. Buka ulang Detail Wawan Setiawan > Tab Role > Sub-tab Group Role lalu buka popup Assign Group Role Manage files
21. Centang Delete pada Branch Surabaya
22. Verifikasi Delete Branch Surabaya tercentang pada popup tanpa toast tersimpan (perubahan hanya lokal sampai `[Save]`)
23. Klik `[Save]`
24. Verifikasi toast "Success, group role has been updated."
25. Buka Tab Changelog, Search `Wawan Setiawan`, tekan Enter, lalu muat ulang sampai entri tampil
26. Verifikasi entri `Edit` / Object `Group Role` / Field `Manage files — Branch Surabaya — Delete` / Old Value `Inactive` / New Value `Active` bertambah satu dibanding baseline pada Tab Changelog

### TC-FA-SU-202: Perubahan campuran di satu Save: tambah dan ubah CRUD menghasilkan toast assigned dan satu entri log per perubahan

27. Pulihkan penugasan Manage files Wawan Setiawan ke Pre-setup #23 lewat seed API
28. Catat jumlah entri `Assign` dan `Edit` Object `Group Role` Wawan Setiawan pada Tab Changelog sebagai baseline
29. Kembali ke User List, ganti isi kotak search dengan `Wawan Setiawan`, tekan Enter
30. Buka ulang Detail Wawan Setiawan > Tab Role > Sub-tab Group Role lalu buka popup Assign Group Role Manage files
31. Klik `[+ Assign Group]`, centang General Affairs, klik `[Select]`
32. Centang Delete pada Branch Surabaya
33. Klik `[Save]`
34. Verifikasi toast "Success, group role has been assigned."
35. Buka Tab Changelog, Search `Wawan Setiawan`, tekan Enter, lalu muat ulang sampai entri tampil
36. Verifikasi satu entri `Assign` untuk grup baru General Affairs bertambah dibanding baseline pada Tab Changelog
37. Verifikasi satu entri `Edit` untuk permission Delete Branch Surabaya bertambah dibanding baseline pada Tab Changelog
38. Verifikasi tidak ada entri berlebih: total entri baru pada Tab Changelog tepat dua

### TC-FA-SU-203: Save popup Assign Group Role tanpa perubahan: toast No-Op dan tanpa entri log

39. Pulihkan penugasan Manage files Wawan Setiawan ke Pre-setup #23 lewat seed API
40. Catat jumlah seluruh entri Object `Group Role` Wawan Setiawan pada tiga permukaan log sebagai baseline
41. Kembali ke User List, ganti isi kotak search dengan `Wawan Setiawan`, tekan Enter
42. Buka ulang Detail Wawan Setiawan > Tab Role > Sub-tab Group Role lalu buka popup Assign Group Role Manage files
43. Verifikasi `[Save]` Enabled sejak popup dibuka
44. Klik `[Save]` tanpa mengubah apa pun
45. Verifikasi popup menutup
46. Verifikasi toast "No changes to save."
47. Buka Tab Changelog, Search `Wawan Setiawan`, tekan Enter
48. Verifikasi jumlah entri Object `Group Role` Wawan Setiawan pada Tab Changelog sama dengan baseline
49. Buka Tab System Log aktor dan Search `Wawan Setiawan`, tekan Enter
50. Verifikasi jumlah entri Object `Group Role` Wawan Setiawan pada Tab System Log sama dengan baseline
51. Buka Activity Log
52. Verifikasi jumlah entri Object `Group Role` Wawan Setiawan pada Activity Log sama dengan baseline

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 17, 18, 27, 28, 39 dan 40. Pemulihan lewat seed API memulihkan Pre-setup #23 sebelum TC berikutnya mengandalkannya (S-09); baseline log mengikuti S-12; penutupan popup dirty pada TC-FA-SU-200 mengikuti S-08.
- Langkah penghubung Search (R-16, S-03; bagian 8b butir 9 dan 13): langkah 2, 19, 29, dan 41 mencari baris target dengan nama persis sebelum aksi pada baris itu, tanpa `Verifikasi`; tabel User List dapat memuat lebih dari satu halaman (25 pengguna, 3 halaman).
- Langkah pola baca-log: langkah 15, 16, 25, 26, 35 sampai 38 dan 47 sampai 52. Search `Wawan Setiawan` pada langkah itu adalah langkah penghubung untuk menemukan baris target (R-16).
- TC-FA-SU-203: klausa "tidak ada entri log baru" pada Save no-op ditulis sebagai asersi jumlah dengan baseline di spec fungsional (bagian 3 prinsip 13 butir g, S-12); toast "No changes to save." menjadi anchor positif (bagian 8b butir 2).
- Jumlah langkah 52, di atas smell 35 langkah karena blok baca-log berpola (14 langkah: buka surface, cari entri, `Verifikasi` kolom log; tidak dihitung pada smell, bagian 3 prinsip 13) dan 4 langkah Search penghubung per baris target (R-16); di luar blok baca-log 38 langkah, seluruhnya satu topik (Group Role Manage files Wawan Setiawan) dan satu kelas harness.
- Home Group: spec ini menambah General Affairs lewat popup Select Group (langkah 31) pada Wawan Setiawan; pada Pre-setup #43 Home Group Wawan adalah Finance & Accounting sehingga gate Home Group (FI-32) men-Disabled node di luar constraint. Sesuai Catatan TC (TC penugasan Section 3d dijalankan pada varian tanpa Home Group), spec memakai Pre-setup #50; Precondition TC-FA-SU-200 sampai 202 tidak memuat #50 dan perlu disesuaikan.
- Temuan untuk QA:
  - TC-FA-SU-200 butir a ("tanpa request") tidak punya cara observasi di UI; spec mengasersi baris hilang di popup dan tidak tersimpan setelah popup dibuka ulang.
  - TC-FA-SU-201 butir a ("hanya mengubah state lokal sampai Save") tidak punya cara observasi langsung; spec mengasersi tidak ada toast tersimpan sebelum `[Save]`.
  - Post Condition TC-FA-SU-200 sampai 202 butir Settings > Role & Permission (dua arah) tidak punya langkah observasi di TC dan tidak diasersi.
