---
id: TC-FA-RP-E2E-366-submit-campuran-tiga-dialog-d13-d04-d05-assign-role-transaksi
title: "Submit campuran target Standard turun tangga, Total Control, dan Group Manager: tiga dialog berurutan D-13, D-04, D-05; Cancel pada dialog terakhir membatalkan seluruh Submit"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1193
coverage:
  web: automated
---

# Submit campuran target Standard turun tangga, Total Control, dan Group Manager: tiga dialog berurutan D-13, D-04, D-05; Cancel pada dialog terakhir membatalkan seluruh Submit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #3 (Rina Wulandari, Total Control kedua; target Total Control), #13 (Kevin Susanto, Group Manager hanya di `Data Center`; target Group Manager), #18 (pohon Group), #19 (seed Role Transaksi sub-tab `Disposal`). Precondition TC: Nadia Putri (Standard) memegang Asset Admin pada `Data Center` sub-tab `Disposal`; disiapkan lewat seed API di hook `before`.
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: langkah 41 menetapkan Nadia Putri, Rina Wulandari, dan Kevin Susanto sebagai Monitoring & Report `Disposal` di `Data Center`, melepas tingkat akses Total Control Rina Wulandari (beserta baris polanya), dan melepas penugasan Group Manager Kevin Susanto (baris pola GM dipertahankan sebagai penugasan biasa, kecuali baris Asset Admin `Data Center` yang digantikan Monitoring & Report oleh aksi pemicu). Hook `after` memulihkan Nadia Putri, Rina Wulandari, dan Kevin Susanto ke state Pre-setup #19, #3, dan #13 lewat fixture backend yang disediakan tim FE/BE (TC: "dipulihkan ke state Pre-setup #19, #3, dan #13 oleh automation baseline"), tidak berasumsi langkah spec berhasil penuh. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1193: Submit campuran, jalur Cancel pada dialog ketiga

