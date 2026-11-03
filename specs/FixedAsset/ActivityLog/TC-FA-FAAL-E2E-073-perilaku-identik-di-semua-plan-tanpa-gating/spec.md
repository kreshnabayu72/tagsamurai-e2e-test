---
id: TC-FA-FAAL-E2E-073-perilaku-identik-di-semua-plan-tanpa-gating
title: "State Tenant: Perilaku Activity Log Identik di Plan Starter, Growth, Professional, dan Enterprise"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-276
coverage:
  web: automated
---

# State Tenant: Perilaku Activity Log Identik di Plan Starter, Growth, Professional, dan Enterprise

## Prerequisites

- Mode: FE+BE (backend nyata; empat client dengan plan berbeda, tanpa intercept).
- Akun aktor: Total Control tiap client pada tabel di bawah (Pre-setup #17), satu akun Total Control per client. Email dan password akun tiap client tidak tertulis di Pre-setup TC dan disediakan tim FE (lihat Temuan untuk QA). Login akun pertama (client Starter) dilakukan lewat langkah ganti akun eksplisit pada iterasi pertama karena hook `before` login ke akun default suite; hook `after` mengembalikan sesi ke akun default suite.
- Client yang diuji (tabel parameter langkah 1 sampai 9, satu iterasi per baris):

  | Iterasi | Client | Plan |
  |---|---|---|
  | 1 | Client Starter (rujukan perbandingan) | Starter |
  | 2 | Client Growth | Growth |
  | 3 | Client Professional | Professional |
  | 4 | Client Enterprise | Enterprise |

- Data Pre-setup: empat client dengan plan Starter, Growth, Professional, dan Enterprise, masing-masing dengan Total Control (#17). Data Uji dari TC sumber: Format CSV; Search dan Filter dengan nilai yang cocok dengan sedikitnya satu baris client itu, ditetapkan tim FE sesuai seed #17 (lihat Temuan untuk QA). Identitas data dirujuk lewat `fixtures/activity-log.json` (belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Kemampuan teknis (disediakan tim FE/BE): seed log pada tiap client plan agar Search, Filter, dan Download memiliki data; penangkap unduhan browser.
- Spec ini tidak mengubah plan atau state global client; plan tiap client adalah state tetap Pre-setup #17 yang tidak diubah.
- Suite berjalan serial (`parallel: false`).
- Hook suite (flag Guided Tooltip, seed dan pemulihan lewat API, pemulihan plan) mengikuti `suite.md`.
- Env var: `FA_TC_PASSWORD` (akun default suite di hook `before` dan `after`), didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.

## Test Steps

### Untuk setiap iterasi pada tabel Prerequisites (langkah 1 sampai 9)

1. Ganti akun: logout, lalu login sebagai Total Control client iterasi (Pre-setup #17)
2. Buka Fixed Asset > Reports & Logs > Activity Log, lalu klik tab User Action
3. Verifikasi Tab Session dan Tab User Action keduanya tampil
4. Verifikasi kolom kedua tab sama dengan client Starter (iterasi 1 menjadi rujukan perbandingan)
5. Ketik Search dengan nilai yang cocok dengan sedikitnya satu baris client, tekan Enter
6. Terapkan Filter dengan nilai yang cocok dengan sedikitnya satu baris client
7. Klik icon Download, pilih `Download as CSV`
8. Verifikasi Search, Filter, dan Download berjalan sama dengan client Starter: hasil tersaring tampil dan berkas CSV terunduh
9. Verifikasi tidak ada pembatasan, ikon upsell, maupun batas jumlah baris khusus plan

## Notes

- Mode: FE+BE, kelas h (state tenant): spec membandingkan perilaku di empat plan. Plan tidak diubah.
- Langkah yang diulang (S-10, bagian 8b butir 7): langkah 1 sampai 9 diulang untuk empat client sehingga ekspansi 36 langkah; parameter tiap iterasi ada di tabel Prerequisites. Alasan melewati sekitar 35 langkah: seluruh iterasi satu blok TC (TC-FA-FAAL-276) dengan satu kelas harness dan langkah identik per client; tidak ada langkah bersyarat.
- Perbandingan (langkah 4 dan 8): iterasi 1 (Starter) menjadi rujukan; iterasi 2 sampai 4 membandingkan terhadap hasil Starter. `Verifikasi` di iterasi 1 mencatat kolom, hasil Search dan Filter, serta berkas sebagai rujukan.
- Urutan asersi pada langkah 7 sampai 9: absence ikon upsell dan pembatasan didahului langkah 3 dan 8 sebagai anchor positif bahwa halaman dan hasil tampil (bagian 8b butir 2).
- Langkah penghubung (S-03): langkah 2 (membuka layar di client yang dilogin).
- Temuan untuk QA:
  - TC-FA-FAAL-276 tidak menyebut nilai Search dan Filter, akun Total Control tiap client, atau data log tiap client; nilai dan akun ditetapkan tim FE sesuai seed Pre-setup #17.
  - TC-FA-FAAL-276 langkah 3 ("Bandingkan tampilan dan perilaku") tidak mendefinisikan cara membandingkan; spec memakai client Starter sebagai rujukan.
  - TC-FA-FAAL-276 butir b memuat tiga klausa (pembatasan, ikon upsell, batas jumlah baris) yang digabung dalam satu `Verifikasi` (langkah 9) sebagai daftar elemen yang sama-sama tidak ada.
