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
6. Muat ulang halaman Import > Brand setiap 5 detik sampai kartu Total Rows menampilkan 150 (batas tunggu 2 menit)
7. Mundurkan penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
8. Baca jumlah percobaan pelanjutan pada kontrol worker commit setiap 5 detik sampai bernilai 1 (batas tunggu 5 menit)
9. Verifikasi jumlah percobaan pelanjutan pada kontrol worker commit bernilai 1
10. Mundurkan lagi penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
11. Muat ulang halaman Import > Brand setiap 5 detik sampai `[Discard]` Enabled (batas tunggu 5 menit)
12. Verifikasi Unsaved Banner tampil
13. Verifikasi `[Discard]` pada Unsaved Banner Enabled
14. Verifikasi kartu Total Rows menampilkan 150
15. Verifikasi Banner Hasil Commit tidak tampil
16. Buka notifikasi lonceng
17. Verifikasi notifikasi "Import Brand stopped" tampil
18. Verifikasi jumlah notifikasi "Import Brand stopped" bertambah tepat 1 dari baseline langkah 3

### TC-GS-IMPORT-840: Commit yang berhenti dengan baris duplicate dan error

19. Reset Client E (D-47) dan seed draft Brand D-57 (250 baris: 248 `pending`, 1 `error` baris #5, 1 `duplicate` baris #20) dengan hook umur draft D-76 varian 1 lewat skrip fixture; pastikan mock AI mode normal
20. Buka Global Settings > Import, pilih Sub-Tab Brand
21. Klik `[Changelog]` di header halaman, catat total entri Changelog Import sebagai baseline, lalu tutup modal Changelog
22. Aktifkan kontrol worker commit mode 3 (dijeda setelah batch pertama selesai; tidak dijalankan lagi)
23. Klik `[Import (248)]`
24. Muat ulang halaman Import > Brand setiap 5 detik sampai kartu Total Rows menampilkan 150 (batas tunggu 2 menit)
25. Verifikasi kartu Total Rows menampilkan 150
26. Mundurkan penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
27. Baca jumlah percobaan pelanjutan pada kontrol worker commit setiap 5 detik sampai bernilai 1 (batas tunggu 5 menit)
28. Verifikasi jumlah percobaan pelanjutan pada kontrol worker commit bernilai 1
29. Mundurkan lagi penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
30. Muat ulang halaman Import > Brand setiap 5 detik sampai `[Discard]` Enabled (batas tunggu 5 menit)
31. Verifikasi `[Discard]` Enabled (job kembali `draft`)
32. Verifikasi kartu Total Rows menampilkan 150
33. Verifikasi kartu Ready to Import menampilkan 148
34. Verifikasi kartu Errors menampilkan 1
35. Verifikasi kartu Duplicates menampilkan 1
36. Klik kartu Duplicates
37. Verifikasi Staging Table menampilkan satu baris `Samsung` berstatus `duplicate`
38. Verifikasi baris `Samsung` bernomor 2
39. Buka notifikasi lonceng
40. Verifikasi notifikasi terbaru memuat judul "Import Brand stopped"
41. Verifikasi notifikasi terbaru memuat isi "100 records imported. 148 rows remain."
42. Verifikasi notifikasi terbaru memuat tombol `[Detail]`
43. Klik tombol `[Changelog]` di header halaman
44. Verifikasi total entri Changelog Import bertambah tepat 1 dari baseline langkah 21
45. Verifikasi entri baru memiliki Action `Import Brand`
46. Verifikasi entri baru memiliki Data "100 records imported, 0 duplicates ignored, 148 rows remaining"
47. Verifikasi entri baru memiliki Modified By `Yoga P`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (d); objek uji adalah hasil commit yang berhenti (penanda kemajuan job sebagai batas yang diuji, notifikasi, Changelog). Mock AI normal hanya pemicu badge saran (P-2).
- Alasan melewati sekitar 35 langkah (47 langkah nominal): dua blok homogen (satu job `committing` yang berhenti per blok), satu kelas harness dan berdiri sendiri dengan reset Client E di awal tiap blok.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 19), pembukaan halaman dan Sub-Tab, pencatatan baseline (langkah 3, 21), aktivasi kontrol worker, penyetelan penanda kemajuan (langkah 7, 10, 26, 29), polling job (langkah 6, 8, 11, 24, 27, 30), membuka dan menutup lonceng dan modal Changelog. Langkah 36 mengklik kartu Duplicates agar Staging Table menampilkan baris `duplicate`.
- Asersi "tanpa Banner Hasil Commit" (langkah 15) didahului langkah 12 sampai 14 (Unsaved Banner tampil, `[Discard]` Enabled, Total Rows 150) sebagai anchor positif pada halaman yang sama setelah muat ulang. Asersi notifikasi dan entri Changelog memakai baseline jumlah (S-12) dan tidak memakai posisi absolut; langkah 40 sampai 42 dan 45 sampai 47 membaca entri terbaru yang tercipta oleh aksi spec ini.
- Temuan untuk QA:
  - TC-GS-IMPORT-361 menulis "menghentikan worker commit setelah batch pertama selesai"; D-47 mendefinisikan "dijeda setelah batch pertama selesai" (mode 3). Spec memakai mode 3.
  - TC-GS-IMPORT-361 Expected d menyatakan "Import Brand stopped sebagai satu-satunya hasil commit yang berhenti" tanpa baseline; spec memakai baseline jumlah notifikasi (S-12) dan mengasersi pertambahan tepat 1.
  - TC-GS-IMPORT-840 Expected e menyebut baris `Samsung` bernomor 2 (setelah baris `error` menjadi nomor 1 pada draft sisa); nomor baris mengikuti penomoran Staging Table pasca-commit sebagian.
  - TC-GS-IMPORT-840 Expected g mengasersi entri teratas Changelog; spec memakai baseline total entri (S-12) dan menyatakan "entri baru" pada Action, Data, Modified By.
  - Post Condition TC-GS-IMPORT-361 dan TC-GS-IMPORT-840 (draft 150 baris, 100 record Brand tersimpan, entri ringkasan Changelog) tidak punya langkah observasi tersendiri selain Expected dan tidak diasersi tambahan (S-01); TC-GS-IMPORT-840 Post Condition c dikonfirmasi oleh Expected g.
