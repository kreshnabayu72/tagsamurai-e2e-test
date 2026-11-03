---
id: TC-AC-CS-E2E-097-list-setup-column-overlay-guard-cache-bersama
title: "List Setup Column: Overlay, Guard, dan Cache Bersama"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-376
  - TC-AC-CS-373
  - TC-AC-CS-374
  - TC-AC-CS-375
coverage:
  web: automated
---

# List Setup Column: Overlay, Guard, dan Cache Bersama

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Konfigurasi kolom Setup Column dan overlay Column Visibility yang disimpan spec (List dan Modal Changelog) dipulihkan dengan menghapus preferensi kolom di browser di hook `after` (kemampuan disediakan tim FE); langkah penghubung "Hapus preferensi kolom di browser" memakai kemampuan yang sama.
- Cache Setup Column browser dikosongkan di hook `before` (kemampuan disediakan tim FE); konfigurasi akhir spec dikembalikan ke bawaan oleh langkah penghubung dan hook `after`.

## Test Steps

### TC-AC-CS-376: Overlay Column Visibility menerapkan perubahan langsung tanpa Save

1. Klik ikon `⋯` pada header kolom Actions untuk membuka overlay Column Visibility
2. Hilangkan centang `End Date`
3. Verifikasi kolom End Date langsung hilang dari tabel tanpa tombol Save
4. Seret `Plan` ke atas `Product` pada overlay
5. Verifikasi urutan kolom pada tabel langsung berubah sesuai urutan pada overlay
6. Tekan F5
7. Verifikasi perubahan (End Date tersembunyi dan Plan di atas Product) bertahan setelah F5

### TC-AC-CS-373: Guard kolom visible terakhir tidak dapat di-uncheck

8. Buka overlay Column Visibility lalu hilangkan centang semua kolom kecuali `Client`
9. Arahkan kursor ke checkbox `Client`
10. Verifikasi checkbox `Client` Disabled
11. Verifikasi tooltip "At least one column must remain visible."
12. Centang satu kolom lain (`Plan`)
13. Verifikasi checkbox `Client` kembali Enabled
14. Buka modal Setup Column (`⋯` lalu `[Setup Column]`), klik `[Reset to Default]`, lalu klik `[Save]`
15. Tunggu aksi selesai (modal Setup Column tertutup)

### TC-AC-CS-374: Konfigurasi Setup Column dibagi antara tab Current dan History

16. Buka overlay Column Visibility lalu hilangkan centang `Product` pada tab `Current`
17. Klik tab `History`
18. Verifikasi kolom Product juga tersembunyi pada tab `History`
19. Pada overlay tab `History` seret `Plan` ke atas `Client`
20. Klik tab `Current`
21. Verifikasi urutan Plan di atas Client langsung terlihat pada tab `Current`
22. Buka modal Setup Column pada tab `Current`, klik `[Reset to Default]`, lalu klik `[Save]`
23. Verifikasi tab `Current` memakai konfigurasi bawaan (Product tampil, Plan setelah Product)
24. Klik tab `History`
25. Verifikasi tab `History` memakai konfigurasi bawaan yang sama

### TC-AC-CS-375: Cache Setup Column List tidak memengaruhi tabel Modal Changelog

26. Klik tab `Current` lalu hilangkan centang `Product` pada overlay Column Visibility tabel List
27. Klik ikon Changelog di toolbar
28. Verifikasi modal Changelog tetap menampilkan ketujuh kolomnya (Date, Action, Client — Product, Field, Old Value, New Value, Modified By) tanpa dipengaruhi konfigurasi List
29. Buka overlay Column Visibility pada modal Changelog lalu hilangkan centang `Old Value`
30. Klik `[✕]` untuk menutup modal Changelog
31. Verifikasi kolom tabel List tidak berubah oleh langkah pada modal Changelog (Product tetap tersembunyi; Subscription ID, Client, Plan, Status, Start Date, End Date, dan Plan Owner tampil)
32. Buka modal Setup Column, klik `[Reset to Default]`, lalu klik `[Save]`

## Notes

- TC-AC-CS-371 dan TC-AC-CS-372 dicakup spec lain suite ini.
- Urutan blok TC-AC-CS-376, 373, 374, 375 mengikuti keadaan konfigurasi kolom: perubahan overlay disimpan di browser, sehingga tiap blok diakhiri pemulihan ke bawaan lewat langkah penghubung (S-09).
- Langkah penghubung (S-03): langkah `[Reset to Default]` dan `[Save]` tanpa `Verifikasi` di akhir blok TC-AC-CS-373 dan di akhir spec; klik tab `Current` dan `History`; langkah menutup modal Changelog.
- Langkah penghubung (S-03, bagian 8b butir 8): langkah `Tunggu aksi selesai` (langkah 15) menunggu modal Setup Column tertutup sesudah `[Save]` sebelum langkah berikutnya mengubah permukaan.
- Temuan untuk QA:
  - TC-AC-CS-373 Expected c (menyalakan satu kolom lain mengembalikan checkbox `Client` ke Enabled) tidak punya langkah di Langkah Uji; spec menambah langkah mencentang `Plan` (pilihan spec).
  - TC-AC-CS-374 hanya punya dua langkah, sedangkan Expected b (mengubah urutan di tab `History` terlihat di tab `Current`) dan Expected c (Reset to Default berlaku untuk kedua tab) tidak punya langkah; spec menambah langkah menggeser `Plan` ke atas `Client` di tab `History` dan langkah Reset to Default. Kolom yang digeser tidak dinyatakan TC.
  - TC-AC-CS-375 Expected b (menyembunyikan kolom di modal Changelog tidak memengaruhi kolom List) tidak punya langkah; spec menambah langkah menyembunyikan `Old Value` di modal Changelog (pilihan spec).
  - TC-AC-CS-376 Precondition Cache dikosongkan tidak menyebut cara pengosongan; dikosongkan di hook `before` oleh kemampuan tim FE.
