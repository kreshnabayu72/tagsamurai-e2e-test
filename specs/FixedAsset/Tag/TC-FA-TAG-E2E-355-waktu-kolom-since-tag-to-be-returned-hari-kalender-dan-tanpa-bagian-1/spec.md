---
id: TC-FA-TAG-E2E-355-waktu-kolom-since-tag-to-be-returned-hari-kalender-dan-tanpa-bagian-1
title: "Waktu: Kolom Since Hari ke-0 sampai ke-14 Tanpa Peringatan dan Tanpa Notifikasi Overdue pada Hari ke-7 sampai ke-30"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1255
  - TC-FA-TAG-1256
  - TC-FA-TAG-1257
  - TC-FA-TAG-1258
  - TC-FA-TAG-1353
  - TC-FA-TAG-1354
  - TC-FA-TAG-1355
  - TC-FA-TAG-1356
coverage:
  web: automated
---

# Waktu: Kolom Since Hari ke-0 sampai ke-14 Tanpa Peringatan dan Tanpa Notifikasi Overdue pada Hari ke-7 sampai ke-30

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor:
  - Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
  - Pengguna Budi S., pemegang Update di group Disposal Center (tidak ada di Pre-setup TC; disediakan tim FE), password `Spectra.env.FA_TAG_BUDI_DISPOSAL_PASSWORD` (nama env usulan; akun tersendiri untuk capability Update di group Disposal Center, tidak dipakai bersama spec 357 yang memakai akun Budi S. dengan Update di group Plant B, sehingga satu nama env hanya berarti satu capability). Dipakai pada langkah ganti akun (langkah 8 dan 9).
  - Nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk kedua akun, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): fixture timestamp masuk To Be Returned (umur Tag dalam hari kalender menurut zona waktu client); pemicu job harian sistem pada hari tertentu beserta kueri status job (menunggu job selesai memakai kueri status job dengan batas tunggu 2 menit, bagian 6); seed idempotent Tag To Be Returned dan satu notifikasi kontrol milik Budi S. (dipakai sebagai anchor positif, bukan butir Expected TC). Umur Tag dihitung dari fixture timestamp sehingga jam server dan jam browser tidak diubah spec ini.
- Jeda "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 14) sebelum asersi absence notifikasi in-app (langkah 15) adalah pilihan spec (bukan nilai TC atau PRD) sampai TC menyatakan durasinya (bagian 6); anchor positifnya adalah langkah 13.
- Data (tanpa suffix `{runId}` karena asersi bergantung pada kode persis): Tag [RFID] RF-00071 (Last Asset Excavator 20 Ton - 2, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.) berstatus To Be Returned dan belum dikembalikan.
- Tabel 1 (parameter langkah 2 sampai 7):

| Hari | Teks kolom Since |
|---|---|
| 0 | (0 days) |
| 1 | (1 day) |
| 7 | (7 days) |
| 14 | (14 days) |

- Tabel 2 (parameter langkah 10 sampai 15):

| Hari |
|---|
| 7 |
| 14 |
| 15 |
| 30 |

- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan Tag RF-00071 dan notifikasi Budi S. ke keadaan awal lewat fixture backend, lalu kembalikan sesi ke akun default suite.
- State global: tidak ada yang diubah selain data di atas. Suite serial (`parallel: false`).
- Nilai literal Pre-setup (kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengatur Tag RF-00071 To Be Returned lewat fixture timestamp (langkah 2, 10) serta memicu job harian sistem (langkah 11); PRD tag.md dan TC tidak menyatakan efek tak terpulihkan untuk job itu.

## Test Steps

### TC-FA-TAG-1353 sampai TC-FA-TAG-1356: kolom Since pada hari ke-0, 1, 7, 14

1. Buka Fixed Asset > TAG > To Be Returned

Untuk setiap baris Tabel 1 (langkah 2 sampai 7):

2. Atur fixture: Tag RF-00071 masuk To Be Returned sebanyak Hari hari kalender yang lalu menurut zona waktu client
3. Muat ulang halaman To Be Returned
4. Verifikasi kolom Since baris RF-00071 menampilkan tanggal masuk diikuti Teks kolom Since
5. Verifikasi Teks kolom Since tidak bertanda warning
6. Arahkan kursor ke Teks kolom Since
7. Verifikasi tidak ada tooltip batas pengembalian

### Ganti akun

8. Logout dari akun Total Control
9. Login sebagai Budi S.

### TC-FA-TAG-1255 sampai TC-FA-TAG-1258: tanpa notifikasi pengingat atau overdue

Untuk setiap baris Tabel 2 (langkah 10 sampai 15):

10. Atur fixture: Tag RF-00071 masuk To Be Returned sebanyak Hari hari kalender yang lalu dan belum dikembalikan
11. Jalankan job harian sistem pada hari ke-Hari lalu tunggu hingga job selesai (async job)
12. Muat ulang halaman lalu buka dropdown notifikasi
13. Verifikasi dropdown notifikasi tampil dan memuat notifikasi kontrol milik Budi S.
14. Tunggu 5 detik tanpa memuat ulang halaman
15. Verifikasi tidak ada notifikasi pengingat, Overdue, maupun usulan Report Missing untuk RF-00071

## Notes

- Spec harness eksternal waktu dan job latar (kelas d). Pemicu job dan umur Tag lewat fixture timestamp; tidak ada langkah "Tunggu" lebih dari 30 detik (R-10).
- Langkah yang diulang per baris tabel (bagian 8b butir 7): 2 sampai 7 dan 10 sampai 15. Parameter tiap iterasi ada di Tabel 1 dan Tabel 2 pada `## Prerequisites`; `Verifikasi` yang diulang tetap satu per klausa (S-01). Ekspansi: 1 + 4 x 6 + 2 + 4 x 6 = 51 langkah.
- Alasan melewati sekitar 35 langkah (bagian 3 prinsip 13): semua blok berada pada satu kelas harness (waktu dan job latar) dan berdiri sendiri; kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna karena tiap iterasi mengatur ulang fixture sendiri.
- Langkah penghubung (tanpa awalan `Verifikasi`): 1 (membuka tab), 3 (muat ulang), 6 (hover), 8 dan 9 (ganti akun), 12 (muat ulang dan buka dropdown), 14 (Tunggu 5 detik tanpa memuat ulang halaman, bagian 6).
- Anchor positif absence (bagian 8b butir 2): langkah 4 (untuk langkah 5 dan 7) dan langkah 13 (untuk langkah 15, dengan langkah Tunggu 5 detik tanpa memuat ulang halaman di antaranya). Anchor notifikasi kontrol pada langkah 13 adalah tambahan di luar Expected TC (S-03); alasannya agar hasil kosong bukan karena dropdown belum dimuat.
- A-15: nilai literal Pre-setup (kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengatur Tag RF-00071 To Be Returned lewat fixture timestamp (langkah 2, 10) serta memicu job harian sistem (langkah 11); PRD tag.md dan TC tidak menyatakan efek tak terpulihkan untuk job itu.
- Temuan untuk QA:
  - TC-FA-TAG-1255 sampai TC-FA-TAG-1258 tidak punya baris `Role:` di Precondition; aktor "Pengguna Budi S." tidak ada di Pre-setup. Spec menulisnya sebagai akun yang disediakan tim FE.
  - TC-FA-TAG-1255 sampai TC-FA-TAG-1258 memberi Budi S. Update di group Disposal Center, sedangkan TC-FA-TAG-1361 sampai TC-FA-TAG-1370 (spec 357) memberinya Update di group Plant B dan TC-FA-TAG-1242 memberinya Read; spec ini memakai akun dan env terpisah per capability (butir A-15: capability akun bersama tidak diubah) sampai QA memetakan nama ke akun.
  - TC-FA-TAG-1255 sampai TC-FA-TAG-1258 tidak menyebut cara menjalankan "job harian sistem pada hari ke-N"; spec menulisnya sebagai kemampuan pemicu job yang disediakan tim FE/BE.
  - TC-FA-TAG-1353 sampai TC-FA-TAG-1356 hanya menyebut "tidak ada tooltip batas pengembalian" tanpa langkah hover; spec menambah langkah penghubung 6 agar absence tooltip bermakna.
