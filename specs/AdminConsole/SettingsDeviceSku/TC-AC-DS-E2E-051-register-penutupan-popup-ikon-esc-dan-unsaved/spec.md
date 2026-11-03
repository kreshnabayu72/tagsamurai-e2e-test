---
id: TC-AC-DS-E2E-051-register-penutupan-popup-ikon-esc-dan-unsaved
title: "Register SKU: Penutupan Popup Kosong dan Terisi, Esc, dan Dialog Unsaved Changes"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-166
  - TC-AC-DS-167
  - TC-AC-DS-168
coverage:
  web: automated
---

# Register SKU: Penutupan Popup Kosong dan Terisi, Esc, dan Dialog Unsaved Changes

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment): SKU inti #29, pohon Category #25, Device Name #26, Brand #27, dan file foto uji #37 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: tidak ada. Spec tidak men-Submit form sehingga tidak membuat SKU dan tidak ada cleanup. Jumlah total SKU pada footer pagination List dicatat di langkah 1 sebagai baseline N (dibaca dari UI, bukan angka absolut).
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

1. Catat jumlah total SKU pada footer pagination List sebagai baseline N

### TC-AC-DS-166: Menutup popup Register yang masih kosong tidak memunculkan dialog Unsaved Changes

2. Klik tombol `[+ SKU]` pada toolbar
3. Klik ikon close `[✕]`
4. Verifikasi popup Register langsung tertutup
5. Verifikasi dialog Unsaved Changes tidak muncul
6. Klik tombol `[+ SKU]` pada toolbar
7. Tekan Esc
8. Verifikasi popup Register langsung tertutup
9. Verifikasi dialog Unsaved Changes tidak muncul

### TC-AC-DS-167: Menutup popup Register yang sudah terisi lewat ikon close menampilkan dialog Unsaved Changes

10. Klik tombol `[+ SKU]` pada toolbar
11. Ketik `H-DIRTY` pada field Model/Type
12. Klik ikon close `[✕]`
13. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
14. Klik `[Cancel]`
15. Verifikasi dialog Unsaved Changes tertutup
16. Verifikasi popup Register tetap terbuka
17. Verifikasi input `H-DIRTY` dipertahankan
18. Klik ikon close `[✕]`
19. Klik `[Leave]`
20. Verifikasi dialog Unsaved Changes tertutup
21. Verifikasi popup Register tertutup tanpa menyimpan

### TC-AC-DS-168: Menekan Esc pada popup Register yang terisi menampilkan dialog Unsaved Changes

22. Klik tombol `[+ SKU]` pada toolbar
23. Ketik `H-DIRTY2` pada field Model/Type
24. Tekan Esc
25. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
26. Tekan Esc pada dialog Unsaved Changes
27. Verifikasi dialog Unsaved Changes tertutup (Esc pada dialog konfirmasi setara `[Cancel]`)
28. Verifikasi popup Register tetap terbuka
29. Verifikasi input `H-DIRTY2` dipertahankan
30. Klik ikon close `[✕]`
31. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
32. Klik `[Leave]`
33. Verifikasi jumlah total SKU pada footer pagination sama dengan baseline N: tidak ada SKU baru dari ketiga TC

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 1 mencatat baseline N; langkah 30 sampai 32 menutup form dirty TC-AC-DS-168 secara deterministik (S-08).
- Butir "tidak ada SKU baru" pada Expected TC-AC-DS-167 butir c diasersi sekali di langkah akhir dengan selisih terhadap baseline N (S-12) karena tidak ada baris yang bisa dicari.
- Anchor absence (bagian 8b butir 2): Verifikasi dialog Unsaved Changes tidak muncul didahului Verifikasi popup Register tertutup.
- Pembagian TC lintas spec: TC-AC-DS-169 dan TC-AC-DS-170 (klik backdrop dan perubahan yang dikembalikan ke nilai awal) ada di spec 187.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-051` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
