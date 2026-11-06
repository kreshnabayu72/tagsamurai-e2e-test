---
id: TC-FA-RP-E2E-376-assign-role-sama-pada-node-turunan-atau-induk-saat-overlap-diizinkan
title: "Assign role yang sama pada node turunan atau node induk saat penugasan overlap diizinkan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1208
  - TC-FA-RP-1209
coverage:
  web: automated
---

# Assign role yang sama pada node turunan atau node induk saat penugasan overlap diizinkan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #18 (pohon Group), #19 (Nadia Putri Asset Admin di `IT Infrastructure` sub-tab `Disposal`; `Data Center` tanpa baris manual), dan #17 (Joko Santoso, Home Group `IT Infrastructure`).
- Kondisi awal yang di-seed di hook `before` (precondition TC, tidak diasersi): Joko Santoso Asset Admin di `Data Center` sub-tab `Disposal`; Nadia Putri tanpa penugasan di `Data Center` dan Joko Santoso tanpa penugasan di `IT Infrastructure`. Seeding lewat kemampuan seeding API yang disediakan tim FE/BE (tanpa endpoint karangan).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: langkah 6 menambah baris Nadia Putri Asset Admin di `Data Center` dan langkah 17 menambah baris Joko Santoso Asset Admin di `IT Infrastructure`. Hook `after` menghapus kedua baris hasil Assign itu dan baris seed Joko Santoso di `Data Center` (tidak berasumsi langkah spec berhasil penuh) sehingga Pre-setup #19 kembali ke kondisi Tabel Data Uji Pre-setup TC. Entri Changelog yang tercatat tetap ada (audit trail permanen). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1208: Assign role yang sama pada node turunan saat ancestor memegangnya

1. Klik Tab `Transaction Role`, klik node `Data Center` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
2. Klik `[+ Assign]` pada section Asset Admin
3. Ketik Search `Nadia Putri`, tekan Enter
4. Verifikasi Nadia Putri ada di daftar picker
5. Centang Nadia Putri
6. Klik `[Assign]`
7. Verifikasi muncul toast sukses: `Success, Asset Admin has been assigned.`
8. Verifikasi tidak ada dialog konfirmasi
9. Verifikasi baris Nadia Putri tampil di section Asset Admin `Data Center`
10. Klik node `IT Infrastructure` di Sidebar Group Tree
11. Verifikasi baris Nadia Putri di section Asset Admin `IT Infrastructure` tetap ada dan tidak berubah

### TC-FA-RP-1209: Assign role yang sama pada node induk saat descendant memegangnya

12. Klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
13. Klik `[+ Assign]` pada section Asset Admin
14. Ketik Search `Joko Santoso`, tekan Enter
15. Verifikasi Joko Santoso ada di daftar picker
16. Centang Joko Santoso
17. Klik `[Assign]`
18. Verifikasi muncul toast sukses: `Success, Asset Admin has been assigned.`
19. Verifikasi tidak ada dialog konfirmasi
20. Verifikasi baris Joko Santoso tampil di section Asset Admin `IT Infrastructure`
21. Klik node `Data Center` di Sidebar Group Tree
22. Verifikasi baris Joko Santoso di section Asset Admin `Data Center` tetap ada dan tidak berubah

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 22 langkah.
- Langkah penghubung (S-03): langkah 1, 10, 12, dan 21 (navigasi Tab, node, sub-tab). Langkah 3 dan 14 adalah Search nama kandidat di picker (R-16, R-22): Search menemukan target di Table User Picker yang dapat memuat lebih dari satu halaman; popup ditutup oleh `[Assign]` sehingga Search tidak perlu dibersihkan.
- Langkah 7 dan 18 (toast sukses) menjadi anchor positif atas asersi absence dialog konfirmasi langkah 8 dan 19 (bagian 8b butir 2 dan 11). Dialog konfirmasi di sini adalah dialog apa pun (misalnya D-13) yang akan muncul bila penugasan dianggap penurunan atau penggantian tangga.
- Asersi pada TC ini adalah presence (baris tetap ada), bukan absence log; tidak ada asersi "tidak ada entri" (S-05). Pemulihan baris hasil Assign dilakukan hook `after` (S-06, S-11).
- Temuan untuk QA:
  - Hak efektif pada modul konsumen tidak teramati di surface ini (NC-11): Post Condition TC-FA-RP-1208 ("Nadia Putri memegang Asset Admin di dua node; hak efektif adalah gabungan penugasan") tidak punya langkah observasi dan tidak diasersi. Tidak ada asersi hak efektif di spec ini.
  - NC-19 / Open Item #8 (penugasan mencakup node beserta descendant, overlap diizinkan) belum dikonfirmasi PM; bila PM menetapkan lain, Expected 1208 dan 1209 usang.
  - "Tidak berubah" pada TC-FA-RP-1208.c dan 1209.c tidak mendefinisikan atribut yang dibandingkan; spec mengasersi baris user tetap tampil di section Asset Admin node itu.
  - Seed Joko Santoso hanya diperlukan untuk TC-FA-RP-1209. Home Group Joko Santoso (`IT Infrastructure`) sama dengan node tujuan Assign sehingga lolos gate constraint Role Transaksi (V-17/V-18); aktor sebelumnya (Gunawan Halim, Home Group `Data Center`) ditolak gate pada `IT Infrastructure` karena ancestor Home Group-nya. Spec tidak mengasersi gate itu (cakupan TC-FA-RP-1209 hanya overlap).
