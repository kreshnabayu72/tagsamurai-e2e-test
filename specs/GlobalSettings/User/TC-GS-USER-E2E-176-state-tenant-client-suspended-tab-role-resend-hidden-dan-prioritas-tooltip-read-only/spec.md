---
id: TC-GS-USER-E2E-176-state-tenant-client-suspended-tab-role-resend-hidden-dan-prioritas-tooltip-read-only
title: "State Tenant Client Suspended: Tab Role Disabled, Resend Hidden, dan Tooltip Suspended Menang atas Read Only"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-USER-1102
  - TC-GS-USER-1134
  - TC-GS-USER-1130
coverage:
  web: automated
---

# State Tenant Client Suspended: Tab Role Disabled, Resend Hidden, dan Tooltip Suspended Menang atas Read Only

## Prerequisites

- Mode: FE+BE. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`); berlaku untuk kedua akun Client Suspended di bawah (flag disetel untuk akun aktor yang dipakai spec).
- Akun yang diuji (berganti akun secara eksplisit di langkah 32). Kedua akun berada di Client yang statusnya sudah Suspended; akun dan Client ini tidak ada di Tabel Data Uji Pre-setup dan disediakan tim FE:

  | Urutan | Role | Email | Environment variable password |
  |---|---|---|---|
  | 1 | Total Control Client Suspended (disediakan tim FE) | `totalControlGlobalSettings_automated_{namaCompanySuspended}@qwertysystem.net` | `GS_CLIENTSUSP_TC_PASSWORD` |
  | 2 | Read Only Client Suspended (disediakan tim FE; email akun ini tidak tertulis di Pre-setup TC, lihat Temuan untuk QA) | disediakan tim FE | `GS_CLIENTSUSP_RO_PASSWORD` (belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan tim FE) |

  Login akun 1 di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `Spectra.env.GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Env var: `GS_CLIENTSUSP_TC_PASSWORD`, `GS_CLIENTSUSP_RO_PASSWORD`, `GS_TC_PASSWORD`.
- Data: Client Suspended adalah Client tetap yang disiapkan tim FE. Karena aksi tulis terkunci, spec tidak men-seed data dan hanya membaca; Client memuat salinan data Pre-setup (Tabel Data Uji Pre-setup No. 10 sampai 22, disediakan tim FE): `Ahmad Fauzi` (Holder `Manage TAG`), `Mike Tan` (Pending Activation), `Rina Putri` (Pending Email Confirmation), dan `Dewi Lestari` (Basic, Activated).
- State global yang diubah: tidak ada. Spec tidak mengubah data Client mana pun dan tidak mengubah status Client; satu-satunya pemulihan adalah mengembalikan sesi.
- Semua TC: Client berstatus Suspended; TC-GS-USER-1102 dan 1134 login sebagai Total Control, TC-GS-USER-1130 login sebagai Read Only; semuanya berada di Global Settings > User > User List (sub-tab Login User).

## Test Steps

### TC-GS-USER-1102: Switch Active dan checkbox Tab Role Disabled dengan tooltip

1. Klik icon Search, ketik `Ahmad Fauzi`, tekan Enter
2. Klik Name `Ahmad Fauzi`
3. Klik Tab `Role`
4. Hover switch Active baris `Manage TAG`
5. Verifikasi switch Active baris `Manage TAG` tampil
6. Verifikasi switch Active baris `Manage TAG` Disabled dengan tooltip `"Entity is suspended."`
7. Hover checkbox Update baris `Manage TAG`
8. Verifikasi checkbox Update baris `Manage TAG` tampil
9. Verifikasi checkbox Update baris `Manage TAG` Disabled dengan tooltip `"Entity is suspended."`

### TC-GS-USER-1134: Resend Activation dan Confirmation Email Hidden di User List dan header Detail

10. Klik menu User di sidebar Global Settings
11. Klik icon Search, ketik `Mike Tan`, tekan Enter
12. Klik `⋯` pada baris `Mike Tan`
13. Hover opsi `Edit`
14. Verifikasi opsi `Edit` tampil
15. Verifikasi opsi `Edit` Disabled dengan tooltip `"Entity is suspended."`
16. Verifikasi opsi `Resend Activation Email` tidak ada di overlay (⋯)
17. Tekan Esc untuk menutup overlay (⋯)
18. Hover switch Active baris `Mike Tan`
19. Verifikasi switch Active baris `Mike Tan` tampil
20. Verifikasi switch Active baris `Mike Tan` Disabled dengan tooltip `"Entity is suspended."`
21. Ganti isi kotak search dengan `Rina Putri`, tekan Enter
22. Klik `⋯` pada baris `Rina Putri`
23. Hover opsi `Edit`
24. Verifikasi opsi `Edit` tampil
25. Verifikasi opsi `Edit` Disabled dengan tooltip `"Entity is suspended."`
26. Verifikasi opsi `Resend Confirmation Email` tidak ada di overlay (⋯)
27. Tekan Esc untuk menutup overlay (⋯)
28. Ganti isi kotak search dengan `Mike Tan`, tekan Enter
29. Klik Name `Mike Tan`
30. Verifikasi nama `Mike Tan` tampil di header Detail
31. Verifikasi `Resend Activation Email` tidak ada di header Detail

