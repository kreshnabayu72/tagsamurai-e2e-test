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
- State global: tidak ada yang diubah. Record seed dibersihkan di hook `after`; tidak ada form dirty yang tersisa (langkah 17 sampai 19 menutup form dirty, langkah 22 menutup form pristine).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Screening Form Edit

1. Ketik Search `{allocId}`, tekan Enter
2. Klik row action `Edit` pada baris milik sendiri berstatus `Waiting for Approval`
3. Verifikasi header modal berjudul `Edit Allocation` dengan tombol silang `[✕]`
4. Verifikasi Client `PT Sejahtera` read-only (terkunci)
5. Verifikasi Target dan Type pre-filled dan dapat diubah, serta Additional Quantity `5` pre-filled
6. Verifikasi section Payment menampilkan Pay From read-only, Cost snapshot, dan selisih terhadap Reserve sebelumnya
7. Verifikasi footer menampilkan `[Clear Field]` dan `[Save]` rata kanan
8. Verifikasi `[Save]` Disabled saat form pertama dibuka (sampai ada perubahan)

### Save Disabled sampai ada perubahan

9. Ubah Additional Quantity dari `5` menjadi `6`
10. Verifikasi `[Save]` Enabled saat Quantity `6`
11. Ubah Additional Quantity kembali menjadi `5`
12. Verifikasi `[Save]` kembali Disabled saat Quantity kembali `5` (tanpa perubahan)

### Clear Field pada Form Edit

13. Klik `[Clear Field]`
14. Verifikasi Target, Type, dan Additional Quantity kosong
15. Verifikasi Client `PT Sejahtera` tetap read-only
16. Verifikasi form tetap terbuka tanpa dialog
17. Klik `[✕]`
18. Verifikasi dialog `Unsaved Changes` dengan isi `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
19. Klik `[Leave]`
20. Klik row action `Edit` pada baris yang sama
21. Verifikasi Target dan Type pre-filled dengan nilai tersimpan dan Additional Quantity `5` (nilai tersimpan tidak berubah di server)
22. Klik `[✕]`

## Notes

- Langkah penghubung (S-03, R-16): langkah 1 (Search untuk menemukan baris seed), langkah 17 sampai 19 (menutup form dirty sesuai S-08), langkah 20 dan 22 (membuka ulang form untuk mengamati nilai tersimpan dan menutupnya tanpa perubahan).
- Satu `Verifikasi` pada langkah 8 memenuhi dua Expected sekaligus: TC-AC-LA-188 butir c (`[Save]` Disabled sampai ada perubahan) dan TC-AC-LA-189 butir a (`[Save]` Disabled saat pertama dibuka); keduanya menyatakan keadaan yang sama pada pembukaan form yang sama.
- Urutan langkah mengikuti state form (S-10): screening, perubahan Quantity bolak-balik sampai pristine, Clear Field sebagai aksi terakhir yang membuat form dirty, lalu penutupan.
- Validasi field Form Edit (Type, Target, Additional Quantity) ada di spec 070.
- Temuan untuk QA:
  - TC-AC-LA-210 butir b ("nilai tersimpan tidak berubah di server") tidak punya langkah observasi di LK. Spec mengamatinya lewat membuka ulang Form Edit (langkah 20 dan 21) sebagai langkah penghubung.
  - TC-AC-LA-188 menyebut "Amati Zona 1, 2, dan 3 modal" dan butir Expected Cost snapshot serta selisih Reserve tanpa nilai; spec hanya mengasersi keberadaan elemen Payment, bukan nominal.
  - TC-AC-LA-188 dan TC-AC-LA-189 tidak menyebut Allocation ID atau cara menemukan baris di List yang berisi banyak alokasi seed; spec memakai Search atas Allocation ID record seed milik spec.
