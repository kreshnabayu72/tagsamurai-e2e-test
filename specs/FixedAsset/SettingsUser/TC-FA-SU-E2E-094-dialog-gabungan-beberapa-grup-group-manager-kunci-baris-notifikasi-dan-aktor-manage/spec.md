---
id: TC-FA-SU-E2E-094-dialog-gabungan-beberapa-grup-group-manager-kunci-baris-notifikasi-dan-aktor-manage
title: "Dialog Gabungan Beberapa Grup Group Manager, Kunci Baris, dan Notifikasi Auto-Revert"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-297
  - TC-FA-SU-298
  - TC-FA-SU-319
coverage:
  web: automated
---

# Dialog Gabungan Beberapa Grup Group Manager, Kunci Baris, dan Notifikasi Auto-Revert

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23). Pengguna target: Oscar Pranata (Pre-setup #9; Group Manager IT Infrastructure dan Accounts Payable; memegang baris pola Group Manager pada kedua grup: Group Role katalog selain Manage user & role dengan CRUD penuh sesuai kolom yang berlaku dan Transaction Role Asset Admin serta Approver pada setiap Jenis Transaksi), akun `Spectra.env.FA_GM_PASSWORD`; email akun ini tidak tertulis di Pre-setup TC (disediakan tim FE). Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): entri `Edit Home Group` dan `Auto-Revert` pada Tab Changelog pengguna target, Tab System Log aktor, dan Activity Log, serta entri `Remove (via Group Manager)` pada modal Changelog User > Group Role, modal Changelog User > Transaction Role, Tab Changelog pengguna target, Tab System Log aktor, dan Activity Log, dibaca sebelum dan sesudah aksi. Audit trail bersifat permanen sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut.
- Kemampuan baca notifikasi in-app per pengguna (disediakan tim FE/BE): jumlah notifikasi Auto-Revert Oscar Pranata per grup dan per judul dibaca sebelum aksi.
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan penugasan peran pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC. Pemulihan dijalankan sebagai langkah penghubung dan di hook `after` (cadangan). Oscar Pranata dipulihkan sesudah tiap aksi (langkah 17, 29) dan di hook `after`. Efek pada Pre-setup: Home Group dan status Group Manager Oscar Pranata berubah (Last Updated, Modified By), entri log permanen `Edit Home Group` dan `Auto-Revert` bertambah, dan Oscar Pranata menerima notifikasi in-app. Spec berakhir pada akun Oscar Pranata; hook `after` memulihkan sesi ke akun default suite.

## Test Steps

1. Catat jumlah entri `Edit Home Group` dan `Auto-Revert` pada Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log, jumlah entri `Remove (via Group Manager)` pada modal Changelog User > Group Role, modal Changelog User > Transaction Role, Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log, serta jumlah notifikasi Auto-Revert Oscar Pranata untuk IT Infrastructure dan Accounts Payable sebagai baseline

### TC-FA-SU-297: Satu dialog D-10 untuk lebih dari satu grup

2. Klik ⋯ pada baris Oscar Pranata lalu klik `Edit Home Group`
3. Klik node Branch Surabaya lalu klik `[Select]`
4. Verifikasi satu dialog Title `Role Outside Constraint Will Be Revoked` memuat bullet `• Manage group — Accounts Payable`, `• Manage group — IT Infrastructure`, `• Group Manager — Accounts Payable`, dan `• Group Manager — IT Infrastructure`, kalimat `Setting the Home Group constraint to Branch Surabaya for Oscar Pranata will revoke these assignments outside this group.` dan `Are you sure you want to revoke them?`
5. Klik `[Revoke]`
6. Tunggu aksi selesai: permintaan `[Revoke]` pada langkah 5 selesai dan dialog tertutup
7. Buka Detail Oscar Pranata > Tab Changelog
8. Verifikasi satu entri `Auto-Revert` per grup (IT Infrastructure dan Accounts Payable) tercatat
9. Baca jumlah entri `Auto-Revert` dan `Remove (via Group Manager)` pada Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log
10. Verifikasi jumlah entri `Auto-Revert` bertambah 2 (satu per grup) dibanding baseline pada Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log
11. Verifikasi jumlah entri `Remove (via Group Manager)` sama dengan baseline pada Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log (entri itu hanya tampil di kedua modal Changelog User)
12. Buka Detail Oscar Pranata > Tab Role > Sub-tab Group Role, buka modal Changelog User > Group Role, muat ulang sampai entri tampil, lalu baca jumlah entri `Remove (via Group Manager)`
13. Verifikasi jumlah entri `Remove (via Group Manager)` pada modal Changelog User > Group Role bertambah dibanding baseline, satu entri untuk tiap baris pola Group Role Group Manager kedua grup (IT Infrastructure dan Accounts Payable) yang dicabut
14. Tutup modal dengan `[✕]`, klik Sub-tab Transaction Role, buka modal Changelog User > Transaction Role, muat ulang sampai entri tampil, lalu baca jumlah entri `Remove (via Group Manager)`
15. Verifikasi jumlah entri `Remove (via Group Manager)` pada modal Changelog User > Transaction Role bertambah dibanding baseline, satu entri untuk tiap baris pola Transaction Role Group Manager kedua grup (IT Infrastructure dan Accounts Payable) yang dicabut
16. Tutup modal dengan `[✕]`
17. Pulihkan Home Group dan status Group Manager Oscar Pranata ke kondisi Pre-setup lewat seed API
18. Catat jumlah entri `Remove (via Group Manager)` pada modal Changelog User > Group Role dan modal Changelog User > Transaction Role Oscar Pranata sebagai baseline TC-FA-SU-298

### TC-FA-SU-298: Kunci baris Group Manager tidak menghalangi pencabutan

19. Kembali ke User List lalu klik ⋯ pada baris Oscar Pranata dan klik `Edit Home Group`
20. Klik node Accounts Payable lalu klik `[Select]`
21. Klik `[Revoke]`
22. Verifikasi pencabutan Group Role penopang Group Manager tersimpan setelah dialog D-10 dikonfirmasi
23. Verifikasi Total Control dapat mencabut Group Role penopang Group Manager walau baris itu terkunci bagi aktor Manage user & role
24. Buka Detail Oscar Pranata > Tab Role > Sub-tab Group Role, buka modal Changelog User > Group Role, muat ulang sampai entri tampil, lalu baca jumlah entri `Remove (via Group Manager)`
25. Verifikasi baris pola Group Manager yang terkunci (S-16) ikut dicabut karena status Group Manager terlepas: jumlah entri `Remove (via Group Manager)` pada modal Changelog User > Group Role bertambah dibanding baseline TC-FA-SU-298
26. Tutup modal dengan `[✕]`, klik Sub-tab Transaction Role, buka modal Changelog User > Transaction Role, muat ulang sampai entri tampil, lalu baca jumlah entri `Remove (via Group Manager)`
27. Verifikasi baris pola Group Manager yang terkunci (S-16) ikut dicabut karena status Group Manager terlepas: jumlah entri `Remove (via Group Manager)` pada modal Changelog User > Transaction Role bertambah dibanding baseline TC-FA-SU-298
28. Tutup modal dengan `[✕]`
29. Pulihkan Home Group dan status Group Manager Oscar Pranata ke kondisi Pre-setup lewat seed API

### TC-FA-SU-319: Notifikasi Auto-Revert akibat Edit Home Group

30. Klik ⋯ pada baris Oscar Pranata lalu klik `Edit Home Group`
31. Klik node Accounts Payable lalu klik `[Select]`
32. Klik `[Revoke]`
33. Tunggu aksi selesai: permintaan `[Revoke]` pada langkah 32 selesai dan dialog tertutup
34. Ganti akun: Logout lalu login sebagai Oscar Pranata
35. Buka panel notifikasi
36. Verifikasi notifikasi in-app view-only per grup yang terlepas bertambah dibanding baseline: IT Infrastructure 3 dan Accounts Payable 1 notifikasi baru (IT Infrastructure satu dari tiap TC-FA-SU-297, TC-FA-SU-298, dan TC-FA-SU-319; Accounts Payable satu dari TC-FA-SU-297 saja)
37. Verifikasi notifikasi terbaru memiliki Title `You are no longer Group Manager for IT Infrastructure`
38. Verifikasi Body `Your Group Manager status for IT Infrastructure was automatically removed after Lina Marlina set your Home Group on [Date].` dengan nama aktor Lina Marlina dan [Date] tanggal aksi
39. Verifikasi notifikasi tidak dapat ditindaklanjuti (tanpa tombol aksi)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Notifikasi Oscar Pranata diamati sekali pada akhir spec karena satu kali ganti akun cukup; selisih kumulatif terhadap baseline langkah 1: IT Infrastructure 3 (TC-FA-SU-297, TC-FA-SU-298, TC-FA-SU-319) dan Accounts Payable 1 (TC-FA-SU-297). Rincian: TC-FA-SU-297 memilih node Branch Surabaya sehingga status Group Manager terlepas di kedua grup (IT Infrastructure +1, Accounts Payable +1); TC-FA-SU-298 dan TC-FA-SU-319 memilih node Accounts Payable sebagai Home Group sehingga hanya IT Infrastructure yang terlepas (+1 masing-masing), bukan Accounts Payable. Copy Title dan Body diasersi pada notifikasi terbaru (hasil TC-FA-SU-319).
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 (baseline), kembali ke User List, dan langkah 17 serta 29 (pemulihan), langkah 6 (menunggu aksi `[Revoke]` selesai sebelum membuka Tab Changelog), langkah 33 (menunggu aksi `[Revoke]` selesai sebelum ganti akun, bagian 8b butir 8), serta langkah 12, 14, 16, 24, 26, dan 28 (membuka dan menutup modal Changelog User per Sub-tab, sekaligus membaca jumlah entri `Remove (via Group Manager)` lewat kemampuan baca tim FE/BE; langkah 18 adalah baseline TC-FA-SU-298). Pelaku kedua tidak dipakai; pergantian akun ke Oscar Pranata hanya untuk membaca notifikasi (berurutan, bukan sesi paralel).
- Expected b TC-FA-SU-297 ("hanya di modal Changelog User") ditulis sebagai selisih positif pada kedua modal (langkah 13 dan 15) dan selisih nol pada tiga surface lain (langkah 11), dengan Verifikasi entri `Auto-Revert` (langkah 10) sebagai anchor positif (bagian 8b butir 2); tidak ada spec absence yang memuat aksi nyata TC ini sehingga Verifikasi berbaseline ada di spec ini (S-05, S-12). Expected b TC-FA-SU-298 diamati pada kedua modal yang sama dengan baseline sendiri (langkah 18) karena baseline dicatat ulang per TC (S-12).
- Alasan di atas sekitar 35 langkah: ketiga TC satu kelas (dialog D-10 Edit Home Group atas satu pengguna target dengan pemulihan seed di antaranya), tiap TC berdiri sendiri dan kegagalan satu TC tidak membuat TC lain kehilangan makna; langkah baca modal Changelog User berpola (buka modal, baca jumlah, `Verifikasi` selisih, tutup) dan dipakai dua kali sehingga tidak dihitung menurut bagian 3 prinsip 13 (Smell).
- Temuan untuk QA (S-15): (1) TC-FA-SU-319 berlabel `Manual Only — (d) dua sesi paralel`; spec menjalankannya berurutan (aksi lalu ganti akun) karena asersi hanya pada hasil. (2) TC-FA-SU-297 Expected b menyebut "notifikasi tetap satu per grup" tanpa langkah pengamatan; diamati bersama TC-FA-SU-319. (3) Post Condition TC-FA-SU-298 (Home Group berubah, entri `Auto-Revert` per grup, notifikasi terkirim) tanpa langkah observasi tidak diasersi kecuali yang tercakup Expected. (4) Expected b TC-FA-SU-298 ("baris pola GM yang terkunci (S-16) ikut dicabut") tidak menyebut baris atau jumlahnya; spec mengasersi selisih jumlah entri `Remove (via Group Manager)` pada kedua modal tanpa angka absolut.
