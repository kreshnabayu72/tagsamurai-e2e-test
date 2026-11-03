---
id: TC-AC-DS-E2E-187-register-backdrop-dan-perubahan-dikembalikan-dianggap-bersih
title: "Register SKU: Klik Backdrop Tidak Menutup Popup dan Perubahan yang Dikembalikan ke Nilai Awal Dianggap Bersih"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-169
  - TC-AC-DS-170
coverage:
  web: automated
---

# Register SKU: Klik Backdrop Tidak Menutup Popup dan Perubahan yang Dikembalikan ke Nilai Awal Dianggap Bersih

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment): SKU inti #29, pohon Category #25, Device Name #26, Brand #27, dan file foto uji #37 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: tidak ada. Spec tidak men-Submit form sehingga tidak membuat SKU dan tidak ada cleanup.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

### TC-AC-DS-169: Klik backdrop pada popup Register tidak menutup popup baik kosong maupun terisi

1. Klik tombol `[+ SKU]` pada toolbar
2. Klik area backdrop di luar popup
3. Verifikasi popup Register tetap terbuka pada form kosong
4. Ketik `H-BACK` pada field Model/Type
5. Klik area backdrop di luar popup lagi
6. Verifikasi popup Register tetap terbuka pada form terisi
7. Verifikasi dialog Unsaved Changes tidak muncul
8. Verifikasi input `H-BACK` dipertahankan

### TC-AC-DS-170: Mengubah lalu mengembalikan isian ke nilai awal dianggap bersih dan tidak memunculkan dialog

9. Hapus seluruh teks `H-BACK` pada field Model/Type sampai kosong
10. Klik ikon close `[✕]`
11. Verifikasi popup Register langsung tertutup
12. Verifikasi dialog Unsaved Changes tidak muncul

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pemakaian ulang popup (bagian 3, halaman yang sama dipakai berulang): TC-AC-DS-170 melanjutkan popup TC-AC-DS-169 yang berisi `H-BACK`; nilai itu menggantikan `H-REV` pada langkah 3 TC-AC-DS-170 dan dikosongkan kembali sehingga identik dengan keadaan awal.
- Anchor absence (bagian 8b butir 2): Verifikasi dialog Unsaved Changes tidak muncul pada TC-AC-DS-169 didahului Verifikasi popup Register tetap terbuka, dan pada TC-AC-DS-170 didahului Verifikasi popup Register tertutup.
- Pembagian TC lintas spec: TC-AC-DS-166, TC-AC-DS-167, dan TC-AC-DS-168 (penutupan popup lewat ikon close dan Esc) ada di spec 051.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-187` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
