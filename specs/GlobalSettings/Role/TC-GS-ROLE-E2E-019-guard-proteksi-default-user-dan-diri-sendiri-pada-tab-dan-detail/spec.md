---
id: TC-GS-ROLE-E2E-019-guard-proteksi-default-user-dan-diri-sendiri-pada-tab-dan-detail
title: "Guard Proteksi Default User dan Diri Sendiri pada Tab Total Control dan Detail"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-41
  - TC-GS-ROLE-42
  - TC-GS-ROLE-43
coverage:
  web: automated
---

# Guard Proteksi Default User dan Diri Sendiri pada Tab Total Control dan Detail

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data; hanya hover, klik pada checkbox yang terkunci, dan membuka overlay.
- Akun aktor pertama (login di hook `before`): Ahmad Fauzi (Total Control), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD` (Pre-setup #1). Akun kedua (ganti akun di langkah 50): Hendra Wijaya (Manage user and role C/R/U/D), `manageUserAndRoleCrud_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_ROLE_MANAGE_CRUD_PASSWORD` (Pre-setup #5). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`; env baru `GS_ROLE_MANAGE_CRUD_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE).
- Data Pre-setup (hanya dibaca): Ahmad Fauzi (Total Control) dan Hendra Wijaya masing-masing punya baris role Manage TAG (Pre-setup #1, #5); Budi Santoso (Default User, Total Control, Pre-setup #2); Dewi Lestari (Total Control, Inactive, Pre-setup #3); Siti Nurhaliza (Read Only, Active, punya baris Manage TAG, Pre-setup #4); Doni Pratama (Manage TAG R, Pre-setup #10). Detail "Manage TAG" memuat baris kelima user tersebut dan Hendra Wijaya; Tab Total Control memuat Ahmad Fauzi, Budi Santoso, dan Dewi Lestari.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: membuka Global Settings > Role & Permission > Tab Total Control.
- Hook `after`: mengembalikan sesi ke akun default suite (Ahmad Fauzi, `GS_TC_PASSWORD`) karena spec berakhir di akun Hendra Wijaya.
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: mengarahkan kursor ke checkbox disabled dan ke item overlay untuk membaca tooltip; mengamati request jaringan yang keluar dari halaman (langkah 46 dan 54); membaca ikon dan severity item overlay.

## Test Steps

### TC-GS-ROLE-41: Detail untuk aktor Total Control: baris diri sendiri, Default User, dan target TC/RO

1. Buka Detail "Manage TAG"
2. Arahkan kursor ke checkbox Update baris Ahmad Fauzi
3. Verifikasi checkbox Update baris Ahmad Fauzi tampil dan disabled
4. Verifikasi tooltip `You can't manage your own account from here.`
5. Arahkan kursor ke checkbox Remove baris Ahmad Fauzi
6. Verifikasi checkbox Remove baris Ahmad Fauzi tampil dan disabled
7. Verifikasi tooltip `You can't manage your own account from here.`
8. Arahkan kursor ke checkbox seleksi baris Ahmad Fauzi
9. Verifikasi checkbox seleksi baris Ahmad Fauzi tampil dan disabled
10. Verifikasi tooltip `You can't manage your own account from here.`
11. Arahkan kursor ke checkbox Update baris Budi Santoso
12. Verifikasi checkbox Update baris Budi Santoso disabled
13. Verifikasi tooltip `Default User cannot be modified.`
14. Arahkan kursor ke checkbox Remove baris Budi Santoso
15. Verifikasi checkbox Remove baris Budi Santoso disabled
16. Verifikasi tooltip `Default User cannot be modified.`
17. Arahkan kursor ke checkbox seleksi baris Budi Santoso
18. Verifikasi checkbox seleksi baris Budi Santoso disabled
19. Verifikasi tooltip `Default User cannot be modified.`
20. Arahkan kursor ke checkbox Update baris Dewi Lestari
21. Arahkan kursor ke checkbox Remove baris Dewi Lestari
22. Arahkan kursor ke checkbox seleksi baris Dewi Lestari
23. Verifikasi checkbox Update, Remove, dan checkbox seleksi baris Dewi Lestari (Total Control) enabled
24. Arahkan kursor ke checkbox Update baris Siti Nurhaliza
25. Arahkan kursor ke checkbox Remove baris Siti Nurhaliza
26. Arahkan kursor ke checkbox seleksi baris Siti Nurhaliza
27. Verifikasi checkbox Update, Remove, dan checkbox seleksi baris Siti Nurhaliza (Read Only) enabled

