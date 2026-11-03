---
id: TC-FA-RP-E2E-018-resilience-baca-error-load-dan-try-again-per-permukaan-2
title: "Resilience baca: Error load dan Try Again per permukaan (2/2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-69
  - TC-FA-RP-70
  - TC-FA-RP-71
coverage:
  web: automated
---

# Resilience baca: Error load dan Try Again per permukaan (2/2)

## Prerequisites

- Mode: FE+BE. Intercept parsial (`Spectra.intercept()`) di atas backend nyata: hanya respons baca yang disebut TC yang dipaksa berstatus 5xx; respons lain dan respons setelah intercept dilepas berasal dari backend nyata, karena TC mengharapkan `[Try Again]` memuat data nyata. Endpoint yang dicegat tidak tercantum di TC; nama endpoint ditentukan tim FE dari respons yang disebut TC (kandidat popup Assign, log Changelog, struktur group).
- Login di hook `before` spec ini sebagai Total Control Company Alpha (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `FA_TC_PASSWORD`).
- Akun aktor (password hanya lewat env); urutan baris = urutan pemakaian:

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati), Company Alpha | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |
| Total Control pada `Company Changelog` | #24 | disediakan tim FE (email tidak tertulis di Pre-setup TC; lihat Temuan untuk QA) | `Spectra.env.FA_CHANGELOG_TC_PASSWORD` |

- Data Pre-setup: #15 (pool pengguna sebagai kandidat popup Assign), #18 (pohon group), #24 (`Company Changelog`: log 25 entri campuran).
- Kemampuan teknis (disediakan tim FE): intercept respons HTTP dengan status 5xx pada surface yang disebut tiap langkah, dilepas segera sesudah asersi (S-09); hook `after` melepas intercept yang tersisa; akun Total Control `Company Changelog`.
- Spec tidak mengubah data dan tidak mengubah state global.

## Test Steps

### TC-FA-RP-71: Error load Sidebar Group Tree

1. Klik Tab `Group Manager`
2. Pasang intercept respons struktur group dengan status 5xx, lalu muat ulang Tab `Group Manager`
3. Verifikasi area konten menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
4. Verifikasi area konten bukan empty state
5. Verifikasi halaman tidak tertutup
6. Lepas intercept respons struktur group
7. Klik `[Try Again]`
8. Verifikasi data berhasil dimuat dan tampil normal

### TC-FA-RP-69: Error load popup Assign

9. Klik Tab `Total Control`
10. Pasang intercept respons kandidat dengan status 5xx, lalu klik `[+ Assign]`
11. Verifikasi area konten popup menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
12. Verifikasi area konten bukan empty state
13. Verifikasi popup tidak tertutup
14. Lepas intercept respons kandidat
15. Klik `[Try Again]`
16. Verifikasi data kandidat berhasil dimuat dan tampil normal
17. Klik `[✕]` untuk menutup popup

### Ganti akun ke Total Control Company Changelog

18. Logout dari akun Total Control Company Alpha, lalu login sebagai Total Control `Company Changelog` dengan `Spectra.env.FA_CHANGELOG_TC_PASSWORD`
19. Buka menu Settings > Role & Permission dari sidebar

### TC-FA-RP-70: Error load modal Changelog

20. Pasang intercept respons log dengan status 5xx, lalu klik ikon `Changelog`
21. Verifikasi area konten modal menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
22. Verifikasi area konten bukan empty state
23. Verifikasi modal tidak tertutup
24. Lepas intercept respons log
25. Klik `[Try Again]`
26. Verifikasi data log berhasil dimuat dan tampil normal
27. Klik `[✕]` untuk menutup modal Changelog

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-69, 70, 71). TC-FA-RP-64 sampai 68 ada di spec `TC-FA-RP-E2E-017-resilience-baca-error-load-dan-try-again-per-permukaan-1`.
- Spec ditulis per blok akun karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`); ganti akun pada langkah 18. Urutan TC di spec: TC-FA-RP-71, 69 (Company Alpha), lalu TC-FA-RP-70 (`Company Changelog`).
- Langkah penghubung (tanpa awalan `Verifikasi`): klik tab; memasang intercept sebagai pemicu kegagalan; melepas intercept segera sesudah asersi (S-09); klik `[Try Again]`; menutup popup dan modal dengan `[✕]`; ganti akun dan membuka menu.
- Temuan untuk QA:
  - TC-FA-RP-69, 70, dan 71 memakai frasa "blokir respons"; spec memaknainya sebagai intercept respons 5xx. Nama endpoint yang dicegat tidak tercantum di TC.
  - TC-FA-RP-69, 70, dan 71 mengasersi `[Try Again]` memuat data nyata, sehingga spec ini FE+BE dengan intercept parsial, bukan `Mode: mock` penuh (bagian 6 konvensi).
  - TC-FA-RP-70 merujuk Pre-setup #24 (`Company Changelog`); akun Total Control company itu tidak tertulis di Pre-setup TC dan disediakan tim FE. Bila #24 hanya data pada Company Alpha, langkah ganti akun tidak diperlukan.
  - Post Condition TC-FA-RP-69, 70, dan 71 tidak memberi langkah observasi tambahan; tidak diasersi.
