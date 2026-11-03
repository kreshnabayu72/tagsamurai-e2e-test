---
id: TC-FA-LIC-E2E-101-changelog-allocation-quota-setup-column-pin-reset-x-esc
title: "Setup Column Modal Changelog Allocation Quota: Pin dan Unpin per Kolom, Reset to Default, Tutup X atau Esc, dan Satu Kolom Tersisa"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-353
  - TC-FA-LIC-354
  - TC-FA-LIC-355
  - TC-FA-LIC-356
coverage:
  web: automated
---

# Setup Column Modal Changelog Allocation Quota: Pin dan Unpin per Kolom, Reset to Default, Tutup X atau Esc, dan Satu Kolom Tersisa

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup, pemulihan konfigurasi kolom): dinyatakan sekali di `suite.md`; spec ini merujuknya. Spec ini menyimpan konfigurasi Setup Column modal Changelog Allocation Quota; hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`).
- Data Pre-setup (hanya dibaca; fixture BE pemulih riwayat memulihkannya di hook `before` dan `after`): riwayat Changelog Allocation Quota #27 (6 entri) lewat `Fixture.fixedAssetLicense.changelogAllocationQuota` (fixture belum ada, disediakan tim FE). Kolom default (urutan awal, semua tercentang): Date, Action, Group Name, Field, Old Value, New Value, Modified By.
- Tabel kolom Setup Column (dipakai langkah 3 sampai 13): Date, Action, Group Name, Field, Old Value, New Value, Modified By.
- Kemampuan teknis: viewport browser disempitkan pada langkah 2 sehingga tabel Changelog dapat digeser horizontal (pilihan spec; TC hanya menulis "geser tabel horizontal") dan dipulihkan pada langkah 14; disediakan tim FE untuk asersi pembekuan kolom.
- State yang diubah spec: konfigurasi kolom tersimpan (pin, visibilitas, urutan); dipulihkan per iterasi (Unpin) dan oleh blok `[Reset to Default]` serta hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka tab Allocation Quota pada node All Groups, klik ikon Changelog pada toolbar Level 1 Groups Quota

### TC-FA-LIC-353: Pin dan Unpin per kolom Hideable Visible default

2. Sempitkan viewport browser sehingga tabel dapat digeser horizontal

Untuk setiap baris tabel "Tabel kolom Setup Column" (langkah 3 sampai 13):

3. Klik header kolom Actions `⋯`, klik `Setup Column...`
4. Klik ikon Pin pada kolom di baris tabel, klik `[Save]`
5. Geser tabel horizontal
6. Verifikasi kolom membeku (sticky) di kiri saat scroll horizontal
7. Muat ulang halaman (F5), buka tab Allocation Quota, klik ikon Changelog pada toolbar Level 1 Groups Quota
8. Verifikasi kolom tetap membeku setelah F5
9. Klik header kolom Actions `⋯`, klik `Setup Column...`
10. Klik ikon Pin pada kolom di baris tabel (Unpin), klik `[Save]`
11. Geser tabel horizontal
12. Verifikasi Unpin melepas pembekuan kolom
13. Gulir tabel kembali ke kiri

14. Pulihkan viewport browser ke ukuran semula

### TC-FA-LIC-354: Reset to Default

15. Klik header kolom Actions `⋯`, klik `Setup Column...`
16. Sembunyikan kolom `Field` dan seret kolom `Modified By` ke posisi pertama
17. Klik `[Reset to Default]`
18. Verifikasi Live Preview kembali ke susunan default modul
19. Klik `[Save]`
20. Verifikasi susunan default tersimpan pada tabel
21. Muat ulang halaman (F5), buka tab Allocation Quota, klik ikon Changelog pada toolbar Level 1 Groups Quota
22. Verifikasi susunan default bertahan setelah F5

### TC-FA-LIC-355: X atau Esc membuang perubahan

23. Klik header kolom Actions `⋯`, klik `Setup Column...`, sembunyikan kolom `Field`
24. Klik `(×)`
25. Verifikasi modal Setup Column tertutup
26. Verifikasi perubahan preview dibuang
27. Verifikasi tabel memakai konfigurasi tersimpan terakhir (ketujuh kolom tampil)
28. Klik header kolom Actions `⋯`, klik `Setup Column...`, sembunyikan kolom `Field`
29. Tekan Esc
30. Verifikasi modal Setup Column tertutup
31. Verifikasi perubahan preview dibuang
32. Verifikasi tabel memakai konfigurasi tersimpan terakhir (ketujuh kolom tampil)

### TC-FA-LIC-356: Satu kolom visible tersisa tidak dapat di-uncheck

33. Klik header kolom Actions `⋯`, klik `Setup Column...`
34. Hilangkan centang semua kolom kecuali `Date`
35. Coba hilangkan centang kolom `Date`
36. Arahkan kursor ke checkbox `Date`
37. Verifikasi checkbox kolom terakhir disabled
38. Verifikasi tooltip `At least one column must remain visible.`
39. Klik `(×)`, lalu tutup modal Changelog dengan `[×]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 7 dan 21 membuka kembali modal sesudah F5; langkah 10 (Unpin) dan langkah 13 memulihkan state per iterasi; langkah 2 dan 14 menyempitkan dan memulihkan viewport; langkah 39 membuang perubahan dan menutup modal (S-09). Langkah 1 membuka modal Changelog sekali untuk seluruh blok.
- Langkah yang diulang per baris tabel kolom: langkah 3 sampai 13 (7 iterasi) (bagian 8b butir 7).
- Spec di atas 35 langkah (39 langkah nominal dan sekitar 105 langkah dengan ekspansi): alasan dipertahankan, seluruh blok adalah Setup Column pada modal yang sama dengan dataset yang sama dan berdiri sendiri; tiap iterasi Pin diakhiri Unpin dan blok sesudahnya dimulai dari konfigurasi default, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-LIC-353 langkah 3 ("geser tabel horizontal") tidak menyebut cara membuat tabel dapat digeser; spec menyempitkan viewport (langkah 2) dan memulihkannya (langkah 14).
  - TC-FA-LIC-355 langkah 3 ("klik `(×)` atau tekan Esc") menyatukan dua cara; spec menjalankan keduanya berurutan (langkah 24 dan 29).
  - TC-FA-LIC-354 langkah 2 ("ubah visibilitas dan urutan beberapa kolom") tidak menyebut kolom yang diubah; spec menyembunyikan `Field` dan menyeret `Modified By` ke posisi pertama.
  - TC-FA-LIC-356 langkah 2 tidak menyebut kolom yang tersisa; spec memakai `Date`.
