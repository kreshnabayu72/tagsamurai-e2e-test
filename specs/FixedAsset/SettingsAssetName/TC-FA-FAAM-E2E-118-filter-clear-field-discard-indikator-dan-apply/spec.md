---
id: TC-FA-FAAM-E2E-118-filter-clear-field-discard-indikator-dan-apply
title: "Filter: Clear Field, Menutup Tanpa Apply, Indikator Titik, Baris Kosong, dan Reset Halaman"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-375
  - TC-FA-FAAM-376
  - TC-FA-FAAM-377
  - TC-FA-FAAM-378
  - TC-FA-FAAM-379
coverage:
  web: automated
---

# Filter: Clear Field, Menutup Tanpa Apply, Indikator Titik, Baris Kosong, dan Reset Halaman

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`). Baris yang dirujuk: `Dell Latitude` (Pre-setup #10, Default Addon `Audit`), `Ergonomic Chair` (Pre-setup #11), `Warehouse Pallet` (Pre-setup #13, Default Addon `—`).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-375: Clear Field mengosongkan kriteria filter panel tanpa mereset Search dan Sort
1. Ketik Search `Dell`, tekan Enter
2. Klik header kolom Code
3. Klik icon Filter, pilih UoM `Unit`, lalu klik `[Apply]`
4. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
5. Klik icon Filter
6. Verifikasi field UoM kembali `All units` (kriteria filter kosong)
7. Verifikasi kotak Search tetap berisi `Dell`
8. Verifikasi header kolom Code tetap menampilkan sort Ascending
9. Klik icon Filter untuk menutup Filter Panel
10. Klik `(←)` pada kotak Search
11. Klik header kolom Code dua kali sampai kembali netral
### TC-FA-FAAM-376: Menutup panel tanpa Apply membuang perubahan yang belum di-Apply
12. Klik icon Filter
13. Pilih UoM `Unit` tanpa Apply
14. Klik icon Filter lagi
15. Klik icon Filter untuk membuka panel lagi
16. Verifikasi panel menampilkan nilai ter-Apply terakhir: field UoM `All units`, bukan draft
17. Verifikasi tabel tidak tersaring: baris `Dell Latitude` dan `Ergonomic Chair` tampil
18. Klik icon Filter untuk menutup Filter Panel
### TC-FA-FAAM-377: Indikator titik pada icon Filter selama ada filter ter-Apply
19. Klik icon Filter
20. Pilih UoM `Unit`, lalu klik `[Apply]`
21. Verifikasi badge titik tampil pada icon Filter saat panel tertutup
22. Klik icon Filter untuk membuka panel
23. Verifikasi badge titik tampil pada icon Filter saat panel terbuka
24. Klik icon Filter untuk menutup panel
25. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
26. Verifikasi badge titik pada icon Filter hilang
### TC-FA-FAAM-378: Baris bernilai kosong hanya tampil saat filter kolom itu tidak dipakai
27. Klik icon Filter
28. Pilih Default Addon `Audit`, lalu klik `[Apply]`
29. Verifikasi baris `Dell Latitude` (Default Addon `Audit`) tampil di tabel
30. Verifikasi baris `Warehouse Pallet` (Default Addon `—`) tidak tampil
31. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
### TC-FA-FAAM-379: Apply filter mereset halaman ke halaman 1
32. Pindah ke halaman 2
33. Klik icon Filter, pilih UoM `Unit`, lalu klik `[Apply]`
34. Verifikasi tabel kembali ke halaman 1
35. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): menutup panel, klik `(←)` pada Search dan klik header Code dua kali sampai netral di akhir blok TC-FA-FAAM-375, serta `[Clear Field]` lalu `[Apply]` di akhir blok (S-09).
- Langkah "Klik icon Filter lagi" pada TC-FA-FAAM-376 menutup panel dan langkah berikutnya membukanya lagi, sesuai TC; Verifikasi hanya pada panel yang dibuka ulang.
- Asersi absence pada TC-FA-FAAM-378 beranchor Verifikasi baris `Dell Latitude` tampil pada filter yang sama (bagian 8b butir 2).
- Asersi "kembali ke halaman 1" pada TC-FA-FAAM-379 didahului langkah pindah ke halaman 2 (S-14).
