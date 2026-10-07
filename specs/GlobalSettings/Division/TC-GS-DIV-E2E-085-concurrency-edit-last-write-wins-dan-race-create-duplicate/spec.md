---
id: TC-GS-DIV-E2E-085-concurrency-edit-last-write-wins-dan-race-create-duplicate
title: "Konkurensi Antar-Admin: Last-Write-Wins pada Edit Bersamaan, Penolakan Duplicate Name, dan Penolakan Duplicate Manual Code"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-DIV-271
  - TC-GS-DIV-272
  - TC-GS-DIV-273
coverage:
  web: automated
---

# Konkurensi Antar-Admin: Last-Write-Wins pada Edit Bersamaan, Penolakan Duplicate Name, dan Penolakan Duplicate Manual Code

## Prerequisites

- Login sebagai Role: Total Control Admin A dan Admin B
- Dua sesi browser aktif (Admin A dan Admin B)
- Division "Strategy and Planning" (SNP) ada di entitas
- User berada di Global Settings > User > Division
- Division `Strategy and Planning` (Code `SNP`) ada
- Division `Shared Services` belum ada
- Code `OPX` belum dipakai

## Test Steps

### Dua admin mengedit Name Division yang sama: Save terakhir menimpa tanpa dialog konflik (TC-GS-DIV-271)

1. Admin A dan Admin B membuka Edit Division `Strategy and Planning`
2. Admin B mengubah Name menjadi `Strategy Office` lalu klik `[Save]`
3. Admin A mengubah Name menjadi `Planning Office` lalu klik `[Save]`
4. Buka Modal Changelog
5. Verifikasi Save Admin B sukses: toast `Success, division has been updated.`
6. Verifikasi Save Admin A juga sukses: toast `Success, division has been updated.` tanpa dialog konflik
7. Verifikasi Nama akhir `Planning Office` (Save terakhir menang)
8. Verifikasi Changelog mencatat dua entri Edit Name terpisah: `Strategy and Planning` ke `Strategy Office`, lalu `Strategy Office` ke `Planning Office`

### Dua admin membuat Division dengan Name sama bersamaan: yang kedua ditolak duplicate (TC-GS-DIV-272)

9. Admin A dan Admin B membuka Create Division dan mengisi Name `Shared Services` dengan Code berbeda
10. Admin A klik `[Submit]` lebih dulu
11. Admin B klik `[Submit]`
12. Verifikasi Create Admin A sukses dengan toast `Success, division has been created.`
13. Verifikasi Create Admin B ditolak: error inline `Division Name already exists` dan modal tetap terbuka
14. Verifikasi Hanya 1 Division `Shared Services` tersimpan

### Dua admin membuat Division dengan Code manual sama bersamaan: yang kedua ditolak duplicate (TC-GS-DIV-273)

15. Admin A mengisi Name `Operations X` Code `OPX`; Admin B mengisi Name `Operations Y` Code `OPX`
16. Admin A klik `[Submit]` lebih dulu
17. Admin B klik `[Submit]`
18. Verifikasi Create Admin A sukses
19. Verifikasi Create Admin B ditolak: error inline `Code already exists` dan modal tetap terbuka

## Notes

- Memvalidasi aturan NC-01 dan error-handling-convention.md §5.7: edit bersamaan pada record yang sama menganut last-write-wins tanpa dialog konflik versi, sedangkan submit create bersamaan dengan Name atau Code sama menghasilkan penolakan duplicate pada submit kedua (PRD §9.4.2 D6).
- Sumber pemetaan test case granular: TC-GS-DIV-271, TC-GS-DIV-272, TC-GS-DIV-273.
