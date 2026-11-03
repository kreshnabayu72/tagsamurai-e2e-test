---
id: TC-GS-NLU-E2E-083-list-sort-bagian-2-kolom-curated-custom-field-per-kelas-data
title: "List Sort bagian 2: sort tiga tahap kolom curated Custom Field per kelas data (teks, numerik, dropdown, tanggal)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-484
  - TC-GS-NLU-485
  - TC-GS-NLU-486
  - TC-GS-NLU-489
coverage:
  web: automated
---

# List Sort bagian 2: sort tiga tahap kolom curated Custom Field per kelas data (teks, numerik, dropdown, tanggal)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1; `{namaCompany}` diisi sesuai Client uji). Login sekali di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password lewat `Spectra.env.GS_TC_PASSWORD`, tidak ditulis di spec atau fixture.
- Layar awal: Global Settings > User > User List > sub-tab Non-Login User, dibuka hook `beforeEach` suite.
- Data Pre-setup (No. 13; hanya dibaca): Custom Field dasar `Blood Type` (Dropdown A/B/O/AB), `Emergency Phone` (Phone), dan `Badge Note` (Text), semua Active dan tidak Required.
- Data Dinamis (di-seed hook `before` lewat API, mekanisme disediakan tim FE/BE; dihapus hook `after`): Custom Field `Skor Uji` (Numeric, 0 desimal, Active) dan `Tanggal Uji` (Date, Active) hanya selama spec ini; sisa field bernama sama dari run sebelumnya dibersihkan hook `before`. Tiga Non-Login User milik spec (Division `Operations`, Represented By `Ahmad Fauzi`, Active): `Sortir CF Satu {runId}-083`, `Sortir CF Dua {runId}-083`, `Sortir CF Tiga {runId}-083`, dengan nilai Custom Field berikut (menggantikan `Sortir CF Satu/Dua/Tiga` Pre-setup agar Pre-setup tidak ditulis dan hasil Search tidak bercampur):

| Custom Field | Satu | Dua | Tiga |
|---|---|---|---|
| `Badge Note` | `Bravo` | `Alfa` | `Charlie` |
| `Emergency Phone` | `+62 81200000003` | `+62 81200000001` | `+62 81200000002` |
| `Skor Uji` | `100` | `9` | `20` |
| `Blood Type` | `B` | `A` | `O` |
| `Tanggal Uji` | hari ini +10 | hari ini +5 | hari ini +20 |

- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-non-login-user` true untuk akun Total Control dan hook suite `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pembacaan urutan baris; penghapusan preferensi kolom di browser di hook `after` (disediakan tim FE; spec ini menyimpan konfigurasi kolom lewat Setup Column).
- State global: konfigurasi kolom (kolom Badge Note, Emergency Phone, Skor Uji, Blood Type, Tanggal Uji diaktifkan) dipulihkan hook `after`; Custom Field `Skor Uji` dan `Tanggal Uji` dibuat dan dihapus hook. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-484: Sort 3 tahap kelas teks pada kolom curated Custom Field Badge Note dan Emergency Phone

1. Klik `⋯` header Actions > `Setup Column...`, centang kolom Badge Note dan Emergency Phone, klik `[Save]`
2. Ketik Search `{runId}-083`, tekan Enter (menyaring ketiga record milik spec)
3. Klik header `Badge Note`
4. Verifikasi Badge Note klik #1 ascending: Dua, Satu, Tiga
5. Klik header `Badge Note`
6. Verifikasi Badge Note klik #2 descending: Tiga, Satu, Dua
7. Klik header `Badge Note`
8. Verifikasi Badge Note klik #3 kembali ke default sort Name A-Z: Dua, Satu, Tiga
9. Klik header `Emergency Phone`
10. Verifikasi Emergency Phone klik #1 ascending: Dua, Tiga, Satu
11. Klik header `Emergency Phone`
12. Verifikasi Emergency Phone klik #2 descending: Satu, Tiga, Dua
13. Klik header `Emergency Phone`
14. Verifikasi Emergency Phone klik #3 kembali ke default sort Name A-Z

### TC-GS-NLU-485: Sort 3 tahap kelas numerik pada kolom curated Custom Field Skor Uji memakai nilai angka

15. Klik `⋯` header Actions > `Setup Column...`, centang kolom Skor Uji, klik `[Save]`
16. Klik header `Skor Uji`
17. Verifikasi klik #1 ascending berdasarkan nilai angka: Dua `9`, Tiga `20`, Satu `100` (bukan urutan teks)
18. Klik header `Skor Uji`
19. Verifikasi klik #2 descending: Satu `100`, Tiga `20`, Dua `9`
20. Klik header `Skor Uji`
21. Verifikasi klik #3 kembali ke default sort Name A-Z

### TC-GS-NLU-486: Sort 3 tahap kelas dropdown pada kolom curated Custom Field Blood Type

22. Klik `⋯` header Actions > `Setup Column...`, centang kolom Blood Type, klik `[Save]`
23. Klik header `Blood Type`
24. Verifikasi klik #1 ascending A-Z: Dua `A`, Satu `B`, Tiga `O`
25. Klik header `Blood Type`
26. Verifikasi klik #2 descending Z-A: Tiga `O`, Satu `B`, Dua `A`
27. Klik header `Blood Type`
28. Verifikasi klik #3 kembali ke default sort Name A-Z

### TC-GS-NLU-489: Sort 3 tahap kelas tanggal pada kolom curated Custom Field Tanggal Uji

29. Klik `⋯` header Actions > `Setup Column...`, centang kolom Tanggal Uji, klik `[Save]`
30. Klik header `Tanggal Uji`
31. Verifikasi klik #1 `Oldest First`: Dua, Satu, Tiga
32. Klik header `Tanggal Uji`
33. Verifikasi klik #2 `Newest First`: Tiga, Satu, Dua
34. Klik header `Tanggal Uji`
35. Verifikasi klik #3 kembali ke default sort Name A-Z
36. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): Search `{runId}-083` menyaring ketiga record milik spec (langkah dipakai ulang oleh TC-GS-NLU-485, TC-GS-NLU-486, dan TC-GS-NLU-489 karena Search tetap aktif; TC mengulang "Ketik `Sortir CF` pada Search"), dan `(←)` terakhir yang mengosongkan Search.
- Nama `Sortir CF Satu/Dua/Tiga` pada Expected TC dibaca sebagai `Sortir CF Satu/Dua/Tiga {runId}-083`; urutan Name A-Z (Dua, Satu, Tiga) tidak berubah karena suffix.
- Di atas 35 langkah, alasan: Spec ini sekitar 36 langkah dan dipertahankan utuh karena seluruh blok satu kelas harness (fungsional, tabel List yang sama, data milik spec) dan berdiri sendiri: kegagalan sort satu kelas data tidak membuat kelas lain kehilangan makna.
- Temuan untuk QA:
  - TC-GS-NLU-484 sampai TC-GS-NLU-489 memakai Name `Sortir CF Satu/Dua/Tiga` Pre-setup yang bercampur dengan record milik spec jika Search `Sortir CF` dipakai; spec memakai Search `{runId}-083`.
  - TC-GS-NLU-485 dan TC-GS-NLU-489 mensyaratkan Custom Field `Skor Uji` dan `Tanggal Uji` Active hanya selama TC; nama literal mengikuti TC (Lampiran A tidak memuat pengecualian S-12 untuk modul ini; `suite.md` menyatakan field uji dibuat dan dibersihkan hook).
  - Spec ini menyimpan konfigurasi kolom lewat Setup Column, tetapi `suite.md` belum mendaftarkannya pada daftar spec Setup Column.
