---
id: TC-FA-CAT-E2E-009-kontras-badge-dan-chip-wcag
title: "Kontras Badge dan Chip Memenuhi WCAG 2.1 AA (Manual Only)"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-638
coverage:
  web: automated
---

# Kontras Badge dan Chip Memenuhi WCAG 2.1 AA (Manual Only)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) client CatMain `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; ganti akun ke Total Control client CatPostT0 (Pre-setup #33) dengan password yang sama pada langkah 9. Login akun pertama di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: CatMain (Pre-setup #20, #22, #40): node `Laptop` dengan aset Pre-setup #22 (Status, Brand, Model/Type, Group terisi) dan label Pre-setup #40 (sel `+N more`). CatPostT0 (Pre-setup #33): T-0 sudah lewat, Starter cap 5, 8 kategori usable sehingga Alert Consolidation tampil dan popup Category Consolidation memuat badge Status `Usable` dan `Excess`.
- Kemampuan teknis: pengukuran rasio kontras warna teks terhadap latar (alat ukur disediakan penguji; ambang rasio >= 4.5:1). Pemulihan: preferensi kolom Setup Column yang disimpan langkah 3 dihapus di hook `after` (butir Pemulihan Setup Column di `suite.md`).
- Cakupan: TC berstatus Manual Only (pengukuran visual kontras), tetapi `coverage.web: automated` sampai tim FE menyatakan pengukuran ini tidak dapat diotomasi; spec menuliskan langkah dan kebutuhannya.
- Flag Guided Tooltip halaman Categories: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan client Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-categories.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-638: Kontras badge dan chip memenuhi WCAG 2.1 AA (>= 4.5:1)

1. Klik node `Electronics` di sidebar
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
3. Buka Setup Column pada tabel Assets Popup Detail `Laptop`, tampilkan kolom `Label`, lalu klik `[Save]`
4. Ukur rasio kontras teks terhadap latar badge Status, Brand, Model/Type, Group, dan chip `+N more` Label pada state default
5. Verifikasi seluruh badge dan chip yang diukur memiliki rasio kontras minimal 4.5:1 (WCAG 2.1 AA) pada state default
6. Hover tiap badge dan chip lalu ukur ulang rasio kontras
7. Verifikasi tidak ada badge atau chip dengan rasio di bawah 4.5:1 pada state hover
8. Tutup Popup Detail
9. Logout lalu login sebagai Total Control client CatPostT0 (Pre-setup #33)
10. Buka Fixed Asset > Settings > Categories
11. Klik `[Choose Categories]` pada Alert Category Consolidation untuk membuka popup Category Consolidation
12. Ukur rasio kontras badge Status `Usable` dan `Excess` pada popup Category Consolidation
13. Verifikasi badge Status `Usable` dan `Excess` memiliki rasio kontras minimal 4.5:1 pada state default
14. Hover badge Status `Usable` dan `Excess` lalu ukur ulang rasio kontras
15. Verifikasi tidak ada badge Status dengan rasio di bawah 4.5:1 pada state hover
16. Tutup popup Category Consolidation

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): langkah 8 dan 16 (menutup popup), langkah 9 (ganti akun eksplisit ke client CatPostT0).
- Cakupan: `coverage.web: automated` (keputusan QA) walau TC berstatus Manual Only; diubah ke `unsupported` bila tim FE menyatakan pengukuran kontras visual tidak dapat diotomasi.
- Temuan untuk QA:
  - TC-FA-CAT-638 langkah 3 tidak menyebut cara membuka popup Category Consolidation; spec memakai `[Choose Categories]` pada Alert client CatPostT0 (Pre-setup #33).
  - TC-FA-CAT-638 tidak menyebut alat ukur kontras; ambang 4.5:1 dari Data Uji.
  - Email akun Total Control client CatPostT0 tidak tertulis eksplisit di Pre-setup TC; spec memakai pola Pre-setup #1 dengan `{namaCompany}` CatPostT0.
- Ukuran spec 16 langkah, di bawah ambang sekitar 35.
