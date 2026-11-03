---
id: TC-AC-DC-E2E-049-delete-berhasil-leaf-dan-state-submitting
title: "Delete Category: Berhasil pada Leaf, State Submitting, dan Klik Ganda pada Family"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-129
  - TC-AC-DC-142
  - TC-AC-DC-143
coverage:
  web: automated
---

# Delete Category: Berhasil pada Leaf, State Submitting, dan Klik Ganda pada Family

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, di bawah `Handheld Reader`; nama bersuffix `{runId}-049`; tanpa Device Name pengacu): `Daun {runId}-049` (leaf; TC-129), `Daun Lambat {runId}-049` (leaf; TC-143), dan family `Induk Fam {runId}-049F` dengan anak `Anak A Fam {runId}-049F` (leaf) dan `Anak B Fam {runId}-049F`, serta cucu `Cucu Fam {runId}-049F` di bawah `Anak B Fam {runId}-049F` (TC-142). Seluruh node dihapus oleh langkah spec; hook `after` menghapus sisa node yang belum terhapus (bila spec gagal di tengah) lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Kemampuan teknis: `Spectra.intercept()` menahan respons endpoint delete Category selama 3 detik pada TC-143 (penundaan jaringan, bukan kegagalan) dan dilepas segera sesudahnya. Search pada modal Changelog dipakai untuk menemukan entri berdasarkan nama bersuffix unik (baseline nol untuk entri `Delete`).

## Test Steps

### Delete leaf berhasil (TC-129)

1. Expand `Hardware` lalu `Handheld Reader`
2. Hover node `Daun {runId}-049`, klik aksi Delete
3. Klik `[Delete]` pada dialog konfirmasi
4. Verifikasi toast sukses "Success, category has been deleted."
5. Verifikasi dialog tertutup
6. Verifikasi node `Daun {runId}-049` hilang dari tree
7. Klik ikon Changelog pada header Sidebar Category
8. Ketik Search `Daun {runId}-049`, tekan Enter
9. Verifikasi satu entri dengan Action `Delete` untuk Category `Daun {runId}-049`
10. Klik `[×]` pada modal Changelog

### State Submitting pada Delete (TC-143)

11. Tahan respons endpoint delete Category selama 3 detik
12. Hover node `Daun Lambat {runId}-049`, klik aksi Delete
13. Klik `[Delete]` pada dialog konfirmasi
14. Verifikasi tombol `[Delete]` dalam state disabled selama respons tertunda
15. Verifikasi tombol dialog lain dalam state disabled selama respons tertunda
16. Verifikasi indikator loading tampil selama respons tertunda
17. Lepas tahanan respons endpoint delete Category
18. Verifikasi dialog tertutup
19. Verifikasi toast sukses "Success, category has been deleted."

### Klik ganda cepat pada Delete family (TC-142)

20. Tunggu toast lama hilang otomatis (toast sukses dari blok sebelumnya)
21. Hover node `Induk Fam {runId}-049F`, klik aksi Delete
22. Klik `[Delete]` pada dialog konfirmasi dua kali dengan sangat cepat
23. Verifikasi hanya satu toast sukses "Success, category has been deleted."
24. Verifikasi family `Induk Fam {runId}-049F` hilang dari tree
25. Klik ikon Changelog pada header Sidebar Category
26. Ketik Search `{runId}-049F`, tekan Enter
27. Verifikasi tepat empat entri dengan Action `Delete` untuk Category `Induk Fam {runId}-049F`, `Anak A Fam {runId}-049F`, `Anak B Fam {runId}-049F`, dan `Cucu Fam {runId}-049F`, masing-masing satu kali
28. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1 (membuka cabang tree), langkah 10 dan 28 (menutup modal Changelog), langkah 11 dan 17 (memasang dan melepas tahanan respons), langkah 20 (menunggu toast lama hilang agar hitungan "hanya satu toast" bermakna, R-12). Search pada modal Changelog (langkah 8, 26) menemukan entri berdasarkan nama bersuffix unik.
- Urutan TC dalam spec: TC-129 lebih dulu, TC-143 kedua, lalu TC-142 (family) terakhir karena aksi menghapus family ditaruh di akhir (S-10).
- Temuan untuk QA:
  - TC memakai node literal Pre-setup #14 `Hapus Daun` dan `Hapus Keluarga` sebagai target Delete dan menyebut Device Name Pre-setup #15 sebagai precondition tanpa memakainya pada langkah atau Expected. Spec memakai node milik spec dan tidak memakai Device Name Pre-setup #15.
  - Post Condition TC-129 (opsi Category pada form Device Name tidak lagi memuat node, entri pada System Log dan Activity Log, konsumen read) tidak diasersi karena TC tidak memberi langkah observasinya (S-01).
  - Entri Changelog family pada TC-142 diasersi sebagai Expected "empat entri Delete tercatat tepat satu kali"; TC tidak menyebut urutan entri sehingga spec tidak mengasersi urutan.
