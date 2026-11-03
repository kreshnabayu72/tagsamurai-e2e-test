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
- Akun aktor pertama (login di hook `before`): Ahmad Fauzi (Total Control), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD` (Pre-setup #1). Akun kedua (ganti akun di langkah 62): Hendra Wijaya (Manage user and role C/R/U/D), `manageUserAndRoleCrud_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_ROLE_MANAGE_CRUD_PASSWORD` (Pre-setup #5). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`; env baru `GS_ROLE_MANAGE_CRUD_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE).
- Data Pre-setup (hanya dibaca): Ahmad Fauzi (Total Control) dan Hendra Wijaya masing-masing punya baris role Manage TAG (Pre-setup #1, #5); Budi Santoso (Default User, Total Control, Pre-setup #2); Dewi Lestari (Total Control, Inactive, Pre-setup #3); Siti Nurhaliza (Read Only, Active, punya baris Manage TAG, Pre-setup #4); Doni Pratama (Manage TAG R, Pre-setup #10). Detail "Manage TAG" memuat baris kelima user tersebut dan Hendra Wijaya; Tab Total Control memuat Ahmad Fauzi, Budi Santoso, dan Dewi Lestari.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: membuka Global Settings > Role & Permission > Tab Total Control.
- Hook `after`: mengembalikan sesi ke akun default suite (Ahmad Fauzi, `GS_TC_PASSWORD`) karena spec berakhir di akun Hendra Wijaya.
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: membuka overlay (⋯) pada baris Detail; mengarahkan kursor ke checkbox disabled dan ke item overlay untuk membaca tooltip; mengamati request jaringan yang keluar dari halaman (langkah 58 dan 66); membaca ikon dan severity item overlay.

## Test Steps

### TC-GS-ROLE-41: Detail untuk aktor Total Control: baris diri sendiri, Default User, dan target TC/RO

1. Buka Detail "Manage TAG"
2. Arahkan kursor ke checkbox Update baris Ahmad Fauzi
3. Verifikasi checkbox Update baris Ahmad Fauzi tampil dan disabled
4. Verifikasi tooltip `You can't manage your own account from here.`
5. Buka overlay (⋯) baris Ahmad Fauzi
6. Arahkan kursor ke item Remove
7. Verifikasi item Remove baris Ahmad Fauzi tampil dan disabled
8. Verifikasi tooltip `You can't manage your own account from here.`
9. Tekan Esc untuk menutup overlay
10. Arahkan kursor ke checkbox seleksi baris Ahmad Fauzi
11. Verifikasi checkbox seleksi baris Ahmad Fauzi tampil dan disabled
12. Verifikasi tooltip `You can't manage your own account from here.`
13. Arahkan kursor ke checkbox Update baris Budi Santoso
14. Verifikasi checkbox Update baris Budi Santoso disabled
15. Verifikasi tooltip `Default User cannot be modified.`
16. Buka overlay (⋯) baris Budi Santoso
17. Arahkan kursor ke item Remove
18. Verifikasi item Remove baris Budi Santoso disabled
19. Verifikasi tooltip `Default User cannot be modified.`
20. Tekan Esc untuk menutup overlay
21. Arahkan kursor ke checkbox seleksi baris Budi Santoso
22. Verifikasi checkbox seleksi baris Budi Santoso disabled
23. Verifikasi tooltip `Default User cannot be modified.`
24. Arahkan kursor ke checkbox Update baris Dewi Lestari
25. Verifikasi checkbox Update baris Dewi Lestari (Total Control) enabled
26. Buka overlay (⋯) baris Dewi Lestari
27. Arahkan kursor ke item Remove
28. Verifikasi item Remove baris Dewi Lestari (Total Control) enabled
29. Tekan Esc untuk menutup overlay
30. Arahkan kursor ke checkbox seleksi baris Dewi Lestari
31. Verifikasi checkbox seleksi baris Dewi Lestari (Total Control) enabled
32. Arahkan kursor ke checkbox Update baris Siti Nurhaliza
33. Verifikasi checkbox Update baris Siti Nurhaliza (Read Only) enabled
34. Buka overlay (⋯) baris Siti Nurhaliza
35. Arahkan kursor ke item Remove
36. Verifikasi item Remove baris Siti Nurhaliza (Read Only) enabled
37. Tekan Esc untuk menutup overlay
38. Arahkan kursor ke checkbox seleksi baris Siti Nurhaliza
39. Verifikasi checkbox seleksi baris Siti Nurhaliza (Read Only) enabled

### TC-GS-ROLE-42: Remove di Tab Total Control untuk Default User dan diri sendiri

