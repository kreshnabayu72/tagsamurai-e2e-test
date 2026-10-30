---
id: TC-GS-ROLE-E2E-044-bulk-action-bar-seleksi-select-all-dan-retensi
title: "Bulk Action Bar Detail: Seleksi, Select All, dan Retensi Seleksi saat Search Dikosongkan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-120
  - TC-GS-ROLE-121
  - TC-GS-ROLE-122
  - TC-GS-ROLE-123
  - TC-GS-ROLE-136
coverage:
  web: automated
---

# Bulk Action Bar Detail: Seleksi, Select All, dan Retensi Seleksi saat Search Dikosongkan

## Prerequisites

- Mode: FE+BE.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti pernyataan hook suite di `suite.md`.
- Akun aktor hook `before`: Ahmad Fauzi (Total Control, Pre-setup #1), email `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan di hook `before`; hook `beforeEach` membuka Global Settings > Role & Permission > Tab System. Spec memakai satu akun; tidak ada ganti akun.
- Data Dinamis (disiapkan di hook `before` lewat seeding API, kemampuan disediakan tim FE/BE): Detail `Manage hardware` berisi tepat 20 baris. Dua di antaranya baris dengan checkbox seleksi disabled (Ahmad Fauzi sebagai Self dan Budi Santoso sebagai Default User, Pre-setup #1 dan #2) dan 18 baris eligible. Jumlah baris eligible N = 18 ditetapkan seeding: hook mencatat jumlah baris eligible yang sudah ada (K, Pre-setup tetap), lalu men-seed 18 - K user Active (Access Global Settings, nama bersuffix `Bulk Hardware {nn}+{runId}-044`) dengan baris `Manage hardware`, dan memastikan Wawan Setiawan (Pre-setup #11) termasuk baris eligible dengan baris `Manage hardware`. N tidak dibaca dari tabel yang hanya menampilkan satu halaman. Dengan Pagination default 10 baris, tabel terdiri atas dua halaman (halaman 1: Ahmad Fauzi, Budi Santoso, dan 8 baris eligible; halaman 2: 10 baris eligible), urutan default Name A-Z, dan Wawan Setiawan berada di halaman 2.
- Data yang diubah spec: baris `Manage hardware` seeding dan Wawan Setiawan. Hook `after` menghapus user seeding bersuffix `+{runId}-044` dan menghapus baris `Manage hardware` Wawan Setiawan sehingga Wawan kembali menjadi kandidat Pre-setup #11. Spec tidak menjalankan aksi Remove; seleksi hanya dibuat lalu dibatalkan.
- Selection Limit memakai nilai default environment (lebih besar dari N); spec tidak mengubahnya.
- Kemampuan teknis: Search dengan Enter; Pagination.
- State global: tidak ada yang diubah (suite berjalan serial, `suite.md`).

## Test Steps

### TC-GS-ROLE-120: Screening Bulk Action Bar Detail

1. Klik Role Name `Manage hardware`
2. Centang satu baris eligible pertama di halaman 1
3. Verifikasi urutan elemen Bulk Action Bar: button Bulk Action, counter, button Select All, icon `(X)`
4. Verifikasi counter "1 User selected"
5. Verifikasi button "Select All (18 records)"
6. Centang baris eligible kedua di halaman 1
7. Verifikasi counter "2 Users selected"
8. Klik `(X)` pada Bulk Action Bar

### TC-GS-ROLE-121: Checkbox header Detail, select page, header tidak checked penuh, deselect

9. Centang checkbox header
10. Verifikasi semua baris eligible di halaman 1 checked
11. Verifikasi baris Ahmad Fauzi dan Budi Santoso (checkbox disabled) tetap unchecked
12. Verifikasi Bulk Action Bar muncul
13. Hapus centang satu baris eligible di halaman 1
14. Verifikasi checkbox header tidak lagi checked penuh
15. Hapus centang checkbox header
16. Verifikasi semua baris di halaman 1 unchecked
17. Verifikasi Bulk Action Bar hilang

### TC-GS-ROLE-122: Clear seleksi lewat (X) di Bulk Action Bar

18. Centang dua baris eligible di halaman 1
19. Klik `(X)` pada Bulk Action Bar
20. Verifikasi seleksi dibatalkan (semua baris di halaman 1 unchecked)
21. Verifikasi Bulk Action Bar tertutup

### TC-GS-ROLE-123: Select All lintas halaman dan Unselect All

22. Centang satu baris eligible di halaman 1
23. Klik button "Select All (18 records)"
24. Verifikasi semua baris eligible di halaman 1 checked
25. Verifikasi counter "18 Users selected"
26. Buka halaman 2
27. Verifikasi semua baris di halaman 2 tetap checked
28. Verifikasi button berubah menjadi "Unselect All"
29. Klik button "Unselect All"
30. Verifikasi seleksi dibatalkan (semua baris di halaman 2 unchecked)
31. Verifikasi Bulk Action Bar tertutup

### TC-GS-ROLE-136: Seleksi tetap bertahan saat Search dikosongkan

32. Ketik Search `Wawan`, tekan Enter
33. Centang Wawan Setiawan
34. Klik `(←)` pada kotak Search
35. Buka halaman 2
36. Verifikasi Wawan Setiawan tetap tercentang
37. Verifikasi counter tetap "1 User selected"
38. Klik `(X)` pada Bulk Action Bar

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC sumber.
- Spec melewati sekitar 35 langkah (38 langkah) karena kelima TC berada di satu kelas harness (fungsional, Bulk Action Bar pada satu dataset: Detail `Manage hardware`) dan berbagi seeding 18 baris eligible; memisahkannya menggandakan seeding. Tiap blok dimulai dari seleksi kosong, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (tanpa awalan `Verifikasi`): membatalkan seleksi dengan `(X)` di akhir blok (langkah 8 dan 38), mencentang satu baris agar Bulk Action Bar muncul sebelum klik "Select All" (langkah 22), dan mengosongkan Search lewat `(←)` (langkah 34, aksi bagian dari TC-GS-ROLE-136).
- Pada TC-GS-ROLE-121, kondisi awal "baris disabled tetap unchecked" diamati pada Ahmad Fauzi dan Budi Santoso di halaman 1 (langkah 11).
- Temuan untuk QA:
  - TC-GS-ROLE-120 sampai TC-GS-ROLE-123 dan TC-GS-ROLE-136 tidak punya Post Condition.
  - TC-GS-ROLE-121 tidak menyebut baris disabled mana yang diamati; spec memakai baris Self (Ahmad Fauzi) dan Default User (Budi Santoso).
  - TC-GS-ROLE-121 langkah 3 ("Uncheck checkbox header") dilakukan saat header berstatus tidak checked penuh; TC tidak menyebut apakah klik pada state itu membatalkan seluruh seleksi halaman atau memilih ulang. Spec mengikuti Expected c (semua unchecked).
  - TC-GS-ROLE-123 langkah 1 tidak menyebut centang satu baris yang memunculkan Bulk Action Bar (button Select All hanya ada di bar); spec menambah langkah 22.
  - TC-GS-ROLE-136 tidak menyebut halaman tempat Wawan Setiawan berada setelah Search dikosongkan; spec membuka halaman 2 (langkah 35) sesuai urutan A-Z dataset.
