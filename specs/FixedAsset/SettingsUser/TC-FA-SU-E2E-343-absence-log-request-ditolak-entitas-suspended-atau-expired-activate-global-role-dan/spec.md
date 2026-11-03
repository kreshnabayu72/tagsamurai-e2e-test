---
id: TC-FA-SU-E2E-343-absence-log-request-ditolak-entitas-suspended-atau-expired-activate-global-role-dan
title: "Absence Log Request Ditolak: Entitas Suspended atau Expired: Activate, Global Role, dan Group Role"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-976
  - TC-FA-SU-977
  - TC-FA-SU-978
  - TC-FA-SU-979
coverage:
  web: automated
---

# Absence Log Request Ditolak: Entitas Suspended atau Expired: Activate, Global Role, dan Group Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Transaction Role (#39). Status Suspended dan Expired setara Client Pre-setup #34 `FaUserSuspended` dan #35 `FaUserExpired`; spec ini mengubah status Client `FaUserMain` (akun aktor Pre-setup #1 berada di Client itu) lewat Principal Automation (#12). Target: Doni Prasetyo, Gita Permata, Wawan Setiawan.
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE.
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri pada Tab Changelog target, Tab System Log aktor, dan Activity Log dibaca sebelum permintaan (baseline, S-12) dan sesudah permintaan; audit trail bersifat permanen sehingga asersi memakai selisih terhadap baseline, bukan angka absolut. Log yang menunggu eventual dibaca ulang (muat ulang surface) sampai batas tunggu 2 menit.
- Principal Automation (Pre-setup #12): akun atau kemampuan "disediakan tim FE" untuk mengubah status Client lewat sesi API (R-20, bukan konteks kedua). Token sesi API aktor Total Control tetap berlaku sesudah status Client berubah (disediakan tim FE/BE).
- State global dan pemulihan: status Client `FaUserMain` diubah menjadi Suspended lalu Expired dan dipulihkan menjadi Aktif pada langkah 35 serta di hook `after` (cadangan). Pre-setup lain tidak diubah karena setiap permintaan ditolak server. Suite berjalan serial (`parallel: false`).

## Test Steps

### Client `FaUserMain` berstatus Suspended: TC-FA-SU-976, 977, 978, 979

1. Principal Automation mengubah status Client `FaUserMain` menjadi Suspended hingga perubahan status tersimpan
2. [TC-FA-SU-976] Catat jumlah entri log pada Tab Changelog Doni Prasetyo, Tab System Log aktor, dan Activity Log sebagai baseline
3. [TC-FA-SU-976] Kirim permintaan langsung ke API Activate Doni Prasetyo memakai klien HTTP dengan token sesi Lina Marlina
4. Verifikasi anchor: [TC-FA-SU-976] server menolak permintaan
5. Verifikasi [TC-FA-SU-976] tidak ada entri log baru pada Tab Changelog Doni Prasetyo, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline
6. [TC-FA-SU-977] Catat jumlah entri log pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline
7. [TC-FA-SU-977] Kirim permintaan langsung ke API nyalakan switch Manage asset ID configuration untuk Gita Permata memakai klien HTTP dengan token sesi Lina Marlina
8. Verifikasi anchor: [TC-FA-SU-977] server menolak permintaan
9. Verifikasi [TC-FA-SU-977] tidak ada entri log baru pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline
10. [TC-FA-SU-978] Catat jumlah entri log pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline
11. [TC-FA-SU-978] Kirim permintaan langsung ke API centang Update Manage accounting untuk Gita Permata memakai klien HTTP dengan token sesi Lina Marlina
12. Verifikasi anchor: [TC-FA-SU-978] server menolak permintaan
13. Verifikasi [TC-FA-SU-978] tidak ada entri log baru pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline
14. [TC-FA-SU-979] Catat jumlah entri log pada Tab Changelog Wawan Setiawan, Tab System Log aktor, dan Activity Log sebagai baseline
15. [TC-FA-SU-979] Kirim permintaan langsung ke API tambah grup General Affairs ke Manage files milik Wawan Setiawan memakai klien HTTP dengan token sesi Lina Marlina
16. Verifikasi anchor: [TC-FA-SU-979] server menolak permintaan
17. Verifikasi [TC-FA-SU-979] tidak ada entri log baru pada Tab Changelog Wawan Setiawan, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

### Client `FaUserMain` berstatus Expired: TC-FA-SU-976, 977, 978, 979

18. Principal Automation mengubah status Client `FaUserMain` menjadi Expired hingga perubahan status tersimpan
19. [TC-FA-SU-976] Catat jumlah entri log pada Tab Changelog Doni Prasetyo, Tab System Log aktor, dan Activity Log sebagai baseline
20. [TC-FA-SU-976] Kirim permintaan langsung ke API Activate Doni Prasetyo memakai klien HTTP dengan token sesi Lina Marlina
21. Verifikasi anchor: [TC-FA-SU-976] server menolak permintaan
22. Verifikasi [TC-FA-SU-976] tidak ada entri log baru pada Tab Changelog Doni Prasetyo, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline
23. [TC-FA-SU-977] Catat jumlah entri log pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline
24. [TC-FA-SU-977] Kirim permintaan langsung ke API nyalakan switch Manage asset ID configuration untuk Gita Permata memakai klien HTTP dengan token sesi Lina Marlina
25. Verifikasi anchor: [TC-FA-SU-977] server menolak permintaan
26. Verifikasi [TC-FA-SU-977] tidak ada entri log baru pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline
27. [TC-FA-SU-978] Catat jumlah entri log pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline
28. [TC-FA-SU-978] Kirim permintaan langsung ke API centang Update Manage accounting untuk Gita Permata memakai klien HTTP dengan token sesi Lina Marlina
29. Verifikasi anchor: [TC-FA-SU-978] server menolak permintaan
30. Verifikasi [TC-FA-SU-978] tidak ada entri log baru pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline
31. [TC-FA-SU-979] Catat jumlah entri log pada Tab Changelog Wawan Setiawan, Tab System Log aktor, dan Activity Log sebagai baseline
32. [TC-FA-SU-979] Kirim permintaan langsung ke API tambah grup General Affairs ke Manage files milik Wawan Setiawan memakai klien HTTP dengan token sesi Lina Marlina
33. Verifikasi anchor: [TC-FA-SU-979] server menolak permintaan
34. Verifikasi [TC-FA-SU-979] tidak ada entri log baru pada Tab Changelog Wawan Setiawan, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline
35. Principal Automation memulihkan status Client `FaUserMain` menjadi Aktif hingga perubahan status tersimpan

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- S-05 dan P-5 butir a: spec ini memuat TC-FA-SU-976 sampai 979 untuk asersi absence (kelas g) dengan permintaan langsung ke server sebagai pemicu yang ditolak, user dan baseline sendiri pada tiap TC. Asersi status respons dan state data TC yang sama ada di spec 328. Status 403 pada tiap TC dipakai sebagai anchor bahwa penolakan sudah diproses (bagian 8b butir 2).
- TC sumber menulis "Suspended atau Expired"; kedua status dijalankan berurutan pada empat TC yang sama (langkah 1 sampai 18 untuk Suspended dan langkah 18 sampai 35 untuk Expired), tiap TC dengan baseline sendiri. Awalan `[TC-FA-SU-nnn]` pada langkah menandai TC asal.
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 2, 6, 10, 14, 19, 23, 27, 31, 35.
- Temuan untuk QA:
  - Expected TC menyebut "Tab Changelog, Tab System Log, dan Activity Log" tanpa menyebut pemilik tiap surface; spec memakai Tab Changelog target, Tab System Log aktor, dan Activity Log mengikuti rumusan Post Condition TC-FA-SU-1064.
  - Seluruh TC pada spec ini berkolom FE Test `-` atau Expected berupa respons API (K-1); tidak ada langkah UI, sehingga seluruh langkah adalah permintaan langsung dan pembacaan jumlah entri log.
  - Pre-setup #34 dan #35 adalah Client terpisah; spec memakai `FaUserMain` yang diubah statusnya (sama dengan spec 328). Tim FE menetapkan bila Client #34 dan #35 yang harus dipakai.
