---
id: TC-AC-CS-E2E-002-list-toolbar-dan-label-aksesibel-ikon
title: "List: Toolbar dan Label Aksesibel Ikon"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-583
  - TC-AC-CS-586
  - TC-AC-CS-35
  - TC-AC-CS-569
coverage:
  web: automated
---

# List: Toolbar dan Label Aksesibel Ikon

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Total Control, Principal PT ABC; Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Data seed Pre-setup #82 (120 baris term di tab Current dan 60 baris di tab History untuk Client campuran, Plan Owner PT Maju Bersama dan CV Karya Mandiri) bersifat baca-saja; spec tidak menulis data.
- Kemampuan teknis: pembacaan nama aksesibel (accessibility label) elemen, disediakan tim FE.

## Test Steps

### TC-AC-CS-569: Ikon toolbar dan trigger Column Visibility memiliki label aksesibel

1. Periksa nama aksesibel ikon Search, Filter, Download, dan Changelog di toolbar
2. Verifikasi ikon Search memiliki label "Search"
3. Verifikasi ikon Filter memiliki label "Filter"
4. Verifikasi ikon Download memiliki label "Download"
5. Verifikasi ikon Changelog memiliki label "Changelog"
6. Periksa nama aksesibel header kolom Actions `⋯`
7. Verifikasi header kolom Actions `⋯` memiliki label "Column Visibility"

### TC-AC-CS-35: Tooltip ikon toolbar dan trigger Column Visibility

8. Arahkan kursor ke ikon Search
9. Verifikasi tooltip Search "Search"
10. Arahkan kursor ke ikon Filter
11. Verifikasi tooltip Filter "Filter"
12. Arahkan kursor ke ikon Download
13. Verifikasi tooltip Download "Download"
14. Arahkan kursor ke ikon Changelog
15. Verifikasi tooltip Changelog "Changelog"
16. Arahkan kursor ke header kolom `⋯`
17. Verifikasi tooltip header kolom Actions `⋯` "Column Visibility"

### TC-AC-CS-583: Toolbar tetap tampil saat hasil pencarian kosong (empty filtered)

18. Ketik Search `zzzzqqq`, tekan Enter
19. Verifikasi EmptyState "No results found" dengan Description "Try adjusting your search or filter." tampil
20. Verifikasi EmptyState hanya menggantikan area tabel
21. Verifikasi Toolbar tetap tampil rata kanan di atas area tabel dengan isi `Search | Filter | Download | Changelog | [+ Subscription] | [+ Activate Trial]`
22. Verifikasi kolom pencarian tetap berisi `zzzzqqq`
23. Klik `(←)` pada kotak Search

### TC-AC-CS-586: Toolbar tab History hanya Search, Filter, dan Download

24. Verifikasi pada tab `Current` Toolbar rata kanan berisi `Search | Filter | Download | Changelog | [+ Subscription] | [+ Activate Trial]` sesuai capability aktor
25. Klik tab `History`
26. Verifikasi pada tab `History` Toolbar berisi `Search | Filter | Download`
27. Verifikasi ikon Changelog, `[+ Subscription]`, dan `[+ Activate Trial]` tidak dirender (bukan disabled)
28. Ketik Search `PT Maju Bersama`, tekan Enter
29. Verifikasi sedikitnya satu baris hasil Search tampil di tab `History`
30. Verifikasi Search pada tab `History` hanya memengaruhi baris tab `History`
31. Klik tab `Current`
32. Verifikasi keenam elemen Toolbar tampil lagi: `Search | Filter | Download | Changelog | [+ Subscription] | [+ Activate Trial]`
33. Verifikasi state pencarian tab `History` tidak dibawa ke tab `Current` (ACCS-LOGIC-09d)

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): `Klik (←)` pada kotak Search sesudah TC-AC-CS-583 mengosongkan Search sebelum TC-AC-CS-586.
- Urutan TC dalam spec: TC-AC-CS-569, 35, 583, 586 (aksi diam dan hover lebih dulu, lalu Search, lalu pindah tab; S-10).
- Temuan untuk QA:
  - TC-AC-CS-569 tidak menyebut alat untuk memeriksa nama aksesibel; kemampuan pembacaan nama aksesibel ditulis sebagai disediakan tim FE (S-11).
  - TC-AC-CS-586 Expected c ("Search pada tab History hanya memengaruhi baris tab History") tidak menyatakan cara mengamati; spec memakai Verifikasi bahwa hasil Search berada di tab History dengan pembanding sedikitnya satu baris tampil (S-15).
