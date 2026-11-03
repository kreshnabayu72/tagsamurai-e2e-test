---
id: TC-AC-DS-E2E-090-filter-list-screening-opsi-pencarian-dropdown-dan-tutup-tanpa-apply
title: "Filter List: Screening Panel, Isi Opsi Dropdown, Pencarian di Dalam Dropdown, dan Tutup Tanpa Apply"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-311
  - TC-AC-DS-312
  - TC-AC-DS-313
  - TC-AC-DS-322
coverage:
  web: automated
---

# Filter List: Screening Panel, Isi Opsi Dropdown, Pencarian di Dalam Dropdown, dan Tutup Tanpa Apply

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal): hanya dibaca, tidak diubah. Dipasang idempoten oleh seeding di hook `before`. Opsi dropdown yang diasersi (Device Name, Brand, Hardware Type, Range Type, TAG Type) diturunkan dari data itu; Brand `Zephyr` ada di master Brand (#27) tetapi belum dipakai SKU mana pun.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE (lihat Temuan untuk QA).
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat; filter yang diterapkan dilepas oleh langkah pemulihan di akhir spec.

## Test Steps

### TC-AC-DS-311: Screening Filter Panel

1. Hover ikon Filter
2. Klik ikon Filter
3. Verifikasi ikon Filter berubah gelap
4. Verifikasi Filter Panel tampil di bawah toolbar
5. Verifikasi field berurutan (maksimum 4 per baris): Device Name "All device names", Brand "All brands", Current Stock "Min" dan "Max", Last Modified "Select date", Hardware Type "All hardware types", Range Type "All range types", dan TAG Type "All TAG types"
6. Verifikasi Category tidak ada di Filter Panel
7. Verifikasi tombol `[Clear Field]` di kiri dan `[Apply]` di kanan

### TC-AC-DS-312: Isi opsi dropdown Filter berasal dari data tabel

8. Klik field Device Name
9. Verifikasi Device Name memuat `4-Port Fixed Reader`, `anggur sensor`, `Apel sensor`, `Asset TAG`, `BLE Gateway`, `Industrial Handheld Reader`, `Seed Tag`, `Tunnel Scanner`, `UHF Handheld Reader`, dan `Wearable TAG`
10. Tekan Esc, lalu klik field Brand
11. Verifikasi Brand memuat `Arcturus`, `International Scanner Solutions`, `Kinetia`, dan `Veltrix`
12. Verifikasi `Zephyr` tidak ada di opsi Brand karena belum dipakai SKU mana pun
13. Tekan Esc, lalu klik field Hardware Type
14. Verifikasi Hardware Type memuat `Handheld Reader`, `Smart Fixed Reader`, dan `BLE Gateway`
15. Verifikasi tidak ada opsi untuk nilai kosong di Hardware Type
16. Tekan Esc, lalu klik field Range Type
17. Verifikasi Range Type memuat `Long Range` dan `Short Range`
18. Tekan Esc, lalu klik field TAG Type
19. Verifikasi TAG Type memuat `Object` dan `User`
20. Tekan Esc

### TC-AC-DS-313: Pencarian internal dropdown Filter

21. Klik field Brand
22. Ketik `kin` pada kotak pencarian di dalam dropdown
23. Verifikasi hanya opsi `Kinetia` tampil (substring, tidak membedakan huruf besar-kecil)
24. Ganti isi kotak pencarian di dalam dropdown dengan `zzz`
25. Verifikasi dropdown menampilkan teks "No results found" (teks saja, tanpa ilustrasi) dan tidak ada opsi yang cocok
26. Tekan Esc

### TC-AC-DS-322: Menutup Filter Panel tanpa Apply

27. Pada field Brand pilih `Veltrix`
28. Klik `[Apply]`
29. Pada field Hardware Type pilih `BLE Gateway`
30. Klik ikon Filter sehingga panel tertutup tanpa Apply
31. Klik ikon Filter sehingga panel dibuka kembali
32. Verifikasi panel menampilkan Brand `Veltrix` (nilai ter-Apply terakhir)
33. Verifikasi Hardware Type `BLE Gateway` yang belum di-Apply tidak ada di panel
34. Verifikasi tabel tetap menampilkan hasil filter Brand `Veltrix`: `SFR-VEL-4P` dan `SFR-ZERO-01`
35. Klik `[Clear Field]`, lalu `[Apply]`

## Notes

- Langkah penghubung (S-03, S-09): Esc di langkah 10, 13, 16, 18, 20, dan 26 menutup dropdown sebelum membuka field berikutnya; langkah 35 melepas filter agar state tidak terbawa.
- Ukuran: 35 langkah; semua blok memakai Filter Panel List yang sama, tanpa aksi tulis.
- Temuan untuk QA:
  - S-12: asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. opsi Device Name dan Brand turunan data itu, `SFR-VEL-4P`). Lampiran A tidak memuat butir modul ini. Spec mengikuti TC dengan seeding idempoten dan suite serial; keputusan pengecualian nama literal masih terbuka.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - TC-AC-DS-311 langkah 2 (hover ikon Filter) tidak punya Expected; tidak diasersi.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya bila menutupi layar belum ditetapkan.
