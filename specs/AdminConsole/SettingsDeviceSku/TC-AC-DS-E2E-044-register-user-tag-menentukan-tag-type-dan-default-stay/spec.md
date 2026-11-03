---
id: TC-AC-DS-E2E-044-register-user-tag-menentukan-tag-type-dan-default-stay
title: "Register SKU: Checkbox This is User TAG Menentukan TAG Type dan Default Checkbox Stay on this form"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-152
  - TC-AC-DS-153
coverage:
  web: automated
---

# Register SKU: Checkbox This is User TAG Menentukan TAG Type dan Default Checkbox Stay on this form

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`TAG > NFC > Asset TAG`); Device Name #26 (`Asset TAG`); Brand Principal #27 (`Arcturus`); File foto uji #37 (`foto-a.jpg`, 200 KB); kolom `TAG Type` pada List berstatus Hidden secara default; SKU inti #29 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: SKU `NEW-UTAG-1-{runId}-044` (This is User TAG dicentang) dan `NEW-UTAG-2-{runId}-044` (tidak dicentang), dibuat oleh TC-AC-DS-152. Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API SKU bersuffix `{runId}-044` milik Principal.
- State yang diubah: kolom `TAG Type` pada List di-unhide lewat Column Visibility oleh langkah 19. Pemulihan di hook `after` dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

### TC-AC-DS-153: Checkbox Stay on this form after submitting bernilai tidak tercentang secara default

1. Klik tombol `[+ SKU]` pada toolbar
2. Verifikasi checkbox `Stay on this form after submitting` tidak tercentang pada pembukaan pertama
3. Klik ikon close `[✕]`
4. Klik tombol `[+ SKU]` pada toolbar
5. Verifikasi checkbox `Stay on this form after submitting` tidak tercentang pada pembukaan berikutnya

### TC-AC-DS-152: Checkbox This is User TAG dicentang menghasilkan TAG Type User dan tidak dicentang menghasilkan Object

6. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
7. Klik field Device Name lalu pilih `Asset TAG`
8. Klik field Brand lalu pilih `Arcturus`
9. Ketik `T-UT1` pada field Model/Type
10. Ketik `NEW-UTAG-1-{runId}-044` pada field SKU
11. Centang checkbox `This is User TAG`
12. Unggah `foto-a.jpg` pada field Photo
13. Klik `[Submit]`
14. Verifikasi toast sukses "Success, device SKU has been registered." tampil untuk pendaftaran pertama
15. Tunggu toast sukses pertama hilang otomatis
16. Klik `[+ SKU]` lalu daftarkan SKU `NEW-UTAG-2-{runId}-044` (Category `Asset TAG`, Device Name `Asset TAG`, Brand `Arcturus`, Model/Type `T-UT2`, Photo `foto-a.jpg`) tanpa mencentang checkbox `This is User TAG`
17. Klik `[Submit]`
18. Verifikasi toast sukses "Success, device SKU has been registered." tampil untuk pendaftaran kedua
19. Unhide kolom `TAG Type` lewat Column Visibility
20. Ketik Search `{runId}-044`, tekan Enter
21. Verifikasi baris `NEW-UTAG-1-{runId}-044` menampilkan TAG Type `User`
22. Verifikasi baris `NEW-UTAG-2-{runId}-044` menampilkan TAG Type `Object`
23. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 15 menunggu toast pertama hilang (R-12); langkah 19 adalah bagian TC-AC-DS-152 (langkah 13 TC); langkah 20 dan 23 (Search untuk menemukan baris target lalu menutup Search, R-16). Popup tertutup sendiri sesudah Submit sukses. Pada TC-AC-DS-153 popup ditutup dengan `[✕]` dari form bersih sehingga tidak ada dialog Unsaved Changes (TC-AC-DS-153 langkah 4).
- Urutan TC diubah: TC-AC-DS-153 (screening tanpa Submit) dijalankan sebelum TC-AC-DS-152 (S-10); Model/Type `T-UT2` pada pendaftaran kedua dipilih spec karena TC hanya menyebut "Asset TAG tanpa mencentang checkbox".
- Pembagian TC lintas spec: TC-AC-DS-160 (Stay tercentang mereset semua field) ada di spec 186.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-044` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - Search `{runId}-044` pada langkah 20 mengandalkan Search mencocokkan substring kode SKU; cara pencocokan Search tidak dijelaskan di TC.
  - suite.md belum mendaftarkan pemulihan Setup Column (bagian 4); spec ini mengubah visibilitas kolom `TAG Type` dan menuliskan pemulihannya di Prerequisites.
