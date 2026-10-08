---
id: TC-GS-ROLE-E2E-059-tabel-utama-pencarian-toolbar-dan-scoping-kolom
title: "Pencarian Toolbar Tabel Utama Tab TC & RO: Ekspansi, Substring Name/Email, Case-Insensitive, dan Pengecualian Kolom Status/Role/Date"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-137
  - TC-GS-ROLE-138
  - TC-GS-ROLE-139
  - TC-GS-ROLE-140
  - TC-GS-ROLE-141
coverage:
  web: automated
---

# Pencarian Toolbar Tabel Utama Tab TC & RO: Ekspansi, Substring Name/Email, Case-Insensitive, dan Pengecualian Kolom Status/Role/Date

## Prerequisites

- Login sebagai Total Control
- Data Uji: Pre-setup data tabel utama
- Setup Hook: beforeEach: navigateTo(Tab Total Control)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Pre-setup tersedia; Tab Total Control dan Tab Read Only masing-masing berisi ≥3 user dengan Position/Division berbeda
- Ahmad Fauzi punya TAG "TG-00451"
- User berada di Global Settings > Role & Permission > Total Control

## Test Steps

### Siklus interaksi Search Tab Total Control dan Tab Read Only (TC-GS-ROLE-137)

1. Tab Total Control: klik icon Search
2. Ketik "dew"
3. Tekan Enter
4. Klik (✕)
5. Tekan Enter
6. Ketik "dew" + Enter lalu klik (←)
7. Ulangi langkah 1–6 di Tab Read Only dengan "rin"
8. Verifikasi Langkah 1: search bar melebar, auto-focus, placeholder "Search name..."
9. Verifikasi Langkah 2: icon (✕) muncul, tabel belum tersaring
10. Verifikasi Langkah 3: tabel hanya baris yang cocok
11. Verifikasi Langkah 4: input kosong, fokus tetap, tabel masih tersaring
12. Verifikasi Langkah 5: tabel kembali semua data
13. Verifikasi Langkah 6: search bar collapse dan tabel langsung reset
14. Verifikasi Tab Read Only: perilaku identik a–f

### Search kolom teks visible Tab Total Control dan Tab Read Only (TC-GS-ROLE-138)

15. Tab Total Control: search tiap keyword pada Data Uji + Enter, catat hasil
16. Ulangi di Tab Read Only dengan nilai baris Read Only
17. Verifikasi Name: baris Dewi Lestari cocok (case-insensitive)
18. Verifikasi Position: baris ber-Position mengandung "Manag" cocok (substring)
19. Verifikasi Division: baris Division Finance cocok
20. Verifikasi Modified By: baris dengan Modified By "Budi S" cocok
21. Verifikasi Tab Read Only: hasil per kolom identik pola a–d

### Search kolom badge Status, Activation Status, Temporary User di Tab Total Control/Read Only (TC-GS-ROLE-139)

22. Tab Total Control: search "inactive" + Enter
23. Search "Pending" + Enter (Activation Status Hidden)
24. Tampilkan kolom Activation Status dan Temporary User via Setup Column > Save
25. Search "Pending" + Enter
26. Search "Yes" + Enter
27. Verifikasi Status: keyword "inactive" (case-insensitive) menampilkan Dewi Lestari dan user Inactive lain di Tab Total Control
28. Verifikasi Activation Status: setelah kolom ditampilkan, keyword "Pending" menampilkan Rudi Hartono
29. Verifikasi Temporary User: setelah kolom ditampilkan, keyword "Yes" menampilkan user temporary
30. Verifikasi Saat kolom Activation Status disembunyikan, keyword "Pending" tidak mencocokkan

### Search kolom TAG saat di-hide dan setelah di-unhide (TC-GS-ROLE-140)

31. Search "TG-00451" + Enter (kolom TAG default Hidden)
32. Tampilkan kolom TAG via Setup Column > Save
33. Search "TG-00451" + Enter
34. Verifikasi Langkah 1: "No results found"
35. Verifikasi Langkah 3: baris Ahmad Fauzi cocok

### Search tidak mencocokkan kolom tanggal Last Updated dan Temporary Until (TC-GS-ROLE-141)

36. Search tanggal Last Updated baris Dewi Lestari (format tampil) + Enter
37. Search tanggal Temporary Until salah satu user + Enter
38. Verifikasi Kedua pencarian menampilkan "No results found"
39. Verifikasi Penyaringan tanggal hanya lewat Filter Panel

## Notes

- Memvalidasi alur skenario "Pencarian Toolbar Tabel Utama Tab TC & RO: Ekspansi, Substring Name/Email, Case-Insensitive, dan Pengecualian Kolom Status/Role/Date".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.2 Tab: Total Control; global-settings/role/PRD/role.md §5 Search; foundation/process/prd-process/prd-conventions.md §9.1; global-settings/role/PRD/role.md §4.1.1; global-settings/role/PRD/role.md §4.1.2; global-settings/role/PRD/role.md §5; global-settings/role/PRD/role.md §4.1.1 Name (badge kondisional Pending bukan teks Name, tidak tercakup Search); foundation/process/prd-process/prd-conventions.md §9.3; global-settings/role/PRD/role.md §4.1.1 TAG.
- Sumber pemetaan test case granular: TC-GS-ROLE-137, TC-GS-ROLE-138, TC-GS-ROLE-139, TC-GS-ROLE-140, TC-GS-ROLE-141.
