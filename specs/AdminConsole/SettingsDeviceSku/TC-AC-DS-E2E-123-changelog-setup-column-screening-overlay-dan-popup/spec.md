---
id: TC-AC-DS-E2E-123-changelog-setup-column-screening-overlay-dan-popup
title: "Setup Column Changelog: Screening Overlay dan Popup"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-412
  - TC-AC-DS-413
coverage:
  web: automated
---

# Setup Column Changelog: Screening Overlay dan Popup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti dan seed (#29, #30), riwayat Changelog Principal (#33), General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: tidak ada. Spec tidak menyimpan konfigurasi kolom.
- Kemampuan teknis (disediakan tim FE): menghapus preferensi kolom Setup Column modal Changelog di browser (hook `before` agar kolom berada pada konfigurasi bawaan, dan hook `after`), bukan lewat [Reset to Default].
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-412: Screening Overlay Column Visibility modal Changelog

1. Klik ikon Changelog
2. Verifikasi modal "Changelog: Device SKU" tampil
3. Klik header kolom Actions (⋯) pada modal
4. Verifikasi Overlay Column Visibility tampil
5. Verifikasi tombol `Setup Column...` tampil di bagian bawah overlay
6. Verifikasi daftar kolom berurutan `Date | Action | SKU | Field | Old Value | New Value | Modified By`
7. Verifikasi ketujuh kolom tercentang dan enabled (Hideable)
8. Verifikasi setiap kolom memiliki drag handle
9. Verifikasi kolom Actions tidak tampil sebagai baris

### TC-AC-DS-413: Screening Popup Setup Column modal Changelog dan Preview Table

10. Klik `Setup Column...`
11. Verifikasi Popup Setup Column tampil
12. Verifikasi header memuat judul "Setup Column"
13. Verifikasi header memuat deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns."
14. Verifikasi header memuat ikon close `[✕]`
15. Verifikasi body memuat tujuh kolom dengan checkbox tercentang
16. Verifikasi setiap kolom memiliki drag handle
17. Verifikasi setiap kolom memiliki ikon Pin
18. Verifikasi section Live Preview menampilkan urutan header dan data yang sama dengan tabel asli
19. Verifikasi footer memuat tombol `[Reset to Default]` dan `[Save]` rata kanan
20. Verifikasi footer tidak memuat tombol `[Cancel]`

### Pemulihan state akhir

21. Klik ikon close `[✕]` pada Popup Setup Column; tutup modal Changelog

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 21 (menutup popup tanpa perubahan lalu modal; popup tidak berubah sehingga tidak ada dialog Unsaved Changes yang diasumsikan, S-03).
- Expected 412 butir b dipecah menjadi langkah 6 (urutan) dan langkah 7 (tercentang dan enabled); butir c menjadi langkah 8 dan 9. Expected 413 butir b.i dipecah menjadi langkah 15 sampai 17 (checkbox, drag handle, Pin per klausa S-01).
- Pembagian TC lintas spec: ceklis dan unceklis kolom (TC-AC-DS-414) ada di spec 192; geser urutan dan Reset to Default di spec 124; pin dan batas pin keempat di spec 125; tutup tanpa Save, kolom terakhir, dan isolasi konfigurasi di spec 126.
- Temuan untuk QA:
  - Fixture rancangan Pre-setup #33 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
  - TC 413 Expected butir b.ii tidak menyebut data Live Preview yang diasersi selain "sama dengan tabel asli"; spec mengikuti TC.
