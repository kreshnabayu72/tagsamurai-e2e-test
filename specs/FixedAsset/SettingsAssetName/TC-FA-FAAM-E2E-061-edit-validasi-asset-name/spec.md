---
id: TC-FA-FAAM-E2E-061-edit-validasi-asset-name
title: "Edit: Validasi Asset Name (Required, Batas 120, Trim, Duplikat, Nama Sendiri, Emoji)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-182
  - TC-FA-FAAM-183
  - TC-FA-FAAM-184
  - TC-FA-FAAM-185
  - TC-FA-FAAM-186
  - TC-FA-FAAM-187
  - TC-FA-FAAM-188
coverage:
  web: automated
---

# Edit: Validasi Asset Name (Required, Batas 120, Trim, Duplikat, Nama Sendiri, Emoji)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #13d: Asset Name `Edit Target Item` (Code `ETI`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell` model `5420`, UoM `Unit`, Total Asset 0), dirujuk lewat fixture baru `Fixture.faAssetName.editTargetItem`; dipakai TC-182, 184, 186, 187, 188 hanya untuk dibuka dan ditolak validasi, tidak disimpan sehingga Last Updated tidak berubah (S-06, pengecualian aksi ditolak atau dibatalkan). Pre-setup #10 `Dell Latitude` (Code `DLAT`) hanya dirujuk sebagai nama yang sudah ada untuk TC-186 dan tidak diubah.
- Data Dinamis (salinan seed fixture #13d, Dinamis #19 dan #20): `Edit Target Item 183 {runId}-061` (Code `ETI183`) untuk TC-183 dan `Edit Target Item 185 {runId}-061` (Code `ETI185`) untuk TC-185. Nilai yang diketik TC-183 adalah Asset Name 120 karakter: awalan `A` diisi hingga total 120 karakter termasuk suffix ` {runId}-061` (R-06). Nilai yang diketik TC-185 adalah dua spasi + `Edit Trim {runId}-061` + dua spasi; nilai tersimpan `Edit Trim {runId}-061`.
- Kemampuan teknis (disediakan tim FE/BE): seed API per TC untuk salinan fixture bernama bersuffix `{runId}-061` (Code salinan mengikuti pola TC dan tetap di bawah batas 15 karakter) dan sesi API aktor; salinan dihapus lewat id hasil seed di hook `after`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-182: Asset Name dikosongkan saat Save menampilkan error required

1. Ketik Search `Edit Target Item`, tekan Enter
2. Klik `⋯` baris `Edit Target Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Kosongkan field Asset Name
4. Klik `[Save]`
5. Verifikasi error inline `Asset name must not be empty`
6. Ketik kembali Asset Name `Edit Target Item`

### TC-FA-FAAM-184: Asset Name 121 karakter menampilkan error real-time saat Edit

7. Ganti isi field Asset Name dengan 121 karakter `A`
8. Verifikasi error inline `Max. 120 characters` muncul langsung tanpa Save

### TC-FA-FAAM-188: Emoji pada Asset Name diblok di level input saat Edit

9. Ganti isi field Asset Name dengan nilai tersimpan `Edit Target Item`
10. Ketik dan paste emoji `🔥` di field Asset Name
11. Verifikasi emoji tidak masuk ke field (Asset Name tetap `Edit Target Item`)
12. Verifikasi tidak ada pesan error pada field Asset Name

### TC-FA-FAAM-186: Rename ke nama Asset Name lain menampilkan error duplikat

13. Ubah Asset Name menjadi `dell latitude` lalu tunggu lebih dari 500 ms
14. Klik `[Save]`
15. Verifikasi error inline `Asset name already exists`

### TC-FA-FAAM-187: Mengetik ulang nama sendiri tidak dianggap duplikat

16. Ubah Asset Name menjadi `edit target item` (kapitalisasi beda)
17. Tunggu lebih dari 500 ms
18. Verifikasi field Asset Name berisi `edit target item`
19. Verifikasi tidak ada error `Asset name already exists`
20. Ganti isi field Asset Name dengan nilai tersimpan `Edit Target Item`
21. Klik `[✕]` pada modal Edit

### TC-FA-FAAM-182 (Expected b) dan TC-FA-FAAM-186 (Expected b): record tidak berubah

22. Verifikasi baris `Edit Target Item` tampil di tabel dengan Code `ETI` (record tidak berubah dan tanpa mutasi)

### TC-FA-FAAM-183: Asset Name tepat 120 karakter diterima saat Edit

23. Ganti isi kotak search dengan `Edit Target Item 183 {runId}-061`, tekan Enter
24. Klik `⋯` baris `Edit Target Item 183 {runId}-061` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
25. Ubah Asset Name menjadi 120 karakter (awalan `A` hingga total 120 karakter termasuk suffix ` {runId}-061`)
26. Verifikasi field Asset Name berisi 120 karakter
27. Verifikasi tidak ada error inline pada field Asset Name
28. Klik `[Save]`
29. Verifikasi toast `Success, asset name has been updated.` tampil

### TC-FA-FAAM-185: Asset Name hasil Edit disimpan ter-trim

30. Ganti isi kotak search dengan `Edit Target Item 185 {runId}-061`, tekan Enter
31. Klik `⋯` baris `Edit Target Item 185 {runId}-061` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
32. Ubah Asset Name menjadi dua spasi + `Edit Trim {runId}-061` + dua spasi
33. Klik `[Save]`
34. Ganti isi kotak search dengan `Edit Trim {runId}-061`, tekan Enter
35. Verifikasi baris tampil dengan nama `Edit Trim {runId}-061` tanpa spasi tepi

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1, 23, 30, dan 34 untuk menemukan baris target (R-16); langkah 6, 9, dan 20 mengembalikan Asset Name ke nilai tersimpan agar error inline TC sebelumnya tidak terbawa (R-12, S-09); penutupan modal pada langkah 21 tanpa dialog karena form sudah sama dengan nilai tersimpan.
- Urutan TC: validasi yang diblokir lebih dulu (TC-FA-FAAM-182, 184, 188, 186, 187) pada satu pembukaan popup `Edit Target Item`, lalu aksi sukses pada salinan (TC-FA-FAAM-183, 185) (S-10, prinsip 6 bagian 3).
- Langkah 22 memenuhi TC-FA-FAAM-182 Expected b ("Record tidak berubah") dan TC-FA-FAAM-186 Expected b ("Tanpa mutasi") sekaligus, diamati pada baris tabel setelah form ditutup.
- Verifikasi field Asset Name berisi 120 karakter (TC-FA-FAAM-183) dan Verifikasi field Asset Name berisi `edit target item` (TC-FA-FAAM-187) adalah anchor untuk asersi ketiadaan error di bawahnya (bagian 8b butir 2).
- Keunikan nilai Code yang diketik (batas 15 karakter tidak menyisakan ruang untuk suffix `{runId}-<NNN>`): nilai Code mengikuti TC, nomor TC membuatnya berbeda antar spec, seed salinan idempotent, cleanup hanya menghapus yang dibuat spec ini, dan suite berjalan serial (S-12).
- Temuan untuk QA:
  - TC-FA-FAAM-183 dan TC-FA-FAAM-185 mengubah Asset Name salinan menjadi nilai literal tanpa suffix per run; spec menambahkan suffix ` {runId}-061` pada nilai yang diketik dan dibandingkan (S-12) dan menghitung 120 karakter termasuk suffix.
  - TC-FA-FAAM-186 mengasersi duplikat terhadap nama Pre-setup #10 `Dell Latitude` dengan kapitalisasi beda (`dell latitude`); spec mengikuti TC dan hanya membaca baris itu.
