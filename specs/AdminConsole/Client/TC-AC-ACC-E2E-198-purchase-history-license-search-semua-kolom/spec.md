---
id: TC-AC-ACC-E2E-198-purchase-history-license-search-semua-kolom
title: "Purchase History License: Search per Kolom Teks, Numerik, dan Kolom Tanggal yang Tidak Dicari"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-281
  - TC-AC-ACC-757
  - TC-AC-ACC-758
coverage:
  web: automated
---

# Purchase History License: Search per Kolom Teks, Numerik, dan Kolom Tanggal yang Tidak Dicari

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2/A3): C-01 "PT Sejahtera Abadi". Seed Purchase History (Tabel A3, F6) C-01: License sub-tab FAMS P-L1 (Professional / Fixed Asset / New / 12 months / Qty 500 / CV Mitra Sejati / Andi Wijaya / 01 Jan 2026 08:00), P-L2 (Professional / Fixed Asset / Additional / 12 months / Qty 150 / CV Mitra Sejati / Andi Wijaya / 20 Jun 2026 14:00), P-L3 (Growth / Addon: Maintenance / New / 6 months / Qty 50 / PT Distribusi Nusantara / Budi Santoso / 15 Mar 2026 11:00), P-L4 (Growth / Fixed Asset / New / 24 months / Qty 100 / PT Distribusi Nusantara / Citra Dewi / 02 Jan 2025 09:00); Subscription ID P-L1 dan P-L2 `SUBS-20260101-A1B2C`, P-L3 `SUBS-20260315-K9L0M`, P-L4 `SUBS-20250102-X7Y8Z`. Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- General Settings: Date Format dan Time Zone tenant uji tidak diubah (asersi tanggal mengikuti format General Settings).
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.
- Search hanya menyaring saat Enter; ukuran halaman Purchase History License diubah ke 100 baris pada langkah pertama sehingga seluruh seed tampil.

## Test Steps

### TC-AC-ACC-281: Search Purchase History License menemukan nilai kolom Subscription, Plan, Item, Purchase Type, Source, dan Action by

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Klik Tab `Subscription`, sub-tab `FAMS`
4. Ubah ukuran halaman Purchase History License menjadi 100 baris
5. Klik ikon Search pada toolbar Purchase History License, ketik `growth` lalu tekan Enter
6. Verifikasi Plan "growth": P-L3 (Qty 50) dan P-L4 (Qty 100) tampil
7. Verifikasi Plan "growth": P-L1 (Qty 500) tidak tampil
8. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `maintenance` dan tekan Enter
9. Verifikasi Item "maintenance": P-L3 (Qty 50) tampil
10. Verifikasi Item "maintenance": P-L1 (Qty 500) tidak tampil
11. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `additional` dan tekan Enter
12. Verifikasi Purchase Type "additional": P-L2 (Qty 150) tampil
13. Verifikasi Purchase Type "additional": P-L1 (Qty 500) tidak tampil
14. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `distribusi` dan tekan Enter
15. Verifikasi Source "distribusi": P-L3 (Qty 50) dan P-L4 (Qty 100) tampil
16. Verifikasi Source "distribusi": P-L1 (Qty 500) tidak tampil
17. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `citra` dan tekan Enter
18. Verifikasi Action by "citra": P-L4 (Qty 100) tampil
19. Verifikasi Action by "citra": P-L1 (Qty 500) tidak tampil
20. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `A1B2C` dan tekan Enter
21. Verifikasi Subscription "A1B2C": P-L1 (Qty 500) dan P-L2 (Qty 150) tampil
22. Verifikasi Subscription "A1B2C": P-L3 (Qty 50) dan P-L4 (Qty 100) tidak tampil

### TC-AC-ACC-757: Search Purchase History License kolom numerik: Duration dan Qty

23. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `6 months` dan tekan Enter
24. Verifikasi Duration "6 months": P-L3 (Qty 50) (Duration 6 months) tampil
25. Verifikasi Duration "6 months": P-L1 (Qty 500) (Duration 12 months) dan P-L4 (Qty 100) (Duration 24 months) tidak tampil
26. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `500` dan tekan Enter
27. Verifikasi Qty "500": P-L1 (Qty 500) tampil
28. Verifikasi Qty "500": P-L2 (Qty 150), P-L3 (Qty 50), dan P-L4 (Qty 100) tidak tampil

### TC-AC-ACC-758: Search Purchase History License tidak mencakup kolom tanggal: Activation Date, Expired Date, dan Date

29. Klik ikon ✕ pada input Search lalu tekan Enter
30. Catat teks sel Date baris P-L2, teks sel Activation Date baris P-L1, dan teks sel Expired Date baris P-L1 persis seperti tampil
31. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `teks sel Date baris P-L2 yang dicatat` dan tekan Enter
32. Verifikasi pencarian teks sel Date: tidak ada baris yang cocok, empty state "No results found" dengan deskripsi "Try adjusting your search or filter."
33. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `teks sel Activation Date baris P-L1 yang dicatat` dan tekan Enter
34. Verifikasi pencarian teks sel Activation Date: tidak ada baris yang cocok, empty state "No results found" dengan deskripsi "Try adjusting your search or filter."
35. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `teks sel Expired Date baris P-L1 yang dicatat` dan tekan Enter
36. Verifikasi pencarian teks sel Expired Date: tidak ada baris yang cocok, empty state "No results found" dengan deskripsi "Try adjusting your search or filter."
37. Klik ikon ✕ pada input Search lalu tekan Enter

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok berupa pencarian pada satu tabel dan satu dataset, tiap blok berdiri sendiri (membuka Detail Client sendiri lewat Search), dan kegagalan keras satu blok tidak membuat blok lain kehilangan makna.
- Langkah "Klik ikon ✕ ... tekan Enter" yang mengosongkan Search di antara kata kunci, langkah "Catat teks sel", dan pengosongan Search di akhir spec adalah langkah penghubung (S-03, S-09, bagian 8b butir 9).
- Pembagian TC lintas spec: Filter, Sort, dan screening kolom Purchase History License C-01 ada di spec lain; id TC masing-masing tetap satu spec.
- Temuan untuk QA (S-15): TC-758 meminta teks sel tanggal "persis seperti tampil" tanpa menyebut format tanggalnya (mengikuti General Settings); spec mencatat teks dari sel. Asersi absence memakai baris seed lain yang tampil pada kata kunci sebelumnya sebagai anchor (bagian 8b butir 2) dan empty state "No results found" sebagai anchor positif untuk TC-758. Post Condition seluruh TC `-`.
