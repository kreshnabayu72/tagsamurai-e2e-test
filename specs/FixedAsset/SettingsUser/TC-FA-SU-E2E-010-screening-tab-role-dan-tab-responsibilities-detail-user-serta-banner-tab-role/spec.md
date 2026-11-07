---
id: TC-FA-SU-E2E-010-screening-tab-role-dan-tab-responsibilities-detail-user-serta-banner-tab-role
title: "Screening Tab Role dan Tab Responsibilities Detail User serta Banner Tab Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-30
  - TC-FA-SU-31
  - TC-FA-SU-32
coverage:
  web: automated
---

# Screening Tab Role dan Tab Responsibilities Detail User serta Banner Tab Role

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md`.
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` dengan 25 pengguna (#20); penugasan tier (#23): Lina Marlina (Total Control), Citra Lestari (Read Only), Oscar Pranata (Group Manager IT Infrastructure dan Accounts Payable), Budi Santoso (tanpa tingkat akses dan bukan Group Manager); Responsibilities Budi Santoso (#24 Borrowed Assets 5 baris dan Assigned Assets 5 baris, #25 Pending Approvals 5 baris dan Pending Tasks 5 baris), Hana Kusuma tanpa tanggung jawab; Transaction Role (#39). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE).
- Syarat data Budi Santoso yang belum tertulis di Pre-setup #23 dan #39 (perlu dijamin seed; lihat Temuan untuk QA): sedikitnya satu baris Transaction Role pada Sub-tab Transaction Role (dibutuhkan langkah 14 dan 16) dan lebih dari satu Global Role (dibutuhkan langkah 6, urut A-Z).
- Data Dinamis: tidak ada.
- Kemampuan teknis: tidak ada selain pengamatan UI.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-30: Screening Tab Role: sub-tab, banner, dan kolom per sub-tab

1. Ketik Search `Budi Santoso`, tekan Enter
2. Klik nama `Budi Santoso` di User List
3. Verifikasi sub-tab switcher `Global Role`, `Group Role`, dan `Transaction Role`
4. Verifikasi sub-tab Global Role aktif saat Tab Role dibuka
5. Verifikasi sub-tab Global Role memuat kolom `Active`, `Role Name`, `Create`, `Read`, `Update`, dan `Delete`
6. Verifikasi baris sub-tab Global Role urut Role Name A-Z
7. Verifikasi toolbar sub-tab Global Role hanya memuat icon Changelog
8. Klik sub-tab Group Role
9. Verifikasi sub-tab Group Role memuat kolom `Role Name`, `Group`, dan `Actions`
10. Verifikasi tiap baris sub-tab Group Role memiliki `[Detail]` dan `[Assign Group]`
11. Verifikasi sub-tab Group Role tanpa switch aktif
12. Klik sub-tab Transaction Role
13. Verifikasi toolbar sub-tab Transaction Role memuat `Search`, `Filter`, `[+ Assign]`, dan `Changelog`
14. Centang satu baris Transaction Role
15. Verifikasi `[Bulk Remove]` tampil saat ada seleksi
16. Hilangkan centang baris Transaction Role
17. Verifikasi sub-tab Transaction Role memuat kolom `Transaction`, `Role`, `Group`, dan `Actions`

### TC-FA-SU-31: Banner Tab Role per tingkat akses dan Group Manager

18. Klik segmen Breadcrumb `User`
19. Ganti isi kotak search dengan `Lina Marlina`, tekan Enter
20. Klik nama `Lina Marlina`
21. Verifikasi banner info read-only "This user has Total Control access." tampil di atas tabel Sub-tab Global Role
22. Klik sub-tab Group Role
23. Verifikasi banner "This user has Total Control access." tampil di atas tabel Sub-tab Group Role
24. Verifikasi banner tanpa tombol aksi
25. Verifikasi tidak ada baris Total Control atau Read Only yang disisipkan ke tabel Global Role maupun Group Role
26. Klik sub-tab Transaction Role
27. Verifikasi banner "This user has Total Control access." tampil di atas tabel Sub-tab Transaction Role
28. Klik segmen Breadcrumb `User`
29. Ganti isi kotak search dengan `Citra Lestari`, tekan Enter
30. Klik nama `Citra Lestari`
31. Verifikasi banner "This user has Read Only access." tampil di atas tabel Sub-tab Global Role
32. Klik segmen Breadcrumb `User`
33. Ganti isi kotak search dengan `Oscar Pranata`, tekan Enter
34. Klik nama `Oscar Pranata`
35. Verifikasi banner "This user is a Group Manager for: Accounts Payable, IT Infrastructure." tampil dengan nama grup dipisah koma dan urut A-Z
36. Klik sub-tab Group Role
37. Verifikasi banner "This user is a Group Manager for: Accounts Payable, IT Infrastructure." tampil juga di atas tabel Sub-tab Group Role dengan nama grup urut A-Z (FI-20)
38. Klik sub-tab Transaction Role
39. Verifikasi banner "This user is a Group Manager for: Accounts Payable, IT Infrastructure." tampil juga di atas tabel Sub-tab Transaction Role dengan nama grup urut A-Z (FI-20)
40. Klik segmen Breadcrumb `User`
41. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter
42. Klik nama `Budi Santoso`
43. Verifikasi tabel Sub-tab Global Role tampil tanpa banner (tanpa tingkat akses dan bukan Group Manager)

### TC-FA-SU-32: Screening Tab Responsibilities: label, sub-tab, dan empty state gabungan

44. Klik tab Responsibilities
45. Verifikasi label tab `Responsibilities (20)` dan sub-tab `Borrowed Assets (5)`, `Assigned Assets (5)`, `Pending Approvals (5)`, dan `Pending Tasks (5)`
46. Verifikasi keempat sub-tab tampil
47. Verifikasi angka tab `20` sama dengan jumlah baris seluruh sub-tab (5+5+5+5)
48. Klik segmen Breadcrumb `User`
49. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter
50. Klik nama `Hana Kusuma`
51. Klik tab Responsibilities
52. Verifikasi label tab `Responsibilities (0)` (angka tampil juga saat 0)
53. Verifikasi area konten menampilkan empty state "No pending responsibilities" dengan deskripsi "This user has no active custody, pending approvals, or tasks."
54. Verifikasi empty state menggantikan sub-tab switcher
55. Verifikasi tidak ada aksi tulis dan tidak ada tautan keluar dari tab Responsibilities
56. Klik segmen Breadcrumb `User`
57. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 18, 28, 32, 40, 48, dan 56 (kembali ke User List lewat Breadcrumb), langkah 1, 19, 29, 33, 41, dan 49 (Search untuk menemukan baris target, R-16; langkah pertama "Ketik Search" dan sisanya "Ganti isi kotak search" karena kotak masih berisi nama sebelumnya, bagian 8b butir 9), langkah 57 (mengosongkan Search, S-09), langkah 14 dan 16 (centang dan hilangkan centang baris untuk mengamati `[Bulk Remove]`, S-09). Langkah 2, 20, 30, 34, 42, dan 50 membuka Detail; langkah 44 dan 51 membuka Tab Responsibilities.
- Langkah 36 (membuka Sub-tab Group Role Oscar Pranata) dan langkah 38 (membuka Sub-tab Transaction Role Oscar Pranata) adalah langkah penghubung; langkah 23 dan 37 membuktikan banner tier dan banner Group Manager tampil di Sub-tab Group Role, langkah 27 dan 39 di Sub-tab Transaction Role (TC-FA-SU-31 Expected a, c, d; TC-FA-SU-1074).
- Langkah 1 TC-FA-SU-32 ("Buka Tab Responsibilities pada Budi Santoso") dilanjutkan dari Detail Budi Santoso yang masih terbuka pada langkah 42.
- Langkah 25 (absence baris Total Control atau Read Only) beranchor banner pada langkah 21 dan 23; langkah 43 beranchor tabel Global Role yang termuat.
- Spec melewati sekitar 35 langkah (57 langkah). Seluruhnya satu kelas (screening tab Detail User, satu akun, tanpa mengubah data), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain.
- Pembagian TC lintas spec: Tab Non-Login User, Changelog, System Log, Transaction Admin Log, dan User Log (TC-FA-SU-33 dan 34) ada di spec 011.
- Temuan untuk QA:
  - TC-FA-SU-31 Expected a dan d menyatakan banner tier dan banner Group Manager tampil juga di Sub-tab Transaction Role; spec mengasersinya pada langkah 27 dan 39.
  - TC-FA-SU-30 Expected d menyebut `[Bulk Remove]` saat ada seleksi, tetapi Pre-setup #39 tidak memberi Transaction Role untuk Budi Santoso; spec mengikuti Langkah Uji TC (Budi Santoso) dan membutuhkan sedikitnya satu baris Transaction Role pada Budi Santoso (langkah 14), yang perlu dijamin seed.
  - TC-FA-SU-30 Expected b menyebut urut Role Name A-Z tanpa nilai; spec mengasersi urutan A-Z pada baris yang tampil (Budi Santoso memiliki lebih dari satu Global Role).
  - TC-FA-SU-31 Expected c menulis banner "Group Manager untuk dua grup" tanpa menyebut grup; spec memakai Oscar Pranata (Group Manager IT Infrastructure dan Accounts Payable, Pre-setup #23) dan nama grup urut A-Z.
  - TC-FA-SU-32 Expected b ("keempat sub-tab selalu tampil walau sebagian kosong") tidak punya pengguna dengan sebagian sub-tab kosong pada Pre-setup #24 dan #25; spec mengasersi keempat sub-tab pada Budi Santoso (semuanya berisi 5 baris) dan empty state gabungan pada Hana Kusuma.
