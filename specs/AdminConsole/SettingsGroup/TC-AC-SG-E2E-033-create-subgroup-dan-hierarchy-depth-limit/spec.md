---
id: TC-AC-SG-E2E-033-create-subgroup-dan-hierarchy-depth-limit
title: "Create Subgroup dan Hierarchy Depth Limit: Limit-1, Sama dengan Limit, Limit+1, Level 1, Cek Ulang Server, dan Penurunan Limit"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-107
  - TC-AC-SG-108
  - TC-AC-SG-109
  - TC-AC-SG-110
  - TC-AC-SG-111
  - TC-AC-SG-112
coverage:
  web: automated
---

# Create Subgroup dan Hierarchy Depth Limit: Limit-1, Sama dengan Limit, Limit+1, Level 1, Cek Ulang Server, dan Penurunan Limit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas `Distributor Pohon Dalam` (Pre-setup #26) `totalControlPohonDalam_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_POHONDALAM_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data: entitas `Distributor Pohon Dalam` dengan pohon rantai `Level 1` > `Level 2` > `Level 3` > `Level 4` > `Level 5` (Pre-setup #26). Hierarchy Depth Limit awal 5 (nilai minimum range 5 sampai 100); level 1 dihitung depth 1 dan root "All Groups" tidak dihitung. Node pada rantai itu adalah node Pre-setup yang menjadi parent aksi (pengecualian S-06); group yang dibuat memakai nama bersuffix milik spec.
- Data Dinamis (nama dari TC diberi suffix per run, S-12):

| TC | Nama di TC | Nama di spec | Parent |
|---|---|---|---|
| TC-AC-SG-107 | `Level 4 Baru` | `Level 4 Baru-{runId}-033` | `Level 3` (depth 3) |
| TC-AC-SG-108 | `Level 5 Baru` | `Level 5 Baru-{runId}-033` | `Level 4` (depth 4) |
| TC-AC-SG-110 | `Level Satu Baru` | `Level Satu Baru-{runId}-033` | level 1 |
| TC-AC-SG-111 | `Level 6 Cek Ulang` (tidak pernah tersimpan) | `Level 6 Cek Ulang` | `Level 5` (depth 5) |

- State global: Hierarchy Depth Limit entitas `Distributor Pohon Dalam` diubah menjadi 6 lalu 5 pada TC-AC-SG-111 dan TC-AC-SG-112 lewat konfigurasi lingkungan uji (seed) yang disediakan tim FE (tidak ada akun pengubah System Limits di Pre-setup); hook `after` memulihkannya ke 5 (lihat `suite.md`).
- Kemampuan teknis: Fixture BE (seeding, pemulihan baseline pohon `Distributor Pohon Dalam`, dan pengaturan Hierarchy Depth Limit) disediakan tim FE/BE (lihat `suite.md`). Pelaku "Sesi B" pada TC-AC-SG-111 diganti pemicu Fixture BE yang menurunkan limit (bukan sesi UI kedua).
- Pemulihan: hook `before` dan `after` memulihkan baseline pohon (hanya `Level 1` sampai `Level 5`) dan limit 5.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SG-107: Depth limit-1 diizinkan

1. Klik ikon `⋯` pada node `Level 3` di sidebar, lalu pilih "+ Add Subgroup"
2. Verifikasi Popup Add Subgroup terbuka tanpa dialog blok (group baru berada di depth 4 = limit-1)
3. Ketik `Level 4 Baru-{runId}-033` pada Group Name, klik `[Submit]`
4. Verifikasi subgroup `Level 4 Baru-{runId}-033` dibuat di bawah `Level 3`
5. Verifikasi toast sukses: "Success, group has been created."

### TC-AC-SG-108: Depth sama dengan limit diizinkan

6. Klik ikon `⋯` pada node `Level 4` di sidebar, lalu pilih "+ Add Subgroup"
7. Verifikasi Popup Add Subgroup terbuka tanpa dialog blok (depth group baru 5 = limit)
8. Ketik `Level 5 Baru-{runId}-033` pada Group Name, klik `[Submit]`
9. Verifikasi subgroup `Level 5 Baru-{runId}-033` dibuat di bawah `Level 4`
10. Verifikasi toast sukses: "Success, group has been created."

### TC-AC-SG-109: Depth limit+1 diblok dengan dialog

11. Klik ikon `⋯` pada node `Level 5` di sidebar
12. Verifikasi pilihan "+ Add Subgroup" enabled sebelum diklik
13. Klik "+ Add Subgroup"
14. Verifikasi dialog blok: Title "Cannot Add Group", body "You've reached the platform limit of 5 levels. Contact support if you need a higher limit.", tombol `[OK]` tanpa CTA upgrade plan
15. Verifikasi Popup Create tidak dibuka
16. Klik `[OK]` pada dialog
17. Verifikasi dialog tertutup tanpa group baru

### TC-AC-SG-110: `[+] Group` level 1 tidak dicek Hierarchy Depth Limit

