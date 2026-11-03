---
id: TC-AC-CS-E2E-028-form-add-opsi-dropdown-client-dan-product
title: "Form Add: Opsi Dropdown Client dan Product"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-107
  - TC-AC-CS-108
  - TC-AC-CS-111
coverage:
  web: automated
---

# Form Add: Opsi Dropdown Client dan Product

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Data Pre-setup yang dibaca (hanya dropdown dibuka, tidak ada Submit): Client `PT Sejahtera` (Pre-setup #38; FAMS punya term Active, SAMS dan SIEM kosong), Client `PT Bintang Timur` (Pre-setup #37; FAMS punya trial Waiting for Approval `SUBS-20260819-00004` tanpa term paid, SAMS dan SIEM kosong; Pre-setup #59), Client `Apotek Sehat Sentosa` (Pre-setup #29). Tidak diubah.
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`): Client `Client Tanpa Subscription+{runId}-028` (padanan Pre-setup #48: tanpa term dan tanpa trial) dan Client `Client Penuh+{runId}-028` yang ketiga Product-nya (FAMS, SAMS, SIEM) sudah punya term live di tab Current.
- Kata kunci pencarian dropdown: `SEHAT` dan `zzzz` (TC-AC-CS-111).

## Test Steps

### TC-AC-CS-107: Opsi Client varian Add hanya Client yang masih punya Product tanpa baris di tab Current

1. Klik `[+ Subscription]`
2. Buka dropdown Client
3. Ketik `Sejahtera` pada kotak pencarian dropdown
4. Verifikasi opsi `PT Sejahtera` ada karena SAMS dan SIEM belum punya baris Current
5. Ganti isi kotak pencarian dropdown dengan `Client Tanpa Subscription+{runId}-028`
6. Verifikasi opsi `Client Tanpa Subscription+{runId}-028` ada
7. Ganti isi kotak pencarian dropdown dengan `Client Penuh+{runId}-028`
8. Verifikasi opsi `Client Penuh+{runId}-028` tidak ada di dropdown karena semua Product-nya sudah punya term live atau baris Trial di tab Current
9. Ganti isi kotak pencarian dropdown dengan `Bintang Timur`
10. Verifikasi opsi `PT Bintang Timur` ada karena SAMS dan SIEM belum punya baris Current
11. Pilih Client `PT Bintang Timur`, lalu buka dropdown Product
12. Verifikasi dropdown Product memuat `SAMS` dan `SIEM`
13. Verifikasi `FAMS` tidak ada di dropdown Product karena ada baris Trial Waiting for Approval di tab `Current`

### TC-AC-CS-108: Opsi Product mengikuti Client terpilih

14. Tekan `Esc` untuk menutup dropdown Product, lalu klik `[Clear Field]`
15. Pilih Client `PT Sejahtera`, lalu buka dropdown Product
16. Verifikasi dropdown Product memuat `SAMS` dan `SIEM`
17. Verifikasi `FAMS` tidak ada di dropdown Product karena sudah punya term live

### TC-AC-CS-111: Pencarian di dalam dropdown Client memakai substring tanpa membedakan huruf besar kecil

18. Tekan `Esc` untuk menutup dropdown Product, lalu klik `[Clear Field]`
19. Buka dropdown Client
20. Ketik `SEHAT` pada kotak pencarian dropdown
21. Verifikasi opsi `Apotek Sehat Sentosa` muncul untuk `SEHAT`
22. Verifikasi opsi Client lain tidak muncul untuk `SEHAT`
23. Ganti isi kotak pencarian dropdown dengan `zzzz`
24. Verifikasi dropdown menampilkan teks "No results found" tanpa opsi
25. Tekan `Esc` untuk menutup dropdown, lalu klik `[✕]` pada header modal

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Form dibuka sekali untuk ketiga TC (kasus tanpa Submit memakai satu pembukaan dengan field dikosongkan di antara kasus).
- Langkah penghubung (S-03): `[Clear Field]` dan `Esc` untuk mengosongkan form dan menutup dropdown (langkah 14, 18); ketik kata kunci pada kotak pencarian dropdown untuk menemukan opsi (langkah 3, 5, 7, 9); `[✕]` pada form bersih (langkah 25).
- Anchor absence (butir 8b.2): langkah 6 (opsi seed lain tampil) mendahului langkah 8; langkah 12 (opsi `SAMS` dan `SIEM` tampil) mendahului langkah 13; langkah 16 mendahului langkah 17; langkah 21 mendahului langkah 22.
- Temuan untuk QA:
  - TC-AC-CS-107 Expected c menyebut "Client yang semua Product-nya sudah punya term live atau baris Trial di tab Current tidak ada di dropdown" tanpa menamai Client dan tanpa Pre-setup; spec memakai seed `Client Penuh+{runId}-028` dengan tiga term live.
  - TC-AC-CS-107 Precondition menyebut `Client Tanpa Subscription` sebagai Client yang ada di dropdown sementara TC-AC-CS-108 hanya bergantung pada `PT Sejahtera`; spec memakai seed bersuffix untuk `Client Tanpa Subscription` karena data Pre-setup #48 dipakai destruktif oleh banyak TC lain.
