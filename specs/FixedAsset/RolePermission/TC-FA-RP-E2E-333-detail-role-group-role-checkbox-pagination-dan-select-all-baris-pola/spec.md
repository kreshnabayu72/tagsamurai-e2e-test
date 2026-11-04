---
id: TC-FA-RP-E2E-333-detail-role-group-role-checkbox-pagination-dan-select-all-baris-pola
title: "Detail Role Group Role: pagination 41 baris All Groups dan checkbox serta Select All dengan baris pola"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1177
  - TC-FA-RP-1178
coverage:
  web: automated
---

# Detail Role Group Role: pagination 41 baris All Groups dan checkbox serta Select All dengan baris pola

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.
- Data Pre-setup (Company Alpha): #39 (Detail Role Group Role `Manage files`, 41 baris pada `All Groups`: 6 baris non-pola dan 35 baris pola), #18 (pohon Group, tujuh node), #1 (Admin Utama, Default User), #3 (Rina Wulandari, Total Control), dan #12 (Maya Anggraeni, Read Only); Dewi Anggraini (Read Only, Pre-setup #4) dan Fitri Handayani (Pre-setup #16, #39). Seluruh data hanya dibaca; tidak ada aksi tulis. Identitas Pre-setup mengacu ke fixture `Fixture.fixedAssetRolePermission` (belum ada di repo, tanpa password; ditandai untuk tim FE).
- Baris non-pola Pre-setup #39: Ahmad Fauzi (`Data Center`), Budi Santoso (`Helpdesk`), Citra Lestari (`Head Office`), Dimas Pranata (`Data Center`), Endah Susanti (`Rack A1`), Fitri Handayani (`Dock 1`). Baris pola `Manage files`: Admin Utama, Siti Rahmawati, Rina Wulandari, Dewi Anggraini, dan Maya Anggraeni masing-masing pada tujuh group (35 baris). Node `Dock 1` memuat Fitri Handayani dan lima baris pola (6 baris).
- Ukuran halaman default 10 (pilihan 10, 25, 50, 100); ukuran halaman diubah ke 50 pada langkah 25 dan dikembalikan ke 10 pada langkah 27. Sort default Name A-Z.
- Kemampuan teknis (disediakan tim FE/BE): hover pada checkbox baris untuk membaca tooltip.
- Pemulihan: tidak ada perubahan data. State UI (ukuran halaman dan seleksi baris) dipulihkan oleh langkah 27 dan 46; Pre-setup #39 tidak diubah spec ini.

## Test Steps

### TC-FA-RP-1177: Pagination Detail Role Group Role: baris pola menambah jumlah baris `All Groups` menjadi 41 dan menggeser baris non-pola ke halaman berikutnya pada ukuran default 10

1. Klik Tab `System`
2. Klik Role Name `Manage files` pada section Group Role
3. Klik `All Groups` di Sidebar Group Tree
4. Verifikasi tabel terdiri dari 5 halaman pada ukuran halaman default 10
5. Verifikasi Sort default Name A-Z
6. Verifikasi halaman 1 berisi 10 baris
7. Verifikasi halaman 1 memuat Ahmad Fauzi, Budi Santoso, dan Citra Lestari
8. Pindah ke halaman 2
9. Verifikasi halaman 2 berisi 10 baris
10. Verifikasi halaman 2 memuat Dimas Pranata, Endah Susanti, dan Fitri Handayani
11. Pindah ke halaman 3
12. Verifikasi halaman 3 berisi 10 baris
13. Verifikasi halaman 3 tidak memuat baris non-pola
14. Pindah ke halaman 4
15. Verifikasi halaman 4 berisi 10 baris
16. Verifikasi halaman 4 tidak memuat baris non-pola
17. Pindah ke halaman 5
18. Verifikasi halaman 5 berisi 1 baris
19. Verifikasi halaman 5 tidak memuat baris non-pola
20. Klik node `Dock 1` di Sidebar Group Tree
21. Verifikasi node `Dock 1` menampilkan 6 baris: Fitri Handayani dan lima baris pola
22. Verifikasi 6 baris tampil pada satu halaman
23. Verifikasi tidak ada halaman 2 pada node `Dock 1`
24. Klik `All Groups` di Sidebar Group Tree
25. Ganti ukuran halaman menjadi 50
26. Verifikasi seluruh 41 baris tampil pada satu halaman
27. Ganti ukuran halaman kembali menjadi 10

### TC-FA-RP-1178: Detail Role Group Role: checkbox baris pola Default User dan baris sendiri Disabled, baris pola Total Control/Read Only dapat dicentang Total Control, dan Select All hanya memilih baris yang dapat dipilih

