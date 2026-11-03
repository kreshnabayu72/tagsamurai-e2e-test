---
id: TC-AC-LA-E2E-056-edit-dirty-guard-dan-penyesuaian-type-target
title: "Edit Allocation: Dirty-Guard, Cancel D-02, Reset Type Saat Ganti Target, dan Asset Control App"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-209
  - TC-AC-LA-486
  - TC-AC-LA-194
  - TC-AC-LA-195
coverage:
  web: automated
---

# Edit Allocation: Dirty-Guard, Cancel D-02, Reset Type Saat Ganti Target, dan Asset Control App

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Dewi Anggraini (Pre-setup #4, Distributor PT Maju Bersama, Manage allocation Create+Read+Update); halaman dibuka hook `beforeEach` suite (tab Current).
- Akun: `dewiFullLic_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19), CV Mitra Sejati (Pre-setup #22), dua seed `Waiting for Approval` milik Dewi Anggraini bentuk Pre-setup #41 dan #44 (lihat Data Dinamis).
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`): (a) alokasi `Waiting for Approval` Concurrent User +5 ke Subscription `SUBS-20260101-A1B2C` PT Sejahtera (Allocation ID `{allocIdCU}`); (b) alokasi `Waiting for Approval` Asset Control App milik Dewi Anggraini pada CV Mitra Sejati (Allocation ID `{allocIdApp}`), pada Subscription yang belum punya Asset Control App Active atau Pending.
- Kemampuan teknis: seeding alokasi lewat API/fixture backend dan pembersihan record seed di hook `after` (disediakan tim FE/BE).
- State global: tidak ada yang diubah. Semua form dirty ditutup lewat langkah eksplisit; hook `beforeEach` suite menjadi jaring pengaman (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Dirty-guard Form Edit

1. Ketik Search `{allocIdCU}`, tekan Enter
2. Klik row action `Edit` pada baris milik sendiri berstatus `Waiting for Approval`
3. Ubah Additional Quantity dari `5` menjadi `6`
4. Klik area backdrop
5. Verifikasi klik backdrop diabaikan: tidak ada dialog dan Form Edit tetap terbuka
6. Tekan `Esc`
7. Verifikasi dialog D-02 dengan Title `Unsaved Changes`, Body `You have unsaved changes. Are you sure you want to leave?`, serta tombol `[Leave]` dan `[Cancel]`
8. Klik `[Cancel]`
9. Verifikasi dialog tertutup dan Form Edit tetap terbuka dengan Additional Quantity `6` utuh
10. Verifikasi `[Save]` Enabled
11. Tekan `Esc`
12. Klik `[Leave]`
13. Verifikasi Form Edit tertutup tanpa menyimpan
14. Klik row action `Edit` pada baris yang sama
15. Verifikasi Additional Quantity `5` (data tersimpan tetap Quantity `5`)

### Ganti Target me-reset Type

16. Ganti Target ke `Client-wide`
17. Verifikasi Type di-reset (kosong) karena Concurrent User tidak berlaku untuk Client-wide
18. Verifikasi opsi Type hanya `Asset Control Station` dan `Storage`
19. Verifikasi `[Save]` Disabled (Type belum diisi)
20. Klik `[✕]`
21. Verifikasi dialog `Unsaved Changes` dengan isi `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
22. Klik `[Leave]`

### Edit Asset Control App

23. Ganti isi kotak search dengan `{allocIdApp}`, tekan Enter
24. Klik row action `Edit` pada baris Asset Control App milik sendiri
25. Verifikasi Client `CV Mitra Sejati` read-only dan hanya Target dan Type dapat diubah
26. Verifikasi field Additional Quantity tidak tampil
27. Klik `[✕]`

## Notes

- Langkah penghubung (S-03, R-16): langkah 1 dan 23 (Search untuk menemukan baris seed), langkah 11 sampai 13 (menutup form dirty memakai `Esc` dan `[Leave]` seperti TC-AC-LA-209), langkah 14 dan 15 (membuka ulang form untuk mengamati data tersimpan, Expected c TC-AC-LA-486), langkah 20 sampai 22 (menutup form dirty sesuai S-08), langkah 27 (menutup form pristine).
- Satu `Verifikasi` dialog D-02 pada langkah 7 memenuhi TC-AC-LA-209 butir b dan TC-AC-LA-486 butir a (dialog dan isinya sama). TC-AC-LA-209 butir c ada di langkah 13.
- Pemetaan Expected: TC-AC-LA-486 butir b di langkah 9, butir c di langkah 10 dan 15; TC-AC-LA-194 butir a, b, c di langkah 17, 18, 19; TC-AC-LA-195 butir a, b di langkah 25, 26.
- Temuan untuk QA:
  - TC-AC-LA-194 butir c ("`[Save]` Disabled sampai Type diisi") tidak menyebut nilai Type dan Quantity yang dipilih setelahnya; spec hanya mengasersi `[Save]` Disabled sebelum Type diisi dan tidak mengasersi bagian "sampai Type diisi".
  - TC-AC-LA-195 memakai Pre-setup #44 (dua alokasi App ke `SUBS-20260105-K2L3M`) sedangkan Pre-setup #53 menyatakan Subscription yang sama sudah punya Asset Control App Active; spec memakai seed App milik spec pada Subscription tanpa App Active atau Pending.
  - TC-AC-LA-195 tidak menyebut apakah form Edit Asset Control App pristine saat ditutup; spec menutup form tanpa perubahan lewat `[✕]` tanpa dialog.
