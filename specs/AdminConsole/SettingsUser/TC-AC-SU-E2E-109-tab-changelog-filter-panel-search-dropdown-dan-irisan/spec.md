---
id: TC-AC-SU-E2E-109-tab-changelog-filter-panel-search-dropdown-dan-irisan
title: "Tab Changelog: Search dalam Dropdown Filter dan Irisan Search dengan Filter"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-389
  - TC-AC-SU-390
  - TC-AC-SU-391
coverage:
  web: automated
---

# Tab Changelog: Search dalam Dropdown Filter dan Irisan Search dengan Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE): user `Jane Smith {runId}-109` (email `janesmith+{runId}-109@qwertysystem.net`) dengan 5 entri Changelog: (1) Action `Assign`, Field `Manage group`; (2) Action `Edit`, Field `Manage group`; (3) Action `Remove`, Field `Access Level`; (4) Action `Activate`, Field `Status`; (5) Action `Edit`, Field `Activation Email`. Opsi `Action` ada lebih dari 3 nilai dan hanya `Remove` yang memuat `rem`; kata `Manage` memuat entri (1) dan (2), dan hanya entri (2) yang ber-Action `Edit`.
- Kemampuan teknis: kemampuan seed entri Changelog disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-389: Search di dalam dropdown Action

1. Ketik Search `Jane Smith {runId}-109`, tekan Enter
2. Klik Name `Jane Smith {runId}-109`
3. Klik tab `Changelog`
4. Klik icon Filter
5. Buka dropdown `Action`
6. Ketik `rem` di kotak search dropdown
7. Verifikasi opsi `Remove` tampil
8. Verifikasi opsi yang tidak memuat `rem` (`Assign`, `Edit`, `Activate`) tidak tampil
9. Ganti isi kotak search dropdown dengan `zzqx`
10. Verifikasi dropdown menampilkan state tidak ada opsi cocok
11. Kosongkan kotak search dropdown, lalu tutup dropdown
12. Klik icon Filter untuk menutup Filter Panel

### TC-AC-SU-390: Search lalu Filter, hasil irisan

13. Ketik Search `Manage`, tekan Enter
14. Klik icon Filter
15. Pilih `Edit` di field `Action`
16. Klik `[Apply]`
17. Verifikasi sedikitnya satu baris tampil
18. Verifikasi setiap baris yang tampil memuat `Manage` dan memiliki Action `Edit`
19. Verifikasi keyword Search `Manage` tetap terisi
20. Klik icon Filter
21. Klik `[Clear Field]`, lalu klik `[Apply]`
22. Klik icon `(←)` pada kotak Search

### TC-AC-SU-391: Filter lalu Search, hasil irisan

23. Klik icon Filter
24. Pilih `Edit` di field `Action`
25. Klik `[Apply]`
26. Ketik Search `Manage`, tekan Enter
27. Verifikasi sedikitnya satu baris tampil
28. Verifikasi setiap baris yang tampil memiliki Action `Edit` dan memuat `Manage`
29. Klik icon `(←)` pada search bar
30. Verifikasi baris Action `Edit` yang tidak memuat `Manage` tampil kembali
31. Verifikasi setiap baris yang tampil memiliki Action `Edit` (filter Action `Edit` tetap aktif)
32. Klik icon Filter
33. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah 1 dan 2 (Ketik Search nama user target, lalu Klik Name untuk membuka Detail) adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- `[Clear Field]` lalu `[Apply]` pada akhir blok adalah langkah penghubung yang mengosongkan Filter (S-09); klik icon Filter sebelum tiap pengaturan Filter membuka panel.
- Mengosongkan kotak search dropdown, menutup panel, dan klik `(←)` adalah langkah penghubung yang membersihkan state (S-09).
- Verifikasi 'baris Action `Edit` yang tidak memuat `Manage` tampil kembali' pada TC-391 menjadi bukti bahwa filter tetap menyaring setelah search ditutup; ia diturunkan dari Expected b TC-391 dengan entri (5) sebagai pembanding.
- Temuan untuk QA:
  - TC-389 'state tidak ada opsi cocok' tidak menyebut teks; spec tidak menuliskan teks tertentu.
  - Perilaku Filter Panel setelah `[Apply]` (tetap terbuka atau menutup) tidak dinyatakan di TC. Spec mengasumsikan panel menutup setelah Apply dan membukanya lagi dengan klik icon Filter.
  - Cara men-seed entri audit trail (Date, Action, Field, Old Value, New Value, pelaku) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
