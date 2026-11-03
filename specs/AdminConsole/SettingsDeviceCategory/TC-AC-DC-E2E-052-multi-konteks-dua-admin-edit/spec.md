---
id: TC-AC-DC-E2E-052-multi-konteks-dua-admin-edit
title: "Dua Admin: Edit saat Node Dihapus dan Edit Bersamaan pada Node yang Sama"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DC-122
  - TC-AC-DC-123
coverage:
  web: automated
---

# Dua Admin: Edit saat Node Dihapus dan Edit Bersamaan pada Node yang Sama

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Admin kedua (Pre-setup #9, Maya Putri, Total Control Principal): `totalControlDevCat2_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DC_TC2_PASSWORD` (nama env baru; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`, satu arti: password Total Control kedua Admin Console Settings Device Category). Admin kedua bertindak lewat sesi API aktor (hanya memicu perubahan state; tidak ada konteks UI kedua).
- Login akun aktor pertama di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, di bawah `Handheld Reader`; nama bersuffix `{runId}-052`): `Daun {runId}-052` (leaf; TC-122, dihapus admin kedua), `Pemindai {runId}-052` (leaf; TC-123, diubah admin kedua menjadi `Nama Admin Dua {runId}-052` lalu oleh aktor menjadi `Nama Admin Satu {runId}-052`). Hook `after` menghapus sisa node milik spec lewat sesi API. Entri Changelog hasil seeding, aksi admin kedua, dan cleanup bersifat permanen dan tidak dihapus.
- Kemampuan teknis: Search pada modal Changelog dipakai untuk menemukan entri berdasarkan nama bersuffix unik.

## Test Steps

### Node dihapus admin lain sebelum Save (TC-122)

1. Expand `Hardware` lalu `Handheld Reader`
2. Hover node `Daun {runId}-052`, klik aksi Edit
3. Ubah nilai menjadi `Daun Baru {runId}-052` tetapi belum klik `[Save]`
4. Admin kedua (sesi API) menghapus node `Daun {runId}-052` hingga terhapus
5. Tunggu aksi admin kedua selesai
6. Klik `[Save]`
7. Verifikasi toast netral "This category is no longer available."
8. Verifikasi tidak ada toast error terpisah
9. Verifikasi input ditutup
10. Verifikasi tree di-refresh sehingga `Daun {runId}-052` tidak lagi tampil
11. Verifikasi `Hardware` dan `Handheld Reader` tetap ter-expand
12. Klik ikon Changelog pada header Sidebar Category
13. Ketik Search `Daun Baru {runId}-052`, tekan Enter
14. Verifikasi empty state "No results found" (tidak ada entri `Edit` untuk `Daun Baru {runId}-052`)
15. Klik `[×]` pada modal Changelog

### Edit-vs-Edit pada node yang sama (TC-123)

16. Hover node `Pemindai {runId}-052`, klik aksi Edit
17. Ubah nilai menjadi `Nama Admin Satu {runId}-052` tetapi belum klik `[Save]`
18. Admin kedua (sesi API) mengubah nama `Pemindai {runId}-052` menjadi `Nama Admin Dua {runId}-052` hingga tersimpan
19. Tunggu aksi admin kedua selesai
20. Klik `[Save]`
21. Verifikasi toast sukses "Success, category has been updated."
22. Verifikasi tidak ada dialog konflik versi
23. Verifikasi nama akhir node adalah `Nama Admin Satu {runId}-052`
24. Klik ikon Changelog pada header Sidebar Category
25. Ketik Search `Nama Admin Dua {runId}-052`, tekan Enter
26. Verifikasi ada entri `Edit` dengan Old Value `Pemindai {runId}-052` dan New Value `Nama Admin Dua {runId}-052`
27. Verifikasi ada entri `Edit` dengan Old Value `Nama Admin Dua {runId}-052` dan New Value `Nama Admin Satu {runId}-052`
28. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1 (membuka cabang tree), langkah 5 dan 19 (menunggu aksi admin kedua selesai sebelum aksi sesi pertama), langkah 15 dan 28 (menutup modal Changelog). Search pada modal Changelog (langkah 13, 25) menemukan entri berdasarkan nama bersuffix unik.
- Pelaku kedua memakai sesi API pada langkah 4 dan 18 karena hanya memicu perubahan state dan hasil di sesi itu tidak diasersi.
- Pembagian TC lintas spec: TC-281 (Edit ke nama yang baru dibuat admin lain, memakai konteks browser kedua) ada di spec 094.
- S-05: klausa "tidak ada entri Edit" pada TC-122 dinyatakan sebagai asersi nama bersuffix unik dengan baseline nol (langkah 14), bukan asersi absence kelas g.
- Temuan untuk QA:
  - TC memakai node literal Pre-setup #14 `Hapus Daun` dan `Rugged Scanner`. Spec memakai node milik spec bersuffix `{runId}-052`.
  - TC-123 menyebut "dua entri Edit berurutan"; kolom Date berketelitian menit sehingga spec mengasersi kedua pasangan Old/New tanpa mengasersi urutan.
  - TC-122 dan TC-123 ditandai `Manual Only (d)`; dua pelaku tidak menghambat penulisan.
