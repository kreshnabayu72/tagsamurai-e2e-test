---
id: TC-AC-PF-E2E-042-tooltip-ikon-toolbar-plans-list-per-tab-dan-sub-tab
title: Tooltip Ikon Toolbar Plans List per Tab dan Sub-tab
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-692
  - TC-AC-PF-693
  - TC-AC-PF-694
  - TC-AC-PF-695
coverage:
  web: automated
---

# Tooltip Ikon Toolbar Plans List per Tab dan Sub-tab

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal; password dari env `AC_TC_PASSWORD`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip mengikuti pernyataan di `suite.md` (hook suite menyetel flag true untuk akun aktor pre-setup).
- Data Pre-setup: Dataset Plan A (default aktif Starter, Growth, Professional, Enterprise, SIEM; default archived `Growth Plus (old)`; custom Principal aktif `Growth Tier`; custom Principal archived `Enterprise Reseller`). Spec hanya membaca data ini; nama literal tanpa suffix memakai pengecualian S-06/S-12 butir A-14 (nilai dirujuk lewat fixture data `fixtures/plans-licensing-plans-features.json` yang belum ada, ditandai di sini sesuai S-12).
- Kemampuan teknis: fixture backend (pemulihan Dataset Pre-setup) disediakan tim FE/BE dan dinyatakan di `suite.md`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-PF-692: tab Default sub-tab Active

1. Hover ikon Changelog pada toolbar.
2. Verifikasi tooltip `Changelog` tampil.

### TC-AC-PF-694: tab Default sub-tab Archive

3. Klik sub-tab Archive.
4. Hover ikon Search.
5. Verifikasi tooltip `Search` tampil.
6. Hover ikon Filter.
7. Verifikasi tooltip `Filter` tampil.
8. Hover ikon Download.
9. Verifikasi tooltip `Download` tampil.
10. Hover ikon Changelog.
11. Verifikasi tooltip `Changelog` tampil.

### TC-AC-PF-693: tab Custom sub-tab Active

12. Klik tab Custom.
13. Klik sub-tab Active.
14. Hover ikon Filter pada toolbar.
15. Verifikasi tooltip `Filter` tampil.
16. Hover ikon Changelog pada toolbar.
17. Verifikasi tooltip `Changelog` tampil.

### TC-AC-PF-695: tab Custom sub-tab Archive

18. Klik sub-tab Archive.
19. Hover ikon Search.
20. Verifikasi tooltip `Search` tampil.
21. Hover ikon Filter.
22. Verifikasi tooltip `Filter` tampil.
23. Hover ikon Download.
24. Verifikasi tooltip `Download` tampil.
25. Hover ikon Changelog.
26. Verifikasi tooltip `Changelog` tampil.

## Notes

- Langkah penghubung (S-03): langkah 3, 12, 13, dan 18 (pindah tab dan sub-tab).
- Urutan TC: TC-AC-PF-694 dijalankan sebelum TC-AC-PF-693 agar sub-tab Archive tab Default dan sub-tab Active tab Custom dibuka berurutan tanpa kembali ke tab Default.
- Tooltip diasersi tepat sesudah hover masing-masing (bagian 8b butir 5).
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tanpa langkah observasi tidak diasersi (S-01).
