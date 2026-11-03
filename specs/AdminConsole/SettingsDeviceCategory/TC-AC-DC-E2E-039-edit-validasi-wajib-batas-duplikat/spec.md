---
id: TC-AC-DC-E2E-039-edit-validasi-wajib-batas-duplikat
title: "Edit Category: Validasi Nama Wajib, Batas 121 Karakter, Nama Reserved, dan Duplikat Saat Mengetik"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DC-101
  - TC-AC-DC-103
  - TC-AC-DC-111
  - TC-AC-DC-107
coverage:
  web: automated
---

# Edit Category: Validasi Nama Wajib, Batas 121 Karakter, Nama Reserved, dan Duplikat Saat Mengetik

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, di bawah `Handheld Reader`; nama bersuffix `{runId}-039`): `Pemindai {runId}-039` (target Edit; namanya tidak berubah selama spec) dan `Saudara {runId}-039` (sibling yang namanya diduplikasi pada TC-107). Hook `after` menghapus keduanya lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Nilai uji: nama 121 karakter `Fixture.settingsDeviceCategory.name121` (TC-103, diblokir sehingga tidak tersimpan dan tidak bersuffix); `All Categories` dan `  ALL CATEGORIES  ` (TC-111).
- Kemampuan teknis: jumlah baris hasil Search pada modal Changelog dapat dibaca sebagai baseline sebelum aksi (disediakan tim FE/BE).

## Test Steps

### Baseline Changelog

1. Expand `Hardware` lalu `Handheld Reader`
2. Klik ikon Changelog pada header Sidebar Category
3. Ketik Search `{runId}-039`, tekan Enter
4. Catat jumlah baris hasil Search sebagai baseline (entri hasil seeding)
5. Klik `[×]` pada modal Changelog

### Nama dikosongkan (TC-101)

6. Hover node `Pemindai {runId}-039`, klik aksi Edit
7. Klik `[Clear Field]`, klik `[Save]`
8. Verifikasi pesan error inline "Category name must not be empty"
9. Verifikasi input tetap terbuka
10. Verifikasi tidak ada toast

### Nama 121 karakter (TC-103)

11. Ganti isi input dengan nama 121 karakter
12. Verifikasi pesan error inline "Max. 120 characters" tampil langsung saat melebihi batas
13. Klik `[Save]`
14. Verifikasi tidak ada toast

### Nama All Categories direservasi (TC-111)

15. Ganti isi input dengan `All Categories`, klik `[Save]`
16. Verifikasi pesan error inline "'All Categories' is a reserved name and cannot be used"
17. Klik `[Clear Field]`
18. Ganti isi input dengan `  ALL CATEGORIES  `, klik `[Save]`
19. Verifikasi pesan error inline "'All Categories' is a reserved name and cannot be used"

### Duplikat dengan sibling saat mengetik (TC-107)

20. Klik `[Clear Field]`
21. Ketik `Saudara {runId}-039`, tunggu 1 detik tanpa memindahkan fokus
22. Verifikasi pesan error inline "Category name already exists" tampil sekitar 500ms setelah berhenti mengetik
23. Klik `[Save]`
24. Verifikasi tidak ada toast

### Pemulihan dan pemeriksaan akhir

25. Klik `[Clear Field]`, ketik ulang `Pemindai {runId}-039`, tekan Esc
26. Verifikasi nama node tetap `Pemindai {runId}-039`
27. Klik ikon Changelog pada header Sidebar Category
28. Ketik Search `{runId}-039`, tekan Enter
29. Verifikasi jumlah baris hasil Search sama dengan baseline
30. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1 (membuka cabang tree), langkah 5 dan 30 (menutup modal Changelog), langkah 17 dan 20 (`[Clear Field]` sebagai pembersih error sebelum kasus berikutnya, R-12), langkah 25 (mengembalikan input ke nilai tersimpan sehingga input bersih lalu menutupnya tanpa dialog, S-09). Satu pembukaan input Edit dipakai untuk seluruh kasus tanpa Save sukses.
- S-05: klausa "nama node tidak berubah dan tidak ada entri log" pada TC-101, TC-103, TC-111, TC-107 dinyatakan sebagai asersi jumlah dengan baseline (langkah 4, 26, 29), bukan asersi absence kelas g, karena tidak ada kasus yang berhasil menyimpan.
- Temuan untuk QA:
  - TC memakai node literal Pre-setup #14 `Rugged Scanner` sebagai target Edit dan `Barcode Handheld` sebagai sibling duplikat. Spec memakai node milik spec `Pemindai {runId}-039` dan `Saudara {runId}-039`.
  - TC-103 tidak menyebut apakah `[Save]` pada nama 121 karakter menampilkan ulang pesan; spec hanya mengasersi tidak adanya toast (langkah 14).
