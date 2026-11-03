---
id: TC-FA-FAAM-E2E-070-edit-sukses-multi-field-dan-isolasi-field-lain
title: "Edit Sukses: Beberapa Field Sekaligus, Satu Field Tidak Mengubah Field Lain, dan Submit Penuh"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-227
  - TC-FA-FAAM-228
  - TC-FA-FAAM-229
coverage:
  web: automated
---

# Edit Sukses: Beberapa Field Sekaligus, Satu Field Tidak Mengubah Field Lain, dan Submit Penuh

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Dinamis (salinan seed fixture #13d, Dinamis #29, #30, #31): `Edit Target Item 227 {runId}-070` (Code `ETI227`), `Edit Target Item 228 {runId}-070` (Code `ETI228`), dan `Edit Target Item 229 {runId}-070` (Code `ETI229`). Nilai yang diketik: TC-227 Asset Name `EDIT TARGET ITEM 227 {runId}-070` dan Code `ETI227-3`; TC-228 Asset Name `Edit Done Item {runId}-070`, Code `EDI`, UoM `Pcs`, Default Label `Fragile` (Pre-setup #25), Default Addon `Audit`; TC-229 Code `ETI229-5`.
- Pencarian di Modal Changelog memakai Search nama unik bersuffix sehingga baseline entri nol (S-12).
- Kemampuan teknis (disediakan tim FE/BE): seed API per TC untuk salinan fixture bernama bersuffix `{runId}-070` (Code salinan mengikuti pola TC dan tetap di bawah batas 15 karakter) dan sesi API aktor; salinan dihapus lewat id hasil seed di hook `after`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-229: Edit satu field tidak mengubah nilai field lain

1. Ketik Search `Edit Target Item 229 {runId}-070`, tekan Enter
2. Klik `⋯` baris `Edit Target Item 229 {runId}-070` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Ubah hanya Code menjadi `ETI229-5`
4. Klik `[Save]`
5. Tunggu aksi selesai (modal Edit tertutup)
6. Klik `⋯` baris `Edit Target Item 229 {runId}-070` lalu `Detail`
7. Verifikasi Detail menampilkan Code `ETI229-5`
8. Verifikasi Asset Name, Category, TAG Type, Brand, model, UoM, Default Addon, dan Default Label di Detail tidak berubah dari nilai awal salinan
9. Tutup Popup Detail

### TC-FA-FAAM-227: Perubahan field lain menyimpan seluruh submit termasuk kapitalisasi yang dikirim

10. Ganti isi kotak search dengan `Edit Target Item 227 {runId}-070`, tekan Enter
11. Klik `⋯` baris `Edit Target Item 227 {runId}-070` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
12. Ubah Asset Name menjadi `EDIT TARGET ITEM 227 {runId}-070` dan Code menjadi `ETI227-3`
13. Klik `[Save]`
14. Verifikasi toast `Success, asset name has been updated.` tampil
15. Ganti isi kotak search dengan `EDIT TARGET ITEM 227 {runId}-070`, tekan Enter
16. Verifikasi baris tampil dengan nama tersimpan `EDIT TARGET ITEM 227 {runId}-070`
17. Buka Changelog (icon Changelog) dan ketik Search `EDIT TARGET ITEM 227 {runId}-070`, tekan Enter
18. Verifikasi Changelog memuat 1 baris Edit Field `Asset Name`
19. Verifikasi Changelog memuat 1 baris Edit Field `Code`
20. Tutup Modal Changelog

### TC-FA-FAAM-228: Edit beberapa field sekaligus pada Asset Name tanpa aset berhasil

21. Ganti isi kotak search dengan `Edit Target Item 228 {runId}-070`, tekan Enter
22. Klik `⋯` baris `Edit Target Item 228 {runId}-070` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
23. Ubah Asset Name menjadi `Edit Done Item {runId}-070`, Code `EDI`, dan UoM `Pcs`
24. Tambahkan Default Label `Fragile` dan Default Addon `Audit`
25. Klik `[Save]`
26. Verifikasi toast `Success, asset name has been updated.` tampil
27. Verifikasi modal Edit tertutup
28. Ganti isi kotak search dengan `Edit Done Item {runId}-070`, tekan Enter
29. Verifikasi List menampilkan baris dengan Asset Name `Edit Done Item {runId}-070`, Code `EDI`, UoM `Pcs`, Default Label `Fragile`, dan Default Addon `Audit`
30. Buka Changelog (icon Changelog) dan ketik Search `Edit Done Item {runId}-070`, tekan Enter
31. Verifikasi Changelog memuat 1 baris Edit per field yang berubah: `Asset Name`, `Code`, `UoM`, `Default Label`, dan `Default Addon`
32. Tutup Modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1, 10, 15, 21, dan 28 untuk menemukan baris target (R-16); tunggu aksi selesai pada langkah 5 (Save tanpa toast di Expected TC-FA-FAAM-229, langkah berikutnya berpindah ke Popup Detail, bagian 8b butir 8); penutupan Popup Detail pada langkah 9; membuka dan menutup Modal Changelog pada langkah 17 sampai 20 dan 30 sampai 32.
- Changelog dicari lewat Search nama bersuffix yang unik, sehingga hanya entri milik salinan itu yang diamati (baseline nol, S-12); "entri teratas" pada Langkah Uji TC-FA-FAAM-227 dan 228 diterjemahkan menjadi entri hasil Search itu.
- Keunikan nilai Code yang diketik (batas 15 karakter tidak menyisakan ruang untuk suffix `{runId}-<NNN>`): nilai Code mengikuti TC, nomor TC membuatnya berbeda antar spec, seed salinan idempotent, cleanup hanya menghapus yang dibuat spec ini, dan suite berjalan serial (S-12).
- Temuan untuk QA:
  - TC-FA-FAAM-227 mengetik Asset Name literal `EDIT TARGET ITEM 227` tanpa suffix per run; spec menambahkan suffix ` {runId}-070` pada nilai yang diketik dan dibandingkan (S-12).
  - TC-FA-FAAM-228 Post Condition (Popup Detail dan kolom Asset Name di settings-asset-transactional-policy serta detail aset di asset/) tidak punya langkah observasi di TC; tidak diasersi.
  - TC-FA-FAAM-228 Expected b menulis satu butir "List menampilkan baris dengan nilai baru" berisi lima nilai; spec mengasersinya sebagai satu verifikasi baris.
