---
id: TC-FA-RP-E2E-378-d13-hanya-pada-node-sama-dan-approver-ancestor-descendant-berdampingan
title: "Dialog D-13 hanya pada node yang sama dan Approver di ancestor dan descendant berdampingan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1212
  - TC-FA-RP-1213
coverage:
  web: automated
---

# Dialog D-13 hanya pada node yang sama dan Approver di ancestor dan descendant berdampingan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #18 (pohon Group) dan #19 (Nadia Putri Asset Admin dan Pandu Wijaya Approver di `IT Infrastructure` sub-tab `Disposal`; Pandu Wijaya hanya sub-tab `Disposal`; Require Approval OFF di semua node).
- Kondisi awal yang di-seed di hook `before` (precondition TC, tidak diasersi): Nadia Putri Asset Admin di `Data Center` sub-tab `Disposal`; Pandu Wijaya tanpa penugasan di `Data Center`; Require Approval `Disposal` OFF di semua node. Seeding lewat kemampuan seeding API yang disediakan tim FE/BE (tanpa endpoint karangan).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: langkah 5 mengganti baris Nadia Putri Asset Admin di `Data Center` menjadi Staff; langkah 19 menambah baris Pandu Wijaya Approver di `Data Center` dan langkah 25 menghapusnya. Hook `after` menghapus baris Nadia Putri di `Data Center` (Asset Admin dan Staff) dan baris Pandu Wijaya di `Data Center` bila masih ada (tidak berasumsi langkah spec berhasil penuh) sehingga Pre-setup #19 kembali ke kondisi Tabel Data Uji Pre-setup TC. Entri Changelog yang tercatat tetap ada (audit trail permanen). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1212: Dialog D-13 dan penggantian role hanya pada node yang sama

1. Klik Tab `Transaction Role`, klik node `Data Center` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
2. Klik `[+ Assign]` pada section Staff
3. Ketik Search `Nadia Putri`, tekan Enter
4. Centang Nadia Putri
5. Klik `[Assign]`
6. Verifikasi dialog severity warning: Title `Change Transaction Role`; Body diawali bullet `• Nadia P (currently Asset Admin)`, lalu `This will change their role for Disposal to Staff in Data Center.`, ditutup `Are you sure you want to change it?`; tombol `[Cancel]` dan `[Change]`
7. Verifikasi dialog tidak menyebut `IT Infrastructure`
8. Klik `[Change]`
9. Verifikasi muncul toast sukses: `Success, Staff has been assigned.`
10. Verifikasi Nadia Putri tampil di section Staff `Data Center`
11. Verifikasi Nadia Putri tidak lagi ada di section Asset Admin `Data Center`
12. Klik node `IT Infrastructure` di Sidebar Group Tree
13. Verifikasi Nadia Putri tetap di section Asset Admin `IT Infrastructure`

### TC-FA-RP-1213: Approver di ancestor dan descendant untuk user yang sama berdampingan

14. Klik node `Data Center` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
15. Klik `[+ Assign]` pada section Approver
16. Ketik Search `Pandu Wijaya`, tekan Enter
17. Verifikasi Pandu Wijaya ada di daftar picker
18. Centang Pandu Wijaya
19. Klik `[Assign]`
20. Verifikasi muncul toast sukses: `Success, Approver has been assigned.`
21. Verifikasi baris Pandu Wijaya tampil di section Approver `Data Center`
22. Klik `[⋯]` baris Pandu Wijaya lalu `Remove`
23. Verifikasi dialog severity danger `Remove Approver`: Body `• Pandu W` lalu `This user will no longer be assigned to this role for Data Center.`
24. Verifikasi dialog D-09 tidak tampil
25. Klik `[Remove]`
26. Verifikasi muncul toast sukses: `Success, Approver has been removed.`
27. Klik node `IT Infrastructure` di Sidebar Group Tree
28. Verifikasi baris Pandu Wijaya di section Approver `IT Infrastructure` tetap ada

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 28 langkah.
- Langkah penghubung (S-03): langkah 1, 12, 14, dan 27 (navigasi Tab, node, sub-tab); langkah 3 dan 16 adalah Search nama kandidat di picker (R-16, R-22): popup ditutup oleh `[Assign]` sehingga Search tidak perlu dibersihkan.
- Langkah 6 menjadi anchor positif atas asersi absence `IT Infrastructure` langkah 7 (bagian 8b butir 2 dan 11); langkah 9 menjadi anchor atas asersi absence langkah 11; langkah 23 menjadi anchor atas asersi absence dialog D-09 langkah 24.
- Urutan: TC-FA-RP-1213 menghapus baris Pandu Wijaya di `Data Center` dan diletakkan terakhir (S-10); baris Nadia Putri yang berubah pada TC-FA-RP-1212 tidak dibutuhkan TC-FA-RP-1213.
- Temuan untuk QA:
  - Pre-setup #19 baru: seed Pandu Wijaya hanya sub-tab `Disposal` (tanpa Approver manual di sub-tab lain); spec mengandalkan itu dan tidak men-seed sub-tab lain.
  - Copy dialog D-13 pada TC-FA-RP-1212 bertanda `copy usulan, PRD 12 #1` dan belum disetujui PM; Expected 1212.a ditulis sesuai TC. Langkah 7 ("dialog tidak menyebut `IT Infrastructure`") mengikuti klausa terakhir Expected 1212.a.
  - NC-19 / Open Item #8 (penugasan mencakup node beserta descendant, tangga hanya pada node yang sama) belum dikonfirmasi PM; bila PM menetapkan lain, Expected 1212 dan 1213 usang.
  - Hak efektif pada modul konsumen tidak teramati di surface ini (NC-11); tidak ada asersi hak efektif Nadia Putri atau Pandu Wijaya.
  - TC-FA-RP-1213 menyebut dialog `Remove Approver` "biasa ... tanpa D-09 karena toggle OFF"; teks D-09 tidak dikutip di TC, sehingga langkah 24 mengasersi ketiadaan dialog D-09 dengan anchor dialog Remove biasa (langkah 23).
