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
  - Pengguna Budi S., pemegang Update di group Plant B (tidak ada di Pre-setup TC; disediakan tim FE), password `Spectra.env.FA_TAG_BUDI_PASSWORD` (nama env usulan). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
  - Pengguna Maya R., pemegang Update hanya di group Plant A (tidak ada di Pre-setup TC; disediakan tim FE), password `Spectra.env.FA_TAG_MAYA_PASSWORD` (nama env usulan). Dipakai pada langkah ganti akun (langkah 24 dan 25).
  - Akun admin untuk mengubah status entitas Client (tidak ada di Pre-setup TC; disediakan tim FE sebagai kemampuan, langkah 16 dan 17).
  - Nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk kedua akun, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): fixture timestamp pembuatan dan penutupan laporan Tag (umur dalam hari kalender menurut zona waktu client); pemicu job pengingat laporan harian beserta kueri status job (menunggu job selesai memakai kueri status job dengan batas tunggu 2 menit, bagian 6); perubahan dan pemulihan status entitas Client (Active, Suspended); seed idempotent laporan, aset, dan satu notifikasi kontrol per pengguna (dipakai sebagai anchor positif, bukan butir Expected TC). Umur laporan dihitung dari fixture timestamp sehingga jam server dan jam browser tidak diubah spec ini.
- Data (tanpa suffix `{runId}` karena asersi bergantung pada kode persis): aset AST-0020 'Excavator 20 Ton - 20' (Group Plant B) dengan Tag RF-00130 punya laporan terbuka Damaged; aset AST-0044 'Excavator 20 Ton - 44' (Group Plant B) dengan Tag RF-00132 dan QR-00232 (hanya TC-FA-TAG-1370). Umur laporan diatur per langkah.
- Tabel 1 (parameter langkah 1 sampai 4):

| Hari |
|---|
| 0 |
| 7 |

- Tabel 2 (parameter langkah 12 sampai 15):

| Status penutupan | Keterangan |
|---|---|
| Declined | laporan dibuat 8 hari kalender yang lalu dan ditutup Declined pada hari ke-5 |
| Canceled | laporan dibuat 8 hari kalender yang lalu dan ditutup Canceled pada hari ke-5 |
| Replaced | laporan dibuat 8 hari kalender yang lalu dan ditutup Replaced oleh Replace TAG pada hari ke-5 |

- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan status entitas Client ke Active, laporan, notifikasi, dan aset ke keadaan awal lewat fixture backend, lalu kembalikan sesi ke akun default suite.
- State global: status entitas Client diubah pada langkah 16 dan dipulihkan pada langkah 17. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1361 dan TC-FA-TAG-1362: hari ke-0 dan hari ke-7

Untuk setiap baris Tabel 1 (langkah 1 sampai 4):

1. Atur fixture: laporan terbuka Damaged untuk Tag RF-00130 pada AST-0020 dibuat Hari hari kalender yang lalu, lalu jalankan job pengingat laporan harian dan tunggu hingga job selesai (async job)
2. Muat ulang halaman lalu buka dropdown notifikasi
3. Verifikasi dropdown notifikasi tampil dan memuat notifikasi kontrol milik Budi S.
4. Verifikasi tidak ada notifikasi "TAG report is still open" untuk RF-00130

### TC-FA-TAG-1363: hari ke-8 dikirim

5. Atur fixture: laporan terbuka Damaged untuk Tag RF-00130 pada AST-0020 dibuat 8 hari kalender yang lalu, lalu jalankan job pengingat laporan harian dan tunggu hingga job selesai (async job)
6. Muat ulang halaman lalu buka dropdown notifikasi
7. Verifikasi tepat satu notifikasi "TAG report is still open" dengan isi "The report on RF-00130 (AST-0020) is still waiting for action." tampil
8. Verifikasi notifikasi itu tampil bersama tombol aksi dan [Mark as Read]

### TC-FA-TAG-1364: hari ke-9 tidak dikirim ulang

9. Atur fixture: laporan terbuka Damaged untuk Tag RF-00130 pada AST-0020 dibuat 9 hari kalender yang lalu dengan pengingat hari ke-8 sudah terkirim, lalu jalankan job pengingat laporan harian dan tunggu hingga job selesai (async job)
10. Muat ulang halaman lalu buka dropdown notifikasi
11. Verifikasi jumlah notifikasi "TAG report is still open" untuk RF-00130 tetap satu

### TC-FA-TAG-1365 sampai TC-FA-TAG-1367: laporan ditutup sebelum hari ke-8

Untuk setiap baris Tabel 2 (langkah 12 sampai 15):

