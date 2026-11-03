---
id: TC-FA-SU-E2E-329-defense-in-depth-entitas-suspended-atau-expired-transaction-role-edit-home-group-dan
title: "Defense-in-depth Entitas Suspended atau Expired: Transaction Role, Edit Home Group, dan Activate"
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

# Defense-in-depth Entitas Suspended atau Expired: Transaction Role, Edit Home Group, dan Activate

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Transaction Role (#39). Status Suspended dan Expired setara Client Pre-setup #34 dan #35; spec ini mengubah status Client `FaUserMain` lewat Principal Automation (#12) karena akun aktor Pre-setup #1 berada di Client itu. Target: Lina Marlina (akun sendiri), Ahmad Dahlan (Default User, Home Group awal IT Infrastructure), Gita Permata, dan Mira Anggraini.
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE.
- Principal Automation (Pre-setup #12): akun atau kemampuan "disediakan tim FE" untuk mengubah status Client lewat sesi API (R-20, bukan konteks kedua). Token sesi API aktor Total Control tetap berlaku sesudah status Client berubah (disediakan tim FE/BE).
- State global dan pemulihan: status Client `FaUserMain` diubah menjadi Suspended lalu Expired dan dipulihkan menjadi Aktif pada langkah 25 serta di hook `after` (cadangan). Pre-setup lain tidak diubah karena setiap permintaan ditolak server. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-304: Permintaan langsung Edit Home Group untuk akun sendiri, Default User, dan saat Suspended

1. Kirim permintaan langsung ke API Edit Home Group akun sendiri (Lina Marlina) ke Branch Surabaya memakai klien HTTP dengan token sesi Lina Marlina
2. Verifikasi server menolak permintaan dengan status 403
3. Kirim permintaan langsung ke API Edit Home Group Ahmad Dahlan (Default User) ke Branch Surabaya memakai klien HTTP dengan token sesi Lina Marlina
4. Verifikasi server menolak permintaan dengan status 403
5. Principal Automation mengubah status Client `FaUserMain` menjadi Suspended hingga perubahan status tersimpan
6. Kirim permintaan langsung ke API Edit Home Group Gita Permata ke IT Infrastructure memakai klien HTTP dengan token sesi Lina Marlina
7. Verifikasi server menolak permintaan dengan status 403
8. Verifikasi Home Group Lina Marlina, Ahmad Dahlan, dan Gita Permata tidak berubah (dibaca lewat API)

### TC-FA-SU-130: Permintaan langsung Activate atau Deactivate saat entitas Suspended

9. Kirim permintaan langsung ke API Deactivate Gita Permata memakai klien HTTP dengan token sesi Lina Marlina
10. Verifikasi server menolak permintaan dengan status 403
11. Verifikasi status Gita Permata tidak berubah, tetap Active (dibaca lewat API)

### Client `FaUserMain` berstatus Suspended: TC-FA-SU-980 dan 981

12. [TC-FA-SU-980] Kirim permintaan langsung ke API assign Transfer × Asset Admin pada Finance & Accounting untuk Mira Anggraini memakai klien HTTP dengan token sesi Lina Marlina
13. Verifikasi [TC-FA-SU-980] server menolak permintaan
14. Verifikasi [TC-FA-SU-980] Transaction Role Mira Anggraini tidak berubah (dibaca lewat API)
15. [TC-FA-SU-981] Kirim permintaan langsung ke API remove baris Borrowing & Assignment × Approver milik Mira Anggraini memakai klien HTTP dengan token sesi Lina Marlina
16. Verifikasi [TC-FA-SU-981] server menolak permintaan
17. Verifikasi [TC-FA-SU-981] baris Borrowing & Assignment × Approver milik Mira Anggraini tetap ada (dibaca lewat API)

### Client `FaUserMain` berstatus Expired: TC-FA-SU-980 dan 981

18. Principal Automation mengubah status Client `FaUserMain` menjadi Expired hingga perubahan status tersimpan
19. [TC-FA-SU-980] Kirim permintaan langsung ke API assign Transfer × Asset Admin pada Finance & Accounting untuk Mira Anggraini memakai klien HTTP dengan token sesi Lina Marlina
20. Verifikasi [TC-FA-SU-980] server menolak permintaan
21. Verifikasi [TC-FA-SU-980] Transaction Role Mira Anggraini tidak berubah (dibaca lewat API)
22. [TC-FA-SU-981] Kirim permintaan langsung ke API remove baris Borrowing & Assignment × Approver milik Mira Anggraini memakai klien HTTP dengan token sesi Lina Marlina
23. Verifikasi [TC-FA-SU-981] server menolak permintaan
24. Verifikasi [TC-FA-SU-981] baris Borrowing & Assignment × Approver milik Mira Anggraini tetap ada (dibaca lewat API)
25. Principal Automation memulihkan status Client `FaUserMain` menjadi Aktif hingga perubahan status tersimpan

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- K-1 dan bagian 8b butir 1: TC-FA-SU-130, 304, 980, dan 981 berformat Expected respons API (status respons dan state data). TC tetap masuk spec FE+BE walau tumpang tindih dengan pengujian tingkat endpoint; asersi spec hanya status respons dan state data, bukan tampilan UI.
- S-05: klausa "tidak ada entri log baru" pada TC-FA-SU-130, 304, 980, dan 981 diasersi di spec 344 (kelas g) dengan permintaan yang sama sebagai pemicu, user dan baseline sendiri. Spec ini hanya mengasersi status respons dan state data; id TC tetap di `sourceTc` kedua spec.
- Urutan TC sumber diubah (TC-FA-SU-304, 130, 980, 981) supaya perubahan status Client minimal: dua permintaan pertama TC-FA-SU-304 dijalankan sebelum Suspended, lalu Suspended dipakai bersama TC-FA-SU-130, 980, dan 981 sebelum Expired (langkah 18).
- TC-FA-SU-980 dan 981 menulis "Suspended atau Expired"; kedua status dijalankan berurutan. Awalan `[TC-FA-SU-nnn]` pada langkah menandai TC asal. Expected a TC-FA-SU-980 dan 981 tidak menyebut kode status, sehingga spec mengasersi "menolak permintaan" tanpa kode.
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 25.
- Temuan untuk QA:
  - TC-FA-SU-304 tidak menyebut nilai Home Group baru dan Langkah Uji 3 tidak menyebut urutan terhadap Langkah 1 dan 2 selain "Principal membuat Client Suspended"; spec memakai Branch Surabaya dan IT Infrastructure.
  - Pre-setup #34 dan #35 adalah Client terpisah, sedangkan Langkah Uji menyebut Principal mengubah status Client; spec memakai `FaUserMain` yang diubah statusnya. Tim FE menetapkan bila Client #34 dan #35 yang harus dipakai.
  - TC-FA-SU-130, 304, 980, dan 981 berkolom FE Test `-`; seluruh langkah adalah permintaan langsung (K-1).
