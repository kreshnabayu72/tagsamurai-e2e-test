---
id: TC-GS-ROLE-E2E-071-resilience-tulis-remove-access-level
title: "Resilience Tulis: Remove Total Control dan Remove Read Only Gagal 5xx"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-89
  - TC-GS-ROLE-90
coverage:
  web: automated
---

# Resilience Tulis: Remove Total Control dan Remove Read Only Gagal 5xx

## Prerequisites

- Mode: FE+BE dengan intercept parsial di atas backend nyata (bagian 6 konvensi; kelas harness fault injection, prinsip 13b).
- Akun aktor: Total Control, Ahmad Fauzi (`Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: kembali ke layar Global Settings > Role & Permission > Total Control.
- Data Pre-setup (tetap di environment, hanya dibaca): Rina Putri (Pre-setup #4; Read Only, Inactive) berada di Tab Read Only. Submit Remove digagalkan oleh intercept tanpa meneruskan request ke server, sehingga state Rina Putri tidak berubah.
- Seeding precondition TC-GS-ROLE-89 (Given, Tabel Data Uji Dinamis #2; lewat API oleh akun Ahmad Fauzi di hook `before`; kemampuan dari `openapi.yaml`: POST/DELETE `/v2/iam/products/{product}/roles/access-level` dan DELETE `/v2/iam/products/{product}/roles/capabilities/users`): Maya Anggraini (Pre-setup #11, Inactive) di-assign Total Control. Hook `after` mengembalikan Maya Anggraini ke kondisi kandidat Pre-setup #11 (tanpa access level, tanpa baris role) lewat API tanpa berasumsi seeding berhasil penuh.
- Kebutuhan intercept (`Spectra.intercept()`), dilepas segera setelah dipakai: respons Remove access level `DELETE /v2/iam/products/{product}/roles/access-level` (`openapi.yaml`, `low-level-design.md`) dipaksa HTTP 500 tanpa meneruskan request ke server (TC-GS-ROLE-89 untuk Total Control, TC-GS-ROLE-90 untuk Read Only).
- Pemulihan di hook `after` (tetap jalan walau spec gagal di tengah): intercept dilepas; dialog Remove ditutup; Maya Anggraini dipulihkan seperti di atas.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-89: Remove Total Control gagal 5xx

1. Ketik Search `Maya Anggraini`, tekan Enter
2. Klik `(⋯)` pada baris Maya Anggraini
3. Klik `Remove`
4. Pasang intercept pada respons Remove access level: jawab 500
5. Klik `[Remove]` pada dialog Remove
6. Verifikasi toast error `Error, failed to remove Total Control.`
7. Verifikasi dialog Remove tetap terbuka
8. Verifikasi `[Remove]` aktif kembali untuk retry
9. Lepas intercept 500
10. Klik `[Cancel]` pada dialog Remove
11. Verifikasi Maya Anggraini tetap tampil di Tab Total Control
12. Klik `(←)` pada kotak Search
13. Klik Tab `System`
14. Klik Role Name `Manage TAG`
15. Ketik Search `Maya Anggraini`, tekan Enter
16. Verifikasi baris Maya Anggraini tampil dengan Read checked
17. Verifikasi baris Maya Anggraini tampil dengan Update checked
18. Klik `(←)` pada kotak Search

### TC-GS-ROLE-90: Remove Read Only gagal 5xx

19. Klik menu sidebar `Role & Permission`
20. Klik Tab `Read Only`
21. Ketik Search `Rina Putri`, tekan Enter
22. Klik `(⋯)` pada baris Rina Putri
23. Klik `Remove`
24. Pasang intercept pada respons Remove access level: jawab 500
25. Klik `[Remove]` pada dialog Remove
26. Verifikasi toast error `Error, failed to remove Read Only.`
27. Verifikasi dialog Remove tetap terbuka
28. Verifikasi `[Remove]` aktif kembali untuk retry
29. Lepas intercept 500
30. Klik `[Cancel]` pada dialog Remove
31. Verifikasi Rina Putri tetap tampil di Tab Read Only
32. Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE dengan intercept parsial (prinsip 13b); kegagalan dipicu dengan `Spectra.intercept()` pada request browser, sehingga bukan `Mode: mock`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (89, 90) dipertahankan.
- Expected b dan c TC-GS-ROLE-89 dan TC-GS-ROLE-90 (baris tetap ada) diasersi sesudah dialog ditutup lewat `[Cancel]` (langkah 10 dan 30), karena tabel tertutup dialog selama dialog terbuka; Expected c (dialog tetap terbuka dan `[Remove]` aktif) diasersi lebih dulu (langkah 7, 8, 27, dan 28) sesuai urutan state.
- Klausa "baris role tidak berubah" pada Expected b TC-GS-ROLE-89 diasersi pada Detail "Manage TAG": baris Maya Anggraini tetap dengan Read dan Update checked (langkah 13 sampai 17), nilai yang dihasilkan Assign Total Control (TC-GS-ROLE-58 Expected e).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 12, 15, 18, 21, dan 32 (Search dan penutupan Search untuk menemukan baris), langkah 9 dan 29 (melepas intercept segera setelah pemicu, S-09; intercept dipasang pada langkah 4 dan 24), langkah 10 dan 30 (menutup dialog), langkah 13, 14, 19, dan 20 (pindah ke Detail "Manage TAG" lalu kembali ke Tab Read Only).
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-ROLE-89 dan 90 tidak menyebut apakah respons 5xx dipaksa dengan atau tanpa meneruskan request ke server; spec memaksa respons tanpa meneruskan request.
  - TC-GS-ROLE-89 Expected b ("baris role tidak berubah") tidak menyebut role mana yang diamati; spec mengamati Detail "Manage TAG" (Read dan Update checked).
  - TC-GS-ROLE-89 Dependensi TC-GS-ROLE-59 (Maya Anggraini dan Rudi Hartono bersama); spec hanya men-seed Maya Anggraini karena Rudi Hartono tidak diasersi.
