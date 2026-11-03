---
id: TC-AC-RP-E2E-044-resilience-tulis-assign-user-edit-crud-dan-toggle
title: "Resilience Tulis: Assign User to Role, Edit CRUD, dan Toggle Gagal 5xx"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-171
  - TC-AC-RP-175
  - TC-AC-RP-220
coverage:
  web: automated
---

# Resilience Tulis: Assign User to Role, Edit CRUD, dan Toggle Gagal 5xx

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; respons dipaksa lewat `Spectra.intercept()` dan state Role Detail diasersi)
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (`Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal: `Default Group`, `Region A` dengan anak `Branch 1`, `Region Jawa` dengan anak `Jakarta` dan `Surabaya`, `Sumatera`), #12 (user Standard), #15 (penugasan peran individual), dan #17 (approver dan toggle). Target aksi memakai user Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini.
- Pre-setup #17: toggle `Manage allocation` `Sumatera` OFF tersimpan (TC-AC-RP-220).
- Pemulihan state: intercept dilepas setelah tiap pemicu dan dipulihkan di hook `after`; kegagalan yang dipaksa tidak menyimpan perubahan sehingga data Pre-setup tidak berubah. Kemampuan reset baseline (suite.md) tetap dijalankan di hook `before` dan `after`.
- Failure injection lewat `Spectra.intercept()` pada respons jaringan (Tabel Data Uji Pre-setup #23): respons 5xx, penahanan respons, dan timeout atau koneksi terputus. Intercept dilepas segera setelah pemicu selesai dan dipulihkan di hook `after` bila spec gagal di tengah.
- Penahanan respons update permissions lalu pengembalian respons 5xx (Pre-setup #23: penundaan respons dan 5xx) dipakai pada TC-AC-RP-175 dan TC-AC-RP-220 agar state sementara cell (TC-AC-RP-175) dan switch (TC-AC-RP-220) dapat diasersi sebelum kembali (bagian 8b butir 5).
- Tunggu waktu nyata: 10 detik pada langkah "Amati toast selama 10 detik" untuk memastikan toast error persisten tetap tampil (jeda pendek, bagian 6 konvensi).
- Suite berjalan serial (`parallel: false`) karena spec mengubah state Pre-setup bersama.
- Env var `AC_RP_TC_PASSWORD` dipakai langkah login hook `before`; nama ini perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-171: Assign User to Role gagal 5xx

1. Klik tab `System`
2. Klik `⋯` pada baris `Manage language` di section Global Role lalu klik `Detail`
3. Klik "+ Assign"
4. Ketik Search `Alex Tan`, tekan Enter
5. Centang `Alex Tan`
6. Atur intercept respons submit Assign User to Role menjadi 5xx
7. Klik `[Assign]`
8. Verifikasi toast "Error, failed to assign role."
9. Verifikasi popup tetap terbuka
10. Verifikasi centangan `Alex Tan` dipertahankan
11. Lepas intercept 5xx
12. Klik `[Cancel]`

### TC-AC-RP-175: Edit CRUD gagal 5xx mengembalikan nilai

13. Buka halaman `Settings > Role & Permission`, lalu klik tab `System`
14. Klik `⋯` pada baris `Manage device master data` di section Global Role lalu klik `Detail`
15. Ketik Search `John Dohan`, tekan Enter
16. Atur intercept respons update permissions: tahan respons lalu kembalikan 5xx
17. Centang D pada baris `John Dohan`
18. Verifikasi cell D baris `John Dohan` berubah sementara menjadi tercentang
19. Lepaskan tahanan respons sehingga respons 5xx diterima
20. Verifikasi cell D baris `John Dohan` kembali tidak tercentang
21. Verifikasi toast "Error, failed to update permissions."
22. Amati toast selama 10 detik tanpa men-dismiss
23. Verifikasi toast tetap tampil sampai di-dismiss
24. Dismiss toast secara manual
25. Lepas intercept 5xx

### TC-AC-RP-220: Toggle gagal 5xx kembali ke posisi semula

26. Buka halaman `Settings > Role & Permission`, lalu klik tab `System`
27. Klik `⋯` pada baris `Manage allocation` di section Group Role lalu klik `Detail`
28. Klik node `Sumatera`
29. Atur intercept respons update permissions: tahan respons lalu kembalikan 5xx
30. Klik toggle
31. Verifikasi switch berubah sementara menjadi ON
32. Lepaskan tahanan respons sehingga respons 5xx diterima
33. Verifikasi switch kembali ke OFF
34. Verifikasi toast "Error, failed to update permissions."
35. Lepas intercept 5xx

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 11, 12, 13, 22, 24, 25, 26, 35 (tanpa `Verifikasi`; menyiapkan, membersihkan, atau memulihkan state).
- Search untuk menemukan baris target (langkah penghubung, R-16): langkah 4, 15.
- Penahanan respons pada TC-AC-RP-175 (langkah 16) dan TC-AC-RP-220 (langkah 29) hanya untuk mengamati state sementara (cell, switch) sebelum kembali; intercept dilepas di langkah penghubung berikutnya (langkah 25 dan 35).
- Temuan untuk QA:
  - TC-AC-RP-175 Expected "Cell berubah sementara lalu kembali" tidak dapat diasersi deterministik tanpa penahanan respons; spec menahan respons lalu mengembalikan 5xx (kemampuan Pre-setup #23) dan hal ini bukan bagian TC.
  - TC-AC-RP-175 dan 220 tidak menyebut kolom toggle atau label toggle (hanya "Klik toggle"); spec mengikuti teks TC.
