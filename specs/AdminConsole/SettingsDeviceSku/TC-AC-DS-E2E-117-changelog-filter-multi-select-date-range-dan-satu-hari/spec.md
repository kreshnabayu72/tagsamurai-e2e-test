---
id: TC-AC-DS-E2E-117-changelog-filter-multi-select-date-range-dan-satu-hari
title: "Filter Changelog: Multi-select Action, SKU, Field, Modified By, Date Range Inklusif, dan Satu Hari"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-399
  - TC-AC-DS-400
  - TC-AC-DS-599
coverage:
  web: automated
---

# Filter Changelog: Multi-select Action, SKU, Field, Modified By, Date Range Inklusif, dan Satu Hari

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal), dipasang idempoten oleh seeding di hook `before`. Riwayat Changelog Principal (#33): 35 entri (4 halaman pada 10 baris per halaman; 18 entri oleh `Jane S`, 17 oleh `Budi K`). Keadaan awal 35 entri dipulihkan baseline data uji yang disediakan tim FE/BE (lihat Temuan untuk QA).
- Konfigurasi General Settings (Pre-setup #35): Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta; hanya dibaca, tidak diubah.
- Tabel "Filter Multi-select Changelog" untuk langkah 4 sampai 7:

| Field | Opsi yang dipilih | Hasil yang tampil |
|---|---|---|
| Action | `Delete` | 1 entri: Delete `HHR-ARC-300` |
| SKU | `4-Port Fixed Reader (SFR-VEL-4P)` | 1 entri (`Photo — Set as default`) |
| Field | `Photo — Set as default` | 1 entri `SFR-VEL-4P` |
| Modified By | `Budi K` | 17 entri (2 halaman pada 10 baris per halaman) |

- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE.
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat; filter dilepas oleh langkah pemulihan setiap bagian.

## Test Steps

### TC-AC-DS-399: Filter multi-select Action, SKU, Field, dan Modified By

1. Klik ikon Changelog
2. Klik ikon Filter pada modal
3. Untuk setiap baris tabel "Filter Multi-select Changelog", lakukan langkah 4 sampai 7
4. Pada field {Field} pilih {Opsi yang dipilih}
5. Klik `[Apply]` pada Filter Panel modal
6. Verifikasi tabel menampilkan {Hasil yang tampil}
7. Klik `[Clear Field]`, lalu `[Apply]`

### TC-AC-DS-400: Filter Date range inklusif

8. Klik field Date, lalu pilih rentang `28/09/26` sampai `01/10/26`
9. Klik `[Apply]` pada Filter Panel modal
10. Verifikasi tabel memuat tepat 5 entri karena kedua ujung inklusif: Edit `HHR-ARC-100` (01/10/26 09:15), Edit Model/Type `HHR-BIG-01` (30/09/26 18:00), Edit Model/Type `HHR-BIG-01` (29/09/26 08:00), Edit Model/Type `HHR-BIG-01` (28/09/26 08:00), dan Edit `HHR-ARC-200` (28/09/26 14:40)
11. Verifikasi teks tanggal pada input mengikuti Date Format `dd/MM/yy`
12. Klik `[Clear Field]`, lalu `[Apply]`

### TC-AC-DS-599: Filter Date satu hari

13. Klik field Date, lalu pilih tanggal `28/09/26` sebagai awal dan akhir
14. Klik `[Apply]` pada Filter Panel modal
15. Verifikasi tabel memuat tepat 2 entri pada 28/09/26 berurutan Newest First: Edit `HHR-ARC-200` (28/09/26 14:40) lalu Edit Model/Type `HHR-BIG-01` (28/09/26 08:00)
16. Verifikasi entri tanggal 27/09/26 dan 29/09/26 tidak tampil
17. Verifikasi teks tanggal pada input mengikuti Date Format `dd/MM/yy`
18. Klik `[Clear Field]`, lalu `[Apply]`
19. Klik ikon close `[✕]` pada modal

## Notes

- Langkah 4 sampai 7 diulang untuk empat baris tabel "Filter Multi-select Changelog" (ekspansi 16 langkah; total spec 30 langkah dengan ekspansi). Parameter tiap iterasi ada di tabel Prerequisites, tanpa langkah bersyarat.
- Langkah penghubung (S-03, S-09): `[Clear Field]` lalu `[Apply]` di langkah 7, 12, dan 18 melepas filter sebelum langkah berikutnya; langkah 19 menutup modal; tanpa asersi tambahan.
- Asersi absence langkah 16 didahului langkah 15 yang membuktikan entri 28/09/26 tampil pada tabel yang sama.
- Temuan untuk QA:
  - S-12: Pre-setup #33 menetapkan jumlah entri absolut (1, 2, 5, 17, dan 35 entri) sebagai keadaan awal; konvensi menyatakan total audit trail tidak boleh absolut karena tiap spec menambah entri. Spec mengikuti TC dan menggantungkan keadaan awal pada baseline data uji; keputusan pengecualian masih terbuka. Asersi juga bergantung pada nama literal Pre-setup #29; Lampiran A tidak memuat butir modul ini.
  - TC-AC-DS-399 tidak memberi Expected untuk chip yang tampil di dalam field; chip tidak diasersi. TC-AC-DS-399 Expected d menyebut 17 entri tanpa menyebut tampilan jumlahnya; spec mengamatinya lewat jumlah halaman.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
