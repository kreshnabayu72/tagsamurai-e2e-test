---
id: TC-FA-SU-E2E-328-defense-in-depth-entitas-suspended-atau-expired-activate-global-role-dan-group-role
title: "Defense-in-depth Entitas Suspended atau Expired: Activate, Global Role, dan Group Role"
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

# Defense-in-depth Entitas Suspended atau Expired: Activate, Global Role, dan Group Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Transaction Role (#39). Status Suspended dan Expired setara Client Pre-setup #34 `FaUserSuspended` dan #35 `FaUserExpired`; spec ini mengubah status Client `FaUserMain` (akun aktor Pre-setup #1 berada di Client itu) lewat Principal Automation (#12). Target: Doni Prasetyo (Inactive), Gita Permata, dan Wawan Setiawan.
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE.
- Principal Automation (Pre-setup #12): akun atau kemampuan "disediakan tim FE" untuk mengubah status Client lewat sesi API (R-20, bukan konteks kedua). Token sesi API aktor Total Control tetap berlaku sesudah status Client berubah (disediakan tim FE/BE).
- State global dan pemulihan: status Client `FaUserMain` diubah menjadi Suspended lalu Expired dan dipulihkan menjadi Aktif pada langkah 27 serta di hook `after` (cadangan, tetap jalan walau spec gagal di tengah). Pre-setup lain tidak diubah karena setiap permintaan ditolak server. Suite berjalan serial (`parallel: false`).

## Test Steps

### Client `FaUserMain` berstatus Suspended: TC-FA-SU-976, 977, 978, 979

1. Principal Automation mengubah status Client `FaUserMain` menjadi Suspended hingga perubahan status tersimpan
2. [TC-FA-SU-976] Kirim permintaan langsung ke API Activate Doni Prasetyo memakai klien HTTP dengan token sesi Lina Marlina
3. Verifikasi [TC-FA-SU-976] server menolak permintaan
4. Verifikasi [TC-FA-SU-976] Doni Prasetyo tetap Inactive (dibaca lewat API)
5. [TC-FA-SU-977] Kirim permintaan langsung ke API nyalakan switch Manage asset ID configuration untuk Gita Permata memakai klien HTTP dengan token sesi Lina Marlina
6. Verifikasi [TC-FA-SU-977] server menolak permintaan
7. Verifikasi [TC-FA-SU-977] switch Manage asset ID configuration Gita Permata tetap OFF (dibaca lewat API)
8. [TC-FA-SU-978] Kirim permintaan langsung ke API centang Update Manage accounting untuk Gita Permata memakai klien HTTP dengan token sesi Lina Marlina
9. Verifikasi [TC-FA-SU-978] server menolak permintaan
10. Verifikasi [TC-FA-SU-978] nilai Update Manage accounting Gita Permata tidak berubah (dibaca lewat API)
11. [TC-FA-SU-979] Kirim permintaan langsung ke API tambah grup General Affairs ke Manage files milik Wawan Setiawan memakai klien HTTP dengan token sesi Lina Marlina
12. Verifikasi [TC-FA-SU-979] server menolak permintaan
13. Verifikasi [TC-FA-SU-979] penugasan grup Group Role Wawan Setiawan tidak berubah (dibaca lewat API)

### Client `FaUserMain` berstatus Expired: TC-FA-SU-976, 977, 978, 979

14. Principal Automation mengubah status Client `FaUserMain` menjadi Expired hingga perubahan status tersimpan
15. [TC-FA-SU-976] Kirim permintaan langsung ke API Activate Doni Prasetyo memakai klien HTTP dengan token sesi Lina Marlina
16. Verifikasi [TC-FA-SU-976] server menolak permintaan
17. Verifikasi [TC-FA-SU-976] Doni Prasetyo tetap Inactive (dibaca lewat API)
18. [TC-FA-SU-977] Kirim permintaan langsung ke API nyalakan switch Manage asset ID configuration untuk Gita Permata memakai klien HTTP dengan token sesi Lina Marlina
19. Verifikasi [TC-FA-SU-977] server menolak permintaan
20. Verifikasi [TC-FA-SU-977] switch Manage asset ID configuration Gita Permata tetap OFF (dibaca lewat API)
21. [TC-FA-SU-978] Kirim permintaan langsung ke API centang Update Manage accounting untuk Gita Permata memakai klien HTTP dengan token sesi Lina Marlina
22. Verifikasi [TC-FA-SU-978] server menolak permintaan
23. Verifikasi [TC-FA-SU-978] nilai Update Manage accounting Gita Permata tidak berubah (dibaca lewat API)
24. [TC-FA-SU-979] Kirim permintaan langsung ke API tambah grup General Affairs ke Manage files milik Wawan Setiawan memakai klien HTTP dengan token sesi Lina Marlina
25. Verifikasi [TC-FA-SU-979] server menolak permintaan
26. Verifikasi [TC-FA-SU-979] penugasan grup Group Role Wawan Setiawan tidak berubah (dibaca lewat API)
27. Principal Automation memulihkan status Client `FaUserMain` menjadi Aktif hingga perubahan status tersimpan

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- K-1 dan bagian 8b butir 1: TC-FA-SU-976 sampai 979 berformat Expected respons API (status respons dan state data). TC tetap masuk spec FE+BE walau tumpang tindih dengan pengujian tingkat endpoint; asersi spec hanya status respons dan state data, bukan tampilan UI.
- S-05: klausa "tidak ada entri log baru" pada TC-FA-SU-976 sampai 979 diasersi di spec 343 (kelas g) dengan permintaan yang sama sebagai pemicu, user dan baseline sendiri. Spec ini hanya mengasersi status respons dan state data; id TC tetap di `sourceTc` kedua spec.
- TC sumber menulis "Suspended atau Expired"; kedua status dijalankan berurutan pada empat TC yang sama (langkah 1 sampai 14 untuk Suspended dan langkah 14 sampai 27 untuk Expired). Awalan `[TC-FA-SU-nnn]` pada langkah menandai TC asal.
- Expected a TC sumber tidak menyebut kode status; spec mengasersi "menolak permintaan" tanpa kode.
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 27.
- Temuan untuk QA:
  - TC-FA-SU-976 sampai 979 menulis "Suspended atau Expired" tanpa menyatakan apakah keduanya diuji; spec menguji keduanya (Pre-setup #34 dan #35 tercantum di Data Uji).
  - Pre-setup #34 dan #35 adalah Client terpisah dengan 25 pengguna, sedangkan Langkah Uji menyebut Principal mengubah status Client; akun aktor #1 hanya ada di `FaUserMain`, sehingga spec memakai `FaUserMain` yang diubah statusnya. Tim FE menetapkan bila Client #34 dan #35 yang harus dipakai.
  - TC-FA-SU-976 sampai 979 berkolom FE Test `-`; seluruh langkah adalah permintaan langsung (K-1).
