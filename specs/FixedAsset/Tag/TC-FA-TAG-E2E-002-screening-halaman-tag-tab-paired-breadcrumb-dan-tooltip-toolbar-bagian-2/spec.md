---
id: TC-FA-TAG-E2E-002-screening-halaman-tag-tab-paired-breadcrumb-dan-tooltip-toolbar-bagian-2
title: "Tooltip Toolbar dan Header Kolom Actions Tab Paired"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-8
  - TC-FA-TAG-9
  - TC-FA-TAG-10
  - TC-FA-TAG-11
  - TC-FA-TAG-12
coverage:
  web: automated
---

# Tooltip Toolbar dan Header Kolom Actions Tab Paired

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat suite.md); spec ini tidak mengubahnya.
- Data: tabel grup tab Paired memuat sedikitnya satu baris (Pre-setup tab Paired dari seeding backend; hanya dibaca, tidak diubah).
- Tidak ada state global yang diubah; cleanup tidak diperlukan karena spec hanya membaca.

## Test Steps

### TC-FA-TAG-8: Tooltip ikon Search pada Table Tools tab Paired

1. Arahkan pointer ke ikon Search pada Table Tools
2. Verifikasi tooltip `Search` tampil saat hover
3. Pindahkan fokus keyboard ke ikon Search dengan Tab
4. Verifikasi tooltip `Search` tampil saat fokus keyboard

### TC-FA-TAG-9: Tooltip ikon Filter pada Table Tools tab Paired

5. Arahkan pointer ke ikon Filter pada Table Tools
6. Verifikasi tooltip `Filter` tampil saat hover
7. Pindahkan fokus keyboard ke ikon Filter dengan Tab
8. Verifikasi tooltip `Filter` tampil saat fokus keyboard

### TC-FA-TAG-10: Tooltip ikon Download pada Table Tools tab Paired

9. Arahkan pointer ke ikon Download pada Table Tools
10. Verifikasi tooltip `Download` tampil saat hover
11. Pindahkan fokus keyboard ke ikon Download dengan Tab
12. Verifikasi tooltip `Download` tampil saat fokus keyboard

### TC-FA-TAG-11: Tooltip tombol Changelog pada Table Tools tab Paired

13. Arahkan pointer ke tombol `Changelog`
14. Verifikasi tooltip `Changelog` tampil

### TC-FA-TAG-12: Tooltip header kolom Actions sebagai trigger Column Visibility

15. Arahkan pointer ke header kolom terakhir `⋯` pada tabel grup
16. Verifikasi tooltip `Column Visibility` tampil

## Notes

- TC-FA-TAG-1 sampai 3 ada di spec 001, TC-FA-TAG-4 sampai 7 ada di spec 018, dan TC-FA-TAG-13 ada di spec 379.
- Temuan untuk QA:
  - TC-FA-TAG-12 Post Condition menyebut konfigurasi kolom tersimpan di cache browser "sesuai langkah yang dilakukan", tetapi langkah TC hanya hover; spec tidak mengubah konfigurasi kolom dan tidak mengasersi Post Condition itu (S-01).
