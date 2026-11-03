---
id: TC-AC-LA-E2E-059-edit-blokir-saldo-dan-app-kedua
title: "Edit Allocation Ditolak karena Kondisi Data: Saldo Tidak Cukup dan Asset Control App Kedua"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-196
  - TC-AC-LA-204
coverage:
  web: automated
---

# Edit Allocation Ditolak karena Kondisi Data: Saldo Tidak Cukup dan Asset Control App Kedua

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Dewi Anggraini (Pre-setup #4, Distributor PT Maju Bersama, Manage allocation Create+Read+Update); halaman dibuka hook `beforeEach` suite (tab Current).
- Akun: `dewiFullLic_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19), CV Mitra Sejati (Pre-setup #22), Product Price Concurrent User $365 per unit per tahun (Pre-setup #34).
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`):
  - `{idSaldo}`: alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, requester Dewi Anggraini, Cost $150.00 di-Reserve (bentuk Pre-setup #41);
  - `{idApp}`: alokasi `Waiting for Approval` Concurrent User +2 ke `SUBS-20260105-K2L3M` CV Mitra Sejati, requester Dewi Anggraini, Cost $60.00 di-Reserve (bentuk Pre-setup #77); Subscription yang sama sudah punya alokasi Asset Control App Active (bentuk Pre-setup #53).
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut endpoint atau halamannya): seeding alokasi dan pembersihannya, fixture saldo untuk menurunkan dan memulihkan saldo Available kantong Distributor PT Maju Bersama, klien HTTP atau fixture BE dengan sesi API Dewi Anggraini untuk request Edit langsung, serta kemampuan membaca state record (Type, Quantity, Reserve).
- State global: saldo Available kantong diturunkan menjadi $10.00 pada langkah 1 dan dipulihkan pada langkah 14 serta di hook `after` sebagai cadangan.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Saldo kantong tidak cukup untuk Reserve baru

1. Turunkan saldo Available kantong Distributor PT Maju Bersama menjadi `$10.00` (fixture saldo)
2. Ketik Search `{idSaldo}`, tekan Enter
3. Klik row action `Edit`
4. Ubah Additional Quantity dari `5` menjadi `100`
5. Klik `[Save]`
6. Verifikasi pesan penolakan server `Insufficient wallet balance.`
7. Klik `[✕]`
8. Verifikasi dialog `Unsaved Changes` dengan isi `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
9. Klik `[Leave]`
10. Verifikasi Cost pada List `{idSaldo}` tetap `$150.00` (Reserve utuh)
11. Klik row action `Edit`
12. Verifikasi Additional Quantity tetap `5`
13. Klik `[✕]`
14. Pulihkan saldo Available kantong Distributor PT Maju Bersama ke nilai awal (fixture saldo)

### Request Edit langsung mengganti Type ke Asset Control App kedua

15. Kirim request Edit langsung (sesi API Dewi Anggraini) untuk `{idApp}` dengan Type `Asset Control App`
16. Verifikasi respons ditolak dengan pesan `Asset Control App is already active for this subscription.`
17. Verifikasi record `{idApp}` tidak berubah: Type tetap `Concurrent User` dan Quantity tetap `2`

## Notes

- K-1: langkah 15 sampai 17 adalah TC defense-in-depth kelas a yang Expected-nya respons API (pesan penolakan dan state data lewat kemampuan baca BE); TC granular tetap sumber dan TC ini tepat satu spec. Sesuai 8b butir 1, hanya respons server dan state data yang diasersi, tanpa asersi tampilan.
- P-5: TC-AC-LA-204 adalah objek-uji ringan kelas a (satu request langsung tanpa harness eksternal) bersama TC-AC-LA-196 pada spec blokir kondisi data Edit; jumlah objek uji ringan tidak melebihi dua.
- Langkah penghubung (S-03, R-16): langkah 2 (Search untuk menemukan baris seed), langkah 7 sampai 9 (menutup form dirty sesuai S-08), langkah 11 sampai 13 (membuka ulang form untuk mengamati nilai tersimpan dan menutupnya), langkah 14 (memulihkan saldo).
- Langkah 11 dan 12 membuka form `Edit` untuk membaca Quantity tersimpan; Reserve utuh diamati lewat Cost pada List (langkah 10).
- Temuan untuk QA:
  - TC-AC-LA-196 butir a tidak menyebut apakah pesan `Insufficient wallet balance.` berupa toast, alert, atau pesan inline; spec mengasersi teks pesan tanpa menyebut bentuknya.
  - TC-AC-LA-196 butir b ("Record tetap Quantity `5` dan Reserve `$150.00`") tidak punya langkah observasi; langkah 10 sampai 12 mengamatinya lewat List dan membuka ulang Form Edit. Reserve kantong tidak dibaca langsung karena TC tidak menyebut cara membacanya.
  - TC-AC-LA-204 langkah 1 menyebut "Klik `Edit` dan ganti Type ... lewat request langsung" sehingga ambigu antara aksi UI dan request langsung; spec mengirim request langsung saja (8b butir 1) dan tidak menyalin aksi UI.
  - TC-AC-LA-204 tidak menyebut cara mengirim request atau endpoint-nya (tidak ada API/LLD modul); kemampuan itu ditulis sebagai disediakan tim FE/BE.
  - Pre-setup #53 menyatakan Subscription `SUBS-20260105-K2L3M` sudah punya Asset Control App Active, sedangkan Pre-setup #44 memakai Subscription yang sama sebagai target dua alokasi App `Waiting for Approval`; TC-AC-LA-204 bergantung pada keadaan #53.
