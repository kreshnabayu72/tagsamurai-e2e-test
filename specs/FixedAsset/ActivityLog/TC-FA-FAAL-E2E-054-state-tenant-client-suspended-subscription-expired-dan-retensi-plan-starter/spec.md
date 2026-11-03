---
id: TC-FA-FAAL-E2E-054-state-tenant-client-suspended-subscription-expired-dan-retensi-plan-starter
title: "State Tenant: Client Suspended, Subscription Expired, dan Retensi Baris pada Plan Starter"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAL-273
  - TC-FA-FAAL-274
  - TC-FA-FAAL-275
coverage:
  web: automated
---

# State Tenant: Client Suspended, Subscription Expired, dan Retensi Baris pada Plan Starter

## Prerequisites

- Mode: FE+BE (backend nyata; status client dan subscription diubah lewat fixture BE, tanpa intercept).
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Tab Session terbuka, sesi Fixed Asset sudah terbuka). Langkah 26 memakai akun Total Control di client plan Starter (ganti akun eksplisit); akun itu tidak tertulis di Pre-setup TC dan disediakan tim FE (lihat Temuan untuk QA). Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: Data Log Tab User Action UA-01 sampai UA-15 (#12) dan Tab Session (#11) pada client akun default; client akun default itu juga yang status client-nya menjadi Suspended dan subscription Fixed Asset-nya Expired (status diubah fixture BE saat spec berjalan, sesi Fixed Asset sudah dibuka sebelum perubahan); baris Tab User Action dan Tab Session berusia 2 tahun di client plan Starter (#14). Identitas data dirujuk lewat `fixtures/activity-log.json` (belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Uji dari TC sumber: Format CSV; Search `Gedung`; Filter Date rentang dua tahun lalu (nilai tanggal rentang yang memuat baris berusia 2 tahun ditetapkan seed Pre-setup #14).
- Total entri (Z): dibaca dari teks `Showing X–Y of Z entries` sebelum status diubah. Asersi "seluruh baris" memakai Z yang sama sesudah status berubah, bukan angka absolut, karena log bersifat permanen dan spec lain menambah baris (S-12, bagian 8b butir 10).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): mengubah status client menjadi Suspended dan subscription Fixed Asset menjadi Expired lewat fixture BE sementara sesi Fixed Asset tetap terbuka; memulihkan keduanya ke Active; penangkap unduhan browser.
- State global yang diubah dan pemulihannya: status client (Suspended) dan status subscription Fixed Asset (Expired). Langkah 14 dan 25 memulihkan keduanya ke Active; hook `after` memulihkan sebagai cadangan.
- Suite berjalan serial (`parallel: false`) karena status client dan subscription adalah state global.
- Hook suite (flag Guided Tooltip, seed dan pemulihan lewat API, pemulihan plan, status client, dan subscription) mengikuti `suite.md`.
- Env var: `FA_TC_PASSWORD`, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.

## Test Steps

### TC-FA-FAAL-273: Client Suspended, Activity Log tetap dapat dibaca

1. Klik tab User Action
2. Catat Z dari teks `Showing X–Y of Z entries`
3. Klik tab Session
4. Catat Z dari teks `Showing X–Y of Z entries`
5. Ubah status client menjadi Suspended lewat fixture BE (sesi Fixed Asset tetap terbuka)
6. Buka Fixed Asset > Reports & Logs > Activity Log, lalu klik tab User Action
7. Verifikasi Tab User Action menampilkan seluruh baris: sedikitnya satu baris tampil dan Z sama dengan nilai yang dicatat pada langkah 2
8. Klik tab Session
9. Verifikasi Tab Session menampilkan seluruh baris: sedikitnya satu baris tampil dan Z sama dengan nilai yang dicatat pada langkah 4
10. Klik tab User Action
11. Klik icon Download, pilih `Download as CSV`
12. Verifikasi tidak ada toast
13. Verifikasi berkas CSV terunduh
14. Pulihkan status client menjadi Active lewat fixture BE

