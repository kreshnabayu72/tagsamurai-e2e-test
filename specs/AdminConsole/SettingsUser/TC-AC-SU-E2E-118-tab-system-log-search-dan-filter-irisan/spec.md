---
id: TC-AC-SU-E2E-118-tab-system-log-search-dan-filter-irisan
title: "Tab System Log: Irisan Search dengan Filter"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-420
  - TC-AC-SU-421
coverage:
  web: automated
---

# Tab System Log: Irisan Search dengan Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE): user `Jane Smith {runId}-118` (email `janesmith+{runId}-118@qwertysystem.net`) sebagai aktor dengan 4 entri System Log: (1) Object `User`, Name `John Doe {runId}-118`; (2) Object `Global Role`, Name `John Doe {runId}-118`; (3) Object `User`, Name `Sarah Lee {runId}-118`; (4) Object `Total Control`, Name `Rina Putri {runId}-118`. Action, Field, Old Value, dan New Value bebas (tidak diasersi). Kata `John` memuat entri (1) dan (2); hanya entri (1) yang ber-Object `User`.
- Kemampuan teknis: kemampuan seed entri System Log disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-420: Search lalu Filter, hasil irisan

1. Ketik Search `Jane Smith {runId}-118`, tekan Enter
2. Klik Name `Jane Smith {runId}-118`
3. Klik tab `System Log`
4. Ketik Search `John`, tekan Enter
5. Klik icon Filter
6. Pilih `User` di field `Object`
7. Klik `[Apply]`
8. Verifikasi sedikitnya satu baris tampil
9. Verifikasi setiap baris yang tampil memuat `John` dan memiliki Object `User`
10. Verifikasi keyword Search `John` tetap terisi
11. Klik icon Filter
12. Klik `[Clear Field]`, lalu klik `[Apply]`
13. Klik icon `(←)` pada kotak Search

### TC-AC-SU-421: Filter lalu Search, hasil irisan

14. Klik icon Filter
15. Pilih `User` di field `Object`
16. Klik `[Apply]`
17. Ketik Search `John`, tekan Enter
18. Verifikasi sedikitnya satu baris tampil
19. Verifikasi setiap baris yang tampil memiliki Object `User` dan memuat `John`
20. Klik icon `(←)` pada search bar
21. Verifikasi baris Object `User` yang tidak memuat `John` tampil kembali
22. Verifikasi setiap baris yang tampil memiliki Object `User` (filter Object `User` tetap aktif)
23. Klik icon Filter
24. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah 1 dan 2 (Ketik Search nama user target, lalu Klik Name untuk membuka Detail) adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- `[Clear Field]` lalu `[Apply]` pada akhir blok adalah langkah penghubung yang mengosongkan Filter (S-09); klik icon Filter sebelum tiap pengaturan Filter membuka panel. Klik `(←)` adalah langkah penghubung yang mengosongkan Search.
- Verifikasi 'baris Object `User` yang tidak memuat `John` tampil kembali' pada TC-421 menjadi bukti bahwa filter tetap menyaring setelah search ditutup; ia diturunkan dari Expected b TC-421 dengan entri (3) sebagai pembanding.
- Temuan untuk QA:
  - Perilaku Filter Panel setelah `[Apply]` (tetap terbuka atau menutup) tidak dinyatakan di TC. Spec mengasumsikan panel menutup setelah Apply dan membukanya lagi dengan klik icon Filter.
  - Cara men-seed entri System Log (Date, Action, Object, Name, Field, Old Value, New Value, aktor, termasuk snapshot full path untuk Object `Group`) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
