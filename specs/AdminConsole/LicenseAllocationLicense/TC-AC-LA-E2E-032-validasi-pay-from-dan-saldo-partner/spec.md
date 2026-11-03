---
id: TC-AC-LA-E2E-032-validasi-pay-from-dan-saldo-partner
title: "Validasi Payment Partner: Pay From Kosong dan Saldo Kantong Kurang"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-117
  - TC-AC-LA-144
coverage:
  web: automated
---

# Validasi Payment Partner: Pay From Kosong dan Saldo Kantong Kurang

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Partner multi kantong `partnerMultiLic_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, Pre-setup #16), password `Spectra.env.AC_LA_PARTNER_MULTI_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): Partner satu kantong `partnerFullLic_automated_{namaCompany}@qwertysystem.net` (`Rian Tarigan`, Pre-setup #15), password `Spectra.env.AC_LA_PARTNER_FULL_PASSWORD`.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup: Client PT Abadi Jaya (#25, term `SUBS-20260110-C1D2E`), kantong wallet (#33), Product Price (#34: Concurrent User $365 per unit per tahun), kantong Partner CV Karya Mandiri saldo $20.00 untuk aktor `partnerFullLic` (#35). Kondisi saldo $20.00 (#35) diatur fixture backend (disediakan tim FE/BE) di hook `before` dan saldo dipulihkan ke keadaan awal di hook `after`.
- Jam: tanggal acuan server uji 22 Dec 2026 (fixture waktu, nilai absolut); jam server dan jam browser diatur bersama di hook `before` dan dipulihkan di hook `after`.
- Data Dinamis: tidak ada; kedua `[Submit]` diblokir (TC-AC-LA-117 oleh V-19; TC-AC-LA-144 tombol disabled) sehingga tidak ada alokasi yang dibuat.
- Baseline: daftar Allocation ID baris di halaman pertama tab Current dicatat sebelum aksi TC-AC-LA-117 (langkah 1).
- Kemampuan teknis: pengaturan saldo kantong (fixture backend, disediakan tim FE/BE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-117: Pay From kosong untuk Partner dengan lebih dari satu kantong ditolak (V-19)

1. Catat baseline Allocation ID baris di halaman pertama tab Current
2. Klik `[+ Allocation]`
3. Pilih Client `PT Abadi Jaya`, Target `SUBS-20260110-C1D2E`, Type `Concurrent User`, isi Additional Quantity `2`, biarkan Pay From kosong
4. Klik `[Submit]`
5. Verifikasi pesan inline di bawah Pay From `Pay From must not be empty`
6. Klik `[✕]` pada header
7. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
8. Klik `[Leave]`
9. Verifikasi sedikitnya satu baris tampil pada tab Current
10. Verifikasi daftar Allocation ID baris di halaman pertama tab Current sama dengan baseline langkah 1 (alokasi tidak dibuat)

### TC-AC-LA-144: Warning saldo kantong kurang dari Cost memblok Submit (V-18)

11. Ganti akun: logout `Budi Santoso`, login sebagai `Rian Tarigan` dengan `Spectra.env.AC_LA_PARTNER_FULL_PASSWORD`, buka Allocation > License Allocation tab Current
12. Klik `[+ Allocation]`
13. Pilih Client `PT Abadi Jaya`, Target `SUBS-20260110-C1D2E`, Type `Concurrent User`, isi Additional Quantity `10`
14. Tunggu preview Cost dimuat (skeleton hilang)
15. Verifikasi Alert severity danger `Insufficient balance in your pocket. Available: $20.00. Required: $100.00.`
16. Verifikasi Alert tampil real-time setelah preview Cost dimuat, tanpa klik `[Submit]`
17. Verifikasi tombol `[Submit]` disabled
18. Klik `[✕]` pada header
19. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
20. Klik `[Leave]`

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 2 kali, kejadian menutup 2 (langkah 6 sampai 8 dan 18 sampai 20).
- Kelas harness: blokir kondisi data (prinsip 12): kondisi penolak (Pay From kosong, saldo kantong $20.00) disiapkan milik spec; submit diblokir lalu cek tidak ada record.
- Langkah penghubung (S-03): langkah 1 (baseline), langkah 6 sampai 8 dan 18 sampai 20 (menutup form dirty, S-08), langkah 14 (menunggu preview Cost), dan ganti akun pada langkah 11 (S-07). Langkah 9 adalah anchor positif untuk asersi langkah 10 (bagian 8b butir 2).
- Temuan untuk QA:
  - Pre-setup #33 menyebut saldo kantong Partner CV Karya Mandiri $5,000.00 (dipakai TC-AC-LA-106, 153, 171, 530) sedangkan Pre-setup #35 menyebut saldo kantong yang sama untuk aktor `partnerFullLic` $20.00 (TC-AC-LA-144 dan 145); TC tidak menyatakan cara beralih. Spec menyiapkan saldo $20.00 lewat fixture backend yang disediakan tim FE/BE.
  - TC-AC-LA-117 Post Condition "Tidak ada record" dan Expected b "Alokasi tidak dibuat" tidak punya langkah observasi; spec membandingkan daftar dengan baseline (langkah 9 sampai 10) dan tidak mengasersi log.
  - TC-AC-LA-144 Expected c ("Alert muncul real-time setelah preview Cost dimuat") tidak menyebut selang waktu; spec hanya mengasersi Alert tampil tanpa klik `[Submit]` setelah preview dimuat.
