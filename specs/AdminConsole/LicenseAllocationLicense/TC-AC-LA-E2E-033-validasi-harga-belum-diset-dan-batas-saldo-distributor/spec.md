---
id: TC-AC-LA-E2E-033-validasi-harga-belum-diset-dan-batas-saldo-distributor
title: "Validasi Payment Distributor: Harga Belum Di-set dan Batas Saldo Wallet 15 Digit"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-146
  - TC-AC-LA-510
coverage:
  web: automated
---

# Validasi Payment Distributor: Harga Belum Di-set dan Batas Saldo Wallet 15 Digit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup: Client PT Sejahtera (#19, term `SUBS-20260101-A1B2C`), Klinik Harapan Bunda (#24, Client-wide), Product Price (#34: Asset Control Station $50.00 per Station), item Addon Maps pada Product Price kantong Distributor belum di-set (#37), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (#33). Kondisi harga Maps belum di-set dijamin fixture backend (disediakan tim FE/BE) di hook `before` dan dipulihkan di hook `after`.
- Data Dinamis: tidak ada; kedua blok diblokir sehingga tidak ada alokasi yang dibuat.
- Baseline: daftar Allocation ID baris di halaman pertama tab Current dicatat sebelum aksi pertama (langkah 1).
- Kemampuan teknis: mengisi 15 digit ke field Additional Quantity.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Catat baseline Allocation ID baris di halaman pertama tab Current
2. Klik `[+ Allocation]`

### TC-AC-LA-146: Harga item belum di-set memblok Submit dengan tooltip V-17

3. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Maps`, isi Additional Quantity `1`
4. Hover tombol `[Submit]`
5. Verifikasi tombol `[Submit]` disabled
6. Verifikasi tooltip `Set product price first (Wallet > Product Price).`

### TC-AC-LA-510: Additional Quantity 15 digit oleh Distributor tetap dibatasi saldo Wallet (V-18)

7. Pilih Client `Klinik Harapan Bunda`, Target `Client-wide`, Type `Asset Control Station`, isi Additional Quantity `999999999999999`
8. Tunggu preview Cost dimuat (skeleton hilang)
9. Verifikasi field Additional Quantity menampilkan nilai `999999999999999` utuh (anchor)
10. Verifikasi tidak ada error `Max. 15 characters` pada Additional Quantity
11. Verifikasi Alert severity danger berawalan `Insufficient balance in your pocket. Available: $10,000.00. Required:` diikuti nominal Cost hasil hitung (999999999999999 × $50.00)
12. Verifikasi tombol `[Submit]` disabled
13. Klik `[×]` pada header
14. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
15. Klik `[Leave]`
16. Verifikasi sedikitnya satu baris tampil pada tab Current
17. Verifikasi daftar Allocation ID baris di halaman pertama tab Current sama dengan baseline langkah 1 (tidak ada record dari TC-AC-LA-510)

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 1 kali, kejadian menutup 1 (langkah 13 sampai 15).
- Kelas harness: blokir kondisi data (prinsip 12); kondisi penolak disiapkan milik spec dan submit diblokir lalu cek tidak ada record.
- Langkah penghubung (S-03): langkah 1 (baseline), langkah 8 (menunggu preview Cost), langkah 13 sampai 15 (menutup form dirty, S-08). Langkah 16 adalah anchor positif untuk asersi langkah 17 (bagian 8b butir 2). Mengganti Client pada langkah 7 mereset Target, Type, dan Current Quota (TC-AC-LA-136) sehingga TC-AC-LA-510 dimulai dari state yang setara dengan form baru; Additional Quantity `1` dari langkah 3 ditimpa.
- Asersi tambahan (S-03): langkah 9 (field Additional Quantity menampilkan nilai utuh) adalah anchor positif pada form yang sama sebelum asersi absence error `Max. 15 characters` pada langkah 10 (bagian 8b butir 2, keputusan 2026-11-04).
- Temuan untuk QA:
  - TC-AC-LA-510 Expected b hanya menyebut awalan Alert dan "nominal Cost hasil hitung"; 999999999999999 × $50.00 = $49,999,999,999,999,950.00 melebihi bilangan bulat aman JavaScript (2^53), sehingga nominal persis dapat tergeser; TC tidak menyatakan nilai persis dan spec tidak mengasersi nominal persis.
  - TC-AC-LA-146 dan TC-AC-LA-510 memakai Post Condition "Tidak ada record" tanpa langkah observasi; spec membandingkan daftar dengan baseline dan tidak mengasersi log.
  - Pre-setup #37 (harga Maps belum di-set) bertentangan dengan TC-AC-LA-158 yang mensyaratkan harga kelima Addon (termasuk Maps) di-set, dan #34 tidak mencantumkan harga Audit, Maintenance, Tracking, dan Maps; pengaturan harga antar TC diserahkan ke fixture backend.
