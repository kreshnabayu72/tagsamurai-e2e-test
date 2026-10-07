---
id: TC-GS-DIV-E2E-004-empty-state-pencarian-dan-filter-tanpa-hasil
title: "Empty State Hasil Saring: Ilustrasi dan Keterangan No Results Found pada Search dan Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-6
  - TC-GS-DIV-7
coverage:
  web: automated
---

# Empty State Hasil Saring: Ilustrasi dan Keterangan No Results Found pada Search dan Filter

## Prerequisites

- Login sebagai Role: Total Control
- Tabel Division terisi data
- User berada di Global Settings > User > Division

## Test Steps

### Empty state tabel saat Search tidak menemukan hasil (TC-GS-DIV-6)

1. Klik icon Search
2. Ketik `zzzzqq` pada kotak Search
3. Tekan Enter
4. Verifikasi Tabel menampilkan Illustration (100x100)
5. Verifikasi Title: `No results found`
6. Verifikasi Description: `Try adjusting your search or filter.`

### Empty state tabel saat Filter Last Updated tidak menemukan hasil (TC-GS-DIV-7)

7. Klik icon Filter
8. Pilih Last Updated rentang tanggal sebelum seluruh Last Updated Division (mis. 1 Jan 2020 sampai 31 Jan 2020)
9. Klik [Apply]
10. Verifikasi Tabel menampilkan Illustration (100x100)
11. Verifikasi Title: `No results found`
12. Verifikasi Description: `Try adjusting your search or filter.`

## Notes

- Memvalidasi empty state tersaring (S-04) dengan ilustrasi 100x100, Title "No results found", dan Description "Try adjusting your search or filter." saat pencarian atau filter tanggal tidak menemukan data cocok (PRD §7).
- Sumber pemetaan test case granular: TC-GS-DIV-6, TC-GS-DIV-7.
