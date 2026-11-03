---
id: TC-AC-DS-E2E-091-filter-list-multi-select-searchable-dan-logika-or-and
title: "Filter List: Kelas Multi-select Searchable, Logika OR antar Opsi, dan AND antar Field"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-314
  - TC-AC-DS-315
  - TC-AC-DS-316
coverage:
  web: automated
---

# Filter List: Kelas Multi-select Searchable, Logika OR antar Opsi, dan AND antar Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal): hanya dibaca, tidak diubah. Dipasang idempoten oleh seeding di hook `before`.
- Tabel "Field Filter" untuk langkah 3 sampai 6 (tiap field memakai sedikitnya dua nilai distinct pada kolomnya di data Pre-setup #29):

| Field | Opsi yang dipilih | Baris yang tampil |
|---|---|---|
| Device Name | `BLE Gateway` | `BLE-KIN-GW1` |
| Brand | `Kinetia` | `BLE-KIN-GW1` |
| Hardware Type | `BLE Gateway` | `BLE-KIN-GW1` |
| Range Type | `Long Range` | `HHR-ARC-100` |
| TAG Type | `User` | `TAG-ARC-USR` |

- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE (lihat Temuan untuk QA).
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat; filter dilepas oleh langkah pemulihan di akhir spec.

## Test Steps

### TC-AC-DS-314: Filter kelas multi-select searchable

1. Klik ikon Filter
2. Untuk setiap baris tabel "Field Filter", lakukan langkah 3 sampai 6
3. Pada field {Field} pilih {Opsi yang dipilih}
4. Klik `[Apply]`
5. Verifikasi tabel menampilkan baris {Baris yang tampil}
6. Klik `[Clear Field]`, lalu `[Apply]`

### TC-AC-DS-315: Beberapa opsi dalam satu field (OR)

7. Pada field Brand pilih `Kinetia` dan `Veltrix`
8. Klik `[Apply]`
9. Verifikasi tabel memuat baris Brand `Kinetia` atau `Veltrix`: `BLE-KIN-GW1`, `SFR-VEL-4P`, dan `SFR-ZERO-01`
10. Verifikasi baris Brand `Arcturus` tidak tampil
11. Klik `[Clear Field]`, lalu `[Apply]`

### TC-AC-DS-316: Beberapa field (AND)

12. Pada field Brand pilih `Arcturus`
13. Pada field Hardware Type pilih `Handheld Reader`
14. Klik `[Apply]`
15. Verifikasi tabel hanya memuat baris Brand `Arcturus` dan Hardware Type `Handheld Reader`: `HHR-ARC-100` dan `HHR-ARC-200`
16. Verifikasi `HHR-BIG-01` (Brand lain) dan baris TAG tidak tampil
17. Klik `[Clear Field]`, lalu `[Apply]`

## Notes

- Langkah 3 sampai 6 diulang untuk lima baris tabel "Field Filter" (ekspansi 20 langkah; total spec 32 langkah dengan ekspansi). Parameter tiap iterasi ada di tabel Prerequisites, tanpa langkah bersyarat.
- Langkah penghubung (S-03, S-09): `[Clear Field]` lalu `[Apply]` di langkah 6, 11, dan 17 melepas filter sebelum bagian berikutnya; tanpa asersi tambahan.
- Asersi absence langkah 10 dan 16 didahului Verifikasi baris pembanding pada tabel yang sama (langkah 9 dan 15).
- Temuan untuk QA:
  - S-12: asersi bergantung pada nama literal Pre-setup #29 (mis. `BLE-KIN-GW1`, `HHR-ARC-100`). Lampiran A tidak memuat butir modul ini. Spec mengikuti TC dengan seeding idempoten dan suite serial; keputusan pengecualian nama literal masih terbuka.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - TC-AC-DS-314 tidak memberi Expected untuk chip yang tampil di dalam field; chip tidak diasersi.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya bila menutupi layar belum ditetapkan.
