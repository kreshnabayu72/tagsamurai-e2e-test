---
id: TC-FA-FAAM-E2E-234-state-tenant-pembacaan-tetap-berfungsi-dan-transisi-addon
title: "State Tenant Suspended dan Expired: Pembacaan Tetap Berfungsi dan Transisi Otomatis Addon Berjalan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-610
  - TC-FA-FAAM-624
coverage:
  web: automated
---

# State Tenant Suspended dan Expired: Pembacaan Tetap Berfungsi dan Transisi Otomatis Addon Berjalan

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor default (hook `before`): Total Control client utama `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Halaman dibuka hook `beforeEach` suite. Langkah 1 pada tiap iterasi tabel dan langkah 14 mengganti akun dan client secara eksplisit; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Tabel "Client yang diuji" untuk TC-FA-FAAM-624 (spec dijalankan untuk setiap baris; email Total Control tiap client tidak tertulis di Pre-setup TC dan disediakan tim FE):

  | Client | Pre-setup | Akun Total Control | Env |
  |---|---|---|---|
  | Suspended (plan Growth) | No. 18 | disediakan tim FE | `Spectra.env.FA_SUSP_TC_PASSWORD` |
  | Expired (plan Growth) | No. 18c | disediakan tim FE | `Spectra.env.FA_EXP_TC_PASSWORD` |

- Client TC-FA-FAAM-610: client Suspended dengan aset `pending_quota` (Pre-setup No. 18b); email Total Control disediakan tim FE, `Spectra.env.FA_SUSP_PENDING_TC_PASSWORD` (nama baru, didaftarkan di `spectra.config.ts` dan `.env.example` oleh pemilik repo).
- Env var: `FA_TC_PASSWORD`, `FA_SUSP_TC_PASSWORD`, `FA_EXP_TC_PASSWORD`, `FA_SUSP_PENDING_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): No. 18 dan 18c (salinan `Dell Latitude` sebagai baris yang dibaca di List, Detail, dan Download), No. 18b (aset `pending_quota` yang lisensi addon-nya baru tersedia).
- Kemampuan teknis: alokasi lisensi addon ke client lewat sesi API hingga tersimpan (kemampuan disediakan tim BE/FE); roster modul addon (mode baca); polling worker commit (muat ulang tiap 5 detik, batas 60 detik; bagian 6 konvensi); Download CSV.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): kembalikan alokasi lisensi addon dan status aset `pending_quota` client Pre-setup No. 18b ke keadaan awal lewat seed API; hapus berkas unduhan.
- State global yang diubah: alokasi lisensi addon client Pre-setup No. 18b (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-610 dan 624: login sebagai Total Control pada client yang bersangkutan dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### TC-FA-FAAM-624: Pembacaan List, Detail, Download, dan Changelog tetap berfungsi

Untuk setiap baris tabel "Client yang diuji" (langkah 1 sampai 12):

1. Logout lalu login sebagai Total Control pada client baris tabel
2. Buka Fixed Asset > Settings > Asset Master > Asset Name
3. Verifikasi List menampilkan sedikitnya satu baris mengikuti scope
4. Ketik Search `Dell Latitude`, tekan Enter
5. Klik nama `Dell Latitude`
6. Verifikasi Popup Detail `Dell Latitude` tampil
7. Tutup Popup Detail
8. Klik Download lalu CSV
9. Verifikasi berkas CSV terunduh
10. Klik icon Changelog
11. Verifikasi Modal Changelog tampil
12. Tutup Modal Changelog

### TC-FA-FAAM-610: Pada entitas Suspended transisi otomatis status Default Addon tetap berjalan

13. Buka Fixed Asset > Settings > Asset Master > Asset Name
14. Logout lalu login sebagai Total Control pada client Suspended dengan aset `pending_quota` (Pre-setup No. 18b)
15. Buka roster modul addon (mode baca)
16. Verifikasi aset `pending_quota` berstatus `pending_quota` di roster addon
17. Alokasikan lisensi addon ke client hingga tersimpan
18. Muat ulang roster addon tiap 5 detik sampai status aset berubah, batas 60 detik sejak langkah 17
19. Verifikasi di roster modul addon aset berpindah ke `enrolled_via_default`
20. Verifikasi client tetap berstatus Suspended

## Notes

- Langkah 1 sampai 12 diulang untuk baris Suspended lalu baris Expired (ekspansi 24 langkah); total ekspansi spec 32 langkah. Parameter tiap iterasi hanya akun dan client, ada di tabel Prerequisites.
- Langkah penghubung tanpa `Verifikasi`: langkah 2, 13 (navigasi), langkah 4 (Search untuk menemukan baris target), langkah 7 dan 12 (menutup popup atau modal), langkah 5, 8, 10 (membuka Popup Detail, Download, Changelog), langkah 14 (ganti akun eksplisit; S-07), langkah 15 (membuka roster), langkah 17 (pemicu alokasi lisensi; pelaku sistem), dan langkah 18 (idiom polling worker commit).
- Langkah 16 adalah anchor positif sebelum langkah 19; langkah 19 membuktikan perpindahan status tanpa asumsi urutan surface pemicu (status diamati di roster addon, bukan di surface alokasi lisensi).
- Pembagian TC lintas spec: TC-FA-FAAM-619 dan 620 ada di spec 233; TC-FA-FAAM-621, 622, 623 ada di spec 250.
- Temuan untuk QA:
  - Pre-setup No. 18, 18b, dan 18c tidak memuat email akun Total Control.
  - TC-FA-FAAM-624 butir a/b ("semua aksi baca berfungsi mengikuti scope") tidak menyebut scope; spec mengasersi tiap aksi baca tampil tanpa menyatakan isi.
  - TC-FA-FAAM-610 tidak menyebut pelaku "Alokasikan lisensi addon ke client"; spec memakai sesi API hingga tersimpan (kemampuan disediakan tim BE/FE).
