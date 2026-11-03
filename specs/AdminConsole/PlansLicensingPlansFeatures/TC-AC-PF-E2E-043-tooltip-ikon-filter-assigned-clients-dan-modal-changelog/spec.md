---
id: TC-AC-PF-E2E-043-tooltip-ikon-filter-assigned-clients-dan-modal-changelog
title: Tooltip Ikon Filter Tab Assigned Clients dan Ikon Toolbar Tiga Modal Changelog
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-696
  - TC-AC-PF-697
  - TC-AC-PF-698
  - TC-AC-PF-699
coverage:
  web: automated
---

# Tooltip Ikon Filter Tab Assigned Clients dan Ikon Toolbar Tiga Modal Changelog

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal; password dari env `AC_TC_PASSWORD`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip mengikuti pernyataan di `suite.md` (hook suite menyetel flag true untuk akun aktor pre-setup).
- Data Pre-setup: Dataset Plan D (`Growth` v5 dengan 9 client), Dataset Log D (Changelog Default 5 entri), Dataset Log C (Changelog Custom Principal 6 entri), Dataset Log G (Changelog Global Settings 5 entri). Spec hanya membaca data ini; nama literal tanpa suffix memakai pengecualian S-06/S-12 butir A-14 (nilai dirujuk lewat fixture data `fixtures/plans-licensing-plans-features.json` yang belum ada, ditandai di sini sesuai S-12).
- Kemampuan teknis: fixture backend (pemulihan Dataset Pre-setup dan Changelog) disediakan tim FE/BE dan dinyatakan di `suite.md`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-PF-696: ikon Filter Tab Assigned Clients

1. Buka Plan Detail `Growth` (klik Plan Name).
2. Klik Tab Assigned Clients.
3. Hover ikon Filter pada toolbar.
4. Verifikasi tooltip `Filter` tampil.

### TC-AC-PF-697: ikon Filter modal Changelog Default

5. Kembali ke list lewat Breadcrumb.
6. Klik ikon Changelog pada toolbar tab Default.
7. Hover ikon Filter pada toolbar modal.
8. Verifikasi tooltip `Filter` tampil.
9. Tutup modal Changelog.

### TC-AC-PF-698: ikon toolbar modal Changelog Custom

10. Klik tab Custom.
11. Klik ikon Changelog pada toolbar tab Custom.
12. Hover ikon Search pada toolbar modal.
13. Verifikasi tooltip `Search` tampil.
14. Hover ikon Filter.
15. Verifikasi tooltip `Filter` tampil.
16. Hover ikon Download.
17. Verifikasi tooltip `Download` tampil.
18. Tutup modal Changelog.

### TC-AC-PF-699: ikon toolbar modal Changelog Global Settings

19. Klik tab Global Settings.
20. Klik ikon Changelog di pojok kanan atas Card.
21. Hover ikon Search pada toolbar modal.
22. Verifikasi tooltip `Search` tampil.
23. Hover ikon Filter.
24. Verifikasi tooltip `Filter` tampil.
25. Hover ikon Download.
26. Verifikasi tooltip `Download` tampil.
27. Tutup modal Changelog.

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 (membuka Plan Detail dan Tab Assigned Clients), langkah 5 (kembali ke list), langkah 9, 18, dan 27 (menutup modal Changelog), langkah 10 dan 19 (pindah tab).
- Tooltip diasersi tepat sesudah hover masing-masing (bagian 8b butir 5).
- Pembagian TC lintas spec: TC-AC-PF-644 ada di spec 046.
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tanpa langkah observasi tidak diasersi (S-01).
