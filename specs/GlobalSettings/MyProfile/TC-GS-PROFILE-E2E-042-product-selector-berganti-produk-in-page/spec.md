---
id: TC-GS-PROFILE-E2E-042-product-selector-berganti-produk-in-page
title: "Product Selector: Berganti Produk In-Page, Loading, Refresh, dan Buka Ulang Kembali ke Default"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-186
  - TC-GS-PROFILE-187
  - TC-GS-PROFILE-199
  - TC-GS-PROFILE-200
coverage:
  web: automated
---

# Product Selector: Berganti Produk In-Page, Loading, Refresh, dan Buka Ulang Kembali ke Default

## Prerequisites

- Mode: FE+BE
- Akun aktor: Pre-setup #5 (Sinta Maharani, Total Control; App Access Global Settings, Fixed Asset, Admin Console, Supply Asset, SIEM; `Fixture.myProfile.accounts.multiAccess.email`, `Spectra.env.GS_PROFILE_MULTI_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Kemampuan teknis: (a) `Spectra.intercept()` parsial di atas backend nyata yang menahan respons fetch Access & Status selama 3 detik pada TC-GS-PROFILE-187 (hanya untuk mengamati loading, bukan kelas b; path request disediakan tim FE karena `openapi.yaml` dan `low-level-design.md` tidak ada di folder modul); intercept dilepas segera sesudah TC-nya (S-09); (b) penanda DOM `window.__marker` disetel lewat eksekusi skrip pada halaman (TC-GS-PROFILE-186).
- Data: tidak ada data yang dibuat atau diubah. Jeda nyata: tidak ada selain penahanan respons 3 detik.
- Hook suite berikut berlaku; lihat `suite.md`:
  - Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
  - Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
  - Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
  - Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Suite serial: `parallel: false`.

## Test Steps

### TC-GS-PROFILE-186: Berganti produk in-page

1. Setel penanda DOM `window.__marker` pada halaman
2. Catat URL halaman
3. Catat isi Header dan Section Identity
4. Pilih opsi "Fixed Asset" pada Product Selector
5. Verifikasi URL tidak berubah dan tidak ada navigasi penuh
6. Verifikasi `window.__marker` masih ada (halaman tidak reload)
7. Verifikasi Header dan Section Identity tidak berubah dari isi yang dicatat di langkah 3
8. Verifikasi Section Access & Status dirender ulang untuk konteks Fixed Asset (Product Selector menampilkan "Viewing: Fixed Asset")

### TC-GS-PROFILE-187: Loading pada Section Access & Status

9. Tahan respons fetch Access & Status selama 3 detik
10. Pilih opsi "Admin Console" pada Product Selector
11. Verifikasi indikator loading tampil pada Section Access & Status selama fetch
12. Tunggu Section Access & Status selesai memuat
13. Lepas penahanan respons fetch Access & Status

### TC-GS-PROFILE-199: Refresh mengembalikan ke default

14. Pilih opsi "Fixed Asset" pada Product Selector
15. Muat ulang halaman (F5)
16. Verifikasi Product Selector menampilkan "Viewing: Global Settings" (default)

### TC-GS-PROFILE-200: Buka ulang My Profile mengembalikan ke default

17. Pilih opsi "Admin Console" pada Product Selector
18. Klik item navigasi lain
19. Buka My Profile dari account menu navbar
20. Verifikasi Product Selector menampilkan "Viewing: Global Settings"

## Notes

- Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-186, 187, 199, 200). Tidak ada TC hanya-BE.
- Subjudul `###` memetakan langkah ke id TC. Penahanan respons pada TC-GS-PROFILE-187 hanya untuk mengamati loading, bukan kelas b (prinsip 13).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 3 (baseline isi Header dan Section Identity untuk Expected c TC-GS-PROFILE-186), langkah 12 dan 13 (menunggu fetch selesai dan melepas intercept), langkah 14 (memilih produk selain default sebelum muat ulang; TC-GS-PROFILE-199 memulai dari My Profile di Global Settings yang sudah dibuka hook), langkah 17 sampai 19 (TC-GS-PROFILE-200 langkah 2 dan 3).
- Temuan untuk QA:
  - TC-GS-PROFILE-186 Expected c dan d ("Header dan Section Identity tidak berubah", "hanya Section Access & Status yang dirender ulang") tidak menyebut baseline; spec mencatat isi Header dan Section Identity sebelum aksi dan memakai `window.__marker` sesuai Precondition d.
  - TC-GS-PROFILE-187 tidak menyebut apa yang diamati sesudah loading selesai; tidak ada asersi tambahan.
