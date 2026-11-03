---
id: TC-AC-DS-E2E-116-changelog-filter-screening-opsi-dan-pencarian-dropdown
title: "Filter Changelog: Screening Panel, Isi Opsi dari Data Tabel, dan Pencarian di Dalam Dropdown"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-397
  - TC-AC-DS-398
  - TC-AC-DS-565
coverage:
  web: automated
---

# Filter Changelog: Screening Panel, Isi Opsi dari Data Tabel, dan Pencarian di Dalam Dropdown

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal), dipasang idempoten oleh seeding di hook `before`. Riwayat Changelog Principal (#33): 35 entri; opsi Filter modal diturunkan dari entri itu (Action `Create`, `Delete`, `Edit`; SKU `4-Port Fixed Reader (SFR-VEL-4P)`, `BLE Gateway (BLE-KIN-GW1)`, `Industrial Handheld Reader (HHR-BIG-01)`, `UHF Handheld Reader (HHR-ARC-100)`, `UHF Handheld Reader (HHR-ARC-200)`, `UHF Handheld Reader (HHR-ARC-300)`; Field `Model/Type`, `Photo — Set as default`, `SKU`; Modified By `Jane S`, `Budi K`). Keadaan awal 35 entri dipulihkan baseline data uji yang disediakan tim FE/BE (lihat Temuan untuk QA).
- Konfigurasi General Settings (Pre-setup #35): Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta; hanya dibaca, tidak diubah.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE.
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat.

## Test Steps

### TC-AC-DS-397: Screening Filter Panel modal

1. Klik ikon Changelog
2. Klik ikon Filter pada modal
3. Verifikasi field berurutan: Date "Select date", Action "All actions", SKU "All SKUs", Field "All fields", dan Modified By "All users"
4. Verifikasi tombol `[Clear Field]` di kiri dan `[Apply]` di kanan

### TC-AC-DS-398: Isi opsi Filter berasal dari data tabel Changelog

5. Klik field Action
6. Verifikasi Action memuat `Create`, `Delete`, dan `Edit`
7. Tekan Esc, lalu klik field SKU
8. Verifikasi SKU memuat `4-Port Fixed Reader (SFR-VEL-4P)`, `BLE Gateway (BLE-KIN-GW1)`, `Industrial Handheld Reader (HHR-BIG-01)`, `UHF Handheld Reader (HHR-ARC-100)`, `UHF Handheld Reader (HHR-ARC-200)`, dan `UHF Handheld Reader (HHR-ARC-300)` (SKU yang sudah dihapus tetap terdaftar)
9. Tekan Esc, lalu klik field Field
10. Verifikasi Field memuat `Model/Type`, `Photo — Set as default`, dan `SKU`
11. Tekan Esc, lalu klik field Modified By
12. Verifikasi Modified By memuat `Jane S` dan `Budi K`
13. Tekan Esc

### TC-AC-DS-565: Pencarian di dalam dropdown Filter

14. Klik field SKU
15. Ketik `sfr` pada kotak pencarian di dalam dropdown
16. Verifikasi hanya opsi `4-Port Fixed Reader (SFR-VEL-4P)` tampil (substring, tidak membedakan huruf besar-kecil)
17. Ganti isi kotak pencarian di dalam dropdown dengan `zzz`
18. Verifikasi dropdown menampilkan teks "No results found" (teks saja, tanpa ilustrasi) dan tidak ada opsi yang cocok
19. Tekan Esc, lalu klik ikon close `[✕]` pada modal

## Notes

- Langkah penghubung (S-03, S-09): Esc di langkah 7, 9, 11, 13, dan 19 menutup dropdown sebelum langkah berikutnya; klik ikon close di langkah 19 menutup modal; tanpa asersi tambahan.
- Temuan untuk QA:
  - S-12: opsi Filter diturunkan dari riwayat Changelog Pre-setup #33 yang berisi nama literal SKU dan pelaku; konvensi menyatakan audit trail tumbuh sehingga opsi bergantung pada baseline data uji. Spec mengikuti TC; keputusan pengecualian masih terbuka. Asersi juga bergantung pada nama literal Pre-setup #29 dan #30; Lampiran A tidak memuat butir modul ini.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
