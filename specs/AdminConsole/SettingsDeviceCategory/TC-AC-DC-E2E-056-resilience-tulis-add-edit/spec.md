---
id: TC-AC-DC-E2E-056-resilience-tulis-add-edit
title: "Resilience: Gagal Memuat Tree, Kegagalan Server saat Add, dan Kegagalan Server saat Edit"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DC-13
  - TC-AC-DC-97
  - TC-AC-DC-126
coverage:
  web: automated
---

# Resilience: Gagal Memuat Tree, Kegagalan Server saat Add, dan Kegagalan Server saat Edit

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; hanya respons endpoint yang dipaksa gagal yang diganti, selebihnya backend nyata).
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` melepas intercept yang masih terpasang dan mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, di bawah `Handheld Reader`; nama bersuffix `{runId}-056`): `Induk {runId}-056` dengan satu anak `Anak Awal {runId}-056` (target Add; pembanding) dan `Pemindai {runId}-056` (leaf; target Edit, namanya tidak berubah). Hook `after` menghapus ketiganya lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Kemampuan teknis: `Spectra.intercept()` memaksa error 500 pada endpoint tree Category (TC-13), endpoint create Category (TC-97), dan endpoint update Category (TC-126); masing-masing intercept dilepas segera setelah pemicunya selesai (nama endpoint diambil tim FE dari `openapi.yaml` dan `low-level-design.md` modul; tidak dikarang di spec ini). Jumlah baris hasil Search pada modal Changelog dapat dibaca sebagai baseline sebelum aksi (disediakan tim FE/BE).
- Jeda nyata 5 detik (pilihan spec, bukan nilai TC) dipakai untuk mengamati bahwa toast error tidak hilang otomatis.

## Test Steps

### Gagal memuat tree (TC-13)

1. Paksa endpoint tree Category mengembalikan error 500
2. Muat ulang halaman Settings > Device > Device Name
3. Verifikasi area tree menampilkan pesan "Unable to load this data."
4. Verifikasi tidak ada tombol `[Try Again]` pada area tree
5. Verifikasi tidak ada ilustrasi empty state "No results found" pada area tree
6. Lepas paksaan error endpoint tree Category
7. Muat ulang halaman Settings > Device > Device Name

### Baseline Changelog

8. Expand `Hardware` lalu `Handheld Reader`
9. Klik ikon Changelog pada header Sidebar Category
10. Ketik Search `{runId}-056`, tekan Enter
11. Catat jumlah baris hasil Search sebagai baseline (entri hasil seeding)
12. Klik `[×]` pada modal Changelog

### Kegagalan server saat Add (TC-97)

13. Paksa endpoint create Category mengembalikan error 500
14. Hover node `Induk {runId}-056`, klik aksi `+ Subcategory`
15. Ketik `Pemindai Gagal {runId}-056`, klik `[Submit]`
16. Verifikasi toast error "Error, failed to create category."
17. Tunggu 5 detik tanpa menutup toast
18. Verifikasi toast error masih tampil sampai ditutup manual
19. Verifikasi input inline Add tetap terbuka dengan nilai `Pemindai Gagal {runId}-056`
20. Verifikasi tombol `[Submit]` aktif kembali
21. Lepas paksaan error endpoint create Category
22. Klik tombol tutup pada toast error
23. Klik `[Clear Field]`, tekan Esc

### Kegagalan server saat Edit (TC-126)

24. Paksa endpoint update Category mengembalikan error 500
25. Hover node `Pemindai {runId}-056`, klik aksi Edit
26. Ubah nilai menjadi `Pemindai Gagal {runId}-056`, klik `[Save]`
27. Verifikasi toast error "Error, failed to update category."
28. Tunggu 5 detik tanpa menutup toast
29. Verifikasi toast error masih tampil sampai ditutup manual
30. Verifikasi input Edit tetap terbuka dengan nilai `Pemindai Gagal {runId}-056`
31. Verifikasi tombol `[Save]` aktif kembali
32. Lepas paksaan error endpoint update Category
33. Klik tombol tutup pada toast error
34. Klik `[Clear Field]`, ketik ulang `Pemindai {runId}-056`, tekan Esc
35. Verifikasi nama node tetap `Pemindai {runId}-056`

### Pemeriksaan akhir tidak ada node dan tidak ada entri baru

36. Verifikasi `Induk {runId}-056` hanya memuat anak `Anak Awal {runId}-056`
37. Klik ikon Changelog pada header Sidebar Category
38. Ketik Search `{runId}-056`, tekan Enter
39. Verifikasi jumlah baris hasil Search sama dengan baseline
40. Klik `[×]` pada modal Changelog

## Notes

- Spec ini melewati sekitar 35 langkah (40). Ketiga TC adalah blok resilience satu kelas harness (kelas b, intercept parsial) yang berdiri sendiri, memakai data milik masing-masing, dan pemeriksaan akhir mengonsolidasikan asersi "tidak ada node dan tidak ada entri log" satu kali; kegagalan satu blok tidak membuat blok lain kehilangan makna. Satu spec resilience untuk Add dan Edit mengikuti prinsip penggabungan kelas ringan per modul.
- S-03, langkah penghubung: langkah 1, 6, 13, 21, 24, 32 (memasang dan melepas paksaan error endpoint segera setelah pemicunya selesai, S-09), langkah 7 (memuat ulang halaman setelah intercept tree dilepas), langkah 8 (membuka cabang tree), langkah 12 dan 40 (menutup modal Changelog), langkah 17 dan 28 (jeda 5 detik pilihan spec untuk mengamati toast yang tidak hilang otomatis), langkah 22 dan 33 (menutup toast error manual), langkah 23 dan 34 (memulihkan input ke keadaan bersih lalu menutupnya tanpa dialog).
- S-05: klausa "tidak ada node baru dan tidak ada entri log" pada TC-97 dan TC-126 dinyatakan sebagai asersi jumlah dengan baseline (langkah 11, 36, 39), bukan asersi absence kelas g.
- Temuan untuk QA:
  - TC memakai node literal Pre-setup #14 `Rugged Scanner` sebagai induk Add dan target Edit. Spec memakai node milik spec bersuffix `{runId}-056`.
  - TC-13 tidak menyebut apakah halaman perlu dimuat ulang untuk memicu kegagalan tree; spec memasang paksaan error lalu memuat ulang halaman.
  - TC-97 dan TC-126 mengharapkan toast error "tetap tampil sampai ditutup manual" tanpa menyebut cara menutupnya; spec memakai tombol tutup pada toast.
