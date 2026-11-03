---
id: TC-AC-DC-E2E-081-log-system-log-dan-activity-log
title: "System Log Aktor dan Activity Log Admin Console Mencatat Create, Edit, dan Delete Category"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-224
  - TC-AC-DC-225
coverage:
  web: automated
---

# System Log Aktor dan Activity Log Admin Console Mencatat Create, Edit, dan Delete Category

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control #1 (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Budi Santoso; Modified By tampil `Budi S`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture backend (disediakan tim FE/BE; endpoint tidak dikarang di spec ini). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: pohon Pre-setup #14 (`Hardware` > `Handheld Reader`) hanya dibaca sebagai induk node milik spec dan tidak diubah.
- Data Dinamis (suffix `{runId}-081`): `Induk Uji {runId}-081` (leaf di bawah `Handheld Reader`, induk Add kedua blok), dibuat lewat sesi API aktor di hook `before`. Node yang dibuat spec lewat UI: `Log Sistem {runId}-081` (langkah 3), diubah menjadi `Log Sistem {runId}-081 Baru` (langkah 5), lalu dihapus (langkah 7); `Log Aktivitas {runId}-081` (langkah 21), diubah menjadi `Log Aktivitas {runId}-081 Baru` (langkah 23), lalu dihapus (langkah 25). Nama memuat `Log Sistem {runId}-081` dan `Log Aktivitas {runId}-081` sehingga satu kata kunci mencakup ketiga entri tiap blok; baseline entri nol karena nama unik per run (S-12).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Induk Uji {runId}-081` dan sisa node di atas bila masih ada. Entri log tidak dapat dihapus; nama bersuffix run.
- Kemampuan teknis (disediakan tim FE/BE): membuka Detail User akun aktor tab System Log dan Activity Log Admin Console; kolom yang dicakup Search pada System Log dan Activity Log tidak disebut TC (lihat Temuan untuk QA).
- State global: tidak ada yang diubah.

## Test Steps

### TC-AC-DC-224: System Log aktor mencatat Create, Edit, dan Delete Category dengan snapshot

1. Expand `Hardware`, lalu expand `Handheld Reader`
2. Hover node `Induk Uji {runId}-081`, lalu klik aksi `+ Subcategory`
3. Ketik "Log Sistem {runId}-081", lalu klik `[Submit]`
4. Hover node `Log Sistem {runId}-081`, lalu klik aksi Edit
5. Ubah nama menjadi "Log Sistem {runId}-081 Baru", lalu klik `[Save]`
6. Hover node `Log Sistem {runId}-081 Baru`, lalu klik aksi Delete
7. Klik `[Delete]` pada dialog konfirmasi
8. Tunggu aksi selesai
9. Buka Detail User akun aktor, lalu buka tab System Log
10. Ketik Search `Log Sistem {runId}-081`, tekan Enter
11. Verifikasi hasil Search menampilkan tepat tiga baris
12. Verifikasi entri Create dengan New Value "Log Sistem {runId}-081" tampil
13. Verifikasi entri Edit dengan Old Value "Log Sistem {runId}-081" dan New Value "Log Sistem {runId}-081 Baru" tampil
14. Verifikasi entri Delete dengan Old Value "Log Sistem {runId}-081 Baru" tampil
15. Verifikasi ketiga entri: kolom Object berisi "Category" dan kolom Field berisi "Category"
16. Verifikasi kolom Name pada entri Create berisi "Log Sistem {runId}-081", pada entri Edit berisi "Log Sistem {runId}-081 Baru", dan pada entri Delete berisi "Log Sistem {runId}-081 Baru" (nama Category pada saat aksi)
17. Verifikasi Old Value pada entri Create berisi "—" dan New Value pada entri Delete berisi "—"

### TC-AC-DC-225: Activity Log Admin Console mencatat Create, Edit, dan Delete Category dengan Modified By

18. Buka halaman Settings > Device > Device Name
19. Expand `Hardware`, lalu expand `Handheld Reader`
20. Hover node `Induk Uji {runId}-081`, lalu klik aksi `+ Subcategory`
21. Ketik "Log Aktivitas {runId}-081", lalu klik `[Submit]`
22. Hover node `Log Aktivitas {runId}-081`, lalu klik aksi Edit
23. Ubah nama menjadi "Log Aktivitas {runId}-081 Baru", lalu klik `[Save]`
24. Hover node `Log Aktivitas {runId}-081 Baru`, lalu klik aksi Delete
25. Klik `[Delete]` pada dialog konfirmasi
26. Tunggu aksi selesai
27. Buka Activity Log Admin Console
28. Ketik Search `Log Aktivitas {runId}-081`, tekan Enter
29. Verifikasi hasil Search menampilkan tepat tiga baris dengan Object "Category"
30. Verifikasi ketiga entri: Modified By "Budi S"
31. Verifikasi ketiga entri: kolom Name menampilkan nama Category pada saat aksi (`Log Aktivitas {runId}-081` pada Create, `Log Aktivitas {runId}-081 Baru` pada Edit dan Delete) dan kolom Field berisi "Category"
32. Verifikasi Old Value pada entri Create berisi "—" dan New Value pada entri Delete berisi "—"

## Notes

- Langkah penghubung (S-03): langkah 8 dan 26 (menunggu aksi hapus selesai karena langkah berikutnya berpindah surface, bagian 8b butir 8), langkah 18 (kembali ke halaman Device Name untuk blok kedua), dan Search pada langkah 10 dan 28 untuk menemukan entri target (R-16).
- Pembagian TC lintas spec: Changelog Category untuk aksi yang sama ada di spec 079 dan 080; sinkron tiga surface dan aktor ada di spec 082; absence log ada di spec 083, 084, 097, dan 098 (S-05).
- Temuan untuk QA:
  - TC-AC-DC-224 dan 225 tidak menyebut kolom yang dicakup Search pada System Log dan Activity Log, tidak menyebut tab Activity Log tempat entri Category tampil (Session atau User Action), dan tidak menyebut nama kolom Action pada kedua surface. Spec memakai Search dengan nama bersuffix sebagai langkah penghubung dan menyebut entri berdasarkan jenis aksi; bila Search tidak mencakup Name, Old Value, atau New Value, QA/FE perlu menetapkan cara menemukan entri.
  - TC-AC-DC-224 Expected b ("Name berisi nama Category pada saat aksi") tidak menyatakan nama pada entri Edit: sebelum atau sesudah rename. Spec mengikuti konvensi Changelog TC-AC-DC-217 (Category = nama sesudah perubahan) dan menulis nama sesudah rename pada entri Edit; QA perlu mengonfirmasi.
  - TC memakai node literal Pre-setup #14 (`Rugged Scanner`) sebagai induk dan target; spec memakai node bersuffix milik spec (keputusan data tulis).
