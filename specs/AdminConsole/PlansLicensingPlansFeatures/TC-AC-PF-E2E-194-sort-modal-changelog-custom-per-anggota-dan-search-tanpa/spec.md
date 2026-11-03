---
id: TC-AC-PF-E2E-194-sort-modal-changelog-custom-per-anggota-dan-search-tanpa
title: Sort modal Changelog Custom per anggota kolom dan Search tanpa hasil
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-621
  - TC-AC-PF-680
coverage:
  web: automated
---

# Sort modal Changelog Custom per anggota kolom dan Search tanpa hasil

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log C, Changelog Custom Principal enam entri, terbaru dahulu: `29 Jun 26, 10:00` Push Update `Region Jawa Client` (Plan Version, Old `v3`, New `v20`, Sarah T); `28 Jun 26, 16:00` Edit `Growth Tier` (API call quota, Old `100K/month`, New `1M/month`, John D); `28 Jun 26, 09:10` Edit `Growth Tier` (Custom Report Builder, Old `No`, New `Yes`, John D); `17 Jun 26, 14:30` Create `Growth Tier` (Plan Name, Old `—`, New `Growth Tier`, John D); `12 Jun 26, 16:00` Delete `Pilot Reseller` (Plan Name, Old `Pilot Reseller`, New `—`, Jane S); `10 Jun 26, 09:15` Archive `Enterprise Reseller` (Status, Old `Active`, New `Archived`, Jane S). Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Custom Principal tepat sama dengan Dataset Log C di hook `before` dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### Sort per anggota kolom (TC-AC-PF-621)

1. Klik tab Custom
2. Klik ikon Changelog pada toolbar
3. Klik header `Date` satu kali
4. Verifikasi Date ascending: entri `10 Jun 26` (`Archive`) paling atas
5. Klik header `Action` satu kali
6. Verifikasi Action ascending: `Archive` paling atas
7. Klik header `Plan Name` satu kali
8. Verifikasi Plan Name ascending: `Enterprise Reseller` paling atas
9. Klik header `Field` satu kali
10. Verifikasi Field ascending: `API call quota` paling atas
11. Klik header `Modified By` satu kali
12. Verifikasi Modified By ascending berdasarkan nama lengkap: dua entri `Jane S` paling atas

### Search tanpa hasil (TC-AC-PF-680)

13. Klik ikon Search, ketik `zzzzz`, tekan Enter
14. Verifikasi empty state: Illustration, Title "No results found", dan Description "Try adjusting your search or filter."
15. Kosongkan isi kotak search, tekan Enter
16. Verifikasi seluruh entri tampil kembali (enam entri)

## Notes

- Urutan sort tiap kolom bergantung pada klik header kolom baru yang menggantikan sort kolom sebelumnya (satu sort aktif); TC tidak menyatakan reset sort antar kolom.
- Pembagian TC lintas spec: TC-AC-PF-810 (sort campuran tipe modal Custom) ada di spec 184.
- Temuan untuk QA: TC menetapkan enam entri sebagai seluruh isi Changelog Custom. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
