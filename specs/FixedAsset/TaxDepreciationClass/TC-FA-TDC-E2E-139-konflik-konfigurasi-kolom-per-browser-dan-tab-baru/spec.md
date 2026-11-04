---
id: TC-FA-TDC-E2E-139-konflik-konfigurasi-kolom-per-browser-dan-tab-baru
title: "Multi-Konteks: Konfigurasi Kolom Tersimpan per Browser dan Tab Browser Baru Memulai dari State Default"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-551
  - TC-FA-TDC-563
coverage:
  web: automated
---

# Multi-Konteks: Konfigurasi Kolom Tersimpan per Browser dan Tab Browser Baru Memulai dari State Default

## Prerequisites

- Mode: FE+BE.
- Akun browser A: Total Control A (company uji Fixed Asset). Role diuji dibaca dari Precondition TC-FA-TDC-551 butir a ("browser A dengan user Total Control A"); email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Akun browser B: Total Control B (akun berbeda). Email tidak tertulis di TC dan disediakan tim FE; password lewat `Spectra.env.FA_TC_B_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Browser B adalah konteks browser kedua yang hasilnya diasersi (langkah 7), login di langkah 1.
- Login browser A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk tabel 26 class), pemulihan Setup Column, flag Guided Tooltip disetel true oleh hook suite (untuk kedua akun), hook `beforeEach` mengonfirmasi `beforeunload`.
- State yang diubah: konfigurasi kolom browser A (kolom Used By disembunyikan pada TC-FA-TDC-551); dipulihkan dengan langkah eksplisit (langkah 8 sampai 10; 8b.14, R-24) dan di hook `after` dengan menghapus preferensi kolom di browser sebagai cadangan.
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `exampleData9` | `BLD-NP`, `BLD-P`, `LAND`, `NB-1`, `NB-2`, `NB-4`, `NB-KHS`, `NB-OLD`, `NB-SL` | sembilan class Example Data PRD dengan nilai kolom persis Example Data |
| `tdc17` | `TDC-01` sampai `TDC-17` | 17 class Active tambahan: Asset Type Building, Allowed Methods Straight Line, Class Name `Kelas uji 01` sampai `Kelas uji 17`; tabel berisi 26 class dengan urutan default Class Code A-Z: sembilan class Example Data lalu `TDC-01` sampai `TDC-17` (dipakai oleh TC-FA-TDC-563) |

- Cakupan preferensi kolom lintas akun tidak dijamin; TC-FA-TDC-551 menguji tepat hal itu (konfigurasi kolom per browser/akun).
- Suite berjalan serial (`parallel: false`) karena konfigurasi Setup Column adalah state global.

## Test Steps

### TC-FA-TDC-551: Column Visibility tersimpan per browser dan tidak memengaruhi user lain

1. Buka konteks browser kedua (browser B) dan login sebagai Total Control B dengan `Spectra.env.FA_TC_B_PASSWORD`
2. Browser A: klik header kolom Actions (Column Visibility ⋯) untuk membuka Overlay Column Visibility
3. Browser A: uncheck kolom Used By
4. Browser A: tutup Overlay Column Visibility
5. Verifikasi browser A: kolom Used By tersembunyi
6. Browser B: buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
7. Verifikasi browser B: kolom Used By tetap tampil sesuai default
8. Browser A: klik header kolom Actions (Column Visibility ⋯)
9. Browser A: check kembali kolom Used By
10. Browser A: tutup Overlay Column Visibility
11. Tutup konteks browser B

### TC-FA-TDC-563: Tab browser baru memulai tabel dari state default

12. Ketik Search `TDC`, tekan Enter
13. Terapkan Filter Asset Type `Building`
14. Klik header Class Name dua kali (Descending)
15. Pindah ke halaman 2
16. Buka tab browser baru (Tab 2) lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
17. Verifikasi Tab 2: Search kosong
18. Verifikasi Tab 2: tidak ada filter yang aktif
19. Verifikasi Tab 2: sort Class Code A-Z
20. Verifikasi Tab 2: halaman 1
21. Tutup Tab 2
22. Tab 1: muat ulang halaman (F5) untuk kembali ke state default

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 4, 10 (menutup Overlay Column Visibility; TC tidak menyebut `[Save]` sehingga tidak ditulis), langkah 8 sampai 10 (pemulihan Setup Column, 8b.14, R-24; hook `after` hanya cadangan), langkah 11 dan 21 (menutup konteks atau tab kedua; S-09), langkah 22 (memulihkan state tabel Tab 1: Search, filter, sort, dan halaman; S-09). Langkah 12 adalah Search yang dinyatakan langkah TC (kata kunci `TDC`), bukan Search untuk menemukan baris target.
- Langkah 5 dan 17 sampai 20 (S-14): kolom di-hide sebelum dicek hilang pada langkah 3 sampai 5; Tab 2 dibuka sesudah Search, filter, sort, dan halaman 2 diatur di Tab 1 (langkah 12 sampai 15).
- Langkah 7: browser B membuka halaman sesudah browser A menyembunyikan kolom (langkah 3), sehingga kolom Used By yang tampil membuktikan konfigurasi tidak ikut ke akun lain (8b.14, catatan Cakupan preferensi kolom lintas akun).
- Langkah 17 (Search kosong) dan 18 (tidak ada filter): pembanding generik, tabel Tab 2 memuat sedikitnya satu baris yang diamati bersama langkah 20 (halaman 1) (8b.2).
- Temuan untuk QA:
  - Email akun Total Control A dan Total Control B tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code `TDC-01` sampai `TDC-17` dan seed Example Data ditulis literal tanpa suffix `{runId}-<NNN>` (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - TC-FA-TDC-551 langkah 1 tidak menyebut `[Save]` pada panel Column Visibility; spec mengikuti TC (hanya uncheck lalu tutup overlay). Bila Setup Column memerlukan `[Save]` agar perubahan berlaku, TC perlu diperbarui.
  - TC-FA-TDC-563 langkah 1 menyebut "Ketik `TDC` pada Search lalu Enter" lalu Filter `Building`; tidak ada asersi di Tab 1 setelah langkah 1 sampai 4, sehingga spec tidak mengasersi state Tab 1 sebelum Tab 2 dibuka.
  - TC-FA-TDC-563 Expected "state default: Search kosong, tanpa filter, sort Class Code A-Z, halaman 1" disatukan satu butir; spec memecahnya per klausa (S-01).
  - Kolom Automation TC-FA-TDC-551 dan TC-FA-TDC-563 memuat `Automatable`; TC ini masuk spec kelas c karena memuat dua konteks browser atau tab.