1. Klik Tab `Transaction Role`
2. Klik node `Data Center` pada Sidebar Group Tree
3. Klik sub-tab `Disposal`
4. Klik `[+ Assign]` pada section Monitoring & Report
5. Ketik Search `Nadia Putri`, tekan Enter
6. Centang Nadia Putri
7. Ganti isi kotak search dengan `Rina Wulandari`, tekan Enter
8. Centang Rina Wulandari
9. Ganti isi kotak search dengan `Kevin Susanto`, tekan Enter
10. Centang Kevin Susanto
11. Klik `[Assign]`
12. Verifikasi dialog pertama `D-13` severity warning: Title `Change Transaction Role`; bullet `• Nadia P (currently Asset Admin)` saja (Rina dan Kevin tidak didaftar), `This will change their role for Disposal to Monitoring & Report in Data Center.`, `Are you sure you want to change it?`; tombol `[Cancel]` dan `[Change]` (copy usulan, PRD 12 #1)
13. Klik `[Change]`
14. Verifikasi dialog kedua `D-04` varian Role Transaksi hanya untuk `• Rina W` (Title `Remove Total Control`, tombol `[Cancel]` dan `[Remove]`; copy usulan, PRD 12 #1), tidak digabung dengan dialog pertama
15. Klik `[Remove]`
16. Verifikasi dialog ketiga `D-05` varian Role Transaksi hanya untuk `• Kevin S` (Title `Remove Group Manager`; Body `This change will remove Group Manager status for this group.` lalu `Their other role assignments will remain as they are.` dan `Are you sure you want to remove it?`; tombol `[Cancel]` dan `[Remove]`; copy usulan, PRD 12 #7)
17. Klik `[Cancel]`
18. Verifikasi ketiga dialog tertutup
19. Verifikasi tidak ada toast
20. Verifikasi Nadia Putri tetap tampil di section Asset Admin pada `Data Center` sub-tab `Disposal`
21. Klik Tab `Total Control`
22. Verifikasi Rina Wulandari tetap tampil di Tab `Total Control`
23. Klik Tab `Group Manager`
24. Verifikasi Kevin Susanto tetap tampil di Tab `Group Manager`

### TC-FA-RP-1193: Submit campuran, jalur Confirm pada dialog ketiga

25. Klik Tab `Transaction Role`
26. Klik node `Data Center` pada Sidebar Group Tree
27. Klik sub-tab `Disposal`
28. Klik `[+ Assign]` pada section Monitoring & Report
29. Ketik Search `Nadia Putri`, tekan Enter
30. Centang Nadia Putri
31. Ganti isi kotak search dengan `Rina Wulandari`, tekan Enter
32. Centang Rina Wulandari
33. Ganti isi kotak search dengan `Kevin Susanto`, tekan Enter
34. Centang Kevin Susanto
35. Klik `[Assign]`
36. Verifikasi dialog pertama `D-13` muncul lebih dulu (Title `Change Transaction Role`)
37. Klik `[Change]`
38. Verifikasi dialog kedua `D-04` muncul sesudah dialog pertama (Title `Remove Total Control`)
39. Klik `[Remove]`
40. Verifikasi dialog ketiga `D-05` muncul sesudah dialog kedua (Title `Remove Group Manager`)
41. Klik `[Remove]` pada dialog ketiga
42. Verifikasi Nadia Putri, Rina Wulandari, dan Kevin Susanto tampil di section Monitoring & Report pada `Data Center` sub-tab `Disposal`
43. Verifikasi sedikitnya satu baris lain tampil di section Asset Admin pada `Data Center`
44. Verifikasi Kevin Susanto tidak lagi tampil di section Asset Admin pada `Data Center` (digantikan Monitoring & Report oleh aksi pemicu)
45. Verifikasi baris Approver Kevin Susanto tetap tampil di section Approver pada `Data Center` (baris pola dipertahankan)
46. Klik Tab `Total Control`
47. Verifikasi sedikitnya satu baris Total Control lain tampil di Tab `Total Control`
48. Verifikasi Rina Wulandari tidak lagi ada di Tab `Total Control`
49. Klik Tab `Group Manager`
50. Verifikasi sedikitnya satu baris Group Manager lain tampil di Tab `Group Manager`
51. Verifikasi Kevin Susanto tidak lagi ada di Tab `Group Manager`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular (satu TC, dua jalur: Cancel lalu Confirm; langkah TC "Ulangi langkah 2 sampai 4" ditulis utuh pada langkah 25 sampai 41, S-04). Spec ini memuat 51 langkah.
- Alasan di atas sekitar 35 langkah (51 langkah): satu TC, satu alur Submit campuran dengan dua jalur (Cancel lalu Confirm) pada target dan state yang sama; jalur Confirm bermakna hanya bila jalur Cancel membuktikan tidak ada penugasan yang bocor, dan keduanya satu kelas fungsional. Tiga pemilihan kandidat (Search lalu centang, tiga kali per jalur) dan tiga dialog berurutan per jalur membuat langkah tidak dapat dipadatkan tanpa menghilangkan butir Expected.
- Langkah penghubung (S-03): langkah 1 sampai 4, 21, 23, dan 25 sampai 28 (navigasi Tab, node, sub-tab, popup Assign), langkah 5 sampai 10 dan 29 sampai 34 (pemilihan kandidat lewat Search di popup Assign, R-16 dan R-23; asumsi seleksi tetap terbawa saat isi kotak search diganti, lihat Temuan untuk QA), langkah 43, 47, dan 50 adalah `Verifikasi` pembanding sebagai anchor absence atas langkah 44, 48, dan 51 (bagian 8b butir 2). Langkah 12, 14, dan 16 menjadi anchor positif atas asersi langkah 18 dan 19; langkah 36, 38, dan 40 mengasersi urutan dialog jalur Confirm.
- Tanpa Search pada section role dan Tab `Total Control`: masing-masing memuat paling banyak sepuluh baris, dalam satu halaman.
- Pembagian TC lintas spec: TC-FA-RP-1191 (Assign Staff ke target Group Manager, satu dialog D-05) ada di spec 356.
- Fix pass 4 (keputusan: auto-revert GM mempertahankan baris): hanya baris Asset Admin Kevin Susanto di `Data Center` yang digantikan Monitoring & Report oleh aksi pemicu; baris Approver `Data Center` dan baris pola GM lainnya dipertahankan. Copy D-05 Role Transaksi penutup `Their other role assignments will remain as they are.`
- Temuan untuk QA:
  - TC-FA-RP-1193 menandai copy dialog D-13 dan D-04 sebagai `copy usulan, PRD 12 #1` dan D-05 sebagai `copy usulan, PRD 12 #7`; spec menulis teks TC apa adanya.
  - TC tidak menyebut apakah seleksi kandidat tetap terbawa saat isi kotak search popup Assign diganti; spec mengasumsikan ya (langkah 7, 9, 31, 33).
  - Post Condition "satu notifikasi ke Rina Wulandari dan satu ke Kevin Susanto" tidak punya langkah observasi di TC; tidak diasersi. Post Condition pemulihan Nadia Putri, Rina Wulandari, dan Kevin Susanto juga tidak diasersi; dipulihkan di hook `after`.
  - Expected d "baris pola GM lainnya tetap ada" tidak merinci sub-tab dan role; spec menelusuri section Asset Admin dan Approver `Data Center` sub-tab `Disposal` saja.
  - Seed Kevin Susanto tidak konsisten antar sumber: Pre-setup #13 dan #43 hanya `Data Center`, Pre-setup #38 dan beberapa TC lain `Data Center` dan `Helpdesk`. Spec mengikuti #13.
  - Pre-setup #3 (Rina Wulandari) adalah Total Control kedua yang juga dipakai sebagai akun aktor kedua suite (`FA_TC2_PASSWORD`); spec ini tidak login sebagai Rina Wulandari.
