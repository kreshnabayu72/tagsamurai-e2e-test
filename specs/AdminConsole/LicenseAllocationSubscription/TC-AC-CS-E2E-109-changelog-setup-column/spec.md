---
id: TC-AC-CS-E2E-109-changelog-setup-column
title: "Changelog: Setup Column"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-422
  - TC-AC-CS-423
  - TC-AC-CS-424
  - TC-AC-CS-425
  - TC-AC-CS-426
  - TC-AC-CS-427
coverage:
  web: automated
---

# Changelog: Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Data seed Pre-setup #84 (Changelog Client Subscription berisi 24 entri contoh PRD §4.1.2 dengan Action Edit, Activate, Cancel, Renew, Add Subscription, Resubmit, Timeout Auto-Cancel, Cancel Request, Scheduled Flip Auto-Cancel, Convert, dan Schedule Renewal, Modified By `Fajar N`, `Dewi A`, `Rina P`, `Hendra W`, `Maya T`, `Budi S`, dan `System`) bersifat baca-saja; spec tidak menulis entri Changelog. Changelog adalah audit trail permanen: asersi posisi atau urutan memakai entri seed #84 pada keadaan yang dipulihkan baseline automation sebelum tiap spec (Catatan TC; S-14).
- Changelog, Activity Log, dan System Log adalah audit trail permanen: spec ini tidak menulis entri dan tidak mengasersi total entri sebagai angka absolut (S-12).
- Konfigurasi kolom Setup Column dan overlay Column Visibility yang disimpan spec (List dan Modal Changelog) dipulihkan dengan menghapus preferensi kolom di browser di hook `after` (kemampuan disediakan tim FE); langkah penghubung "Hapus preferensi kolom di browser" memakai kemampuan yang sama.
- Cache Setup Column browser dikosongkan di hook `before` (kemampuan disediakan tim FE). Viewport dipersempit di hook `before` supaya tabel Changelog dapat digulir horizontal (TC-AC-CS-425); viewport dipulihkan di hook `after`.

## Test Steps

1. Klik ikon Changelog di toolbar

### TC-AC-CS-422: Screening overlay Column Visibility Modal Changelog

2. Klik header kolom Actions `⋯` pada tabel modal
3. Verifikasi item "Setup Column..." di bagian bawah panel
4. Verifikasi tujuh kolom tercentang dan enabled: Date, Action, Client — Product, Field, Old Value, New Value, Modified By
5. Verifikasi setiap baris punya drag handle

### TC-AC-CS-423: Screening modal Setup Column untuk tabel Changelog

6. Klik item `[Setup Column]` pada overlay
7. Verifikasi title "Setup Column", deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.", dan tombol silang tampil
8. Verifikasi tujuh kolom Hideable tercentang
9. Verifikasi Live Preview sesuai tabel
10. Verifikasi footer `[Reset to Default]` dan `[Save]` tampil tanpa `[Cancel]`
11. Klik `[✕]` untuk menutup modal Setup Column

### TC-AC-CS-427: Guard kolom Changelog terakhir tidak dapat disembunyikan

12. Buka overlay Column Visibility lalu hilangkan centang semua kolom kecuali `Date`
13. Arahkan kursor ke checkbox `Date`
14. Verifikasi checkbox `Date` Disabled dengan tooltip "At least one column must remain visible."
15. Centang kembali semua kolom pada overlay

### TC-AC-CS-424: Hide dan unhide kolom Changelog lalu Save

16. Buka modal Setup Column lalu hilangkan centang `Old Value` dan `New Value`
17. Klik `[Save]`
18. Verifikasi tabel Changelog menyembunyikan kolom Old Value dan New Value
19. Tekan F5 lalu buka lagi modal Changelog
20. Verifikasi konfigurasi bertahan setelah F5 (Old Value dan New Value tetap tersembunyi)

### TC-AC-CS-425: Geser dan pin kolom Changelog

21. Buka modal Setup Column lalu seret `Modified By` ke atas dan klik icon Pin pada `Date`
22. Klik `[Save]`
23. Verifikasi `Modified By` menjadi kolom pertama dan urutan bertahan
24. Gulir tabel ke kanan
25. Verifikasi kolom Date tetap saat tabel digulir horizontal

### TC-AC-CS-426: Reset to Default dan discard pada Setup Column Changelog

26. Buka modal Setup Column, klik `[Reset to Default]`, lalu klik `[Save]`
27. Verifikasi tujuh kolom kembali ke susunan bawaan
28. Buka modal Setup Column lagi, hilangkan centang `Field`, lalu klik `[✕]`
29. Verifikasi tabel memakai konfigurasi tersimpan (kolom Field tampil)

## Notes

- TC-AC-CS-629 sampai 631 (Setup Column Changelog anggota Hideable lain) dicakup spec lain suite ini.
- Urutan blok: TC-AC-CS-427 sebelum TC-AC-CS-424 karena guard memakai overlay sebelum konfigurasi disimpan, dan TC-AC-CS-426 (Reset dan discard) di akhir sebagai kasus menutup form (bagian 3).
- Langkah penghubung (S-03): langkah mencentang kembali semua kolom pada overlay setelah guard (TC-AC-CS-427), klik `[✕]` untuk menutup modal Setup Column, dan klik ikon Changelog untuk membuka modal.
- Temuan untuk QA:
  - TC-AC-CS-424 butir Langkah Uji ke-3 menyebut F5 lalu membuka lagi modal Changelog; spec mengasersi bertahannya konfigurasi setelah F5 dan menempatkan `Verifikasi` Old Value dan New Value tersembunyi sebelum F5 mengikuti urutan Expected a lalu b.
  - TC-AC-CS-426 Precondition ("konfigurasi kolom sudah diubah") tidak menyebut perubahan awal; blok TC-AC-CS-425 yang mendahuluinya sudah mengubah konfigurasi.
