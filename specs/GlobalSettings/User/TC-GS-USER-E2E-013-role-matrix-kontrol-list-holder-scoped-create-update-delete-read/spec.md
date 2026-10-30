---
id: TC-GS-USER-E2E-013-role-matrix-kontrol-list-holder-scoped-create-update-delete-read
title: "Role Matrix: Kontrol User List untuk Holder Manage user and role Create-Only, Update-Only, Delete-Only, dan Read-Only role terhadap Target Normal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-63
  - TC-GS-USER-64
  - TC-GS-USER-65
  - TC-GS-USER-66
  - TC-GS-USER-1004
coverage:
  web: automated
---

# Role Matrix: Kontrol User List untuk Holder Manage user and role Create-Only, Update-Only, Delete-Only, dan Read-Only role terhadap Target Normal

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`). Flag disetel untuk keempat akun pada tabel (mekanisme disediakan tim FE/BE).
- Role yang diuji (tiap role memakai akunnya sendiri; langkah ganti akun ditulis eksplisit di Test Steps). Kolom hasil berlaku untuk target Normal Dewi Lestari dan Mike Tan (Pending Activation); "Hidden" berarti tidak dirender; "disabled" berarti tampil namun disabled dengan tooltip `You don't have permission to edit.`:

| Role | Akun | Nama user | Env var password | TC | `[+ User]` | Kolom checkbox | Switch Active Dewi | `Edit` Dewi | `Delete` Dewi | `Resend Activation Email` Mike |
|---|---|---|---|---|---|---|---|---|---|---|
| Manage user and role (Create-Only: C+R) | `manageUserCreate_automated_{namaCompany}@qwertysystem.net` | Lestari Ayu (Tabel Pre-setup No. 5) | `Spectra.env.GS_CREATE_PASSWORD` | TC-GS-USER-63 | tampil | Hidden (header dan body) | disabled | disabled | disabled | Hidden |
| Manage user and role (Update-Only: R+U) | `manageUserUpdate_automated_{namaCompany}@qwertysystem.net` | Bayu Saputra (No. 6) | `Spectra.env.GS_UPDATE_PASSWORD` | TC-GS-USER-64 | Hidden | tampil | enabled | enabled | disabled | tampil |
| Manage user and role (Delete-Only: R+D) | `manageUserDelete_automated_{namaCompany}@qwertysystem.net` | Citra Melati (No. 7) | `Spectra.env.GS_DELETE_PASSWORD` | TC-GS-USER-65 | Hidden | tampil | disabled | disabled | enabled | Hidden |
| Manage user and role (Read-Only role: R saja) | `manageUserRead_automated_{namaCompany}@qwertysystem.net` | Eko Prasetyo (No. 8) | `Spectra.env.GS_READ_PASSWORD` | TC-GS-USER-66, TC-GS-USER-1004 | Hidden | Hidden (header dan body) | disabled | disabled | disabled | Hidden |

- Pada keempat role, baris Dewi Lestari dan Mike Tan tampil di tabel, dan opsi `Detail` pada overlay keduanya tampil dan enabled.
- Login: hook `before` memakai akun default suite (Total Control, `Spectra.env.GS_TC_PASSWORD`) dan tidak dipakai langkah; setiap putaran role dimulai dengan langkah ganti akun eksplisit. Spec berakhir di akun Read-Only role, sehingga hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD`, `GS_READ_PASSWORD`, `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup, hanya dibaca; spec tidak membuat, mengubah, atau menghapus data): Dewi Lestari (No. 12, Normal, Activated), Mike Tan (No. 14, Pending Activation). Data Dinamis: tidak ada.
- Kemampuan teknis: logout dan login ulang dengan akun berbeda dalam satu spec; hover elemen (switch, opsi overlay) dan membaca tooltip; membaca state enabled atau disabled; menekan Esc.
- State global yang diubah: tidak ada selain flag Guided Tooltip (dipulihkan hook suite).

## Test Steps

### TC-GS-USER-63, TC-GS-USER-64, TC-GS-USER-65, TC-GS-USER-66: Kontrol List per role terhadap target Normal

Lakukan langkah 1 sampai 21 berikut untuk setiap role pada tabel "Role yang diuji", berurutan dari baris pertama sampai baris terakhir. Setiap `Verifikasi` memakai kolom tabel pada baris role yang sedang diuji; tooltip `You don't have permission to edit.` diverifikasi pada elemen yang berstatus disabled menurut tabel.

