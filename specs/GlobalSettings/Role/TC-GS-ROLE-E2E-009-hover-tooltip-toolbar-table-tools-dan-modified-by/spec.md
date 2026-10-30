---
id: TC-GS-ROLE-E2E-009-hover-tooltip-toolbar-table-tools-dan-modified-by
title: "Hover Tooltip Icon Table Tools pada Tab Total Control, Tab System, dan Detail, serta Tooltip Modified By"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-23
  - TC-GS-ROLE-25
coverage:
  web: automated
---

# Hover Tooltip Icon Table Tools pada Tab Total Control, Tab System, dan Detail, serta Tooltip Modified By

## Prerequisites

- Mode: mock.
- Seluruh API di-mock (spec dijalankan tim FE sebagai integration test, tanpa backend nyata). Spec tidak memakai hook suite Guided Tooltip; flag `guided_tooltip_seen_gs-role` diatur lewat respons mock yang disediakan tim FE (seen = true).
- Aktor: Ahmad Fauzi (Total Control, Pre-setup #1) sebagai identitas mock dengan akses Global Settings. Karena API di-mock, tidak ada login nyata dan tidak ada password. API pendukung di luar sumber modul (identitas pengguna, menu sidebar, flag Guided Tooltip) disediakan tim FE.
- Layar awal: hook `beforeEach` membuka Global Settings > Role & Permission dengan Tab Total Control aktif.
- Endpoint yang dipanggil halaman pada kondisi uji (`global-settings/role/API/openapi.yaml`, awalan `/v2/iam/products/{product}/roles`, semuanya `POST`):
  - `/access-level/list` (Tab Total Control): respons 200 berisi tiga baris. `Ahmad Fauzi`; `Budi Santoso` (`isDefault: true`); `Dewi Lestari` (`isActive: false`, `modifiedBy` = Budi Santoso, `fullName` "Budi Santoso") sehingga sel Modified By baris Dewi Lestari menampilkan "Budi S" (Pre-setup #3 dan precondition c TC-GS-ROLE-25).
  - `/access-level/options` (opsi Filter Tab Total Control; dipanggil bila halaman memuatnya): respons 200.
  - `/capabilities/list` (Tab System): respons 200 berisi enam role tetap dengan `totalUsers` ≥1.
  - `/capabilities/users/list` (Detail "Manage TAG"): respons 200 berisi beberapa baris.
  - `/capabilities/users/options` (opsi Filter Detail; dipanggil bila halaman memuatnya): respons 200.
  - Aliran SSE `user.role_assigned` (bila halaman berlangganan; disebut `low-level-design.md`) disediakan tim FE sebagai aliran tanpa event; endpoint aliran tidak disebut di sumber.
  - Modal Changelog dan Popup Assign tidak dibuka sehingga endpoint data keduanya tidak dipanggil.
- Respons mock sukses tidak dibaca ulang; isi baris hanya mendukung asersi tooltip.
- Kemampuan teknis: hover kursor pada icon Table Tools, header kolom, dan sel Modified By, serta pembacaan teks tooltip.

## Test Steps

### TC-GS-ROLE-25: Hover Modified By menampilkan nama lengkap

1. Arahkan kursor ke sel Modified By baris `Dewi Lestari`
2. Verifikasi sel Modified By baris `Dewi Lestari` menampilkan "Budi S"
3. Verifikasi tooltip menampilkan "Budi Santoso"

### TC-GS-ROLE-23: Hover tooltip icon Table Tools pada tiap surface

4. Arahkan kursor ke icon Search di Tab Total Control
5. Verifikasi tooltip "Search" tampil
6. Arahkan kursor ke icon Filter di Tab Total Control
7. Verifikasi tooltip "Filter" tampil
8. Arahkan kursor ke icon Download di Tab Total Control
9. Verifikasi tooltip "Download" tampil
10. Arahkan kursor ke icon Changelog di Tab Total Control
11. Verifikasi tooltip "Changelog" tampil
12. Arahkan kursor ke header (⋯) di Tab Total Control
13. Verifikasi tooltip "Column Visibility" tampil
14. Klik Tab System
15. Arahkan kursor ke icon Search di Tab System
16. Verifikasi tooltip "Search" tampil
17. Arahkan kursor ke icon Download di Tab System
18. Verifikasi tooltip "Download" tampil
19. Arahkan kursor ke icon Changelog di Tab System
20. Verifikasi tooltip "Changelog" tampil
21. Arahkan kursor ke header (⋯) di Tab System
22. Verifikasi tooltip "Column Visibility" tampil
23. Klik Role Name `Manage TAG`
24. Arahkan kursor ke icon Search di Detail
25. Verifikasi tooltip "Search" tampil
26. Arahkan kursor ke icon Filter di Detail
27. Verifikasi tooltip "Filter" tampil
28. Arahkan kursor ke icon Download di Detail
29. Verifikasi tooltip "Download" tampil
30. Arahkan kursor ke icon Changelog di Detail
31. Verifikasi tooltip "Changelog" tampil
32. Arahkan kursor ke header (⋯) di Detail
33. Verifikasi tooltip "Column Visibility" tampil

## Notes

- Mode: mock. Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: TC-GS-ROLE-25 dijalankan lebih dulu karena memakai Tab Total Control yang sudah termuat; TC-GS-ROLE-23 menyusul dan berpindah ke Tab System lalu Detail.
- Langkah penghubung (bukan dari TC sumber, tanpa `Verifikasi`): pindah ke Tab System (langkah 14) dan membuka Detail (langkah 23). Tiap tooltip diasersi segera setelah hover pada icon yang bersangkutan, sebelum hover berikutnya menggantinya (8b butir 5).
- Temuan untuk QA:
  - TC-GS-ROLE-25 menyebut sel Modified By "Budi S" tanpa menyebut aturan singkatan; spec memakai data mock yang menghasilkan "Budi S" sesuai Expected.
  - TC-GS-ROLE-23 Expected a, b, c tidak menyebut apakah tooltip hilang setelah kursor pindah; spec tidak mengasersi hilangnya tooltip.
