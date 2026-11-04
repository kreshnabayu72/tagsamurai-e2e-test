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
- Data Pre-setup (hanya dibaca, tidak diubah): #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal), dipasang idempoten oleh seeding di hook `before`. Riwayat Changelog Principal (#33): seed 35 entri bertanggal 01/09/26 sampai 03/10/26 (18 entri oleh `Jane S`, 17 oleh `Budi K`); total pada modal dapat lebih besar karena entri yang ditulis spec lain, sehingga TC-AC-DS-399 memakai Filter Date seed `01/09/26` sampai `03/10/26`, dan TC-AC-DS-400 dan TC-AC-DS-599 mengasersi entri seed pada rentang tanggalnya. Entri buatan spec lain dipulihkan baseline data uji yang disediakan tim FE/BE (lihat Temuan untuk QA).
- Konfigurasi General Settings (Pre-setup #35): Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta; hanya dibaca, tidak diubah.
- Tabel "Filter Multi-select Changelog" untuk langkah 4 sampai 7 (tiap iterasi juga memilih field Date rentang `01/09/26` sampai `03/10/26`, sesuai TC-AC-DS-399):

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
4. Pada field {Field} pilih {Opsi yang dipilih} dan pada field Date pilih rentang `01/09/26` sampai `03/10/26`
5. Klik `[Apply]` pada Filter Panel modal
6. Verifikasi tabel menampilkan {Hasil yang tampil}
7. Klik `[Clear Field]`, lalu `[Apply]`

### TC-AC-DS-400: Filter Date range inklusif

8. Klik field Date, lalu pilih rentang `28/09/26` sampai `01/10/26`
9. Klik `[Apply]` pada Filter Panel modal
10. Verifikasi tabel memuat entri seed berikut karena kedua ujung inklusif: Edit `HHR-ARC-100` (01/10/26 09:15), Edit Model/Type `HHR-BIG-01` (30/09/26 18:00), Edit Model/Type `HHR-BIG-01` (29/09/26 08:00), Edit Model/Type `HHR-BIG-01` (28/09/26 08:00), dan Edit `HHR-ARC-200` (28/09/26 14:40)
11. Verifikasi tabel tidak memuat entri bertanggal di luar rentang `28/09/26` sampai `01/10/26`
12. Verifikasi teks tanggal pada input mengikuti Date Format `dd/MM/yy`
13. Klik `[Clear Field]`, lalu `[Apply]`

### TC-AC-DS-599: Filter Date satu hari

14. Klik field Date, lalu pilih tanggal `28/09/26` sebagai awal dan akhir
15. Klik `[Apply]` pada Filter Panel modal
16. Verifikasi tabel memuat entri seed pada 28/09/26 berurutan Newest First: Edit `HHR-ARC-200` (28/09/26 14:40) lalu Edit Model/Type `HHR-BIG-01` (28/09/26 08:00)
17. Verifikasi entri tanggal 27/09/26 dan 29/09/26 tidak tampil
18. Verifikasi teks tanggal pada input mengikuti Date Format `dd/MM/yy`
19. Klik `[Clear Field]`, lalu `[Apply]`
20. Klik ikon close `[✕]` pada modal

## Notes

- Langkah 4 sampai 7 diulang untuk empat baris tabel "Filter Multi-select Changelog" (ekspansi 16 langkah; total spec 32 langkah dengan ekspansi). Parameter tiap iterasi ada di tabel Prerequisites, tanpa langkah bersyarat.
- Langkah penghubung (S-03, S-09): `[Clear Field]` lalu `[Apply]` di langkah 7, 13, dan 19 melepas filter sebelum langkah berikutnya; langkah 20 menutup modal; tanpa asersi tambahan.
- Asersi absence langkah 11 didahului langkah 10, dan asersi absence langkah 17 didahului langkah 16, yang membuktikan entri seed pada rentang tanggalnya tampil pada tabel yang sama.
- Temuan untuk QA:
  - S-12: jumlah entri (1 dan 17) diasersi di bawah Filter Date seed `01/09/26` sampai `03/10/26` sesuai TC-AC-DS-399, dan TC-AC-DS-400 dan TC-AC-DS-599 mengasersi entri seed pada rentangnya, bukan total modal; asersi bergantung pada nama literal Pre-setup #29 dan #33 (pengecualian S-12 A-11, `suite.md`).
  - TC-AC-DS-399 tidak memberi Expected untuk chip yang tampil di dalam field; chip tidak diasersi. TC-AC-DS-399 Expected d menyebut 17 entri tanpa menyebut tampilan jumlahnya; spec mengamatinya lewat jumlah halaman.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