28. Klik menu Settings > Role & Permission di sidebar untuk mereset state halaman
29. Klik Tab `System`
30. Klik Role Name `Manage files` pada section Group Role
31. Klik node `Dock 1` di Sidebar Group Tree
32. Hover checkbox baris Admin Utama
33. Verifikasi checkbox baris pola Admin Utama (Default User) Disabled dengan tooltip `Default User cannot be modified.`
34. Hover checkbox baris Siti Rahmawati
35. Verifikasi checkbox baris pola Siti Rahmawati (baris sendiri) Disabled dengan tooltip `You can't manage your own account from here.`
36. Verifikasi checkbox baris pola Rina Wulandari (Total Control) Enabled
37. Verifikasi checkbox baris pola Dewi Anggraini (Read Only) Enabled
38. Verifikasi checkbox baris pola Maya Anggraeni (Read Only) Enabled
39. Verifikasi checkbox baris Fitri Handayani Enabled
40. Centang baris Fitri Handayani
41. Klik `Select All` pada Bulk Action Bar
42. Verifikasi counter Bulk Action Bar `4 Users selected`
43. Verifikasi keempat baris Enabled (Rina Wulandari, Dewi Anggraini, Maya Anggraeni, dan Fitri Handayani) tercentang
44. Verifikasi baris Admin Utama tidak tercentang
45. Verifikasi baris Siti Rahmawati tidak tercentang
46. Klik `Unselect All` pada Bulk Action Bar

## Notes

- Spec ini memuat 46 langkah. Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-1177, TC-FA-RP-1178). Subjudul `###` memetakan langkah ke id TC granular. Mode FE+BE; tidak ada intercept.
- Langkah penghubung (S-03): langkah 1 sampai 3 dan 29 sampai 31 (membuka Tab System, Detail Role, dan node; langkah TC 1 dan 2), langkah 8, 11, 14, dan 17 (pindah halaman; langkah TC 3), langkah 24 (kembali ke `All Groups`; langkah TC 5), langkah 27 (mengembalikan ukuran halaman ke 10), langkah 28 (klik ulang menu untuk mereset state sebelum blok TC kedua, S-09; klik sidebar mereset Search, Sort, dan Filter), langkah 40 (centang Fitri Handayani, langkah TC 5), dan langkah 46 (`Unselect All` memulihkan seleksi, S-09). Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah 6, 9, 12, 15, dan 18 (jumlah baris tiap halaman) juga menjadi anchor positif bagi asersi absence langkah 13, 16, dan 19 (butir 8b.2). Tooltip pada langkah 33 dan 35 diasersi sebelum langkah berikutnya yang mengubah state hover (butir 8b.5).
- Spec ini di atas 35 langkah (46 langkah, tanpa blok yang diulang). Alasan: kedua TC sama kelas (fungsional Edge), memakai akun, halaman Detail Role `Manage files`, dan dataset Pre-setup #39 yang sama, seluruhnya baca saja; jumlah langkah berasal dari `Verifikasi` per klausa Expected (S-01) yang tidak dapat digabung, bukan dari navigasi berulang. State antar blok dibersihkan oleh langkah 27, 28, dan 46, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Nomor cadangan 347 tidak dipakai.
- Pembagian TC: kedua TC hanya ada di spec ini.
- Temuan untuk QA:
  - TC-FA-RP-1177 langkah 5 mengganti ukuran halaman menjadi 50 tanpa langkah pemulihan, dan tidak menyebut apakah ukuran halaman tersimpan per akun; spec menambah langkah penghubung 27 yang mengembalikan ukuran halaman ke 10.
  - TC-FA-RP-1177 Expected a hanya menyebut isi halaman 1 dan 2; halaman 3 sampai 5 hanya dinyatakan "tidak memuat baris non-pola" tanpa nama baris. Urutan antar baris pola bernama sama (satu per group) tidak diasersi.
  - TC-FA-RP-1177 Expected b menyebut node `Dock 1` "tanpa halaman 2" tanpa menyebut bahwa halaman aktif kembali ke halaman 1 saat berpindah node dari halaman 5; spec mengikuti TC dan hanya mengasersi enam baris pada satu halaman.
  - TC-FA-RP-1178 Expected c menyatakan baris Admin Utama dan Siti Rahmawati "tidak pernah tercentang", sedangkan keadaan sementara selama klik `Select All` tidak teramati; spec hanya mengasersi keadaan akhir (langkah 44 dan 45). Klausa "Select All dan counter tidak menghitung baris Admin Utama dan Siti Rahmawati" hanya dapat diamati lewat counter `4 Users selected` (langkah 42): TC tidak menyebut label tombol `Select All` bila ikut menampilkan jumlah (seperti `Select All (N records)`), sehingga jumlah itu tidak diasersi.
  - TC-FA-RP-1178 Expected b menyebut Fitri Handayani Enabled, sedangkan Pre-setup #39 menyebut Fitri Handayani berstatus Pending Email Confirmation dan Temporary User Yes; spec mengikuti TC. Label tombol pemulihan seleksi (`Unselect All`) tidak disebut TC; spec memakai nama yang dipakai spec sibling (TC-FA-RP-288).
  - TC-FA-RP-1178 mencantumkan Pre-setup #1, #3, #12, #18, dan #39, sedangkan Dewi Anggraini (Pre-setup #4) tidak tercantum padahal baris polanya diasersi.
  - Email Admin Utama pada Pre-setup #39 tidak tertulis (Gap Spec di TC); baris Admin Utama diidentifikasi lewat nama tampil.
  - Pernyataan Pre-setup bersama di `suite.md` menyebut data tabel #36 sampai #42 sehingga #39 tercakup, tetapi 41 baris `All Groups` dan lima baris pola `Manage files` tidak disebut eksplisit; pemulihannya dijamin tim FE/BE (spec ini tidak mengubah #39).