### TC-GS-ROLE-42: Remove di Tab Total Control untuk Default User dan diri sendiri

28. Buka Tab Total Control
29. Buka overlay (⋯) baris Budi Santoso
30. Arahkan kursor ke Remove
31. Verifikasi Remove tampil disabled
32. Verifikasi tooltip `Default User cannot be modified.`
33. Tekan Esc untuk menutup overlay
34. Buka overlay (⋯) baris Ahmad Fauzi
35. Arahkan kursor ke Remove
36. Verifikasi Remove tampil disabled
37. Verifikasi tooltip `You can't manage your own account from here.`
38. Tekan Esc untuk menutup overlay
39. Buka overlay (⋯) baris Dewi Lestari
40. Verifikasi Remove enabled
41. Verifikasi icon Remove `DeleteBin6Line` dengan severity danger
42. Tekan Esc untuk menutup overlay

### TC-GS-ROLE-43: Checkbox Read selalu checked dan terkunci untuk semua aktor

43. Buka Detail "Manage TAG"
44. Klik checkbox Read baris Doni Pratama
45. Verifikasi tidak ada toast
46. Verifikasi tidak ada request yang dikirim dari klik tersebut
47. Verifikasi checkbox Read baris Doni Pratama tetap checked
48. Arahkan kursor ke checkbox Read baris Doni Pratama
49. Verifikasi tooltip `Read access is required and can only be removed by removing the role.` untuk Ahmad Fauzi
50. Logout, lalu login sebagai Hendra Wijaya
51. Buka Detail "Manage TAG"
52. Klik checkbox Read baris Doni Pratama
53. Verifikasi tidak ada toast
54. Verifikasi tidak ada request yang dikirim dari klik tersebut
55. Verifikasi checkbox Read baris Doni Pratama tetap checked
56. Arahkan kursor ke checkbox Read baris Doni Pratama
57. Verifikasi tooltip `Read access is required and can only be removed by removing the role.` untuk Hendra Wijaya

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (41, 42, 43) dipertahankan; TC-GS-ROLE-43 terakhir karena memuat ganti akun ke Hendra Wijaya.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC sumber): menutup overlay dengan Esc (langkah 33, 38, 42), membuka Tab Total Control (langkah 28) dan Detail "Manage TAG" (langkah 43, 51), serta logout lalu login ke Hendra Wijaya (langkah 50). Langkah 20 sampai 22 dan 24 sampai 26 adalah hover yang dipakai TC-GS-ROLE-41 langkah 2 untuk baris Dewi Lestari dan Siti Nurhaliza; hasilnya diverifikasi per baris pada langkah 23 dan 27 karena Expected c TC memuat ketiga elemen sebagai satu klausa.
- Spec melewati sekitar 35 langkah (57 langkah) karena tiga TC guard dijalankan berurutan: blok hover per elemen dan per baris (langkah 2 sampai 27 dan 29 sampai 42) serta blok klik dan hover checkbox Read per aktor (langkah 43 sampai 49 dan 51 sampai 57) berpola sama. Semua blok satu kelas harness (fungsional, guard state disabled dan tooltip) dan berdiri sendiri: tiap blok membuka tab atau Detail sendiri; bagian sesudah ganti akun (langkah 51 sampai 57) tetap bermakna walau bagian sebelumnya gagal.
- Pembagian TC lintas spec: TC-GS-ROLE-44, 45, 46 (prioritas tooltip) ada di spec 020; TC-GS-ROLE-47, 48 (keyboard dan focus trap) ada di spec 021; TC-GS-ROLE-49, 50 (checkbox seleksi dan Select All) ada di spec 022.
- Temuan untuk QA:
  - TC-GS-ROLE-43 Expected a ("tidak ada request") membutuhkan kemampuan mengamati request jaringan; mekanismenya tidak didefinisikan di TC, PRD, atau LLD dan disediakan tim FE.
  - TC-GS-ROLE-43 langkah 4 ("Ulangi langkah 1-3 login sbg Hendra Wijaya") tidak menyebut logout; spec menulis ganti akun eksplisit (langkah 50).
  - TC-GS-ROLE-41 langkah 2 dan Expected c tidak menyebut tooltip untuk checkbox yang enabled; spec hanya memverifikasi state enabled.
