---
id: TC-FA-FAAC-E2E-187-multi-sesi-dua-admin-race
title: "Multi-Sesi: Dua Admin Menyimpan Edit, Create Class Code Sama, dan Cancel Scheduled Version Hampir Bersamaan"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-182
  - TC-FA-FAAC-669
  - TC-FA-FAAC-687
sourceRules: ["T-02", "F-FAAC-02.k4", "L-02", "T-01", "F-FAAC-01.k1", "R-01", "§4.2f#b2", "N-10", "L-01", "F-FAAC-17.k6", "T-16", "S-17", "L-13", "E-FAAC-119"]
smoke: []
dependsOn: []
trace:
  "T-02": [7, 9]
  "F-FAAC-02.k4": [10, 13]
  "L-02": [14, 15]
  "T-01": 21
  "F-FAAC-01.k1": 22
  "R-01": 23
  "§4.2f#b2": 25
  "N-10": 28
  "L-01": 30
  "F-FAAC-17.k6": [35, 36]
  "T-16": 37
  "S-17": 38
  "L-13": 41
  "E-FAAC-119": 42
coverage:
  web: automated
---

# Multi-Sesi: Dua Admin Menyimpan Edit, Create Class Code Sama, dan Cancel Scheduled Version Hampir Bersamaan

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`) di dua konteks browser: sesi A dan sesi B. Sesi A login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite. Sesi B dibuka dan login pada langkah 1 (akun sama, konteks browser kedua) dan ditutup pada langkah 45 serta oleh hook `after`.
- Kemampuan teknis: dua konteks browser dengan akun yang sama dan dua sesi web aktif bersamaan (disediakan tim FE/BE; TC menulis "sesi A dan sesi B login sebagai Total Control" tanpa menyebut batas sesi web); pembacaan Class Name `B-LWW`, jumlah Asset Class `B-CRACE`, versi Scheduled `B-SCHED3`, dan jumlah entri Changelog Asset Class lewat kemampuan baca BE (audit trail permanen, asersi memakai selisih terhadap baseline, bukan angka absolut).
- Jam: bulan berjalan M mengikuti zona waktu General Settings client (NC-11); jam server dan jam browser tidak digeser.
- Data seed Pre-setup (kode literal TC, disediakan fixture BE): Asset Class `B-LWW`; Asset Class `B-SCHED3` dengan dua versi Scheduled M+2 dan M+4 dan aktor memiliki Update. Class Code `B-CRACE` belum ada; dibuat sesi A pada langkah 19 dan dihapus fixture BE di hook `after`. Fixture BE memulihkan Class Name `B-LWW` dan kedua versi Scheduled `B-SCHED3` di hook `after`.
- Data Uji TC-669: Class Code `B-CRACE`; Class Name `Create Race`; Method `Straight Line`; Useful Life `120`; Residual `10` dengan unit `Percent`; Tax Depreciation Class `Bukan bangunan – Kelompok 3`; Tax Method `Declining Balance`. Field wajib lain (Depreciation Start Convention dan Tax Depreciation Start Rule) memakai nilai awal bawaan form.
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (flag Guided Tooltip, seed dan fixture BE): dinyatakan sekali di suite.md; suite serial (`parallel: false`).

## Test Steps

1. Buka konteks browser kedua (sesi B), login sebagai Total Control, lalu buka Fixed Asset > Settings > Accounting > tab Asset Class
2. Catat baseline lewat kemampuan baca BE: Class Name `B-LWW` dan jumlah entri Changelog Asset Class untuk `B-LWW`, `B-CRACE`, dan `B-SCHED3`

### TC-FA-FAAC-182: Dua admin menyimpan Edit atas Asset Class yang sama hampir bersamaan

3. Di sesi A dan sesi B, ketik Search `B-LWW`, tekan Enter, lalu klik link Class Code `B-LWW`
4. Di sesi A ubah Class Name menjadi `Name A`
5. Di sesi B ubah Class Name menjadi `Name B` tanpa memuat ulang
6. Klik `Save` di sesi A
7. Verifikasi toast sukses `Success, asset class has been updated.` di sesi A
8. Klik `Save` di sesi B
9. Verifikasi toast sukses `Success, asset class has been updated.` di sesi B
10. Verifikasi nilai akhir Class Name `B-LWW` adalah `Name B` (last-write-wins)
11. Di sesi A dan sesi B klik breadcrumb `Asset Class`, lalu di sesi B klik icon `Changelog`
12. Ketik Search `B-LWW` pada Modal Changelog, tekan Enter
13. Verifikasi jumlah entri Changelog `B-LWW` bertambah dua dibanding baseline
14. Verifikasi satu baris Edit Class Name dari Class Name awal `B-LWW` ke `Name A`
15. Verifikasi satu baris Edit Class Name dari `Name A` ke `Name B`
16. Tutup Modal Changelog

### TC-FA-FAAC-669: Dua sesi Create Asset Class dengan Class Code sama hampir bersamaan

17. Di sesi A dan sesi B klik tombol `+ Asset Class` di toolbar tabel
18. Di kedua sesi isi data yang sama (Data Uji TC-669), tanpa memuat ulang
19. Klik `Submit` di sesi A
20. Segera klik `Submit` di sesi B
21. Verifikasi toast sukses `Success, asset class has been created.` di sesi A
22. Verifikasi caption pada Class Code di sesi B `Class code already exists`
23. Verifikasi form di sesi B tetap terbuka tanpa toast sukses
24. Di sesi B klik breadcrumb `Asset Class`
25. Verifikasi dialog `Unsaved Changes` tampil di sesi B
26. Klik `[Leave]` di sesi B
27. Di sesi A ganti isi kotak search dengan `B-CRACE`, tekan Enter
28. Verifikasi hanya satu Asset Class `B-CRACE` di tabel
29. Di sesi A klik icon `Changelog`, lalu ketik Search `B-CRACE` pada Modal Changelog, tekan Enter
30. Verifikasi jumlah entri Changelog `B-CRACE` bertambah satu dibanding baseline dan entri itu adalah entri Create untuk `B-CRACE`
31. Tutup Modal Changelog

### TC-FA-FAAC-687: Cancel Scheduled Version ditolak tanpa membatalkan versi lain bila versi yang dipilih sudah dibatalkan admin lain saat Confirm

32. Di sesi A ganti isi kotak search dengan `B-SCHED3`, tekan Enter, klik link Class Code `B-SCHED3`, lalu klik `Cancel scheduled version` (dialog menampilkan Effective From versi M+2)
33. Di sesi B ganti isi kotak search dengan `B-SCHED3`, tekan Enter, klik link Class Code `B-SCHED3`, klik `Cancel scheduled version`, lalu klik `Cancel version` (versi M+2 dibatalkan)
34. Di sesi A, tanpa memuat ulang, klik `Cancel version`
35. Verifikasi server menolak tanpa membatalkan versi lain: versi M+4 tetap Scheduled
36. Verifikasi dialog `Cancel Scheduled Version` menutup di sesi A
37. Verifikasi toast netral (severity Info) `This scheduled version is no longer available.` di sesi A
38. Verifikasi Alert versi Scheduled di sesi A disegarkan menjadi `Next version starts [MMM YYYY].` untuk versi M+4 (mis. `Feb 2027` bila bulan berjalan `Oct 2026`)
39. Klik breadcrumb `Asset Class` di sesi A
40. Klik icon `Changelog`, lalu ketik Search `B-SCHED3` pada Modal Changelog, tekan Enter
41. Verifikasi satu entri L-13 untuk Effective From M+2 (dari sesi B) tampil di Modal Changelog
42. Verifikasi tidak ada entri L-13 dari sesi A
43. Tutup Modal Changelog
44. Klik `(←)` pada kotak Search di sesi A
45. Tutup konteks browser kedua (sesi B)

## Notes

1. Subjudul `###` memetakan langkah ke id TC granular. Spec ini kelas c (multi-konteks): hasil diasersi di dua sesi UI. Hanya pelaku kedua yang memicu state tanpa diasersi memakai sesi API di spec lain suite ini.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (membuka sesi B, ganti konteks eksplisit; S-07); langkah 3, 27, 29, 32, dan 33 memuat Search untuk menemukan baris target (R-16); langkah 11, 24, dan 39 (kembali ke tabel); langkah 24 sampai 26 (menutup form Create sesi B yang dirty lewat breadcrumb, S-08; `Verifikasi` dialog `Unsaved Changes` diwajibkan S-08); langkah 16, 31, dan 43 (menutup Modal Changelog); langkah 44 (mengosongkan Search); langkah 45 (menutup konteks sesi B, S-09).
3. Cara baca Changelog (S-12, S-14): entri baru dibaca sesudah selisih jumlah entri terhadap baseline dibuktikan; entri dalam menit yang sama dibaca sebagai himpunan baris teratas sebanyak selisih tanpa mengandalkan urutan di antaranya. Jumlah entri `B-LWW` bertambah dua (langkah 13): dua Edit Class Name dibaca sebagai himpunan.
4. Pengecualian kode seed literal (S-06/S-12): TC mewajibkan `B-LWW`, `B-CRACE`, dan `B-SCHED3`; kode dipakai apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Seed milik spec ini dipulihkan atau dihapus fixture BE di hook `after`.
5. Alasan di atas sekitar 35 langkah: ketiga blok satu kelas harness (c, multi-konteks dua admin) dengan jenis harness yang sama (dua konteks browser, akun yang sama); konvensi bagian 3 prinsip 13 menetapkan kelas berat satu spec per jenis harness. Tiap blok memakai Asset Class dan baseline sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
6. Temuan untuk QA: TC-182 tidak menyebut cara memverifikasi nilai akhir `Name B` sehingga spec memakai kemampuan baca BE; TC-669 tidak menyebut nilai field wajib lain; TC-687 meletakkan klik "Cancel scheduled version" di sesi A lebih dulu dan tidak menyebut Search. Post Condition TC-669 dan TC-687 tidak punya langkah observasi dan tidak diasersi terpisah selain yang tercakup Expected.
