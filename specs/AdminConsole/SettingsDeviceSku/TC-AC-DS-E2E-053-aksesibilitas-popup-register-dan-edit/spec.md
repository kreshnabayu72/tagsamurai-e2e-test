---
id: TC-AC-DS-E2E-053-aksesibilitas-popup-register-dan-edit
title: "Aksesibilitas Popup Register dan Edit: Focus Trap, Esc, dan Atribut Aria"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-174
  - TC-AC-DS-254
coverage:
  web: automated
---

# Aksesibilitas Popup Register dan Edit: Focus Trap, Esc, dan Atribut Aria

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): SKU inti #29 `HHR-ARC-200` (stok 0, hanya dibuka di popup Edit tanpa disimpan; Last Modified tidak berubah); pohon Category #25, Device Name #26, Brand #27, dan file foto uji #37 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: tidak ada. Spec tidak menyimpan perubahan sehingga tidak membuat SKU dan tidak ada cleanup.
- Kemampuan teknis (disediakan tim FE): pembacaan atribut DOM (`aria-required`, `aria-describedby`) dan posisi fokus keyboard.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

### TC-AC-DS-174: Accessibility Popup Register: focus trap, Esc, dan atribut aria

1. Klik tombol `[+ SKU]` pada toolbar
2. Tekan Tab berulang melewati seluruh kontrol popup
3. Verifikasi fokus tetap berputar di dalam popup dan tidak keluar ke halaman di belakang
4. Klik `[Submit]` tanpa mengisi field apa pun
5. Periksa atribut aria pada field wajib dan field yang memiliki error
6. Verifikasi field wajib memiliki aria-required
7. Verifikasi field yang memiliki error memiliki aria-describedby
8. Tekan Esc
9. Verifikasi popup Register tertutup bersih tanpa dialog Unsaved Changes

### TC-AC-DS-254: Accessibility Popup Edit: focus trap, Esc, dan atribut aria

10. Klik ⋯ pada baris `HHR-ARC-200` lalu pilih `Edit`
11. Tekan Tab berulang melewati seluruh kontrol popup
12. Verifikasi fokus tetap berputar di dalam popup
13. Kosongkan field Model/Type lalu klik `[Save]`
14. Periksa atribut aria pada field wajib, field terkunci, dan field dengan error
15. Verifikasi field wajib memiliki aria-required
16. Verifikasi field dengan error memiliki aria-describedby
17. Pindahkan fokus keyboard ke field Category yang terkunci
18. Verifikasi tooltip field terkunci dapat dicapai dengan fokus keyboard
19. Klik ikon close `[✕]`
20. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
21. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 4 dan 13 memicu error validasi supaya atribut `aria-describedby` pada field dengan error dapat diamati (TC tidak memicu error); langkah 19 sampai 21 menutup form dirty secara deterministik (S-08). Popup Edit tidak pernah tersimpan karena `[Save]` ditolak oleh pesan wajib diisi.
- Urutan Verifikasi popup Register: Esc menutup popup (Expected c TC-AC-DS-174) diasersi pada keadaan form kosong dengan error, yang bersih menurut TC-AC-DS-166.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-053` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - TC-AC-DS-174 dan TC-AC-DS-254 tidak memicu keadaan error padahal Expected memeriksa aria-describedby field dengan error; spec menambahkan pemicu (langkah penghubung) tanpa mengubah Expected.
  - TC-AC-DS-254 memakai SKU `HHR-ARC-200` (stok 0) sehingga hanya Category yang terkunci dan tidak ada tooltip kunci stok; spec menguji fokus keyboard pada field Category. Bila yang dimaksud TC adalah tooltip kunci stok (SKU, Range Type, User TAG), TC perlu memakai SKU berstok lebih dari 0 (mis. `HHR-ARC-100`).