12. Atur fixture: laporan Damaged untuk RF-00130 pada AST-0020 dengan Keterangan, lalu jalankan job pengingat laporan harian dan tunggu hingga job selesai (async job)
13. Muat ulang halaman lalu buka dropdown notifikasi
14. Verifikasi dropdown notifikasi tampil dan memuat notifikasi kontrol milik Budi S.
15. Verifikasi tidak ada notifikasi "TAG report is still open" untuk RF-00130

### TC-FA-TAG-1368: entitas Suspended

16. Atur fixture: laporan terbuka Damaged untuk RF-00130 pada AST-0020 dibuat 8 hari kalender yang lalu, status entitas Client Suspended, lalu jalankan job pengingat laporan harian dan tunggu hingga job selesai (async job)
17. Pulihkan status entitas Client ke Active
18. Muat ulang halaman lalu buka dropdown notifikasi
19. Verifikasi notifikasi "TAG report is still open" untuk RF-00130 tampil

### TC-FA-TAG-1370: dua laporan terbuka

20. Atur fixture: laporan terbuka untuk RF-00132 dan QR-00232 pada AST-0044 dibuat 8 hari kalender yang lalu, lalu jalankan job pengingat laporan harian dan tunggu hingga job selesai (async job)
21. Muat ulang halaman lalu buka dropdown notifikasi
22. Verifikasi satu notifikasi "TAG report is still open" untuk RF-00132 tampil
23. Verifikasi satu notifikasi "TAG report is still open" untuk QR-00232 tampil

### Ganti akun

24. Logout dari akun Budi S.
25. Login sebagai Maya R.

### TC-FA-TAG-1369: hanya pemegang Update dalam scope group

26. Atur fixture: laporan terbuka Damaged untuk RF-00130 pada AST-0020 dibuat 8 hari kalender yang lalu, lalu jalankan job pengingat laporan harian dan tunggu hingga job selesai (async job)
27. Muat ulang halaman lalu buka dropdown notifikasi
28. Verifikasi dropdown notifikasi tampil dan memuat notifikasi kontrol milik Maya R.
29. Verifikasi tidak ada notifikasi "TAG report is still open" untuk RF-00130 pada Maya R.

## Notes

- Spec harness eksternal job latar (kelas d). Pemicu job dan umur laporan lewat fixture timestamp; tidak ada langkah "Tunggu" lebih dari 30 detik (R-10).
- Langkah yang diulang per baris tabel (bagian 8b butir 7): 1 sampai 4 dan 12 sampai 15. Parameter tiap iterasi ada di Tabel 1 dan Tabel 2 pada `## Prerequisites`; `Verifikasi` yang diulang tetap satu per klausa (S-01). Ekspansi: 2 x 4 + 4 + 3 + 3 x 4 + 4 + 4 + 6 = 41 langkah.
- Alasan melewati sekitar 35 langkah (bagian 3 prinsip 13): semua blok berada pada satu kelas harness (job latar pengingat) dan berdiri sendiri; tiap iterasi mengatur ulang fixture laporan dan menjalankan job sendiri.
- Langkah penghubung (tanpa awalan `Verifikasi`): 2, 6, 10, 13, 18, 21, 27 (memuat ulang halaman dan membuka dropdown), 17 (pemulihan state global, S-09), 24 dan 25 (ganti akun).
- Anchor positif absence (bagian 8b butir 2): langkah 3 untuk langkah 4, langkah 14 untuk langkah 15, dan langkah 28 untuk langkah 29. Notifikasi kontrol adalah tambahan di luar Expected TC (S-03); alasannya agar hasil kosong bukan karena dropdown belum dimuat. TC-FA-TAG-1364 (jumlah tetap satu) dan TC-FA-TAG-1363 mengasersi keberadaan, sehingga tidak butuh anchor tambahan.
- Urutan: TC-FA-TAG-1369 ditaruh terakhir karena memakai ganti akun ke Maya R.; urutan di TC tidak dipertahankan agar ganti akun hanya sekali.
- Temuan untuk QA:
  - TC-FA-TAG-1361 sampai TC-FA-TAG-1370 tidak punya baris `Role:` di Precondition; aktor "Pengguna Budi S." dan "Maya R." tidak ada di Pre-setup. Spec menulisnya sebagai akun yang disediakan tim FE.
  - TC-FA-TAG-1361 sampai TC-FA-TAG-1370 tidak menyebut cara menjalankan job pengingat laporan harian; spec menulisnya sebagai kemampuan pemicu job yang disediakan tim FE/BE.
  - TC-FA-TAG-1370 tidak menyebut aset dan Tag milik Maya R.; TC-FA-TAG-1369 mengasersi Maya R. hanya untuk RF-00130.
  - TC-FA-TAG-1368 tidak menyebut siapa yang memulihkan entitas ke Active dan cara menjalankannya; spec memakai akun admin yang disediakan tim FE.
  - Nilai literal Pre-setup (ID aset, kode Tag) tidak bisa bersuffix `{runId}` karena asersi bergantung pada kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
