---
id: TC-AC-PF-E2E-129-global-settings-unsaved-changes-klik-menu-sidebar-dan-buka-changelog-saat-dirty
title: "Global Settings: Unsaved Changes Saat Klik Menu Sidebar dan Buka Modal Changelog Saat Form Dirty"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-297
  - TC-AC-PF-298
coverage:
  web: automated
---

# Global Settings: Unsaved Changes Saat Klik Menu Sidebar dan Buka Modal Changelog Saat Form Dirty

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active).
- Data: Global FAMS Settings tersimpan `Max custom fields per asset name` = `5` dan `Max depreciation methods (Multi Depreciation tier)` = `2` (precondition TC; Tabel Pre-setup tidak memuat baris bernomor untuk data ini, lihat Temuan untuk QA).
- State global: suite serial (`parallel: false`). Global FAMS Settings adalah singleton (S-06, pengecualian 2026-10-30): nilai `5` dan `2` dipulihkan lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after`. Spec ini tidak menyimpan perubahan apa pun; form yang dirty dibuang lewat `[Leave]` atau dikembalikan ke nilai tersimpan pada langkah 20 (S-09).
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca nilai tersimpan Global FAMS Settings untuk asersi "nilai tersimpan".
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.

## Test Steps

### TC-AC-PF-297: Unsaved Changes saat klik menu sidebar

1. Klik tab `Global Settings`
2. Ubah `Max custom fields per asset name` menjadi `9`
3. Klik menu Plans & Licensing > Plans & Features di sidebar
4. Verifikasi Dialog dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
5. Klik `[Cancel]`
6. Verifikasi Dialog tertutup
7. Verifikasi Pengguna tetap berada di tab Global Settings
8. Verifikasi `Max custom fields per asset name` bernilai `9`
9. Klik menu Plans & Licensing > Plans & Features di sidebar
10. Klik `[Leave]`
11. Verifikasi Navigasi dilanjutkan: halaman Plans & Licensing > Plans & Features tampil
12. Verifikasi Perubahan dibuang: nilai tersimpan `Max custom fields per asset name` tetap `5`

### TC-AC-PF-298: Buka modal Changelog saat perubahan belum disimpan

13. Klik tab `Global Settings`
14. Ubah `Max custom fields per asset name` menjadi `9`
15. Klik ikon Changelog di Card
16. Verifikasi Modal Changelog Global Settings terbuka
17. Verifikasi Tidak ada dialog `Unsaved Changes`
18. Verifikasi Input `Max custom fields per asset name` tetap `9` di belakang modal
19. Tutup modal Changelog
20. Kembalikan `Max custom fields per asset name` ke nilai tersimpan `5`

## Notes

- Langkah penghubung (S-03): klik tab `Global Settings` sebagai precondition tiap TC (langkah 1 dan 13), tutup modal Changelog (langkah 19), dan pengembalian field ke nilai tersimpan (langkah 20). Langkah "Ulangi aksi pemicu lalu klik `[Leave]`" pada TC ditulis sebagai dua langkah (langkah 9 dan 10).
- Pembagian TC lintas spec: TC-AC-PF-294 sampai TC-AC-PF-296 ada di spec 116.
- Temuan untuk QA:
  - Tabel Pre-setup TC tidak memuat baris bernomor untuk nilai awal Global FAMS Settings (`5` dan `2`); nilai itu hanya tertulis di precondition tiap TC. Spec memakai S-06 pengecualian 2026-10-30 (singleton, pemulihan lewat Fixture BE).
  - TC-AC-PF-297 Expected butir c ("nilai tersimpan tetap `5`") tidak menyatakan cara membaca nilai tersimpan; spec memakai kemampuan baca nilai tersimpan yang disediakan tim FE/BE tanpa endpoint karangan (langkah 12).
