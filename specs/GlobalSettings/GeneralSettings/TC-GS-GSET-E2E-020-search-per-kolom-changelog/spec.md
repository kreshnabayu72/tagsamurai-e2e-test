---
id: TC-GS-GSET-E2E-020-search-per-kolom-changelog
title: Pencarian per kolom tabel changelog
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-44
  - TC-GS-GSET-45
  - TC-GS-GSET-46
  - TC-GS-GSET-47
  - TC-GS-GSET-48
  - TC-GS-GSET-49
coverage:
  web: automated
---

# Pencarian per kolom Action, Field, Old/New Value, dan Modified By

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Data changelog yang dikenal: baris A `Action=Edit`, `Field=Session Idle Timeout`,
  `Old Value=30 minutes`, `New Value=1 hour`, `Modified By=Olivia`.
- Baris B, C, D menyediakan variasi `Action=Edit`, `Field=Time Zone`, dan `Modified By` bervariasi.

## Test Steps

### Pencarian pada kolom Action & Field

1. Buka Modal Changelog
2. Masukkan pencarian `Edit`
3. Verifikasi seluruh baris dengan Action `Edit` tampil
4. Masukkan pencarian `Session`
5. Verifikasi baris dengan Field `Session Idle Timeout` tampil (pencocokan parsial)
6. Masukkan pencarian `zzz`; verifikasi no-result

### Pencarian pada kolom Old Value & New Value

7. Masukkan pencarian `30 minutes`
8. Verifikasi baris yang Old Value-nya `30 minutes` tampil
9. Masukkan pencarian `1 hour`
10. Verifikasi baris yang New Value-nya `1 hour` tampil
11. Masukkan pencarian `idle`; verifikasi pencarian juga mencocokkan teks nilai (bukan hanya label field)

### Pencarian pada kolom Modified By

12. Masukkan pencarian `Olivia`
13. Verifikasi baris dengan Modified By bernama `Olivia` tampil
14. Masukkan pencarian `oli` (parsial, case-insensitive)
15. Verifikasi tetap memunculkan baris Modified By `Olivia`

### Guard kolom Date

16. Masukkan pencarian berformat tanggal (misal `17/04` atau `2024-04`)
17. Verifikasi pencarian tidak membatasi hasil oleh kolom `Date Modified` (atau diperlakukan bukan
    filter tanggal sesuai PRD)
18. Verifikasi kolom Date Modified tidak bisa difilter lewat search (hanya lewat filter tanggal pada
    kolom filter yang sah)

### Cakupan pencarian hanya pada kolom diperbolehkan

19. Verifikasi pencarian tidak pernah mencocokkan isi kolom `Date Modified`
20. Verifikasi hasil konsisten saat query diketik ulang dan dihapus (state search box kembali terbuka)

## Notes

- Verifikasi cakupan sesuai PRD §3.4.x: search memberikan pencocokan parsial pada `Action`, `Field`,
  `Old Value`, `New Value`, dan `Modified By`, serta tidak menyentuh `Date Modified`.