---
id: TC-GS-ROLE-E2E-046-bulk-remove-dialog-screening-dan-cancel
title: "Bulk Remove: Screening Dialog Konfirmasi dan Cancel Mempertahankan Seleksi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-126
  - TC-GS-ROLE-127
  - TC-GS-ROLE-129
  - TC-GS-ROLE-130
coverage:
  web: automated
---

# Bulk Remove: Screening Dialog Konfirmasi dan Cancel Mempertahankan Seleksi

## Prerequisites

- Mode: FE+BE.
- Akun aktor (login di hook `before`): Total Control, Ahmad Fauzi, `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), password `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD` (sudah terdaftar). Tidak ada env baru.
- Layar awal (hook `beforeEach`): Global Settings > Role & Permission > System > Detail `Manage hardware`. Blok TC-GS-ROLE-129 dan TC-GS-ROLE-130 berpindah ke Detail `Manage master reference` lewat langkah 28.
- Data Pre-setup yang dipakai (Tabel Data Uji Pre-setup): Nina Kartika dan Wawan Setiawan (baris 11, kandidat tanpa access level), Agus Salim (baris 9, user tanpa role), Siti Nurhaliza dan Rina Putri (baris 4, Read Only).
- Given (hook `before`, lewat seeding API; dipakai sebagai precondition TC, tidak diasersi selain tampilan dialog):
  - Detail `Manage hardware`: Nina Kartika dan Agus Salim punya baris Manage hardware, tanpa access level (precondition TC-GS-ROLE-126 dan Given TC-GS-ROLE-127).
  - Detail `Manage master reference`: Wawan Setiawan (tanpa access level), Rina Putri (Read Only; di-assign ulang Read Only bila sudah kehilangan Read Only, Tabel Data Uji Dinamis baris 14), dan Siti Nurhaliza (Total Control, hasil upgrade setara TC-GS-ROLE-60) punya baris Manage master reference.
- Spec tidak menjalankan Remove: semua dialog ditutup dengan `[Cancel]`, sehingga tidak ada baris yang terhapus dan tidak ada toast.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): hapus baris Manage hardware milik Nina Kartika dan Agus Salim; hapus baris Manage master reference milik Wawan Setiawan, Rina Putri, dan Siti Nurhaliza; lalu kembalikan Siti Nurhaliza dan Rina Putri ke Read Only (state Pre-setup baris 4; baris Manage TAG keduanya tidak disentuh). Last Updated baris Pre-setup yang disentuh seeding berubah dan tidak dipulihkan.
- Kemampuan teknis: mengarahkan kursor (hover) ke komponen user di body dialog; membaca teks body dialog; membaca centang baris dan Bulk Action Bar. Dialog dan overlay Bulk Action memakai komponen yang sama pada kedua Detail.
- Kemampuan teknis (seeding): seeding API untuk akses level, baris role, dan data user disediakan tim FE/BE; nama endpoint tidak disebut di TC dan PRD dan tidak dikarang di spec.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-GS-ROLE-126: Screening dialog Bulk Remove tanpa baris Total Control/Read Only

1. Centang baris `Nina Kartika`
2. Centang baris `Agus Salim`
3. Klik `Bulk Action`
4. Verifikasi overlay Bulk Action berisi `Remove` (ikon DeleteBin6Line, danger)
5. Klik `Remove`
6. Verifikasi Title dialog `Remove Access`
7. Verifikasi body dialog memuat bullet `• Nina K` dan `• Agus S`, masing-masing berupa komponen user (ikon user generik + first name + inisial last name)
8. Arahkan kursor ke `Nina K`
9. Verifikasi hover pada `Nina K` menampilkan nama lengkap `Nina Kartika`
10. Arahkan kursor ke `Agus S`
11. Verifikasi hover pada `Agus S` menampilkan nama lengkap `Agus Salim`
12. Verifikasi body dialog memuat kalimat `Are you sure you want to remove them? This action cannot be undone.`
13. Verifikasi tombol `[Cancel]` dan `[Remove]` (danger) tampil
14. Klik `[Cancel]`
15. Hapus centang baris `Nina Kartika`
16. Hapus centang baris `Agus Salim`

### TC-GS-ROLE-127: Cancel dialog Bulk Remove mempertahankan seleksi

17. Centang baris `Nina Kartika`
18. Centang baris `Agus Salim`
19. Klik `Bulk Action`
20. Klik `Remove`
21. Klik `[Cancel]`
22. Verifikasi toast tidak tampil
23. Verifikasi baris `Nina Kartika` dan `Agus Salim` tetap tampil di Detail `Manage hardware` (tidak ada baris terhapus)
24. Verifikasi baris `Nina Kartika` dan `Agus Salim` tetap tercentang
25. Verifikasi Bulk Action Bar tetap tampil
26. Hapus centang baris `Nina Kartika`
27. Hapus centang baris `Agus Salim`
28. Buka Tab System, lalu klik role `Manage master reference` untuk membuka Detail-nya

### TC-GS-ROLE-129: Screening dialog Bulk Remove dengan satu baris Read Only

29. Centang baris `Wawan Setiawan`
30. Centang baris `Rina Putri`
31. Klik `Bulk Action`
32. Klik `Remove`
33. Verifikasi Title dialog `Remove Access`
34. Verifikasi body dialog memuat bullet `• Wawan S` dan `• Rina P`, masing-masing berupa komponen user (ikon user generik + first name + inisial last name)
35. Verifikasi bullet `Rina P` diberi label `Read Only`
36. Arahkan kursor ke `Wawan S`
37. Verifikasi hover pada `Wawan S` menampilkan nama lengkap `Wawan Setiawan`
38. Arahkan kursor ke `Rina P`
39. Verifikasi hover pada `Rina P` menampilkan nama lengkap `Rina Putri`
40. Verifikasi body dialog memuat kalimat `The user marked above will lose their Read Only access as a result.`
41. Verifikasi body dialog memuat kalimat `This action cannot be undone. Are you sure you want to remove them?`
42. Verifikasi tombol `[Cancel]` dan `[Remove]` (danger) tampil
43. Klik `[Cancel]`
44. Hapus centang baris `Wawan Setiawan`
45. Hapus centang baris `Rina Putri`

### TC-GS-ROLE-130: Screening dialog Bulk Remove dengan baris Total Control dan Read Only

46. Centang baris `Siti Nurhaliza`
47. Centang baris `Rina Putri`
48. Klik `Bulk Action`
49. Klik `Remove`
50. Verifikasi body dialog memuat bullet `• Siti N` diberi label `Total Control`, berupa komponen user (ikon user generik + first name + inisial last name)
51. Verifikasi body dialog memuat bullet `• Rina P` diberi label `Read Only`, berupa komponen user (ikon user generik + first name + inisial last name)
52. Arahkan kursor ke `Siti N`
53. Verifikasi hover pada `Siti N` menampilkan nama lengkap `Siti Nurhaliza`
54. Arahkan kursor ke `Rina P`
55. Verifikasi hover pada `Rina P` menampilkan nama lengkap `Rina Putri`
56. Verifikasi body dialog memuat kalimat `The users marked above will lose their Total Control/Read Only access as a result.`
57. Verifikasi body dialog memuat kalimat `This action cannot be undone. Are you sure you want to remove them?`
58. Verifikasi tombol `[Cancel]` dan `[Remove]` (danger) tampil
59. Klik `[Cancel]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): `[Cancel]` yang menutup dialog TC-GS-ROLE-126, 129, dan 130 (langkah 14, 43, 59; `[Cancel]` pada TC-GS-ROLE-127 adalah langkah TC), hapus centang baris sebelum blok berikutnya (langkah 15, 16, 26, 27, 44, 45), dan berpindah ke Detail `Manage master reference` (langkah 28).
- Spec melewati sekitar 35 langkah (59 langkah) karena empat TC menguji dialog Bulk Remove yang sama pada dua Detail dengan pasangan baris berbeda, dan tiap klausa Expected (judul, bullet komponen user, label tier, hover nama lengkap tiap bullet, kalimat konfirmasi, tombol) menjadi satu `Verifikasi` (S-01). Semua blok satu kelas harness (fungsional), satu aktor, tanpa aksi yang mengubah data; tiap blok berdiri sendiri (seleksi dibuat ulang dan dibersihkan) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber diubah: TC-GS-ROLE-126 dan TC-GS-ROLE-127 (Detail `Manage hardware`) dijalankan lebih dulu, lalu TC-GS-ROLE-129 dan TC-GS-ROLE-130 (Detail `Manage master reference`), sehingga hanya ada satu perpindahan Detail.
- Temuan untuk QA:
  - TC-GS-ROLE-126 menulis kalimat `Are you sure you want to remove them? This action cannot be undone.`, sedangkan TC-GS-ROLE-129 dan 130 menulis `This action cannot be undone. Are you sure you want to remove them?` (urutan kalimat berbeda untuk dialog yang sama); spec mengikuti masing-masing TC.
  - TC-GS-ROLE-126 (precondition) dan TC-GS-ROLE-127 (Given lewat `[+ Assign]`) menyatakan state yang sama (Nina Kartika dan Agus Salim punya baris Manage hardware); spec menyiapkannya sekali di hook `before`.
  - TC-GS-ROLE-130 tidak menyebut Title dialog, sehingga Title tidak diasersi pada blok itu.
