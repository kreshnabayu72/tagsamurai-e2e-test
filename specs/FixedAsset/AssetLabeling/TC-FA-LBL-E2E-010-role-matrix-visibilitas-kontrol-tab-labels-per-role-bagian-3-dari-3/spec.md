---
id: TC-FA-LBL-E2E-010-role-matrix-visibilitas-kontrol-tab-labels-per-role-bagian-3-dari-3
title: "Role Matrix: Visibilitas Kontrol Tab Labels per Role (bagian 3/3)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-31
  - TC-FA-LBL-506
coverage:
  web: automated
---

# Role Matrix: Visibilitas Kontrol Tab Labels per Role (bagian 3/3)

## Prerequisites

- Mode: FE+BE.
- Hook suite: `before`, `beforeEach`, dan `after` berlaku sesuai `suite.md` (termasuk flag Guided Tooltip `seen`); spec ini tidak menulis ulang isinya.
- Role yang diuji (Full-CRUD login di hook `before` spec ini menggantikan akun default suite; halaman dibuka hook `beforeEach` suite; Default User lewat langkah Ganti akun; hook `after` mengembalikan sesi ke akun default suite, Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`):

| Role | Pre-setup | Akun (Fixture) | Env | TC | Langkah |
|---|---|---|---|---|---|
| Full-CRUD | #7 | `Fixture.assetLabeling.akun.fullCrud` | `Spectra.env.FA_FULLCRUD_PASSWORD` | TC-FA-LBL-31 | 1 sampai 12 |
| Default User (Total Control permanen) | #31 | `Fixture.assetLabeling.akun.defaultUser` | `Spectra.env.FA_DEFAULTUSER_PASSWORD` | TC-FA-LBL-506 | 13 sampai 19 |

- Environment variable: `FA_FULLCRUD_PASSWORD`, `FA_DEFAULTUSER_PASSWORD`, `FA_LBL_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Fixture: `Fixture.assetLabeling.*` (`fixtures/asset-labeling.json`) memuat identitas akun tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Data Pre-setup (dibaca saja, tidak diubah spec): #12 (katalog Company Alpha 9 label; dipakai: `Seasonal Event`).
- State global: tidak ada yang diubah selain sesi login. Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### Full-CRUD: TC-FA-LBL-31

1. Verifikasi Tab `Labels` tampil
2. Verifikasi tombol `[+ Label]` tampil dan aktif
3. Verifikasi kolom Checkbox dan Select All tampil
4. Klik `⋯` pada baris `Seasonal Event`
5. Verifikasi menu `⋯` baris `Seasonal Event` memuat: `Detail`, `Edit`, `Delete`
6. Verifikasi Search, Filter, Sort, Pagination, Download, Changelog, header kolom Actions (⋯), dan Setup Column tetap tampil dan aktif
7. Tutup menu `⋯` dengan Esc
8. Centang satu baris (`Seasonal Event`)
9. Verifikasi Bulk Action Bar tampil
10. Klik `Bulk Action`
11. Verifikasi overlay `Bulk Action` memuat `Delete` (icon `DeleteBin6Line`, severity danger)
12. Tutup overlay `Bulk Action` dan hilangkan centang baris `Seasonal Event`

### Default User: TC-FA-LBL-506

13. Ganti akun: Logout, login sebagai Default User `Fixture.assetLabeling.akun.defaultUser` (`Spectra.env.FA_DEFAULTUSER_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab `Labels`
14. Verifikasi Tab `Labels` tampil
15. Verifikasi tombol `[+ Label]` tampil dan aktif
16. Verifikasi kolom Checkbox dan Select All tampil
17. Klik `⋯` pada baris `Seasonal Event`
18. Verifikasi menu `⋯` baris `Seasonal Event` memuat: `Detail`, `Edit`, `Delete`
19. Verifikasi Search, Filter, Sort, Pagination, Download, Changelog, header kolom Actions (⋯), dan Setup Column tetap tampil dan aktif, sama dengan Total Control

## Notes

- Spec ditulis per blok role dengan langkah Ganti akun eksplisit (langkah 13) karena akun pertama login di hook `before` dan langkah tiap role berbeda (bagian 3a, varian A).
- Langkah penghubung (S-03): langkah 7 (menutup menu `⋯`), langkah 10 (klik `Bulk Action` untuk membuka overlay yang diasersi TC-FA-LBL-31 butir f), langkah 12 (menutup overlay dan menghilangkan centang).
- Langkah 19: asersi "sama dengan Total Control" diwujudkan sebagai daftar elemen yang sama dengan langkah 6 (Total Control diuji pada spec 008).
- Temuan untuk QA: Expected f TC-FA-LBL-31 menyebut overlay `Bulk Action` tanpa menyebut aksi membukanya; langkah 10 (klik `Bulk Action`) ditambahkan sebagai langkah penghubung. TC-FA-LBL-506 tidak memuat Bulk Action Bar walau Checkbox tampil; tidak ada asersi tambahan.
