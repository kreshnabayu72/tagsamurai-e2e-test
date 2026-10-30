---
id: TC-GS-USER-E2E-008-role-matrix-visibilitas-menu-user-dan-direct-url
title: "Role Matrix: Visibilitas Menu User di Sidebar Global Settings dan Direct URL per Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-41
  - TC-GS-USER-42
  - TC-GS-USER-43
  - TC-GS-USER-44
  - TC-GS-USER-45
  - TC-GS-USER-46
coverage:
  web: automated
---

# Role Matrix: Visibilitas Menu User di Sidebar Global Settings dan Direct URL per Role

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`). Flag disetel untuk akun aktor yang dipakai suite; kelima akun pada tabel di bawah termasuk akun yang disetel (mekanisme disediakan tim FE/BE).
- Role yang diuji (tiap role memakai akunnya sendiri; langkah ganti akun ditulis eksplisit di Test Steps):

| Role | Akun | Nama user | Env var password | TC |
|---|---|---|---|---|
| Total Control | `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` | Siti Nurhaliza (Tabel Pre-setup No. 2) | `Spectra.env.GS_TC_PASSWORD` | TC-GS-USER-41 |
| Read Only | `readOnlyGlobalSettings_automated_{namaCompany}@qwertysystem.net` | Yudi Pratomo (No. 3) | `Spectra.env.GS_RO_PASSWORD` | TC-GS-USER-42 |
| Manage user and role (Full CRUD) | `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` | Fajar Nugroho (No. 4) | `Spectra.env.GS_FULLCRUD_PASSWORD` | TC-GS-USER-43 |
| Manage user and role (Read-Only role: R saja) | `manageUserRead_automated_{namaCompany}@qwertysystem.net` | Eko Prasetyo (No. 8) | `Spectra.env.GS_READ_PASSWORD` | TC-GS-USER-44 |
| Basic (Access Global Settings, tanpa tier akses dan tanpa role individual) | `basicGlobalSettings_automated_{namaCompany}@qwertysystem.net` | Gita Permata (No. 9) | `Spectra.env.GS_BASIC_PASSWORD` | TC-GS-USER-45, TC-GS-USER-46 |

- Login akun aktor pertama spec (Total Control) dilakukan di hook `before`; keempat akun lain memakai langkah ganti akun eksplisit. Karena spec berakhir di akun Basic, hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `GS_RO_PASSWORD`, `GS_FULLCRUD_PASSWORD`, `GS_READ_PASSWORD`, `GS_BASIC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup: hanya kelima akun di atas (dibaca, tidak diubah). Data Dinamis: tidak ada; spec tidak membuat, mengubah, atau menghapus data.
- URL direct: URL halaman Global Settings > User (User List). Nilai URL ditentukan tim FE di tahap script karena TC tidak menyebut path-nya.
- Kemampuan teknis: logout dan login ulang dengan akun berbeda dalam satu spec; mengetik URL langsung di address bar lalu menekan Enter; membaca toast.
- State global yang diubah: tidak ada selain flag Guided Tooltip (dipulihkan hook suite).

## Test Steps

### TC-GS-USER-41: Menu User tampil untuk Total Control

1. Buka Global Settings
2. Verifikasi menu `User` tampil di sidebar Global Settings
3. Klik menu User
4. Verifikasi halaman `User > User List` terbuka
5. Verifikasi tabel tampil

### TC-GS-USER-42: Menu User tampil untuk Read Only

6. Ganti akun: logout, lalu login sebagai Read Only (Yudi Pratomo)
7. Buka Global Settings
8. Verifikasi menu `User` tampil di sidebar Global Settings
9. Klik menu User
10. Verifikasi halaman `User > User List` terbuka
11. Verifikasi tabel tampil

### TC-GS-USER-43: Menu User tampil untuk Manage user and role (Full CRUD)

12. Ganti akun: logout, lalu login sebagai Manage user and role (Full CRUD) (Fajar Nugroho)
13. Buka Global Settings
14. Verifikasi menu `User` tampil di sidebar Global Settings
15. Klik menu User
16. Verifikasi halaman `User > User List` terbuka
17. Verifikasi tabel tampil

### TC-GS-USER-44: Menu User tampil untuk Manage user and role (Read-Only role: R saja)

18. Ganti akun: logout, lalu login sebagai Manage user and role (Read-Only role: R saja) (Eko Prasetyo)
19. Buka Global Settings
20. Verifikasi menu `User` tampil di sidebar Global Settings
21. Klik menu User
22. Verifikasi halaman `User > User List` terbuka
23. Verifikasi tabel tampil

### TC-GS-USER-45: Sidebar Global Settings hidden total untuk Basic

24. Ganti akun: logout, lalu login sebagai Basic (Gita Permata)
25. Buka App Switcher / Portal
26. Verifikasi card Global Settings tampil di Portal
27. Klik card Global Settings
28. Verifikasi sidebar Global Settings tidak menampilkan menu apa pun
29. Verifikasi menu `User` tidak tampil

### TC-GS-USER-46: Direct URL halaman User oleh Basic ditolak

30. Ketik URL halaman Global Settings > User langsung di address bar, tekan Enter
31. Verifikasi toast error `You don't have permission to do this.`
32. Verifikasi data list user tidak ditampilkan

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix (bagian 3a konvensi): satu daftar elemen (menu User, halaman User List, direct URL), banyak role, hasil berbeda per role (tampil untuk empat role, tidak tampil dan ditolak untuk Basic). Tiap role punya blok sendiri karena langkah ganti akun ditulis eksplisit.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6, 12, 18, dan 24 (ganti akun), langkah 25 dan 27 (membuka Portal dan card Global Settings untuk mencapai sidebar Basic).
- Langkah 26 (card Global Settings tampil di Portal) adalah anchor positif untuk asersi absence langkah 28 dan 29 (konvensi 8b butir 2); asersi ini tidak ada di Expected TC-GS-USER-45 dan ditambahkan sebagai anchor.
- Urutan asersi TC-GS-USER-46 dibalik: toast (Expected b) diverifikasi lebih dulu karena toast bersifat sementara dan menjadi anchor positif bagi asersi data list tidak ditampilkan (Expected a).
- Temuan untuk QA:
  - TC-GS-USER-46 menyebut "URL halaman Global Settings > User" tanpa path; nilai URL ditentukan tim FE di tahap script.
  - TC-GS-USER-45 langkah 2 menyebut mengamati card dan sidebar, tetapi Expected hanya menyebut sidebar; keadaan sidebar tanpa menu apa pun (kosong, atau halaman Global Settings tanpa sidebar) tidak dijelaskan. Spec mengasersi sidebar tidak menampilkan menu apa pun sesuai Expected.
  - TC-GS-USER-41 sampai TC-GS-USER-44 menyebut Expected b "halaman terbuka dan tabel tampil" tanpa penanda halaman; spec memeriksa halaman `User > User List` terbuka lalu tabel tampil.
  - TC-GS-USER-45 langkah 1 menyebut membuka App Switcher / Portal dan mengamati sidebar Global Settings tanpa langkah membuka Global Settings; spec mengklik card Global Settings di Portal (langkah 27).
