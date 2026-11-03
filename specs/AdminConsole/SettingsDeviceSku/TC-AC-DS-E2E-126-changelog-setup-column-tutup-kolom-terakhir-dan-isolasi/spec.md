---
id: TC-AC-DS-E2E-126-changelog-setup-column-tutup-kolom-terakhir-dan-isolasi
title: "Setup Column Changelog: Tutup Tanpa Save, Kolom Terakhir Tidak Dapat Di-uncheck, dan Isolasi dari Konfigurasi List"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-418
  - TC-AC-DS-419
  - TC-AC-DS-420
coverage:
  web: automated
---

# Setup Column Changelog: Tutup Tanpa Save, Kolom Terakhir Tidak Dapat Di-uncheck, dan Isolasi dari Konfigurasi List

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti dan seed (#29, #30), riwayat Changelog Principal (#33), General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: tidak ada. Spec tidak menyimpan konfigurasi kolom lewat `[Save]`; satu perubahan kolom modal Changelog (kolom `Modified By` disembunyikan lewat overlay, TC-AC-DS-420) dipulihkan pada langkah terakhir.
- Kemampuan teknis (disediakan tim FE): menghapus preferensi kolom Setup Column modal Changelog dan List di browser (hook `before` agar kedua tabel berada pada konfigurasi bawaan, dan hook `after`), bukan lewat [Reset to Default].
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-418: Menutup Popup Setup Column modal Changelog dengan close atau Esc membuang perubahan

1. Klik ikon Changelog
2. Verifikasi modal "Changelog: Device SKU" tampil
3. Klik header kolom Actions (⋯) pada modal
4. Verifikasi Overlay Column Visibility tampil
5. Klik `Setup Column...`
6. Verifikasi Popup Setup Column tampil
7. Hilangkan centang `Field`
8. Verifikasi preview diperbarui: kolom `Field` hilang dari preview
9. Klik ikon close `[✕]` popup
10. Verifikasi kolom `Field` tetap tampil pada tabel modal
11. Klik header kolom Actions (⋯) pada modal, klik `Setup Column...`
12. Verifikasi checkbox `Field` tercentang pada popup yang dibuka kembali (perubahan preview dibuang)
13. Hilangkan centang `Field`, lalu tekan Esc
14. Verifikasi kolom `Field` tetap tampil pada tabel modal

### TC-AC-DS-419: Kolom terakhir yang tampil pada modal Changelog tidak dapat di-uncheck

15. Klik header kolom Actions (⋯) pada modal, klik `Setup Column...`
16. Verifikasi checkbox `Field` tercentang pada popup yang dibuka kembali (perubahan dari penutupan Esc dibuang)
17. Hilangkan centang kolom `Date`, `Action`, `SKU`, `Field`, `Old Value`, dan `New Value` satu per satu sampai tersisa satu kolom `Modified By`
18. Hover checkbox kolom `Modified By`
19. Verifikasi checkbox kolom `Modified By` disabled
20. Verifikasi tooltip "At least one column must remain visible." tampil
21. Klik ikon close `[✕]` popup

### TC-AC-DS-420: Konfigurasi kolom modal Changelog tidak memengaruhi konfigurasi List

22. Klik header kolom Actions (⋯) pada modal
23. Verifikasi Overlay Column Visibility tampil
24. Hilangkan centang `Modified By` pada overlay modal
25. Verifikasi kolom `Modified By` hilang dari tabel modal
26. Tutup modal Changelog
27. Klik header kolom Actions (⋯) pada List
28. Verifikasi Overlay Column Visibility List tampil
29. Verifikasi kolom List dari Photo sampai Last Modified tidak berubah
30. Klik ikon Changelog
31. Verifikasi kolom `Modified By` tidak tampil pada tabel modal (konfigurasi modal Changelog dan List tersimpan terpisah)

### Pemulihan state akhir

32. Klik header kolom Actions (⋯) pada modal, centang kembali `Modified By` pada overlay; tutup modal Changelog

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 11 dan 15 (membuka kembali popup sesuai alur TC), langkah 21 (menutup popup dengan `[✕]`; perubahan dibuang sesuai TC 418, tidak ada dialog yang diasumsikan), langkah 26, dan langkah 32 (S-03, S-09).
- Langkah 12 dan 16 adalah asersi tambahan atas Expected 418 butir "perubahan preview dibuang" (popup yang dibuka kembali menunjukkan `Field` tercentang); langkah 31 adalah pembuktian Expected 420 butir b ("tersimpan terpisah") karena cache tidak teramati langsung; langkah 29 mengikuti Expected butir a.
- Langkah 17 memilih `Modified By` sebagai kolom terakhir yang tersisa karena TC hanya menyebut "tersisa satu kolom".
- Temuan untuk QA:
  - S-15: TC 418 tidak menyatakan apakah menutup popup dengan `[✕]` atau Esc saat dirty menampilkan dialog Unsaved Changes; spec mengikuti TC (perubahan dibuang tanpa dialog).
  - S-15: TC 419 tidak menyebut kolom mana yang tersisa; TC 420 menyebut "Kolom List (Photo sampai Last Modified)" tanpa daftar utuh sehingga langkah 29 mengikuti frasa TC.
  - Fixture rancangan Pre-setup #33 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
