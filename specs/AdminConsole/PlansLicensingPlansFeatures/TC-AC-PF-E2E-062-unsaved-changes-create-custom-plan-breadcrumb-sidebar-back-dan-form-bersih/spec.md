---
id: TC-AC-PF-E2E-062-unsaved-changes-create-custom-plan-breadcrumb-sidebar-back-dan-form-bersih
title: "Unsaved Changes Create Custom Plan: Breadcrumb, Sidebar, Back, dan Form Bersih"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-155
  - TC-AC-PF-156
  - TC-AC-PF-157
  - TC-AC-PF-158
  - TC-AC-PF-159
coverage:
  web: automated
---

# Unsaved Changes Create Custom Plan: Breadcrumb, Sidebar, Back, dan Form Bersih

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal), akun #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.AC_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_ac-plans-features` true dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): sesi API aktor dan fixture backend idempoten untuk memulihkan Dataset Pre-setup dan menghapus plan buatan spec. General Settings (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) disiapkan fixture sebagai precondition TC dan tidak diubah spec.
- Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12): nilai Pre-setup dirujuk lewat kunci fixture yang dibuat tim FE; password dan token tidak ditulis di spec.
- Data Pre-setup: Dataset Plan A dengan default plan `Growth`.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup (`Growth`) dipakai apa adanya, hanya dibaca (Template); pemulihan Dataset dijamin fixture backend idempoten yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini.
- Data Dinamis: Plan Name `Paket Dirty-{runId}-062` (bersuffix `-{runId}-062`); tidak ada plan yang tersimpan.
- Kemampuan teknis tambahan: tombol Back browser dapat diklik oleh spec.
- State global: Dataset Pre-setup bersama; suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Spec berakhir dengan form bersih (TC-AC-PF-159) pada halaman Default > Active; hook `after` memulihkan Dataset.

## Test Steps

### Dirty: Cancel (TC-AC-PF-155)

1. Buka tab `Custom`, sub-tab `Active`
2. Klik `+ Custom Plan` pada toolbar
3. Pilih Product `FAMS` dan Template `Growth`, isi Plan Name `Paket Dirty-{runId}-062`
4. Klik segmen `Plans & Features` pada breadcrumb
5. Verifikasi dialog `Unsaved Changes` tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
6. Klik `[Cancel]` pada dialog
7. Verifikasi dialog tertutup dan user tetap di Plans & Licensing > Plans & Features > New Custom Plan dengan input dipertahankan

### Dirty: menu sidebar (TC-AC-PF-157)

8. Klik menu Plans & Licensing > Plans & Features di sidebar
9. Verifikasi dialog `Unsaved Changes` tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
10. Verifikasi halaman belum berpindah
11. Klik `[Cancel]` pada dialog

### Dirty: tombol Back browser (TC-AC-PF-158)

12. Klik tombol Back browser
13. Verifikasi dialog tampil dengan body "You have unsaved changes. Are you sure you want to leave?"
14. Klik `[Cancel]` pada dialog
15. Verifikasi user tetap di Plans & Licensing > Plans & Features > New Custom Plan

### Dirty: Leave (TC-AC-PF-156)

16. Klik segmen `Plans & Features` pada breadcrumb
17. Verifikasi dialog tampil dengan body "You have unsaved changes. Are you sure you want to leave?"
18. Klik `[Leave]` pada dialog
19. Verifikasi halaman Plans & Licensing > Plans & Features > Default > Active tampil
20. Buka tab `Custom`, sub-tab `Active`, lalu ketik Search `Paket Dirty-{runId}-062`, tekan Enter
21. Verifikasi tidak ada plan `Paket Dirty-{runId}-062` (empty state `No results found`)

### Form bersih (TC-AC-PF-159)

22. Klik `(←)` pada kotak Search, lalu klik `+ Custom Plan` pada toolbar
23. Klik segmen `Plans & Features` pada breadcrumb tanpa mengisi apa pun
24. Verifikasi halaman Plans & Licensing > Plans & Features > Default > Active tampil langsung tanpa dialog Unsaved Changes

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 11, 20, 22.
- Urutan TC di spec: TC-AC-PF-155, TC-AC-PF-157, dan TC-AC-PF-158 memakai form dirty yang sama dan menutup dialog dengan `[Cancel]`; TC-AC-PF-156 meninggalkan form dengan `[Leave]`; TC-AC-PF-159 memakai form bersih yang baru dibuka. Urutan ini mengikuti prinsip form ditutup di akhir (S-10).
- Langkah penghubung: `[Cancel]` pada dialog TC-AC-PF-157 (menutup dialog yang tidak diinstruksikan TC), Search `Paket Dirty` sebagai anchor absence plan (empty state `No results found` adalah anchor positif yang sah untuk absence hasil Search, bagian 8b butir 2), `(←)` pada Search, dan `+ Custom Plan` untuk form bersih.
- Temuan untuk QA: (1) TC-AC-PF-157 menyebut "Klik menu Plans & Licensing > Plans & Features di sidebar" tanpa menyebut path menu secara lengkap; spec memakai teks TC. (2) Expected b TC-AC-PF-156 "tidak ada plan `Paket Dirty`" tidak punya langkah observasi daftar di TC; spec menambahkan pencarian pada Custom > Active sebagai langkah penghubung.
