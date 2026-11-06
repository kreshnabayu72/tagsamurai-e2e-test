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
- Data Dinamis: tidak ada.
- Kemampuan teknis: tidak ada selain pengamatan UI.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-30: Screening Tab Role: sub-tab, banner, dan kolom per sub-tab

1. Klik nama `Budi Santoso` di User List
2. Verifikasi sub-tab switcher `Global Role`, `Group Role`, dan `Transaction Role`
3. Verifikasi sub-tab Global Role aktif saat Tab Role dibuka
4. Verifikasi sub-tab Global Role memuat kolom `Active`, `Role Name`, `Create`, `Read`, `Update`, dan `Delete`
5. Verifikasi baris sub-tab Global Role urut Role Name A-Z
6. Verifikasi toolbar sub-tab Global Role hanya memuat icon Changelog
7. Klik sub-tab Group Role
8. Verifikasi sub-tab Group Role memuat kolom `Role Name`, `Group`, dan `Actions`
9. Verifikasi tiap baris sub-tab Group Role memiliki `[Detail]` dan `[Assign Group]`
10. Verifikasi sub-tab Group Role tanpa switch aktif
11. Klik sub-tab Transaction Role
12. Verifikasi toolbar sub-tab Transaction Role memuat `Search`, `Filter`, `[+ Assign]`, dan `Changelog`
13. Centang satu baris Transaction Role
14. Verifikasi `[Bulk Remove]` tampil saat ada seleksi
15. Hilangkan centang baris Transaction Role
16. Verifikasi sub-tab Transaction Role memuat kolom `Transaction`, `Role`, `Group`, dan `Actions`

### TC-FA-SU-31: Banner Tab Role per tingkat akses dan Group Manager

17. Klik segmen Breadcrumb `User`
18. Ketik Search `Lina Marlina`, tekan Enter
19. Klik nama `Lina Marlina`
20. Verifikasi banner info read-only "This user has Total Control access." tampil di atas tabel Sub-tab Global Role
21. Klik sub-tab Group Role
22. Verifikasi banner "This user has Total Control access." tampil di atas tabel Sub-tab Group Role
23. Verifikasi banner tanpa tombol aksi
24. Verifikasi tidak ada baris Total Control atau Read Only yang disisipkan ke tabel Global Role maupun Group Role
25. Klik sub-tab Transaction Role
26. Verifikasi banner "This user has Total Control access." tampil di atas tabel Sub-tab Transaction Role
27. Klik segmen Breadcrumb `User`
28. Ganti isi kotak search dengan `Citra Lestari`, tekan Enter
29. Klik nama `Citra Lestari`
30. Verifikasi banner "This user has Read Only access." tampil di atas tabel Sub-tab Global Role
31. Klik segmen Breadcrumb `User`
32. Ganti isi kotak search dengan `Oscar Pranata`, tekan Enter
33. Klik nama `Oscar Pranata`
34. Verifikasi banner "This user is a Group Manager for: Accounts Payable, IT Infrastructure." tampil dengan nama grup dipisah koma dan urut A-Z
35. Klik sub-tab Transaction Role
36. Verifikasi banner "This user is a Group Manager for: Accounts Payable, IT Infrastructure." tampil juga di atas tabel Sub-tab Transaction Role dengan nama grup urut A-Z (FI-20)
37. Klik segmen Breadcrumb `User`
38. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter
39. Klik nama `Budi Santoso`
40. Verifikasi tabel Sub-tab Global Role tampil tanpa banner (tanpa tingkat akses dan bukan Group Manager)

### TC-FA-SU-32: Screening Tab Responsibilities: label, sub-tab, dan empty state gabungan

