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
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan penugasan peran pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC. Pemulihan dijalankan sebagai langkah penghubung dan di hook `after` (cadangan). Pemulihan Home Group Lina Marlina dan Citra Lestari pada langkah 19, 50 dan di hook `after`. Efek pada Pre-setup: Home Group, Last Updated, dan Modified By kedua pengguna berubah dan entri log permanen `Edit Home Group` bertambah.

## Test Steps

1. Catat baris pola Group Role dan Transaction Role Lina Marlina dan Citra Lestari di semua group sebagai baseline

### TC-FA-SU-299: Edit Home Group target Total Control dan Read Only oleh Default User

2. Ketik Search `Lina Marlina`, tekan Enter
3. Edit Home Group Lina Marlina ke Branch Surabaya (klik ⋯, `Edit Home Group`, klik node Branch Surabaya, klik `[Select]`)
4. Verifikasi tidak ada dialog constraint
5. Verifikasi toast "Success, home group has been updated." tampil
6. Verifikasi Home Group Lina Marlina menjadi Branch Surabaya
7. Ganti isi kotak search dengan `Citra Lestari`, tekan Enter
8. Edit Home Group Citra Lestari ke Branch Surabaya (klik ⋯, `Edit Home Group`, klik node Branch Surabaya, klik `[Select]`)
9. Verifikasi tidak ada dialog constraint
10. Verifikasi toast "Success, home group has been updated." tampil
11. Verifikasi Home Group Citra Lestari menjadi Branch Surabaya
12. Ganti isi kotak search dengan `Lina Marlina`, tekan Enter
13. Buka Detail Lina Marlina > Tab Role
14. Verifikasi baris pola Group Role dan Transaction Role Lina Marlina di semua group tetap utuh dan sama dengan baseline
15. Kembali ke User List
16. Ganti isi kotak search dengan `Citra Lestari`, tekan Enter
17. Buka Detail Citra Lestari > Tab Role
18. Verifikasi baris pola Group Role dan Transaction Role Citra Lestari di semua group tetap utuh dan sama dengan baseline
19. Pulihkan Home Group Lina Marlina dan Citra Lestari ke kondisi Pre-setup lewat seed API

### TC-FA-SU-1069: Edit Home Group target Total Control dan Read Only oleh Manage global user & role

