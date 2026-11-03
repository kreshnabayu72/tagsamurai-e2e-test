---
id: TC-FA-FAAM-E2E-072-edit-no-op-spasi-code-kosong-kapitalisasi-dan-record-dihapus
title: "Edit: No-Op Spasi Tepi, Code Dikosongkan, Kapitalisasi, dan Record Dihapus Pengguna Lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAM-224
  - TC-FA-FAAM-225
  - TC-FA-FAAM-226
  - TC-FA-FAAM-230
coverage:
  web: automated
---

# Edit: No-Op Spasi Tepi, Code Dikosongkan, Kapitalisasi, dan Record Dihapus Pengguna Lain

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #13d: Asset Name `Edit Target Item` (Code `ETI`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell` model `5420`, UoM `Unit`, Total Asset 0), dirujuk lewat fixture baru `Fixture.faAssetName.editTargetItem`; pada spec ini hanya dibuka dan ditolak validasi atau dibatalkan, tidak disimpan sehingga Last Updated tidak berubah (S-06).
- Data Pre-setup #13e: Asset Name `Edit Code Item` (Code `ECI`, hasil generator dari nama itu, Total Asset 0) dirujuk lewat fixture baru `Fixture.faAssetName.editCodeItem`, dan #13j `Case Model Item` (Code `CSM`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell` model `X1`, UoM `Unit`, Total Asset 0) lewat `Fixture.faAssetName.caseModelItem`; keduanya hanya diedit tanpa perubahan bermakna (no-op), tidak ada yang tersimpan sehingga Last Updated tidak berubah (S-06).
- Data Dinamis (salinan seed fixture #13d, Dinamis #32): `Edit Target Item 230 {runId}-072` (Code `ETI230`), dihapus oleh sesi API aktor di dalam spec (TC-230).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Changelog, System Log aktor (Detail User aktor > tab System Log), dan Activity Log FAMS sebelum aksi sebagai baseline; asersi memakai selisih terhadap baseline (S-12).
- Kemampuan teknis (disediakan tim FE/BE): seed API per TC untuk salinan fixture bernama bersuffix `{runId}-072` (Code salinan mengikuti pola TC dan tetap di bawah batas 15 karakter) dan sesi API aktor; salinan dihapus lewat id hasil seed di hook `after`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### Baseline log (untuk TC-FA-FAAM-224, 225, 226)

1. Ketik Search `Edit Target Item`, tekan Enter
2. Catat jumlah entri Changelog, System Log aktor, dan Activity Log FAMS sebagai baseline

### TC-FA-FAAM-225: Perubahan hanya spasi tepi dianggap no-op

3. Klik `⋯` baris `Edit Target Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
4. Ubah Asset Name menjadi dua spasi + `Edit Target Item` + dua spasi
5. Klik `[Save]`
6. Verifikasi toast netral `No changes to save.`

### TC-FA-FAAM-226: Code dikosongkan menghasilkan Code yang sama dengan tersimpan dihitung no-op

7. Ganti isi kotak search dengan `Edit Code Item`, tekan Enter
8. Klik `⋯` baris `Edit Code Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
9. Kosongkan Code
10. Klik `[Save]`
11. Verifikasi toast netral `No changes to save.` (generator menghasilkan kode yang sama dengan Code tersimpan)

### TC-FA-FAAM-224: Perubahan hanya kapitalisasi pada Asset Name, Code, dan nama model dianggap no-op

12. Ganti isi kotak search dengan `Case Model Item`, tekan Enter
13. Klik `⋯` baris `Case Model Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
14. Ubah Asset Name menjadi `CASE MODEL ITEM`
15. Ubah Code menjadi `csm`
16. Hapus badge model `X1` lalu ketik `x1` dan tekan Enter
17. Klik `[Save]`
18. Verifikasi toast netral `No changes to save.`
19. Klik `⋯` baris `Case Model Item` lalu `Detail`, buka tab Models per Brand
20. Verifikasi Popup Detail menampilkan Asset Name `Case Model Item`
21. Verifikasi Popup Detail menampilkan Code `CSM`
22. Verifikasi Popup Detail menampilkan model `X1`
23. Tutup Popup Detail

### Log pasca no-op (Expected TC-FA-FAAM-224 c, 225, 226)

24. Buka Changelog (icon Changelog)
25. Verifikasi jumlah entri Changelog sama dengan baseline
26. Tutup Modal Changelog
27. Buka System Log (Detail User aktor > tab System Log)
28. Verifikasi jumlah entri System Log sama dengan baseline
29. Buka Activity Log FAMS
30. Verifikasi jumlah entri Activity Log sama dengan baseline

### TC-FA-FAAM-230: Record dihapus pengguna lain saat Edit: modal tutup, tabel refresh, toast netral

31. Buka Fixed Asset > Settings > Asset Master > Asset Name lalu Ketik Search `Edit Target Item 230 {runId}-072`, tekan Enter
32. Klik `⋯` baris `Edit Target Item 230 {runId}-072` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
33. Hapus `Edit Target Item 230 {runId}-072` lewat sesi API aktor hingga penghapusan tersimpan
34. Ubah Code menjadi `ETI230-6`
35. Klik `[Save]`
36. Verifikasi modal Edit tertutup
37. Verifikasi toast netral `This asset name is no longer available.`
38. Verifikasi tabel di-refresh dan menampilkan empty state `No results found` untuk Search nama itu
39. Verifikasi baris `Edit Target Item 230 {runId}-072` tidak ada

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1, 7, 12, dan 31 untuk menemukan baris target (R-16); penutupan Popup Detail pada langkah 23 dan Modal Changelog pada langkah 26.
- Baseline jumlah entri tiga log dicatat sekali pada awal spec dan dibandingkan sekali setelah tiga aksi no-op (TC-FA-FAAM-225, 226, 224); karena ketiganya tidak boleh menambah entri, selisih nol atas ketiganya sekaligus memenuhi Expected "nol entri log" tiap TC. Toast netral `No changes to save.` tiap TC menjadi anchor (bagian 8b butir 2). Penempatan verifikasi log di akhir blok no-op menyimpang dari urutan per-TC (R-03) demi menghindari tiga kali membuka tiga surface log.
- Jumlah entri log adalah asersi selisih dengan baseline atas aksi no-op yang menjadi alur fungsional TC, bukan asersi absence kelas g.
- Urutan TC: no-op tanpa penyimpanan (TC-FA-FAAM-225, 226, 224) lebih dulu, lalu TC-FA-FAAM-230 yang record-nya dihapus pelaku kedua lewat sesi API (aksi menghapus data di akhir, S-10).
- Keunikan nilai Code yang diketik (batas 15 karakter tidak menyisakan ruang untuk suffix `{runId}-<NNN>`): nilai Code mengikuti TC, nomor TC membuatnya berbeda antar spec, seed salinan idempotent, cleanup hanya menghapus yang dibuat spec ini, dan suite berjalan serial (S-12).
- Temuan untuk QA:
  - TC-FA-FAAM-224 Expected a/b/c mengasersi hasil no-op pada Popup Detail dan tiga surface log; Last Updated tidak diasersi karena tidak ada di Expected TC itu.
  - TC-FA-FAAM-230 Expected a menulis "tabel di-refresh" tanpa kriteria pengamatan; spec memakai empty state `No results found` untuk Search nama salinan sebagai tanda tabel dimuat ulang (diputuskan penulis).
- Alasan melewati sekitar 35 langkah: empat blok berdiri sendiri; tiga blok pertama no-op tanpa penyimpanan dan berbagi satu pembacaan log di akhir, blok terakhir (record dihapus pelaku lain) mandiri. Langkah pembacaan tiga surface log menyumbang tujuh langkah.