### TC-GS-USER-1130: Tooltip suspended menang atas Read Only

32. Ganti akun: logout, lalu login sebagai Read Only Client Suspended dengan `Spectra.env.GS_CLIENTSUSP_RO_PASSWORD`, lalu buka Global Settings > User > User List
33. Klik icon Search, ketik `Dewi Lestari`, tekan Enter
34. Hover switch Active baris `Dewi Lestari`
35. Verifikasi switch Active baris `Dewi Lestari` tampil
36. Verifikasi switch Active baris `Dewi Lestari` Disabled dengan tooltip `"Entity is suspended."`
37. Verifikasi tooltip yang tampil bukan tooltip Read Only `"Read Only access cannot modify data."`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Kelas state tenant (prinsip 13h): kontrol tulis terkunci pada Client yang statusnya sudah Suspended; spec hanya membaca dan tidak mengubah status Client.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (37 langkah). Alasan: tiga TC berada di satu kelas (13h) dan satu layar, blok berdiri sendiri, dan bagian sesudah ganti akun (langkah 32 sampai 37) tetap bermakna walau bagian sebelumnya gagal; langkah banyak karena satu `Verifikasi` per klausa Expected (S-01) dan anchor absence Resend (8b butir 2).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 11, 21, 28, dan 33 (Search baris target dibuka lewat Search nama persis; 8b butir 12, R-16), langkah 10 (kembali ke User List lewat sidebar; S-14), langkah 12, 17, 22, dan 27 (membuka dan menutup overlay `⋯`), langkah 2, 3, dan 29 (membuka Detail dan Tab `Role`), langkah 4, 7, 13, 18, 23, dan 34 (hover untuk tooltip, diasersi segera sesudahnya; 8b butir 5), langkah 32 (ganti akun eksplisit; S-07).
- Asersi tambahan di luar Expected TC: langkah 14, 24 (opsi `Edit` tampil) dan langkah 30 (nama user tampil di header Detail) menjadi anchor positif untuk absence `Resend Activation Email` dan `Resend Confirmation Email` (8b butir 2); langkah 37 mengasersi klausa "bukan tooltip Read Only" TC-GS-USER-1130 dengan teks tooltip Read Only dari TC-GS-USER-1000.
- Urutan Verifikasi pada TC-GS-USER-1134 diubah dari Expected: kontrol tulis lain (Expected b) ditulis lebih dulu sebagai anchor positif untuk asersi Hidden (Expected a).
- Pembagian TC lintas spec: kontrol tulis lain pada Client Suspended dan Expired (Create, Edit, Delete, Toggle Active, request langsung) diverifikasi di spec 156; spec ini memuat TC-GS-USER-1102, 1134, dan 1130 seluruhnya.
- Temuan untuk QA:
  - TC-GS-USER-1102, 1134, dan 1130 menulis tooltip `"Entity is suspended."`, sedangkan TC-GS-USER-1021 sampai 1024 (spec 156) menulis tooltip `"You don't have permission to edit."` untuk kontrol tulis pada Client Suspended; teks tooltip Client Suspended perlu dikonfirmasi. Spec ini mengikuti TC sumbernya.
  - TC-GS-USER-1102 dan 1130: precondition "Client berstatus suspended" tidak menyebut Client, akun, dan cara menyiapkan data; disediakan tim FE sebagai Client tetap dengan salinan data Pre-setup (S-13).
  - TC-GS-USER-1130 membutuhkan akun Read Only di Client Suspended yang tidak ada di Tabel Pre-setup maupun `.env.example`; spec memakai akun `GS_CLIENTSUSP_RO_PASSWORD` yang disediakan tim FE (alternatif: menyuspend Client A sementara, state tenant global; perlu keputusan). Email akun tidak tertulis di Pre-setup TC.
  - TC-GS-USER-1102 langkah 2 menyebut "checkbox baris `Manage TAG`" tanpa menyebut checkbox yang di-hover; spec memakai checkbox Update (mengikuti TC-GS-USER-1000).
  - TC-GS-USER-1134 Expected b ("kontrol tulis lain yang Show") tidak menyebut baris dan header yang diamati; spec mengasersi opsi `Edit` pada overlay Mike Tan dan Rina Putri serta switch Active baris Mike Tan, bukan kontrol di header Detail.
  - TC-GS-USER-1134 langkah 1 menyebut Mike Tan dan Rina Putri tanpa menyebut User List difilter; spec mencari tiap nama lewat Search.
