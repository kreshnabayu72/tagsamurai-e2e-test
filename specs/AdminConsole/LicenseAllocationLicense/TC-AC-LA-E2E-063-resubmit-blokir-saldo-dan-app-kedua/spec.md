---
id: TC-AC-LA-E2E-063-resubmit-blokir-saldo-dan-app-kedua
title: "Resubmit Ditolak karena Kondisi Data: Saldo Kurang dan Asset Control App Kedua"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-521
  - TC-AC-LA-522
coverage:
  web: automated
---

# Resubmit Ditolak karena Kondisi Data: Saldo Kurang dan Asset Control App Kedua

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Dewi Anggraini (Pre-setup #4, Distributor PT Maju Bersama, Manage allocation Create+Read+Update); halaman dibuka hook `beforeEach` suite (tab Current).
- Akun: `dewiFullLic_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19), CV Mitra Sejati (Pre-setup #22), Product Price Concurrent User $365 per unit per tahun (Pre-setup #34), kantong wallet Distributor PT Maju Bersama (Pre-setup #33).
- Konfigurasi: Require Approval for Allocation ON (Pre-setup #38), dipastikan di hook `before` oleh fixture backend (disediakan tim FE/BE) dan dipulihkan di hook `after`.
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`; tidak memakai baris Pre-setup #48 dan #66 bersama):
  - `{idSaldo}`: alokasi `Canceled` manual Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, requester Dewi Anggraini (bentuk Pre-setup #48);
  - `{idApp}`: alokasi `Canceled` manual Asset Control App ke `SUBS-20260105-K2L3M` CV Mitra Sejati, requester Dewi Anggraini (bentuk Pre-setup #66); Subscription yang sama sudah punya Asset Control App Active.
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut endpoint atau halamannya): seeding alokasi dan pembersihannya, fixture waktu (jam server dan jam browser ke tanggal acuan 22 Dec 2026), fixture saldo (menurunkan saldo Available kantong Distributor PT Maju Bersama menjadi $20.00 dan memulihkannya), serta kemampuan membaca state BE (jumlah record yang menunjuk record asal).
- State global: jam server dan jam browser diatur ke 22 Dec 2026 pada langkah 1 dan dipulihkan pada langkah 9; saldo Available diturunkan pada langkah 2 dan dipulihkan pada langkah 9; hook `after` memulihkan keduanya sebagai cadangan.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Saldo kantong kurang dari Cost

1. Atur jam server dan jam browser ke 22 Dec 2026 (fixture waktu)
2. Turunkan saldo Available kantong Distributor PT Maju Bersama menjadi `$20.00` (fixture saldo)
3. Klik tab `History`
4. Ketik Search `{idSaldo}`, tekan Enter
5. Klik row action `Resubmit` pada baris Canceled milik sendiri
6. Verifikasi baris Cost `Cost: $50.00 (5 × $365/unit × 10 days remaining ÷ 365)`
7. Verifikasi Alert severity danger `Insufficient balance in your pocket. Available: $20.00. Required: $50.00.`
8. Verifikasi tombol `[Submit]` disabled
9. Pulihkan saldo Available kantong serta jam server dan jam browser ke nilai awal
10. Klik `[✕]`
11. Verifikasi record asal `{idSaldo}` tetap berstatus `Canceled`
12. Verifikasi tidak ada record baru yang menunjuk `{idSaldo}`

### Asset Control App kedua pada Subscription yang sudah punya App Active

13. Ganti isi kotak search dengan `{idApp}`, tekan Enter
14. Klik row action `Resubmit` pada baris Canceled Asset Control App milik sendiri
15. Klik `[Submit]`
16. Verifikasi pesan `Asset Control App is already active for this subscription.`
17. Verifikasi form tetap terbuka dengan Client `CV Mitra Sejati` dipertahankan
18. Klik `[✕]`
19. Verifikasi record asal `{idApp}` tetap berstatus `Canceled`
20. Verifikasi tidak ada record baru yang menunjuk `{idApp}`

## Notes

- Langkah penghubung (S-03, R-16): langkah 1, 2, dan 9 (mengatur dan memulihkan jam serta saldo), langkah 3 (pindah tab), langkah 4 dan 13 (Search untuk menemukan baris seed), langkah 10 dan 18 (menutup form Resubmit).
- Langkah 9 memulihkan saldo dan jam sebelum asersi record asal supaya state global tidak terbawa ke langkah berikutnya (S-09).
- Temuan untuk QA:
  - TC-AC-LA-521 dan TC-AC-LA-522 butir "tidak ada record baru dan record asal tetap Canceled" tidak punya langkah observasi di LK; spec memakai Status baris di List dan kemampuan baca state BE (jumlah record yang menunjuk record asal) tanpa endpoint karangan.
  - TC-AC-LA-522 butir a ("field lain dipertahankan") tidak menyebut field mana yang dipertahankan atau dikosongkan (TC-AC-LA-202 dan 203 menyebut Target dikosongkan); spec hanya mengasersi Client `CV Mitra Sejati` tetap terisi.
  - TC-AC-LA-522 tidak menyebut apakah form Resubmit dalam keadaan dirty sesudah penolakan; spec menutup form lewat `[✕]` tanpa dialog (tidak ada perubahan oleh pengguna).
  - Pre-setup #53 menyatakan Subscription `SUBS-20260105-K2L3M` sudah punya Asset Control App Active, sedangkan Pre-setup #44 memakai Subscription yang sama sebagai target dua alokasi App `Waiting for Approval`; TC-AC-LA-522 bergantung pada keadaan #53.
  - TC-AC-LA-521 Data Uji menyebut Cost `$50.00` dengan 10 hari tersisa pada tanggal acuan 22 Dec 2026 dan End Date 31 Dec 2026 (kedua tanggal dihitung); konsisten dengan TC, dicatat sebagai asumsi.
