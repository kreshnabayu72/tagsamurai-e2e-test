---
id: TC-AC-ACC-E2E-218-resilience-tabel-tab-subscription-tag-dan-hardware
title: "Resilience: Error State dan Try Again pada Tabel Tab Subscription, TAG, dan Hardware"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-853
  - TC-AC-ACC-854
coverage:
  web: automated
---

# Resilience: Error State dan Try Again pada Tabel Tab Subscription, TAG, dan Hardware

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2): C-01 "PT Sejahtera Abadi". Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis (kelas b, fault injection): `Spectra.intercept()` di atas backend nyata untuk memaksa response data tiap tabel (License Quota, Purchase History License, Quota TAG, Purchase History TAG, Hardware List, Quota, Purchase History Hardware) menjadi 5xx lalu dipulihkan menjadi 200; endpoint tiap tabel tidak disebut TC sehingga daftar endpoint disediakan tim FE (S-13). Intercept dilepas segera setelah pemicu selesai (S-09) dan hook `after` melepas intercept yang tersisa.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-853: Error state gagal memuat tabel Tab Subscription dan Tab TAG dan pulih dengan Try Again

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Aktifkan intercept 5xx pada response data tabel License Quota, lalu klik Tab `Subscription`, sub-tab `FAMS`
4. Verifikasi tabel License Quota menampilkan "Unable to load this data." dengan tombol `[Try Again]`
5. Lepas intercept, lalu klik `[Try Again]` pada tabel License Quota
6. Verifikasi tabel License Quota menampilkan data normal
7. Verifikasi state error tabel License Quota hilang
8. Aktifkan intercept 5xx pada response data tabel Purchase History License, lalu muat ulang Tab `Subscription`
9. Verifikasi tabel Purchase History License menampilkan "Unable to load this data." dengan tombol `[Try Again]`
10. Lepas intercept, lalu klik `[Try Again]` pada tabel Purchase History License
11. Verifikasi tabel Purchase History License menampilkan data normal
12. Verifikasi state error tabel Purchase History License hilang
13. Aktifkan intercept 5xx pada response data tabel Quota TAG, lalu klik Tab `TAG`
14. Verifikasi tabel Quota TAG menampilkan "Unable to load this data." dengan tombol `[Try Again]`
15. Lepas intercept, lalu klik `[Try Again]` pada tabel Quota TAG
16. Verifikasi tabel Quota TAG menampilkan data normal
17. Verifikasi state error tabel Quota TAG hilang
18. Aktifkan intercept 5xx pada response data tabel Purchase History TAG, lalu muat ulang Tab `TAG`
19. Verifikasi tabel Purchase History TAG menampilkan "Unable to load this data." dengan tombol `[Try Again]`
20. Lepas intercept, lalu klik `[Try Again]` pada tabel Purchase History TAG
21. Verifikasi tabel Purchase History TAG menampilkan data normal
22. Verifikasi state error tabel Purchase History TAG hilang

### TC-AC-ACC-854: Error state gagal memuat tabel Tab Hardware dan pulih dengan Try Again

23. Aktifkan intercept 5xx pada response data tabel Hardware List, lalu klik Tab `Hardware`
24. Verifikasi tabel Hardware List menampilkan "Unable to load this data." dengan tombol `[Try Again]`
25. Lepas intercept, lalu klik `[Try Again]` pada tabel Hardware List
26. Verifikasi tabel Hardware List menampilkan data normal
27. Verifikasi state error tabel Hardware List hilang
28. Aktifkan intercept 5xx pada response data tabel Quota, lalu muat ulang Tab `Hardware`
29. Verifikasi tabel Quota menampilkan "Unable to load this data." dengan tombol `[Try Again]`
30. Lepas intercept, lalu klik `[Try Again]` pada tabel Quota
31. Verifikasi tabel Quota menampilkan data normal
32. Verifikasi state error tabel Quota hilang
33. Aktifkan intercept 5xx pada response data tabel Purchase History Hardware, lalu muat ulang Tab `Hardware`
34. Verifikasi tabel Purchase History Hardware menampilkan "Unable to load this data." dengan tombol `[Try Again]`
35. Lepas intercept, lalu klik `[Try Again]` pada tabel Purchase History Hardware
36. Verifikasi tabel Purchase History Hardware menampilkan data normal
37. Verifikasi state error tabel Purchase History Hardware hilang

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Spec ini memuat dua TC kelas b (fault injection) pada satu Client; satu spec per kelas per modul (bagian 3 prinsip 13). Spec melewati sekitar 35 langkah: seluruh blok satu kelas harness (intercept 5xx lalu pulih), tiap tabel berdiri sendiri, dan kegagalan satu tabel tidak membuat tabel lain kehilangan makna. Langkah "Lepas intercept" adalah langkah penghubung (S-03).
- Temuan untuk QA (S-15): TC-853/854 menyebut "Paksa response ... gagal (5xx)" tanpa endpoint; daftar endpoint tiap tabel disediakan tim FE dan tidak dikarang. Mode FE+BE dengan intercept parsial di atas backend nyata (bagian 6); Post Condition seluruh TC `-` sehingga tidak diasersi.
