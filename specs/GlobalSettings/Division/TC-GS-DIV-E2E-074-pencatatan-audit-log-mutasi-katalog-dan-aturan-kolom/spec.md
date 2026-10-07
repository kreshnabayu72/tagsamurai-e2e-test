---
id: TC-GS-DIV-E2E-074-pencatatan-audit-log-mutasi-katalog-dan-aturan-kolom
title: "Pencatatan Mutasi Divisi pada Changelog: Create Hanya Catat Name, Edit Name/Code, Delete, Bulk Delete per Baris, dan Evaluasi No-Op 0 Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-235
  - TC-GS-DIV-236
  - TC-GS-DIV-237
  - TC-GS-DIV-238
  - TC-GS-DIV-239
  - TC-GS-DIV-240
  - TC-GS-DIV-241
coverage:
  web: automated
---

# Pencatatan Mutasi Divisi pada Changelog: Create Hanya Catat Name, Edit Name/Code, Delete, Bulk Delete per Baris, dan Evaluasi No-Op 0 Log

## Prerequisites

- Login sebagai Role: Total Control
- Lakukan mutasi Create, Edit, Delete, Bulk Delete, dan Edit No-Op
- User berada di Global Settings > User > Division
- Division `Log Create` ada (TC-GS-DIV-235)
- Division `Log Create Renamed` (Code `LGC`) ada
- Division `Log Generate` ada
- Division `Log Gen 2` ada
- Division `Log Gen 2` (Code `LG9`) ada dan Code `LG2` belum dipakai

## Test Steps

### Create dengan Code manual mencatat satu entri Division Name saja (TC-GS-DIV-235)

1. Klik `[+ Division]`, isi Name `Log Create` dan Code `LGC`, klik `[Submit]`
2. Buka Modal Changelog dan lihat entri teratas
3. Buka Activity Log Global Settings dan lihat entri teratas
4. Verifikasi Changelog: 1 entri — Action `Create`, Division Name `Log Create`, Field `Division Name`, Old Value `—`, New Value `Log Create`, Modified By aktor
5. Verifikasi Tidak ada entri Field `Code` untuk Create (Code lahir bersama record)
6. Verifikasi Activity Log: 1 entri Action `Create`, Object `Division`, Name `Log Create`, Field `Division Name`, Old Value `—`, New Value `Log Create`

### Create dengan Code di-generate mencatat satu entri Division Name saja (TC-GS-DIV-236)

7. Klik `[+ Division]`, isi Name `Log Generate`, Code kosong, klik `[Submit]`
8. Buka Modal Changelog
9. Verifikasi Hanya 1 entri Create dengan Field `Division Name`; Code hasil auto-generate tidak dicatat sebagai entri terpisah

### Edit hanya Name mencatat satu entri Field Division Name (TC-GS-DIV-237)

10. Edit `Log Create`: ubah Name menjadi `Log Create Renamed`, Save
11. Buka Modal Changelog dan lihat entri teratas
12. Verifikasi 1 entri: Action `Edit`, Division Name `Log Create Renamed` (nama sesudah rename), Field `Division Name`, Old Value `Log Create`, New Value `Log Create Renamed`, Modified By aktor
13. Verifikasi Tidak ada entri Field `Code`

### Edit hanya Code mencatat satu entri Field Code (TC-GS-DIV-238)

14. Edit `Log Create Renamed`: ubah Code `LGC` menjadi `LGC2`, Save
15. Buka Modal Changelog
16. Verifikasi 1 entri: Action `Edit`, Field `Code`, Old Value `LGC`, New Value `LGC2`
17. Verifikasi Tidak ada entri Field `Division Name`

### Edit Name dan Code sekaligus mencatat dua entri terpisah (TC-GS-DIV-239)

18. Edit `Log Generate`: ubah Name menjadi `Log Gen 2` dan Code menjadi `LG9`, Save
19. Buka Modal Changelog
20. Verifikasi Tepat 2 entri Edit: satu Field `Division Name` (`Log Generate` ke `Log Gen 2`) dan satu Field `Code` (kode lama ke `LG9`)
21. Verifikasi Tidak ada entri ganda untuk field yang sama

### Edit tanpa perubahan tidak mencatat entri apa pun (TC-GS-DIV-240)

22. Buka Edit `Log Gen 2`, klik `[Save]` tanpa perubahan
23. Buka Modal Changelog dan Activity Log
24. Verifikasi Toast netral `No changes to save.`
25. Verifikasi Tidak ada entri baru di Changelog maupun Activity Log

### Edit dengan Code dikosongkan mencatat entri Code bila berbeda (TC-GS-DIV-241)

26. Edit `Log Gen 2`: kosongkan Code, Save
27. Buka Modal Changelog
28. Verifikasi 1 entri Edit Field `Code` dengan Old Value `LG9` dan New Value `LG2` (hasil auto-generate dari Name `Log Gen 2`)
29. Verifikasi Tidak ada entri Field `Division Name`

## Notes

- Memvalidasi aturan pencatatan Changelog: Create hanya mencatat Name (Code manual maupun auto-generate tidak dicatat entri terpisah), Edit mencatat per-field, Delete mencatat New Value em-dash (—), Bulk Delete mencatat 1 baris per item, dan No-Op menghasilkan 0 entri (PRD §8.1).
- Sumber pemetaan test case granular: TC-GS-DIV-235, TC-GS-DIV-236, TC-GS-DIV-237, TC-GS-DIV-238, TC-GS-DIV-239, TC-GS-DIV-240, TC-GS-DIV-241.
