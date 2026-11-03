---
id: TC-AC-PF-E2E-193-search-dan-filter-modal-changelog-custom-per-anggota
title: Search dan Filter modal Changelog Custom per anggota kolom
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-619
  - TC-AC-PF-620
coverage:
  web: automated
---

# Search dan Filter modal Changelog Custom per anggota kolom

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log C, Changelog Custom Principal enam entri, terbaru dahulu: `29 Jun 26, 10:00` Push Update `Region Jawa Client` (Plan Version, Old `v3`, New `v20`, Sarah T); `28 Jun 26, 16:00` Edit `Growth Tier` (API call quota, Old `100K/month`, New `1M/month`, John D); `28 Jun 26, 09:10` Edit `Growth Tier` (Custom Report Builder, Old `No`, New `Yes`, John D); `17 Jun 26, 14:30` Create `Growth Tier` (Plan Name, Old `—`, New `Growth Tier`, John D); `12 Jun 26, 16:00` Delete `Pilot Reseller` (Plan Name, Old `Pilot Reseller`, New `—`, Jane S); `10 Jun 26, 09:15` Archive `Enterprise Reseller` (Status, Old `Active`, New `Archived`, Jane S). Modified By Jane S = Jane Smith. Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Custom Principal tepat sama dengan Dataset Log C di hook `before` dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### Search per anggota kolom (TC-AC-PF-619)

1. Klik tab Custom
2. Klik ikon Changelog pada toolbar
3. Ketik Search `push`, tekan Enter
4. Verifikasi satu baris `Push Update` (Action)
5. Ganti isi kotak search dengan `reseller`, tekan Enter
6. Verifikasi dua baris `Delete Pilot Reseller` dan `Archive Enterprise Reseller` (Plan Name)
7. Ganti isi kotak search dengan `status`, tekan Enter
8. Verifikasi baris `Archive Enterprise Reseller` (Field)
9. Ganti isi kotak search dengan `active`, tekan Enter
10. Verifikasi baris `Archive Enterprise Reseller` (Old Value)
11. Ganti isi kotak search dengan `1M`, tekan Enter
12. Verifikasi baris `Edit Growth Tier` API call quota (New Value)
13. Ganti isi kotak search dengan `sarah`, tekan Enter
14. Verifikasi baris `Push Update` (Modified By `Sarah T`)

### Filter per anggota kolom (TC-AC-PF-620)

15. Klik `(←)` pada kotak Search
16. Buka Filter Panel, pilih rentang Date `10 Jun 26` sampai `17 Jun 26`, klik `[Apply]`
17. Verifikasi tiga entri (`17 Jun`, `12 Jun`, `10 Jun`) dengan batas inklusif
18. Buka Filter Panel, klik `[Clear Field]`, pilih Action `Edit`, klik `[Apply]`
19. Verifikasi dua entri `Growth Tier`
20. Buka Filter Panel, klik `[Clear Field]`, pilih Plan Name `Growth Tier`, klik `[Apply]`
21. Verifikasi tiga entri (dua `Edit`, satu `Create`)
22. Buka Filter Panel, klik `[Clear Field]`, pilih Field `Status`, klik `[Apply]`
23. Verifikasi entri `Archive Enterprise Reseller`
24. Buka Filter Panel, klik `[Clear Field]`, pilih Modified By `Jane Smith`, klik `[Apply]`
25. Verifikasi dua entri (`Delete` dan `Archive`)

## Notes

- Langkah penghubung (S-03): langkah 15 menutup input Search dan mereset tabel; `[Clear Field]` pada langkah 18, 20, 22, dan 24 mengganti filter sebelumnya ("Hapus filter" pada TC).
- Temuan untuk QA: TC menetapkan enam entri sebagai seluruh isi Changelog Custom. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
