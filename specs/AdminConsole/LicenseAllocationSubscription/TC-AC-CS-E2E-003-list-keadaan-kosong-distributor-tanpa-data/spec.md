---
id: TC-AC-CS-E2E-003-list-keadaan-kosong-distributor-tanpa-data
title: "List: Keadaan Kosong Distributor Tanpa Data"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-5
  - TC-AC-CS-6
  - TC-AC-CS-581
  - TC-AC-CS-347
  - TC-AC-CS-400
coverage:
  web: automated
---

# List: Keadaan Kosong Distributor Tanpa Data

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `totalControlEmptySub_automated_{namaCompany}@qwertysystem.net` (`Kartika Dewi`, Total Control, Distributor PT Kosong; Pre-setup #91), password `Spectra.env.AC_SUB_EMPTY_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Data: scope Distributor PT Kosong tanpa baris di tab Current maupun tab History dan tanpa entri Changelog (Pre-setup #91); spec tidak menulis data.
- Akun #91 sudah berflag Guided Tooltip `seen` (true); walkthrough diputar manual lewat tombol `[?]` dan tidak mengubah flag.

## Test Steps

### TC-AC-CS-5: Empty state tab Current saat tidak ada baris

1. Verifikasi Illustration tampil
2. Verifikasi Title "No current subscriptions"
3. Verifikasi Description "Subscriptions that are running or waiting for a decision will appear here. Finished ones are in History."
4. Verifikasi tidak ada tombol `[Try Again]`

### TC-AC-CS-581: Toolbar tetap tampil saat tabel kosong (bagian tab Current)

5. Verifikasi pada tab `Current` kosong Toolbar tampil rata kanan di atas area tabel dengan isi `Search | Filter | Download | Changelog | [+ Subscription] | [+ Activate Trial]`
6. Verifikasi EmptyState hanya menggantikan area tabel

### TC-AC-CS-400: Empty state Modal Changelog belum ada entri

7. Klik ikon Changelog di toolbar
8. Verifikasi Illustration, Title "No changelog yet", dan Description "Activities and changes will appear here." tampil
9. Verifikasi tidak ada tombol `[Try Again]`
10. Tutup modal Changelog lewat `✕`

### TC-AC-CS-6: Empty state tab History saat tidak ada baris

11. Klik tab `History`
12. Verifikasi Illustration tampil
13. Verifikasi Title "No subscription history yet"
14. Verifikasi Description "Renewed, canceled, rejected, and archived subscriptions will appear here."

### TC-AC-CS-581: Toolbar tetap tampil saat tabel kosong (bagian tab History)

15. Verifikasi pada tab `History` kosong Toolbar tampil rata kanan dengan isi `Search | Filter | Download`
16. Verifikasi ikon Changelog, `[+ Subscription]`, dan `[+ Activate Trial]` tidak dirender

### TC-AC-CS-347: Dropdown filter tanpa data sumber menampilkan No options available

17. Klik ikon Filter di toolbar
18. Buka dropdown Client
19. Verifikasi dropdown menampilkan teks "No options available"
20. Verifikasi tidak ada error
21. Tutup Filter Panel
22. Klik tab `Current`

### TC-AC-CS-581: Toolbar tetap tampil saat tabel kosong (bagian Guided Tooltip)

23. Klik tombol `[?]` (Show guide) lalu klik `[Next]` ke Step 2
24. Verifikasi Step 2 Guided Tooltip menyorot Toolbar dengan Title "Controls for the Whole List"
25. Klik `[Skip]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- TC-AC-CS-581 terbagi tiga bagian menurut keadaan layar (tab `Current` kosong, tab `History` kosong, Guided Tooltip Step 2) dan ditulis berurutan mengikuti keadaan. Urutan TC: 5, 581 (Current), 400, 6, 581 (History), 347, 581 (Guided Tooltip); alasannya meminimalkan pindah tab (S-10).
- Langkah penghubung (S-03): tutup modal Changelog, tutup Filter Panel, klik tab `Current`, dan `[Skip]` Guided Tooltip.
- Temuan untuk QA:
  - TC-AC-CS-347 menulis Precondition "Tab History tanpa baris" dan LK "Klik tab History lalu Klik ikon Filter"; spec membuka Filter pada tab `History` sesuai LK.
  - TC-AC-CS-581 Expected a menyebut "(S-02)" dan Expected b "(S-07)" tanpa penjelasan rujukan; spec hanya mengasersi teks Expected.
