---
id: TC-FA-TDC-E2E-031-state-tenant-suspended-expired-aksi-baca-tetap-tersedia
title: "State Tenant Suspended dan Expired: Aksi Baca Tabel, Search, Used By, Changelog, dan Drawer Edit Tetap Tersedia"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-889
  - TC-FA-TDC-890
sourceRules: ["E-FATDC-62", "§4.1.1#r2", "§4.1.1#b2", "§4.1.6#p1", "§4.1.1#p8", "§3.9#r2"]
smoke: []
dependsOn: []
trace:
  "E-FATDC-62": [1, 3, 5, 8, 11, 18, 20, 22, 25, 28]
  "§4.1.1#r2": [1, 18]
  "§4.1.1#b2": [3, 20]
  "§4.1.6#p1": [5, 22]
  "§4.1.1#p8": [8, 25]
  "§3.9#r2": [11, 28]
anchor: [12, 29]
coverage:
  web: automated
---

# State Tenant Suspended dan Expired: Aksi Baca Tabel, Search, Used By, Changelog, dan Drawer Edit Tetap Tersedia

## Prerequisites

- Mode: FE+BE.
- Aktor: Total Control pada dua company uji khusus automation: Company Suspended (entitas client berstatus Suspended) dan Company Expired (entitas client berstatus Expired). Akun, email, dan company tidak tertulis di TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan tim FE).
- Login di hook `before` spec ini sebagai Total Control pada Company Suspended; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data uji (kunci di `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada dan disediakan tim FE): pada kedua company, class NB-2 dengan Used By 3 (tiga Asset Class pemakai di-seed fixture BE). Spec hanya membaca data ini dan tidak mengubahnya; tabel memuat baris pada satu halaman.
- Status entitas (Suspended dan Expired) dibentuk fixture BE dan tidak diubah spec ini; kemampuan itu disediakan tim FE/BE.
- State global: tidak ada yang diubah spec ini selain sesi login.
- Rujukan suite: `suite.md` (hook `before`, `beforeEach`, `after`; seed dan pemulihan lewat API).

## Test Steps

### Company Suspended (TC-FA-TDC-889)

1. Verifikasi tabel Tax Depreciation Class memuat class
2. Ketik Search `NB-2`, tekan Enter
3. Verifikasi Search menampilkan baris NB-2
4. Klik angka Used By baris NB-2
5. Verifikasi modal Used By terbuka
6. Tutup modal Used By
7. Klik ikon Changelog di toolbar
8. Verifikasi modal Changelog terbuka
9. Tutup modal Changelog
10. Klik link Class Code NB-2
11. Verifikasi Drawer mode Edit NB-2 terbuka dengan field terisi
12. Verifikasi Drawer tidak menampilkan pesan error
13. Tutup Drawer dengan `[×]`
14. Klik `(←)` pada kotak Search

### Company Expired (TC-FA-TDC-890)

15. Logout
16. Login sebagai Total Control pada Company Expired
17. Buka Settings > Accounting > Tax Depreciation Class
18. Verifikasi tabel Tax Depreciation Class memuat class
19. Ketik Search `NB-2`, tekan Enter
20. Verifikasi Search menampilkan baris NB-2
21. Klik angka Used By baris NB-2
22. Verifikasi modal Used By terbuka
23. Tutup modal Used By
24. Klik ikon Changelog di toolbar
25. Verifikasi modal Changelog terbuka
26. Tutup modal Changelog
27. Klik link Class Code NB-2
28. Verifikasi Drawer mode Edit NB-2 terbuka dengan field terisi
29. Verifikasi Drawer tidak menampilkan pesan error
30. Tutup Drawer dengan `[×]`
31. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): langkah 6, 9, 13, 14, 23, 26, 30, dan 31 menutup modal, Drawer, dan Search; langkah 15 sampai 17 adalah ganti akun eksplisit ke Company Expired (S-07). Pencarian NB-2 pada langkah 2 dan 19 adalah Search yang menemukan baris target (R-16).
- Langkah 12 dan 29: absence pesan error didahului langkah 11 dan 28 yang membuktikan Drawer terbuka dengan field terisi (anchor positif, 8b.2). Pada Drawer yang tidak diedit, `[×]` menutup tanpa dialog `Unsaved Changes`.
- TC-FA-TDC-101 (Search, Changelog, dan Download pada company Suspended dan Expired) ada di spec 231.
- Temuan untuk QA:
  - TC tidak menyebut akun, email, dan company Total Control untuk status Suspended dan Expired.
  - TC-FA-TDC-889 dan TC-FA-TDC-890 tidak menyebut sumber tiga Asset Class pemakai NB-2; spec menyebut seeding oleh fixture BE.
