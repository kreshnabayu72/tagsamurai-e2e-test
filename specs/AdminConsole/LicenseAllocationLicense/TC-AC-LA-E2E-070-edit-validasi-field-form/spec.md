---
id: TC-AC-LA-E2E-070-edit-validasi-field-form
title: "Edit Allocation: Validasi Field Type, Target, dan Additional Quantity"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-205
  - TC-AC-LA-206
  - TC-AC-LA-207
  - TC-AC-LA-208
coverage:
  web: automated
---

# Edit Allocation: Validasi Field Type, Target, dan Additional Quantity

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Dewi Anggraini (Pre-setup #4, Distributor PT Maju Bersama, Manage allocation Create+Read+Update); halaman dibuka hook `beforeEach` suite (tab Current).
- Akun: `dewiFullLic_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19).
- Data Dinamis: satu alokasi `Waiting for Approval` milik Dewi Anggraini (Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, Cost $150.00 di-Reserve) sebagai seed milik spec ini (bentuk Pre-setup #41), dibuat lewat seeding backend di hook `before`; Allocation ID disebut `{allocId}`. Nilai uji: `abc`, `2.5`, `0`, dan 16 digit `1234567890123456` (nilai Data Uji TC), dirujuk lewat `Fixture.license-allocation-license`.
- Kemampuan teknis: seeding alokasi lewat API/fixture backend dan pembersihan record seed di hook `after` (disediakan tim FE/BE).
- State global: tidak ada yang diubah. Semua validasi diblokir sebelum request; record seed dibersihkan di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `{allocId}`, tekan Enter
2. Klik row action `Edit` pada baris milik sendiri berstatus `Waiting for Approval`

### Additional Quantity: non-digit dan lebih dari 15 karakter

3. Kosongkan isi Additional Quantity
4. Ketik `abc` pada Additional Quantity
5. Verifikasi karakter non-digit diblok (Additional Quantity tidak berisi huruf)
6. Ketik `2.5` pada Additional Quantity
7. Verifikasi karakter non-digit diblok (Additional Quantity hanya berisi digit)
8. Kosongkan isi Additional Quantity
9. Ketik 16 digit `1234567890123456` pada Additional Quantity
10. Verifikasi pesan `Max. 15 characters` tampil

### Additional Quantity: kosong dan nol

11. Kosongkan isi Additional Quantity
12. Klik `[Save]`
13. Verifikasi pesan inline `Additional Quantity must not be empty`
14. Isi Additional Quantity `0`
15. Klik `[Save]`
16. Verifikasi pesan inline `Additional Quantity must be greater than 0`

### Type kosong

17. Klik `[Clear Field]`
18. Pilih ulang Target `SUBS-20260101-A1B2C`, biarkan Type kosong
19. Isi Additional Quantity `5`
20. Klik `[Save]`
21. Verifikasi pesan inline `Type must not be empty`

### Target kosong

22. Klik `[Clear Field]`
23. Isi Additional Quantity `5`
24. Klik `[Save]`
25. Verifikasi pesan inline `Target must not be empty`

### Record tidak berubah

26. Klik `[×]`
27. Verifikasi dialog `Unsaved Changes` dengan isi `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
28. Klik `[Leave]`
29. Klik row action `Edit` pada baris yang sama
30. Verifikasi Target dan Type pre-filled dengan nilai tersimpan dan Additional Quantity `5` (record tidak berubah oleh keempat validasi)
31. Klik `[×]`

## Notes

- Langkah penghubung (S-03, R-16): langkah 1 (Search untuk menemukan baris seed), langkah 3, 8, dan 11 (mengosongkan Additional Quantity sebagai pembersih antar kasus, R-12), langkah 17 dan 22 (`[Clear Field]` menghapus pesan error kasus sebelumnya sesuai TC-AC-LA-184), langkah 26 sampai 28 (menutup form dirty sesuai S-08), langkah 29 dan 31 (membuka ulang form untuk mengamati nilai tersimpan dan menutupnya).
- Urutan kasus (208, 207, 205, 206) mengikuti state form: dua kasus pertama memerlukan Target dan Type masih terisi, dua kasus terakhir memerlukan `[Clear Field]`.
- Temuan untuk QA:
  - TC-AC-LA-208 butir a ("hanya digit masuk") tidak menyebut isi field setelah mengetik `2.5`; spec mengasersi bahwa field hanya berisi digit.
  - TC-AC-LA-205, 206, 207 butir "Record tidak berubah" tidak punya langkah observasi di LK; spec mengamatinya sekali lewat membuka ulang Form Edit (langkah 29 dan 30) sebagai langkah penghubung.
  - TC-AC-LA-206: `[Clear Field]` juga mengosongkan Type, sehingga pesan `Type must not be empty` mungkin tampil bersama `Target must not be empty`; TC hanya menyebut pesan Target, spec hanya mengasersi pesan Target.
  - TC-AC-LA-205 menyebut "kosongkan Type lewat `[Clear Field]`" padahal `[Clear Field]` mengosongkan Target, Type, dan Quantity sekaligus (TC-AC-LA-210); spec memilih ulang Target dan mengisi Quantity `5` sesuai langkah TC.
