---
id: TC-AC-LA-E2E-028-screening-payment-distributor-dan-partner
title: "Screening Section Payment: Distributor dan Partner (Pay From)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-104
  - TC-AC-LA-105
  - TC-AC-LA-106
coverage:
  web: automated
---

# Screening Section Payment: Distributor dan Partner (Pay From)

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): Partner multi kantong `partnerMultiLic_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, Pre-setup #16), password `Spectra.env.AC_LA_PARTNER_MULTI_PASSWORD`; lalu Partner satu kantong `partnerFullLic_automated_{namaCompany}@qwertysystem.net` (`Rian Tarigan`, Pre-setup #15), password `Spectra.env.AC_LA_PARTNER_FULL_PASSWORD`.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga Product Price.
- Data Pre-setup: Client PT Sejahtera (#19, `SUBS-20260101-A1B2C`), PT Abadi Jaya (#25, `SUBS-20260110-C1D2E`), kantong wallet (#33: Distributor PT Maju Bersama $10,000.00, Partner CV Karya Mandiri $5,000.00, Principal $5,000.00), Product Price (#34: Concurrent User $365 per unit per tahun). Toggle Require Approval for Allocation OFF (#39) untuk TC-AC-LA-106, diatur fixture backend (disediakan tim FE/BE) di hook `before` dan dipulihkan di hook `after`.
- Jam: tanggal acuan server uji 22 Dec 2026 (fixture waktu, nilai absolut, disediakan tim FE/BE); jam server dan jam browser diatur bersama di hook `before` dan dipulihkan di hook `after`.
- Data Dinamis: satu alokasi Concurrent User +2 PT Abadi Jaya dari `[Submit]` TC-AC-LA-106; tidak dapat dihapus (tanpa Delete), dipulihkan baseline automation.
- Kemampuan teknis: membaca saldo kantong (disediakan tim FE/BE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-104: Screening section Payment untuk Distributor

1. Klik `[+ Allocation]`
2. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `10`
3. Verifikasi section Payment tanpa pilihan Payment Method
4. Verifikasi field Pay From tidak dirender (kantong tunggal)
5. Verifikasi baris preview `Cost: $100.00 (10 × $365/unit × 10 days remaining ÷ 365)`
6. Verifikasi baris `Your pocket balance: $10,000.00`
7. Klik `[✕]` pada header
8. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
9. Klik `[Leave]`

### TC-AC-LA-105: Screening Pay From untuk Partner dengan lebih dari satu kantong

10. Ganti akun: logout `Dewi A`, login sebagai `Budi Santoso` dengan `Spectra.env.AC_LA_PARTNER_MULTI_PASSWORD`, buka Allocation > License Allocation tab Current
11. Klik `[+ Allocation]`
12. Pilih Client `PT Abadi Jaya`, Target `SUBS-20260110-C1D2E`, Type `Concurrent User`, isi Additional Quantity `2`
13. Verifikasi field Pay From tampil dengan placeholder `Select pay from`
14. Buka dropdown Pay From
15. Verifikasi opsi berlabel tipe entitas: `PT Maju Bersama (Distributor)` dan `PT ABC (Principal)`
16. Pilih opsi `PT ABC (Principal)`
17. Verifikasi nilai terpilih menampilkan label opsi yang sama, `PT ABC (Principal)`
18. Klik `[✕]` pada header
19. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
20. Klik `[Leave]`

### TC-AC-LA-106: Screening kondisi Partner dengan satu kantong, Pay From tidak diwajibkan

21. Ganti akun: logout `Budi Santoso`, login sebagai `Rian Tarigan` dengan `Spectra.env.AC_LA_PARTNER_FULL_PASSWORD`, buka Allocation > License Allocation tab Current
22. Klik `[+ Allocation]`
23. Pilih Client `PT Abadi Jaya`, Target `SUBS-20260110-C1D2E`, Type `Concurrent User`, isi Additional Quantity `2`
24. Verifikasi Pay From pre-filled dengan kantong tunggal dan tidak perlu dipilih
25. Klik `[Submit]`
26. Verifikasi pesan V-19 `Pay From must not be empty` tidak tampil di bawah Pay From
27. Tunggu aksi selesai (modal tertutup)

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 3 kali, kejadian menutup 3 (langkah 7 sampai 9, 18 sampai 20, dan modal tertutup oleh Submit di langkah 27).
- Langkah penghubung (S-03): langkah 7 sampai 9 dan 18 sampai 20 (menutup form dirty secara deterministik, S-08), langkah 16 (memilih opsi agar nilai terpilih dapat diasersi), langkah 25 dan 27 (lihat Temuan), dan ganti akun pada langkah 10 dan 21 (S-07).
- Label opsi Pay From Distributor ditulis `PT Maju Bersama (Distributor)` berdasarkan Pre-setup #25 (PT Abadi Jaya di bawah Distributor PT Maju Bersama) dan #33 (kantong Partner CV Karya Mandiri relasi utama Distributor); lihat Temuan.
- Temuan untuk QA:
  - TC-AC-LA-105 Expected b memakai templat `[Nama Distributor] (Distributor)` tanpa menyebut nama Distributor; spec memakai `PT Maju Bersama` hasil turunan dari Pre-setup #25 dan #33.
  - TC-AC-LA-106 Expected b ("Submit tidak menampilkan V-19") tidak punya langkah klik `[Submit]` di Langkah Uji dan tidak menyebut status toggle Require Approval; spec menambah klik `[Submit]` (langkah 25) dengan toggle OFF (#39) sehingga satu alokasi tercipta. Pesan V-19 yang diasersi tidak tampil, bukan keberhasilan Submit.
  - Pre-setup #33 menyebut saldo kantong Partner CV Karya Mandiri $5,000.00 (dipakai TC-AC-LA-106) sedangkan Pre-setup #35 menyebut kantong Partner untuk aktor `partnerFullLic` saldo $20.00 (dipakai TC-AC-LA-144); satu kantong tidak bisa bernilai dua saldo pada baseline yang sama. Spec ini memakai #33; pengaturan saldo antar-TC diserahkan ke fixture backend.
  - Pre-setup #4 menyebut toggle approval ON pada akun `dewiFullLic`, sedangkan toggle adalah konfigurasi group Client (Pre-setup #38 dan #39) bukan atribut akun; TC-AC-LA-104 tidak menyebut statusnya dan tidak memengaruhi asersi.
