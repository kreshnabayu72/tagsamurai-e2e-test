---
id: TC-FA-RP-E2E-377-assign-tangga-rendah-atau-tinggi-di-node-turunan-tidak-menyentuh-ancestor
title: "Assign role tangga lebih rendah atau lebih tinggi di node turunan tidak mengurangi atau menggantikan penugasan ancestor"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1210
  - TC-FA-RP-1211
coverage:
  web: automated
---

# Assign role tangga lebih rendah atau lebih tinggi di node turunan tidak mengurangi atau menggantikan penugasan ancestor

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #18 (pohon Group) dan #19 (Nadia Putri Asset Admin, Oscar Pratama Monitoring & Report, Putri Wulandari Staff di `IT Infrastructure` sub-tab `Disposal`; `Data Center` tanpa baris manual).
- Kondisi awal yang di-seed di hook `before` (precondition TC, tidak diasersi): Nadia Putri, Oscar Pratama, dan Putri Wulandari tanpa penugasan apa pun di `Data Center`. Seeding lewat kemampuan seeding API yang disediakan tim FE/BE (tanpa endpoint karangan).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: langkah 5 menambah baris Nadia Putri Monitoring & Report di `Data Center` dan langkah 19 menambah baris Oscar Pratama dan Putri Wulandari Asset Admin di `Data Center`. Hook `after` menghapus ketiga baris di `Data Center` itu (tidak berasumsi langkah spec berhasil penuh) sehingga Pre-setup #19 kembali ke kondisi Tabel Data Uji Pre-setup TC. Entri Changelog yang tercatat tetap ada (audit trail permanen). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1210: Assign role tangga lebih rendah pada node turunan (klausa a dan b)

1. Klik Tab `Transaction Role`, klik node `Data Center` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
2. Klik `[+ Assign]` pada section Monitoring & Report
3. Ketik Search `Nadia Putri`, tekan Enter
4. Centang Nadia Putri
5. Klik `[Assign]`
6. Verifikasi muncul toast sukses: `Success, Monitoring & Report has been assigned.`
7. Verifikasi dialog `Change Transaction Role` tidak tampil
8. Verifikasi Nadia Putri tampil di section Monitoring & Report `Data Center`
9. Klik node `IT Infrastructure` di Sidebar Group Tree
10. Verifikasi Nadia Putri tetap di section Asset Admin `IT Infrastructure`
11. Verifikasi Oscar Pratama tampil di section Monitoring & Report `IT Infrastructure`
12. Verifikasi Nadia Putri tidak ada di section Monitoring & Report `IT Infrastructure`

### TC-FA-RP-1211: Assign role tangga lebih tinggi pada node turunan (klausa a dan b)

13. Klik node `Data Center` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
14. Klik `[+ Assign]` pada section Asset Admin
15. Ketik Search `Oscar Pratama`, tekan Enter
16. Centang Oscar Pratama
17. Ganti isi kotak search dengan `Putri Wulandari`, tekan Enter
18. Centang Putri Wulandari
19. Klik `[Assign]`
20. Verifikasi muncul satu toast sukses: `Success, Asset Admin has been assigned.`
21. Verifikasi dialog konfirmasi tidak tampil
22. Verifikasi Oscar Pratama dan Putri Wulandari tampil di section Asset Admin `Data Center`
23. Klik node `IT Infrastructure` di Sidebar Group Tree
24. Verifikasi Oscar Pratama tetap di section Monitoring & Report `IT Infrastructure`
25. Verifikasi Putri Wulandari tetap di section Staff `IT Infrastructure`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 25 langkah.
- Pembagian TC lintas spec (S-05): TC-FA-RP-1210 dan TC-FA-RP-1211 muncul di `sourceTc` spec ini dan spec 383. Spec ini memuat klausa a dan b (presence). Klausa c kedua TC (Changelog: entri `Assign` dan tidak ada entri `Remove` untuk baris ancestor) ada di spec 383 beserta baseline dan anchor positifnya; spec ini tidak mengasersi isi Changelog.
- Langkah penghubung (S-03): langkah 1, 9, 13, dan 23 (navigasi Tab, node, sub-tab). Langkah 3, 15, dan 17 adalah Search nama kandidat di picker (R-16, R-22): Search menemukan target di Table User Picker yang dapat memuat lebih dari satu halaman; popup ditutup oleh `[Assign]` sehingga Search tidak perlu dibersihkan.
- Langkah 6 dan 20 (toast sukses) menjadi anchor positif atas asersi absence dialog langkah 7 dan 21. Langkah 11 (Oscar Pratama tampil) menjadi anchor positif atas asersi absence langkah 12 pada section yang sama.
- Pemulihan baris hasil Assign di `Data Center` dilakukan hook `after` (S-06, S-11).
- Temuan untuk QA:
  - Hak efektif pada modul konsumen tidak teramati di surface ini (NC-11): Post Condition TC-FA-RP-1210 ("rung tertinggi efektif pada `Data Center` tetap Asset Admin") dan TC-FA-RP-1211 tidak punya langkah observasi dan tidak diasersi. Tidak ada asersi hak efektif di spec ini.
  - NC-19 / Open Item #8 (penugasan mencakup node beserta descendant, tangga tidak melintasi node) belum dikonfirmasi PM; bila PM menetapkan lain, Expected 1210 dan 1211 usang.
  - TC-FA-RP-1211 langkah 2 mencentang dua user dalam satu popup tanpa menyebut Search; spec memakai Search per nama (R-22) dan mengandalkan seleksi yang dipertahankan di picker antar Search. Bila picker mereset seleksi saat Search diganti, langkah 17 dan 18 perlu disesuaikan.
