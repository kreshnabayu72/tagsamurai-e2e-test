---
id: TC-GS-PROFILE-E2E-041-product-selector-default-sesuai-app-asal
title: "Product Selector: Default Mengikuti App Asal Navigasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-182
  - TC-GS-PROFILE-183
  - TC-GS-PROFILE-184
  - TC-GS-PROFILE-185
coverage:
  web: automated
---

# Product Selector: Default Mengikuti App Asal Navigasi

## Prerequisites

- Mode: FE+BE
- Akun aktor: Pre-setup #5 (Sinta Maharani, Total Control; App Access Global Settings, Fixed Asset, Admin Console, Supply Asset, SIEM; `Fixture.myProfile.accounts.multiAccess.email`, `Spectra.env.GS_PROFILE_MULTI_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data: tidak ada data yang dibuat atau diubah; keempat TC memakai akun yang sama dan hanya berbeda app asal navigasi (Global Settings, Fixed Asset, Admin Console, Supply Asset).
- State global: tidak ada yang diubah; tidak ada pemulihan selain hook `after` suite.
- Hook suite berikut berlaku; lihat `suite.md`:
  - Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
  - Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
  - Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
  - Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Suite serial: `parallel: false`.

## Test Steps

### TC-GS-PROFILE-182: App asal Global Settings

1. Buka halaman lain di Global Settings (meninggalkan My Profile)
2. Klik icon Profile di navbar
3. Klik "My Profile"
4. Verifikasi Product Selector menampilkan "Viewing: Global Settings"

### TC-GS-PROFILE-183: App asal Fixed Asset

5. Buka Fixed Asset
6. Klik icon Profile di navbar
7. Klik "My Profile"
8. Verifikasi Product Selector menampilkan "Viewing: Fixed Asset"

### TC-GS-PROFILE-184: App asal Admin Console

9. Buka Admin Console
10. Klik icon Profile di navbar
11. Klik "My Profile"
12. Verifikasi Product Selector menampilkan "Viewing: Admin Console"

### TC-GS-PROFILE-185: App asal Supply Asset (tidak ada di opsi)

13. Buka Supply Asset
14. Klik icon Profile di navbar
15. Klik "My Profile"
16. Verifikasi Product Selector menampilkan "Viewing: Global Settings"

## Notes

- Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-182, 183, 184, 185). Tidak ada TC hanya-BE.
- Subjudul `###` memetakan langkah ke id TC. Satu akun dan satu topik; variasi app asal berurutan (prinsip 4).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1, 5, 9, dan 13 (menuju app asal sesuai Precondition "User berada di ..."; halaman My Profile dari hook `beforeEach` ditinggalkan agar navigasi ke My Profile dari app asal diuji).
- Temuan untuk QA: tidak ada.
