---
id: TC-AC-DS-E2E-186-register-stay-on-form-mereset-field-dan-popup-tetap-terbuka
title: "Register SKU: Submit dengan Stay on this form Mereset Semua Field termasuk Foto dan Popup Tetap Terbuka"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-160
coverage:
  web: automated
---

# Register SKU: Submit dengan Stay on this form Mereset Semua Field termasuk Foto dan Popup Tetap Terbuka

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`Hardware > Handheld Reader > UHF Handheld`); Device Name #26 (`UHF Handheld Reader`); Brand Principal #27 (`Arcturus`); file foto uji #37 (`foto-a.jpg`, 200 KB); SKU inti #29 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: SKU `NEW-STAY-01-{runId}-186` (Range Type `Short Range`), dibuat oleh TC-AC-DS-160. Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API SKU bersuffix `{runId}-186` milik Principal.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

1. Klik tombol `[+ SKU]` pada toolbar
2. Centang `Stay on this form after submitting`
3. Klik field Category, expand `Hardware` lalu `Handheld Reader`, pilih node `UHF Handheld`, lalu klik `[Select]`
4. Klik field Device Name lalu pilih `UHF Handheld Reader`
5. Klik field Brand lalu pilih `Arcturus`
6. Ketik `H-ST1` pada field Model/Type
7. Ketik `NEW-STAY-01-{runId}-186` pada field SKU
8. Pilih Range Type `Short Range`
9. Unggah `foto-a.jpg` pada field Photo
10. Klik `[Submit]`
11. Verifikasi toast sukses "Success, device SKU has been registered." tampil
12. Verifikasi popup Register tetap terbuka
13. Verifikasi semua field kembali kosong dengan placeholder tampil
14. Verifikasi slot Photo dan section kondisional kembali kosong
15. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
16. Klik ikon close `[✕]`
17. Ketik Search `NEW-STAY-01-{runId}-186`, tekan Enter
18. Verifikasi baris `NEW-STAY-01-{runId}-186` ada pada List
19. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 16 menutup popup form bersih tanpa dialog Unsaved Changes (form direset oleh Stay); langkah 17 dan 19 (Search untuk menemukan baris target lalu menutup Search, R-16). Expected d TC-AC-DS-160 (baris sudah ada pada List di balik popup) diasersi sesudah popup ditutup karena baris di balik popup tidak dapat dicari.
- Pembagian TC lintas spec: TC-AC-DS-161 (dua SKU berturut-turut dengan Stay) ada di spec 045; TC-AC-DS-152 dan TC-AC-DS-153 (checkbox User TAG dan default Stay) ada di spec 044.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-186` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - Post Condition TC-AC-DS-160 (entri log) tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini (S-01).
