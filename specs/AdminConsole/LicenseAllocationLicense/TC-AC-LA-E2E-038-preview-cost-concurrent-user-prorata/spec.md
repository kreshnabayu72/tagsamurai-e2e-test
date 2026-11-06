---
id: TC-AC-LA-E2E-038-preview-cost-concurrent-user-prorata
title: "Preview Cost Concurrent User: Prorata Hari, Term Pending, dan Real-time"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-140
  - TC-AC-LA-142
  - TC-AC-LA-152
coverage:
  web: automated
---

# Preview Cost Concurrent User: Prorata Hari, Term Pending, dan Real-time

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (hanya dibaca): PT Sejahtera (#19, `SUBS-20260101-A1B2C`, End Date 31 Dec 2026), Toko Serba Ada (#21, term Pending `SUBS-20260819-00001`, 1 Jan 2027 sampai 31 Dec 2027, 365 hari), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (#33), Product Price (#34: Concurrent User $365 per unit per tahun).
- Jam: tanggal acuan server uji 22 Dec 2026 (fixture waktu, nilai absolut, disediakan tim FE/BE); jam server dan jam browser diatur bersama di hook `before` dan dipulihkan di hook `after`.
- Data Dinamis: tidak ada; tidak ada `[Submit]` pada spec ini.
- State global: jam server dan jam browser (lihat Jam).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik `[+ Allocation]`

### TC-AC-LA-140: Preview Cost prorata 10 hari untuk Concurrent User ke term Active

2. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `10`
3. Tunggu preview Cost dimuat (skeleton hilang)
4. Verifikasi baris Cost `Cost: $100.00 (10 × $365/unit × 10 days remaining ÷ 365)`
5. Verifikasi faktor hari 10 (22 sampai 31 Dec 2026, kedua tanggal dihitung)
6. Verifikasi baris `Your pocket balance: $10,000.00`

### TC-AC-LA-152: Preview Cost diperbarui real-time saat Additional Quantity berubah

7. Ubah Additional Quantity menjadi `20`
8. Verifikasi Cost berubah dari `$100.00` menjadi `$200.00` tanpa `[Submit]`

### TC-AC-LA-142: Target term Pending menghitung hari dari Start Date term Target

9. Pilih Client `Toko Serba Ada`, Target `SUBS-20260819-00001`, Type `Concurrent User`, ganti isi Additional Quantity dengan `10`
10. Verifikasi baris Cost `Cost: $3,650.00 (10 × $365/unit × 365 days remaining ÷ 365)`
11. Verifikasi hari dihitung dari Start Date term, bukan tanggal Submit
12. Verifikasi pembagi tetap 365
13. Klik `[×]` pada header
14. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
15. Klik `[Leave]`

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 1 kali, kejadian menutup 1 (langkah 13 sampai 15).
- Pembagian TC lintas spec: TC-AC-LA-141 (hari terakhir term) dan TC-AC-LA-154 (zona waktu Plan Owner) ada di spec 053 karena membutuhkan tanggal server dan zona waktu yang berbeda dari 22 Dec 2026.
- Penyimpangan urutan (S-05, S-10): TC-AC-LA-152 dijalankan sebelum TC-AC-LA-142 karena melanjutkan form TC-AC-LA-140 (Additional Quantity 10 diubah menjadi 20), sehingga jumlah buka form tetap 1. Langkah 9 memilih ulang Client agar state awal TC-AC-LA-142 sama dengan form baru.
- Langkah penghubung (S-03): langkah 3 (menunggu preview) dan langkah 13 sampai 15 (menutup form dirty, S-08).
- Temuan untuk QA:
  - TC-AC-LA-140 Expected b ("Faktor hari 10") adalah bagian dari rumus pada baris Cost; spec mengasersi faktor hari sebagai klausa terpisah dari teks baris Cost (langkah 5).
  - TC-AC-LA-152 Expected a ("Cost berubah dari `$100.00` menjadi `$200.00`") menyiratkan nilai Cost sebelumnya dari TC-AC-LA-140; spec mengasersi nilai akhir `$200.00` setelah perubahan Additional Quantity dari 10 menjadi 20 pada form yang sama.
