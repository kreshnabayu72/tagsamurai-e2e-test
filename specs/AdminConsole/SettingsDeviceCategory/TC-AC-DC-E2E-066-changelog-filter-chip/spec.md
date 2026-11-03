---
id: TC-AC-DC-E2E-066-changelog-filter-chip
title: "Modal Changelog Category: Chip Filter, Sinkron Checkbox, Chip +N more, dan Kombinasi AND"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-175
  - TC-AC-DC-176
  - TC-AC-DC-177
  - TC-AC-DC-178
coverage:
  web: automated
---

# Modal Changelog Category: Chip Filter, Sinkron Checkbox, Chip +N more, dan Kombinasi AND

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Principal `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1, nama tampil `Budi Santoso`, Modified By `Budi S`; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14), Riwayat Changelog Uji (No 17: dua belas entri, Field `Category`, pelaku `Budi S` dan `Maya P`), dan General Settings entitas uji (No 19: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Nilai persis dibaca dari tabel Pre-setup TC dan tidak ditulis ulang di luar langkah.
- Pemulihan Changelog: kemampuan fixture BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan mekanismenya) memulihkan Riwayat Changelog entitas uji ke Pre-setup No 17 di hook `before` dan `after`. Jumlah total entri (12) dan pembagian halaman pada asersi bersumber dari No 17.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-175: Chip terpilih dihapus lewat icon X pada chip menyinkronkan checkbox opsi

1. Klik ikon Changelog pada header Sidebar Category
2. Klik ikon Filter, buka dropdown Action, centang "Create" dan "Edit"
3. Klik icon `(✕)` pada chip "Create" tanpa membuka dropdown
4. Buka dropdown Action
5. Verifikasi chip "Create" hilang dari field Action
6. Verifikasi chip "Edit" tetap ada
7. Verifikasi checkbox "Create" tidak tercentang
8. Verifikasi checkbox "Edit" tetap tercentang
9. Pada dropdown Category centang "Gateway Kit" dan "Wearable", klik icon `(✕)` pada chip "Gateway Kit", lalu buka dropdown Category
10. Verifikasi chip "Gateway Kit" hilang dari field Category
11. Verifikasi chip "Wearable" tetap ada
12. Verifikasi checkbox "Gateway Kit" tidak tercentang
13. Pada dropdown Modified By centang "Budi S" dan "Maya P", klik icon `(✕)` pada chip "Budi S", lalu buka dropdown Modified By
14. Verifikasi chip "Budi S" hilang dari field Modified By
15. Verifikasi chip "Maya P" tetap ada
16. Verifikasi checkbox "Budi S" tidak tercentang

### TC-AC-DC-176: Uncheck opsi di dalam dropdown menghapus chip yang bersangkutan

17. Klik `[Clear Field]` pada Filter Panel
18. Buka dropdown Action, centang "Create" dan "Edit"
19. Dengan dropdown tetap terbuka, uncheck "Create"
20. Verifikasi chip "Create" hilang dari field Action
21. Verifikasi chip "Edit" tetap ada
22. Pada dropdown Category centang "Gateway Kit" dan "Wearable", lalu uncheck "Gateway Kit" dari dalam dropdown
23. Verifikasi chip "Gateway Kit" hilang dari field Category
24. Verifikasi chip "Wearable" tetap ada
25. Pada dropdown Modified By centang "Budi S" dan "Maya P", lalu uncheck "Budi S" dari dalam dropdown
26. Verifikasi chip "Budi S" hilang dari field Modified By
27. Verifikasi chip "Maya P" tetap ada

### TC-AC-DC-177: Banyak chip terpilih diringkas menjadi chip +N more

28. Klik `[Clear Field]` pada Filter Panel
29. Buka dropdown Category, centang seluruh 9 opsi
30. Verifikasi field Category menampilkan chip sebanyak yang muat pada lebar field dan sisanya diringkas dalam satu chip "+N more" (jumlah chip tampil + N = 9)
31. Verifikasi field Category tidak melebar keluar panel
32. Verifikasi field Category tidak digulir horizontal

### TC-AC-DC-178: Kombinasi dua field filter berlogika AND

33. Klik `[Clear Field]` pada Filter Panel, klik `[Apply]`
34. Klik ikon Filter, buka dropdown Action, centang "Delete", buka dropdown Modified By, centang "Budi S", klik `[Apply]`
35. Verifikasi tabel menampilkan 1 baris (Delete `Wearable`)
36. Klik ikon Filter, ganti Action ke "Create" dan Modified By ke "Maya P", klik `[Apply]`
37. Verifikasi tabel menampilkan 3 baris (`Tracker Seven`, `Kit Lama Anak`, `Kit Lama`)

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-175, 176, 177, 178). Tidak ada TC hanya-BE di spec ini.
- Alasan melewati sekitar 35 langkah: seluruh blok satu kelas harness (fungsional, satu permukaan Filter Panel modal Changelog) dan tiap TC dimulai dari Filter Panel yang dikosongkan lebih dulu, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah dari TC): langkah 17, 28, 33.
- Langkah 29 tidak mengklik ikon Filter (TC-AC-DC-177 langkah 3 menyebutnya): ikon Filter berfungsi toggle dan Filter Panel masih terbuka sesudah `[Clear Field]` (langkah 28), sehingga klik ikon akan menutupnya; `[Apply]` menutup panel (langkah 33 lalu 34). Perilaku ini dikonfirmasi pengguna 2026-11-02 dan belum tertulis di TC-AC-DC-166/168 (lihat Temuan untuk QA).
- Temuan untuk QA:
  - Asersi spec ini bergantung pada isi persis Riwayat Changelog Pre-setup #17 (dua belas entri, termasuk angka total 12 dan pembagian halaman), sedangkan S-12 melarang angka total absolut pada audit trail permanen dan Lampiran A belum punya butir untuk modul ini. Spec mengikuti TC dan mengandalkan kemampuan fixture BE yang memulihkan Changelog entitas uji ke #17 sebelum dan sesudah spec. Perlu keputusan pengecualian Lampiran A (setara A-5) atau entitas uji khusus Changelog.
  - TC-AC-DC-177 tidak menyebut lebar field atau jumlah chip yang muat; spec hanya mengasersi jumlah chip tampil + N = 9.
  - TC-AC-DC-178 menyebut opsi Modified By dengan nama pendek "Budi" dan "Maya"; label opsi di UI adalah "Budi S" dan "Maya P" (8b butir 12), dan spec memakai label UI itu.
  - Perilaku Filter Panel belum tertulis di TC-AC-DC-166 dan 168: ikon Filter berfungsi toggle (klik saat panel terbuka menutupnya) dan `[Apply]` menutup panel. Karena itu spec tidak mengklik ikon Filter pada langkah 29 dan membukanya kembali sesudah `[Apply]` (langkah 34 dan 36). Perlu ditambahkan ke TC-AC-DC-166/168.
