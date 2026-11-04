---
id: TC-FA-LIC-E2E-109-pencatatan-log-snapshot-entri-tunggal-dan-cascade-delete
title: "Pencatatan Log: Snapshot Immutability, Snapshot Nama Grup, dan Satu Aksi Satu Entri per Surface"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-379
  - TC-FA-LIC-380
  - TC-FA-LIC-381
coverage:
  web: automated
---

# Pencatatan Log: Snapshot Immutability, Snapshot Nama Grup, dan Satu Aksi Satu Entri per Surface

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid (`License allocation per group` ON, General Settings `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup, jam dan format tanggal): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup yang diubah spec: hierarki dan alokasi grup #12 (Divisi Logistik beralokasi 500 dalam Kantor Pusat) pada blok TC-FA-LIC-379 dan TC-FA-LIC-381. Pemulihan oleh fixture BE pemulih (disediakan tim FE/BE) di hook `before` dan `after` serta pada langkah 10 dan 26 antar blok TC (pengecualian S-06: alokasi grup Pre-setup bernama literal tidak dapat dimiliki spec, suite berjalan serial). Efek yang dicatat: kolom Last Updated alokasi Divisi Logistik berubah dan entri baru bertambah permanen di Changelog Allocation Quota, System Log Rudi Hartono, dan Activity Log Fixed Asset.
- Data Dinamis (blok TC-FA-LIC-380, rename grup memakai grup milik spec, bukan grup Pre-setup): grup anak Kantor Pusat `Divisi Logistik+{runId}-109` tanpa alokasi dan tanpa aset aktif, dibuat fixture BE (disediakan tim FE/BE) di hook `before`; nama hasil rename `Divisi Logistik Pusat+{runId}-109`. Fixture di langkah 26 dan hook `after` memulihkan grup ke nama `Divisi Logistik+{runId}-109` tanpa alokasi atau menghapusnya; penghapusan grup beralokasi menambah entri Remove Allocation permanen di tiga surface.
- Kemampuan teknis: membaca jumlah entri Changelog Allocation Quota, System Log Rudi Hartono, dan Activity Log sebelum aksi (baseline, langkah 1 dan 27) disediakan tim FE/BE; asersi jumlah memakai selisih terhadap baseline.
- Data Pre-setup yang dibaca spec: riwayat Changelog Allocation Quota #27 memuat entri seed `Divisi Logistik` `Allocated Quota` `500` ke `600` (29/09/26 10:05) dan `Divisi Keuangan` `—` ke `50` (26/09/26 11:20); fixture BE pemulih riwayat (disediakan tim FE/BE) menjalankannya di hook `before` dan `after`. Entri hasil aksi spec ini dibedakan dari baris seed lewat selisih jumlah entri dan kunci Date ≥ waktu acuan (langkah 1), bukan hanya Group Name, Field, dan Old Value. Jam server dan jam browser sinkron; kolom Date berketelitian menit sehingga waktu acuan dibulatkan ke menit.
- Jalur menu: System Log lewat Global Settings > User > Detail Rudi Hartono > Tab System Log; Activity Log lewat Fixed Asset > Reports & Logs > Activity Log; rename grup lewat Settings > Groups.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-LIC-379: Snapshot immutability: edit dua kali, entri pertama tidak berubah

1. Catat jumlah entri Changelog Allocation Quota (baseline) dan waktu acuan (menit saat ini, sebelum aksi pertama)
2. Buka tab Allocation Quota, klik node `Kantor Pusat`
3. Klik `[Edit]` pada `Divisi Logistik`, isi `600`, klik `[Save]`
4. Klik `[Edit]` pada `Divisi Logistik`, isi `650`, klik `[Save]`
5. Tunggu aksi selesai
6. Klik ikon Changelog pada toolbar Child Groups Quota
7. Verifikasi jumlah entri bertambah tepat dua dari baseline (tidak ada entri yang ditimpa)
8. Verifikasi himpunan dua baris teratas (sebanyak selisih jumlah pada langkah 7, Date ≥ waktu acuan langkah 1, tanpa mengandalkan urutan di antaranya) memuat entri pertama (lebih lama) dengan Group Name `Divisi Logistik`, Field `Allocated Quota`, dan Old Value `500`, tetap New Value `600`
9. Verifikasi himpunan dua baris teratas yang sama memuat entri kedua (lebih baru dari entri pertama) dengan Group Name `Divisi Logistik`, Field `Allocated Quota`, dan Old Value `600`, New Value `650`

### TC-FA-LIC-380: Snapshot nama grup: rename grup tidak mengubah entri lama

10. Tutup modal dengan `[×]`, lalu pulihkan Pre-setup #12 lewat fixture BE
11. Klik node `Kantor Pusat`, klik `[Edit]` pada `Divisi Logistik+{runId}-109`, isi `50`, klik `[Save]`
12. Tunggu aksi selesai
13. Buka Settings > Groups, ketik Search `Divisi Logistik+{runId}-109`, tekan Enter
14. Rename `Divisi Logistik+{runId}-109` menjadi `Divisi Logistik Pusat+{runId}-109` pada baris hasil Search
15. Tunggu aksi selesai
16. Buka License > Allocation Quota, klik node `All Groups`, klik ikon Changelog pada toolbar Level 1 Groups Quota
17. Verifikasi entri lama, dicari lewat Group Name `Divisi Logistik+{runId}-109`, Field `Allocated Quota`, Old Value `—`, dan New Value `50`, tetap tampil dengan Group Name `Divisi Logistik+{runId}-109`
18. Verifikasi tidak ada baris dengan Group Name `Divisi Logistik Pusat+{runId}-109`, Field `Allocated Quota`, Old Value `—`, dan New Value `50` (entri lama tidak ikut berganti nama)
19. Tutup modal dengan `[×]`, klik node `Kantor Pusat`, klik `[Edit]` pada `Divisi Logistik Pusat+{runId}-109`, isi `60`, klik `[Save]`
20. Tunggu aksi selesai
21. Klik ikon Changelog pada toolbar Child Groups Quota
22. Verifikasi entri baru, dicari lewat Field `Allocated Quota`, Old Value `50`, dan New Value `60`, memakai Group Name `Divisi Logistik Pusat+{runId}-109`
23. Buka Filter Panel, buka dropdown `Group Name`
24. Verifikasi opsi Group Name memuat kedua nama `Divisi Logistik+{runId}-109` dan `Divisi Logistik Pusat+{runId}-109` sebagai snapshot historis
25. Tutup dropdown, tutup modal dengan `[×]`

### TC-FA-LIC-381: Satu aksi menghasilkan tepat satu entri per surface

26. Pulihkan Pre-setup #12 lewat fixture BE (grup milik spec kembali ke nama `Divisi Logistik+{runId}-109` tanpa alokasi)
27. Catat jumlah entri Changelog Allocation Quota, System Log Rudi Hartono, dan Activity Log (baseline) dan waktu acuan (menit saat ini, sebelum aksi pada langkah 28)
28. Buka License > Allocation Quota, klik node `Kantor Pusat`, klik `[Edit]` pada `Divisi Logistik`, isi `600`, klik `[Save]`
29. Tunggu aksi selesai
30. Klik ikon Changelog pada toolbar Child Groups Quota
31. Verifikasi jumlah entri Changelog bertambah tepat satu dari baseline
32. Verifikasi entri baru Divisi Logistik dengan Date ≥ waktu acuan langkah 27 tampil di Changelog
33. Verifikasi tidak ada entri baru di Changelog untuk Kantor Pusat, Divisi IT, atau grup lain
34. Tutup modal dengan `[×]`
35. Buka Global Settings > User, ketik Search `Rudi Hartono`, tekan Enter
36. Klik Name `Rudi Hartono`, buka Tab System Log
37. Verifikasi jumlah entri System Log bertambah tepat satu dari baseline
38. Verifikasi entri baru Divisi Logistik dengan Date ≥ waktu acuan langkah 27 tampil di System Log
39. Verifikasi tidak ada entri baru di System Log untuk Kantor Pusat, Divisi IT, atau grup lain
40. Buka Fixed Asset > Reports & Logs > Activity Log
41. Verifikasi jumlah entri Activity Log bertambah tepat satu dari baseline
42. Verifikasi entri baru Divisi Logistik dengan Date ≥ waktu acuan langkah 27 tampil di Activity Log
43. Verifikasi tidak ada entri baru di Activity Log untuk Kantor Pusat, Divisi IT, atau grup lain

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 dan 27 mencatat baseline dan waktu acuan; langkah 10, 25, dan 26 menutup modal dan memulihkan Pre-setup #12 antar blok (S-09); langkah 11 mengalokasikan grup milik spec sebagai sumber entri lama untuk TC-FA-LIC-380; langkah 5, 12, 15, 20, dan 29 menunggu aksi tulis selesai sebelum membuka log atau berpindah surface (bagian 8b butir 8); langkah 13 dan 14 mencari grup milik spec lewat Search sebelum Rename, dan langkah 35 dan 36 mencari baris `Rudi Hartono` lewat Search sebelum membuka Detail (R-16, bagian 8b butir 13); langkah 16 membuka Changelog pada node `All Groups`; langkah 19 menutup modal sebelum edit alokasi grup hasil rename (TC-FA-LIC-380 langkah 3).
- Cara baca entri (S-12, S-14): pada langkah 8 dan 9 entri hasil aksi dibaca sebagai himpunan dua baris teratas sebanyak selisih jumlah yang dibuktikan pada langkah 7, dengan kunci Date ≥ waktu acuan langkah 1 dan tanpa mengandalkan urutan di antara kedua baris, karena baris seed Pre-setup #27 memuat Group Name, Field, dan Old Value yang sama (Divisi Logistik `500`); jam server dan jam browser sinkron, fixture pemulih riwayat #27 dijalankan di hook `before` sehingga tidak ada entri bercap waktu masa depan dari spec lain di atas entri baru. Pada langkah 17 entri lama dicari dengan Group Name lama sebagai kunci, dan langkah 18 membuktikan tidak ada baris bernama baru untuk entri itu (anchor positif: langkah 17). Pada langkah 32, 38, dan 42 entri baru Divisi Logistik dari aksi langkah 28 dikenali lewat Date ≥ waktu acuan langkah 27, bukan lewat nama grup saja (nilai `600` dapat juga ada di entri lama grup bernama sama). Entri pada langkah 22 dicari lewat Field, Old Value, New Value, dan Group Name baru (nilai `50` ke `60` hanya dibuat spec ini).
- Absence di langkah 33, 39, dan 43 didahului `Verifikasi` entri baru milik Divisi Logistik pada surface yang sama (langkah 32, 38, dan 42) sebagai anchor positif (bagian 8b butir 2).
- Spec di atas 35 langkah (43 langkah): seluruh blok adalah pencatatan log snapshot pada tiga surface log yang sama; S-12 menuntut baseline dan `Verifikasi` selisih per surface sebelum isi entri dibaca, dan 8b.8 serta 8b.13 menambah langkah penghubung (Tunggu aksi selesai, Search baris target) yang tidak dapat digabung; tiap blok berdiri sendiri (dipulihkan fixture BE di awal blok).
- Cascade-delete grup beralokasi (TC-FA-LIC-382 dan TC-FA-LIC-602) ada di spec `TC-FA-LIC-E2E-143`.
- Temuan untuk QA:
  - TC-FA-LIC-380 langkah 4 meminta "Buka Filter Panel dan buka opsi `Group Name`" tanpa menyebut modal yang dipakai; spec memakai modal yang sama dengan langkah 17.
  - TC-FA-LIC-381 butir b ("tidak ada entri untuk Kantor Pusat, Divisi IT, atau grup lain") tidak menyebut surface; spec mengasersinya pada ketiga surface.
  - TC-FA-LIC-380 me-rename `Divisi Logistik` Pre-setup dengan prasyarat entri lama (29/09/26 10:05) dari Pre-setup #27; rename grup bernama literal tidak dapat dimiliki spec (S-06). Spec me-rename grup milik spec bersuffix, membuat entri lama sendiri lewat alokasi `50` (Old Value `—`) lalu mengedit ke `60`, bukan `500` dan `620`, karena Remaining Kantor Pusat 200 tidak cukup untuk 500; Date entri lama tidak diasersi.
