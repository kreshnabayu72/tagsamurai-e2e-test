---
id: TC-FA-CF-E2E-042-global-value-phone
title: "Global Value Phone: Batas 15 Digit dan Input Hanya Angka"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-130
  - TC-FA-CF-131
coverage:
  web: automated
---

# Global Value Phone: Batas 15 Digit dan Input Hanya Angka

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, dengan `{namaCompany}` berisi nama Company Alpha. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Company Alpha baseline (Pre-setup #11 dan #12) dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE).
- Data Dinamis (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-042`): `Global Phone {runId}-042` (Phone, TC-FA-CF-130) dan `Global Phone Digit {runId}-042` (Phone, TC-FA-CF-131). Nilai yang diketik: `1234567890123456` (16 digit), `12ab34`.
- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-042`.
- Kemampuan teknis: pengetikan karakter huruf ke input nomor Phone dan pembacaan nilai yang tersisa di input.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-130: Global Value Phone 16 digit ditolak dan 15 digit diterima

1. Klik [+ Custom Field]
2. Isi Field Name `Global Phone {runId}-042`, pilih Data Type `Phone`, Scope `General`, Value Type `Global`
3. Isi nomor 16 digit `1234567890123456`
4. Verifikasi pesan inline "Max. 15 characters" tampil pada input Value
5. Hapus satu digit sehingga 15 digit
6. Klik [Submit]
7. Verifikasi Submit sukses: toast "Success, custom field has been created." tampil

### TC-FA-CF-131: Global Value Phone hanya menerima angka

8. Klik [+ Custom Field]
9. Isi Field Name `Global Phone Digit {runId}-042`, pilih Data Type `Phone`, Scope `General`, Value Type `Global`
10. Ketik `12ab34` pada input nomor
11. Verifikasi karakter huruf tidak masuk ke input
12. Verifikasi nilai yang tersisa hanya angka `1234`
13. Klik [Submit]

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sama dengan sumber (130, 131). TC-FA-CF-130 berakhir dengan Submit sukses yang menutup modal sehingga TC-FA-CF-131 membuka modal baru (langkah 8).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5 (menyusutkan nilai ke batas), serta pengisian form dan klik tombol sebagai bagian langkah TC. Klik [Submit] pada langkah 13 adalah langkah TC tanpa Expected; hook `after` menghapus field yang tersimpan.
- Asersi "Submit sukses" pada TC-FA-CF-130 ditulis sebagai toast sukses baku `Success, custom field has been created.` (tertulis di TC-FA-CF-141, 143, dan 155); asersi tambahan itu dicatat sesuai S-03.
- Temuan untuk QA:
  - TC-FA-CF-131: langkah 4 TC mengklik [Submit] tetapi Expected tidak menyebut hasilnya; nilai `1234` memenuhi batas minimum 4 digit sehingga Submit menyimpan field. Hasil Submit tidak diasersi.
  - TC-FA-CF-130 dan TC-FA-CF-131: TC tidak menyebut pemilihan kode negara (berbeda dengan TC-FA-CF-129 yang memilih kode negara dari katalog); spec mengikuti teks TC dan memakai kode negara bawaan kontrol.
  - Nama field memakai suffix `{runId}-042` (S-12) sehingga tidak sama dengan `Global Phone` pada Data Uji TC.