18. Klik `[+] Group` di Sidebar Group Tree
19. Verifikasi Popup New Group terbuka tanpa dialog depth
20. Ketik `Level Satu Baru-{runId}-033` pada Group Name, klik `[Submit]`
21. Verifikasi group level 1 `Level Satu Baru-{runId}-033` dibuat
22. Verifikasi toast sukses: "Success, group has been created."
23. Pulihkan baseline pohon `Distributor Pohon Dalam` lewat Fixture BE

### TC-AC-SG-111: Server mengecek ulang limit saat Submit

24. Atur Hierarchy Depth Limit entitas menjadi 6 lewat konfigurasi lingkungan uji (seed)
25. Klik ikon `⋯` pada node `Level 5` di sidebar, lalu pilih "+ Add Subgroup"
26. Ketik `Level 6 Cek Ulang` pada Group Name tanpa Submit
27. Verifikasi Popup Add Subgroup tetap terbuka (depth group baru 6 = limit)
28. Ubah Hierarchy Depth Limit entitas menjadi 5 (batas minimum) lewat konfigurasi lingkungan uji (seed) sehingga depth group baru (6) melebihi batas
29. Klik `[Submit]`
30. Verifikasi dialog tampil: Title "Cannot Add Group" dengan body "You've reached the platform limit of 5 levels. Contact support if you need a higher limit."
31. Verifikasi group `Level 6 Cek Ulang` tidak dibuat
32. Klik `[OK]` pada dialog

### TC-AC-SG-112: Limit diturunkan tidak memangkas group existing

33. Kosongkan Group Name pada popup Add Subgroup `Level 5` lewat `[Clear Field]`
34. Klik `✕` pada popup Add Subgroup
35. Atur Hierarchy Depth Limit entitas menjadi 6 lewat konfigurasi lingkungan uji (seed)
36. Turunkan Hierarchy Depth Limit entitas menjadi 5 (batas minimum) saat pohon sudah sedalam 5
37. Muat ulang halaman `Settings > Group`
38. Klik ikon `⋯` pada node `Level 5` di sidebar, lalu pilih "+ Add Subgroup"
39. Verifikasi dialog blok "Cannot Add Group" tampil
40. Verifikasi seluruh `Level 1` sampai `Level 5` tetap ada dan tidak berubah
41. Verifikasi tidak ada notifikasi proaktif tentang penurunan limit
42. Klik `[OK]` pada dialog

## Notes

- Spec ini 42 langkah, di atas smell sekitar 35 langkah. Alasan: satu topik (Hierarchy Depth Limit pada Add Subgroup) pada satu entitas uji dan satu aktor. Limit awal 5 diatur di hook `before` dan dipulihkan di `after`, tetapi TC-AC-SG-111 dan TC-AC-SG-112 mengubah limit di tengah spec (langkah 24, 28, 35, dan 36); memecahnya menjadi spec sendiri mengulang penyiapan entitas dan limit. Parent aksi adalah node Pre-setup rantai `Level 1` sampai `Level 5` (pengecualian S-06; baseline dipulihkan pada langkah 23 dan di hook), sedangkan group yang dibuat milik spec. Tiap blok berdiri sendiri dengan parent atau state limit-nya sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): langkah 23 (pemulihan baseline pohon antar blok TC), langkah 24, 28, 35, dan 36 (pengaturan limit sebagai langkah TC), langkah 32 (menutup dialog setelah Verifikasi langkah 30), langkah 42 (`[OK]` menutup dialog setelah Verifikasi langkah 39 sampai 41), langkah 33 dan 34 (pemulihan form: Group Name `Level 6 Cek Ulang` dikosongkan lalu popup ditutup lewat `✕`, S-08 dan S-09; form kosong tidak memicu dialog Unsaved Changes sehingga tidak ada form dirty saat reload langkah 37).
- Langkah 41: absence notifikasi didahului langkah 39 dan 40 (dialog dan data tree tampil) sebagai anchor positif.
- TC-AC-SG-111 dan TC-AC-SG-112 memakai Fixture BE untuk mengubah limit sebagai pemicu state; tidak ada konteks UI kedua.
- Temuan untuk QA:
  - TC-AC-SG-111 memakai istilah Sesi A dan Sesi B tanpa akun pengubah System Limits; spec memakai pemicu Fixture BE tanpa akun karangan (S-13).
  - TC-AC-SG-111 tidak menyebut keadaan popup Add Subgroup sesudah dialog "Cannot Add Group" ditutup (tetap terbuka dengan input "Level 6 Cek Ulang" atau tertutup); spec mengasumsikan popup masih terbuka sehingga langkah 33 dan 34 dapat dijalankan; bila popup tertutup sendiri setelah `[OK]`, langkah 33 gagal dan perilaku itu perlu dipastikan tim FE.
  - TC-AC-SG-111 mengatur limit 6 setelah halaman dibuka; TC tidak menyebut apakah FE membaca limit saat halaman dimuat atau saat klik "+ Add Subgroup".
  - TC-AC-SG-112 Expected "tanpa notifikasi proaktif" tidak menyebut lokasi pengamatan; spec mengasersi tidak ada toast atau dialog di luar dialog "Cannot Add Group".

