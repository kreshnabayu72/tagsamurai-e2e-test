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

1. Ketik Search `Jane Smith {runId}-108`, tekan Enter
2. Klik Name `Jane Smith {runId}-108`
3. Klik tab `Changelog`
4. Klik icon Filter
5. Pilih `Assign` dan `Remove` di field `Action`
6. Klik `[Apply]`
7. Verifikasi sedikitnya satu baris tampil
8. Verifikasi setiap baris yang tampil memiliki Action `Assign` atau `Remove`
9. Klik icon Filter
10. Tambah `Admin U` di field `Modified By`
11. Klik `[Apply]`
12. Verifikasi sedikitnya satu baris tampil
13. Verifikasi setiap baris yang tampil memiliki Action `Assign` atau `Remove` dan Modified By `Admin U`
14. Klik icon Filter
15. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-SU-387: Chip opsi terpilih dan hapus via (X) chip

16. Klik icon Filter
17. Pilih `Assign` lalu `Remove` di field `Action`
18. Verifikasi chip `Assign` lalu chip `Remove` muncul berdampingan di dalam field `Action`
19. Klik `(X)` pada chip `Assign` tanpa membuka dropdown
20. Verifikasi chip `Assign` hilang
21. Verifikasi chip `Remove` tetap tampil
22. Buka dropdown field `Action`
23. Verifikasi checkbox `Assign` ter-uncheck
24. Verifikasi checkbox `Remove` tetap tercentang
25. Klik `[Apply]`
26. Verifikasi sedikitnya satu baris tampil
27. Verifikasi setiap baris yang tampil memiliki Action `Remove`
28. Klik icon Filter
29. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-SU-388: Hapus opsi lewat uncheck di dalam dropdown

30. Klik icon Filter
31. Pilih `Assign` lalu `Remove` di field `Action`
32. Buka dropdown `Action`, uncheck `Remove`
33. Tutup dropdown
34. Verifikasi chip `Remove` hilang dari field
35. Verifikasi chip `Assign` tetap tampil
36. Klik `[Apply]`
37. Verifikasi sedikitnya satu baris tampil
38. Verifikasi setiap baris yang tampil memiliki Action `Assign`
39. Klik icon Filter
40. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah 1 dan 2 (Ketik Search nama user target, lalu Klik Name untuk membuka Detail) adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- `[Clear Field]` lalu `[Apply]` pada akhir blok adalah langkah penghubung yang mengosongkan Filter (S-09); klik icon Filter sebelum tiap pengaturan Filter membuka panel.
- Temuan untuk QA:
  - Perilaku Filter Panel setelah `[Apply]` (tetap terbuka atau menutup) tidak dinyatakan di TC. Spec mengasumsikan panel menutup setelah Apply dan membukanya lagi dengan klik icon Filter.
  - TC-387 langkah 6 meminta 'Buka dropdown field' tanpa menyebut field; spec membuka dropdown `Action`.
  - Pelaku `Admin U` (nama lengkap `Admin Utama`) tidak terpetakan ke akun mana pun di Tabel Data Uji Pre-setup (#1-#7 hanya email aktor, #8 hanya target user). Spec memakai pelaku seeding bernama depan `Admin` dan belakang `Utama`; suffix `{runId}` ditaruh di email pelaku, bukan di nama, karena format Modified By [First Name] [Last Initial] tidak dapat memuat suffix.
  - Cara men-seed entri audit trail (Date, Action, Field, Old Value, New Value, pelaku) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
- Spec ini melewati sekitar 35 langkah (40 langkah nominal, sekitar 40 dengan ekspansi blok berulang). Alasan pertahanan: seluruh blok berada pada satu permukaan, satu kelas harness (fungsional biasa), memakai dataset seeding yang sama, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
