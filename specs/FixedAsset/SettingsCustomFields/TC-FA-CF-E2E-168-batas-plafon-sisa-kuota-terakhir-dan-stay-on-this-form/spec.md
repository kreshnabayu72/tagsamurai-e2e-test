---
id: TC-FA-CF-E2E-168-batas-plafon-sisa-kuota-terakhir-dan-stay-on-this-form
title: "Batas Plafon Total pada Sisa Kuota Terakhir: Create ke-1000 Berhasil dan Create Berikutnya Diblokir"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-189
  - TC-FA-CF-617
coverage:
  web: automated
---

# Batas Plafon Total pada Sisa Kuota Terakhir: Create ke-1000 Berhasil dan Create Berikutnya Diblokir

## Prerequisites

- Mode: FE+BE (backend nyata). Kelas volume data (999 sampai 1000 field per Company Plafon). Suite serial (`parallel: false`): spec mengubah state global Master Data Count Limit dan volume field Company Plafon.
- Akun aktor: Total Control Company Plafon `totalControl_automated_{namaCompany}@qwertysystem.net`, dengan `{namaCompany}` berisi nama Company Plafon (Pre-setup #17). Akun ini tidak tertulis sebagai baris sendiri di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PLAFON_PASSWORD` (nama env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup Company Plafon (Pre-setup #17; seed fixture backend yang disediakan tim FE/BE, tidak ada endpoint yang dikarang): Master Data Count Limit 1000 dan tepat 999 field tersimpan (varian 999 field). Varian diatur lewat langkah "Atur backend" di awal tiap blok karena tiap TC mengonsumsi kuota terakhir.
- Data Dinamis (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-168`): `Last Slot {runId}-168` (Text, tersimpan), `Stay N {runId}-168` (Text, tersimpan), `Stay N1 {runId}-168` (Text, tidak tersimpan).
- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): hapus lewat API semua field Company Plafon yang namanya memuat `{runId}-168`; kembalikan Company Plafon ke baseline (Master Data Count Limit 1000 dan volume) lewat seed reset Company.
- Kemampuan teknis: pengaturan Master Data Count Limit dan volume field Company Plafon oleh backend (disediakan tim FE/BE; TC menyebut kebutuhan seed tetapi tidak mendefinisikan mekanismenya); pembacaan total record tabel (disediakan tim FE/BE).
- State global yang diubah: Master Data Count Limit dan volume field Company Plafon; dipulihkan di hook `after`.

## Test Steps

### TC-FA-CF-189: Create pada sisa kuota terakhir sukses dan Create berikutnya diblokir

1. Atur backend: Master Data Count Limit 1000 dan tepat 999 field tersimpan
2. Muat ulang halaman (F5)
3. Klik [+ Custom Field]
4. Isi Field Name `Last Slot {runId}-168` dan Data Type `Text`, lalu klik [Submit]
5. Verifikasi toast "Success, custom field has been created." tampil
6. Verifikasi total record tabel menjadi 1000
7. Klik [+ Custom Field]
8. Verifikasi dialog `Limit Reached` tampil karena Create mengonsumsi kuota
9. Klik `[OK]`

### TC-FA-CF-617: Stay on this form pada kuota terakhir: Create ke-N berhasil dan form ter-reset, Create ke-N+1 ditolak dengan dialog plafon

10. Atur backend: Master Data Count Limit 1000 dan tepat 999 field tersimpan
11. Muat ulang halaman (F5)
12. Klik [+ Custom Field]
13. Centang `Stay on this form after submitting`
14. Isi Field Name `Stay N {runId}-168` dan Data Type `Text`, lalu klik [Submit]
15. Verifikasi toast "Success, custom field has been created." tampil
16. Verifikasi modal tetap terbuka
17. Verifikasi seluruh input kembali ke default
18. Verifikasi total record tabel menjadi 1000
19. Isi Field Name `Stay N1 {runId}-168` dan Data Type `Text`, lalu klik [Submit]
20. Verifikasi dialog `Limit Reached` plafon tampil dengan teks "You've reached the platform limit of 1000 custom fields. Contact support if you need a higher limit."
21. Klik `[OK]`
22. Verifikasi dialog tertutup
23. Verifikasi modal tetap terbuka
24. Verifikasi input `Stay N1 {runId}-168` dipertahankan
25. Klik `[✕]`
26. Verifikasi dialog `Unsaved Changes` dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]` tampil
27. Klik `[Leave]`
28. Ketik Search `Stay N1 {runId}-168`, tekan Enter
29. Verifikasi field `Stay N1 {runId}-168` tidak tersimpan: empty state "No results found" tampil
30. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Kelas: volume data (kelas e, bagian 3 prinsip 13e). Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sama dengan sumber (189, 617). Kedua TC memulai dari varian 999 field dan menghabiskan kuota terakhir sehingga masing-masing mengatur ulang volume di awal blok ("Atur backend", langkah 1 dan 10).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 2, 9, 10, 11, 21, 25, 27, 28, 30 ("Atur backend" adalah pengaturan seed oleh tim FE/BE, F5 memuat ulang halaman, `[OK]` menutup dialog, Search menemukan baris target, R-16), serta pengisian form sebagai bagian langkah TC. Langkah 25 sampai 27 menutup form dirty secara deterministik (S-08).
- Langkah 29 memakai empty state hasil Search sebagai anchor positif (bagian 8b butir 2) bahwa `Stay N1 {runId}-168` tidak tersimpan.
- Pembagian TC lintas spec: TC-FA-CF-188, TC-FA-CF-190, TC-FA-CF-324, dan TC-FA-CF-627 ada di spec 058.
- Temuan untuk QA:
  - Akun Total Control Company Plafon tidak tertulis sebagai baris sendiri di Pre-setup TC (Pre-setup #1 hanya Company Alpha); ditulis "disediakan tim FE" (S-11).
  - TC-FA-CF-189: Langkah Uji tidak menyebut klik `[OK]` pada dialog sesudah asersi; spec menambahkannya sebagai langkah penghubung (langkah 9).
  - TC-FA-CF-189 dan TC-FA-CF-617: Expected "total menjadi 1000" membutuhkan pembacaan total record; kemampuan ini tidak didefinisikan di TC, PRD, atau LLD dan ditulis "disediakan tim FE/BE" (S-13).
  - TC-FA-CF-617: Expected a "seluruh input kembali ke default" tidak merinci input; ditulis satu `Verifikasi` mengikuti teks TC.
  - Nama field memakai suffix `{runId}-168` (S-12) sehingga tidak sama dengan `Last Slot`, `Stay N`, dan `Stay N1` pada Data Uji TC.
