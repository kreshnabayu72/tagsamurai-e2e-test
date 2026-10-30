---
id: TC-GS-USER-E2E-010-role-matrix-kontrol-baris-aktor-total-control-per-target
title: "Role Matrix: Kontrol Baris User List untuk Aktor Total Control per Target (Normal, Default User, Self, Tier Total Control, Tier Read Only)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-49
  - TC-GS-USER-50
  - TC-GS-USER-51
  - TC-GS-USER-52
  - TC-GS-USER-53
coverage:
  web: automated
---

# Role Matrix: Kontrol Baris User List untuk Aktor Total Control per Target (Normal, Default User, Self, Tier Total Control, Tier Read Only)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Role yang diuji (satu role, akun default suite):

| Role | Akun | Nama user | Env var password |
|---|---|---|---|
| Total Control | `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` | Siti Nurhaliza (Tabel Pre-setup No. 2) | `Spectra.env.GS_TC_PASSWORD` |

- Login akun Total Control (aktor pertama dan satu-satunya, sama dengan akun default suite) dilakukan di hook `before`; tidak ada langkah ganti akun. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup, hanya dibaca; spec tidak membuat, mengubah, atau menghapus data): target Normal Dewi Lestari (No. 12), target Default User Hendra Gunawan (No. 1), target Self Siti Nurhaliza (No. 2, akun yang login), target Tier Total Control Andi Wijaya (No. 10), target Tier Read Only Doni Pratama (No. 11). Data Dinamis: tidak ada.
- Kemampuan teknis: hover elemen (checkbox, switch, opsi overlay) dan membaca tooltip; membaca state enabled atau disabled; menekan Esc.
- State global yang diubah: tidak ada.

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Pilih 100 baris per halaman pada Pagination

### TC-GS-USER-49: Kontrol baris target Normal untuk aktor Total Control

3. Verifikasi checkbox baris Dewi Lestari enabled
4. Verifikasi switch Active baris Dewi Lestari enabled
5. Klik (⋯) pada baris Dewi Lestari
6. Verifikasi overlay memuat opsi `Detail` | `Edit` | `Delete`, semua enabled
7. Tutup overlay dengan menekan Esc

### TC-GS-USER-50: Kontrol baris target Default User untuk aktor Total Control

8. Arahkan kursor ke checkbox baris Hendra Gunawan
9. Verifikasi checkbox baris Hendra Gunawan tampil namun disabled
10. Verifikasi tooltip `Default User cannot be modified.`
11. Arahkan kursor ke switch Active baris Hendra Gunawan
12. Verifikasi switch Active baris Hendra Gunawan tampil namun disabled
13. Verifikasi tooltip `Default User cannot be modified.`
14. Klik (⋯) pada baris Hendra Gunawan
15. Verifikasi opsi `Detail` dan `Edit` enabled di overlay
16. Arahkan kursor ke opsi `Delete`
17. Verifikasi opsi `Delete` tampil namun disabled
18. Verifikasi tooltip `Default User cannot be modified.`
19. Tutup overlay dengan menekan Esc

### TC-GS-USER-51: Kontrol baris target Self untuk aktor Total Control

20. Arahkan kursor ke checkbox baris Siti Nurhaliza (akun sendiri)
21. Verifikasi checkbox baris Siti Nurhaliza tampil namun disabled
22. Verifikasi tooltip `You can't manage your own account from here.`
23. Arahkan kursor ke switch Active baris Siti Nurhaliza
24. Verifikasi switch Active baris Siti Nurhaliza tampil namun disabled
25. Verifikasi tooltip `You can't manage your own account from here.`
26. Klik (⋯) pada baris Siti Nurhaliza
27. Verifikasi opsi `Detail` dan `Edit` enabled di overlay
28. Arahkan kursor ke opsi `Delete`
29. Verifikasi opsi `Delete` tampil namun disabled
30. Verifikasi tooltip `You can't manage your own account from here.`
31. Tutup overlay dengan menekan Esc

### TC-GS-USER-52: Kontrol baris target Tier Total Control untuk aktor Total Control

32. Verifikasi checkbox baris Andi Wijaya enabled
33. Verifikasi switch Active baris Andi Wijaya enabled
34. Klik (⋯) pada baris Andi Wijaya
35. Verifikasi overlay memuat opsi `Detail` | `Edit` | `Delete` enabled
36. Tutup overlay dengan menekan Esc

### TC-GS-USER-53: Kontrol baris target Tier Read Only untuk aktor Total Control

37. Verifikasi checkbox baris Doni Pratama enabled
38. Verifikasi switch Active baris Doni Pratama enabled
39. Klik (⋯) pada baris Doni Pratama
40. Verifikasi overlay memuat opsi `Detail` | `Edit` | `Delete` enabled

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix (bagian 3a konvensi): satu role (Total Control) dengan lima target yang berbeda hasilnya (kasus target yang terlindungi: Default User dan Self; sesama Total Control boleh saling kelola). Spec melewati sekitar 35 langkah (40 langkah) karena kelima blok satu kelas (kontrol baris, baca saja tanpa aksi yang mengubah data), satu akun, dan berbagi satu pembukaan List; tiap blok TC berdiri sendiri.
- Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2 (memilih 100 baris per halaman, supaya semua baris target tampil tanpa Search), serta langkah 7, 19, 31, dan 36 (menutup overlay row action sebelum TC berikutnya).
- Langkah "Cari baris X" pada TC sumber dipenuhi dengan menemukan baris Name X di halaman 100 baris; langkah "Hover elemen yang disabled" pada TC-GS-USER-49, TC-GS-USER-52, dan TC-GS-USER-53 tidak dijalankan karena tidak ada elemen disabled pada baris itu.
- Temuan untuk QA:
  - TC-GS-USER-51 langkah 1 berbunyi "Cari baris baris akun sendiri" (kata ganda); spec memakai baris Siti Nurhaliza (akun yang login).
  - TC-GS-USER-49, TC-GS-USER-52, dan TC-GS-USER-53 Expected c menyebut overlay `Detail | Edit | Delete` "semua enabled" tanpa menyebut urutan; spec mengasersi opsi dan state enabled, tanpa urutan.
