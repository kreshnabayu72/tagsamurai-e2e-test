---
id: TC-FA-SU-E2E-290-tab-user-log-sub-tab-session-setup-column-dan-pagination
title: "Tab User Log sub-tab Session: Setup Column dan Pagination"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-886
  - TC-FA-SU-887
coverage:
  web: automated
---

# Tab User Log sub-tab Session: Setup Column dan Pagination

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab User Log sub-tab Session Budi Santoso (Pre-setup #30, 9 baris; urutan default Date descending). Label baris = `Date|Note` (kolom Activity bernilai `Session`, kolom Status bernilai `—`); alias dipakai langkah:
  - S-1: `16/07/26 08:12|Session started`
  - S-2: `15/07/26 20:30|Session ended`
  - S-3: `15/07/26 08:00|Session started`
  - S-4: `14/07/26 08:40|Session ended`, IP Address `192.0.2.40`, Device/Browser memuat `Safari`
  - S-5: `14/07/26 08:05|Session started`, IP Address `192.0.2.40`, Device/Browser memuat `Safari`
  - S-6: `13/07/26 17:05|Session ended`
  - S-7: `13/07/26 08:10|Session started`
  - S-8: `12/07/26 17:15|Session ended`
  - S-9: `12/07/26 08:02|Session started`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed User Log #30 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface User Log dan tidak menambah entri pada Budi Santoso.
- Tabel "Kolom Setup Column Hideable" (parameter langkah berulang): Date, Activity, Status, Note, IP Address, Device/Browser.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

### TC-FA-SU-886: Reset to Default, Discard (✕ atau Esc), dan independensi cache Setup Column

1. Buka Detail pengguna Budi Santoso lalu klik tab User Log, sub-tab Session
2. Buka Setup Column, sembunyikan satu kolom dan pin satu kolom
3. Klik `[Reset to Default]`
4. Verifikasi visibility, urutan, dan pin kembali ke default modul pada preview
5. Klik `[Save]`
6. Verifikasi konfigurasi default menjadi permanen setelah `[Save]`
7. Buka Setup Column, sembunyikan satu kolom, lalu tutup lewat ✕
8. Verifikasi perubahan preview dibuang dan tabel memakai konfigurasi tersimpan terakhir
9. Buka Setup Column, sembunyikan satu kolom, lalu tekan Esc
10. Verifikasi perubahan preview dibuang dan tabel memakai konfigurasi tersimpan terakhir
11. Buka Setup Column, sembunyikan satu kolom, klik `[Save]`, lalu buka tabel lain yang punya Setup Column (User List)
12. Verifikasi konfigurasi tabel lain tidak terpengaruh perubahan tabel ini (cache per tabel)
13. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

### TC-FA-SU-887: Pagination: page size, navigasi, dan kasus tepi

14. Verifikasi default 10 baris per halaman
15. Klik dropdown page size
16. Verifikasi pilihan page size 10, 25, 50, 100 tanpa opsi All
17. Tekan Esc untuk menutup dropdown page size
18. Isi nomor halaman `0`, tekan Enter
19. Verifikasi tabel tetap di halaman 1
20. Isi nomor halaman `-1`, tekan Enter
21. Verifikasi tabel tetap di halaman 1
22. Isi nomor halaman `999`, tekan Enter
23. Verifikasi tabel tetap di halaman 1
24. Isi nomor halaman `abc`, tekan Enter
25. Verifikasi tabel tetap di halaman 1
26. Ganti page size ke 25
27. Verifikasi tabel menampilkan halaman 1
28. Ganti page size kembali ke 10
29. Verifikasi tabel menampilkan halaman 1
30. Klik header Date satu kali
31. Verifikasi tabel menampilkan halaman 1
32. Klik header Date dua kali lagi hingga netral
33. Ketik Search `Session`, tekan Enter
34. Verifikasi tabel menampilkan halaman 1
35. Klik icon ← pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah 15 (`Klik dropdown page size`) dan langkah 17 (`Tekan Esc untuk menutup dropdown page size`) mengikuti Langkah Uji TC (klik dropdown page size, amati pilihan, tutup dengan Esc) sehingga pilihan page size diasersi saat dropdown terbuka.
- TC-FA-SU-883 dan TC-FA-SU-884 ada di spec 289; TC-FA-SU-885 ada di spec 294.
- Temuan untuk QA (S-15): (1) Post Condition preferensi kolom tersimpan per perangkat (atau kembali ke default) tidak punya langkah observasi di luar Expected dan tidak diasersi tambahan. Spec ini menyimpan konfigurasi Setup Column di browser; `suite.md` belum mencantumkan daftar spec yang menyimpan konfigurasi kolom (bagian 4 konvensi), sehingga perlu ditambahkan tim FE. (2) TC-FA-SU-887: Expected e adalah catatan tanpa langkah observasi sehingga tidak diasersi.
