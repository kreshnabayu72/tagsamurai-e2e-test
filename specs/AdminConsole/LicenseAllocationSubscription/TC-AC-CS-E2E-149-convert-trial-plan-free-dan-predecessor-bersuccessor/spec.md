---
id: TC-AC-CS-E2E-149-convert-trial-plan-free-dan-predecessor-bersuccessor
title: "Convert Trial: Plan Free dan Predecessor Bersuccessor"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-CS-252
  - TC-AC-CS-253
coverage:
  web: automated
---

# Convert Trial: Plan Free dan Predecessor Bersuccessor

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): Total Control Principal PT ABC, Hendra Wijaya (Pre-setup #1), `totalControlSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_TC_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data Pre-setup: Client `Bengkel Cahaya Motor` dengan term paid FAMS plan Free (`rank=0`) Active (Plan Owner CV Karya Mandiri) dan trial FAMS Growth Active (#74); Client `Toko Prima Sentosa` (binaan langsung PT Maju Bersama) dengan term paid FAMS Active `SUBS-20250825-00001` yang sudah punya successor Waiting for Approval `SUBS-20260817-00006` dan trial FAMS Growth Active `SUBS-20260810-00005` (#115).
- Data Dinamis: tidak ada; kedua kasus tidak menyimpan perubahan data.

## Test Steps

### TC-AC-CS-252: Convert pada Client dengan plan Free berjalan memakai mode Renewal Change plan

1. Ketik Search `Bengkel Cahaya Motor`, tekan Enter, lalu klik ikon `⋯` pada baris term Free
2. Verifikasi item `Renew` tampil enabled
3. Klik item `Renew`
4. Verifikasi dialog blok Title "Cannot Renew Subscription" dengan Body "• Bengkel Cahaya Motor — FAMS" dan "This client has an active trial. Use Convert on the trial row."
5. Klik `[OK]`, lalu klik ikon `⋯` pada baris trial dan pilih `Convert`
6. Verifikasi form Convert terbuka dalam mode Renewal dengan Renewal Option Disabled `Change plan`
7. Klik `[✕]`

### TC-AC-CS-253: Convert mode Renewal ditolak bila predecessor sudah punya successor

8. Ganti isi kotak search dengan `Toko Prima Sentosa`, tekan Enter, klik ikon `⋯` pada baris trial `SUBS-20260810-00005` lalu pilih `Convert`
9. Pilih Plan `Professional`, isi Duration `1`, klik `[Submit]` lalu klik `[Convert]`
10. Verifikasi dialog blok Title "Cannot Renew Subscription" dengan teks "You already have a renewal request pending for this subscription. Cancel or wait until it's resolved before submitting another."
11. Verifikasi tombol tunggal `[OK]`
12. Klik `[OK]`
13. Verifikasi trial `SUBS-20260810-00005` tetap Active dan tidak ada term baru

## Notes

- TC-AC-CS-252 dan TC-AC-CS-253 adalah kasus penolakan Convert pada Client Principal; TC Convert lain ada di spec 063 sampai 067.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16); `✕` menutup form Convert bersih tanpa dialog.
- Temuan untuk QA: (1) TC-AC-CS-252 butir c ("Predecessor adalah term paid plan Free, bukan baris trial") hanya teramati setelah Convert dikonfirmasi; TC tidak punya langkah itu sehingga tidak diasersi. (2) TC-AC-CS-253 tidak menyebut Plan yang dipilih; spec memakai Plan `Professional`.
