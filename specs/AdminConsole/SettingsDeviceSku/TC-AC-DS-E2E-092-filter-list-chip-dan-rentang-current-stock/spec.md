---
id: TC-AC-DS-E2E-092-filter-list-chip-dan-rentang-current-stock
title: "Filter List: Penghapusan Chip, Overflow +N more, dan Rentang Current Stock Inklusif"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-317
  - TC-AC-DS-318
  - TC-AC-DS-319
  - TC-AC-DS-320
coverage:
  web: automated
---

# Filter List: Penghapusan Chip, Overflow +N more, dan Rentang Current Stock Inklusif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #29 (SKU Principal inti; Current Stock `HHR-ARC-100` 120, `SFR-VEL-4P` 36, `TAG-ARC-USR` 500, `HHR-BIG-01` 12500, sisanya 0 atau 8) dan #30 (`SEED-001` sampai `SEED-119`, stok 0; total 129 SKU Principal): hanya dibaca, tidak diubah. Dipasang idempoten oleh seeding di hook `before`.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE (lihat Temuan untuk QA).
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat; filter dilepas oleh langkah pemulihan setiap bagian.

## Test Steps

### TC-AC-DS-317: Hapus chip lewat ikon silang

1. Klik ikon Filter
2. Pada field Brand pilih `Kinetia` dan `Veltrix`
3. Klik ikon `(✕)` pada chip `Kinetia`
4. Verifikasi chip `Kinetia` hilang
5. Verifikasi chip `Veltrix` tetap ada
6. Buka dropdown Brand
7. Verifikasi checkbox `Kinetia` tidak tercentang di dalam dropdown
8. Verifikasi checkbox `Veltrix` tetap tercentang
9. Tekan Esc, lalu klik `[Apply]`
10. Verifikasi tabel memuat baris Brand `Veltrix`: `SFR-VEL-4P` dan `SFR-ZERO-01`
11. Klik `[Clear Field]`, lalu `[Apply]`

### TC-AC-DS-318: Un-check opsi di dalam dropdown menghapus chip

12. Pada field Brand pilih `Kinetia` dan `Veltrix`
13. Buka dropdown Brand lalu hilangkan centang `Kinetia`
14. Verifikasi chip `Kinetia` hilang dari dalam field
15. Verifikasi chip `Veltrix` tetap ada
16. Tekan Esc, lalu klik `[Apply]`
17. Verifikasi tabel memuat baris Brand `Veltrix`: `SFR-VEL-4P` dan `SFR-ZERO-01`
18. Klik `[Clear Field]`, lalu `[Apply]`

### TC-AC-DS-319: Overflow chip +N more

19. Pada field Device Name pilih `4-Port Fixed Reader`, `anggur sensor`, `Apel sensor`, `Asset TAG`, `BLE Gateway`, dan `Industrial Handheld Reader`
20. Verifikasi chip ditampilkan sebanyak yang muat pada lebar field dan sisanya diringkas dalam satu chip `+N more` (jumlah chip tampil ditambah N sama dengan 6)
21. Verifikasi field tidak melebar keluar panel
22. Verifikasi field tidak digulir horizontal
23. Klik `[Clear Field]`

### TC-AC-DS-320: Rentang Current Stock inklusif

24. Isi Min `36` dan Max `120`, lalu klik `[Apply]`
25. Verifikasi tabel menampilkan baris Current Stock 36 dan 120: `SFR-VEL-4P` dan `HHR-ARC-100`
26. Klik `[Clear Field]`, isi hanya Min `500`, lalu klik `[Apply]`
27. Verifikasi tabel menampilkan `TAG-ARC-USR` (500) dan `HHR-BIG-01` (12500)
28. Klik `[Clear Field]`, isi hanya Max `0`, lalu klik `[Apply]`
29. Verifikasi tabel menampilkan sedikitnya satu baris berstok 0 (mis. `HHR-ARC-200`)
30. Verifikasi seluruh baris yang tampil berstok 0
31. Klik `[Clear Field]`, lalu `[Apply]`

## Notes

- Langkah penghubung (S-03, S-09): Esc di langkah 9 dan 16 menutup dropdown sebelum `[Apply]`; `[Clear Field]` lalu `[Apply]` di langkah 11, 18, 23, 26, 28, dan 31 melepas filter; tanpa asersi tambahan.
- Asersi universal langkah 30 didahului baris pembanding di langkah 29.
- Temuan untuk QA:
  - S-12: asersi bergantung pada nama literal dan stok Pre-setup #29 dan #30 (mis. `SFR-VEL-4P` stok 36). Lampiran A tidak memuat butir modul ini. Spec mengikuti TC dengan seeding idempoten dan suite serial; keputusan pengecualian nama literal masih terbuka.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - TC-AC-DS-320 Expected c ("seluruh baris berstok 0") tidak menyebut jumlah baris; spec hanya mengasersi kuantor universal dengan pembanding.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya bila menutupi layar belum ditetapkan.
