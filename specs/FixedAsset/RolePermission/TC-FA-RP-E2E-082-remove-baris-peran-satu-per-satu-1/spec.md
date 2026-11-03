---
id: TC-FA-RP-E2E-082-remove-baris-peran-satu-per-satu-1
title: "Remove baris peran satu per satu (1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-279
  - TC-FA-RP-280
  - TC-FA-RP-281
  - TC-FA-RP-282
coverage:
  web: automated
---

# Remove baris peran satu per satu (1/2)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: pool #15 (Budi Santoso), #18, dan #39 (Detail Role Group Role `Manage files` terisi, termasuk Budi Santoso di `Helpdesk`). Budi Santoso memegang Global Role `Manage Open API`, Group Role `Manage files` di `Data Center` dan di `Helpdesk`; untuk TC-FA-RP-282 Budi Santoso pernah memegang `Manage accounting` dengan Create dan Update aktif lalu di-Remove. Disiapkan lewat seed API di hook `before` dan sebagai langkah penghubung (langkah 21).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan data Pre-setup yang diubah spec ini ke kondisi Tabel Data Uji Pre-setup TC (penugasan Budi Santoso `Manage Open API`, `Manage files` di `Data Center` dan `Helpdesk`, serta `Manage accounting`), mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (lihat suite.md).

## Test Steps

### TC-FA-RP-279: Dialog Remove User dari Role single: copy dan Cancel

1. Klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role
2. Klik `[⋯]` baris Budi Santoso lalu `Remove`
3. Verifikasi dialog severity danger: Title `Remove User`; Body `• Budi S` lalu `The role assignment, including its permissions, will be removed permanently.`; tombol `[Cancel]` dan `[Remove]`
4. Klik `[Cancel]`
5. Verifikasi dialog tertutup
6. Verifikasi baris Budi Santoso tetap ada
7. Verifikasi tidak ada toast

### TC-FA-RP-280: Confirm Remove baris Global Role: penugasan dicabut permanen

8. Klik Tab `System`, lalu catat nilai kolom Users baris `Manage Open API` sebagai baseline
9. Klik Role Name `Manage Open API` pada section Global Role
10. Klik `[⋯]` baris Budi Santoso lalu `Remove`, klik `[Remove]`
11. Verifikasi muncul toast sukses: `Success, user has been removed.`
12. Verifikasi baris Budi Santoso hilang dari tabel
13. Klik Tab `System`
14. Verifikasi nilai kolom Users baris `Manage Open API` berkurang satu dari baseline

### TC-FA-RP-281: Confirm Remove baris Group Role pada satu node tidak mengubah penugasan node lain

15. Klik Tab `System`, klik Role Name `Manage files` pada section Group Role
16. Klik `All Groups` di Sidebar Group Tree
17. Klik `[⋯]` baris Budi Santoso di `Data Center` lalu `Remove`, klik `[Remove]`
18. Verifikasi muncul toast sukses: `Success, user has been removed.`
19. Verifikasi baris Budi Santoso di `Data Center` hilang
20. Verifikasi baris Budi Santoso di `Helpdesk` tetap ada

### TC-FA-RP-282: Assign ulang user yang pernah di-Remove dimulai dari awal

21. Pulihkan state lewat seed API: Budi Santoso pernah memegang Global Role `Manage accounting` dengan Create dan Update aktif lalu di-Remove (tanpa penugasan saat ini)
22. Klik Tab `System`, klik Role Name `Manage accounting` pada section Global Role
23. Klik `[+ Assign]`, centang Budi Santoso, klik `[Assign]`
24. Verifikasi baris Budi Santoso baru tampil dengan Read tercentang Disabled
25. Verifikasi Create, Update, dan Delete tidak tercentang

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-279, TC-FA-RP-280, TC-FA-RP-281, TC-FA-RP-282).
- Langkah penghubung (S-03): membuka Tab System dan Detail Role; mencatat baseline kolom Users (langkah 8) sebelum Remove (S-12); pemulihan state seed (langkah 21).
- Dialog `Remove User` (langkah 3) disebut utuh sebagai satu elemen dialog konfirmasi (S-01): severity, Title, Body, dan kedua tombol.
- Temuan untuk QA:
  - Post Condition TC-FA-RP-280 (log `Remove` tercatat dan Tab Role Settings > User milik Budi Santoso) merujuk Section 5 dan 7 dan tidak punya langkah observasi di TC; tidak diasersi di spec ini (S-01).
  - TC-FA-RP-279 sampai TC-FA-RP-281 tidak menyebut apakah Budi Santoso adalah satu-satunya pemegang `Manage Open API`; asersi memakai baris Budi Santoso dan nilai Users sebelum dan sesudah.
