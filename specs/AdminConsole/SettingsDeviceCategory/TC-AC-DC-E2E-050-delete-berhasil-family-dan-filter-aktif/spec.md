---
id: TC-AC-DC-E2E-050-delete-berhasil-family-dan-filter-aktif
title: "Delete Category: Node Filter Terhapus, Parent Kehilangan Anak Terakhir, dan Family Tiga Level"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-145
  - TC-AC-DC-304
  - TC-AC-DC-130
coverage:
  web: automated
---

# Delete Category: Node Filter Terhapus, Parent Kehilangan Anak Terakhir, dan Family Tiga Level

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` menghapus sisa node milik spec lalu mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup yang hanya dibaca dan tidak diubah: pohon #14 node `Hardware`, `Handheld Reader`, `Filter Induk` > `Filter Anak 1`; Device Name Pre-setup #15 `HR-100` (Category `Dipakai Leaf`), `FN-1` (`Filter Anak 1`), dan Device Name lain pada tabel sebagai pembanding "seluruh data". Nama node dan Device Name dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, di bawah `Handheld Reader`; nama bersuffix `{runId}-050`; tanpa Device Name pengacu): `Daun Filter {runId}-050` (leaf; TC-145); `Cabang {runId}-050` dengan anak tunggal `Anak Tunggal {runId}-050` yang punya anak tunggal `Cucu Tunggal {runId}-050` (TC-304); family `Induk Fam {runId}-050F` dengan anak `Anak A Fam {runId}-050F` (leaf) dan `Anak B Fam {runId}-050F`, serta cucu `Cucu Fam {runId}-050F` di bawah `Anak B Fam {runId}-050F`, dan sibling `Saudara {runId}-050` (leaf; TC-130). Node yang dihapus oleh langkah spec tidak dihapus ulang; hook `after` menghapus sisa node (`Cabang {runId}-050` beserta anaknya dan `Saudara {runId}-050`) lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Kemampuan teknis: pembaca tabel Device Name untuk menentukan baris yang tampil (nama Device Name Pre-setup #15); spec hanya membaca tabel. Search pada tabel tidak dipakai.

## Test Steps

### Delete node yang sedang menjadi filter (TC-145)

1. Expand `Hardware` lalu `Handheld Reader`
2. Klik node `Daun Filter {runId}-050`
3. Hover node `Daun Filter {runId}-050`, klik aksi Delete
4. Klik `[Delete]` pada dialog konfirmasi
5. Verifikasi toast sukses "Success, category has been deleted."
6. Verifikasi tidak ada node yang tercentang pada tree (pilihan filter kosong)
7. Verifikasi tabel Device Name menampilkan seluruh data (sedikitnya Device Name `HR-100` dan `FN-1` tampil)
8. Verifikasi tidak ada partial-check yang tertinggal pada node mana pun

### Parent kehilangan anak terakhir lewat Delete (TC-304)

9. Tunggu toast sukses dari blok sebelumnya hilang otomatis
10. Expand `Cabang {runId}-050`, `Anak Tunggal {runId}-050`, dan `Filter Induk`
11. Centang kotak `Anak Tunggal {runId}-050` dan kotak `Filter Anak 1`
12. Hover node `Cucu Tunggal {runId}-050`, klik aksi Delete
13. Klik `[Delete]` pada dialog konfirmasi
14. Verifikasi toast sukses "Success, category has been deleted."
15. Verifikasi node `Cucu Tunggal {runId}-050` terhapus
16. Verifikasi node `Anak Tunggal {runId}-050` menjadi leaf
17. Verifikasi kotak `Anak Tunggal {runId}-050` tidak tercentang
18. Verifikasi pilihan `Filter Anak 1` tetap tercentang
19. Verifikasi tabel Device Name hanya menampilkan `FN-1`
20. Klik kotak `Filter Anak 1` untuk mengosongkan pilihan

### Family tiga level dihapus atomik (TC-130)

21. Tunggu toast sukses dari blok sebelumnya hilang otomatis
22. Hover node `Induk Fam {runId}-050F`, klik aksi Delete
23. Klik `[Delete]` pada dialog konfirmasi
24. Verifikasi toast sukses "Success, category has been deleted."
25. Verifikasi `Induk Fam {runId}-050F`, `Anak A Fam {runId}-050F`, `Anak B Fam {runId}-050F`, dan `Cucu Fam {runId}-050F` seluruhnya hilang dari tree
26. Verifikasi node sibling `Saudara {runId}-050` tidak berubah

## Notes

- S-03, langkah penghubung: langkah 1 dan 10 (membuka cabang tree), langkah 9 dan 21 (menunggu toast lama hilang), langkah 20 (mengosongkan pilihan filter `Filter Anak 1` sebelum TC berikutnya, S-09).
- Urutan TC dalam spec: TC-145, TC-304, lalu TC-130 (family tiga level) terakhir karena aksi menghapus family ditaruh di akhir (S-10).
- Temuan untuk QA:
  - TC memakai node literal Pre-setup #14 `Hapus Daun`, `Hapus Keluarga`, `Hapus Keluarga Anak B`, dan `Hapus Keluarga Cucu` sebagai target Delete. Spec memakai node milik spec bersuffix `{runId}-050`; pilihan filter kedua `Filter Anak 1` (Device Name `FN-1`) memakai node Pre-setup yang hanya dibaca dan asersi TC-304 bergantung pada nama literal `Filter Anak 1` dan `FN-1`.
  - TC-304 menyebut kotak `Hapus Keluarga Anak B` tercentang sebelum Delete cucunya; spec mengasersi kotak `Anak Tunggal {runId}-050` tidak tercentang setelah Delete sesuai Expected b.
  - Post Condition TC-130 (empat entri Delete, opsi Category pada form Device Name, konsumen read) tidak diasersi karena TC tidak memberi langkah observasinya (S-01). Entri Delete family diasersi di spec 049 (TC-142).
