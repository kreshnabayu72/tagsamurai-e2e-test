---
id: TC-GS-PROFILE-E2E-040-product-selector-daftar-opsi
title: "Product Selector: Daftar Opsi per App Access dan Produk yang Dicabut"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-178
  - TC-GS-PROFILE-179
  - TC-GS-PROFILE-180
  - TC-GS-PROFILE-181
coverage:
  web: automated
---

# Product Selector: Daftar Opsi per App Access dan Produk yang Dicabut

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Pre-setup #5 (Sinta Maharani, Total Control; App Access Global Settings, Fixed Asset, Admin Console, Supply Asset, SIEM; `Fixture.myProfile.accounts.multiAccess.email`, `Spectra.env.GS_PROFILE_MULTI_PASSWORD`) untuk TC-GS-PROFILE-178 dan 181. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (Step ganti akun): Pre-setup #2 (Rina Pratiwi, Read Only; App Access Global Settings dan Fixed Asset; `Fixture.myProfile.accounts.readOnly.email`, `Spectra.env.GS_PROFILE_RO_PASSWORD`) untuk TC-GS-PROFILE-179.
- Akun ketiga (Step ganti akun): Pre-setup #22 (Yoga Pratama, User Basic; App Access Supply Asset dan SIEM saja; `Fixture.myProfile.accounts.samsSiemOnly.email`, `Spectra.env.GS_PROFILE_SAMSSIEM_PASSWORD`) untuk TC-GS-PROFILE-180; My Profile dibuka dari Supply Asset (app asal tidak ada di opsi).
- Pelaku kedua admin: Pre-setup #6 (Hendra Wijaya, Total Control; `Fixture.myProfile.accounts.admin.email`, `Spectra.env.GS_PROFILE_ADMIN_PASSWORD`) mencabut dan memulihkan App Access Admin Console milik Pre-setup #5 lewat sesi API aktor (TC-GS-PROFILE-181); kemampuannya disediakan tim BE/FE.
- State global dan pemulihan: App Access Admin Console milik Pre-setup #5 dicabut pada TC-GS-PROFILE-181 dan dipulihkan oleh langkah pemulihan spec serta di hook `after` spec ini (bukan bagian Hook suite 7); fixture pemulihan disediakan tim BE/FE.
- Hook suite berikut berlaku; lihat `suite.md`:
  - Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
  - Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
  - Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
  - Pelaku kedua admin (Pre-setup #6) memicu perubahan state lewat sesi API aktor yang tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE. Lihat `suite.md`, Hook suite 4.
  - Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Suite serial: `parallel: false`.

## Test Steps

### TC-GS-PROFILE-178: Daftar opsi Pre-setup #5

1. Klik "Viewing: [Product ▾]"
2. Verifikasi opsi berurutan: "Admin Console", "Fixed Asset", "Global Settings"
3. Verifikasi tidak ada opsi "Supply Asset" maupun SIEM
4. Tutup daftar opsi Product Selector

### TC-GS-PROFILE-181: Produk yang App Access-nya dicabut (Pre-setup #5)

5. Admin Pre-setup #6 mencabut App Access Admin Console milik Pre-setup #5 lewat sesi API aktor hingga perubahan tersimpan
6. Muat ulang halaman My Profile (F5)
7. Klik "Viewing: [Product ▾]"
8. Verifikasi opsi memuat "Fixed Asset" dan "Global Settings"
9. Verifikasi opsi tidak memuat "Admin Console"
10. Admin Pre-setup #6 memulihkan App Access Admin Console milik Pre-setup #5 lewat sesi API aktor hingga perubahan tersimpan

### Ganti akun ke Pre-setup #2

11. Logout
12. Login dengan `Fixture.myProfile.accounts.readOnly.email` dan `Spectra.env.GS_PROFILE_RO_PASSWORD`
13. Buka My Profile dari account menu navbar

### TC-GS-PROFILE-179: Daftar opsi Pre-setup #2

14. Klik "Viewing: [Product ▾]"
15. Verifikasi opsi berurutan: "Fixed Asset", "Global Settings"

### Ganti akun ke Pre-setup #22

16. Logout
17. Login dengan `Fixture.myProfile.accounts.samsSiemOnly.email` dan `Spectra.env.GS_PROFILE_SAMSSIEM_PASSWORD`
18. Buka Supply Asset lalu buka My Profile dari account menu navbar

### TC-GS-PROFILE-180: Tanpa App Access Global Settings (Pre-setup #22)

19. Klik "Viewing: [Product ▾]"
20. Verifikasi opsi hanya "Global Settings"
21. Verifikasi Product Selector menampilkan "Viewing: Global Settings"
22. Verifikasi bagian Access Level dan System Role pada Section Access & Status diganti state kosong S-10: Illustration, judul "No access details yet", teks "Your access and status for this view will appear here.", tanpa CTA

## Notes

- Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-178, 179, 180, 181). Tidak ada TC hanya-BE.
- Subjudul `###` memetakan langkah ke id TC. Blok per akun karena ada Step ganti akun eksplisit dan bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3, pemisah nyata butir b); semua TC satu topik (daftar opsi Product Selector).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 4 (menutup daftar opsi), langkah 6 (muat ulang agar App Access terbaru terbaca; TC-GS-PROFILE-181 mensyaratkan App Access sudah dicabut sebelum halaman dibuka), langkah 10 (pemulihan App Access), langkah 11 sampai 13 dan 16 sampai 18 (Step ganti akun).
- Langkah 8 adalah anchor positif (opsi lain tampil pada daftar yang sama) sebelum asersi absence di langkah 9, dan langkah 2 adalah anchor untuk langkah 3 (bagian 8b butir 2).
- Temuan untuk QA:
  - Precondition TC-GS-PROFILE-181 menyebut App Access Admin Console "sudah dicabut admin" tanpa menyebut pelaku; spec memakai admin Pre-setup #6 lewat sesi API aktor.
  - TC-GS-PROFILE-180 memakai "Login sbg Role: User Basic" bersama akun Pre-setup #22 yang tidak punya App Access Global Settings; spec memakai akun Pre-setup #22 sebagai sumber dan membuka My Profile dari Supply Asset sesuai Precondition d.
