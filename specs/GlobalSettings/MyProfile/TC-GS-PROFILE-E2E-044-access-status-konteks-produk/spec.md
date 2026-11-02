---
id: TC-GS-PROFILE-E2E-044-access-status-konteks-produk
title: "Section Access & Status: Konteks Fixed Asset, Admin Console, Status Inactive, dan Produk Belum Ter-provision"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-194
  - TC-GS-PROFILE-195
  - TC-GS-PROFILE-196
  - TC-GS-PROFILE-197
  - TC-GS-PROFILE-198
coverage:
  web: automated
---

# Section Access & Status: Konteks Fixed Asset, Admin Console, Status Inactive, dan Produk Belum Ter-provision

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Pre-setup #1 (Andi Pratama, Total Control; Access Level Total Control di Fixed Asset; `Fixture.myProfile.accounts.totalControl.email`, `Spectra.env.GS_PROFILE_TC_PASSWORD`) untuk TC-GS-PROFILE-196. Akun default suite; login di hook `before`.
- Akun kedua (Step ganti akun): Pre-setup #5 (Sinta Maharani, Total Control; di Fixed Asset tanpa Access Level dengan Global Role "Manage asset master data", status Active; di Admin Console Global Role "Manage group", status Active; `Fixture.myProfile.accounts.multiAccess.email`, `Spectra.env.GS_PROFILE_MULTI_PASSWORD`) untuk TC-GS-PROFILE-195, 197, dan 198.
- Akun ketiga (Step ganti akun): Pre-setup #23 (Lina Marlina, Total Control; App Access Fixed Asset baru ditambahkan dan belum pernah login ke Fixed Asset; `Fixture.myProfile.accounts.unprovisioned.email`, `Spectra.env.GS_PROFILE_UNPROV_PASSWORD`) untuk TC-GS-PROFILE-194.
- Kemampuan teknis disediakan tim BE/FE: fixture BE yang menetapkan status Inactive akun Pre-setup #5 di Admin Console (status Active di Global Settings) untuk TC-GS-PROFILE-198 dan memulihkannya ke Active.
- State global dan pemulihan: status Pre-setup #5 di Admin Console diubah ke Inactive pada TC-GS-PROFILE-198 (diletakkan terakhir pada blok #5 setelah TC-GS-PROFILE-197 yang membutuhkan status Active), dipulihkan ke Active oleh langkah pemulihan spec dan di hook `after` spec ini (bukan bagian Hook suite 7).
- Hook suite berikut berlaku; lihat `suite.md`:
  - Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
  - Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
  - Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
  - Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Suite serial: `parallel: false`.

## Test Steps

### TC-GS-PROFILE-196: Konteks Fixed Asset, Access Level Total Control (Pre-setup #1)

1. Pilih opsi "Fixed Asset" pada Product Selector
2. Verifikasi Access Level: "Total Control" tampil bersama status "Active"

### Ganti akun ke Pre-setup #5

3. Logout
4. Login dengan `Fixture.myProfile.accounts.multiAccess.email` dan `Spectra.env.GS_PROFILE_MULTI_PASSWORD`
5. Buka My Profile dari account menu navbar

### TC-GS-PROFILE-195: Konteks Fixed Asset (Pre-setup #5)

6. Pilih opsi "Fixed Asset" pada Product Selector
7. Verifikasi daftar role: "Manage asset master data"
8. Verifikasi tidak ada Access Level
9. Verifikasi Status: "Active"
10. Verifikasi tidak ada kolom capability CRUD

### TC-GS-PROFILE-197: Konteks Admin Console (Pre-setup #5)

11. Pilih opsi "Admin Console" pada Product Selector
12. Verifikasi daftar role: "Manage group"
13. Verifikasi Status: "Active"

### TC-GS-PROFILE-198: Status Inactive di produk (Pre-setup #5)

14. Tetapkan status akun Pre-setup #5 di Admin Console menjadi Inactive lewat fixture BE, lalu muat ulang My Profile
15. Pilih opsi "Admin Console" pada Product Selector
16. Verifikasi konteks Admin Console: status "Inactive"
17. Pilih opsi "Global Settings" pada Product Selector
18. Verifikasi konteks Global Settings: status "Active"
19. Pulihkan status akun Pre-setup #5 di Admin Console menjadi Active lewat fixture BE

### Ganti akun ke Pre-setup #23

20. Logout
21. Login dengan `Fixture.myProfile.accounts.unprovisioned.email` dan `Spectra.env.GS_PROFILE_UNPROV_PASSWORD`
22. Buka My Profile dari account menu navbar

### TC-GS-PROFILE-194: Produk belum ter-provision (Pre-setup #23)

23. Pilih opsi "Fixed Asset" pada Product Selector
24. Verifikasi Section Access & Status menampilkan Illustration, judul "No access details yet", teks "Your access and status for this view will appear here."
25. Verifikasi tidak ada CTA dan tidak ada error state

## Notes

- Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-194, 195, 196, 197, 198). Tidak ada TC hanya-BE.
- Subjudul `###` memetakan langkah ke id TC. Blok per akun karena ada Step ganti akun eksplisit dan bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3, pemisah nyata butir b); semua TC satu topik (isi Section Access & Status per konteks produk). Urutan TC di spec mengikuti pengelompokan akun, bukan nomor TC.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 3 sampai 5 dan 20 sampai 22 (Step ganti akun), langkah 14 (mengatur status Inactive lewat fixture BE dan memuat ulang halaman), langkah 19 (pemulihan status).
- Langkah 7 menjadi anchor positif untuk asersi absence di langkah 8 dan 10, dan langkah 24 menjadi anchor untuk langkah 25 (bagian 8b butir 2).
- Temuan untuk QA:
  - Data Uji TC-GS-PROFILE-195, 197, dan 198 menyebut Pre-setup #5, konsisten dengan spec; TC-GS-PROFILE-196 dan 190 sama-sama memakai Pre-setup #1 untuk konteks berbeda.
  - Expected a dan b TC-GS-PROFILE-198 (status Inactive di Admin Console, Active di Global Settings) tidak menunjuk langkah pemilihan konteks; spec memilih Admin Console lalu mengasersi Inactive (langkah 15 dan 16), kemudian memilih Global Settings lalu mengasersi Active (langkah 17 dan 18).
  - Precondition TC-GS-PROFILE-198 ("status Inactive di Admin Console") tidak menyebut mekanisme penetapan status; ditulis sebagai fixture BE yang disediakan tim BE/FE tanpa endpoint karangan.
  - Pre-setup #23 (TC-GS-PROFILE-194) hanya valid selama akun belum pernah login ke Fixed Asset; spec tidak membuka Fixed Asset dengan akun itu, tetapi spec lain yang memakai akun yang sama dapat merusak syarat ini.
