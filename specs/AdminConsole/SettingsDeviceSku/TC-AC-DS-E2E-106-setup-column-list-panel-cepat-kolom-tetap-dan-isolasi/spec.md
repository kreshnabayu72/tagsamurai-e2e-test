---
id: TC-AC-DS-E2E-106-setup-column-list-panel-cepat-kolom-tetap-dan-isolasi
title: "Setup Column List: Panel Cepat Tanpa Save, Kolom Checkbox dan Actions Tetap Pinned, Isolasi Konfigurasi, dan Kolom Curated Tampil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-357
  - TC-AC-DS-359
  - TC-AC-DS-360
  - TC-AC-DS-361
coverage:
  web: automated
---

# Setup Column List: Panel Cepat Tanpa Save, Kolom Checkbox dan Actions Tetap Pinned, Isolasi Konfigurasi, dan Kolom Curated Tampil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #29 (SKU Principal inti; `HHR-ARC-100` TAG Type `—`, `TAG-ARC-USR` TAG Type `User`) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal): hanya dibaca, tidak diubah. Dipasang idempoten oleh seeding di hook `before`. Riwayat Changelog Pre-setup #33 dibaca untuk membuka modal Changelog.
- Lebar viewport cukup sempit sehingga tabel dapat digulir horizontal; ukuran viewport disediakan tim FE.
- Preferensi kolom List: langkah 2, 4, 15, dan 22 mengubah konfigurasi kolom List (tersimpan di cache browser); langkah 27 dan 28 memulihkannya. Hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Nilai data diacu lewat `Fixture.settingsDeviceSku.<kunci>`; berkas fixture disediakan tim FE (lihat Temuan untuk QA).
- Tidak ada state global lain yang diubah dan tidak ada entitas yang dibuat.

## Test Steps

### TC-AC-DS-357: Panel cepat Column Visibility

1. Klik header kolom Actions (⋯)
2. Hilangkan centang `Model/Type` pada overlay
3. Verifikasi kolom Model/Type langsung hilang dari tabel tanpa tombol Save
4. Seret `Brand` ke posisi pertama pada overlay
5. Verifikasi urutan Brand langsung berubah tanpa tombol Save
6. Muat ulang halaman dengan F5
7. Verifikasi perubahan tersimpan di cache browser dan tetap berlaku setelah muat ulang: kolom Model/Type tidak tampil dan Brand berada di posisi pertama

### TC-AC-DS-359: Kolom Checkbox dan Actions

8. Klik header kolom Actions (⋯)
9. Klik `Setup Column...` pada overlay
10. Verifikasi daftar popup memuat sedikitnya satu baris kolom lain (mis. `Device Name`)
11. Verifikasi daftar popup tidak memuat baris Checkbox maupun Actions
12. Klik ikon close `[✕]` pada popup
13. Gulir tabel secara horizontal
14. Verifikasi kolom Checkbox tetap di kiri dan kolom Actions tetap di kanan saat tabel digulir

### TC-AC-DS-360: Konfigurasi kolom List tidak memengaruhi tabel lain

15. Klik header kolom Actions (⋯), lalu hilangkan centang `Brand` pada overlay List
16. Verifikasi kolom Brand hilang dari tabel List
17. Klik ikon Changelog
18. Klik header kolom Column Visibility (⋯) pada modal
19. Verifikasi kolom pada modal Changelog tidak berubah: ketujuh kolom `Date`, `Action`, `SKU`, `Field`, `Old Value`, `New Value`, dan `Modified By` tetap tampil
20. Tutup overlay dan modal Changelog dengan ikon close `[✕]`
21. Verifikasi cache konfigurasi List dan Changelog tersimpan terpisah: kolom Brand tetap Hidden pada tabel List sementara ketujuh kolom Changelog tidak berubah

### TC-AC-DS-361: Kolom curated yang di-unhide

22. Klik header kolom Actions (⋯), lalu centang `TAG Type` pada overlay
23. Ketik Search `ARC-`, tekan Enter
24. Verifikasi kolom TAG Type tampil dengan badge `User` untuk `TAG-ARC-USR` dan `—` untuk `HHR-ARC-100`
25. Verifikasi kolom lain tidak bergeser
26. Klik `(←)` pada kotak Search

### Pemulihan state akhir

27. Klik header kolom Actions (⋯), lalu hilangkan centang `TAG Type`, centang `Model/Type` dan `Brand` pada overlay
28. Klik header kolom Actions (⋯), lalu seret `Brand` ke posisi tepat di bawah `Category` pada overlay

## Notes

- Langkah penghubung (S-03, R-16): langkah 12 dan 20 menutup popup dan modal; langkah 23 mencari baris `TAG-ARC-USR` dan `HHR-ARC-100` karena keduanya tidak berada pada halaman 1 default; langkah 26 menutup Search; tanpa asersi tambahan, kecuali langkah 10.
- Langkah penghubung pemulihan (tanpa `Verifikasi`, S-03, S-09): langkah 27 menyembunyikan kembali `TAG Type` serta menampilkan kembali `Model/Type` dan `Brand`; langkah 28 memindahkan `Brand` kembali ke posisi awal; hook `after` tetap menghapus preferensi kolom sebagai cadangan.
- Langkah 10 adalah asersi tambahan di luar Expected TC (S-03): baris kolom lain pada popup yang sama tampil sebagai pembanding sebelum asersi absence Checkbox dan Actions (langkah 11), supaya popup yang belum terisi tidak meloloskan absence (8b butir 2).
- Langkah 20 menutup overlay dan modal agar langkah 21 mengamati tabel List; TC-AC-DS-360 tidak menyebut cara mengamati Expected b ("cache terpisah"); spec mengasersinya lewat keadaan kolom List dan Changelog yang berbeda.
- Temuan untuk QA:
  - TC-AC-DS-361 langkah 3 menyebut baris `TAG-ARC-USR` dan `HHR-ARC-100` tanpa menyebut halaman; spec memakai Search `ARC-` (langkah 23).
  - Expected TC-AC-DS-361 b ("kolom lain tidak bergeser") tidak menyebut susunan kolom; spec mengasersi relatif terhadap konfigurasi pada langkah 2, 4, dan 15.
  - S-12: asersi bergantung pada nama literal Pre-setup #29, #30, dan #33 sesuai pengecualian S-12 A-11 (`suite.md`); seeding idempoten dan suite serial.
  - `suite.md` belum mendaftarkan pemulihan konfigurasi kolom yang disimpan spec (konvensi bagian 4); pemulihan lewat penghapusan preferensi kolom di browser membutuhkan kemampuan dari tim FE.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.settingsDeviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
