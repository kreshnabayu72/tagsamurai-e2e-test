---
id: TC-FA-SU-E2E-106-edit-home-group-target-total-control-dan-read-only-oleh-default-user-dan-manage-global-user-dan-role
title: "Edit Home Group Target Total Control dan Read Only oleh Default User dan Manage global user & role"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-299
  - TC-FA-SU-1069
coverage:
  web: automated
---

# Edit Home Group Target Total Control dan Read Only oleh Default User dan Manage global user & role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2), `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite (Total Control Lina Marlina, `FA_TC_PASSWORD`). Aktor kedua (Manage global user & role (Update) Qori Akbar, Pre-setup #4, kredensial `Spectra.env.FA_MURG_UPD_PASSWORD`; email tidak tertulis di Pre-setup TC dan disediakan tim FE) berganti akun lewat langkah eksplisit.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23). Pengguna target: Lina Marlina (Total Control) dan Citra Lestari (Read Only). Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): entri `Edit Home Group` pada Tab Changelog pengguna target, Tab System Log aktor, dan Activity Log, dibaca sebelum dan sesudah aksi. Audit trail bersifat permanen sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut.
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan penugasan peran pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC. Pemulihan dijalankan sebagai langkah penghubung dan di hook `after` (cadangan). Pemulihan Home Group Lina Marlina dan Citra Lestari pada langkah 14, 36 dan di hook `after`. Efek pada Pre-setup: Home Group, Last Updated, dan Modified By kedua pengguna berubah dan entri log permanen `Edit Home Group` bertambah.

## Test Steps

1. Catat jumlah entri `Auto-Revert` pada Tab Changelog Lina Marlina dan Tab Changelog Citra Lestari sebagai baseline; catat juga baris pola Group Role dan Transaction Role Lina Marlina dan Citra Lestari di semua group

### TC-FA-SU-299: Edit Home Group target Total Control dan Read Only oleh Default User

2. Edit Home Group Lina Marlina ke Branch Surabaya (klik ⋯, `Edit Home Group`, klik node Branch Surabaya, klik `[Select]`)
3. Verifikasi tidak ada dialog constraint
4. Verifikasi toast "Success, home group has been updated." tampil
5. Verifikasi Home Group Lina Marlina menjadi Branch Surabaya
6. Edit Home Group Citra Lestari ke Branch Surabaya (klik ⋯, `Edit Home Group`, klik node Branch Surabaya, klik `[Select]`)
7. Verifikasi tidak ada dialog constraint
8. Verifikasi toast "Success, home group has been updated." tampil
9. Verifikasi Home Group Citra Lestari menjadi Branch Surabaya
10. Buka Detail Lina Marlina > Tab Role
11. Verifikasi baris pola Group Role dan Transaction Role Lina Marlina di semua group tetap utuh dan sama dengan baseline
12. Buka Detail Citra Lestari > Tab Role
13. Verifikasi baris pola Group Role dan Transaction Role Citra Lestari di semua group tetap utuh dan sama dengan baseline
14. Pulihkan Home Group Lina Marlina dan Citra Lestari ke kondisi Pre-setup lewat seed API

### TC-FA-SU-1069: Edit Home Group target Total Control dan Read Only oleh Manage global user & role

15. Ganti akun: Logout lalu login sebagai Manage global user & role (Update) Qori Akbar
16. Klik ⋯ pada baris Lina Marlina
17. Verifikasi aksi `Edit Home Group` tampil pada baris Lina Marlina
18. Tekan Esc untuk menutup menu ⋯
19. Klik ⋯ pada baris Citra Lestari
20. Verifikasi aksi `Edit Home Group` tampil pada baris Citra Lestari
21. Tekan Esc untuk menutup menu ⋯
22. Edit Home Group Lina Marlina ke Branch Surabaya (klik ⋯, `Edit Home Group`, klik node Branch Surabaya, klik `[Select]`)
23. Verifikasi tidak ada dialog constraint
24. Verifikasi toast "Success, home group has been updated." tampil
25. Edit Home Group Citra Lestari ke Branch Surabaya (klik ⋯, `Edit Home Group`, klik node Branch Surabaya, klik `[Select]`)
26. Verifikasi tidak ada dialog constraint
27. Verifikasi toast "Success, home group has been updated." tampil
28. Buka Detail Lina Marlina > Tab Role
29. Verifikasi banner Total Control tetap tampil pada Tab Role Lina Marlina
30. Verifikasi baris pola Group Role dan Transaction Role Lina Marlina di semua group tetap utuh dan sama dengan baseline
31. Buka Detail Citra Lestari > Tab Role
32. Verifikasi banner Read Only tetap tampil pada Tab Role Citra Lestari
33. Verifikasi baris pola Group Role dan Transaction Role Citra Lestari di semua group tetap utuh dan sama dengan baseline
34. Baca jumlah entri `Auto-Revert` pada Tab Changelog Lina Marlina dan Tab Changelog Citra Lestari
35. Verifikasi jumlah entri `Auto-Revert` sama dengan baseline pada Tab Changelog Lina Marlina dan Tab Changelog Citra Lestari
36. Pulihkan Home Group Lina Marlina dan Citra Lestari ke kondisi Pre-setup lewat seed API

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular. Aktor Default User Ahmad Dahlan login di hook `before` (akun pertama spec); hook `after` memulihkan sesi ke akun default suite.
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 (baseline), membuka Detail (langkah 10 dan 12), menutup menu ⋯ dengan Esc, ganti akun, dan langkah 14 serta 36 (pemulihan). Pemulihan antar TC diperlukan supaya Lina Marlina dan Citra Lestari belum berada di Branch Surabaya pada TC-FA-SU-1069.
- "Tidak ada entri `Auto-Revert`" (TC-FA-SU-1069 Expected c) ditulis sebagai asersi jumlah dengan baseline (S-12), bukan kelas g; toast sukses server menjadi anchor positif.
- TC-FA-SU-299 butir b dan c serta TC-FA-SU-1069 butir b dan c diperbarui (gate Home Group): baris pola Group Role dan Transaction Role Total Control dan Read Only dikecualikan dari constraint dan tidak dicabut; spec mengasersi tidak ada dialog constraint dan baris pola di semua group sama dengan baseline (langkah 11, 13, 30, 33), menggantikan klaim lama bahwa tidak ada Group Role yang dibatasi.
- Jumlah langkah 36 (di atas 35 langkah) dengan alasan: satu skenario, dua TC (299, 1069) pada target yang sama; baris pola Group Role dan Role Transaksi TC/RO direkam di baseline lalu diverifikasi utuh di dua titik (langkah 11, 13, 30, 33) dan seed dipulihkan dua kali (langkah 14, 36). Pemecahan akan menggandakan baseline yang sama.
- Temuan untuk QA (S-15): (1) Post Condition TC-FA-SU-299 butir b dan TC-FA-SU-1069 butir b (satu entri `Edit Home Group` per pengguna pada Tab Changelog target, Tab System Log aktor, dan Activity Log) tidak punya langkah observasi dan tidak diasersi. (2) Email akun Qori Akbar tidak tertulis di Pre-setup TC. (3) Home Group awal Lina Marlina dan Citra Lestari tidak tertulis di Pre-setup TC selain Citra Lestari (General Affairs, Pre-setup #43); pemulihan memakai kondisi Pre-setup.