40. Buka Tab Total Control
41. Buka overlay (⋯) baris Budi Santoso
42. Arahkan kursor ke Remove
43. Verifikasi Remove tampil disabled
44. Verifikasi tooltip `Default User cannot be modified.`
45. Tekan Esc untuk menutup overlay
46. Buka overlay (⋯) baris Ahmad Fauzi
47. Arahkan kursor ke Remove
48. Verifikasi Remove tampil disabled
49. Verifikasi tooltip `You can't manage your own account from here.`
50. Tekan Esc untuk menutup overlay
51. Buka overlay (⋯) baris Dewi Lestari
52. Verifikasi Remove enabled
53. Verifikasi icon Remove `DeleteBin6Line` dengan severity danger
54. Tekan Esc untuk menutup overlay

### TC-GS-ROLE-43: Checkbox Read selalu checked dan terkunci untuk semua aktor

55. Buka Detail "Manage TAG"
56. Klik checkbox Read baris Doni Pratama
57. Verifikasi tidak ada toast
58. Verifikasi tidak ada request yang dikirim dari klik tersebut
59. Verifikasi checkbox Read baris Doni Pratama tetap checked
60. Arahkan kursor ke checkbox Read baris Doni Pratama
61. Verifikasi tooltip `Read access is required and can only be removed by removing the role.` untuk Ahmad Fauzi
62. Logout, lalu login sebagai Hendra Wijaya
63. Buka Detail "Manage TAG"
64. Klik checkbox Read baris Doni Pratama
65. Verifikasi tidak ada toast
66. Verifikasi tidak ada request yang dikirim dari klik tersebut
67. Verifikasi checkbox Read baris Doni Pratama tetap checked
68. Arahkan kursor ke checkbox Read baris Doni Pratama
69. Verifikasi tooltip `Read access is required and can only be removed by removing the role.` untuk Hendra Wijaya

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (41, 42, 43) dipertahankan; TC-GS-ROLE-43 terakhir karena memuat ganti akun ke Hendra Wijaya.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC sumber): membuka overlay (⋯) pada baris Detail untuk menjangkau item Remove (langkah 5, 16, 26, 34) dan menutupnya dengan Esc (langkah 9, 20, 29, 37), menutup overlay Tab Total Control dengan Esc (langkah 45, 50, 54), membuka Tab Total Control (langkah 40) dan Detail "Manage TAG" (langkah 55, 63), serta logout lalu login ke Hendra Wijaya (langkah 62). Untuk baris Dewi Lestari dan Siti Nurhaliza, hover checkbox Update (langkah 24, 32), item Remove (langkah 27, 35), dan checkbox seleksi (langkah 30, 38) masing-masing diverifikasi enabled karena Expected c TC memuat ketiga elemen sebagai satu klausa.
- Spec melewati sekitar 35 langkah (69 langkah) karena tiga TC guard dijalankan berurutan: blok hover per elemen dan per baris (langkah 2 sampai 39 dan 41 sampai 54) serta blok klik dan hover checkbox Read per aktor (langkah 55 sampai 61 dan 63 sampai 69) berpola sama. Semua blok satu kelas harness (fungsional, guard state disabled dan tooltip) dan berdiri sendiri: tiap blok membuka tab atau Detail sendiri; bagian sesudah ganti akun (langkah 63 sampai 69) tetap bermakna walau bagian sebelumnya gagal.
- Pembagian TC lintas spec: TC-GS-ROLE-44, 45, 46 (prioritas tooltip) ada di spec 020; TC-GS-ROLE-47, 48 (keyboard dan focus trap) ada di spec 021; TC-GS-ROLE-49, 50 (checkbox seleksi dan Select All) ada di spec 022.
- Temuan untuk QA:
  - TC-GS-ROLE-43 Expected a ("tidak ada request") membutuhkan kemampuan mengamati request jaringan; mekanismenya tidak didefinisikan di TC, PRD, atau LLD dan disediakan tim FE.
  - TC-GS-ROLE-43 langkah 4 ("Ulangi langkah 1-3 login sbg Hendra Wijaya") tidak menyebut logout; spec menulis ganti akun eksplisit (langkah 62).
  - TC-GS-ROLE-41 langkah 2 dan Expected c tidak menyebut tooltip untuk checkbox yang enabled; spec hanya memverifikasi state enabled.
  - TC-GS-ROLE-41 langkah 2 dan Expected a sampai c menyebut "checkbox ... Remove", padahal Remove adalah row action pada overlay (⋯) kolom Actions (PRD §4.3 dan §4.8; TC-GS-ROLE-4 Expected b.i; TC-GS-ROLE-42); spec membuka overlay (⋯) baris, mengarahkan kursor ke item Remove, memverifikasi disabled atau enabled dan tooltip, lalu menutup overlay dengan Esc.
