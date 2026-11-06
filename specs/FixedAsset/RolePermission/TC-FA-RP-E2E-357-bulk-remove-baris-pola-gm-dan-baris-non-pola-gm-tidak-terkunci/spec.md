---
id: TC-FA-RP-E2E-357-bulk-remove-baris-pola-gm-dan-baris-non-pola-gm-tidak-terkunci
title: "Baris non-pola milik target GM tidak terkunci, dan Bulk Remove yang memuat baris pola GM dan baris Standard memicu dialog D-07 dengan anotasi Group Manager"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1190
  - TC-FA-RP-1194
coverage:
  web: automated
---

# Baris non-pola milik target GM tidak terkunci, dan Bulk Remove yang memuat baris pola GM dan baris Standard memicu dialog D-07 dengan anotasi Group Manager

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #13 (Kevin Susanto, Group Manager hanya di `Data Center`; baris pola GM di `Data Center` dan `Rack A1`: Group Role katalog selain `Manage user & role` dengan CRUD penuh; baris non-pola: Group Role `Manage user & role` di `Data Center`), #18 (pohon Group), #39 (Detail Role `Manage files` terisi; Ahmad Fauzi memegang `Manage files` di `Data Center`; hitungan baris berlaku tanpa seed GM, sehingga baris pola Kevin Susanto menambah baris pada `Data Center` dan `Rack A1`). Precondition TC-FA-RP-1194: Kevin Susanto memegang Group Role `Manage user & role` di `Data Center` sebagai baris reguler (bagian dari Pre-setup #13).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: baris Group Role `Manage user & role` Kevin Susanto di `Data Center` dihapus oleh langkah 10; baris `Manage files` Ahmad Fauzi dan Kevin Susanto di `Data Center` dihapus oleh langkah 33; penugasan Group Manager Kevin Susanto di `Data Center` dilepas oleh langkah 33 (baris pola GM lainnya dipertahankan sebagai penugasan biasa). Hook `before` memastikan state Pre-setup #13 dan #39 dan hook `after` memulihkan keduanya lewat fixture backend yang disediakan tim FE/BE (TC: "dipulihkan ke state Pre-setup #13 dan #39 oleh automation baseline"), tidak berasumsi langkah spec berhasil penuh. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1194: Baris non-pola milik target Group Manager tidak terkunci

1. Klik Tab `System`
2. Buka Detail Role `Manage user & role`
3. Klik node `Data Center` pada Sidebar Group Tree
4. Hapus centang Update pada baris Kevin Susanto
5. Verifikasi toast sukses `Success, permissions have been updated.`
6. Verifikasi dialog auto-revert tidak tampil
7. Klik `[⋯]` baris Kevin Susanto lalu `Remove`
8. Verifikasi dialog Remove biasa `D-03` tampil: Title `Remove User`, bullet `• Kevin S`
9. Verifikasi dialog `D-05` tidak tampil
10. Klik `[Remove]` pada dialog
11. Verifikasi toast sukses `Success, user has been removed.`
12. Klik Tab `Group Manager`
13. Verifikasi Kevin Susanto tetap tampil di Tab `Group Manager`
14. Klik Tab `System`
15. Buka Detail Role `Manage files`
16. Klik node `Data Center` pada Sidebar Group Tree
17. Verifikasi baris pola `Manage files` Kevin Susanto di `Data Center` tetap ada

### TC-FA-RP-1190: Bulk Remove yang memuat baris pola GM dan baris Standard

