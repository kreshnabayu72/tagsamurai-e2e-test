---
id: TC-AC-DC-E2E-055-multi-konteks-dua-admin-delete-ganda
title: "Dua Admin: Delete pada Node yang Sudah Dihapus Admin Lain dan Permintaan Delete Kedua dari Tab Lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DC-140
  - TC-AC-DC-141
coverage:
  web: automated
---

# Dua Admin: Delete pada Node yang Sudah Dihapus Admin Lain dan Permintaan Delete Kedua dari Tab Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Admin kedua (Pre-setup #9, Maya Putri, Total Control Principal): `totalControlDevCat2_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DC_TC2_PASSWORD` (nama env baru; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`, satu arti: password Total Control kedua Admin Console Settings Device Category). Pada TC-140 admin kedua bertindak lewat sesi API aktor (hanya memicu perubahan state). TC-141 memakai dua tab browser pada sesi akun aktor yang sama (bukan admin kedua).
- Login akun aktor pertama di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` menutup tab kedua bila masih terbuka dan mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, di bawah `Handheld Reader`; nama bersuffix `{runId}-055`; tanpa Device Name pengacu): `Daun A {runId}-055` (leaf; TC-140, dihapus admin kedua) dan `Daun B {runId}-055` (leaf; TC-141, dihapus dari tab pertama). Seluruh node dihapus oleh langkah spec; hook `after` menghapus sisa node yang belum terhapus lewat sesi API. Entri Changelog hasil seeding, aksi admin kedua, dan cleanup bersifat permanen dan tidak dihapus.
- Kemampuan teknis: membuka tab browser kedua pada sesi yang sama (TC-141) disediakan tim FE. Search pada modal Changelog dipakai untuk menemukan entri berdasarkan nama bersuffix unik.

## Test Steps

### Delete saat node sudah dihapus admin lain (TC-140)

1. Expand `Hardware` lalu `Handheld Reader`
2. Hover node `Daun A {runId}-055`, klik aksi Delete
3. Admin kedua (sesi API) menghapus node `Daun A {runId}-055` hingga terhapus
4. Tunggu aksi admin kedua selesai
5. Klik `[Delete]` pada dialog konfirmasi
6. Verifikasi toast netral "This category is no longer available."
7. Verifikasi tree di-refresh dan `Daun A {runId}-055` tidak ada
8. Verifikasi `Hardware` dan `Handheld Reader` tetap ter-expand
9. Verifikasi tidak ada toast error
10. Klik ikon Changelog pada header Sidebar Category
11. Ketik Search `Daun A {runId}-055`, tekan Enter
12. Verifikasi tepat satu entri dengan Action `Delete` untuk Category `Daun A {runId}-055` (dari admin kedua)
13. Klik `[×]` pada modal Changelog

### Permintaan Delete kedua dari tab lain (TC-141)

14. Tunggu toast netral dari blok sebelumnya hilang otomatis
15. Buka tab browser kedua pada sesi yang sama, buka Settings > Device > Device Name, lalu expand `Hardware` dan `Handheld Reader`, dan jangan muat ulang tab kedua
16. Kembali ke tab pertama
17. Hover node `Daun B {runId}-055`, klik aksi Delete
18. Klik `[Delete]` pada dialog konfirmasi
19. Verifikasi toast sukses "Success, category has been deleted." pada tab pertama
20. Pindah ke tab kedua
21. Hover node `Daun B {runId}-055`, klik aksi Delete
22. Klik `[Delete]` pada dialog konfirmasi
23. Verifikasi toast netral "This category is no longer available." pada tab kedua
24. Verifikasi tree di-refresh pada tab kedua dan `Daun B {runId}-055` tidak ada
25. Tutup tab kedua dan kembali ke tab pertama
26. Klik ikon Changelog pada header Sidebar Category
27. Ketik Search `Daun B {runId}-055`, tekan Enter
28. Verifikasi tepat satu entri dengan Action `Delete` untuk Category `Daun B {runId}-055`
29. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1 (membuka cabang tree), langkah 4 (menunggu aksi admin kedua selesai sebelum aksi sesi pertama), langkah 13 dan 29 (menutup modal Changelog), langkah 14 (menunggu toast lama hilang), langkah 15, 16, 20, 25 (membuka, berpindah, dan menutup tab kedua untuk TC-141). Search pada modal Changelog (langkah 11, 27) menemukan entri berdasarkan nama bersuffix unik.
- Pelaku kedua memakai sesi API pada langkah 3 karena hanya memicu perubahan state dan hasil di sesi itu tidak diasersi. Tab kedua pada TC-141 adalah konteks UI kedua yang diasersi (langkah 23 dan 24).
- Klausa "tidak ada entri Delete tambahan; state akhir sama dengan satu kali Delete" (TC-140 dan TC-141) dinyatakan sebagai asersi jumlah tepat satu entri `Delete` (langkah 12 dan 28), bukan asersi absence kelas g.
- Temuan untuk QA:
  - TC memakai node literal Pre-setup #14 `Hapus Daun`. Spec memakai `Daun A {runId}-055` dan `Daun B {runId}-055` milik spec.
  - TC-140 dan TC-141 ditandai `Manual Only (d)`; dua pelaku tidak menghambat penulisan.