### TC-FA-FAAL-274: Subscription Expired dengan sesi lama

15. Ubah status subscription Fixed Asset menjadi Expired lewat fixture BE (sesi Fixed Asset lama tetap terbuka)
16. Buka Fixed Asset > Reports & Logs > Activity Log, lalu klik tab User Action
17. Verifikasi Tab User Action menampilkan seluruh baris: sedikitnya satu baris tampil dan Z sama dengan nilai yang dicatat pada langkah 2
18. Klik tab Session
19. Verifikasi Tab Session menampilkan seluruh baris: sedikitnya satu baris tampil dan Z sama dengan nilai yang dicatat pada langkah 4
20. Klik tab User Action, lalu ketik Search `Gedung`, tekan Enter
21. Verifikasi Search berjalan normal: baris hasil dengan `Gedung` tampil di tabel
22. Klik icon Download, pilih `Download as CSV`
23. Verifikasi tidak ada toast error
24. Verifikasi berkas CSV terunduh
25. Pulihkan status subscription Fixed Asset menjadi Active lewat fixture BE, lalu klik `(←)` pada kotak Search

### TC-FA-FAAL-275: Baris berusia sangat lama tetap tampil tanpa rolling window per plan

26. Ganti akun: logout, lalu login sebagai Total Control client plan Starter (Pre-setup #14)
27. Buka Fixed Asset > Reports & Logs > Activity Log, lalu klik tab User Action
28. Terapkan Filter Date dengan rentang dua tahun lalu
29. Verifikasi baris berusia 2 tahun tampil di Tab User Action
30. Klik tab Session
31. Terapkan Filter Date dengan rentang dua tahun lalu
32. Verifikasi baris berusia 2 tahun tampil di Tab Session

## Notes

- Mode: FE+BE, kelas h (state tenant): spec mengubah status client dan subscription lewat fixture BE dan mengasersi akses baca. Perubahan plan dan akses Auth ada di spec 073 dan 074.
- Langkah 5 dan 15 mengubah state sementara sesi Fixed Asset tetap terbuka; pemicu itu bukan objek uji dan tidak diasersi (bagian 3 prinsip 13h, P-2 untuk pemicu state).
- Langkah 6 dan 16 membuka layar lagi lewat menu karena TC mensyaratkan membuka Activity Log sesudah status berubah; hook `beforeEach` suite sudah membukanya sebelum status berubah.
- Langkah penghubung (S-03, S-09): langkah 1 sampai 4 (mencatat baseline Z sebelum status diubah), langkah 14 dan 25 (memulihkan status), langkah 26 dan 27 (ganti akun eksplisit dan membuka layar di client Starter, S-07), langkah 3, 8, 10, 18 dan 30 (pindah tab).
- Urutan asersi pada langkah 12 dan 13, 23 dan 24: absence toast segera setelah pemicu dan sebelum asersi berkas (bagian 8b butir 11).
- Temuan untuk QA:
  - TC-FA-FAAL-273 dan 274 mengasersi "seluruh baris" tanpa angka; spec mengartikannya sebagai Z yang sama dengan sebelum status berubah dan sedikitnya satu baris tampil.
  - TC-FA-FAAL-273 dan 274 tidak menyebut client mana yang diubah statusnya; spec memakai client akun default (Total Control Pre-setup #1) dan memulihkannya ke Active, sehingga suite berjalan serial.
  - TC-FA-FAAL-274 langkah 3 ("Search dan Download pada salah satu tab") tidak menyebut tab; spec memakai Tab User Action dan kata kunci `Gedung` (nama group seed UA-02, UA-13, UA-14, UA-15).
  - TC-FA-FAAL-275 tidak menyebut tanggal untuk "rentang 2 tahun lalu" dan akun Total Control client Starter; tanggal ditetapkan seed Pre-setup #14 dan akun disediakan tim FE. Expected "tidak terhapus oleh batas retensi plan" adalah kesimpulan dari baris tampil, sehingga tidak punya `Verifikasi` terpisah (S-03).
