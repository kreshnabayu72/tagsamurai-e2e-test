---
id: TC-FA-CF-E2E-011-role-matrix-visibilitas-total-control-default-user-read-only
title: "Role Matrix: Visibilitas Elemen Halaman Custom Fields per Role (Total Control, Default User, Read Only)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-33
  - TC-FA-CF-34
  - TC-FA-CF-35
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Halaman Custom Fields per Role (Total Control, Default User, Read Only)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji (Company Alpha, `{namaCompany}` = Company Alpha; password tidak ditulis di spec atau fixture):

| Role | Akun (Pre-setup) | Env password | Dipakai di langkah |
|---|---|---|---|
| Total Control | #1 `totalControl_automated_{namaCompany}@qwertysystem.net`, login di hook `before` spec ini | `Spectra.env.FA_TC_PASSWORD` | 1 sampai 13 |
| Default User (Total Control permanen) | #2 `defaultUser_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_DU_PASSWORD` | 14 sampai 25 |
| Read Only | #3 `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` | 26 sampai 37 |

- Halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite untuk akun pertama; hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha). Nama env baru (`FA_TC_PASSWORD`, `FA_DU_PASSWORD`, `FA_RO_PASSWORD`) didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (Pre-setup #11) dengan baseline tab General (Pre-setup #12; dipakai: baris `Asset Serial Tag` dan `Equipment Class` dengan chip `+1 more` pada Value Setting), dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE); spec hanya membaca dan tidak mengubah data.
- Kemampuan teknis: hover.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk setiap akun aktor yang dipakai spec dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-33: Visibilitas elemen UI untuk Total Control

1. Verifikasi menu Settings > Custom Fields dan ketiga tab tampil
2. Verifikasi tombol `[+ Custom Field]` tampil
3. Buka menu row action baris `Asset Serial Tag`
4. Verifikasi row action `Edit` dan `Delete` tampil
5. Tutup menu row action dengan menekan `Esc`
6. Verifikasi switch Active tampil Enabled
7. Verifikasi checkbox baris tampil
8. Centang baris `Asset Serial Tag`
9. Verifikasi Bulk Action Bar muncul
10. Verifikasi toolbar Search, Download, dan Changelog tampil
11. Klik chip `+1 more` pada kolom Value Setting baris `Equipment Class`
12. Verifikasi chip `+1 more` membuka Popup All Values Preview
13. Tutup Popup All Values Preview dengan icon close `[✕]`

### TC-FA-CF-34: Visibilitas elemen UI untuk Default User (Total Control permanen)

14. Ganti akun: Logout dari akun Total Control
15. Login sebagai Default User (Pre-setup #2) dengan `Spectra.env.FA_DU_PASSWORD` dan buka Fixed Asset > Settings > Custom Fields (tab General)
16. Verifikasi menu dan ketiga tab tampil
17. Verifikasi tombol `[+ Custom Field]` tampil
18. Buka menu row action baris `Asset Serial Tag`
19. Verifikasi row action `Edit` dan `Delete` tampil
20. Tutup menu row action dengan menekan `Esc`
21. Verifikasi switch Active tampil Enabled
22. Verifikasi checkbox baris tampil
23. Centang baris `Asset Serial Tag`
24. Verifikasi Bulk Action Bar tampil
25. Verifikasi toolbar Search, Download, dan Changelog tampil

### TC-FA-CF-35: Visibilitas elemen UI untuk Read Only

26. Ganti akun: Logout dari akun Default User
27. Login sebagai Read Only (Pre-setup #3) dengan `Spectra.env.FA_RO_PASSWORD` dan buka Fixed Asset > Settings > Custom Fields (tab General)
28. Verifikasi menu dan tab tampil
29. Verifikasi tombol `[+ Custom Field]` Hidden
30. Verifikasi row action `Edit` dan `Delete` Hidden
31. Arahkan kursor ke switch Active baris `Asset Serial Tag`
32. Verifikasi switch Active tampil Disabled dengan tooltip `You don't have permission to do this.`
33. Verifikasi kolom Checkbox baris dan Bulk Action Bar Hidden
34. Verifikasi toolbar Search, Download, dan Changelog tampil
35. Klik chip `+1 more` pada kolom Value Setting baris `Equipment Class`
36. Verifikasi chip `+1 more` tetap membuka Popup All Values Preview
37. Tutup Popup All Values Preview dengan icon close `[✕]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Spec hanya membaca; subjudul `###` memetakan langkah ke id TC granular.
- Spec Role Matrix ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`) dan hasil per role berbeda (bagian 3a, S-07). Title spec tidak memakai kata "Positif" atau "Negatif" karena memuat kedua polaritas.
- Alasan di atas 35 langkah: spec memuat 37 langkah (sedikit di atas sekitar 35). satu topik (Role Matrix visibilitas elemen halaman yang sama), tiga blok role berurutan pada satu halaman dan satu dataset, tiap blok berdiri sendiri tanpa langkah bersyarat; memecah per role hanya menambah login dan hook tanpa menambah makna, dan dua langkah penutup popup (langkah 13 dan 37) menutup popup sesuai S-09.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 3, 18 (membuka menu row action agar `Edit` dan `Delete` teramati), langkah 5 dan 20 (menutup menu), langkah 8 dan 23 (mencentang baris agar Bulk Action Bar teramati; Langkah Uji TC "Centang satu baris bila checkbox tampil"), langkah 11 dan 35 (klik chip sesuai langkah uji TC), langkah 15 dan 27 (login akun baru dan membuka halaman), langkah 31 (hover agar tooltip switch Disabled teramati), serta langkah 13 dan 37 (menutup Popup All Values Preview dengan icon close `[✕]` supaya popup tidak terbuka saat Ganti akun: Logout pada langkah 14 dan saat hook `after` mengakhiri sesi; S-09, tanpa `Verifikasi` karena Expected TC tidak memuat penutupan popup).
- Absence Hidden pada langkah 29, 30, dan 33 beranchor langkah 28 (menu dan tab tampil) serta toolbar yang sudah termuat pada blok yang sama (8b butir 2, elemen UI Role Matrix). Pada blok Read Only tidak ada baris yang dicentang karena kolom Checkbox Hidden.
- Pada langkah 8 dan 23, baris yang dicentang dibiarkan karena ganti akun berikutnya mengakhiri sesi.
- Temuan untuk QA:
  - TC-FA-CF-33 dan TC-FA-CF-35 Langkah Uji 4 menyebut "chip `+N more` pada kolom Value Setting atau Scope"; spec memakai chip Value Setting baris `Equipment Class` (satu-satunya baris Value Setting dengan `+1 more`, Pre-setup #12) dan tidak mengklik chip Scope.
  - Post Condition tiga TC kosong (`-`); tidak ada yang dicatat.