18. Centang baris Kevin Susanto
19. Centang baris Ahmad Fauzi
20. Klik `Bulk Action` lalu `Remove`
21. Verifikasi dialog `D-07` severity danger: Title `Remove Users`; Body bullet `• Kevin S (Group Manager)` dan `• Ahmad F`, lalu `The role assignments, including their permissions, will be removed permanently.`, lalu `Kevin Susanto will lose their access level as a result.`, ditutup `Are you sure you want to remove them?`; tombol `[Cancel]` dan `[Remove]` (copy usulan, PRD 12 #7)
22. Verifikasi dialog `D-06` tidak tampil
23. Klik `[Cancel]`
24. Verifikasi baris Kevin Susanto dan Ahmad Fauzi tetap ada di `Data Center`
25. Klik Tab `Group Manager`
26. Verifikasi Kevin Susanto tetap tampil sebagai Group Manager di Tab `Group Manager`
27. Klik Tab `System`
28. Buka Detail Role `Manage files`
29. Klik node `Data Center` pada Sidebar Group Tree
30. Centang baris Kevin Susanto
31. Centang baris Ahmad Fauzi
32. Klik `Bulk Action` lalu `Remove`
33. Klik `[Remove]` pada dialog
34. Verifikasi sedikitnya satu baris lain tampil pada node `Data Center`
35. Verifikasi baris Ahmad Fauzi di `Data Center` hilang (baris yang dipilih terhapus oleh aksi Remove)
36. Verifikasi baris Kevin Susanto di `Data Center` hilang (baris yang dipilih terhapus oleh aksi Remove)
37. Klik node `Rack A1` pada Sidebar Group Tree
38. Verifikasi baris Kevin Susanto pada `Manage files` di `Rack A1` tetap ada (baris pola yang tidak dipilih dipertahankan)
39. Klik Tab `Transaction Role`
40. Klik node `Data Center` pada Sidebar Group Tree
41. Klik sub-tab `Disposal`
42. Verifikasi Kevin Susanto tetap tampil di section Asset Admin dan Approver pada `Data Center`
43. Verifikasi lewat kemampuan baca seluruh baris Group Role pola GM lain Kevin Susanto di `Data Center` dan `Rack A1` (selain `Manage files` yang dipilih) tetap ada
44. Klik Tab `Group Manager`
45. Verifikasi sedikitnya satu baris Group Manager lain tampil di Tab `Group Manager`
46. Verifikasi Kevin Susanto tidak ada di Tab `Group Manager`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 46 langkah.
- Alasan di atas sekitar 35 langkah (46 langkah): dua TC satu topik (kunci atau tidaknya baris Kevin Susanto di Detail Role) yang berbagi Detail Role, node `Data Center`, dan target; TC-FA-RP-1190 melepas Group Manager Kevin Susanto sehingga ditaruh di akhir, dan langkah 17 menyerahkan Detail Role `Manage files` `Data Center` langsung ke langkah 18. Asersi pasca-Remove TC-FA-RP-1190 (baris pola lain di Group Role dan Role Transaksi dipertahankan) menambah langkah baca pada aksi yang tidak dapat diulang. Kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Perubahan urutan TC dibanding TC sumber (S-05): TC-FA-RP-1194 ditulis lebih dulu daripada TC-FA-RP-1190 karena TC-FA-RP-1194 membutuhkan Kevin Susanto masih Group Manager, sedangkan TC-FA-RP-1190 melepasnya.
- Langkah penghubung (S-03): langkah 1 sampai 3, 12, 14 sampai 16, 25, 27 sampai 29, 37, 39 sampai 41, dan 44 (navigasi Tab, Detail Role, node, sub-tab). Tanpa Search pada tabel Detail Role: tiap node memuat paling banyak sepuluh baris, dalam satu halaman (R-16). Langkah 5 menjadi anchor positif atas asersi absence dialog langkah 6 (HINT g: edit berhasil), langkah 8 atas langkah 9, dan langkah 21 atas langkah 22. Langkah 34 dan 45 adalah `Verifikasi` pembanding sebagai anchor absence atas langkah 35 sampai 36 dan 46 (bagian 8b butir 2).
- TC-FA-RP-1190 tidak mengasersi toast hasil Bulk Remove (TC: tidak ditetapkan untuk campuran baris tier); langkah 33 tidak diikuti `Verifikasi` toast. Anchor absence untuk langkah 35 sampai 36 adalah baris pembanding langkah 34.
- Pembagian TC lintas spec: tidak ada; kedua TC hanya ada di spec ini.
- Fix pass 4 (keputusan: auto-revert GM mempertahankan baris): hanya baris yang dipilih Bulk Remove yang terhapus; baris pola GM lain (Kevin Susanto `Manage files` di `Rack A1`, Group Role lain, Asset Admin dan Approver) tetap ada, tanpa asersi log per baris.
- Temuan untuk QA:
  - TC-FA-RP-1194 (baris MUR milik GM) menunggu konfirmasi PM atas maksud FARP-LOGIC-24 dan 24d; spec mengasersi apa yang tertulis di TC (edit dan Remove memakai alur biasa tanpa auto-revert, Open Item #7).
  - TC-FA-RP-1190 Expected b: interpretasi bahwa baris yang dihapus oleh aksi pemicu (baris yang dipilih) tetap terhapus, bukan dikembalikan, menunggu konfirmasi PM.
  - TC-FA-RP-1190 menandai copy dialog D-07 sebagai `copy usulan, PRD 12 #7`; spec menulis teks TC apa adanya.
  - TC-FA-RP-1190 Expected b "seluruh baris pola GM lainnya (Group Role di `Data Center` dan `Rack A1`)" tidak merinci role; spec menelusuri `Manage files` di `Rack A1` lewat UI dan Group Role lain lewat kemampuan baca (langkah 43), serta Asset Admin dan Approver sub-tab `Disposal` `Data Center`.
  - Seed Kevin Susanto tidak konsisten antar sumber: Pre-setup #13 dan #43 hanya `Data Center`, Pre-setup #38 dan beberapa TC lain `Data Center` dan `Helpdesk`. Spec mengikuti #13.
  - TC-FA-RP-1194 Expected a tidak menyebut apakah penghapusan centang Update memicu dialog konfirmasi biasa; spec mengasersi toast sukses dan tidak ada dialog auto-revert.
  - Post Condition "dipulihkan ke state Pre-setup #13 dan #39" pada kedua TC tidak punya langkah observasi di TC; tidak diasersi, dipulihkan di hook `after`.
