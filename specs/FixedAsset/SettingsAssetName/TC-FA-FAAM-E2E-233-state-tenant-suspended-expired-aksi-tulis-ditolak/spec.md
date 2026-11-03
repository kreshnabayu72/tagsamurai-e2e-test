---
id: TC-FA-FAAM-E2E-233-state-tenant-suspended-expired-aksi-tulis-ditolak
title: "State Tenant Suspended dan Expired: Create dan Edit Ditolak Server"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-619
  - TC-FA-FAAM-620
coverage:
  web: automated
---

# State Tenant Suspended dan Expired: Create dan Edit Ditolak Server

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor default (hook `before`): Total Control client utama `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Halaman dibuka hook `beforeEach` suite. Langkah 1 pada tiap iterasi tabel mengganti akun dan client secara eksplisit; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Tabel "Client yang diuji" (spec dijalankan untuk setiap baris; email Total Control tiap client tidak tertulis di Pre-setup TC dan disediakan tim FE):

  | Client | Pre-setup | Akun Total Control | Env |
  |---|---|---|---|
  | Suspended (plan Growth) | No. 18 | disediakan tim FE | `Spectra.env.FA_SUSP_TC_PASSWORD` |
  | Expired (plan Growth) | No. 18c | disediakan tim FE | `Spectra.env.FA_EXP_TC_PASSWORD` |

- Env var: `FA_TC_PASSWORD`, `FA_SUSP_TC_PASSWORD`, `FA_EXP_TC_PASSWORD` (nama baru, didaftarkan di `spectra.config.ts` dan `.env.example` oleh pemilik repo).
- Data Pre-setup (hanya dibaca, tidak berubah karena seluruh aksi tulis ditolak server): pada kedua client terdapat salinan `Dell Latitude` (Code `DLAT`), `Warehouse Pallet`, `Bulk Clean A`, dan `Bulk Clean B` (Total Asset 0 untuk tiga terakhir). Nama literal karena dipakai pada client khusus tanpa mutasi.
- Data uji: Asset Name `Blocked Create Item`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell`, UoM `Unit` (TC-FA-FAAM-619); Code `DLAT` menjadi `DLX` (TC-FA-FAAM-620).
- Kemampuan teknis: client Suspended dan Expired dengan akun Total Control (disediakan tim FE/BE).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan state client (status Suspended dan Expired) bila diubah; tidak ada data yang dibuat spec.
- State global yang diubah: tidak ada (status client tidak diubah spec ini). Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-619 dan 620: login sebagai Total Control pada client Suspended (lalu Expired) dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

Untuk setiap baris tabel "Client yang diuji" (langkah 1 sampai 23):

1. Logout lalu login sebagai Total Control pada client baris tabel
2. Buka Fixed Asset > Settings > Asset Master > Asset Name
3. Klik `[+ Asset Name]`
4. Isi Asset Name `Blocked Create Item`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell`, UoM `Unit`
5. Klik `[Submit]`
6. Verifikasi server menolak dengan 403 Forbidden
7. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.`
8. Klik `✕` pada Modal Create
9. Verifikasi dialog `Unsaved Changes`
10. Klik `[Leave]`
11. Ketik Search `Dell Latitude`, tekan Enter
12. Klik `⋯` baris `Dell Latitude` lalu `Edit`
13. Ubah Code dari `DLAT` menjadi `DLX`
14. Klik `[Save]`
15. Verifikasi server menolak dengan 403 Forbidden
16. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.`
17. Klik `✕` pada Modal Edit
18. Verifikasi dialog `Unsaved Changes`
19. Klik `[Leave]`
20. Muat ulang List dan ketik Search `Blocked Create Item`, tekan Enter
21. Verifikasi empty state `No results found`, sehingga `Blocked Create Item` tidak tercipta
22. Ganti isi kotak search dengan `Dell Latitude`, tekan Enter
23. Verifikasi Code baris `Dell Latitude` tetap `DLAT`

## Notes

- Langkah 1 sampai 23 diulang untuk baris Suspended lalu baris Expired (ekspansi 46 langkah). Di atas ~35 karena alasan berikut: kedua client memakai langkah identik, seluruh blok kelas h (state tenant), dan memisahkan per client akan memecah TC-FA-FAAM-619 dan 620 ke dua spec (satu TC satu spec). Parameter tiap iterasi hanya akun dan client, ada di tabel Prerequisites.
- TC-FA-FAAM-619 dan 620 menyebut "Ulangi langkah 1 pada Client Expired"; urutan final per client (bukan per TC) agar login client tidak berulang. Perubahan urutan ini dicatat sebagai keputusan penulis.
- Langkah penghubung tanpa `Verifikasi`: langkah 11 dan 20 (Search), langkah 8, 10, 17, 19 (menutup form dirty secara deterministik; S-08), dan langkah 2.
- Langkah 21 adalah asersi absence dengan anchor empty state `No results found` hasil Search. Langkah 23 mengasersi Code tidak berubah (tanpa mutasi) dengan anchor baris `Dell Latitude` tampil; langkah 22 adalah Search.
- Pembagian TC lintas spec: TC-FA-FAAM-621, 622, 623 ada di spec 250; TC-FA-FAAM-610 dan 624 ada di spec 234. Absence entri log atas Create dan Edit yang ditolak ada di spec 253 (TC-FA-FAAM-842).
- Temuan untuk QA:
  - Pre-setup No. 18 dan 18c tidak memuat email akun Total Control untuk client Suspended dan Expired.
  - Teks toast dan isi 403 hanya diasersi pada UI; TC tidak menyebut apakah respons 403 diamati lewat intercept jaringan.
