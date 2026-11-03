---
id: TC-AC-DN-E2E-091-usage-sort
title: "Usage by Company: Sort Company, Entity Type, Total SKU, dan Total Stock"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-258
  - TC-AC-DN-259
  - TC-AC-DN-260
  - TC-AC-DN-261
coverage:
  web: automated
---

# Usage by Company: Sort Company, Entity Type, Total SKU, dan Total Stock

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip dinyatakan di `suite.md`. Spec ini tidak mengulangnya.
- Data Pre-setup (dibaca saja, tidak diubah; nilai dirujuk lewat `Fixture.settings-device-name`): #16 Device Name inti `Gate Antenna` (Category `Antenna`, Measurement `Unit`); #18 Usage by Company untuk Device Name `Gate Antenna`: `Company A` (Principal, Total SKU 3, Total Stock 40), `Company B` (Distributor dan Client, 2, 2), `Company C` (Client, 0, 6), `Company D` (Distributor, 4, 0), `Company E` (Client, 0, 12). Daftar List default tanpa Search, Filter, atau Sidebar aktif saat spec dimulai.
- Data Dinamis: tidak ada record yang dibuat atau diubah; tabel Usage hanya dibaca.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: klik, ketik, hover, dan membaca urutan baris serta isi sel tabel Usage by Company.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Klik teks nama `Gate Antenna` pada kolom Device Name

### TC-AC-DN-258: Sort kolom Company pada Usage by Company dengan siklus tiga tahap

2. Klik ikon sort pada header `Company` sekali
3. Verifikasi urutan ascending: `Company A`, `Company B`, `Company C`, `Company D`, `Company E`
4. Klik ikon sort pada header `Company` sekali lagi
5. Verifikasi urutan descending: `Company E`, `Company D`, `Company C`, `Company B`, `Company A`
6. Klik ikon sort pada header `Company` sekali lagi
7. Verifikasi indikator sort hilang dan urutan kembali default `Company A` sampai `Company E`

### TC-AC-DN-259: Sort kolom Entity Type pada Usage by Company

8. Klik ikon sort pada header `Entity Type` sekali
9. Verifikasi urutan ascending: `Company C` dan `Company E` (`Client`, sesuai urutan Company A-Z), `Company D` (`Distributor`), `Company B` (`Distributor` dan `Client`), `Company A` (`Principal`)
10. Verifikasi `Company B` yang memuat dua badge dibandingkan memakai label gabungan sesuai urutan tampil badge (`Distributor`, lalu `Client`), sehingga berada setelah `Company D`
11. Klik ikon sort pada header `Entity Type` sekali lagi
12. Verifikasi urutan descending: `Company A`, `Company B`, `Company D`, lalu `Company C` dan `Company E` sesuai urutan Company A-Z
13. Klik ikon sort pada header `Entity Type` sekali lagi hingga indikator sort hilang

### TC-AC-DN-260: Sort kolom Total SKU pada Usage by Company secara numerik

14. Klik ikon sort pada header `Total SKU` sekali
15. Verifikasi urutan ascending: `Company C`, `Company E` (masing-masing 0), `Company B` (2), `Company A` (3), `Company D` (4)
16. Klik ikon sort pada header `Total SKU` sekali lagi
17. Verifikasi urutan descending: `Company D` (4), `Company A` (3), `Company B` (2), lalu `Company C` dan `Company E` (0) sesuai urutan Company A-Z
18. Klik ikon sort pada header `Total SKU` sekali lagi hingga indikator sort hilang

### TC-AC-DN-261: Sort kolom Total Stock pada Usage by Company secara numerik

19. Klik ikon sort pada header `Total Stock` sekali
20. Verifikasi urutan ascending: `Company D` (0), `Company B` (2), `Company C` (6), `Company E` (12), `Company A` (40)
21. Klik ikon sort pada header `Total Stock` sekali lagi
22. Verifikasi urutan descending: `Company A` (40), `Company E` (12), `Company C` (6), `Company B` (2), `Company D` (0)
23. Klik ikon sort pada header `Total Stock` sekali lagi hingga indikator sort hilang
24. Klik ikon `[X]` pada dialog Detail

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Satu pembukaan dialog Detail dipakai bersama keempat blok: tiap blok mengakhiri siklus sort dengan klik ketiga sehingga indikator sort hilang dan kolom berikutnya mulai dari urutan default (S-09). Klik ketiga pada blok TC-AC-DN-259 sampai TC-AC-DN-261 adalah langkah penghubung tanpa asersi (S-03); hanya TC-AC-DN-258 mengasersi klik ketiga.
- Ukuran spec: di bawah smell 35 langkah.
- Temuan untuk QA:
  - Post Condition kosong (`-`) pada semua TC spec ini (S-01).
  - TC-AC-DN-258 hingga TC-AC-DN-261 menyebut hanya `Company A` sampai `Company E`; Pre-setup #18 juga mencantumkan `Company F` sampai `Company I` untuk `Gate Antenna` yang dikhususkan bagi TC lain. Spec mengasumsikan baris itu tidak ada (lihat spec Usage lain di suite ini).
