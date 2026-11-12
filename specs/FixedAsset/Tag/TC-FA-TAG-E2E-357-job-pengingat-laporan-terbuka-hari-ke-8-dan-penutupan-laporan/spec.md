---
id: TC-FA-TAG-E2E-357-job-pengingat-laporan-terbuka-hari-ke-8-dan-penutupan-laporan
title: "Job Pengingat: Laporan Terbuka Mendapat Pengingat Tepat pada Hari ke-8 dan Tidak pada Kondisi Lain"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-1361
  - TC-FA-TAG-1362
  - TC-FA-TAG-1363
  - TC-FA-TAG-1364
  - TC-FA-TAG-1365
  - TC-FA-TAG-1366
  - TC-FA-TAG-1367
  - TC-FA-TAG-1368
  - TC-FA-TAG-1369
  - TC-FA-TAG-1370
coverage:
  web: automated
---

# Job Pengingat: Laporan Terbuka Mendapat Pengingat Tepat pada Hari ke-8 dan Tidak pada Kondisi Lain

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor:
  - Pengguna Budi S., pemegang Update di group Plant B (tidak ada di Pre-setup TC; disediakan tim FE), password `Spectra.env.FA_TAG_BUDI_PLANT_B_PASSWORD` (nama env usulan; akun tersendiri untuk capability Update di group Plant B, tidak dipakai bersama spec 355 yang memakai akun Budi S. dengan Update di group Disposal Center, sehingga satu nama env hanya berarti satu capability). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
  - Pengguna Maya R., pemegang Update hanya di group Plant A (tidak ada di Pre-setup TC; disediakan tim FE), password `Spectra.env.FA_TAG_MAYA_PASSWORD` (nama env usulan). Dipakai pada langkah ganti akun (langkah 27 dan 28).
  - Akun admin untuk mengubah status entitas Client (tidak ada di Pre-setup TC; disediakan tim FE sebagai kemampuan, langkah 19 dan 20).
  - Nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk kedua akun, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): fixture timestamp pembuatan dan penutupan laporan Tag (umur dalam hari kalender menurut zona waktu client); pemicu job pengingat laporan harian beserta kueri status job (menunggu job selesai memakai kueri status job dengan batas tunggu 2 menit, bagian 6); perubahan dan pemulihan status entitas Client (Active, Suspended); seed idempotent laporan, aset, dan satu notifikasi kontrol per pengguna, serta penghapusan notifikasi pengingat tertentu milik pengguna (tanpa menghapus notifikasi kontrol) (dipakai sebagai anchor positif, bukan butir Expected TC). Umur laporan dihitung dari fixture timestamp sehingga jam server dan jam browser tidak diubah spec ini.
- Data (tanpa suffix `{runId}` karena asersi bergantung pada kode persis): aset AST-0020 'Excavator 20 Ton - 20' (Group Plant B) dengan Tag RF-00130 punya laporan terbuka Damaged; aset AST-0044 'Excavator 20 Ton - 44' (Group Plant B) dengan Tag RF-00132 dan QR-00232 (hanya TC-FA-TAG-1370). Umur laporan diatur per langkah.
- Tabel 1 (parameter langkah 1 sampai 5):

| Hari |
|---|
| 0 |
| 7 |

- Tabel 2 (parameter langkah 14 sampai 18):

| Status penutupan | Keterangan |
|---|---|
| Declined | laporan dibuat 8 hari kalender yang lalu dan ditutup Declined pada hari ke-5 |
| Canceled | laporan dibuat 8 hari kalender yang lalu dan ditutup Canceled pada hari ke-5 |
| Replaced | laporan dibuat 8 hari kalender yang lalu dan ditutup Replaced oleh Replace TAG pada hari ke-5 |

