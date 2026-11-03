---
id: TC-FA-CF-E2E-040-grup-field-terikat-ke-tab-asal
title: "Grup Field Terikat ke Tab Asal pada Create"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-54
  - TC-FA-CF-55
  - TC-FA-CF-56
coverage:
  web: automated
---

# Grup Field Terikat ke Tab Asal pada Create

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password lewat `Spectra.env.FA_TC_PASSWORD`; environment variable: `FA_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook `before` suite untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Baseline Company: Company Alpha (Pre-setup #11 dan #12) dipulihkan oleh hook `before` suite (seed reset Company). Spec tidak mengubah, mengedit, atau menghapus baris Pre-setup (S-06).
- Data Pre-setup (hanya dibaca, dipakai sebagai baris pembanding anchor): `Asset Serial Tag` pada tab General (Pre-setup #12), `Vendor Code` pada tab Purchasing dan `Cost Center` pada tab Accounting (Pre-setup #13). Tab Accounting dapat dibuka karena Company Alpha berlisensi FA-7 aktif (Pre-setup #11).
- Data dinamis (dibuat lewat UI oleh spec ini): D-1 `Group Bound General {runId}-040` (tab General), D-2 `Group Bound Purchasing {runId}-040` (tab Purchasing), D-3 `Group Bound Accounting {runId}-040` (tab Accounting); semuanya Data Type Text.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-040`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

#### TC-FA-CF-54: Create dari tab General mengikat grup field ke tab General tanpa input pemilihan grup

1. Klik `[+ Custom Field]`
2. Verifikasi modal tidak memiliki input pemilihan grup
3. Isi Field Name `Group Bound General {runId}-040` dan Data Type `Text`
4. Klik `[Submit]`
5. Verifikasi baris `Group Bound General {runId}-040` tampil pada tabel tab General
6. Klik tab `Purchasing`
7. Verifikasi baris pembanding `Vendor Code` tampil pada tabel tab Purchasing
8. Verifikasi tidak ada baris `Group Bound General {runId}-040` pada tabel tab Purchasing
9. Klik tab `Accounting`
10. Verifikasi baris pembanding `Cost Center` tampil pada tabel tab Accounting
11. Verifikasi tidak ada baris `Group Bound General {runId}-040` pada tabel tab Accounting

#### TC-FA-CF-55: Create dari tab Purchasing mengikat grup field ke tab Purchasing tanpa input pemilihan grup

12. Klik tab `Purchasing`
13. Klik `[+ Custom Field]`
14. Verifikasi modal tidak memiliki input pemilihan grup
15. Isi Field Name `Group Bound Purchasing {runId}-040` dan Data Type `Text`
16. Klik `[Submit]`
17. Verifikasi baris `Group Bound Purchasing {runId}-040` tampil pada tabel tab Purchasing
18. Klik tab `General`
19. Verifikasi baris pembanding `Asset Serial Tag` tampil pada tabel tab General
20. Verifikasi tidak ada baris `Group Bound Purchasing {runId}-040` pada tabel tab General
21. Klik tab `Accounting`
22. Verifikasi baris pembanding `Cost Center` tampil pada tabel tab Accounting
23. Verifikasi tidak ada baris `Group Bound Purchasing {runId}-040` pada tabel tab Accounting

#### TC-FA-CF-56: Create dari tab Accounting mengikat grup field ke tab Accounting tanpa input pemilihan grup

24. Klik `[+ Custom Field]`
25. Verifikasi modal tidak memiliki input pemilihan grup
26. Isi Field Name `Group Bound Accounting {runId}-040` dan Data Type `Text`
27. Klik `[Submit]`
28. Verifikasi baris `Group Bound Accounting {runId}-040` tampil pada tabel tab Accounting
29. Klik tab `General`
30. Verifikasi baris pembanding `Asset Serial Tag` tampil pada tabel tab General
31. Verifikasi tidak ada baris `Group Bound Accounting {runId}-040` pada tabel tab General
32. Klik tab `Purchasing`
33. Verifikasi baris pembanding `Vendor Code` tampil pada tabel tab Purchasing
34. Verifikasi tidak ada baris `Group Bound Accounting {runId}-040` pada tabel tab Purchasing

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Subjudul `####` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): klik tab; tab asal TC-FA-CF-54 adalah General (dibuka hook `beforeEach`), tab asal TC-FA-CF-55 dibuka pada langkah 12, dan tab asal TC-FA-CF-56 (Accounting) sudah terbuka karena langkah klik tab terakhir TC-FA-CF-55 (S-14).
- Asersi absence baris pada tab lain memakai baris pembanding Pre-setup pada tabel yang sama sebagai anchor positif (8b butir 2); tabel tiap tab kecil sehingga baris diasumsikan tampil dalam satu halaman tanpa Search.
- Field Dinamis bernama bersuffix `{runId}-040` (S-12); `{runId}` hanya terdiri atas digit. Data Pre-setup hanya dibaca.
- Temuan untuk QA:
  - TC-FA-CF-54 sampai 56 langkah 5 'Klik tab lain (`General`, `Purchasing`, `Accounting` selain tab asal)' memuat daftar tab yang termasuk tab asal; spec mengikuti arti 'selain tab asal'.
  - TC tidak menyebut ukuran halaman default tabel; baris `Group Bound ...` dan baris pembanding diasumsikan tampil dalam satu halaman.
