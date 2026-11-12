---
id: TC-AC-LA-E2E-055-edit-screening-save-disabled-dan-clear-field
title: "Edit Allocation: Screening Popup Edit, Save Disabled, dan Clear Field"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-188
  - TC-AC-LA-189
  - TC-AC-LA-210
coverage:
  web: automated
---

# Edit Allocation: Screening Popup Edit, Save Disabled, dan Clear Field

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Dewi Anggraini (Pre-setup #4, Distributor PT Maju Bersama, Manage allocation Create+Read+Update); halaman dibuka hook `beforeEach` suite (tab Current). Spec ini tidak mengubah flag Guided Tooltip; hook suite `before` dan `after` yang menanganinya.
- Akun: `dewiFullLic_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19), kantong wallet (Pre-setup #33), Product Price (Pre-setup #34).
- Data Dinamis: satu alokasi `Waiting for Approval` milik Dewi Anggraini (Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, Cost $150.00 di-Reserve) sebagai seed milik spec ini (bentuk Pre-setup #41), dibuat lewat seeding backend di hook `before`. Allocation ID dikembalikan oleh seeding dan disebut `{allocId}` pada langkah.
- Kemampuan teknis: seeding alokasi lewat API/fixture backend dan pembersihan record seed di hook `after` (disediakan tim FE/BE; TC dan PRD tidak menyebut endpoint).
- State global: tidak ada yang diubah. Record seed dibersihkan di hook `after`; tidak ada form dirty yang tersisa (langkah 23 sampai 25 menutup form dirty, langkah 29 menutup form pristine).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Screening Form Edit

1. Ketik Search `{allocId}`, tekan Enter
2. Klik row action `Edit` pada baris milik sendiri berstatus `Waiting for Approval`
3. Verifikasi header modal berjudul `Edit Allocation` dengan tombol silang `[×]`
4. Verifikasi Client `PT Sejahtera` read-only (terkunci)
5. Verifikasi Target pre-filled dan dapat diubah
6. Verifikasi Type pre-filled dan dapat diubah
7. Verifikasi Additional Quantity `5` pre-filled
8. Verifikasi section Payment menampilkan Pay From read-only
9. Verifikasi section Payment menampilkan Cost snapshot
10. Verifikasi section Payment menampilkan selisih terhadap Reserve sebelumnya
11. Verifikasi footer menampilkan `[Clear Field]` dan `[Save]` rata kanan
12. Verifikasi `[Save]` Disabled saat form pertama dibuka (sampai ada perubahan)

### Save Disabled sampai ada perubahan

13. Ubah Additional Quantity dari `5` menjadi `6`
14. Verifikasi `[Save]` Enabled saat Quantity `6`
15. Ubah Additional Quantity kembali menjadi `5`
16. Verifikasi `[Save]` kembali Disabled saat Quantity kembali `5` (tanpa perubahan)

### Clear Field pada Form Edit

17. Klik `[Clear Field]`
18. Verifikasi Target kosong
19. Verifikasi Type kosong
20. Verifikasi Additional Quantity kosong
21. Verifikasi Client `PT Sejahtera` tetap read-only
22. Verifikasi form tetap terbuka tanpa dialog
23. Klik `[×]`
24. Verifikasi dialog `Unsaved Changes` dengan isi `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
25. Klik `[Leave]`
26. Klik row action `Edit` pada baris yang sama
27. Verifikasi Target dan Type pre-filled dengan nilai tersimpan
28. Verifikasi Additional Quantity `5` (nilai tersimpan tidak berubah di server)
29. Klik `[×]`

## Notes

- Langkah penghubung (S-03, R-16): langkah 1 (Search untuk menemukan baris seed), langkah 23 sampai 25 (menutup form dirty sesuai S-08), langkah 26 dan 29 (membuka ulang form untuk mengamati nilai tersimpan dan menutupnya tanpa perubahan).
- Satu `Verifikasi` pada langkah 12 memenuhi dua Expected sekaligus: TC-AC-LA-188 butir c (`[Save]` Disabled sampai ada perubahan) dan TC-AC-LA-189 butir a (`[Save]` Disabled saat pertama dibuka); keduanya menyatakan keadaan yang sama pada pembukaan form yang sama.
- Urutan langkah mengikuti state form (S-10): screening, perubahan Quantity bolak-balik sampai pristine, Clear Field sebagai aksi terakhir yang membuat form dirty, lalu penutupan.
- Validasi field Form Edit (Type, Target, Additional Quantity) ada di spec 070.
- Temuan untuk QA:
  - TC-AC-LA-210 butir b ("nilai tersimpan tidak berubah di server") tidak punya langkah observasi di LK. Spec mengamatinya lewat membuka ulang Form Edit (langkah 26 dan 27) sebagai langkah penghubung.
  - TC-AC-LA-188 menyebut "Amati Zona 1, 2, dan 3 modal" dan butir Expected Cost snapshot serta selisih Reserve tanpa nilai; spec hanya mengasersi keberadaan elemen Payment, bukan nominal.
  - TC-AC-LA-188 dan TC-AC-LA-189 tidak menyebut Allocation ID atau cara menemukan baris di List yang berisi banyak alokasi seed; spec memakai Search atas Allocation ID record seed milik spec.
