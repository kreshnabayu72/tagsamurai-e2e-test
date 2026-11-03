---
id: TC-AC-SU-E2E-108-tab-changelog-filter-panel-kombinasi-chip-dan-uncheck
title: "Tab Changelog: Filter Panel (Kombinasi OR/AND, Chip, dan Uncheck Opsi)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-386
  - TC-AC-SU-387
  - TC-AC-SU-388
coverage:
  web: automated
---

# Tab Changelog: Filter Panel (Kombinasi OR/AND, Chip, dan Uncheck Opsi)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE): user `Jane Smith {runId}-108` (email `janesmith+{runId}-108@qwertysystem.net`) dengan 5 entri Changelog:

| Entri | Action | Field | Modified By |
|---|---|---|---|
| R1 | Assign | Manage group | Admin U |
| R2 | Edit | Manage group | Budi S |
| R3 | Remove | Access Level | Admin U |
| R4 | Activate | Status | Cici A |
| R5 | Remove | Manage group | Budi S |

- Kemampuan teknis: kemampuan seed entri Changelog disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-386: OR di dalam satu field, AND antar field

1. Cari `Jane Smith {runId}-108` di Search pada User List, tekan Enter, lalu buka Detail user tersebut
2. Klik tab `Changelog`
3. Klik icon Filter
4. Pilih `Assign` dan `Remove` di field `Action`
5. Klik `[Apply]`
6. Verifikasi sedikitnya satu baris tampil
7. Verifikasi setiap baris yang tampil memiliki Action `Assign` atau `Remove`
8. Klik icon Filter
9. Tambah `Admin U` di field `Modified By`
10. Klik `[Apply]`
11. Verifikasi sedikitnya satu baris tampil
12. Verifikasi setiap baris yang tampil memiliki Action `Assign` atau `Remove` dan Modified By `Admin U`
13. Klik icon Filter
14. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-SU-387: Chip opsi terpilih dan hapus via (X) chip

15. Klik icon Filter
16. Pilih `Assign` lalu `Remove` di field `Action`
17. Verifikasi chip `Assign` lalu chip `Remove` muncul berdampingan di dalam field `Action`
18. Klik `(X)` pada chip `Assign` tanpa membuka dropdown
19. Verifikasi chip `Assign` hilang
20. Verifikasi chip `Remove` tetap tampil
21. Buka dropdown field `Action`
22. Verifikasi checkbox `Assign` ter-uncheck
23. Verifikasi checkbox `Remove` tetap tercentang
24. Klik `[Apply]`
25. Verifikasi sedikitnya satu baris tampil
26. Verifikasi setiap baris yang tampil memiliki Action `Remove`
27. Klik icon Filter
28. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-SU-388: Hapus opsi lewat uncheck di dalam dropdown

29. Klik icon Filter
30. Pilih `Assign` lalu `Remove` di field `Action`
31. Buka dropdown `Action`, uncheck `Remove`
32. Tutup dropdown
33. Verifikasi chip `Remove` hilang dari field
34. Verifikasi chip `Assign` tetap tampil
35. Klik `[Apply]`
36. Verifikasi sedikitnya satu baris tampil
37. Verifikasi setiap baris yang tampil memiliki Action `Assign`
38. Klik icon Filter
39. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah pembuka yang mencari user target lewat Search pada User List lalu membuka Detail adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- `[Clear Field]` lalu `[Apply]` pada akhir blok adalah langkah penghubung yang mengosongkan Filter (S-09); klik icon Filter sebelum tiap pengaturan Filter membuka panel.
- Temuan untuk QA:
  - Perilaku Filter Panel setelah `[Apply]` (tetap terbuka atau menutup) tidak dinyatakan di TC. Spec mengasumsikan panel menutup setelah Apply dan membukanya lagi dengan klik icon Filter.
  - TC-387 langkah 5 meminta 'Buka dropdown field' tanpa menyebut field; spec membuka dropdown `Action`.
  - Pelaku `Admin U` (nama lengkap `Admin Utama`) tidak terpetakan ke akun mana pun di Tabel Data Uji Pre-setup (#1-#7 hanya email aktor, #8 hanya target user). Spec memakai pelaku seeding bernama depan `Admin` dan belakang `Utama`; suffix `{runId}` ditaruh di email pelaku, bukan di nama, karena format Modified By [First Name] [Last Initial] tidak dapat memuat suffix.
  - Cara men-seed entri audit trail (Date, Action, Field, Old Value, New Value, pelaku) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
- Spec ini melewati sekitar 35 langkah (39 langkah nominal, sekitar 39 dengan ekspansi blok berulang). Alasan pertahanan: seluruh blok berada pada satu permukaan, satu kelas harness (fungsional biasa), memakai dataset seeding yang sama, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
