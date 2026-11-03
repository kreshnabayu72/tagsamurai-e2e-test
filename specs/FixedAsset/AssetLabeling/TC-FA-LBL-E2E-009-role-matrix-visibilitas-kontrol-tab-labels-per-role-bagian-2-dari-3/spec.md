---
id: TC-FA-LBL-E2E-009-role-matrix-visibilitas-kontrol-tab-labels-per-role-bagian-2-dari-3
title: "Role Matrix: Visibilitas Kontrol Tab Labels per Role (bagian 2/3)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-28
  - TC-FA-LBL-29
  - TC-FA-LBL-30
coverage:
  web: automated
---

# Role Matrix: Visibilitas Kontrol Tab Labels per Role (bagian 2/3)

## Prerequisites

- Mode: FE+BE.
- Hook suite: `before`, `beforeEach`, dan `after` berlaku sesuai `suite.md` (termasuk flag Guided Tooltip `seen`); spec ini tidak menulis ulang isinya.
- Role yang diuji (Update-Only login di hook `before` spec ini menggantikan akun default suite; halaman dibuka hook `beforeEach` suite; role lain lewat langkah Ganti akun; hook `after` mengembalikan sesi ke akun default suite, Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`):

| Role | Pre-setup | Akun (Fixture) | Env | TC | Langkah |
|---|---|---|---|---|---|
| Update-Only | #4 | `Fixture.assetLabeling.akun.updateOnly` | `Spectra.env.FA_UPDATEONLY_PASSWORD` | TC-FA-LBL-28 | 1 sampai 6 |
| Delete-Only | #5 | `Fixture.assetLabeling.akun.deleteOnly` | `Spectra.env.FA_DELETEONLY_PASSWORD` | TC-FA-LBL-29 | 7 sampai 19 |
| Read-Capability | #6 | `Fixture.assetLabeling.akun.readCapability` | `Spectra.env.FA_READCAP_PASSWORD` | TC-FA-LBL-30 | 20 sampai 26 |

- Environment variable: `FA_UPDATEONLY_PASSWORD`, `FA_DELETEONLY_PASSWORD`, `FA_READCAP_PASSWORD`, `FA_LBL_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Fixture: `Fixture.assetLabeling.*` (`fixtures/asset-labeling.json`) memuat identitas akun tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Data Pre-setup (dibaca saja, tidak diubah spec): #12 (katalog Company Alpha 9 label; dipakai: `Seasonal Event`).
- State global: tidak ada yang diubah selain sesi login. Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### Update-Only: TC-FA-LBL-28

1. Verifikasi Tab `Labels` tampil
2. Verifikasi tombol `[+ Label]` Hidden (tidak dirender)
3. Verifikasi kolom Checkbox dan Select All Hidden (tidak dirender)
4. Klik `⋯` pada baris `Seasonal Event`
5. Verifikasi menu `⋯` baris `Seasonal Event` memuat `Detail` dan `Edit`; `Delete` Hidden
6. Verifikasi Search, Filter, Sort, Pagination, Download, Changelog, header kolom Actions (⋯), dan Setup Column tetap tampil dan aktif

### Delete-Only: TC-FA-LBL-29

7. Ganti akun: Logout, login sebagai Delete-Only `Fixture.assetLabeling.akun.deleteOnly` (`Spectra.env.FA_DELETEONLY_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab `Labels`
8. Verifikasi Tab `Labels` tampil
9. Verifikasi tombol `[+ Label]` Hidden (tidak dirender)
10. Verifikasi kolom Checkbox dan Select All tampil
11. Klik `⋯` pada baris `Seasonal Event`
12. Verifikasi menu `⋯` baris `Seasonal Event` memuat `Detail` dan `Delete`; `Edit` Hidden
13. Verifikasi Search, Filter, Sort, Pagination, Download, Changelog, header kolom Actions (⋯), dan Setup Column tetap tampil dan aktif
14. Tutup menu `⋯` dengan Esc
15. Centang satu baris (`Seasonal Event`)
16. Verifikasi Bulk Action Bar tampil
17. Klik `Bulk Action`
18. Verifikasi overlay `Bulk Action` hanya memuat `Delete` (icon `DeleteBin6Line`, severity danger)
19. Tutup overlay `Bulk Action` dan hilangkan centang baris `Seasonal Event`

### Read-Capability: TC-FA-LBL-30

20. Ganti akun: Logout, login sebagai Read-Capability `Fixture.assetLabeling.akun.readCapability` (`Spectra.env.FA_READCAP_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab `Labels`
21. Verifikasi Tab `Labels` tampil
22. Verifikasi tombol `[+ Label]` Hidden (tidak dirender)
23. Verifikasi kolom Checkbox dan Select All Hidden (tidak dirender)
24. Klik `⋯` pada baris `Seasonal Event`
25. Verifikasi menu `⋯` baris `Seasonal Event` memuat `Detail` saja; `Edit` dan `Delete` Hidden
26. Verifikasi Search, Filter, Sort, Pagination, Download, Changelog, header kolom Actions (⋯), dan Setup Column tetap tampil dan aktif

## Notes

- Spec ditulis per blok role dengan langkah Ganti akun eksplisit (langkah 7 dan 20) karena akun pertama login di hook `before` dan langkah tiap role berbeda (bagian 3a, varian A).
- Langkah penghubung (S-03): langkah 14 (menutup menu `⋯`), langkah 17 (klik `Bulk Action` untuk membuka overlay yang diasersi TC-FA-LBL-29 butir f), langkah 19 (menutup overlay dan menghilangkan centang).
- Asersi `Hidden` pada langkah 2, 3, 9, 22, 23: Tab `Labels` yang sudah termuat (langkah 1, 8, 21) menjadi anchor permukaan (bagian 8b butir 2).
- Temuan untuk QA: Expected f TC-FA-LBL-29 menyebut overlay `Bulk Action` tanpa menyebut aksi membukanya; langkah 17 (klik `Bulk Action`) ditambahkan sebagai langkah penghubung.
