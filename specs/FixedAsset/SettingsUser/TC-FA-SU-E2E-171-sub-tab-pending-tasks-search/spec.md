---
id: TC-FA-SU-E2E-171-sub-tab-pending-tasks-search
title: "Sub-tab Pending Tasks: Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-508
  - TC-FA-SU-509
  - TC-FA-SU-510
coverage:
  web: automated
---

# Sub-tab Pending Tasks: Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Responsibilities (#25): pengguna target Budi Santoso dengan 5 baris Sub-tab Pending Tasks (`BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`). Nilai kolom tiap baris mengikuti Pre-setup #25; asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11).
- Data Dinamis: tidak ada.
- Nilai Date untuk TC-FA-SU-509 (dari TC): kolom Request Date memuat `12/07/26` dan kolom Last Updated memuat `12/07/26`; baris asalnya tidak tertulis di Pre-setup #25.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; perubahan tampilan (Search, Filter, Sort, Column Visibility) dipulihkan oleh langkah penghubung spec.
- Urutan default (Request Date ascending): `BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`.

## Test Steps

1. Ketik Search `Budi Santoso` pada User List, tekan Enter, lalu buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Pending Tasks

### TC-FA-SU-508: Siklus interaksi Search

2. Hover icon Search
3. Verifikasi tooltip `Search`
4. Klik icon Search
5. Verifikasi input Search melebar
6. Verifikasi kursor fokus di input Search
7. Verifikasi placeholder `Search transaction ID, status, or group...`
8. Ketik karakter pertama `A` pada kotak Search tanpa menekan Enter
9. Verifikasi icon ✕ tampil di kanan input
10. Verifikasi tabel belum tersaring (kelima baris tampil)
11. Ketik sisa `SG-2026` pada kotak Search, tekan Enter
12. Verifikasi tabel tersaring menjadi `ASG-20260715-0045`, `ASG-20260718-0067`
13. Klik ✕ pada kotak Search
14. Verifikasi input kosong
15. Verifikasi search bar tetap terbuka
16. Verifikasi kursor fokus di input Search
17. Verifikasi tabel tetap menampilkan hasil search terakhir (`ASG-20260715-0045`, `ASG-20260718-0067`)
18. Tekan Enter pada input kosong
19. Verifikasi tabel kembali ke semua baris (kelima baris)
20. Ketik Search `ASG-2026`, tekan Enter
21. Klik `←` pada kotak Search
22. Verifikasi search bar menutup
23. Verifikasi keyword dikosongkan
24. Verifikasi tabel langsung kembali ke semua baris (kelima baris)
25. Ketik Search `  ASG-2026  ` (spasi awal dan akhir), tekan Enter
26. Verifikasi hasil sama dengan `ASG-2026` tanpa spasi (`ASG-20260715-0045`, `ASG-20260718-0067`)
27. Verifikasi isi input tidak berubah (spasi awal dan akhir tetap ada)

### TC-FA-SU-509: Guard kolom non-searchable (Request Date, Last Updated)

28. Klik `←` pada kotak Search
29. Verifikasi sel kolom Request Date pada salah satu baris tabel bernilai `12/07/26`
30. Verifikasi sel kolom Last Updated pada salah satu baris tabel bernilai `12/07/26`
31. Ketik Search `12/07/26` (nilai kolom Request Date), tekan Enter
32. Verifikasi `12/07/26` tidak mencocokkan baris melalui Search; empty state `No results found` tampil
33. Ganti isi kotak search dengan `12/07/26` (nilai kolom Last Updated), tekan Enter
34. Verifikasi `12/07/26` tidak mencocokkan baris melalui Search; empty state `No results found` tampil

### TC-FA-SU-510: Search terikat visibilitas kolom Transaction ID

35. Klik `←` pada kotak Search
36. Ketik Search `ASG-2026`, tekan Enter
37. Verifikasi keyword `ASG-2026` menyisakan `ASG-20260715-0045`, `ASG-20260718-0067`
38. Klik header kolom Actions (⋯), lalu hilangkan centang Transaction ID
39. Ganti isi kotak search dengan `ASG-2026`, tekan Enter
40. Verifikasi setelah kolom Transaction ID di-hide, keyword yang sama menyisakan tidak ada baris (kolom tersembunyi tidak dicari)
41. Klik header kolom Actions (⋯), lalu centang kembali Transaction ID
42. Ganti isi kotak search dengan `ASG-2026`, tekan Enter
43. Verifikasi setelah kolom Transaction ID di-unhide, hasil kembali `ASG-20260715-0045`, `ASG-20260718-0067`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Detail Budi Santoso; `←` pada kotak Search sebelum TC-FA-SU-509 dan TC-FA-SU-510 (S-09).
- Langkah penghubung Search (R-16, bagian 8b butir 9 dan 13): langkah 1 mengetik Search `Budi Santoso` pada User List sebelum membuka Detail, karena User List memuat 3 halaman sehingga spec tidak mengandalkan posisi baris di halaman.
- Verifikasi nilai Date pada langkah 29 dan 30 ditambahkan sebagai anchor positif sebelum asersi Search tanpa hasil pada langkah 32 dan 34 (8b butir 2); nilai `12/07/26` berasal dari TC-FA-SU-509.
- Jumlah langkah: 43 tertulis, 43 dengan ekspansi iterasi.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (43 langkah). Seluruh blok berada pada satu surface (satu sub-tab, satu dataset), satu kelas fungsional, tanpa mengubah data backend, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
