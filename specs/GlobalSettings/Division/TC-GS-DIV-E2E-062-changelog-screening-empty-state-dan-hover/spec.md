---
id: TC-GS-DIV-E2E-062-changelog-screening-empty-state-dan-hover
title: "Screening Modal Changelog Division: Pembukaan via Toolbar, Read-Only Tanpa Row Action, Default Sort Date Newest, Empty State, dan Hover Tooltip"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-188
  - TC-GS-DIV-189
  - TC-GS-DIV-190
  - TC-GS-DIV-191
  - TC-GS-DIV-224
  - TC-GS-DIV-230
coverage:
  web: automated
---

# Screening Modal Changelog Division: Pembukaan via Toolbar, Read-Only Tanpa Row Action, Default Sort Date Newest, Empty State, dan Hover Tooltip

## Prerequisites

- Login sebagai Role: Total Control
- Klik icon [Changelog] pada toolbar tabel
- User berada di Global Settings > User > Division
- Riwayat Changelog Division terisi (Create dari TC-GS-DIV-30, Edit dan Delete dari TC Section 3; Modified By: Sari D, Rina M, Agus W, Dewi L)
- Entri Create, Delete, dan Edit tersedia dengan Modified By `Sari D`
- Entitas tanpa riwayat Changelog Division sama sekali
- Division 120 karakter sudah dibuat (TC-GS-DIV-37)

## Test Steps

### Screening Modal Changelog: Division (TC-GS-DIV-188)

1. Klik icon Changelog di Table Tools
2. Verifikasi Title `Changelog: Division`
3. Verifikasi Icon close `[✕]`
4. Verifikasi Toolbar: `Search | Filter | Download`
5. Verifikasi Kolom: `Date (sortable) | Action (sortable) | Division Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Column Visibility (⋯) (unsortable — header klik = buka overlay Column Visibility → CTA [Setup Column] di dalamnya)`
6. Verifikasi Tidak ada kolom checkbox dan tidak ada row action; Filter Panel tersembunyi secara default
7. Verifikasi Pagination: default 10 data per halaman

### Format isi sel Modal Changelog: strip, nama singkat, dan hover Modified By (TC-GS-DIV-189)

8. Klik icon Changelog di Table Tools
9. Lihat baris Create dan baris Delete
10. Hover nama pada kolom Modified By
11. Perhatikan kolom Action dan Division Name
12. Verifikasi Baris Create: Old Value tampil `—`
13. Verifikasi Baris Delete: New Value tampil `—`
14. Verifikasi Modified By tampil `Sari D` dan hover menampilkan tooltip nama lengkap `Sari Dewi`
15. Verifikasi Action tampil sebagai teks biasa (bukan badge)
16. Verifikasi Date tampil memakai format tanggal dan jam General Settings

### Urutan default Modal Changelog adalah tanggal terbaru di atas (TC-GS-DIV-190)

17. Klik icon Changelog di Table Tools
18. Perhatikan urutan baris dan ikon sort kolom Date
19. Verifikasi Baris terurut Date descending (terbaru di atas)
20. Verifikasi Ikon sort kolom Date menunjukkan Newest First

### Empty state Modal Changelog saat belum ada riwayat (TC-GS-DIV-191)

21. Klik icon Changelog di Table Tools
22. Verifikasi Illustration (100x100)
23. Verifikasi Title: `No changelog yet`
24. Verifikasi Description: `Activities and changes will appear here.`

### Hover icon toolbar Modal Changelog menampilkan tooltip (TC-GS-DIV-224)

25. Klik icon Changelog di Table Tools
26. Hover icon Search
27. Hover icon Filter
28. Hover icon Download
29. Verifikasi Tooltip `Search`
30. Verifikasi Tooltip `Filter`
31. Verifikasi Tooltip `Download`

### Nilai panjang pada kolom Old Value dan New Value tampil penuh (TC-GS-DIV-230)

32. Klik icon Changelog di Table Tools
33. Cari entri Create Division 120 karakter
34. Perhatikan kolom New Value dan Division Name
35. Verifikasi New Value dan Division Name tampil utuh tanpa pemotongan `..`
36. Verifikasi Kolom melebar atau teks wrap natural mengikuti isi

## Notes

- Memvalidasi modal Changelog: Division (size lg), tabel T-DIV-02 read-only tanpa row action, urutan default Date Newest first, S-03 empty state "No changelog yet", format strip (—), hover Modified By, dan nilai panjang tampil penuh (PRD §4.1.2, §7, §8.1).
- Sumber pemetaan test case granular: TC-GS-DIV-188, TC-GS-DIV-189, TC-GS-DIV-190, TC-GS-DIV-191, TC-GS-DIV-224, TC-GS-DIV-230.
