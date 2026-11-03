---
id: TC-FA-LBL-E2E-078-search-modal-changelog-bagian-2-2
title: "Search Modal Changelog (bagian 2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-295
  - TC-FA-LBL-492
  - TC-FA-LBL-508
coverage:
  web: automated
---

# Search Modal Changelog (bagian 2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Changelog (Pre-setup #17; pengguna Sarah Johnson), email dari `Fixture.assetLabeling.akun.totalControlChangelog` (pola `totalControl_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_CHANGELOG_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`). Email lengkap Company Changelog tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Hook suite (`before`, `beforeEach`, `after` pada `suite.md`) berlaku, termasuk flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan state global. Fixture `fixtures/asset-labeling.json` (identitas akun dan nilai seed, tanpa rahasia) belum ada dan disediakan tim FE. Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlChangelog` (belum ada; disediakan tim FE, S-12).
- Data Pre-setup #17 (Company Changelog, hanya dibaca): log Changelog Labels memuat tujuh baris seed (Date 08 sampai 15 Sep 2026): Create `High Priority` (15 Sep 2026 14:20, Sarah J), Edit `High Priority` Color `#DC2626` ke `#EF4444` (15 Sep 2026 14:25, Sarah J), Create `Finance Department` (14 Sep 2026 11:15, David K), Edit `Finance Department` Label Name `Finance Dept` ke `Finance Department` (14 Sep 2026 11:30, David K), Create `Audit Ready` (12 Sep 2026 09:40, Sarah J), Create `Executive Asset` (10 Sep 2026 16:30, Michael W), Delete `Old Tag` (08 Sep 2026 13:00, David K). Entri TC lain (mis. Delete bertanggal hari run dari TC-FA-LBL-325) menambah entri permanen bertanggal hari run sehingga ketujuh baris seed dapat bergeser ke luar halaman pertama (pagination default 10 per halaman). Karena itu spec menerapkan Filter Date `08 Sep 2026` sampai `15 Sep 2026` (rentang inklusif) di Filter Panel Modal Changelog sebelum mengamati baris seed, dan asersi dinilai atas hasil filter itu: tepat tujuh baris seed (entri TC lain berada di luar rentang) (S-12, S-14). N = jumlah entri log dalam rentang Filter Date itu, dibaca lewat pembacaan BE sebelum aksi pertama yang diasersi.
- Kemampuan teknis: pembacaan jumlah entri log Company Changelog dalam rentang Filter Date `08 Sep 2026` sampai `15 Sep 2026` (N) lewat fixture BE yang disediakan tim FE/BE (endpoint tidak tertulis di TC); dipakai sebelum aksi pertama yang diasersi (bagian 8b butir 10).
- State global yang diubah: tidak ada. Tidak ada data dinamis; spec tidak membuat atau mengubah data backend. State Search dibersihkan di akhir spec.

## Test Steps

### Membuka Modal Changelog

1. Baca jumlah entri N Company Changelog dengan Date `08 Sep 2026` sampai `15 Sep 2026` lewat pembacaan BE
2. Klik icon Changelog di Table Tools

### TC-FA-LBL-295: Guard: kolom Date tidak ikut dicari

3. Ketik Search `15 Sep 2026`, tekan Enter
4. Verifikasi empty state `No results found`
5. Klik `(←)` pada kotak Search

### TC-FA-LBL-492: Search toolbar Modal Changelog: reveal, auto-focus, placeholder, tooltip, clear, submit lewat Enter, dan collapse

6. Klik icon Filter di toolbar modal
7. Pilih rentang `08 Sep 2026` sampai `15 Sep 2026` lalu klik `[Apply]`
8. Hover icon Search di toolbar modal
9. Verifikasi tooltip `Search`
10. Klik icon Search di toolbar modal
11. Verifikasi search bar melebar
12. Verifikasi kursor fokus di input
13. Verifikasi placeholder `Search label name, action...`
14. Ketik `Finance` tanpa menekan Enter
15. Verifikasi ikon `(✕)` muncul
16. Verifikasi tabel belum tersaring: baris `Create Audit Ready` masih tampil
17. Tekan Enter
18. Verifikasi tabel memuat tepat dua baris `Finance Department`
19. Klik ikon `(✕)` di dalam input
20. Verifikasi input kosong
21. Verifikasi search bar tetap terbuka
22. Verifikasi tabel masih menampilkan hasil `Finance`: tepat dua baris `Finance Department`
23. Tekan Enter pada input yang kosong
24. Verifikasi N baris hasil Filter Date tampil kembali (jumlah sama seperti sebelum Search), tepat tujuh baris seed
25. Klik ikon panah `(←)`
26. Verifikasi search bar menutup menjadi ikon Search
27. Verifikasi keyword Search kosong

### TC-FA-LBL-508: Search Changelog kolom Modified By mencocokkan nama lengkap user

28. Ketik Search `Johnson`, tekan Enter
29. Verifikasi pada hasil Filter Date, tabel memuat tiga baris seed `Sarah J`: `Create High Priority`, `Edit High Priority`, `Create Audit Ready`
30. Klik `(←)` pada kotak Search
31. Tutup Modal Changelog dengan `[✕]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` (bagian 4b).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Modal dibuka sekali di awal; tiap TC dimulai dari kotak Search yang tertutup dan kosong. TC-FA-LBL-295 berjalan lebih dulu tanpa Filter karena langkahnya tidak memuat Filter; Filter Date rentang seed di-Apply pada TC-FA-LBL-492 (langkah 6 dan 7) dan tetap berlaku untuk TC-FA-LBL-508, yang memuat langkah Filter identik.
- Langkah penghubung (tanpa awalan `Verifikasi`): membaca jumlah entri N dalam rentang Filter Date sebelum Modal Changelog dibuka (TC-FA-LBL-492), `(←)` pada kotak Search sesudah TC-FA-LBL-295 dan TC-FA-LBL-508 (menutup input dan mereset tabel), dan menutup Modal Changelog di akhir spec. `(←)` sesudah TC-FA-LBL-295 menyiapkan kotak Search tertutup untuk reveal pada TC-FA-LBL-492.
- Pada TC-FA-LBL-295 empty state `No results found` hasil Search menjadi anchor positif asersi (bagian 8b butir 2). Pada TC-FA-LBL-492 asersi "belum tersaring" memakai baris seed `Create Audit Ready` sebagai pembanding.
- Pasangan TC pencarian bagian 1 (TC-FA-LBL-290 sampai TC-FA-LBL-294) ada di spec 077.
- Temuan untuk QA:
  - TC-FA-LBL-295 memuat klausa kedua "penyaringan tanggal hanya lewat Filter Panel" yang berupa pernyataan aturan tanpa langkah observasi; spec tidak menambah langkah observasi sendiri. Penyaringan tanggal lewat Filter Panel dicakup TC-FA-LBL-298 di spec lain.
  - TC-FA-LBL-508 memakai Company Changelog dengan pengguna Sarah Johnson dan keyword `Johnson`, sementara TC-FA-LBL-294 memakai `david` tanpa nama lengkap David K; Pre-setup #17 tidak mencantumkan nama lengkap Modified By selain Sarah Johnson.
  - Email akun Total Control Company Changelog tidak tertulis lengkap di Pre-setup #17 (hanya pola dengan `{namaCompany}`); akun disediakan tim FE.
