---
id: TC-AC-LA-E2E-039-preview-cost-per-jenis-license
title: "Preview Cost per Jenis License: Asset Control App, Storage, dan Station"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-148
  - TC-AC-LA-149
  - TC-AC-LA-150
  - TC-AC-LA-511
coverage:
  web: automated
---

# Preview Cost per Jenis License: Asset Control App, Storage, dan Station

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (hanya dibaca): Bengkel Cahaya Motor (#23, FAMS Professional Paid Active, End Date 31 Dec 2026, belum punya Asset Control App), Klinik Harapan Bunda (#24), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (#33), Product Price (#34: Asset Control App flat $150.00, Storage $2 per GB, Asset Control Station $50.00 per Station).
- Jam: tanggal acuan server uji 22 Dec 2026 (fixture waktu, nilai absolut, disediakan tim FE/BE) di hook `before`; digeser ke 30 Dec 2026 pada langkah 18 untuk TC-AC-LA-150; jam server dan jam browser diatur bersama dan dipulihkan di hook `after`.
- Data Dinamis: tidak ada; tidak ada `[Submit]` pada spec ini.
- State global yang diubah: jam server dan jam browser (lihat Jam).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik `[+ Allocation]`

### TC-AC-LA-148: Preview Asset Control App flat activation fee

2. Pilih Client `Bengkel Cahaya Motor`, Target term FAMS Professional, Type `Asset Control App`
3. Tunggu preview Cost dimuat (skeleton hilang)
4. Verifikasi baris Cost `Cost: $150.00 (flat activation fee)` tanpa faktor qty dan hari

### TC-AC-LA-149: Preview Storage dihitung per GB tanpa faktor hari

5. Pilih Client `Klinik Harapan Bunda`, Target `Client-wide`, Type `Storage`, isi Additional Quantity `50`
6. Tunggu preview Cost dimuat (skeleton hilang)
7. Verifikasi baris Cost `Cost: $100.00 (50 GB × $2/GB)` tanpa faktor hari

### TC-AC-LA-511: Preview Cost Asset Control Station Quantity × harga per unit tanpa faktor hari

8. Ganti Type ke `Asset Control Station` dan isi Additional Quantity `3`
9. Verifikasi baris Cost `Cost: $150.00 (3 × $50/unit)`
10. Verifikasi baris Cost langkah 9 tanpa faktor `days remaining`
11. Ubah Additional Quantity menjadi `10`
12. Verifikasi baris Cost `Cost: $500.00 (10 × $50/unit)`
13. Verifikasi baris Cost langkah 12 tanpa faktor `days remaining`

### TC-AC-LA-150: Cost Asset Control Station sama pada tanggal Submit berbeda

14. Verifikasi baris Cost pada tanggal acuan 22 Dec 2026 `Cost: $500.00 (10 × $50/unit)` tanpa faktor `days remaining`
15. Klik `[×]` pada header
16. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
17. Klik `[Leave]`
18. Geser jam server dan jam browser ke 30 Dec 2026, lalu buka ulang Allocation > License Allocation tab Current
19. Klik `[+ Allocation]`
20. Pilih Client `Klinik Harapan Bunda`, Target `Client-wide`, Type `Asset Control Station`, isi Additional Quantity `10`
21. Tunggu preview Cost dimuat (skeleton hilang)
22. Verifikasi baris Cost pada tanggal acuan 30 Dec 2026 `Cost: $500.00 (10 × $50/unit)` tanpa faktor `days remaining`
23. Verifikasi nilai Cost tidak berubah menurut tanggal Submit (sama dengan nilai pada 22 Dec 2026)
24. Klik `[×]` pada header
25. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
26. Klik `[Leave]`

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 2 kali, kejadian menutup 2 (langkah 15 sampai 17 dan 24 sampai 26).
- Penyimpangan urutan (S-10): TC-AC-LA-511 dijalankan sebelum TC-AC-LA-150 karena sama-sama memakai Station pada Klinik Harapan Bunda; observasi 22 Dec 2026 TC-AC-LA-150 (Langkah 6 TC) berada di langkah 14 pada form yang sama, lalu jam digeser dan form dibuka ulang (Langkah 7 TC).
- Langkah penghubung (S-03): langkah 3, 6, dan 21 (menunggu preview), langkah 15 sampai 17 dan 24 sampai 26 (menutup form dirty, S-08), dan langkah 18 (menggeser jam; jam dipulihkan di hook `after`).
- Temuan untuk QA:
  - TC-AC-LA-148 Langkah 3 menulis Target "term FAMS Professional" tanpa ID Subscription; Pre-setup #23 tidak mencantumkan ID.
  - TC-AC-LA-150 Data Uji menyebut "$50.00 per Station (nilai Example Data $500.00)" sedangkan Pre-setup #34 menyebut harga Station sebagai "angka ilustrasi"; spec memakai $50.00 sesuai #34.
  - TC-AC-LA-511 Expected c ("tanpa faktor `days remaining`") berlaku untuk dua baris sekaligus; spec memuatnya sebagai dua `Verifikasi`, satu per baris tepat sesudah baris itu tampil (langkah 10 dan 13).
