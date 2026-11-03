---
id: TC-FA-SU-E2E-060-pilih-node-select-group-cancel-popup-dan-tambah-grup-ke-group-role
title: "Pilih Node Select Group, Cancel Popup, dan Tambah Grup ke Group Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-196
  - TC-FA-SU-197
  - TC-FA-SU-198
  - TC-FA-SU-199
coverage:
  web: automated
---

# Pilih Node Select Group, Cancel Popup, dan Tambah Grup ke Group Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21: Finance & Accounting dengan anak Accounts Payable, IT Infrastructure, Branch Surabaya, General Affairs, Logistics Warehouse, Region Jawa dengan anak Jakarta Selatan Distribution Center) dan penugasan (Pre-setup #23).
- Pengguna target: Wawan Setiawan; Group Role `Manage files` pada IT Infrastructure dan Branch Surabaya; `Manage asset & TAG` tanpa grup; Role Count awal 7 roles (Pre-setup #43).
- Data uji: node Finance & Accounting dan General Affairs sebagai grup yang ditambahkan; role `Manage asset & TAG` yang diberi seluruh grup tersedia lewat seed API (TC-FA-SU-197).
- Kemampuan teknis: seed API untuk menugaskan dan melepas penugasan Group Role Wawan Setiawan (disediakan tim FE/BE); pembacaan jumlah entri tiga permukaan log (Tab Changelog target, Tab System Log aktor, Activity Log) sebelum aksi sebagai baseline (disediakan tim FE/BE, bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: penugasan Group Role `Manage files` dan `Manage asset & TAG` milik Wawan Setiawan; dipulihkan ke Pre-setup #23 lewat seed API pada langkah penghubung dan di hook `after`.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-196: Pilih node di Select Group tidak men-cascade ke descendant

1. Buka Detail Wawan Setiawan > Tab Role > Sub-tab Group Role
2. Klik `[Assign Group]` pada baris Manage files lalu klik `[+ Assign Group]` untuk membuka popup Select Group
3. Centang node Finance & Accounting
4. Verifikasi node Accounts Payable tidak tercentang
5. Klik `[Select]`
6. Verifikasi hanya Finance & Accounting yang ditambahkan ke tabel popup, dengan Read tercentang terkunci dan kapabilitas lain tidak tercentang
7. Klik `[✕]` pada popup Assign Group Role
8. Verifikasi dialog `Unsaved Changes`
9. Klik `[Leave]`

### TC-FA-SU-197: Semua node Disabled: pohon tetap tampil dan tombol Select Disabled

10. Assign role Manage asset & TAG Wawan Setiawan ke seluruh grup tersedia lewat seed API hingga penugasan tersimpan
11. Buka ulang Detail Wawan Setiawan > Tab Role > Sub-tab Group Role
12. Klik `[Assign Group]` pada baris Manage asset & TAG lalu klik `[+ Assign Group]` untuk membuka popup Select Group
13. Verifikasi pohon grup tetap tampil dan seluruh node Disabled karena sudah ter-assign
14. Verifikasi `[Select]` Disabled
15. Klik `[Cancel]` pada popup Select Group lalu klik `[✕]` pada popup Assign Group Role
16. Lepas penugasan Manage asset & TAG Wawan Setiawan lewat seed API hingga role tanpa grup

### TC-FA-SU-198: Cancel popup Select Group kembali ke popup Assign Group Role tanpa menambahkan

17. Buka ulang Detail Wawan Setiawan > Tab Role > Sub-tab Group Role
18. Klik `[Assign Group]` pada baris Manage files lalu klik `[+ Assign Group]` untuk membuka popup Select Group
19. Centang node General Affairs
20. Klik `[Cancel]`
21. Verifikasi popup Select Group tertutup dan popup Assign Group Role Manage files tetap terbuka dengan isi utuh (IT Infrastructure dan Branch Surabaya)
22. Klik `[+ Assign Group]` untuk membuka popup Select Group lagi
23. Verifikasi node General Affairs tidak tercentang
24. Klik `[Cancel]` pada popup Select Group lalu klik `[✕]` pada popup Assign Group Role

### TC-FA-SU-199: Tambah grup ke Group Role lalu Save: toast assigned, tabel refresh, log Assign per grup, dan Role Count bertambah

25. Catat Role Count Wawan Setiawan di User List dan jumlah entri `Assign` Object `Group Role` pada Tab Changelog target, Tab System Log aktor, dan Activity Log sebagai baseline
26. Buka Detail Wawan Setiawan > Tab Role > Sub-tab Group Role
27. Klik `[Assign Group]` pada baris Manage files
28. Klik `[+ Assign Group]`, centang General Affairs, klik `[Select]`
29. Verifikasi baris General Affairs ditambahkan dengan Read tercentang Disabled dan Delete tidak tercentang
30. Klik `[Save]`
31. Verifikasi popup menutup
32. Verifikasi toast "Success, group role has been assigned."
33. Verifikasi kolom Group baris Manage files menampilkan badge General Affairs bersama IT Infrastructure dan Branch Surabaya
34. Buka Tab Changelog, Search `Wawan Setiawan`, tekan Enter, lalu muat ulang sampai entri tampil
35. Verifikasi entri `Assign` / Object `Group Role` / Field `Manage files — General Affairs` / Old Value `—` / New Value `Assigned` bertambah satu dibanding baseline pada Tab Changelog
36. Buka Tab System Log aktor dan Search `Wawan Setiawan`, tekan Enter
37. Verifikasi entri `Assign` / Object `Group Role` / Field `Manage files — General Affairs` / Old Value `—` / New Value `Assigned` bertambah satu dibanding baseline pada Tab System Log
38. Buka Activity Log
39. Verifikasi entri `Assign` / Object `Group Role` / Field `Manage files — General Affairs` / Old Value `—` / New Value `Assigned` bertambah satu dibanding baseline pada Activity Log
40. Buka User List
41. Verifikasi Role Count Wawan Setiawan bertambah satu dibanding baseline
42. Lepas General Affairs dari Manage files Wawan Setiawan lewat seed API (pemulihan)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 7 sampai 9, 15, 16, 24, 25 dan 42. Penutupan popup dirty mengikuti S-08 (`✕`, dialog `Unsaved Changes`, `[Leave]`); lepas penugasan lewat seed API memulihkan Pre-setup #23 sebelum TC berikutnya mengandalkannya (S-09).
- Langkah pola baca-log: langkah 34 sampai 39. Search `Wawan Setiawan` pada langkah itu adalah langkah penghubung untuk menemukan baris target (R-16).
- Jumlah langkah 42, di atas smell 35 langkah hanya karena blok baca-log berpola (6 langkah: buka surface, cari entri, `Verifikasi` kolom log) yang tidak dihitung pada smell (bagian 3 prinsip 13); di luar blok itu 36 langkah, seluruhnya satu topik dan satu kelas harness.
- Temuan untuk QA:
  - TC-FA-SU-196 tidak menyebut role yang dipakai membuka popup Select Group dan menulis "C/U/D tidak tercentang" padahal popup Assign Group Role Manage files hanya berkolom Read dan Delete (TC-FA-SU-194); spec memakai role Manage files dan mengasersi kapabilitas selain Read tidak tercentang.
  - TC-FA-SU-199 butir d mengharapkan Role Count Wawan Setiawan bertambah satu setelah menambah grup ke Manage files, padahal role itu sudah punya grup (aktif) sehingga jumlah role aktif tidak berubah; spec mengikuti teks TC dan butir ini berpotensi gagal.
  - TC-FA-SU-199 butir c menyebut "satu kali per grup di tiga permukaan log"; spec mengasersi selisih satu entri terhadap baseline untuk satu grup yang ditambahkan.
  - Post Condition TC-FA-SU-199 butir d (Settings > Role & Permission > Detail Role Group Role menampilkan perubahan dua arah) tidak punya langkah observasi di TC dan tidak diasersi.
