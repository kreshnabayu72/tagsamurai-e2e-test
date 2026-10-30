---
id: TC-GS-IMPORT-E2E-159-kontrol-worker-commit-commit-berhenti-tanpa-banner-hasil-commit
title: "Kontrol worker commit: commit berhenti tanpa Banner Hasil Commit, notifikasi stopped, duplicate tetap tampil, rows remaining, Changelog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-361
  - TC-GS-IMPORT-840
coverage:
  web: automated
---

# Kontrol worker commit: commit berhenti tanpa Banner Hasil Commit, notifikasi stopped, duplicate tetap tampil, rows remaining, Changelog

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec mengubah state global (kontrol worker commit, penanda kemajuan job, mode mock AI) dan melakukan commit nyata (batch pertama) di Client E; Changelog Import dan notifikasi lonceng Client E bersifat permanen sehingga asersi memakai baseline; lihat `suite.md`.
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client E dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; TC-361 tidak merujuk D-47 pada kolom D-ref tetapi membutuhkannya):
  - Kontrol worker commit D-47 mode 3 (dijeda setelah batch pertama selesai, 100 baris terkomit, tidak dijalankan lagi selama blok) dan hook membaca jumlah percobaan pelanjutan job.
  - Fixture timestamp kemajuan job: memundurkan penanda kemajuan job 16 menit (dua kali); dihitung di server dan tidak diamati lewat countdown UI sehingga jam browser tidak diubah.
  - Margin terhadap batas 15 menit (kurang dari 5 menit; 8b.3): tiap pergeseran 16 menit (langkah 8, 11, 28, 31) memberi margin 16 − 15 = 1 menit (60 detik) di atas batas; usia tanpa kemajuan = pergeseran + waktu nyata sejak kemajuan terakhir, sehingga waktu nyata hanya menambah usia (arah aman: batas tetap terlampaui). Nilai 16 menit mengikuti TC dan tidak dinaikkan.
  - Hook umur draft D-76 varian 1 (>=24 jam; `created_at` dimundurkan 25 jam) agar Unsaved Banner dan `[Discard]` tampil.
  - Mock layanan AI mode normal D-40 (tabel D-41 dan D-42) untuk badge saran baris #5 (TC-840).
  - Skrip fixture reset Client E (D-47: hapus draft, lanjutkan worker, hapus Brand hasil commit, reset hasil commit terakhir) dan seeding draft.
  - Jeda nyata: polling "muat ulang setiap 5 detik" menunggu job latar belakang (bukan menunggu jam).
- Baseline log (S-12): jumlah notifikasi "Import Brand stopped" pada lonceng dan total entri Changelog Import Client E dicatat sebelum aksi pemicu pertama tiap blok; asersi "baru" memakai selisih terhadap baseline, bukan posisi atau angka absolut.
- Data Dinamis (milik spec ini; draft dibuang dan hasil commit batch pertama dihapus oleh reset):
  - D-56 `brand-250-impor.csv`: `Brand Impor 001` sampai `Brand Impor 250`, semua valid dan unik (TC-361).
  - D-57 `brand-250-mixed.csv` (TC-840): 248 `pending` (`Brand Impor nnn`), baris #5 `error` (Brand Name 121 karakter nilai sumber Brand pertama tabel D-41, badge saran `Samsung Electronics Indonesia`), baris #20 `duplicate` (`Samsung`); batch pertama = baris #1-#4, #6-#19, #21-#102.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): lanjutkan worker commit, kembalikan penanda kemajuan job dan mock AI ke normal, hapus draft Client E, hapus Brand hasil commit batch pertama, reset hasil commit terakhir, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-361: Commit yang berhenti tidak memunculkan Banner Hasil Commit

1. Reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
2. Buka Global Settings > Import, pilih Sub-Tab Brand
3. Buka notifikasi lonceng, catat jumlah notifikasi "Import Brand stopped" sebagai baseline, lalu tutup lonceng
4. Aktifkan kontrol worker commit mode 3 (dijeda setelah batch pertama selesai; tidak dijalankan lagi) dan pencatat jumlah percobaan pelanjutan job
5. Klik `[Import (250)]`
6. Tunggu aksi selesai (permintaan mendapat respons)
7. Muat ulang halaman Import > Brand setiap 5 detik sampai kartu Total Rows menampilkan 150 (batas tunggu 2 menit)
8. Mundurkan penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
9. Baca jumlah percobaan pelanjutan pada kontrol worker commit setiap 5 detik sampai bernilai 1 (batas tunggu 5 menit)
10. Verifikasi jumlah percobaan pelanjutan pada kontrol worker commit bernilai 1
11. Mundurkan lagi penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
12. Muat ulang halaman Import > Brand setiap 5 detik sampai `[Discard]` Enabled (batas tunggu 5 menit)
13. Verifikasi Unsaved Banner tampil
14. Verifikasi `[Discard]` pada Unsaved Banner Enabled
15. Verifikasi kartu Total Rows menampilkan 150
16. Verifikasi Banner Hasil Commit tidak tampil
17. Buka notifikasi lonceng
18. Verifikasi notifikasi "Import Brand stopped" tampil
19. Verifikasi jumlah notifikasi "Import Brand stopped" bertambah tepat 1 dari baseline langkah 3

### TC-GS-IMPORT-840: Commit yang berhenti dengan baris duplicate dan error

