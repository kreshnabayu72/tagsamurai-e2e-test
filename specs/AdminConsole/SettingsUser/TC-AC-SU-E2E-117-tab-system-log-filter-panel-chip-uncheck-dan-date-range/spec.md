---
id: TC-AC-SU-E2E-117-tab-system-log-filter-panel-chip-uncheck-dan-date-range
title: "Tab System Log: Filter Panel (Chip, Uncheck Opsi, dan Date Range Inklusif)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-418
  - TC-AC-SU-419
  - TC-AC-SU-653
coverage:
  web: automated
---

# Tab System Log: Filter Panel (Chip, Uncheck Opsi, dan Date Range Inklusif)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE): user `Jane Smith {runId}-117` (email `janesmith+{runId}-117@qwertysystem.net`) sebagai aktor dengan 3 entri System Log (Date bulan berjalan): (1) tanggal 02, Object `User`; (2) tanggal 05, Object `Global Role`; (3) tanggal 08, Object `User`. Action, Name, dan Field bebas (tidak diasersi, dipakai sebagai precondition TC).
- Kemampuan teknis: kemampuan seed entri System Log dengan Date tertentu disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-418: Chip opsi terpilih dan hapus via (X) chip

1. Cari `Jane Smith {runId}-117` di Search pada User List, tekan Enter, lalu buka Detail user tersebut
2. Klik tab `System Log`
3. Klik icon Filter
4. Pilih `User` lalu `Global Role` di field `Object`
5. Verifikasi chip `User` lalu chip `Global Role` muncul berdampingan di dalam field `Object`
6. Klik `(X)` pada chip `User` tanpa membuka dropdown
7. Verifikasi chip `User` hilang
8. Verifikasi chip `Global Role` tetap tampil
9. Buka dropdown field `Object`
10. Verifikasi checkbox `User` ter-uncheck
11. Verifikasi checkbox `Global Role` tetap tercentang
12. Klik `[Apply]`
13. Verifikasi sedikitnya satu baris tampil
14. Verifikasi setiap baris yang tampil memiliki Object `Global Role`
15. Klik icon Filter
16. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-SU-419: Hapus opsi lewat uncheck di dalam dropdown

17. Klik icon Filter
18. Pilih `User` lalu `Global Role` di field `Object`
19. Buka dropdown `Object`, uncheck `Global Role`
20. Tutup dropdown
21. Verifikasi chip `Global Role` hilang dari field
22. Verifikasi chip `User` tetap tampil
23. Klik `[Apply]`
24. Verifikasi sedikitnya satu baris tampil
25. Verifikasi setiap baris yang tampil memiliki Object `User`
26. Klik icon Filter
27. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-SU-653: Date range Date inklusif

28. Klik icon Filter
29. Klik field `Date`
30. Pilih tanggal awal 02 dan tanggal akhir 05
31. Verifikasi isi field `Date` tampil sesuai Date Format General Settings
32. Klik `[Apply]`
33. Verifikasi baris Date 02 dan 05 tampil (batas inklusif)
34. Verifikasi baris Date 08 tidak tampil
35. Klik icon Filter
36. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah pembuka yang mencari user target lewat Search pada User List lalu membuka Detail adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- `[Clear Field]` lalu `[Apply]` pada akhir blok adalah langkah penghubung yang mengosongkan Filter (S-09); klik icon Filter sebelum tiap pengaturan Filter membuka panel.
- Temuan untuk QA:
  - Perilaku Filter Panel setelah `[Apply]` (tetap terbuka atau menutup) tidak dinyatakan di TC. Spec mengasumsikan panel menutup setelah Apply dan membukanya lagi dengan klik icon Filter.
  - TC-418 langkah 5 meminta 'Buka dropdown field' tanpa menyebut field; spec membuka dropdown `Object`.
  - TC-653 'baris dengan Date tanggal 02, 05, dan 08 bulan berjalan': bila hari ini sebelum tanggal 08, entri bertanggal 08 berada di masa depan; TC tidak menyatakan penanganannya. Nilai Date Format General Settings tidak tertulis di TC; asersi format tanggal dibaca dari General Settings entitas Principal.
  - Cara men-seed entri System Log (Date, Action, Object, Name, Field, Old Value, New Value, aktor, termasuk snapshot full path untuk Object `Group`) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
- Spec ini melewati sekitar 35 langkah (36 langkah nominal, sekitar 36 dengan ekspansi blok berulang). Alasan pertahanan: seluruh blok berada pada satu permukaan, satu kelas harness (fungsional biasa), memakai dataset seeding yang sama, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
