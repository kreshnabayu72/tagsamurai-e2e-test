---
id: TC-AC-PF-E2E-184-sort-modal-changelog-default-dan-custom
title: Sort modal Changelog Default dan Custom per kolom, tipe campuran, dan nilai kosong
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-471
  - TC-AC-PF-472
  - TC-AC-PF-473
  - TC-AC-PF-474
  - TC-AC-PF-714
  - TC-AC-PF-810
coverage:
  web: automated
---

# Sort modal Changelog Default dan Custom per kolom, tipe campuran, dan nilai kosong

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log D, Changelog Default Principal lima entri, terbaru dahulu: `12 Aug 26, 09:00` Create `Enterprise` (Plan Name, Old `—`, New `Enterprise`, Jane S); `01 Aug 26, 08:00` Archive `Growth Plus (old)` (Status, Old `Active`, New `Archived`, Jane S); `20 Jul 26, 10:00` Push Update `PT Wahana Nusantara` (Plan Version, Old `v1`, New `v5`, Sarah T); `10 Jul 26, 12:00` Delete `Pilot Default` (Plan Name, Old `Pilot Default`, New `—`, John D); `05 Jun 26, 15:40` Edit `Growth` (Group count, Old `3`, New `5`, Jane S). Dataset Log C, Changelog Custom Principal enam entri: `29 Jun 26, 10:00` Push Update `Region Jawa Client` (Plan Version, Old `v3`, New `v20`, Sarah T); `28 Jun 26, 16:00` Edit `Growth Tier` (API call quota, Old `100K/month`, New `1M/month`, John D); `28 Jun 26, 09:10` Edit `Growth Tier` (Custom Report Builder, Old `No`, New `Yes`, John D); `17 Jun 26, 14:30` Create `Growth Tier` (Plan Name, Old `—`, New `Growth Tier`, John D); `12 Jun 26, 16:00` Delete `Pilot Reseller` (Plan Name, Old `Pilot Reseller`, New `—`, Jane S); `10 Jun 26, 09:15` Archive `Enterprise Reseller` (Status, Old `Active`, New `Archived`, Jane S). Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Default Principal tepat sama dengan Dataset Log D dan Changelog Custom Principal tepat sama dengan Dataset Log C di hook `before`, dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### Sort Date (TC-AC-PF-471)

1. Klik ikon Changelog pada toolbar tab Default
2. Verifikasi urutan default Newest First: entri `12 Aug 26` paling atas
3. Klik header `Date` satu kali
4. Verifikasi entri `05 Jun 26` paling atas
5. Klik header `Date` kedua kali
6. Verifikasi entri `12 Aug 26` paling atas
7. Klik header `Date` ketiga kali
8. Verifikasi urutan kembali ke default (entri `12 Aug 26` paling atas)

### Sort kolom teks Action, Plan Name, Field (TC-AC-PF-472)

9. Klik header `Action` satu kali
10. Verifikasi Action ascending: `Archive`, `Create`, `Delete`, `Edit`, `Push Update`
11. Klik header `Plan Name` satu kali
12. Verifikasi Plan Name ascending: `Enterprise`, `Growth`, `Growth Plus (old)`, `Pilot Default`, `PT Wahana Nusantara`
13. Klik header `Field` satu kali
14. Verifikasi Field ascending: `Group count`, `Plan Name` (dua baris), `Plan Version`, `Status`

### Sort Old Value dan New Value campuran tipe (TC-AC-PF-473)

15. Klik header `Old Value` satu kali
16. Verifikasi Old Value ascending: `3` (numerik), lalu teks `Active`, `Pilot Default`, `v1`, lalu `—` di akhir
17. Klik header `New Value` satu kali
18. Verifikasi New Value ascending: `5` (numerik), lalu teks `Archived`, `Enterprise`, `v5`, lalu `—` di akhir

### Sort Modified By (TC-AC-PF-474)

19. Klik header `Modified By` satu kali
20. Verifikasi Modified By ascending: `Jane S` (tiga baris), `John D`, `Sarah T`
21. Hover `Sarah T`
22. Verifikasi tooltip `Sarah Tan`

### Sort descending Old Value dan New Value (TC-AC-PF-714)

23. Klik header `Old Value` dua kali
24. Verifikasi Old Value descending: `—` di awal, lalu `v1`, `Pilot Default`, `Active`, dan `3` di akhir
25. Klik header `New Value` dua kali
26. Verifikasi New Value descending: `—` di awal, lalu `v5`, `Enterprise`, `Archived`, dan `5` di akhir

### Sort campuran tipe modal Changelog Custom (TC-AC-PF-810)

27. Tutup modal dengan icon (X)
28. Klik tab Custom
29. Klik ikon Changelog pada toolbar
30. Klik header `Old Value` satu kali
31. Verifikasi Old Value ascending: `100K/month`, `Active`, `No`, `Pilot Reseller`, `v3`, lalu `—` di akhir
32. Klik header `New Value` satu kali
33. Verifikasi New Value ascending: `1M/month`, `Archived`, `Growth Tier`, `v20`, `Yes`, lalu `—` di akhir

## Notes

- Langkah penghubung (S-03): langkah 27 sampai 29 berpindah dari modal Default ke modal Custom.
- Urutan sort tiap blok bergantung pada klik header kolom baru yang menggantikan sort kolom sebelumnya (satu sort aktif); TC tidak menyatakan reset sort antar kolom.
- Temuan untuk QA:
  - TC-AC-PF-471 menyatakan "Default dan klik 2: entri `12 Aug 26` paling atas" sehingga default, klik kedua, dan klik ketiga menampilkan entri teratas yang sama; spec mengasersi tiap keadaan sesuai TC.
  - TC menetapkan lima dan enam entri sebagai seluruh isi Changelog. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
