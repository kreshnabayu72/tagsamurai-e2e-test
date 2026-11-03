---
id: TC-AC-DC-E2E-038-edit-case-only-submitting-dan-klik-ganda
title: "Edit Category: Perubahan Huruf Besar-Kecil Saja, State Submitting, dan Klik Ganda Save"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DC-114
  - TC-AC-DC-124
  - TC-AC-DC-125
coverage:
  web: automated
---

# Edit Category: Perubahan Huruf Besar-Kecil Saja, State Submitting, dan Klik Ganda Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, di bawah `Handheld Reader`; nama bersuffix `{runId}-038`): `Pemindai {runId}-038` (leaf). Nama node berubah berurutan menjadi `Pemindai Lambat {runId}-038` (TC-124) lalu `Pemindai Ganda {runId}-038` (TC-125); hook `after` menghapus node dengan nama terakhir itu lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Kemampuan teknis: `Spectra.intercept()` menahan respons endpoint update Category selama 3 detik pada TC-124 (penundaan jaringan, bukan kegagalan) dan dilepas segera sesudahnya. Jumlah baris hasil Search pada modal Changelog dapat dibaca sebagai baseline sebelum aksi (disediakan tim FE/BE). Search pada modal Changelog dipakai untuk menemukan entri berdasarkan nama bersuffix unik.

## Test Steps

### Save yang hanya mengubah huruf besar-kecil (TC-114)

1. Expand `Hardware` lalu `Handheld Reader`
2. Klik ikon Changelog pada header Sidebar Category
3. Ketik Search `{runId}-038`, tekan Enter
4. Catat jumlah baris hasil Search sebagai baseline (entri hasil seeding)
5. Klik `[×]` pada modal Changelog
6. Hover node `Pemindai {runId}-038`, klik aksi Edit
7. Ganti isi input dengan `pemindai {runId}-038`, klik `[Save]`
8. Verifikasi toast netral "No changes to save."
9. Verifikasi nama node tetap `Pemindai {runId}-038`
10. Klik ikon Changelog pada header Sidebar Category
11. Ketik Search `{runId}-038`, tekan Enter
12. Verifikasi jumlah baris hasil Search sama dengan baseline
13. Klik `[×]` pada modal Changelog

### State Submitting pada Edit (TC-124)

14. Tahan respons endpoint update Category selama 3 detik
15. Hover node `Pemindai {runId}-038`, klik aksi Edit
16. Ganti isi input dengan `Pemindai Lambat {runId}-038`, klik `[Save]`
17. Verifikasi input dalam state disabled selama respons tertunda
18. Verifikasi tombol `[Save]` dan `[Clear Field]` dalam state disabled selama respons tertunda
19. Verifikasi indikator loading tampil selama respons tertunda
20. Lepas tahanan respons endpoint update Category
21. Verifikasi toast sukses "Success, category has been updated."
22. Verifikasi input tertutup

### Klik ganda cepat pada Save (TC-125)

23. Tunggu toast lama hilang otomatis (toast sukses dari blok sebelumnya)
24. Hover node `Pemindai Lambat {runId}-038`, klik aksi Edit
25. Ganti isi input dengan `Pemindai Ganda {runId}-038`, klik `[Save]` dua kali dengan sangat cepat
26. Verifikasi nama node berubah menjadi `Pemindai Ganda {runId}-038` sekali
27. Verifikasi hanya satu toast sukses "Success, category has been updated."
28. Klik ikon Changelog pada header Sidebar Category
29. Ketik Search `Pemindai Ganda {runId}-038`, tekan Enter
30. Verifikasi hanya satu entri `Edit` untuk Category `Pemindai Ganda {runId}-038`
31. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1 (membuka cabang tree), langkah 5, 13, 31 (menutup modal Changelog), langkah 14 dan 20 (memasang dan melepas tahanan respons), langkah 23 (menunggu toast lama hilang agar hitungan "hanya satu toast" bermakna, R-12). Search pada modal Changelog (langkah 3, 11, 29) menemukan entri berdasarkan nama bersuffix unik.
- S-05: klausa "tidak ada entri log baru" pada TC-114 dinyatakan sebagai asersi jumlah dengan baseline (langkah 4 dan 12), bukan asersi absence kelas g.
- Temuan untuk QA:
  - TC-114 mengharapkan tidak ada entri baru di Changelog, System Log, dan Activity Log, tetapi TC tidak memberi langkah membuka System Log dan Activity Log. Spec hanya mengasersi Changelog (langkah 12).
  - TC memakai node literal Pre-setup #14 `Rugged Scanner` sebagai target Edit. Spec memakai `Pemindai {runId}-038` milik spec.
  - Nilai "dua klik cepat" pada TC-125 tidak menyebut selang antar klik; spec memakai dua klik berurutan tanpa jeda buatan.
