---
id: TC-FA-LBL-E2E-007-mobile-modal-create-edit-delete-bulk-delete-modal-changelog-dan-drawer
title: "Mobile: Modal Create/Edit, Delete, Bulk Delete, Modal Changelog, dan Drawer"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-110
  - TC-FA-LBL-156
  - TC-FA-LBL-177
  - TC-FA-LBL-207
  - TC-FA-LBL-326
  - TC-FA-LBL-375
coverage:
  mobile: automated
---

# Mobile: Modal Create/Edit, Delete, Bulk Delete, Modal Changelog, dan Drawer

## Prerequisites

- Mode: FE+BE. Platform: aplikasi mobile Fixed Asset di perangkat Android (full-screen sheet, bottom sheet, long-press).
- Perangkat atau emulator Android dengan aplikasi mobile Fixed Asset terpasang, serta kemampuan mengetuk (tap) dan menekan lama (long-press) (disediakan tim FE). Perangkat Android bersama: `parallel: false` (suite berjalan serial, lihat `suite.md`). Hook suite web (`beforeEach` yang membuka tab Labels) tidak berlaku di aplikasi mobile; layar Labels dibuka oleh langkah spec ini.
- Hook suite: `before` dan `after` berlaku sesuai `suite.md` untuk akun default (Total Control Company Alpha); `after` mengembalikan sesi ke akun default suite.
- Akun aktor (login akun pertama di aplikasi mobile pada hook `before` spec ini):
  - Total Control Company Alpha (Pre-setup #1), `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`: langkah 1 sampai 33.
  - Total Control `Company Changelog` (Pre-setup #17), `Fixture.assetLabeling.akun.totalControlChangelog`, `Spectra.env.FA_TC_CHANGELOG_PASSWORD`: langkah 34 sampai 39 (ganti akun pada langkah 34).
- Environment variable: `FA_LBL_TC_PASSWORD`, `FA_TC_CHANGELOG_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Fixture: `Fixture.assetLabeling.*` (`fixtures/asset-labeling.json`) memuat identitas akun dan nama data tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Data Pre-setup (dibaca saja, tidak diubah spec): #12 (katalog Company Alpha 9 label; dipakai: `Finance Department`), #13 (aset berlabel `Finance Department` untuk isi Drawer), #17 (`Company Changelog` dengan log tujuh entri; dibaca saja dan tidak ditulis spec).
- Data Dinamis (Company Alpha, di-seed lewat sesi API di hook `before`, dibersihkan di hook `after` bila masih ada; bersuffix `{runId}-007`):

| Label | Dipakai di | Kondisi |
|---|---|---|
| `Edit Target 156 {runId}-007` | TC-FA-LBL-156 | bersih, tidak diubah |
| `Delete Target 177 {runId}-007` | TC-FA-LBL-177 | bersih (Total Asset 0, bukan Default Label), dihapus |
| `Bulk Clean A 207 {runId}-007` | TC-FA-LBL-207 | bersih, dihapus |
| `Bulk Clean B 207 {runId}-007` | TC-FA-LBL-207 | bersih, dihapus |

- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label (lihat `suite.md`).
- State global: tidak ada yang diubah selain sesi login di perangkat.

## Test Steps

### TC-FA-LBL-110: Mobile: modal Create Label tampil sebagai full-screen sheet dengan overlay penuh lebar

1. Buka Settings > Asset Master > Labels di aplikasi mobile Fixed Asset
2. Tap `[+ Label]`
3. Verifikasi modal Create Label tampil sebagai full-screen sheet satu kolom
4. Tap Swatch Trigger
5. Verifikasi Color Picker Overlay (swatch preset, kanvas, kolom Hex) tampil penuh lebar di bawah Swatch Trigger
6. Verifikasi Live Preview tetap sticky di atas footer
7. Tutup Color Picker Overlay lalu tutup modal Create Label dengan `✕`

### TC-FA-LBL-375: Mobile: Drawer sebagai full-screen bottom sheet dengan card per aset

8. Tap chip `Finance Department`
9. Verifikasi Drawer tampil sebagai full-screen bottom sheet
10. Verifikasi tabel menjadi card list per aset yang memuat kolom Visible Tabel 2: Name, Asset ID, TAG, Brand, Model/Type, Group, Status, Last Updated
11. Buka bottom sheet toolbar sheet Drawer
12. Verifikasi Search dan Filter tersedia di toolbar bottom sheet yang sama
13. Tutup bottom sheet toolbar dan Drawer

### TC-FA-LBL-156: Mobile: modal Edit Label tampil sebagai full-screen sheet dan zero-delta berlaku

14. Ketik Search `{runId}-007` pada search inline, tekan Enter
15. Tap `⋯` pada card `Edit Target 156 {runId}-007` lalu `Edit`
16. Verifikasi modal Edit Label tampil sebagai full-screen sheet satu kolom
17. Verifikasi nama dan warna terisi pada modal Edit Label
18. Tap `[Save]` tanpa perubahan
19. Verifikasi toast `No changes to save.`
20. Verifikasi modal Edit Label tertutup

### TC-FA-LBL-177: Mobile: Delete dari menu card memakai dialog yang sama

21. Tap `⋯` pada card `Delete Target 177 {runId}-007` lalu `Delete`
22. Verifikasi dialog `Delete Label` dengan bullet `Delete Target 177 {runId}-007` tampil
23. Tap `[Delete]`
24. Verifikasi toast `Success, label has been deleted.`
25. Verifikasi card `Delete Target 177 {runId}-007` hilang

### TC-FA-LBL-207: Mobile: Bulk Delete lewat long-press dan Floating Bottom Bulk Bar

26. Long-press card `Bulk Clean A 207 {runId}-007`
27. Verifikasi mode seleksi aktif, checkbox muncul di semua card, dan bar melayang tampil
28. Tap card `Bulk Clean B 207 {runId}-007`
29. Tap aksi `Delete` pada Floating Bottom Bulk Bar
30. Verifikasi dialog `Delete Labels` dengan kedua nama `Bulk Clean A 207 {runId}-007` dan `Bulk Clean B 207 {runId}-007` tampil
31. Tap `[Delete]`
32. Verifikasi toast `Success, label has been deleted.`
33. Verifikasi mode seleksi berakhir

### TC-FA-LBL-326: Mobile: Modal Changelog tampil sebagai full-screen sheet dengan card per entri

34. Ganti akun: Logout, login sebagai Total Control `Company Changelog` `Fixture.assetLabeling.akun.totalControlChangelog` (`Spectra.env.FA_TC_CHANGELOG_PASSWORD`) di aplikasi mobile, buka Settings > Asset Master > Labels
35. Tap ikon Changelog di header halaman
36. Verifikasi Changelog tampil sebagai full-screen sheet
37. Verifikasi tiap entri berupa card berisi Date, Action, Label Name, Field, Old Value → New Value, Modified By
38. Buka bottom sheet toolbar
39. Verifikasi Filter dan Search tersedia di bottom sheet toolbar

## Notes

- Langkah penghubung (S-03): langkah 1 (membuka layar Labels di aplikasi mobile), langkah 7 (menutup overlay dan modal Create yang tidak dirty), langkah 13 (menutup bottom sheet dan Drawer), langkah 14 (Search untuk menemukan card target, R-16).
- Urutan TC: TC-FA-LBL-375 ditulis sebelum Search langkah 14 karena `Finance Department` tidak masuk hasil Search; TC-FA-LBL-177 dan TC-FA-LBL-207 yang menghapus data ditaruh sesudah TC-FA-LBL-156; TC-FA-LBL-326 paling akhir karena berpindah ke Company Changelog (S-10).
- Alasan di atas sekitar 35 langkah (39 langkah): seluruh blok adalah layar Labels aplikasi mobile pada perangkat Android yang sama (satu kelas harness), tiap blok berdiri sendiri.
- Temuan untuk QA:
  - TC-FA-LBL-326 memakai Pre-setup #17 (`Company Changelog`) yang berbeda dari Company Alpha pada TC lain di spec ini; spec memakai langkah Ganti akun (langkah 34).
  - TC-FA-LBL-207 tidak menyebut apakah dialog `Delete Labels` tampil setelah tap aksi `Delete` di bar atau setelah `[Delete]`; spec memakai urutan langkah TC (dialog tampil sebelum konfirmasi, langkah 30).
