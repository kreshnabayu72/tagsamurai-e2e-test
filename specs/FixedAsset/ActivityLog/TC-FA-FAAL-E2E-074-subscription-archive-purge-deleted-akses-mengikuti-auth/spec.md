---
id: TC-FA-FAAL-E2E-074-subscription-archive-purge-deleted-akses-mengikuti-auth
title: "State Tenant: Subscription Archive, Purge, dan Deleted, Akses Activity Log Mengikuti Auth"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAL-289
coverage:
  web: automated
---

# State Tenant: Subscription Archive, Purge, dan Deleted, Akses Activity Log Mengikuti Auth

## Prerequisites

- Mode: FE+BE (backend nyata; status subscription diubah lewat fixture BE, tanpa intercept).
- Akun aktor: Total Control tiap client pada tabel di bawah (Pre-setup #16). Email dan password akun tiap client tidak tertulis di Pre-setup TC dan disediakan tim FE (lihat Temuan untuk QA). Hook `before` spec ini login ke akun default suite; tiap iterasi memakai langkah ganti akun eksplisit. Hook `after` mengembalikan sesi ke akun default suite. Pengecualian hook `beforeEach` suite: langkah 1 membuka Activity Log sendiri di client iterasi karena layar awal hook dibuka pada akun default.
- Iterasi (parameter langkah 1 sampai 15, satu iterasi per baris):

  | Iterasi | Client | Status subscription Fixed Asset yang diset |
  |---|---|---|
  | 1 | Client pertama | Archive |
  | 2 | Client kedua | Purge |
  | 3 | Client ketiga | Deleted |

- Data Pre-setup: tiga client dengan subscription Fixed Asset berstatus Active (satu per client), masing-masing dengan sesi-produk Fixed Asset yang sudah dibuka; status diubah oleh langkah 2 (#16). Identitas data dirujuk lewat `fixtures/activity-log.json` (belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Uji dari TC sumber: status subscription Archive, Purge, Deleted.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): mengubah status subscription Fixed Asset ke Archive, Purge, dan Deleted lewat seed BE; menyediakan tiga client berstatus Active dengan sesi-produk terbuka sebelum spec berjalan; membaca respons jaringan halaman Activity Log untuk menyatakan permintaan ditolak server; memulihkan ketiga client ke Active. Status Purge dan Deleted tidak dapat dibalik lewat UI; pemulihan dijamin fixture BE yang menyediakan client yang sama atau client pengganti Active setiap run.
- State global yang diubah dan pemulihannya: status subscription ketiga client; pemulihan oleh fixture BE sebelum spec dan di hook `after`.
- Jendela asersi absence dialog: lima detik tanpa memuat ulang halaman, pilihan spec ini (bagian 6).
- Suite berjalan serial (`parallel: false`) karena status subscription adalah state global.
- Hook suite (flag Guided Tooltip, seed dan pemulihan lewat API, pemulihan status subscription) mengikuti `suite.md`.
- Env var: `FA_TC_PASSWORD` (akun default suite di hook `before` dan `after`), didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.

## Test Steps

### Untuk setiap iterasi pada tabel Prerequisites (langkah 1 sampai 15)

1. Ganti akun: logout, lalu login sebagai Total Control client iterasi dengan sesi-produk Fixed Asset terbuka (Pre-setup #16), lalu buka Fixed Asset > Reports & Logs > Activity Log dan klik tab User Action
2. Ubah status subscription Fixed Asset client iterasi sesuai tabel Prerequisites lewat seed BE
3. Tunggu 5 detik tanpa memuat ulang halaman
4. Verifikasi halaman Activity Log client iterasi masih tampil
5. Verifikasi sesi-produk Fixed Asset berakhir senyap tanpa dialog
6. Muat ulang halaman
7. Verifikasi permintaan dari halaman Activity Log ditolak server
8. Verifikasi pengguna diarahkan ke Portal — Product Hub
9. Verifikasi tidak ada dialog yang tampil
10. Buka produk Fixed Asset kembali dari Portal
11. Verifikasi popup Title `Subscription Not Active` dan Body `Your subscription is not active. Please contact your administrator.` tampil
12. Verifikasi tombol `[OK]` tampil pada popup
13. Klik `[OK]`
14. Verifikasi popup tertutup
15. Verifikasi pengguna diarahkan ke Portal — Product Hub

## Notes

- Mode: FE+BE, kelas h (state tenant): spec mengubah status subscription lewat seed BE dan mengasersi akses mengikuti Auth, bukan perilaku Activity Log.
- Langkah yang diulang (S-10, bagian 8b butir 7): langkah 1 sampai 15 diulang untuk tiga iterasi sehingga ekspansi 45 langkah; parameter tiap iterasi ada di tabel Prerequisites. Alasan melewati sekitar 35 langkah: seluruh iterasi satu blok TC (TC-FA-FAAL-289) dengan satu kelas harness dan langkah identik per client; tidak ada langkah bersyarat dan Expected TC memang menyebut ketiga status dengan teks identik.
- Expected butir a, b, dan c TC sumber dipetakan ke `Verifikasi` per klausa: sesi berakhir senyap tanpa dialog (langkah 4 dan 5), permintaan ditolak server (langkah 7), diarahkan ke Portal (langkah 8), tanpa dialog (langkah 9), popup (langkah 11 dan 12), `[OK]` menutup popup (langkah 14) dan mengarahkan ke Portal (langkah 15).
- Langkah 4 menjadi anchor positif untuk asersi absence dialog pada langkah 5; langkah 8 menjadi anchor untuk langkah 9 (bagian 8b butir 2).
- Langkah penghubung (S-03, S-07, S-09): langkah 3 (jendela lima detik), langkah 6 (muat ulang halaman), langkah 13 (menutup popup yang sekaligus bagian Expected).
- Temuan untuk QA:
  - TC-FA-FAAL-289 menyebut tiga client Active dengan sesi-produk terbuka dan "Langkah 1 dan 4" mengubah status, tetapi tidak menyebut akun Total Control per client; akun disediakan tim FE.
  - TC-FA-FAAL-289 mengasumsikan ketiga client dapat dikembalikan ke Active untuk run berikutnya; status Purge dan Deleted bersifat satu arah sehingga tim FE/BE perlu fixture yang menyediakan client baru setiap run.
  - TC-FA-FAAL-289 butir a, b, dan c berisi teks identik untuk ketiga status; spec menuliskan satu rangkaian `Verifikasi` yang diulang per iterasi.
  - TC-FA-FAAL-289 menyebut "permintaan dari halaman Activity Log ditolak server" tanpa kode status; spec tidak mengasersi kode status.
