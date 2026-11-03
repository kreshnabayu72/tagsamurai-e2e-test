---
id: TC-AC-DS-E2E-139-usage-setup-column-reset-tutup-dan-kolom-terakhir
title: "Setup Column Usage: Reset to Default, Tutup Tanpa Save, dan Kolom Terakhir Tidak Dapat Di-uncheck"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-459
  - TC-AC-DS-460
  - TC-AC-DS-461
coverage:
  web: automated
---

# Setup Column Usage: Reset to Default, Tutup Tanpa Save, dan Kolom Terakhir Tidak Dapat Di-uncheck

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti `HHR-ARC-100` serta seed (#29, #30); data Usage `HHR-ARC-100` lima baris (#32, #24). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: tidak ada. Spec menyimpan konfigurasi bawaan kolom Usage pada langkah 9; selebihnya perubahan dibuang tanpa Save.
- Kemampuan teknis (disediakan tim FE): menghapus preferensi kolom Setup Column popup Usage di browser (hook `before` dan hook `after`), bukan lewat [Reset to Default].
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

1. Klik SKU `HHR-ARC-100`
2. Verifikasi Popup `Device SKU Detail` tampil

### TC-AC-DS-459: Reset to Default popup Usage by Company mengembalikan konfigurasi kolom ke bawaan

3. Klik header kolom Actions (⋯) pada popup, klik `Setup Column...`
4. Verifikasi Popup Setup Column tampil
5. Hilangkan centang `Entity Type`
6. Geser `Company` ke posisi akhir
7. Klik `[Reset to Default]`
8. Verifikasi preview kembali ke default: tiga kolom dengan urutan `Company | Entity Type | Total Stock`
9. Klik `[Save]`
10. Verifikasi tabel Usage tetap pada konfigurasi default

### TC-AC-DS-460: Menutup Popup Setup Column Usage dengan close atau Esc membuang perubahan

11. Klik header kolom Actions (⋯) pada popup, klik `Setup Column...`
12. Hilangkan centang `Total Stock`
13. Verifikasi preview diperbarui: kolom `Total Stock` hilang dari preview
14. Klik ikon close `[✕]` popup Setup Column
15. Verifikasi kolom `Total Stock` tetap tampil pada tabel Usage
16. Klik header kolom Actions (⋯) pada popup, klik `Setup Column...`
17. Verifikasi checkbox `Total Stock` tercentang pada popup yang dibuka kembali (perubahan preview dibuang)
18. Hilangkan centang `Total Stock`, lalu tekan Esc
19. Verifikasi kolom `Total Stock` tetap tampil pada tabel Usage

### TC-AC-DS-461: Kolom terakhir yang tampil pada popup Usage tidak dapat di-uncheck

20. Klik header kolom Actions (⋯) pada popup, klik `Setup Column...`
21. Verifikasi checkbox `Total Stock` tercentang pada popup yang dibuka kembali (perubahan dari penutupan Esc dibuang)
22. Hilangkan centang `Company` dan `Entity Type` sampai tersisa satu kolom `Total Stock`
23. Hover checkbox kolom `Total Stock`
24. Verifikasi checkbox kolom `Total Stock` disabled
25. Verifikasi tooltip "At least one column must remain visible." tampil

### Pemulihan state akhir

26. Klik ikon close `[✕]` popup Setup Column; tutup popup `Device SKU Detail` dengan ikon close `[✕]`

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 26 (S-03). Langkah 12 dan 22 menyiapkan perubahan yang dibuang tanpa Save.
- Langkah 17 dan 21 adalah asersi tambahan atas Expected 460 "perubahan preview dibuang" (popup yang dibuka kembali menunjukkan `Total Stock` tercentang), dicatat di sini sebagai pembuktian karena preview tidak teramati setelah popup tertutup.
- Langkah 22 memilih `Total Stock` sebagai kolom yang tersisa karena TC hanya menyebut "tersisa satu kolom".
- Temuan untuk QA:
  - S-15: TC 460 tidak menyatakan apakah menutup popup Setup Column saat dirty menampilkan dialog Unsaved Changes, dan apakah Esc menutup hanya popup Setup Column; spec mengikuti TC.
  - S-15: TC 461 tidak menyebut kolom mana yang tersisa.
  - S-14: TC tidak menyebut Search untuk menemukan baris `HHR-ARC-100`; spec mengandalkan baris itu tampil di halaman pertama List.
  - Fixture rancangan Pre-setup #32 dan #24 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
