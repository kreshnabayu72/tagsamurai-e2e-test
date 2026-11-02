---
id: TC-AC-CS-E2E-154-list-setup-column-reset-dan-discard
title: "List Setup Column: Reset dan Discard"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-371
  - TC-AC-CS-372
coverage:
  web: automated
---

# List Setup Column: Reset dan Discard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Konfigurasi kolom Setup Column dan overlay Column Visibility yang disimpan spec (List dan Modal Changelog) dipulihkan dengan menghapus preferensi kolom di browser di hook `after` (kemampuan disediakan tim FE).
- Cache Setup Column browser dikosongkan di hook `before` (kemampuan disediakan tim FE).

## Test Steps

### TC-AC-CS-371: Reset to Default mengembalikan konfigurasi bawaan setelah Save

1. Buka modal Setup Column (`⋯` lalu `[Setup Column]`), hilangkan centang `Product`, centang `Grace End`, lalu klik `[Save]`
2. Buka modal Setup Column lagi lalu klik `[Reset to Default]`
3. Verifikasi preview kembali ke bawaan (delapan kolom Hideable tampil, Grace End tersembunyi)
4. Klik `[Save]`
5. Verifikasi tabel memakai susunan bawaan
6. Tekan F5
7. Verifikasi susunan bawaan bertahan setelah F5

### TC-AC-CS-372: Menutup modal lewat silang atau Esc membuang perubahan

8. Buka modal Setup Column lalu hilangkan centang `Status`
9. Klik `[✕]`
10. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir (kolom Status tampil)
11. Verifikasi tidak ada dialog konfirmasi pada jalur `[✕]`
12. Buka modal Setup Column lagi, hilangkan centang `Status`, lalu tekan `Esc`
13. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir (kolom Status tampil)
14. Verifikasi tidak ada dialog konfirmasi pada jalur `Esc`

## Notes

- TC-AC-CS-376, 373, 374, dan 375 (Setup Column List lainnya) ada di spec 097.
- Asersi absence dialog konfirmasi (TC-AC-CS-372) didahului `Verifikasi` tabel List dengan kolom Status tampil pada permukaan yang sama (bagian 8b butir 2). Dialog `Unsaved Changes` tidak berlaku di modal Setup Column menurut Expected TC.
- Temuan untuk QA:
  - TC-AC-CS-371 Precondition (Product disembunyikan, Grace End ditampilkan) tidak menyebut langkah penyiapan; spec menyiapkannya pada langkah pertama (S-03).
  - TC-AC-CS-371 Expected b (susunan bawaan bertahan setelah F5) tidak punya langkah F5 di Langkah Uji; spec menambah langkah F5.
