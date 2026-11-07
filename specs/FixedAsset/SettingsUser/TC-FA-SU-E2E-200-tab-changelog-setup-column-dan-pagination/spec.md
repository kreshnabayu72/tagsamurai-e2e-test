---
id: TC-FA-SU-E2E-200-tab-changelog-setup-column-dan-pagination
title: "Tab Changelog: Setup Column dan Pagination"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-599
  - TC-FA-SU-600
coverage:
  web: automated
---

# Tab Changelog: Setup Column dan Pagination

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab Changelog Budi Santoso (Pre-setup #27, 7 baris; urutan default Date descending): dipakai sebagai precondition TC, tidak diasersi.
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

### TC-FA-SU-599: Reset to Default, Discard, independensi cache

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail pengguna Budi Santoso lalu klik tab Changelog
3. Buka Setup Column, sembunyikan satu kolom dan pin satu kolom
4. Klik `[Reset to Default]`
5. Verifikasi visibility, urutan, dan pin kembali ke default modul pada preview
6. Klik `[Save]`
7. Verifikasi konfigurasi default menjadi permanen setelah `[Save]`
8. Buka Setup Column, sembunyikan satu kolom, lalu tutup lewat ✕
9. Verifikasi perubahan preview dibuang dan tabel memakai konfigurasi tersimpan terakhir
10. Buka Setup Column, sembunyikan satu kolom, lalu tekan Esc
11. Verifikasi perubahan preview dibuang dan tabel memakai konfigurasi tersimpan terakhir
12. Buka Setup Column, sembunyikan satu kolom, klik `[Save]`, lalu buka tabel lain yang punya Setup Column (User List)
13. Verifikasi konfigurasi tabel lain tidak terpengaruh perubahan tabel ini (cache per tabel)
14. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

### TC-FA-SU-600: Pagination

15. Kembali ke User List, ganti isi kotak search dengan `Budi Santoso`, tekan Enter, klik nama Budi Santoso, lalu buka tab Changelog
16. Verifikasi default 10 baris per halaman
17. Klik dropdown page size
18. Verifikasi pilihan page size 10, 25, 50, 100 tanpa opsi All
19. Tekan Esc untuk menutup dropdown page size
20. Isi nomor halaman `0`, tekan Enter
21. Verifikasi tabel tetap di halaman 1
22. Isi nomor halaman `-1`, tekan Enter
23. Verifikasi tabel tetap di halaman 1
24. Isi nomor halaman `999`, tekan Enter
25. Verifikasi tabel tetap di halaman 1
26. Isi nomor halaman `abc`, tekan Enter
27. Verifikasi tabel tetap di halaman 1
28. Ganti page size ke 25
29. Verifikasi tabel menampilkan halaman 1
30. Ganti page size kembali ke 10
31. Verifikasi tabel menampilkan halaman 1
32. Klik header Date satu kali
33. Verifikasi tabel menampilkan halaman 1
34. Ketik Search `Home`, tekan Enter
35. Verifikasi tabel menampilkan halaman 1
36. Klik `(←)` pada kotak Search

## Notes

- Jumlah langkah 36, di atas smell 35 langkah; semua blok satu kelas harness (Setup Column dan pagination Tab Changelog Detail) dan berdiri sendiri; kelebihan berasal dari langkah penghubung buka ulang Detail lewat Search (S-03, R-16).
- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pembukaan ulang Detail Budi Santoso > Changelog sesudah User List dan muat ulang (langkah 15), pengosongan Search, penutupan overlay, pembukaan dan penutupan dropdown page size, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung tambahan (S-03): langkah 1 (Ketik Search `Budi Santoso`, tekan Enter sebelum membuka Detail, supaya spec tidak mengandalkan posisi baris pada User List 25 pengguna 3 halaman, R-16, bagian 8b butir 13).
- TC-FA-SU-598 (pin dan unpin Tab Changelog) ada di spec 212.
- Temuan untuk QA (S-15): (1) Expected e (fixture hanya satu halaman, multi-halaman diuji di TC-FA-SU-359 dan TC-FA-SU-1057) adalah catatan tanpa langkah observasi sehingga tidak diasersi. (2) Post Condition TC-FA-SU-599 (preferensi kembali ke default setelah Reset to Default dan Save) tidak punya langkah observasi di luar Expected a dan tidak diasersi tambahan. (3) Langkah `[Save]` pada langkah "Buka Setup Column, sembunyikan satu kolom, klik `[Save]`, lalu buka tabel lain" ditambahkan spec tanpa dasar TC: TC-FA-SU-599 langkah 4 dan 5 hanya menutup lewat ✕ atau Esc, dan langkah 6 membandingkan tabel lain tanpa menyebut Save. Save dipilih agar perubahan tersimpan di tabel ini sebelum dibandingkan dengan User List (Expected c); pemilik TC perlu mengonfirmasi atau menyatakan cara lain.
