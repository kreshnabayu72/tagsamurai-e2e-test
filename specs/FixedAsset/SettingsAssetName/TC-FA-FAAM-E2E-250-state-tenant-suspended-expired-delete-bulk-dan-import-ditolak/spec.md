---
id: TC-FA-FAAM-E2E-250-state-tenant-suspended-expired-delete-bulk-dan-import-ditolak
title: "State Tenant Suspended dan Expired: Delete, Bulk Delete, dan Import Ditolak Server"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-621
  - TC-FA-FAAM-622
  - TC-FA-FAAM-623
coverage:
  web: automated
---

# State Tenant Suspended dan Expired: Delete, Bulk Delete, dan Import Ditolak Server

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor default (hook `before`): Total Control client utama `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Halaman dibuka hook `beforeEach` suite. Langkah 1 pada tiap iterasi tabel mengganti akun dan client secara eksplisit; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Tabel "Client yang diuji" (spec dijalankan untuk setiap baris; email Total Control tiap client tidak tertulis di Pre-setup TC dan disediakan tim FE; keduanya pada plan Growth sehingga modul Import tersedia):

  | Client | Pre-setup | Akun Total Control | Env |
  |---|---|---|---|
  | Suspended (plan Growth) | No. 18 | disediakan tim FE | `Spectra.env.FA_SUSP_TC_PASSWORD` |
  | Expired (plan Growth) | No. 18c | disediakan tim FE | `Spectra.env.FA_EXP_TC_PASSWORD` |

- Env var: `FA_TC_PASSWORD`, `FA_SUSP_TC_PASSWORD`, `FA_EXP_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca, tidak berubah karena seluruh aksi tulis ditolak server): pada kedua client terdapat salinan `Dell Latitude`, `Warehouse Pallet`, `Bulk Clean A`, dan `Bulk Clean B` (Total Asset 0 untuk tiga terakhir). Nama literal karena dipakai pada client khusus tanpa mutasi.
- Data uji: Asset Name `Warehouse Pallet` (TC-FA-FAAM-621), `Bulk Clean A` dan `Bulk Clean B` (TC-FA-FAAM-622), baris impor `Blocked Import Item` (TC-FA-FAAM-623; berkas impor satu baris disediakan tim FE).
- Kemampuan teknis: client Suspended dan Expired dengan akun Total Control; modul Import tab Asset Name pada plan Growth.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan state client bila diubah; tidak ada data yang dibuat spec.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-621, 622, 623: login sebagai Total Control pada client Suspended (lalu Expired) dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

Untuk setiap baris tabel "Client yang diuji" (langkah 1 sampai 25):

1. Logout lalu login sebagai Total Control pada client baris tabel
2. Buka Fixed Asset > Settings > Asset Master > Asset Name
3. Ketik Search `Warehouse Pallet`, tekan Enter
4. Klik `⋯` baris `Warehouse Pallet` lalu `Delete`
5. Klik `[Delete]`
6. Verifikasi server menolak dengan 403 Forbidden
7. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.`
8. Ganti isi kotak search dengan `Bulk Clean`, tekan Enter
9. Centang `Bulk Clean A` dan `Bulk Clean B`
10. Klik `Bulk Action` lalu `Delete`
11. Klik `[Delete]`
12. Verifikasi server menolak dengan 403 Forbidden
13. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.`
14. Klik Unselect All
15. Buka modul Import tab Asset Name
16. Impor satu baris Asset Name baru `Blocked Import Item` lewat modul Import
17. Verifikasi server menolak dengan 403 Forbidden
18. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.`
19. Buka Fixed Asset > Settings > Asset Master > Asset Name
20. Muat ulang List dan ketik Search `Warehouse Pallet`, tekan Enter
21. Verifikasi baris `Warehouse Pallet` masih ada
22. Ganti isi kotak search dengan `Bulk Clean`, tekan Enter
23. Verifikasi baris `Bulk Clean A` dan `Bulk Clean B` masih ada
24. Ganti isi kotak search dengan `Blocked Import Item`, tekan Enter
25. Verifikasi empty state `No results found`, sehingga `Blocked Import Item` tidak tercipta

## Notes

- Langkah 1 sampai 25 diulang untuk baris Suspended lalu baris Expired (ekspansi 50 langkah). Di atas ~35 karena alasan berikut: kedua client memakai langkah identik, seluruh blok kelas h (state tenant), dan memisahkan per client akan memecah tiga TC ke dua spec (satu TC satu spec). Parameter tiap iterasi hanya akun dan client, ada di tabel Prerequisites.
- Urutan final per client (bukan per TC) agar login client tidak berulang; TC-FA-FAAM-621, 622, 623 menyebut "Ulangi langkah 1 pada Client Expired". Aksi Delete dan Bulk Delete ditolak sehingga tidak ada data yang dihapus.
- Langkah penghubung tanpa `Verifikasi`: langkah 2, 15, 19 (navigasi), langkah 3, 8, 20, 22, 24 (Search), dan langkah 14 (Unselect All; S-09).
- Langkah 25 adalah asersi absence dengan anchor empty state `No results found` hasil Search; langkah 21 dan 23 mengasersi baris yang tetap ada.
- Pembagian TC lintas spec: TC-FA-FAAM-619 dan 620 ada di spec 233; TC-FA-FAAM-610 dan 624 ada di spec 234. Absence entri log atas Delete, Bulk Delete, dan Import yang ditolak ada di spec 254 (TC-FA-FAAM-843).
- Temuan untuk QA:
  - Pre-setup No. 18 dan 18c tidak memuat email akun Total Control untuk client Suspended dan Expired.
  - TC-FA-FAAM-623 tidak menyebut format berkas impor; disediakan tim FE.
