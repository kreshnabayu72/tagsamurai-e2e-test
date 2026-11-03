---
id: TC-AC-DS-E2E-097-kombinasi-search-filter-sort-pagination-list-bagian-2
title: "Kombinasi List: Melepas Search, Ganti Sort, serta Tanpa Hasil Lalu Pulih"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-330
  - TC-AC-DS-331
  - TC-AC-DS-332
coverage:
  web: automated
---

# Kombinasi List: Melepas Search, Ganti Sort, serta Tanpa Hasil Lalu Pulih

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #29 (SKU Principal inti; `TAG-ARC-USR` Device Name `Wearable TAG`, `TAG-ARC-OBJ`, `SFR-VEL-4P`, `SFR-ZERO-01`) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal): hanya dibaca, tidak diubah. Dipasang idempoten oleh seeding di hook `before`.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE (lihat Temuan untuk QA).
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat; Search, Filter, dan Sort dipulihkan oleh langkah pemulihan di akhir tiap bagian.

## Test Steps

### TC-AC-DS-330: Mengosongkan Search saat Filter dan Sort aktif

1. Klik ikon Filter
2. Pada field Brand pilih `Arcturus`
3. Klik `[Apply]`
4. Klik header kolom SKU dua kali sampai Descending aktif
5. Ketik Search `Wearable`, tekan Enter
6. Klik `✕` pada Search, tekan Enter pada input kosong
7. Verifikasi Search dilepas: kotak pencarian kosong dan baris `TAG-ARC-OBJ` (tidak cocok `Wearable`) tampil
8. Verifikasi Filter Brand `Arcturus` tetap aktif: Filter Panel menampilkan Brand `Arcturus`
9. Verifikasi Sort SKU Descending tetap aktif
10. Klik `[Clear Field]`, lalu `[Apply]`, lalu klik header kolom SKU sekali sampai netral

### TC-AC-DS-331: Mengganti kolom Sort tidak mereset Search maupun Filter

11. Ketik Search `Arcturus`, tekan Enter
12. Pada field TAG Type pilih `Object`
13. Klik `[Apply]`
14. Klik header kolom Brand sekali, lalu klik header kolom Model/Type sekali
15. Verifikasi Sort aktif berpindah ke Model/Type Ascending
16. Verifikasi Brand kembali netral
17. Verifikasi Search `Arcturus` tetap aktif
18. Verifikasi Filter TAG Type `Object` tetap aktif
19. Klik `[Clear Field]`, lalu `[Apply]`, klik header kolom Model/Type dua kali sampai netral, lalu klik `(←)` pada kotak Search

### TC-AC-DS-332: Search dan Filter tanpa hasil lalu melepas salah satunya

20. Ketik Search `BLE`, tekan Enter
21. Pada field Brand pilih `Veltrix`
22. Klik `[Apply]`
23. Verifikasi kombinasi `BLE` dan Brand `Veltrix` menampilkan "No results found" dan "Try adjusting your search or filter."
24. Klik `✕` pada Search, tekan Enter pada input kosong
25. Verifikasi tabel pulih menampilkan `SFR-VEL-4P` dan `SFR-ZERO-01`
26. Klik `[Clear Field]`, lalu `[Apply]`, lalu klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03, S-09): langkah 10, 19, dan 26 memulihkan Search, Filter, dan Sort sebelum bagian berikutnya; tanpa asersi.
- Langkah 8 dan 18 mengamati Filter lewat nilai ter-Apply pada Filter Panel; TC tidak menyebut cara pengamatannya.
- Sumber TC-AC-DS-335 (opsi Filter hilang dari data, dua sesi) ada di spec TC-AC-DS-E2E-190.
- Temuan untuk QA:
  - S-12: asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `TAG-ARC-OBJ`, `SFR-VEL-4P`). Lampiran A tidak memuat butir modul ini. Spec mengikuti TC dengan seeding idempoten dan suite serial; keputusan pengecualian nama literal masih terbuka.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - Expected TC-AC-DS-330 tidak menyebut baris yang tampil sesudah Search dilepas; spec memakai `TAG-ARC-OBJ` (Brand `Arcturus`, bukan hasil `Wearable`) sebagai anchor.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya bila menutupi layar belum ditetapkan.
