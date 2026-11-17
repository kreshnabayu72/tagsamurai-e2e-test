---
id: TC-FA-TDC-E2E-231-state-tenant-suspended-expired-search-changelog-dan-download-csv-tetap-tersedia
title: "State Tenant Suspended dan Expired: Search, Popup Changelog, dan Download CSV Tetap Tersedia"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-101
sourceRules: ["§4.1#r1", "§5#b2", "§4.1#r7", "T-11a", "§5#b7"]
smoke: []
dependsOn: []
trace:
  "§4.1#r1": [1, 15]
  "§5#b2": [4, 18]
  "§4.1#r7": [6, 20]
  "T-11a": [9, 23]
  "§5#b7": [10, 24]
anchor: [2, 16]
coverage:
  web: automated
---

# State Tenant Suspended dan Expired: Search, Popup Changelog, dan Download CSV Tetap Tersedia

## Prerequisites

- Mode: FE+BE.
- Aktor: Total Control pada dua company uji khusus automation: Company Suspended (entitas client berstatus Suspended) dan Company Expired (entitas client berstatus Expired). Akun, email, dan company tidak tertulis di TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan tim FE).
- Login di hook `before` spec ini sebagai Total Control pada Company Suspended; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca, `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada dan disediakan tim FE): pada kedua company tabel berisi 7 class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) yang belum diubah. Kata kunci Search: `NB-1`.
- Status entitas (Suspended dan Expired) dibentuk fixture BE dan tidak diubah spec ini; kemampuan itu disediakan tim FE/BE.
- Kemampuan unduhan: browser menyimpan berkas hasil `Download as CSV` sehingga nama berkas dapat diamati; isi berkas tidak diasersi di spec ini (kelas f).
- State global: tidak ada yang diubah spec ini selain sesi login.
- Rujukan suite: `suite.md` (hook `before`, `beforeEach`, `after`).

## Test Steps

### Company Suspended

1. Verifikasi tab Tax Depreciation Class terbuka
2. Verifikasi tabel memuat sedikitnya satu baris class
3. Ketik Search `NB-1`, tekan Enter
4. Verifikasi Search menyaring tabel ke NB-1
5. Klik icon Changelog di toolbar
6. Verifikasi Popup Changelog terbuka
7. Tutup Popup Changelog
8. Klik `Download as CSV`
9. Verifikasi tidak ada toast tampil
10. Verifikasi berkas CSV terunduh
11. Klik `(←)` pada kotak Search

### Company Expired

12. Logout
13. Login sebagai Total Control pada Company Expired
14. Buka Settings > Accounting > Tax Depreciation Class
15. Verifikasi tab Tax Depreciation Class terbuka
16. Verifikasi tabel memuat sedikitnya satu baris class
17. Ketik Search `NB-1`, tekan Enter
18. Verifikasi Search menyaring tabel ke NB-1
19. Klik icon Changelog di toolbar
20. Verifikasi Popup Changelog terbuka
21. Tutup Popup Changelog
22. Klik `Download as CSV`
23. Verifikasi tidak ada toast tampil
24. Verifikasi berkas CSV terunduh
25. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): langkah 7, 11, 21, dan 25 menutup popup dan mereset Search; langkah 12 sampai 14 adalah ganti akun eksplisit ke Company Expired (S-07). Search NB-1 pada langkah 3 dan 17 adalah Search yang menemukan baris target (R-16). Langkah 2 dan 16 adalah pembanding sebelum asersi universal Search (8b.2).
- Langkah 9 dan 23: asersi absence toast diletakkan segera setelah pemicu `Download as CSV` dan sebelum asersi artefak; pemicunya menjadi anchor positif yang buktinya menyusul pada langkah 10 dan 24 (8b.11).
- Temuan untuk QA:
  - TC tidak menyebut akun, email, dan company Total Control untuk status Suspended dan Expired.
  - TC-FA-TDC-101 menulis "klik Download as CSV" tanpa menyebut menu unduhan; spec menyalin teks TC.
