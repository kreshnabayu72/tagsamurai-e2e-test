---
id: TC-AC-LA-E2E-026-perpindahan-baris-antar-tab-cancel-dan-resubmit
title: "Perpindahan Baris Antar Tab: Cancel dan Resubmit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-31
  - TC-AC-LA-32
coverage:
  web: automated
---

# Perpindahan Baris Antar Tab: Cancel dan Resubmit

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Distributor Create+Read+Update (PT Maju Bersama) (Pre-setup #4) `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data milik spec (seeding backend di hook `before`, requester `Dewi A`, dibersihkan di hook `after`): satu alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera (Cost $150.00 di-Reserve, menyerupai Pre-setup #41) dan satu alokasi `Canceled` manual Concurrent User +5 PT Sejahtera (menyerupai Pre-setup #48). Allocation ID dirujuk lewat `Fixture.license-allocation-license` (kunci ownWaiting, ownCanceled).
- Konfigurasi Pre-setup #38: Require Approval for Allocation ON pada group Client uji (dipastikan fixture backend sebelum spec; tidak diubah spec). Record hasil Resubmit (berstatus `Waiting for Approval`, Cost $150.00 di-Reserve) dibersihkan fixture backend di hook `after`.
- Kemampuan teknis: baca Allocation ID record terbaru milik `Dewi A` lewat fixture BE (disediakan tim FE/BE); baca jumlah entri Allocation Log lewat UI modal.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-31: Baris berpindah tab otomatis saat status berubah

1. Ketik Search Allocation ID alokasi `Waiting for Approval` milik spec (`Fixture.license-allocation-license.ownWaiting`), tekan Enter
2. Klik Allocation ID baris untuk membuka modal `Allocation Log`, catat jumlah entri sebagai baseline, lalu tutup modal dengan `[✕]`
3. Klik ikon `⋯` pada baris itu, lalu klik `Cancel Allocation`
4. Klik `[Cancel Request]` pada dialog konfirmasi dan tunggu aksi selesai
5. Verifikasi hasil Search tab Current kosong dengan empty state `No results found` (baris hilang dari tab Current)
6. Klik tab `History`
7. Ketik Search Allocation ID `Fixture.license-allocation-license.ownWaiting`, tekan Enter
8. Verifikasi baris tampil di tab History dengan Status `Canceled`
9. Klik ikon `⋯` pada baris itu, lalu klik `Allocation Log`
10. Verifikasi Allocation Log bertambah tepat satu entri dibanding baseline
11. Verifikasi entri baru bertuliskan `Allocation canceled by Dewi A`
12. Tutup modal dengan `[✕]`

### TC-AC-LA-32: Resubmit dari baris Canceled membuat record baru di Current

13. Ganti isi kotak search dengan Allocation ID alokasi `Canceled` milik spec (`Fixture.license-allocation-license.ownCanceled`), tekan Enter
14. Klik ikon `⋯` pada baris `Canceled` milik sendiri, lalu klik `Resubmit`
15. Klik `[Submit]` pada form pre-filled dan tunggu aksi selesai
16. Baca Allocation ID record baru milik `Dewi A` lewat fixture BE hingga record baru tersimpan
17. Klik `(←)` pada kotak Search, lalu klik tab `Current`
18. Ketik Search Allocation ID record baru, tekan Enter
19. Verifikasi record baru dengan Allocation ID baru (berbeda dari `Fixture.license-allocation-license.ownCanceled`) tampil di tab Current dengan Status `Waiting for Approval`
20. Klik tab `History`
21. Ganti isi kotak search dengan Allocation ID `Fixture.license-allocation-license.ownCanceled`, tekan Enter
22. Verifikasi baris `Canceled` asal tetap berada di tab History
23. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), langkah mencatat baseline Allocation Log dan menutup modal, langkah menunggu aksi selesai, langkah pindah tab, dan langkah membaca Allocation ID record baru lewat fixture BE.
- Dalam TC-AC-LA-31 asersi hilangnya baris dari tab Current memakai empty state `No results found` hasil Search sebagai anchor; toast sukses Cancel tidak ada di Expected TC dan tidak diasersi.
- Temuan untuk QA:
  - TC-AC-LA-31 Expected c (`Allocation Log hanya bertambah entri ... dan tidak ada entri lain`) tidak menyebut baseline; spec mencatat jumlah entri sebelum Cancel dan mengasersi selisih satu.
  - TC-AC-LA-31 dan TC-AC-LA-32 menyebut Pre-setup #41 dan #48; spec memakai record milik spec yang menyerupai keduanya karena aksi tulis (S-06).
  - TC-AC-LA-32 Expected a menyebut `Allocation ID baru` tanpa cara membacanya; spec membaca ID lewat fixture BE.
  - Post Condition TC-AC-LA-31 (`Record berstatus Canceled`) dan TC-AC-LA-32 (`Record baru tercatat`) sudah tercakup Expected; tidak ada asersi tambahan.
