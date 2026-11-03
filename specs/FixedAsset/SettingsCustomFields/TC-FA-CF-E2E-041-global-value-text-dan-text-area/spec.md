---
id: TC-FA-CF-E2E-041-global-value-text-dan-text-area
title: "Global Value Text, Text Area, dan Phone Kurang dari Empat Digit pada Create Custom Field"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-127
  - TC-FA-CF-128
  - TC-FA-CF-129
coverage:
  web: automated
---

# Global Value Text, Text Area, dan Phone Kurang dari Empat Digit pada Create Custom Field

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, dengan `{namaCompany}` berisi nama Company Alpha. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Company Alpha baseline (Pre-setup #11 dan #12) dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE).
- Data Dinamis (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-041`): `Global Phone {runId}-041` (Phone, tidak tersimpan), `Global Text {runId}-041` (Text), `Global Text Area {runId}-041` (Text Area). Nilai yang diketik: 121 dan 120 karakter huruf `D`, 361 dan 360 karakter huruf `E`, nomor `123`.
- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-041`.
- Kemampuan teknis: pengisian nilai panjang (121 sampai 361 karakter) pada input Value; katalog kode negara pada kontrol Phone.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-129: Global Value Phone kurang dari 4 digit setelah kode negara ditolak

1. Klik [+ Custom Field]
2. Isi Field Name `Global Phone {runId}-041`, pilih Data Type `Phone`, Scope `General`, Value Type `Global`
3. Pilih kode negara dari katalog dan isi nomor `123`
4. Klik [Submit]
5. Verifikasi pesan inline "Min. 4 characters" tampil pada input Value
6. Verifikasi Submit ditolak: modal tetap terbuka
7. Klik [Clear Field]

### TC-FA-CF-127: Global Value Text 121 karakter ditolak dan 120 karakter diterima

8. Isi Field Name `Global Text {runId}-041`, pilih Data Type `Text`, Scope `General`, Value Type `Global`
9. Isi Value 121 karakter (huruf `D` diulang 121 kali)
10. Verifikasi pesan inline "Max. 120 characters" tampil pada input Value
11. Klik [Submit]
12. Verifikasi Submit ditolak: modal tetap terbuka
13. Hapus satu karakter pada Value sehingga 120 karakter
14. Klik [Submit]
15. Verifikasi Submit sukses: toast "Success, custom field has been created." tampil

### TC-FA-CF-128: Global Value Text Area 361 karakter ditolak dan 360 karakter diterima

16. Klik [+ Custom Field]
17. Isi Field Name `Global Text Area {runId}-041`, pilih Data Type `Text Area`, Scope `General`, Value Type `Global`
18. Isi Value 361 karakter (huruf `E` diulang 361 kali)
19. Verifikasi pesan inline "Max. 360 characters" tampil pada input Value
20. Klik [Submit]
21. Verifikasi Submit ditolak: modal tetap terbuka
22. Hapus satu karakter pada Value sehingga 360 karakter
23. Tunggu toast lama hilang otomatis
24. Klik [Submit]
25. Verifikasi Submit sukses: toast "Success, custom field has been created." tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 129, 127, 128 (urutan sumber 127, 128, 129). TC-FA-CF-129 hanya diblokir sehingga lebih dulu; TC-FA-CF-127 dan TC-FA-CF-128 berakhir dengan Submit sukses yang menutup modal (validasi diblokir sebelum aksi sukses, S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 ([Clear Field] mengosongkan modal agar TC berikutnya memakai modal yang sama; jumlah buka form tidak melebihi jumlah kejadian menutup), langkah 13 dan 22 (menyusutkan nilai ke batas), langkah 16 (membuka modal sesudah Submit sukses menutupnya), serta pengisian form sebagai bagian langkah TC.
- Asersi "Submit sukses" pada TC-FA-CF-127 dan TC-FA-CF-128 ditulis sebagai toast sukses baku `Success, custom field has been created.` (tertulis di TC-FA-CF-141, 143, dan 155); asersi tambahan itu dicatat sesuai S-03. "Submit ditolak" diamati lewat modal yang tetap terbuka.
- Langkah penghubung toast (S-03, R-22): langkah 23 (`Tunggu toast lama hilang otomatis`, aksi tanpa `Verifikasi`) mendahului aksi yang menghasilkan toast sukses berteks sama dengan toast yang sudah diasersi sebelumnya; `Verifikasi` toast berikutnya tidak membaca toast lama.
- Temuan untuk QA:
  - TC-FA-CF-127 dan TC-FA-CF-128: Expected a menyebut "Submit ditolak" pada nilai terlalu panjang, tetapi Langkah Uji tidak memuat klik [Submit] pada nilai itu (klik [Submit] hanya sesudah nilai dipangkas). Spec menambah klik [Submit] pada langkah 11 dan 20 agar penolakan teramati.
  - TC-FA-CF-129: TC tidak menyebut kode negara yang dipilih ("dari katalog"); spec mengikuti teks TC.
  - Nama field memakai suffix `{runId}-041` (S-12) sehingga tidak sama dengan `Global Text`, `Global Text Area`, dan `Global Phone` pada Data Uji TC; asersi tidak bergantung pada nama field.
  - Judul slug folder ini menyebut Text dan Text Area, sedangkan TC-FA-CF-129 (Phone kurang dari 4 digit) dipetakan ke spec ini.