20. Ganti akun: Logout lalu login sebagai Manage global user & role (Update) Qori Akbar
21. Buka Fixed Asset > Settings > User dari sidebar
22. Catat jumlah entri `Auto-Revert` pada Tab Changelog Lina Marlina dan Tab Changelog Citra Lestari sebagai baseline TC-FA-SU-1069
23. Ketik Search `Lina Marlina`, tekan Enter
24. Klik ⋯ pada baris Lina Marlina
25. Verifikasi aksi `Edit Home Group` tampil pada baris Lina Marlina
26. Tekan Esc untuk menutup menu ⋯
27. Ganti isi kotak search dengan `Citra Lestari`, tekan Enter
28. Klik ⋯ pada baris Citra Lestari
29. Verifikasi aksi `Edit Home Group` tampil pada baris Citra Lestari
30. Tekan Esc untuk menutup menu ⋯
31. Ganti isi kotak search dengan `Lina Marlina`, tekan Enter
32. Edit Home Group Lina Marlina ke Branch Surabaya (klik ⋯, `Edit Home Group`, klik node Branch Surabaya, klik `[Select]`)
33. Verifikasi tidak ada dialog constraint
34. Verifikasi toast "Success, home group has been updated." tampil
35. Ganti isi kotak search dengan `Citra Lestari`, tekan Enter
36. Edit Home Group Citra Lestari ke Branch Surabaya (klik ⋯, `Edit Home Group`, klik node Branch Surabaya, klik `[Select]`)
37. Verifikasi tidak ada dialog constraint
38. Verifikasi toast "Success, home group has been updated." tampil
39. Ganti isi kotak search dengan `Lina Marlina`, tekan Enter
40. Buka Detail Lina Marlina > Tab Role
41. Verifikasi banner Total Control tetap tampil pada Tab Role Lina Marlina
42. Verifikasi baris pola Group Role dan Transaction Role Lina Marlina di semua group tetap utuh dan sama dengan baseline
43. Kembali ke User List
44. Ganti isi kotak search dengan `Citra Lestari`, tekan Enter
45. Buka Detail Citra Lestari > Tab Role
46. Verifikasi banner Read Only tetap tampil pada Tab Role Citra Lestari
47. Verifikasi baris pola Group Role dan Transaction Role Citra Lestari di semua group tetap utuh dan sama dengan baseline
48. Baca jumlah entri `Auto-Revert` pada Tab Changelog Lina Marlina dan Tab Changelog Citra Lestari
49. Verifikasi jumlah entri `Auto-Revert` sama dengan baseline langkah 22 pada Tab Changelog Lina Marlina dan Tab Changelog Citra Lestari
50. Pulihkan Home Group Lina Marlina dan Citra Lestari ke kondisi Pre-setup lewat seed API

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular. Aktor Default User Ahmad Dahlan login di hook `before` (akun pertama spec); hook `after` memulihkan sesi ke akun default suite.
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 (baseline baris pola) dan 22 (baseline `Auto-Revert` TC-FA-SU-1069, dicatat tepat sebelum aksi TC itu dan terpisah dari TC-FA-SU-299), membuka Detail (langkah 13, 17, 40, dan 45) dan kembali ke User List (langkah 15 dan 43), Search untuk menemukan baris target (langkah 2, 7, 12, 16, 23, 27, 31, 35, 39, dan 44; R-16 dan butir 8b.13, memakai "ganti isi kotak search" bila kotak sudah berisi), menutup menu ⋯ dengan Esc, ganti akun (langkah 20) dan membuka sidebar Fixed Asset > Settings > User sesudahnya (langkah 21, S-14), serta langkah 19 dan 50 (pemulihan). Pemulihan antar TC diperlukan supaya Lina Marlina dan Citra Lestari belum berada di Branch Surabaya pada TC-FA-SU-1069.
- "Tidak ada entri `Auto-Revert`" (TC-FA-SU-1069 Expected c) ditulis sebagai asersi jumlah dengan baseline (S-12), bukan kelas g; toast sukses server menjadi anchor positif.
- TC-FA-SU-299 butir b dan c serta TC-FA-SU-1069 butir b dan c diperbarui (gate Home Group): baris pola Group Role dan Transaction Role Total Control dan Read Only dikecualikan dari constraint dan tidak dicabut; spec mengasersi tidak ada dialog constraint dan baris pola di semua group sama dengan baseline (langkah 14, 18, 42, 47), menggantikan klaim lama bahwa tidak ada Group Role yang dibatasi.
- Jumlah langkah 50 (di atas smell 35 langkah) dengan alasan: satu skenario, dua TC (299, 1069) pada target yang sama; baris pola Group Role dan Role Transaksi TC/RO direkam di baseline lalu diverifikasi utuh di empat titik (langkah 14, 18, 42, 47) dan seed dipulihkan dua kali (langkah 19, 50). Kelebihan langkah berasal dari Search per baris target (R-16) dan kembali ke User List antar Detail. Pemecahan akan menggandakan baseline yang sama.
- Temuan untuk QA (S-15): (1) Post Condition TC-FA-SU-299 butir b dan TC-FA-SU-1069 butir b (satu entri `Edit Home Group` per pengguna pada Tab Changelog target, Tab System Log aktor, dan Activity Log) tidak punya langkah observasi dan tidak diasersi. (2) Email akun Qori Akbar tidak tertulis di Pre-setup TC. (3) Home Group awal Lina Marlina dan Citra Lestari tidak tertulis di Pre-setup TC selain Citra Lestari (General Affairs, Pre-setup #43); pemulihan memakai kondisi Pre-setup. (4) Baseline `Auto-Revert` hanya diasersi pada TC-FA-SU-1069 (TC-FA-SU-299 tidak memuat asersi itu), sehingga dicatat tepat sebelum aksi TC-FA-SU-1069, bukan di awal spec.
