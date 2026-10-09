---
id: TC-GS-GSET-E2E-028-changelog-kombinasi-search-filter-sort-dan-page-size
title: "Kombinasi Modal Changelog: Search+Filter (irisan dan non-destruktif), Search+Filter+Sort+page size, ganti sort, Clear Field, dan reset kondisi default"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-151
  - TC-GS-GSET-152
  - TC-GS-GSET-153
  - TC-GS-GSET-154
  - TC-GS-GSET-155
  - TC-GS-GSET-156
  - TC-GS-GSET-182
coverage:
  web: automated
---

# Kombinasi Modal Changelog: Search+Filter (irisan dan non-destruktif), Search+Filter+Sort+page size, ganti sort, Clear Field, dan reset kondisi default

## Prerequisites

- Login sebagai Role: Total Control
- Changelog General Settings berisi baris riwayat (dinamis) dengan Field `Time Zone`, `Time Format`, `Session Idle Timeout`, `Currency Code`; Modified By `Budi S`

## Test Steps

### Search lalu Filter (Irisan, Keyword Tetap)

1. Search "Time" lalu `Enter`
2. Buka Filter, pilih Field `Time Zone`, klik `[Apply]`
3. Verifikasi tabel hanya menampilkan baris Field `Time Zone` yang cocok dengan keyword
4. Verifikasi kotak Search tetap berisi "Time" dan keyword tidak di-reset oleh Apply

### Filter lalu Search (Filter Tetap)

5. Kosongkan Search (Enter pada input kosong)
6. Buka Filter, pilih Field `Session Idle Timeout`, klik `[Apply]`
7. Search "hour" lalu `Enter`
8. Verifikasi tabel hanya menampilkan baris Field `Session Idle Timeout` yang Old Value atau New Value-nya memuat "hour"
9. Verifikasi Filter Field `Session Idle Timeout` tetap aktif (chip tetap tampil)

### Kombinasi Search + Filter + Sort + Page Size

10. Kosongkan Search
11. Search "Edit" lalu `Enter`
12. Buka Filter, pilih Modified By `Budi S`, klik `[Apply]`
13. Klik header Field sekali (Ascending)
14. Ubah page size ke 25
15. Verifikasi tabel hanya memuat baris yang cocok dengan keyword "Edit" dan Modified By `Budi S`, terurut Field A-Z, maksimal 25 baris per halaman, dan keempat kondisi aktif bersamaan tanpa saling menimpa

### Clear Search saat Filter dan Sort Aktif

16. Buka Filter, pilih Field `Session Idle Timeout`, klik `[Apply]`
17. Klik header Modified By sekali (Ascending)
18. Search "hour" lalu `Enter`
19. Klik `(✕)` lalu tekan `Enter` pada input kosong
20. Verifikasi keyword dilepas dan tabel menampilkan semua baris Field `Session Idle Timeout`
21. Verifikasi Filter Field dan sort Modified By Ascending tetap aktif

### Ganti Kolom Sort saat Search dan Filter Aktif

22. Search "Edit" lalu `Enter`
23. Buka Filter, pilih Field `Session Idle Timeout`, klik `[Apply]`
24. Klik header Field sekali (Ascending)
25. Klik header Modified By sekali (Ascending)
26. Verifikasi sort berpindah ke kolom Modified By (Ascending), indikator sort kolom Field hilang, dan keyword "Edit" serta filter Field tetap aktif

### No Results lalu Clear Field Memulihkan

27. Buka Filter, pilih Field `Currency Code`, klik `[Apply]`
28. Search "Time" lalu `Enter`
29. Verifikasi empty state "No results found" dengan "Try adjusting your search or filter."
30. Buka Filter, klik `[Clear Field]`, lalu klik `[Apply]`
31. Verifikasi tabel menampilkan baris yang cocok dengan keyword "Time" (Field `Time Zone`, `Time Format`, `Session Idle Timeout`)

### Reopen Modal → Kondisi Default

32. Klik icon Changelog dari halaman (jika perlu buka ulang): search "Edit", pilih Field `Session Idle Timeout`, klik `[Apply]`, klik header Modified By sekali (Ascending)
33. Tutup modal dengan `Esc`, lalu klik icon Changelog lagi
34. Verifikasi kotak Search kosong dan tabel tidak tersaring Search
35. Verifikasi Filter Panel tanpa kriteria (field Field menampilkan placeholder "All fields")
36. Verifikasi tidak ada indikator sort aktif pada Modified By dan urutan Date descending (Newest First)
37. Verifikasi Pagination halaman 1 dengan page size 10

## Notes

- Menggabungkan TC-GS-GSET-151, 152, 153, 154, 155, 156, dan 182 (kombinasi Search, Filter, Sort, page size). Salah satu spec terbesar; bila step > 35, pecah blok Reopen → Default ke spec terpisah.
