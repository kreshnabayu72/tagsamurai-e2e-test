---
id: TC-FA-FAAM-E2E-120-kombinasi-search-filter-sort-dan-pagination
title: "Kombinasi Search, Filter, Sort, dan Pagination (Irisan, Clear, Pindah Sort)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-380
  - TC-FA-FAAM-381
  - TC-FA-FAAM-382
  - TC-FA-FAAM-383
  - TC-FA-FAAM-384
coverage:
  web: automated
---

# Kombinasi Search, Filter, Sort, dan Pagination (Irisan, Clear, Pindah Sort)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`). Baris yang dirujuk: `Seed Item 01` sampai `Seed Item 30` (Pre-setup #15, UoM `Unit`).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-380: Alur Search lalu Filter menghasilkan irisan
1. Ketik Search `Seed`, tekan Enter
2. Klik icon Filter, pilih UoM `Unit`, lalu klik `[Apply]`
3. Verifikasi baris `Seed Item 01` tampil di tabel
4. Verifikasi hasil adalah irisan Search `Seed` dan Filter UoM `Unit`: seluruh baris yang tampil memuat `Seed` dan ber-UoM `Unit`
5. Verifikasi keyword Search `Seed` tidak direset oleh Apply
### TC-FA-FAAM-381: Alur Filter lalu Search menghasilkan irisan identik
6. Klik `(←)` pada kotak Search
7. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
8. Klik icon Filter, pilih UoM `Unit`, lalu klik `[Apply]`
9. Ketik Search `Seed`, tekan Enter
10. Verifikasi baris `Seed Item 01` tampil di tabel
11. Verifikasi hasil identik dengan alur Search lalu Filter: seluruh baris yang tampil memuat `Seed` dan ber-UoM `Unit`
### TC-FA-FAAM-382: Kombinasi Search, Multi-Filter, Sort, dan Pagination bekerja harmonis
12. Klik icon Filter, klik `[Clear Field]`, isi Total Asset `Min` 0, pilih UoM `Unit`, lalu klik `[Apply]`
13. Klik header kolom Code dua kali (Descending)
14. Ubah page size ke 25
15. Verifikasi Search `Seed` aktif: kotak Search berisi `Seed`
16. Verifikasi Filter UoM `Unit` dan Total Asset Min 0 aktif: badge titik tampil pada icon Filter
17. Verifikasi sort Code Descending aktif pada header kolom Code
18. Verifikasi page size 25 aktif
### TC-FA-FAAM-383: Clear Search saat Filter dan Sort aktif mempertahankan keduanya
19. Klik icon Filter, klik `[Clear Field]`, pilih UoM `Unit`, lalu klik `[Apply]`
20. Klik header kolom Code dua kali sampai sort Ascending
21. Klik `(✕)` pada Search, tekan Enter pada input kosong
22. Verifikasi kotak Search kosong
23. Verifikasi Filter UoM `Unit` tetap aktif: badge titik tampil pada icon Filter
24. Verifikasi sort Code Ascending tetap aktif pada header kolom Code
### TC-FA-FAAM-384: Berpindah kolom sort tidak mereset Search dan Filter
25. Ketik Search `Seed`, tekan Enter
26. Klik header kolom Total Asset (Ascending)
27. Verifikasi sort pindah ke kolom Total Asset: header kolom Total Asset menampilkan sort Ascending
28. Verifikasi header kolom Code netral
29. Verifikasi kotak Search tetap berisi `Seed`
30. Verifikasi Filter UoM `Unit` tetap aktif: badge titik tampil pada icon Filter
31. Klik `(←)` pada kotak Search
32. Klik header kolom Total Asset dua kali sampai kembali netral
33. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): membersihkan Search, Filter, dan Sort di antara blok (S-09) dan di akhir spec; mengatur page size kembali ke 10 tidak diperlukan karena page size 25 hanya mengubah tampilan dan dipulihkan dengan memuat ulang halaman oleh hook `beforeEach` suite pada spec berikutnya.
- Pada TC-FA-FAAM-383 sort Code Ascending dicapai dari Descending TC-FA-FAAM-382 dengan klik header dua kali (Descending, netral, lalu Ascending) mengikuti siklus tiga state.
- Pada TC-FA-FAAM-384 Filter UoM `Unit` bawaan blok sebelumnya masih aktif sesuai langkah 1 TC (filter UoM `Unit`) dan Search `Seed` diketik ulang karena Search dikosongkan pada TC-FA-FAAM-383.
- Pembanding "seluruh baris memuat `Seed` dan ber-UoM `Unit`" didahului Verifikasi `Seed Item 01` tampil (bagian 8b butir 2).
