---
id: TC-FA-LBL-E2E-008-role-matrix-visibilitas-kontrol-tab-labels-per-role-bagian-1-dari-3
title: "Role Matrix: Visibilitas Kontrol Tab Labels per Role (bagian 1/3)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-25
  - TC-FA-LBL-26
  - TC-FA-LBL-27
coverage:
  web: automated
---

# Role Matrix: Visibilitas Kontrol Tab Labels per Role (bagian 1/3)

## Prerequisites

- Mode: FE+BE.
- Hook suite: `before`, `beforeEach`, dan `after` berlaku sesuai `suite.md` (termasuk flag Guided Tooltip `seen`); spec ini tidak menulis ulang isinya.
- Role yang diuji (Total Control login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; role lain lewat langkah Ganti akun; hook `after` mengembalikan sesi ke akun default suite, Total Control Company Alpha):

| Role | Pre-setup | Akun (Fixture) | Env | TC | Langkah |
|---|---|---|---|---|---|
| Total Control | #1 | `Fixture.assetLabeling.akun.totalControl` | `Spectra.env.FA_LBL_TC_PASSWORD` | TC-FA-LBL-25 | 1 sampai 12 |
| Read Only | #2 | `Fixture.assetLabeling.akun.readOnly` | `Spectra.env.FA_RO_PASSWORD` | TC-FA-LBL-26 | 13 sampai 23 |
| Create-Only | #3 | `Fixture.assetLabeling.akun.createOnly` | `Spectra.env.FA_CREATEONLY_PASSWORD` | TC-FA-LBL-27 | 24 sampai 30 |

- Environment variable: `FA_LBL_TC_PASSWORD`, `FA_RO_PASSWORD`, `FA_CREATEONLY_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Fixture: `Fixture.assetLabeling.*` (`fixtures/asset-labeling.json`) memuat identitas akun tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Data Pre-setup (dibaca saja, tidak diubah spec): #12 (katalog Company Alpha 9 label; dipakai: `Seasonal Event`); #13 (aset berlabel, untuk isi Drawer pada langkah 22).
- State global: tidak ada yang diubah selain sesi login. Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### Total Control: TC-FA-LBL-25

1. Verifikasi Tab `Labels` tampil
2. Verifikasi tombol `[+ Label]` tampil dan aktif
3. Verifikasi kolom Checkbox dan Select All tampil
4. Klik `⋯` pada baris `Seasonal Event`
5. Verifikasi menu `⋯` baris `Seasonal Event` memuat: `Detail`, `Edit`, `Delete`
6. Verifikasi Search, Filter, Sort, Pagination, Download, Changelog, header kolom Actions (⋯), dan Setup Column tetap tampil dan aktif
7. Tutup menu `⋯` dengan Esc
8. Klik centang baris `Seasonal Event`
9. Verifikasi Bulk Action Bar tampil
10. Klik `Bulk Action`
11. Verifikasi overlay `Bulk Action` memuat `Delete` (icon `DeleteBin6Line`, severity danger)
12. Tutup overlay `Bulk Action` dan hilangkan centang baris `Seasonal Event`

### Read Only: TC-FA-LBL-26

13. Ganti akun: Logout, login sebagai Read Only `Fixture.assetLabeling.akun.readOnly` (`Spectra.env.FA_RO_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab `Labels`
14. Verifikasi Tab `Labels` tampil
15. Verifikasi tombol `[+ Label]` Hidden (tidak dirender)
16. Verifikasi kolom Checkbox dan Select All Hidden (tidak dirender)
17. Klik `⋯` pada baris `Seasonal Event`
18. Verifikasi menu `⋯` baris `Seasonal Event` memuat `Detail` saja; `Edit` dan `Delete` Hidden
19. Verifikasi Search, Filter, Sort, Pagination, Download, Changelog, header kolom Actions (⋯), dan Setup Column tetap tampil dan aktif
20. Tutup menu `⋯` dengan Esc
21. Klik chip `Seasonal Event`
22. Verifikasi Drawer Tagged Asset terbuka
23. Tutup Drawer Tagged Asset

### Create-Only: TC-FA-LBL-27

24. Ganti akun: Logout, login sebagai Create-Only `Fixture.assetLabeling.akun.createOnly` (`Spectra.env.FA_CREATEONLY_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab `Labels`
25. Verifikasi Tab `Labels` tampil
26. Verifikasi tombol `[+ Label]` tampil dan aktif
27. Verifikasi kolom Checkbox dan Select All Hidden (tidak dirender)
28. Klik `⋯` pada baris `Seasonal Event`
29. Verifikasi menu `⋯` baris `Seasonal Event` memuat `Detail` saja; `Edit` dan `Delete` Hidden
30. Verifikasi Search, Filter, Sort, Pagination, Download, Changelog, header kolom Actions (⋯), dan Setup Column tetap tampil dan aktif

## Notes

- Spec ditulis per blok role dengan langkah Ganti akun eksplisit (langkah 13 dan 24) karena akun pertama login di hook `before` dan langkah tiap role berbeda (bagian 3a, varian A).
- Langkah penghubung (S-03): langkah 7 dan 20 (menutup menu `⋯` sebelum langkah berikutnya), langkah 12 (menutup overlay dan menghilangkan centang), langkah 23 (menutup Drawer), langkah 8 dan 10 (membuka Bulk Action Bar dan overlay `Bulk Action` yang dibutuhkan Expected f TC-FA-LBL-25; langkah 8 adalah aksi TC, langkah 10 adalah aksi pembuka overlay).
- Asersi `Hidden` pada langkah 15, 16, 27: Table Tools dan Tab `Labels` yang sudah termuat (langkah 14 dan 25) menjadi anchor permukaan (bagian 8b butir 2).
- Temuan untuk QA: Expected f TC-FA-LBL-25 menyebut overlay `Bulk Action` tanpa menyebut aksi membukanya; langkah 10 (klik `Bulk Action`) ditambahkan sebagai langkah penghubung.