41. Klik tab Responsibilities
42. Verifikasi label tab `Responsibilities (20)` dan sub-tab `Borrowed Assets (5)`, `Assigned Assets (5)`, `Pending Approvals (5)`, dan `Pending Tasks (5)`
43. Verifikasi keempat sub-tab tampil
44. Verifikasi angka tab `20` sama dengan jumlah baris seluruh sub-tab (5+5+5+5)
45. Klik segmen Breadcrumb `User`
46. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter
47. Klik nama `Hana Kusuma`
48. Klik tab Responsibilities
49. Verifikasi label tab `Responsibilities (0)` (angka tampil juga saat 0)
50. Verifikasi area konten menampilkan empty state "No pending responsibilities" dengan deskripsi "This user has no active custody, pending approvals, or tasks."
51. Verifikasi empty state menggantikan sub-tab switcher
52. Verifikasi tidak ada aksi tulis dan tidak ada tautan keluar dari tab Responsibilities
53. Klik segmen Breadcrumb `User`
54. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 17, 27, 31, 37, 45, dan 53 (kembali ke User List lewat Breadcrumb), langkah 18, 28, 32, 38, dan 46 (Search untuk menemukan baris target, R-16), langkah 54 (mengosongkan Search, S-09), langkah 13 dan 15 (centang dan hilangkan centang baris untuk mengamati `[Bulk Remove]`, S-09). Langkah 1, 19, 29, 33, 39, dan 47 membuka Detail; langkah 41 dan 48 membuka Tab Responsibilities.
- Langkah 35 (membuka Sub-tab Transaction Role Oscar Pranata) adalah langkah penghubung; langkah 26 dan 36 membuktikan banner tier dan banner Group Manager juga tampil di Sub-tab Transaction Role (TC-FA-SU-31 Expected a, c, d; TC-FA-SU-1074).
- Langkah 1 TC-FA-SU-32 ("Buka Tab Responsibilities pada Budi Santoso") dilanjutkan dari Detail Budi Santoso yang masih terbuka pada langkah 39.
- Langkah 24 (absence baris Total Control atau Read Only) beranchor banner pada langkah 20 dan 22; langkah 40 beranchor tabel Global Role yang termuat.
- Spec melewati sekitar 35 langkah (54 langkah). Seluruhnya satu kelas (screening tab Detail User, satu akun, tanpa mengubah data), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain.
- Pembagian TC lintas spec: Tab Non-Login User, Changelog, System Log, Transaction Admin Log, dan User Log (TC-FA-SU-33 dan 34) ada di spec 011.
- Temuan untuk QA:
  - Versi spec sebelumnya mengasersi Sub-tab Transaction Role Lina Marlina tanpa banner; ini bertentangan dengan TC-FA-SU-31 Expected a dan d terbaru (banner tier dan banner Group Manager tampil juga di Sub-tab Transaction Role). Langkah 26 dikoreksi dan langkah 35 dan 36 ditambahkan.
  - TC-FA-SU-30 Expected d menyebut `[Bulk Remove]` saat ada seleksi, tetapi Pre-setup #39 tidak memberi Transaction Role untuk Budi Santoso; spec mengikuti Langkah Uji TC (Budi Santoso) dan membutuhkan sedikitnya satu baris Transaction Role pada Budi Santoso (langkah 13), yang perlu dijamin seed.
  - TC-FA-SU-30 Expected b menyebut urut Role Name A-Z tanpa nilai; spec mengasersi urutan A-Z pada baris yang tampil (Budi Santoso memiliki lebih dari satu Global Role).
  - TC-FA-SU-31 Expected c menulis banner "Group Manager untuk dua grup" tanpa menyebut grup; spec memakai Oscar Pranata (Group Manager IT Infrastructure dan Accounts Payable, Pre-setup #23) dan nama grup urut A-Z.
  - TC-FA-SU-32 Expected b ("keempat sub-tab selalu tampil walau sebagian kosong") tidak punya pengguna dengan sebagian sub-tab kosong pada Pre-setup #24 dan #25; spec mengasersi keempat sub-tab pada Budi Santoso (semuanya berisi 5 baris) dan empty state gabungan pada Hana Kusuma.
