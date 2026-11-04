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
- Data seeding (Fixture BE): user `Jane Smith {runId}-117` (email `janesmith+{runId}-117@qwertysystem.net`) sebagai aktor dengan 3 entri System Log (Date relatif terhadap hari uji; T-N berarti N hari sebelum hari uji): (1) T-10, Object `User`; (2) T-7, Object `Global Role`; (3) T-4, Object `User`. Action, Name, dan Field bebas (tidak diasersi, dipakai sebagai precondition TC).
- Kemampuan teknis: kemampuan seed entri System Log dengan Date tertentu disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-418: Chip opsi terpilih dan hapus via (X) chip

1. Ketik Search `Jane Smith {runId}-117`, tekan Enter
2. Klik Name `Jane Smith {runId}-117`
3. Klik tab `System Log`
4. Klik icon Filter
5. Pilih `User` lalu `Global Role` di field `Object`
6. Verifikasi chip `User` lalu chip `Global Role` muncul berdampingan di dalam field `Object`
7. Klik `(X)` pada chip `User` tanpa membuka dropdown
8. Verifikasi chip `User` hilang
9. Verifikasi chip `Global Role` tetap tampil
10. Buka dropdown field `Object`
11. Verifikasi checkbox `User` ter-uncheck
12. Verifikasi checkbox `Global Role` tetap tercentang
13. Klik `[Apply]`
14. Verifikasi sedikitnya satu baris tampil
15. Verifikasi setiap baris yang tampil memiliki Object `Global Role`
16. Klik icon Filter
17. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-SU-419: Hapus opsi lewat uncheck di dalam dropdown

18. Klik icon Filter
19. Pilih `User` lalu `Global Role` di field `Object`
20. Buka dropdown `Object`, uncheck `Global Role`
21. Tutup dropdown
22. Verifikasi chip `Global Role` hilang dari field
23. Verifikasi chip `User` tetap tampil
24. Klik `[Apply]`
25. Verifikasi sedikitnya satu baris tampil
26. Verifikasi setiap baris yang tampil memiliki Object `User`
27. Klik icon Filter
28. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-SU-653: Date range Date inklusif

29. Klik icon Filter
30. Klik field `Date`
31. Pilih tanggal awal T-10 dan tanggal akhir T-7
32. Verifikasi isi field `Date` tampil sesuai Date Format General Settings
33. Klik `[Apply]`
34. Verifikasi baris Date T-10 dan T-7 tampil (batas inklusif)
35. Verifikasi baris Date T-4 tidak tampil
36. Klik icon Filter
37. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah 1 dan 2 (Ketik Search nama user target, lalu Klik Name untuk membuka Detail) adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- `[Clear Field]` lalu `[Apply]` pada akhir blok adalah langkah penghubung yang mengosongkan Filter (S-09); klik icon Filter sebelum tiap pengaturan Filter membuka panel.
- Temuan untuk QA:
  - TC-418 langkah 6 meminta 'Buka dropdown field' tanpa menyebut field; spec membuka dropdown `Object`.
  - Nilai Date Format General Settings tidak tertulis di TC; asersi format tanggal dibaca dari General Settings entitas Principal.
  - Cara men-seed entri System Log (Date, Action, Object, Name, Field, Old Value, New Value, aktor, termasuk snapshot full path untuk Object `Group`) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
- Spec ini melewati sekitar 35 langkah (37 langkah nominal, sekitar 37 dengan ekspansi blok berulang). Alasan pertahanan: seluruh blok berada pada satu permukaan, satu kelas harness (fungsional biasa), memakai dataset seeding yang sama, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
