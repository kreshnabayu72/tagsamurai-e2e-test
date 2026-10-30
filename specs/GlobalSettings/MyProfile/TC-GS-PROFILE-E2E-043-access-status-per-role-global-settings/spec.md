---
id: TC-GS-PROFILE-E2E-043-access-status-per-role-global-settings
title: "Role Matrix: Section Access & Status Konteks Global Settings per Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-190
  - TC-GS-PROFILE-191
  - TC-GS-PROFILE-192
  - TC-GS-PROFILE-193
coverage:
  web: automated
---

# Role Matrix: Section Access & Status Konteks Global Settings per Role

## Prerequisites

- Mode: FE+BE
- Role yang diuji (Role Matrix visibilitas; langkah dan hasil berbeda per role sehingga spec ditulis per blok role):

  | Role | Akun Pre-setup | Email | Env password | Blok |
  |---|---|---|---|---|
  | Total Control | #1 (Andi Pratama; App Access Global Settings, Fixed Asset, Admin Console; Access Level Total Control; status Active) | `Fixture.myProfile.accounts.totalControl.email` | `Spectra.env.GS_PROFILE_TC_PASSWORD` | TC-GS-PROFILE-190 |
  | Read Only | #2 (Rina Pratiwi; Access Level Read Only) | `Fixture.myProfile.accounts.readOnly.email` | `Spectra.env.GS_PROFILE_RO_PASSWORD` | TC-GS-PROFILE-191 |
  | System Role | #3 (Dewi Lestari; tanpa Access Level; role individual "Manage user and role") | `Fixture.myProfile.accounts.systemRole.email` | `Spectra.env.GS_PROFILE_SYSROLE_PASSWORD` | TC-GS-PROFILE-192 |
  | User Basic | #4 (Budi Santoso; tanpa Access Level dan tanpa role individual GS; App Access Fixed Asset saja) | `Fixture.myProfile.accounts.userBasic.email` | `Spectra.env.GS_PROFILE_BASIC_PASSWORD` | TC-GS-PROFILE-193 |

- Akun pertama (Pre-setup #1) adalah akun default suite dan login di hook `before`; ketiga akun lain login lewat Step ganti akun eksplisit.
- Data: tidak ada data yang dibuat atau diubah; spec hanya membaca Section Access & Status. TC-GS-PROFILE-193 membuka My Profile dari Fixed Asset (app asal; satu-satunya App Access Pre-setup #4).
- Hook suite berikut berlaku; lihat `suite.md`:
  - Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
  - Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
  - Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
  - Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Suite serial: `parallel: false`.

## Test Steps

### TC-GS-PROFILE-190: Total Control (Pre-setup #1)

1. Amati Section Access & Status dengan Product Selector "Viewing: Global Settings"
2. Verifikasi User Type badge: "Total Control"
3. Verifikasi daftar product access memuat "Global Settings", "Fixed Asset", "Admin Console"
4. Verifikasi Access Level: "Total Control"
5. Verifikasi Status: "Active"

### Ganti akun ke Read Only (Pre-setup #2)

6. Logout
7. Login dengan `Fixture.myProfile.accounts.readOnly.email` dan `Spectra.env.GS_PROFILE_RO_PASSWORD`
8. Buka My Profile dari account menu navbar

### TC-GS-PROFILE-191: Read Only (Pre-setup #2)

9. Amati Section Access & Status konteks Global Settings
10. Verifikasi User Type badge: "Read Only"
11. Verifikasi Access Level: "Read Only"
12. Verifikasi Status: "Active"

### Ganti akun ke System Role (Pre-setup #3)

13. Logout
14. Login dengan `Fixture.myProfile.accounts.systemRole.email` dan `Spectra.env.GS_PROFILE_SYSROLE_PASSWORD`
15. Buka My Profile dari account menu navbar

### TC-GS-PROFILE-192: System Role (Pre-setup #3)

16. Amati Section Access & Status konteks Global Settings
17. Verifikasi User Type badge: "Admin"
18. Verifikasi System Role: "Manage user and role"
19. Verifikasi tidak ada Access Level
20. Verifikasi Status: "Active"

### Ganti akun ke User Basic (Pre-setup #4)

21. Logout
22. Login dengan `Fixture.myProfile.accounts.userBasic.email` dan `Spectra.env.GS_PROFILE_BASIC_PASSWORD`
23. Buka Fixed Asset lalu buka My Profile dari account menu navbar

### TC-GS-PROFILE-193: User Basic (Pre-setup #4)

24. Amati Product Selector
25. Verifikasi Product Selector menampilkan "Viewing: Fixed Asset" (default mengikuti app asal, S-04)
26. Pilih opsi "Global Settings" pada Product Selector
27. Verifikasi Product Selector menampilkan "Viewing: Global Settings"
28. Amati Section Access & Status konteks Global Settings
29. Verifikasi bagian Access Level dan System Role diganti state kosong: Illustration, judul "No access details yet", teks "Your access and status for this view will appear here.", tanpa CTA
30. Verifikasi User Type badge: "Basic"
31. Verifikasi daftar product access: "Fixed Asset"
32. Verifikasi Status: "Active"
33. Klik "Viewing: [Product ▾]"
34. Verifikasi opsi "Global Settings" tetap ada di Product Selector

## Notes

- Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-190, 191, 192, 193). Tidak ada TC hanya-BE.
- Role Matrix visibilitas satu daftar elemen (User Type badge, daftar product access, Access Level, System Role, Status, state kosong) dengan hasil berbeda per role; title tanpa kata "Positif" atau "Negatif" (bagian 3a). Spec ditulis per blok role karena langkah dan hasil tiap role berbeda dan ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 6 sampai 8, 13 sampai 15, dan 21 sampai 23 (Step ganti akun), langkah 33 (membuka daftar opsi agar butir Expected g TC-GS-PROFILE-193 teramati).
- Langkah 18 menjadi anchor positif untuk asersi absence di langkah 19 (Access Level tidak ada), dan langkah 25 sampai 28 mengikuti urutan state TC-GS-PROFILE-193 (bagian 8b butir 5).
- Temuan untuk QA:
  - Data Uji TC-GS-PROFILE-193 menulis "Login sbg Role: User Basic" dengan Pre-setup #4 yang membuka My Profile dari Fixed Asset; hook `beforeEach` suite membuka My Profile dari Global Settings (akun #4 tidak punya App Access Global Settings), sehingga langkah 23 membuka Fixed Asset secara eksplisit.
