---
id: TC-AC-LA-E2E-088-defense-validasi-request-langsung-quantity-saldo-edit-dan-markup
title: "Defense-in-Depth: Quantity Non-bulat, Saldo, Edit Request Langsung, dan Markup Nama Client"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-115
  - TC-AC-LA-145
  - TC-AC-LA-483
  - TC-AC-LA-508
  - TC-AC-LA-457
coverage:
  web: automated
---

# Defense-in-Depth: Quantity Non-bulat, Saldo, Edit Request Langsung, dan Markup Nama Client

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Pre-setup #1), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): Partner satu kantong `partnerFullLic_automated_{namaCompany}@qwertysystem.net` (`Rian Tarigan`, Pre-setup #15), password `Spectra.env.AC_LA_PARTNER_FULL_PASSWORD`; Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (hanya dibaca; semua request ditolak sehingga tidak ada perubahan): PT Sejahtera (#19) dengan term FAMS `SUBS-20260101-A1B2C`, PT Abadi Jaya (#25), kantong Partner CV Karya Mandiri saldo $20.00 (#35), kantong wallet (#33), Product Price (#34), Toko Campuran (#69) dengan term SIEM `SUBS-20260501-S1T2U` dan term FAMS Free `SUBS-20260502-F3R4E`, toggle Require Approval for Allocation ON (#38). Tanggal acuan server uji 22 Dec 2026 (fixture waktu) untuk TC-AC-LA-145.
- Data Dinamis (seeding lewat API di hook `before`, milik spec ini): alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera oleh `Dewi A` (Cost $150.00 di-Reserve; bentuk #41) untuk TC-AC-LA-483; alokasi `Waiting for Approval` Concurrent User +2 ke `SUBS-20260501-S1T2U` Toko Campuran oleh `Dewi A` (Cost $60.00 di-Reserve; bentuk #70) untuk TC-AC-LA-508; satu Client bersuffix `<script>alert(1)</script> {runId}-088` binaan Distributor PT Maju Bersama dengan alokasi beriwayat log (bentuk #55) untuk TC-AC-LA-457. Allocation ID dan nama Client dibaca dari hasil seeding.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP atau fixture BE yang mengirim request submit dan Edit langsung ke server memakai sesi API aktor masing-masing (login API tidak dihitung sebagai sesi web, `suite.md`), membaca jumlah alokasi dan nilai record lewat fixture BE (tanpa mengarang endpoint, S-13), dan mengatur tanggal acuan server.
- State global yang diubah: tanggal acuan server (dipulihkan di hook `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-115: Request langsung dengan Quantity non-bulat ditolak server

1. Catat jumlah alokasi PT Sejahtera lewat fixture BE sebagai baseline
2. Kirim request submit alokasi langsung ke server dengan Additional Quantity `1.5` untuk Client `PT Sejahtera`
3. Verifikasi respons server menolak sebagai input tidak valid dengan pesan `Additional Quantity must be a whole number` pada field Additional Quantity
4. Verifikasi tidak ada record dibuat (jumlah alokasi PT Sejahtera sama dengan baseline)

### TC-AC-LA-145: Guard server saldo tidak cukup

5. Ganti akun: logout `Hendra W`, login sebagai `Rian Tarigan` dengan `Spectra.env.AC_LA_PARTNER_FULL_PASSWORD`
6. Atur tanggal acuan server uji ke 22 Dec 2026 (fixture waktu), lalu catat jumlah alokasi PT Abadi Jaya dan saldo kantong Partner sebagai baseline
7. Kirim request submit alokasi langsung ke server untuk Concurrent User +10 pada `PT Abadi Jaya` (Cost $100.00, saldo $20.00)
8. Verifikasi respons server menolak dengan pesan `Insufficient wallet balance.`
9. Verifikasi alokasi tidak dibuat (jumlah alokasi PT Abadi Jaya sama dengan baseline)
10. Verifikasi saldo kantong Partner tidak berubah dari baseline

### TC-AC-LA-483: Edit memvalidasi ulang kombinasi Type dan Product Target (V-25)

11. Ganti akun: logout `Rian T`, login sebagai `Dewi Anggraini` dengan `Spectra.env.AC_LA_DIST_FULL_PASSWORD`
12. Kirim request Edit langsung untuk alokasi seed 483 milik sendiri dengan Type `Log Source` pada Target FAMS `SUBS-20260101-A1B2C`
13. Verifikasi respons server menolak sebagai input tidak valid dengan pesan `This license type is not available for the selected subscription.`
14. Verifikasi record seed 483 tetap Type `Concurrent User`, Quantity `5`, dan Reserve `$150.00`

### TC-AC-LA-508: Edit memvalidasi ulang Target Paid dengan Target Free (S-06)

15. Kirim request Edit langsung untuk alokasi seed 508 milik sendiri dengan Target term FAMS Free `SUBS-20260502-F3R4E` dan Type `Concurrent User`
16. Verifikasi respons server menolak sebagai input tidak valid dengan pesan `Only Paid subscriptions can be allocated. Free plan uses its fixed plan cap.`
17. Verifikasi record seed 508 tetap Target SIEM `SUBS-20260501-S1T2U`, Quantity `2`, dan Reserve utuh

### TC-AC-LA-457: Nama Client berisi markup tampil sebagai teks

18. Ketik Search nama Client seed markup di tab Current, tekan Enter
19. Verifikasi nama Client `<script>alert(1)</script> {runId}-088` tampil sebagai teks biasa pada List
20. Verifikasi tidak ada dialog alert yang dieksekusi dari nama Client pada List
21. Klik row action `Allocation Log` pada baris alokasi Client itu
22. Verifikasi nama Client tampil sebagai teks biasa pada Allocation Log
23. Verifikasi tidak ada dialog alert yang dieksekusi dari nama Client pada Allocation Log
24. Tutup modal Allocation Log, lalu buka Changelog dan cari entri Client itu
25. Verifikasi nama Client tampil sebagai teks biasa pada Changelog
26. Verifikasi tidak ada dialog alert yang dieksekusi dari nama Client pada Changelog

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC kelas a yang Expected-nya respons API (TC-AC-LA-115, 145, 483, 508) tetap masuk spec FE+BE walau tumpang tindih dengan TC backend; modul ini tidak punya TC backend. TC-AC-LA-457 berpemicu UI.
- Langkah penghubung (S-03): langkah 1 dan 6 (baseline, S-12), 5 dan 11 (ganti akun), 18 (Search untuk menemukan baris target, R-16), 24 (menutup modal dan membuka Changelog). Asersi hanya respons server dan state data lewat fixture BE (8b butir 1).
- Asersi absence (langkah 4, 9, 10, 20, 23, 26) berbaseline dan beranchor respons server yang sudah diasersi atau teks nama yang tampil pada surface yang sama.
- Temuan untuk QA:
  - TC-AC-LA-115, 145, 483, 508 tidak menyebut status HTTP penolakan; spec mengasersi penolakan dan pesan sesuai TC.
  - TC-AC-LA-145 Expected a tidak menyebut Target dan Type selain Concurrent User +10 pada PT Abadi Jaya; spec memakai Target term Paid Active PT Abadi Jaya.
  - TC-AC-LA-457 Precondition d ("Nama Client `<script>alert(1)</script>` di data uji") bukan baris Pre-setup dan tidak menyebut cara membuat Client; spec memakai Client seed bersuffix yang disediakan tim FE. TC juga tidak menyebut pelaku pengecek eksekusi skrip; spec mengasersi tidak ada dialog alert.
  - TC-AC-LA-457 Langkah 1 ("Buka List, Allocation Log, dan Changelog untuk Client itu") tidak menyebut apakah Changelog dibuka dari modal List; spec membukanya lewat ikon Changelog.
  - TC-AC-LA-508 Precondition menyebut Toko Campuran (#69) sebagai data Pre-setup; record target Edit adalah seed milik spec (S-06).