20. Reset Client E (D-47) dan seed draft Brand D-57 (250 baris: 248 `pending`, 1 `error` baris #5, 1 `duplicate` baris #20) dengan hook umur draft D-76 varian 1 lewat skrip fixture; pastikan mock AI mode normal
21. Buka Global Settings > Import, pilih Sub-Tab Brand
22. Klik `[Changelog]` di header halaman, catat total entri Changelog Import sebagai baseline, lalu tutup modal Changelog
23. Aktifkan kontrol worker commit mode 3 (dijeda setelah batch pertama selesai; tidak dijalankan lagi)
24. Klik `[Import (248)]`
25. Tunggu aksi selesai (permintaan mendapat respons)
26. Muat ulang halaman Import > Brand setiap 5 detik sampai kartu Total Rows menampilkan 150 (batas tunggu 2 menit)
27. Verifikasi kartu Total Rows menampilkan 150
28. Mundurkan penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
29. Baca jumlah percobaan pelanjutan pada kontrol worker commit setiap 5 detik sampai bernilai 1 (batas tunggu 5 menit)
30. Verifikasi jumlah percobaan pelanjutan pada kontrol worker commit bernilai 1
31. Mundurkan lagi penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
32. Muat ulang halaman Import > Brand setiap 5 detik sampai `[Discard]` Enabled (batas tunggu 5 menit)
33. Verifikasi `[Discard]` Enabled (job kembali `draft`)
34. Verifikasi kartu Total Rows menampilkan 150
35. Verifikasi kartu Ready to Import menampilkan 148
36. Verifikasi kartu Errors menampilkan 1
37. Verifikasi kartu Duplicates menampilkan 1
38. Klik kartu Duplicates
39. Verifikasi Staging Table menampilkan satu baris `Samsung` berstatus `duplicate`
40. Verifikasi baris `Samsung` bernomor 2
41. Buka notifikasi lonceng
42. Verifikasi notifikasi terbaru memuat judul "Import Brand stopped"
43. Verifikasi notifikasi terbaru memuat isi "100 records imported. 148 rows remain."
44. Verifikasi notifikasi terbaru memuat tombol `[Detail]`
45. Klik tombol `[Changelog]` di header halaman
46. Verifikasi total entri Changelog Import bertambah tepat 1 dari baseline langkah 22
47. Verifikasi entri baru memiliki Action `Import Brand`
48. Verifikasi entri baru memiliki Data "100 records imported, 0 duplicates ignored, 148 rows remaining"
49. Verifikasi entri baru memiliki Modified By `Yoga P`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (d); objek uji adalah hasil commit yang berhenti (penanda kemajuan job sebagai batas yang diuji, notifikasi, Changelog). Mock AI normal hanya pemicu badge saran (P-2).
- Alasan melewati sekitar 35 langkah (49 langkah nominal): dua blok homogen (satu job `committing` yang berhenti per blok), satu kelas harness dan berdiri sendiri dengan reset Client E di awal tiap blok.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 20), pembukaan halaman dan Sub-Tab, pencatatan baseline (langkah 3, 22), aktivasi kontrol worker, "Tunggu aksi selesai (permintaan mendapat respons)" persis sesudah klik `[Import (N)]` dan sebelum polling (langkah 6, 25; K-16 dan bagian 8b butir 8), penyetelan penanda kemajuan (langkah 8, 11, 28, 31), polling job (langkah 7, 9, 12, 26, 29, 32), membuka dan menutup lonceng dan modal Changelog. Langkah 38 mengklik kartu Duplicates agar Staging Table menampilkan baris `duplicate`.
- Asersi "tanpa Banner Hasil Commit" (langkah 16) didahului langkah 13 sampai 15 (Unsaved Banner tampil, `[Discard]` Enabled, Total Rows 150) sebagai anchor positif pada halaman yang sama setelah muat ulang. Asersi notifikasi dan entri Changelog memakai baseline jumlah (S-12) dan tidak memakai posisi absolut; langkah 42 sampai 44 dan 47 sampai 49 membaca entri terbaru yang tercipta oleh aksi spec ini.
- Temuan untuk QA:
  - Penanda selesai untuk klik `[Import (N)]` (langkah 6, 25) tidak disebut di TC atau PRD; langkah "Tunggu aksi selesai" memakai "permintaan mendapat respons" sampai QA menetapkan penanda yang teramati.
  - TC-GS-IMPORT-361 menulis "menghentikan worker commit setelah batch pertama selesai"; D-47 mendefinisikan "dijeda setelah batch pertama selesai" (mode 3). Spec memakai mode 3.
  - TC-GS-IMPORT-361 Expected d menyatakan "Import Brand stopped sebagai satu-satunya hasil commit yang berhenti" tanpa baseline; spec memakai baseline jumlah notifikasi (S-12) dan mengasersi pertambahan tepat 1.
  - TC-GS-IMPORT-840 Expected e menyebut baris `Samsung` bernomor 2 (setelah baris `error` menjadi nomor 1 pada draft sisa); nomor baris mengikuti penomoran Staging Table pasca-commit sebagian.
  - TC-GS-IMPORT-840 Expected g mengasersi entri teratas Changelog; spec memakai baseline total entri (S-12) dan menyatakan "entri baru" pada Action, Data, Modified By.
  - Post Condition TC-GS-IMPORT-361 dan TC-GS-IMPORT-840 (draft 150 baris, 100 record Brand tersimpan, entri ringkasan Changelog) tidak punya langkah observasi tersendiri selain Expected dan tidak diasersi tambahan (S-01); TC-GS-IMPORT-840 Post Condition c dikonfirmasi oleh Expected g.