- Notifikasi in-app bersifat persisten: pengingat "TAG report is still open" yang dibuat job pada langkah 6 tetap ada di dropdown Budi S. pada langkah berikutnya. Langkah 13 menghapus notifikasi "TAG report is still open" untuk RF-00130, RF-00132, dan QR-00232 milik Budi S. lewat fixture backend (disediakan tim FE/BE; notifikasi kontrol tidak dihapus) sebelum blok TC-FA-TAG-1365 sampai TC-FA-TAG-1367, sehingga absence pada langkah 18 dan `Verifikasi` notifikasi pada langkah 22, 25, dan 26 berasal dari run ini; hook `before` menghapus notifikasi yang sama sisa run sebelumnya. Jeda "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 4, 17, dan 32) sebelum asersi absence notifikasi adalah pilihan spec (bukan nilai TC atau PRD) sampai TC menyatakan durasinya (bagian 6).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan status entitas Client ke Active, laporan, notifikasi (termasuk menghapus notifikasi pengingat "TAG report is still open" untuk RF-00130, RF-00132, dan QR-00232 milik Budi S. dan Maya R.), dan aset ke keadaan awal lewat fixture backend, lalu kembalikan sesi ke akun default suite.
- State global: status entitas Client diubah pada langkah 19 dan dipulihkan pada langkah 20. Suite serial (`parallel: false`).
- Nilai literal Pre-setup (ID aset AST-*, Asset Name, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG lewat UI, dan laporan beserta penutupannya (Declined, Canceled, Replaced) dibuat lewat fixture timestamp (langkah 1, 6, 10, 14, 19, 23, 29) tanpa pernyataan PRD tag.md atau TC tentang entri log dari fixture itu; PRD tag.md dan TC juga tidak menyatakan efek tak terpulihkan untuk job pengingat harian (langkah 1, 6, 10, 14, 19, 23, 29).

## Test Steps

### TC-FA-TAG-1361 dan TC-FA-TAG-1362: hari ke-0 dan hari ke-7

Untuk setiap baris Tabel 1 (langkah 1 sampai 5):

1. Atur fixture: laporan terbuka Damaged untuk Tag RF-00130 pada AST-0020 dibuat Hari hari kalender yang lalu, lalu jalankan job pengingat laporan harian dan tunggu hingga job selesai (async job)
2. Muat ulang halaman lalu buka dropdown notifikasi
3. Verifikasi dropdown notifikasi tampil dan memuat notifikasi kontrol milik Budi S.
4. Tunggu 5 detik tanpa memuat ulang halaman
5. Verifikasi tidak ada notifikasi "TAG report is still open" untuk RF-00130

### TC-FA-TAG-1363: hari ke-8 dikirim

6. Atur fixture: laporan terbuka Damaged untuk Tag RF-00130 pada AST-0020 dibuat 8 hari kalender yang lalu, lalu jalankan job pengingat laporan harian dan tunggu hingga job selesai (async job)
7. Muat ulang halaman lalu buka dropdown notifikasi
8. Verifikasi tepat satu notifikasi "TAG report is still open" dengan isi "The report on RF-00130 (AST-0020) is still waiting for action." tampil
9. Verifikasi notifikasi itu tampil bersama tombol aksi dan [Mark as Read]

### TC-FA-TAG-1364: hari ke-9 tidak dikirim ulang

10. Atur fixture: laporan terbuka Damaged untuk Tag RF-00130 pada AST-0020 dibuat 9 hari kalender yang lalu dengan pengingat hari ke-8 sudah terkirim, lalu jalankan job pengingat laporan harian dan tunggu hingga job selesai (async job)
11. Muat ulang halaman lalu buka dropdown notifikasi
12. Verifikasi jumlah notifikasi "TAG report is still open" untuk RF-00130 tetap satu

### TC-FA-TAG-1365 sampai TC-FA-TAG-1367: laporan ditutup sebelum hari ke-8

13. Bersihkan lewat fixture backend: notifikasi "TAG report is still open" untuk RF-00130, RF-00132, dan QR-00232 milik Budi S. (notifikasi kontrol tidak dihapus), karena pengingat dari langkah 6 tetap tersimpan

Untuk setiap baris Tabel 2 (langkah 14 sampai 18):
14. Atur fixture: laporan Damaged untuk RF-00130 pada AST-0020 dengan Keterangan, lalu jalankan job pengingat laporan harian dan tunggu hingga job selesai (async job)
15. Muat ulang halaman lalu buka dropdown notifikasi
16. Verifikasi dropdown notifikasi tampil dan memuat notifikasi kontrol milik Budi S.
17. Tunggu 5 detik tanpa memuat ulang halaman
18. Verifikasi tidak ada notifikasi "TAG report is still open" untuk RF-00130

### TC-FA-TAG-1368: entitas Suspended

19. Atur fixture: laporan terbuka Damaged untuk RF-00130 pada AST-0020 dibuat 8 hari kalender yang lalu, status entitas Client Suspended, lalu jalankan job pengingat laporan harian dan tunggu hingga job selesai (async job)
20. Pulihkan status entitas Client ke Active
21. Muat ulang halaman lalu buka dropdown notifikasi
22. Verifikasi notifikasi "TAG report is still open" untuk RF-00130 tampil

### TC-FA-TAG-1370: dua laporan terbuka

23. Atur fixture: laporan terbuka untuk RF-00132 dan QR-00232 pada AST-0044 dibuat 8 hari kalender yang lalu, lalu jalankan job pengingat laporan harian dan tunggu hingga job selesai (async job)
24. Muat ulang halaman lalu buka dropdown notifikasi
25. Verifikasi satu notifikasi "TAG report is still open" untuk RF-00132 tampil
26. Verifikasi satu notifikasi "TAG report is still open" untuk QR-00232 tampil

### Ganti akun

27. Logout dari akun Budi S.
28. Login sebagai Maya R.

### TC-FA-TAG-1369: hanya pemegang Update dalam scope group

29. Atur fixture: laporan terbuka Damaged untuk RF-00130 pada AST-0020 dibuat 8 hari kalender yang lalu, lalu jalankan job pengingat laporan harian dan tunggu hingga job selesai (async job)
30. Muat ulang halaman lalu buka dropdown notifikasi
31. Verifikasi dropdown notifikasi tampil dan memuat notifikasi kontrol milik Maya R.
32. Tunggu 5 detik tanpa memuat ulang halaman
33. Verifikasi tidak ada notifikasi "TAG report is still open" untuk RF-00130 pada Maya R.

## Notes

- Spec harness eksternal job latar (kelas d). Pemicu job dan umur laporan lewat fixture timestamp; tidak ada langkah "Tunggu" lebih dari 30 detik (R-10).
- Langkah yang diulang per baris tabel (bagian 8b butir 7): 1 sampai 5 dan 14 sampai 18. Parameter tiap iterasi ada di Tabel 1 dan Tabel 2 pada `## Prerequisites`; `Verifikasi` yang diulang tetap satu per klausa (S-01). Ekspansi: 2 x 5 + 4 + 3 + 1 + 3 x 5 + 4 + 4 + 7 = 48 langkah.
- Alasan melewati sekitar 35 langkah (bagian 3 prinsip 13): semua blok berada pada satu kelas harness (job latar pengingat) dan berdiri sendiri; tiap iterasi mengatur ulang fixture laporan dan menjalankan job sendiri.
- Langkah penghubung (tanpa awalan `Verifikasi`): 2, 7, 11, 15, 21, 24, 30 (memuat ulang halaman dan membuka dropdown), 13 (pembersihan notifikasi pengingat lewat fixture, S-09), 20 (pemulihan state global, S-09), 27 dan 28 (ganti akun), 4, 17, dan 32 (Tunggu 5 detik tanpa memuat ulang halaman, bagian 6).
- Anchor positif absence (bagian 8b butir 2): langkah 3 untuk langkah 5, langkah 16 untuk langkah 18, dan langkah 31 untuk langkah 33, masing-masing dengan langkah Tunggu 5 detik tanpa memuat ulang halaman di antaranya (langkah 4, 17, dan 32). Notifikasi kontrol adalah tambahan di luar Expected TC (S-03); alasannya agar hasil kosong bukan karena dropdown belum dimuat. TC-FA-TAG-1364 (jumlah tetap satu) dan TC-FA-TAG-1363 mengasersi keberadaan, sehingga tidak butuh anchor tambahan.
- Urutan: TC-FA-TAG-1369 ditaruh terakhir karena memakai ganti akun ke Maya R.; urutan di TC tidak dipertahankan agar ganti akun hanya sekali.
- A-15: nilai literal Pre-setup (ID aset AST-*, Asset Name, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG lewat UI, dan laporan beserta penutupannya (Declined, Canceled, Replaced) dibuat lewat fixture timestamp (langkah 1, 6, 10, 14, 19, 23, 29) tanpa pernyataan PRD tag.md atau TC tentang entri log dari fixture itu; PRD tag.md dan TC juga tidak menyatakan efek tak terpulihkan untuk job pengingat harian (langkah 1, 6, 10, 14, 19, 23, 29).
- Temuan untuk QA:
  - TC-FA-TAG-1361 sampai TC-FA-TAG-1370 tidak punya baris `Role:` di Precondition; aktor "Pengguna Budi S." dan "Maya R." tidak ada di Pre-setup. Spec menulisnya sebagai akun yang disediakan tim FE.
  - TC-FA-TAG-1361 sampai TC-FA-TAG-1370 memberi Budi S. Update di group Plant B, sedangkan TC-FA-TAG-1255 sampai TC-FA-TAG-1258 (spec 355) memberinya Update di group Disposal Center; spec ini memakai akun dan env terpisah per capability (butir A-15: capability akun bersama tidak diubah) sampai QA memetakan nama ke akun.
  - TC-FA-TAG-1361 sampai TC-FA-TAG-1370 tidak menyebut cara menjalankan job pengingat laporan harian; spec menulisnya sebagai kemampuan pemicu job yang disediakan tim FE/BE.
  - TC-FA-TAG-1370 tidak menyebut aset dan Tag milik Maya R.; TC-FA-TAG-1369 mengasersi Maya R. hanya untuk RF-00130.
  - TC-FA-TAG-1368 tidak menyebut siapa yang memulihkan entitas ke Active dan cara menjalankannya; spec memakai akun admin yang disediakan tim FE.
