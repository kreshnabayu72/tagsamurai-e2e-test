---
id: TC-GS-GSET-E2E-021-changelog-search-interaksi-per-kolom-dan-guard
title: "Search Modal Changelog: siklus interaksi, pencarian per kolom, guard Date, dan kolom ter-hide"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-66
  - TC-GS-GSET-67
  - TC-GS-GSET-68
  - TC-GS-GSET-69
  - TC-GS-GSET-70
coverage:
  web: automated
---

# Search Modal Changelog: siklus interaksi, pencarian per kolom, guard Date, dan kolom ter-hide

## Prerequisites

- Login sebagai Role: Total Control
- Changelog General Settings berisi baris riwayat (dinamis): Field `Session Idle Timeout` (Old `30 minutes`, New `1 hour`), Field `Time Zone`, Modified By `Budi S`

## Test Steps

### Siklus Interaksi Search

1. Buka Modal Changelog, klik icon Search di toolbar
2. Verifikasi search bar melebar, kursor fokus, placeholder "Search action, field, or value..."
3. Ketik "Time"
4. Verifikasi icon `(✕)` muncul dan tabel belum tersaring
5. Tekan `Enter`
6. Verifikasi tabel menampilkan baris yang cocok dengan "Time"
7. Klik `(✕)`
8. Verifikasi input kosong, search bar tetap terbuka, dan tabel tetap menampilkan hasil search terakhir
9. Tekan `Enter` pada input kosong
10. Verifikasi tabel reset menampilkan semua data
11. Klik icon `(←)`
12. Verifikasi search bar menutup menjadi icon Search dan tabel langsung reset

### Search per Kolom dan Case-Insensitive

13. Search "Edit" lalu `Enter`; verifikasi semua baris ditemukan (Action selalu `Edit`)
14. Search "Session Idle" lalu `Enter`; verifikasi menemukan baris Field `Session Idle Timeout`
15. Search "Budi" lalu `Enter`; verifikasi menemukan baris Modified By `Budi S`
16. Search "edit" (huruf kecil) lalu `Enter`; verifikasi menemukan baris yang sama dengan "Edit"
17. Search "zzzz" lalu `Enter`; verifikasi empty state "No results found" + "Try adjusting your search or filter."

### Search Old Value dan New Value

18. Search "30 minutes" lalu `Enter`; verifikasi menemukan baris Field `Session Idle Timeout` dengan Old Value `30 minutes`
19. Kosongkan Search, lalu search "1 hour" lalu `Enter`; verifikasi menemukan baris Field `Session Idle Timeout` dengan New Value `1 hour`

### Guard Kolom Date

20. Ketik teks tanggal salah satu baris sesuai tampilan kolom Date lalu `Enter`
21. Verifikasi tabel tidak menemukan baris berdasarkan kolom Date (empty state "No results found" + "Try adjusting your search or filter."); penyaringan tanggal hanya lewat Filter Panel

### Kolom Ter-hide

22. Search "Session Idle" lalu `Enter` dan catat hasil (baris Field `Session Idle Timeout` ditemukan)
23. Kosongkan Search, buka Setup Column via header Actions (⋯) > `Setup Column...`, uncheck kolom Field, klik `[Save]`
24. Search "Session Idle" lalu `Enter`; verifikasi kata kunci tidak mencocokkan baris (empty state "No results found")
25. Buka Setup Column lagi, check kolom Field, klik `[Save]`
26. Search "Session Idle" lalu `Enter`; verifikasi kata kunci kembali mencocokkan

## Notes

- Menggabungkan TC-GS-GSET-66, 67, 68, 69, dan 70 (search Modal Changelog).