1. Ganti akun: logout, lalu login sebagai role pada baris tabel
2. Buka Global Settings > User > User List (sub-tab Login User)
3. Pilih 100 baris per halaman pada Pagination
4. Verifikasi baris Dewi Lestari dan Mike Tan tampil di tabel
5. Verifikasi `[+ User]` sesuai kolom `[+ User]` tabel
6. Verifikasi kolom checkbox (header dan body) sesuai kolom "Kolom checkbox" tabel
7. Arahkan kursor ke switch Active baris Dewi Lestari
8. Verifikasi switch Active baris Dewi Lestari sesuai kolom "Switch Active Dewi" tabel (enabled, atau tampil namun disabled)
9. Verifikasi tooltip `You don't have permission to edit.` pada switch Active bila kolom tabel menyatakan disabled
10. Klik (⋯) pada baris Dewi Lestari
11. Verifikasi opsi `Detail` enabled di overlay Dewi Lestari
12. Arahkan kursor ke opsi `Edit`
13. Verifikasi opsi `Edit` sesuai kolom "`Edit` Dewi" tabel (enabled, atau tampil namun disabled)
14. Verifikasi tooltip `You don't have permission to edit.` pada `Edit` bila kolom tabel menyatakan disabled
15. Arahkan kursor ke opsi `Delete`
16. Verifikasi opsi `Delete` sesuai kolom "`Delete` Dewi" tabel (enabled, atau tampil namun disabled)
17. Verifikasi tooltip `You don't have permission to edit.` pada `Delete` bila kolom tabel menyatakan disabled
18. Tutup overlay dengan menekan Esc
19. Klik (⋯) pada baris Mike Tan (Pending Activation)
20. Verifikasi overlay Mike Tan memuat opsi `Detail`
21. Verifikasi opsi `Resend Activation Email` sesuai kolom "`Resend Activation Email` Mike" tabel (tampil atau Hidden)

### TC-GS-USER-1004: Kolom checkbox Hidden untuk holder Read-only role (sesi akun Read-Only role, putaran terakhir)

22. Verifikasi kolom paling kiri tabel tidak dirender (header dan body)
23. Verifikasi Bulk Action Bar tidak tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular; hasil per role dipetakan lewat kolom TC pada tabel "Role yang diuji".
- Spec Role Matrix (bagian 3a konvensi): langkah identik untuk empat role dan hanya akun login serta hasil yang berbeda, sehingga langkah 1 sampai 21 ditulis satu kali dengan hasil per role pada tabel di Prerequisites. Langkah 22 dan 23 dijalankan sekali, di sesi Read-Only role sesudah putaran terakhir (role terakhir pada tabel).
- Spec memuat 23 langkah bernomor; dieksekusi 4 putaran, satu kelas (Role Matrix, kontrol List, baca saja tanpa aksi yang mengubah data).
- Urutan TC sumber dipertahankan. Hook `before` tidak login sebagai Lestari Ayu; sesi awal adalah akun default suite sehingga langkah ganti akun (langkah 1) berlaku sama untuk keempat role tanpa langkah bersyarat.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ganti akun), 3 (memilih 100 baris per halaman, supaya Dewi Lestari dan Mike Tan tampil tanpa Search), 18 (menutup overlay Dewi Lestari sebelum membuka overlay Mike Tan). Langkah "Hover elemen yang disabled" pada TC sumber dipecah menjadi langkah 7, 12, dan 15.
- Langkah 4 (baris Dewi Lestari dan Mike Tan tampil), langkah 11 dan 20 (`Detail` enabled/tampil) adalah anchor positif untuk asersi absence (Hidden) pada langkah 6, 21, dan 22; langkah 11 sekaligus merupakan Expected d TC sumber.
- Langkah 9, 14, dan 17 menyatakan tooltip hanya untuk elemen disabled menurut tabel; elemen enabled tidak diasersi tooltip-nya.
- Temuan untuk QA:
  - TC-GS-USER-1004 berjudul "Kolom checkbox Hidden untuk holder Create-Only dan Read-only role" tetapi precondition dan langkahnya hanya Read-only role; kolom checkbox Hidden untuk Create-Only diasersi di TC-GS-USER-63 Expected b.
  - TC-GS-USER-1004 Expected a mengulang TC-GS-USER-66 Expected b untuk akun yang sama; Expected b ("Bulk Action Bar tidak pernah tampil") tidak menyebut cara memicu seleksi.
  - TC-GS-USER-63 sampai TC-GS-USER-66 langkah 5 ("Hover elemen yang disabled") tidak menunjuk elemen; spec memakai elemen disabled yang disebut di Expected (switch Active, `Edit`, `Delete`).
  - TC-GS-USER-64 dan TC-GS-USER-65 Expected d tidak menyebut tooltip untuk `Edit` atau `Delete` yang enabled; tidak diasersi.
