---
id: TC-AC-DS-E2E-119-changelog-filter-kombinasi-search-clear-dan-tanpa-hasil
title: "Filter Changelog: Kombinasi Search dan Filter Dua Arah, Clear Field, dan Tanpa Hasil Lalu Pulih"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-404
  - TC-AC-DS-405
  - TC-AC-DS-406
  - TC-AC-DS-407
coverage:
  web: automated
---

# Filter Changelog: Kombinasi Search dan Filter Dua Arah, Clear Field, dan Tanpa Hasil Lalu Pulih

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal), dipasang idempoten oleh seeding di hook `before`. Riwayat Changelog Principal (#33): 35 entri, termasuk Edit `HHR-ARC-100` dan `HHR-ARC-200`, Create `BLE-KIN-GW1`, dan entri oleh `Budi K` (17 entri). Keadaan awal 35 entri dipulihkan baseline data uji yang disediakan tim FE/BE (lihat Temuan untuk QA).
- Konfigurasi General Settings (Pre-setup #35): Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta; hanya dibaca, tidak diubah.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE.
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat; Search, Filter, dan Sort dilepas oleh langkah pemulihan setiap bagian.

## Test Steps

### TC-AC-DS-404: Search lalu Filter

1. Klik ikon Changelog
2. Ketik Search pada modal `HHR-ARC`, tekan Enter
3. Klik ikon Filter pada modal
4. Pada field Action pilih `Edit`
5. Klik `[Apply]` pada Filter Panel modal
6. Verifikasi tabel memuat entri Action `Edit` yang cocok kata kunci `HHR-ARC`: Edit `HHR-ARC-100` dan Edit `HHR-ARC-200`
7. Verifikasi penerapan Filter tidak mereset kata kunci Search: kotak pencarian masih berisi `HHR-ARC`
8. Klik `[Clear Field]`, lalu `[Apply]`, lalu klik `(←)` pada kotak Search modal

### TC-AC-DS-405: Filter lalu Search

9. Pada field Action pilih `Edit`
10. Klik `[Apply]` pada Filter Panel modal
11. Ketik Search pada modal `HHR-ARC`, tekan Enter
12. Verifikasi hasil sama dengan urutan Search lalu Filter: Edit `HHR-ARC-100` dan Edit `HHR-ARC-200`
13. Klik `[Clear Field]`, lalu `[Apply]`, lalu klik `(←)` pada kotak Search modal

### TC-AC-DS-406: Clear Field tidak mereset Search dan Sort

14. Ketik Search pada modal `Edit`, tekan Enter
15. Klik header kolom Action dua kali sampai Descending aktif
16. Klik ikon Filter pada modal
17. Pada field Modified By pilih `Budi K`
18. Klik `[Apply]` pada Filter Panel modal
19. Klik `[Clear Field]`, lalu `[Apply]` sehingga filter dilepas
20. Verifikasi Search `Edit` tetap aktif di kotak pencarian
21. Verifikasi Sort Action Descending tetap aktif
22. Klik header kolom Action sekali sampai netral, lalu klik `(←)` pada kotak Search modal

### TC-AC-DS-407: Search dan Filter tanpa hasil lalu pulih

23. Ketik Search pada modal `Photo`, tekan Enter
24. Pada field Action pilih `Create`
25. Klik `[Apply]` pada Filter Panel modal
26. Verifikasi kombinasi `Photo` dan Action `Create` menampilkan "No results found"
27. Klik `✕` pada Search modal, tekan Enter pada input kosong
28. Verifikasi tabel pulih menampilkan entri Create `BLE-KIN-GW1`
29. Klik `[Clear Field]`, lalu `[Apply]`
30. Klik ikon close `[✕]` pada modal

## Notes

- Langkah penghubung (S-03, S-09): `[Clear Field]` lalu `[Apply]` dan `(←)` di langkah 8, 13, dan 22 melepas Filter, Search, dan Sort; langkah 29 melepas Filter; langkah 30 menutup modal; tanpa asersi tambahan.
- Asersi tabel "hanya" pada langkah 6 dan 12 memakai entri Edit `HHR-ARC-100` dan `HHR-ARC-200` yang dijamin tampil oleh Search dan Filter sebagai pembanding.
- Temuan untuk QA:
  - S-12: Pre-setup #33 menetapkan keadaan awal entri; konvensi menyatakan audit trail tumbuh sehingga asersi bergantung pada baseline data uji. Spec mengikuti TC; keputusan pengecualian masih terbuka. Asersi juga bergantung pada nama literal Pre-setup #29 dan #30; Lampiran A tidak memuat butir modul ini.
  - TC-AC-DS-406 tidak menyebut hasil Filter Modified By `Budi K` sebelum dilepas; hanya Search dan Sort setelah filter dilepas yang diasersi.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
