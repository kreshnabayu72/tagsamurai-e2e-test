---
id: TC-AC-DS-E2E-093-filter-list-last-modified-indikator-dan-clear-field
title: "Filter List: Rentang Last Modified Inklusif, Indikator Titik, dan Clear Field"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-321
  - TC-AC-DS-323
  - TC-AC-DS-324
coverage:
  web: automated
---

# Filter List: Rentang Last Modified Inklusif, Indikator Titik, dan Clear Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #29 (SKU Principal inti; Last Modified `HHR-ARC-100` 01/10/26 09:15, `HHR-BIG-01` 30/09/26 18:00, `HHR-ARC-200` 28/09/26 14:40) dan #30 (`SEED-001` sampai `SEED-119`, Last Modified 01/09/26 06:00; total 129 SKU Principal): hanya dibaca, tidak diubah. Dipasang idempoten oleh seeding di hook `before`.
- Konfigurasi General Settings (Pre-setup #35): Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta; hanya dibaca, tidak diubah.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE (lihat Temuan untuk QA).
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat; Search, Sort, dan Filter dilepas oleh langkah pemulihan di akhir spec.

## Test Steps

### TC-AC-DS-321: Filter Last Modified date range inklusif

1. Klik ikon Filter
2. Klik field Last Modified lalu pilih tanggal `01/10/26` sebagai awal dan akhir
3. Klik `[Apply]`
4. Verifikasi tabel menampilkan baris `HHR-ARC-100` (01/10/26 09:15)
5. Verifikasi teks tanggal pada input mengikuti Date Format `dd/MM/yy`
6. Klik `[Clear Field]`, pilih rentang `28/09/26` sampai `01/10/26`, lalu klik `[Apply]`
7. Verifikasi tabel menampilkan `HHR-ARC-100` (01/10/26 09:15), `HHR-BIG-01` (30/09/26 18:00), dan `HHR-ARC-200` (28/09/26 14:40) karena kedua ujung inklusif

### TC-AC-DS-323: Indikator titik pada ikon Filter

8. Klik `[Clear Field]`, lalu `[Apply]`
9. Pada field Brand pilih `Veltrix`
10. Klik `[Apply]`
11. Verifikasi titik indikator tampil pada ikon Filter saat panel terbuka
12. Klik ikon Filter sehingga panel tertutup
13. Verifikasi titik indikator tampil pada ikon Filter saat panel tertutup
14. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
15. Verifikasi titik indikator pada ikon Filter hilang

### TC-AC-DS-324: Clear Field dan Apply tidak mereset Search dan Sort

16. Ketik Search `Arcturus`, tekan Enter
17. Klik header kolom SKU dua kali sampai arah Descending aktif
18. Pada field Hardware Type pilih `Handheld Reader`
19. Klik `[Apply]`
20. Klik `[Clear Field]`, lalu klik `[Apply]`
21. Verifikasi Search `Arcturus` tetap aktif di kotak pencarian
22. Verifikasi arah Sort SKU Descending tetap aktif
23. Verifikasi tabel memuat baris Brand `Arcturus` terurut SKU Descending
24. Klik header kolom SKU sekali sampai netral, lalu klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03, S-09): langkah 8 melepas filter Last Modified sebelum bagian berikutnya; langkah 24 memulihkan Sort dan Search tanpa asersi.
- Panel Filter tetap terbuka dari langkah 14 sampai langkah 20 sehingga langkah 18 sampai 20 langsung memakai panel yang sama.
- Temuan untuk QA:
  - S-12: asersi bergantung pada nama literal dan Last Modified Pre-setup #29 dan #30 (mis. `HHR-ARC-100` 01/10/26 09:15). Lampiran A tidak memuat butir modul ini. Spec mengikuti TC dengan seeding idempoten dan suite serial; keputusan pengecualian nama literal masih terbuka.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - TC-AC-DS-321 tidak menyebut jam server atau waktu aksi; nilai Last Modified diasumsikan tetap seperti di Pre-setup #29.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya bila menutupi layar belum ditetapkan.
