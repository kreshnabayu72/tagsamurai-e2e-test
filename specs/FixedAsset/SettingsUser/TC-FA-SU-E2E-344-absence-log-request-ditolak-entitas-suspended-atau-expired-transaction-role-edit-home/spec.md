---
id: TC-FA-SU-E2E-344-absence-log-request-ditolak-entitas-suspended-atau-expired-transaction-role-edit-home
title: "Absence Log Request Ditolak: Entitas Suspended atau Expired: Transaction Role, Edit Home Group, dan Activate"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-130
  - TC-FA-SU-304
  - TC-FA-SU-980
  - TC-FA-SU-981
coverage:
  web: automated
---

# Absence Log Request Ditolak: Entitas Suspended atau Expired: Transaction Role, Edit Home Group, dan Activate

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Transaction Role (#39). Status Suspended dan Expired setara Client Pre-setup #34 dan #35; spec ini mengubah status Client `FaUserMain` lewat Principal Automation (#12). Target: Lina Marlina (akun sendiri), Ahmad Dahlan (Default User), Gita Permata, dan Mira Anggraini.
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE.
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri pada Tab Changelog target, Tab System Log aktor, dan Activity Log dibaca sebelum permintaan (baseline, S-12) dan sesudah permintaan; audit trail bersifat permanen sehingga asersi memakai selisih terhadap baseline, bukan angka absolut. Log yang menunggu eventual dibaca ulang (muat ulang surface) sampai batas tunggu 2 menit.
- Principal Automation (Pre-setup #12): akun atau kemampuan "disediakan tim FE" untuk mengubah status Client lewat sesi API (R-20, bukan konteks kedua). Token sesi API aktor Total Control tetap berlaku sesudah status Client berubah (disediakan tim FE/BE).
- State global dan pemulihan: status Client `FaUserMain` diubah menjadi Suspended lalu Expired dan dipulihkan menjadi Aktif pada langkah 31 serta di hook `after` (cadangan). Pre-setup lain tidak diubah karena setiap permintaan ditolak server. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-304: Permintaan langsung Edit Home Group untuk akun sendiri, Default User, dan saat Suspended

1. Catat jumlah entri log pada Tab Changelog Lina Marlina, Ahmad Dahlan, dan Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline
2. Kirim permintaan langsung ke API Edit Home Group akun sendiri (Lina Marlina) ke Branch Surabaya memakai klien HTTP dengan token sesi Lina Marlina
3. Verifikasi anchor: server menolak permintaan dengan status 403
4. Kirim permintaan langsung ke API Edit Home Group Ahmad Dahlan (Default User) ke Branch Surabaya memakai klien HTTP dengan token sesi Lina Marlina
5. Verifikasi anchor: server menolak permintaan dengan status 403
6. Principal Automation mengubah status Client `FaUserMain` menjadi Suspended hingga perubahan status tersimpan
7. Kirim permintaan langsung ke API Edit Home Group Gita Permata ke IT Infrastructure memakai klien HTTP dengan token sesi Lina Marlina
8. Verifikasi anchor: server menolak permintaan dengan status 403
9. Verifikasi tidak ada entri log baru pada Tab Changelog Lina Marlina, Ahmad Dahlan, dan Gita Permata, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

### TC-FA-SU-130: Permintaan langsung Activate atau Deactivate saat entitas Suspended

10. Catat jumlah entri log pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline
11. Kirim permintaan langsung ke API Deactivate Gita Permata memakai klien HTTP dengan token sesi Lina Marlina
12. Verifikasi anchor: server menolak permintaan dengan status 403
13. Verifikasi tidak ada entri log baru pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

### Client `FaUserMain` berstatus Suspended: TC-FA-SU-980 dan 981

14. [TC-FA-SU-980] Catat jumlah entri log pada Tab Changelog Mira Anggraini, Tab System Log aktor, dan Activity Log sebagai baseline
15. [TC-FA-SU-980] Kirim permintaan langsung ke API assign Transfer × Asset Admin pada Finance & Accounting untuk Mira Anggraini memakai klien HTTP dengan token sesi Lina Marlina
16. Verifikasi anchor: [TC-FA-SU-980] server menolak permintaan
17. Verifikasi [TC-FA-SU-980] tidak ada entri log baru pada Tab Changelog Mira Anggraini, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline
18. [TC-FA-SU-981] Catat jumlah entri log pada Tab Changelog Mira Anggraini, Tab System Log aktor, dan Activity Log sebagai baseline
19. [TC-FA-SU-981] Kirim permintaan langsung ke API remove baris Borrowing & Assignment × Approver milik Mira Anggraini memakai klien HTTP dengan token sesi Lina Marlina
20. Verifikasi anchor: [TC-FA-SU-981] server menolak permintaan
21. Verifikasi [TC-FA-SU-981] tidak ada entri log baru pada Tab Changelog Mira Anggraini, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

### Client `FaUserMain` berstatus Expired: TC-FA-SU-980 dan 981

22. Principal Automation mengubah status Client `FaUserMain` menjadi Expired hingga perubahan status tersimpan
23. [TC-FA-SU-980] Catat jumlah entri log pada Tab Changelog Mira Anggraini, Tab System Log aktor, dan Activity Log sebagai baseline
24. [TC-FA-SU-980] Kirim permintaan langsung ke API assign Transfer × Asset Admin pada Finance & Accounting untuk Mira Anggraini memakai klien HTTP dengan token sesi Lina Marlina
25. Verifikasi anchor: [TC-FA-SU-980] server menolak permintaan
26. Verifikasi [TC-FA-SU-980] tidak ada entri log baru pada Tab Changelog Mira Anggraini, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline
27. [TC-FA-SU-981] Catat jumlah entri log pada Tab Changelog Mira Anggraini, Tab System Log aktor, dan Activity Log sebagai baseline
28. [TC-FA-SU-981] Kirim permintaan langsung ke API remove baris Borrowing & Assignment × Approver milik Mira Anggraini memakai klien HTTP dengan token sesi Lina Marlina
29. Verifikasi anchor: [TC-FA-SU-981] server menolak permintaan
30. Verifikasi [TC-FA-SU-981] tidak ada entri log baru pada Tab Changelog Mira Anggraini, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline
31. Principal Automation memulihkan status Client `FaUserMain` menjadi Aktif hingga perubahan status tersimpan

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- S-05 dan P-5 butir a: spec ini memuat TC-FA-SU-130, 304, 980, dan 981 untuk asersi absence (kelas g) dengan permintaan langsung ke server sebagai pemicu yang ditolak, user dan baseline sendiri pada tiap TC. Asersi status respons dan state data TC yang sama ada di spec 329. Status 403 pada tiap TC dipakai sebagai anchor bahwa penolakan sudah diproses (bagian 8b butir 2).
- Urutan TC sumber diubah (TC-FA-SU-304, 130, 980, 981) supaya perubahan status Client minimal; TC-FA-SU-980 dan 981 dijalankan pada Suspended lalu Expired (langkah 22), tiap TC dengan baseline sendiri. Awalan `[TC-FA-SU-nnn]` pada langkah menandai TC asal.
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 1, 10, 14, 18, 23, 27, 31.
- Temuan untuk QA:
  - Expected TC menyebut "Tab Changelog, Tab System Log, dan Activity Log" tanpa menyebut pemilik tiap surface; spec memakai Tab Changelog target, Tab System Log aktor, dan Activity Log mengikuti rumusan Post Condition TC-FA-SU-1064.
  - Seluruh TC pada spec ini berkolom FE Test `-` atau Expected berupa respons API (K-1); tidak ada langkah UI, sehingga seluruh langkah adalah permintaan langsung dan pembacaan jumlah entri log.
  - TC-FA-SU-304 tidak menyebut nilai Home Group baru; spec memakai Branch Surabaya dan IT Infrastructure (sama dengan spec 329).
  - Pre-setup #34 dan #35 adalah Client terpisah; spec memakai `FaUserMain` yang diubah statusnya. Tim FE menetapkan bila Client #34 dan #35 yang harus dipakai.
