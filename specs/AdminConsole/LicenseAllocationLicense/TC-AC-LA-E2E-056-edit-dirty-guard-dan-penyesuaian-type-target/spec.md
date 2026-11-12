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
5. Verifikasi Form Edit tetap terbuka
6. Verifikasi klik backdrop diabaikan: tidak ada dialog
7. Tekan `Esc`
8. Verifikasi dialog D-02 dengan Title `Unsaved Changes`, Body `You have unsaved changes. Are you sure you want to leave?`, serta tombol `[Leave]` dan `[Cancel]`
9. Klik `[Cancel]`
10. Verifikasi dialog tertutup
11. Verifikasi Form Edit tetap terbuka dengan Additional Quantity `6` utuh
12. Verifikasi `[Save]` Enabled
13. Tekan `Esc`
14. Klik `[Leave]`
15. Verifikasi Form Edit tertutup tanpa menyimpan
16. Klik row action `Edit` pada baris yang sama
17. Verifikasi Additional Quantity `5` (data tersimpan tetap Quantity `5`)

### Ganti Target me-reset Type

18. Ganti Target ke `Client-wide`
19. Verifikasi Type di-reset (kosong) karena Concurrent User tidak berlaku untuk Client-wide
20. Verifikasi opsi Type hanya `Asset Control Station` dan `Storage`
21. Verifikasi `[Save]` Disabled (Type belum diisi)
22. Klik `[×]`
23. Verifikasi dialog `Unsaved Changes` dengan isi `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
24. Klik `[Leave]`

### Edit Asset Control App

25. Ganti isi kotak search dengan `{allocIdApp}`, tekan Enter
26. Klik row action `Edit` pada baris Asset Control App milik sendiri
27. Verifikasi Client `CV Mitra Sejati` read-only
28. Verifikasi hanya Target dan Type dapat diubah
29. Verifikasi field Additional Quantity tidak tampil
30. Klik `[×]`

## Notes

- Langkah penghubung (S-03, R-16): langkah 1 dan 25 (Search untuk menemukan baris seed), langkah 13 sampai 15 (menutup form dirty memakai `Esc` dan `[Leave]` seperti TC-AC-LA-209), langkah 16 dan 17 (membuka ulang form untuk mengamati data tersimpan, Expected c TC-AC-LA-486), langkah 22 sampai 24 (menutup form dirty sesuai S-08), langkah 30 (menutup form pristine).
- Satu `Verifikasi` dialog D-02 pada langkah 8 memenuhi TC-AC-LA-209 butir b dan TC-AC-LA-486 butir a (dialog dan isinya sama). TC-AC-LA-209 butir c ada di langkah 15.
- Pemetaan Expected: TC-AC-LA-486 butir b di langkah 10, butir c di langkah 12 dan 17; TC-AC-LA-194 butir a, b, c di langkah 19, 20, 21; TC-AC-LA-195 butir a, b di langkah 27, 29.
- Temuan untuk QA:
  - TC-AC-LA-194 butir c ("`[Save]` Disabled sampai Type diisi") tidak menyebut nilai Type dan Quantity yang dipilih setelahnya; spec hanya mengasersi `[Save]` Disabled sebelum Type diisi dan tidak mengasersi bagian "sampai Type diisi".
  - TC-AC-LA-195 memakai Pre-setup #44 (dua alokasi App ke `SUBS-20260105-K2L3M`) sedangkan Pre-setup #53 menyatakan Subscription yang sama sudah punya Asset Control App Active; spec memakai seed App milik spec pada Subscription tanpa App Active atau Pending.
  - TC-AC-LA-195 tidak menyebut apakah form Edit Asset Control App pristine saat ditutup; spec menutup form tanpa perubahan lewat `[×]` tanpa dialog.
