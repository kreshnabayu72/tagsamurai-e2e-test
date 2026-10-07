---
id: TC-GS-DIV-E2E-068-changelog-sorting-3-state-dan-null-placement
title: "Sorting 7 Kolom Modal Changelog: Alphabetical A-Z, Tanggal Newest/Oldest, dan Penempatan Nilai Kosong/Em-dash (—) di Akhir pada Old/New Value"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-206
  - TC-GS-DIV-207
  - TC-GS-DIV-208
coverage:
  web: automated
---

# Sorting 7 Kolom Modal Changelog: Alphabetical A-Z, Tanggal Newest/Oldest, dan Penempatan Nilai Kosong/Em-dash (—) di Akhir pada Old/New Value

## Prerequisites

- Login sebagai Role: Total Control
- Modal Changelog terisi riwayat Create, Edit, dan Delete
- User berada di Global Settings > User > Division
- Riwayat Changelog Division terisi (Create dari TC-GS-DIV-30, Edit dan Delete dari TC Section 3; Modified By: Sari D, Rina M, Agus W, Dewi L)

## Test Steps

### Sort 3-state kolom teks Action, Division Name, Field, dan Modified By (TC-GS-DIV-206)

1. Klik icon Changelog di Table Tools
2. Klik header Action tiga kali
3. Ulangi untuk Division Name, Field, dan Modified By
4. Verifikasi Tiap kolom: klik 1 ascending A-Z, klik 2 descending Z-A, klik 3 kembali ke default Date terbaru di atas

### Sort 3-state kolom Date Modal Changelog (TC-GS-DIV-207)

5. Klik icon Changelog di Table Tools
6. Klik header Date tiga kali
7. Verifikasi Klik 1: Oldest First
8. Verifikasi Klik 2: Newest First
9. Verifikasi Klik 3: kembali ke default Date terbaru di atas

### Sort kolom Old Value dan New Value menempatkan nilai kosong di akhir saat ascending (TC-GS-DIV-208)

10. Klik icon Changelog di Table Tools
11. Klik header Old Value sekali (ascending)
12. Klik header New Value sekali (ascending)
13. Verifikasi Old Value ascending: baris dengan Old Value `—` (Create) berada paling akhir
14. Verifikasi New Value ascending: baris dengan New Value `—` (Delete) berada paling akhir

## Notes

- Memvalidasi sorting pada seluruh 7 kolom T-DIV-02: Action, Division Name, Field, Modified By secara A-Z; Date Newest/Oldest; dan penempatan khusus nilai kosong/em-dash (—) selalu di akhir pada pengurutan ascending kolom campuran Old/New Value (PRD §4.1.2, prd-conventions.md §9.7).
- Sumber pemetaan test case granular: TC-GS-DIV-206, TC-GS-DIV-207, TC-GS-DIV-208.
