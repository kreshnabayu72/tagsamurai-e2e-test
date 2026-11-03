---
id: TC-FA-CF-E2E-059-batas-cap-per-asset-name-pada-create
title: "Batas Cap Per Asset Name pada Create: Scope Specific, Scope General, Batas Tepat, dan Stay on this Form"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-191
  - TC-FA-CF-192
  - TC-FA-CF-193
  - TC-FA-CF-197
coverage:
  web: automated
---

# Batas Cap Per Asset Name pada Create: Scope Specific, Scope General, Batas Tepat, dan Stay on this Form

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`): spec menambah field Active pada Company Cap sehingga mengubah hitungan Active `Generator`.
- Akun aktor: Total Control Company Cap `totalControl_automated_{namaCompany}@qwertysystem.net`, dengan `{namaCompany}` berisi nama Company Cap (Pre-setup #16). Akun ini tidak tertulis sebagai baris sendiri di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_CAP_PASSWORD` (nama env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup Company Cap (Pre-setup #16; hanya dibaca, dipulihkan hook `before` lewat seed reset Company yang disediakan tim FE/BE): Max custom fields per asset name 2; Asset Name `Compressor`, `Generator`, `Pump`, `Turbine`; field Active `Cap General` (General), `Cap Pump` (`Pump`), `Cap Compressor` (`Compressor`); field Inactive `Cap Pump Inactive`, `Cap Gen Inactive`, `Cap Both Inactive`, `Cap Orphan`. Hitungan Active: `Pump` 2, `Compressor` 2, `Generator` 1, `Turbine` 1.
- Data Dinamis (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-059`): `Cap Pump New {runId}-059`, `Cap General New {runId}-059`, dan `Stay Cap {runId}-059` (Text; tidak tersimpan) serta `Cap Gen New {runId}-059` (Text, Scope `Generator`; tersimpan).
- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): hapus lewat API semua field Company Cap yang namanya memuat `{runId}-059`.
- Kemampuan teknis: pembacaan teks dialog `Limit Reached` dan keadaan modal Create di belakangnya.
- State global: hitungan Active `Generator` bertambah satu oleh TC-FA-CF-193; dipulihkan di hook `after` (hapus field); suite berjalan serial.

## Test Steps

### TC-FA-CF-191: Submit Scope Specific pada Asset Name yang sudah penuh ditolak dengan dialog batas per Asset Name

1. Klik [+ Custom Field]
2. Isi Field Name `Cap Pump New {runId}-059` dan Data Type `Text`, pilih Scope `Specific Asset Name` dengan `Pump`
3. Klik [Submit]
4. Verifikasi dialog blok 🔒 `Limit Reached` dengan teks "You've reached the limit of 2 custom fields for Pump. Remove an existing field or narrow the scope, or contact support if you need a higher limit." dan tombol `[OK]` tampil di atas modal Create
5. Klik `[OK]`
6. Verifikasi dialog tertutup
7. Verifikasi modal Create tetap terbuka
8. Verifikasi seluruh input dipertahankan: Field Name `Cap Pump New {runId}-059`, Data Type `Text`, Scope `Specific Asset Name` dengan `Pump`

### TC-FA-CF-192: Submit Scope General ditolak bila minimal satu Asset Name sudah penuh dan dialog menyebut nama Asset Name yang penuh

9. Ganti isi Field Name dengan `Cap General New {runId}-059`, lalu ganti Scope menjadi `General`
10. Klik [Submit]
11. Verifikasi dialog `Limit Reached` dengan teks "You've reached the limit of 2 custom fields for Compressor and Pump. Remove an existing field or narrow the scope, or contact support if you need a higher limit."
12. Verifikasi field tidak tersimpan: modal tetap terbuka
13. Klik `[OK]`

### TC-FA-CF-197: Checkbox Stay tidak berpengaruh saat Create ditolak karena batas

14. Centang `Stay on this form after submitting`
15. Ganti isi Field Name dengan `Stay Cap {runId}-059`, lalu ganti Scope menjadi `Specific Asset Name` dengan `Pump`
16. Klik [Submit]
17. Verifikasi dialog `Limit Reached` tampil
18. Klik `[OK]`
19. Verifikasi modal tetap terbuka
20. Verifikasi input tidak direset karena tidak ada field yang tersimpan: Field Name `Stay Cap {runId}-059`

### TC-FA-CF-193: Submit Scope Specific pada Asset Name yang belum penuh diterima di batas tepat cap

21. Hapus centang `Stay on this form after submitting`
22. Ganti isi Field Name dengan `Cap Gen New {runId}-059`, lalu ganti Scope menjadi `Specific Asset Name` dengan `Generator`
23. Klik [Submit]
24. Verifikasi toast "Success, custom field has been created." tampil
25. Ketik Search `{runId}-059`, tekan Enter
26. Verifikasi tabel menampilkan tepat 1 baris `Cap Gen New {runId}-059` (field `Cap Pump New`, `Cap General New`, dan `Stay Cap` bersuffix `{runId}-059` tidak tersimpan)
27. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 191, 192, 197, 193 (urutan sumber 191, 192, 193, 197). Tiga kasus yang ditolak memakai satu modal yang sama dan Field Name serta Scope diganti (langkah 9, 15, 22) alih-alih membuka modal baru, karena penolakan karena batas mempertahankan modal dan input (Expected TC-FA-CF-191 butir b); kasus sukses (TC-FA-CF-193) paling akhir karena menutup modal dan menambah hitungan Active `Generator` (S-10). Jumlah buka form (1) sama dengan kejadian menutup (langkah 23).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 5, 13, 14, 18, 21, 25, 27, serta pengisian form dan klik tombol sebagai bagian langkah TC. Klik `[OK]` pada langkah 13 dan 18 menutup dialog sebelum kasus berikutnya; klik `[OK]` pada langkah 13 tidak ada di Langkah Uji TC-FA-CF-192.
- Langkah 26 membuktikan lewat satu baris tersimpan sebagai anchor positif bahwa tiga field yang ditolak tidak muncul; sekaligus menjadi bukti "tabel tidak berubah" pada Expected b TC-FA-CF-191.
- Klausa "sehingga `Generator` memiliki 2 field Active" pada Expected TC-FA-CF-193 adalah akibat dari satu field Active baru pada `Generator` yang sebelumnya 1 (Pre-setup #16); hitungan itu tidak diasersi terpisah karena TC tidak memberi langkah observasinya, dan keberadaan field tersimpan diasersi pada langkah 26.
- Temuan untuk QA:
  - Akun Total Control Company Cap tidak tertulis sebagai baris sendiri di Pre-setup TC (Pre-setup #1 hanya Company Alpha); ditulis "disediakan tim FE" (S-11).
  - TC-FA-CF-193: Expected hanya menyebut toast sukses dan hasil hitungan; spec mengasersi toast dan keberadaan baris tersimpan pada langkah 24 dan 26.
  - Nama field memakai suffix `{runId}-059` (S-12) sehingga tidak sama dengan `Cap Pump New`, `Cap General New`, `Cap Gen New`, dan `Stay Cap` pada Data Uji TC.
