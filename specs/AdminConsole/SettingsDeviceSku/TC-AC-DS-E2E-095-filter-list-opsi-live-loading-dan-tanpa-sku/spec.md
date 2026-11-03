---
id: TC-AC-DS-E2E-095-filter-list-opsi-live-loading-dan-tanpa-sku
title: "Filter List: Opsi Ter-update setelah Register, State Loading Dropdown, dan No options available"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-591
  - TC-AC-DS-592
  - TC-AC-DS-593
coverage:
  web: automated
---

# Filter List: Opsi Ter-update setelah Register, State Loading Dropdown, dan No options available

## Prerequisites

- Mode: FE+BE. Respons pemuatan opsi Filter ditunda lewat `Spectra.intercept()` di atas backend nyata (kemampuan teknis; endpoint opsi Filter tidak disebut TC, PRD, atau LLD sehingga disediakan tim FE, lihat Temuan untuk QA).
- Akun aktor pertama: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor kedua (langkah 22): Total Control Principal Tanpa SKU, `totalControlFresh_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_FRESH_PASSWORD` (Pre-setup #21; belum ada SKU dan belum ada entri Changelog). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal PT Arunika Prima).
- Data Pre-setup (hanya dibaca, tidak diubah): #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal), dipasang idempoten oleh seeding di hook `before`. Pohon Category (#25), Device Name (#26), dan Brand (#27), serta data khusus (#40): Device Name `Perangkat Sementara` (Category `Asset TAG`) dan Brand `Brand Sementara` tersedia di master dan belum dipakai SKU mana pun. File foto `foto-a.jpg` (#37).
- Data Dinamis milik spec (S-12), dibuat di langkah 15 dan dihapus di hook `after` lewat API: SKU `FLT-LIVE-01-{runId}-095` (Category `Asset TAG`, Device Name `Perangkat Sementara`, Brand `Brand Sementara`, Model/Type `T-LV1`, foto `foto-a.jpg`). Pemulihan jumlah SKU (129) dan Changelog (35 entri) dilakukan baseline data uji yang disediakan tim FE/BE.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE.

## Test Steps

### TC-AC-DS-592: State loading dropdown Filter

1. Tunda respons pemuatan opsi Filter dengan intercept
2. Klik ikon Filter
3. Klik field Brand selama respons tertunda
4. Verifikasi dropdown Brand menampilkan indikator loading opsi
5. Verifikasi dropdown Brand tidak menampilkan "No options available" maupun "No results found"
6. Lepaskan respons yang ditunda
7. Verifikasi opsi Brand `Arcturus`, `International Scanner Solutions`, `Kinetia`, dan `Veltrix` tampil

### TC-AC-DS-591: Opsi dropdown Filter ter-update setelah Register

8. Tekan Esc, lalu klik field Brand
9. Verifikasi opsi Brand memuat `Arcturus`
10. Verifikasi opsi Brand tidak memuat `Brand Sementara`
11. Tekan Esc, lalu klik field Device Name
12. Verifikasi opsi Device Name memuat `Asset TAG`
13. Verifikasi opsi Device Name tidak memuat `Perangkat Sementara`
14. Tekan Esc, lalu tutup Filter Panel dengan mengklik ikon Filter
15. Klik `[+ SKU]`, isi Category `Asset TAG`, Device Name `Perangkat Sementara`, SKU `FLT-LIVE-01-{runId}-095`, Brand `Brand Sementara`, Model/Type `T-LV1`, unggah foto `foto-a.jpg`, lalu klik `[Submit]`
16. Verifikasi muncul toast sukses: "Success, device SKU has been registered."
17. Klik ikon Filter, lalu klik field Brand tanpa memuat ulang halaman
18. Verifikasi opsi Brand memuat `Brand Sementara`
19. Tekan Esc, lalu klik field Device Name
20. Verifikasi opsi Device Name memuat `Perangkat Sementara`
21. Tekan Esc

### TC-AC-DS-593: Principal Tanpa SKU

22. Ganti akun: Logout dari Total Control Principal PT Arunika Prima, lalu login sebagai Total Control Principal Tanpa SKU (`totalControlFresh_automated_{namaCompany}@qwertysystem.net`)
23. Buka halaman `Settings > Device > Device SKU`
24. Klik ikon Filter, lalu klik field Brand
25. Verifikasi dropdown Brand menampilkan teks "No options available" (teks saja, bukan error)
26. Tekan Esc, lalu klik field Device Name
27. Verifikasi dropdown Device Name menampilkan teks "No options available"

## Notes

- Langkah penghubung (S-03, S-09): Esc di langkah 8, 11, 14, 19, 21, dan 26 menutup dropdown atau panel sebelum langkah berikutnya; langkah 22 sampai 23 adalah ganti akun eksplisit (S-07) dan membuka halaman karena hook `beforeEach` hanya membuka halaman untuk akun pertama.
- Urutan blok: TC-AC-DS-592 (tanpa aksi tulis) dahulu, TC-AC-DS-591 (aksi tulis), lalu TC-AC-DS-593 (ganti akun); sumber memuatnya berurutan 591, 592, 593. Perubahan urutan agar asersi loading tidak bergantung pada hasil Register.
- Asersi tambahan (S-03): langkah 9 dan 12 membuktikan opsi pembanding tampil sebagai anchor positif absence di langkah 10 dan 13; bukan Expected TC. Absence di langkah 5 didahului pemicu dan indikator loading di langkah 4 (8b butir 11).
- Temuan untuk QA:
  - S-12: asersi bergantung pada nama literal Pre-setup #29 dan #30 serta data khusus #40 (`Perangkat Sementara`, `Brand Sementara`). Lampiran A tidak memuat butir modul ini. Spec mengikuti TC dengan seeding idempoten dan suite serial; keputusan pengecualian nama literal masih terbuka.
  - Fixture rancangan belum diverifikasi ada di environment: akun Principal Tanpa SKU (#21) dan data khusus #40.
  - TC-AC-DS-591 tidak menyebut Device Name dan Brand selain `Perangkat Sementara` dan `Brand Sementara`; kode SKU diberi suffix `{runId}-095` (S-12) dan aturan format kode SKU tidak diketahui spec.
  - Mekanisme menunda respons opsi Filter bergantung pada endpoint yang tidak tercantum di sumber; disediakan tim FE (S-13).
  - Env `AC_DS_TC_PASSWORD` dan `AC_DS_FRESH_PASSWORD` serta berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
