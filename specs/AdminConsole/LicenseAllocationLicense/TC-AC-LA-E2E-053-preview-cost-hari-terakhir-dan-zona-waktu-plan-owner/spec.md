---
id: TC-AC-LA-E2E-053-preview-cost-hari-terakhir-dan-zona-waktu-plan-owner
title: "Preview Cost Hari Terakhir Term dan Zona Waktu Plan Owner"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LA-141
  - TC-AC-LA-154
coverage:
  web: automated
---

# Preview Cost Hari Terakhir Term dan Zona Waktu Plan Owner

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (hanya dibaca): PT Sejahtera (#19, `SUBS-20260101-A1B2C`, End Date 31 Dec 2026), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (#33), Product Price (#34: Concurrent User $365 per unit per tahun).
- Jam (nilai absolut, disediakan tim FE/BE): TC-AC-LA-141 memakai tanggal server uji 31 Dec 2026 (End Date term); TC-AC-LA-154 memakai waktu server uji 21 Dec 2026 23:30 UTC. Jam server dan jam browser diatur bersama di langkah 1 dan 10 dan dipulihkan di hook `after`.
- State global yang diubah: jam server dan jam browser; zona waktu General Settings Plan Owner term menjadi UTC+07:00 (22 Dec 2026 06:30) untuk TC-AC-LA-154, diatur fixture backend (disediakan tim FE/BE) pada langkah 10 dan dipulihkan ke nilai awal di hook `after`.
- Data Dinamis: tidak ada; tidak ada `[Submit]` pada spec ini.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-141: Hari terakhir term dihitung minimum satu hari

1. Atur jam server dan jam browser ke 31 Dec 2026 (End Date term), lalu buka ulang Allocation > License Allocation tab Current
2. Klik `[+ Allocation]`
3. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `10`
4. Tunggu preview Cost dimuat (skeleton hilang)
5. Verifikasi baris Cost `Cost: $10.00 (10 × $365/unit × 1 days remaining ÷ 365)` dengan faktor hari 1 (minimum 1 hari)
6. Klik `[×]` pada header
7. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
8. Klik `[Leave]`

### TC-AC-LA-154: Hari prorata dihitung dari tanggal Submit pertama pada zona waktu Plan Owner

9. Atur zona waktu General Settings Plan Owner term ke UTC+07:00 lewat fixture backend hingga tersimpan
10. Atur jam server ke 21 Dec 2026 23:30 UTC dan jam browser setara, lalu buka ulang Allocation > License Allocation tab Current
11. Klik `[+ Allocation]`
12. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `10`
13. Tunggu preview Cost dimuat (skeleton hilang)
14. Verifikasi faktor hari dihitung 10 (tanggal Submit 22 Dec 2026 pada zona waktu Plan Owner), bukan 11
15. Verifikasi Cost `$100.00`
16. Klik `[×]` pada header
17. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
18. Klik `[Leave]`

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 2 kali, kejadian menutup 2 (langkah 6 sampai 8 dan 16 sampai 18).
- Pembagian TC lintas spec: TC-AC-LA-140, 142, dan 152 (tanggal 22 Dec 2026) ada di spec 038.
- Langkah penghubung (S-03): langkah 1, 9, dan 10 (mengatur jam dan zona waktu), langkah 4 dan 13 (menunggu preview), dan langkah 6 sampai 8 serta 16 sampai 18 (menutup form dirty, S-08).
- Temuan untuk QA:
  - TC-AC-LA-154 tidak menyebut akun atau mekanisme yang mengubah zona waktu General Settings Plan Owner term maupun entitas Plan Owner (PT Maju Bersama atau entitas lain); spec menandainya "disediakan tim FE/BE" tanpa endpoint karangan (S-13).
  - TC-AC-LA-141 Precondition d menyebut "Tanggal acuan server uji 31 Dec 2026 (End Date term)" tanpa jam; spec mengatur hanya tanggal (nilai absolut) dan jam sama dengan zona waktu Plan Owner bawaan.
