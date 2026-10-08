---
id: TC-GS-DIV-E2E-063-changelog-search-per-kolom-dan-guard-date
title: "Pencarian Modal Changelog: Submit Enter, Pencarian pada 6 Kolom Teks, Guard Date Non-Searchable, Empty State No Results, dan Interaksi Toolbar Box"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-192
  - TC-GS-DIV-193
  - TC-GS-DIV-194
  - TC-GS-DIV-195
  - TC-GS-DIV-225
coverage:
  web: automated
---

# Pencarian Modal Changelog: Submit Enter, Pencarian pada 6 Kolom Teks, Guard Date Non-Searchable, Empty State No Results, dan Interaksi Toolbar Box

## Prerequisites

- Login sebagai Role: Total Control
- Modal Changelog terisi entri mutasi Create, Edit, dan Delete
- User berada di Global Settings > User > Division
- Riwayat Changelog Division terisi (Create dari TC-GS-DIV-30, Edit dan Delete dari TC Section 3; Modified By: Sari D, Rina M, Agus W, Dewi L)
- Riwayat memuat entri hasil TC-GS-DIV-101 (Edit Name `Accounting` menjadi `Accounting and Tax`) dan TC-GS-DIV-102 (Edit Code `PRC` menjadi `PROC`), Modified By `Sari D`

## Test Steps

### Empty state Modal Changelog saat Search tidak menemukan hasil (TC-GS-DIV-192)

1. Klik icon Changelog di Table Tools
2. Klik icon Search di modal, ketik `zzzzqq`, tekan Enter
3. Verifikasi Illustration (100x100)
4. Verifikasi Title: `No results found`
5. Verifikasi Description: `Try adjusting your search or filter.`

### Search Modal Changelog per kolom searchable (substring dan tanpa membedakan huruf besar kecil) (TC-GS-DIV-193)

6. Klik icon Changelog di Table Tools
7. Cari `edit` lalu Enter
8. Cari `accounting and` lalu Enter
9. Cari `code` lalu Enter
10. Cari `prc` lalu Enter
11. Cari `proc` lalu Enter
12. Cari `sari` lalu Enter
13. Verifikasi Action: `edit` menemukan baris Action `Edit`
14. Verifikasi Division Name: `accounting and` menemukan baris `Accounting and Tax`
15. Verifikasi Field: `code` menemukan baris Field `Code`
16. Verifikasi Old Value: `prc` menemukan baris Old Value `PRC`
17. Verifikasi New Value: `proc` menemukan baris New Value `PROC` (hasil juga memuat baris Create `Procurement` karena substring)
18. Verifikasi Modified By: `sari` menemukan baris Modified By `Sari D`

### Kolom Date tidak dapat dicari lewat Search Modal Changelog (TC-GS-DIV-194)

19. Klik icon Changelog di Table Tools
20. Ketik teks tanggal yang tampil pada kolom Date di Search lalu Enter
21. Verifikasi Tampil `No results found` (Date bukan kolom searchable); penyaringan tanggal hanya lewat Filter Panel

### Screening Filter Panel Modal Changelog (TC-GS-DIV-195)

22. Klik icon Changelog di Table Tools
23. Klik icon Filter di modal
24. Verifikasi Field `Date` (date range picker, placeholder `Select date`)
25. Verifikasi Field `Action` (multi-select searchable, placeholder `All actions`)
26. Verifikasi Field `Division Name` (multi-select searchable, placeholder `All divisions`)
27. Verifikasi Field `Field` (multi-select searchable, placeholder `All fields`)
28. Verifikasi Field `Modified By` (multi-select searchable, placeholder `All users`)
29. Verifikasi Aksi `[Clear Field]` dan `[Apply]`

### Search Modal Changelog: reveal, auto-focus, submit lewat Enter, clear, dan collapse (TC-GS-DIV-225)

30. Klik icon Changelog di Table Tools
31. Klik icon Search di modal
32. Ketik `edit` dan perhatikan tabel
33. Tekan Enter
34. Klik icon `(✕)`
35. Tekan Enter pada input kosong
36. Ketik `edit`, Enter, lalu klik icon panah `(←)`
37. Verifikasi Search bar melebar dan kursor auto-focus
38. Verifikasi Setelah mengetik tabel belum tersaring dan icon `(✕)` muncul
39. Verifikasi Setelah Enter tabel tersaring
40. Verifikasi Klik `(✕)` mengosongkan input tanpa mereset tabel
41. Verifikasi Enter pada input kosong mereset tabel
42. Verifikasi Klik `(←)` menutup search dan tabel langsung reset

## Notes

- Memvalidasi pencarian Changelog pada 6 kolom teks (Action, Division Name, Field, Old Value, New Value, Modified By), guard kolom Date non-searchable, empty state S-04, dan interaksi box pencarian (PRD §4.1.2, §5).
- Sumber pemetaan test case granular: TC-GS-DIV-192, TC-GS-DIV-193, TC-GS-DIV-194, TC-GS-DIV-195, TC-GS-DIV-225.
