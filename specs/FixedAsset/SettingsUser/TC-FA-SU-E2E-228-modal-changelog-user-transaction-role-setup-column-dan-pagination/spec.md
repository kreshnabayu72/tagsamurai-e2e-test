---
id: TC-FA-SU-E2E-228-modal-changelog-user-transaction-role-setup-column-dan-pagination
title: "Modal Changelog User > Transaction Role: Setup Column dan Pagination"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-695
  - TC-FA-SU-696
coverage:
  web: automated
---

# Modal Changelog User > Transaction Role: Setup Column dan Pagination

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Modal Changelog Budi Santoso > Transaction Role (Pre-setup #27, 5 baris; urutan default Date descending). Alias baris yang dipakai langkah (nilai kolom Field; Modified By):
  - TR-1: `Damaged — Branch Surabaya — Monitoring & Report`; Modified By `Ahmad D`
  - TR-2: `Missing — Branch Surabaya — Approver`; Modified By `Ahmad D`
  - TR-3: `Disposal — Logistics Warehouse — Asset Admin`; Modified By `Lina M`
  - TR-4: `Disposal — Logistics Warehouse — Staff`; Modified By `Lina M`
  - TR-5: `Transfer — Finance & Accounting — Asset Admin`; Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

### TC-FA-SU-695: Reset to Default, Discard, independensi cache

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail pengguna Budi Santoso, klik tab Role, klik sub-tab Transaction Role, lalu klik icon Changelog
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

### TC-FA-SU-696: Pagination

14. Kembali ke User List, ganti isi kotak search dengan `Budi Santoso`, tekan Enter, lalu buka Detail pengguna Budi Santoso, klik tab Role, klik sub-tab Transaction Role, lalu klik icon Changelog
15. Verifikasi default 10 baris per halaman
16. Klik dropdown page size
17. Verifikasi pilihan page size 10, 25, 50, 100 tanpa opsi All
18. Tekan Esc untuk menutup dropdown page size
19. Isi nomor halaman `0`, tekan Enter
20. Verifikasi tabel tetap di halaman 1
21. Isi nomor halaman `-1`, tekan Enter
22. Verifikasi tabel tetap di halaman 1
23. Isi nomor halaman `999`, tekan Enter
24. Verifikasi tabel tetap di halaman 1
25. Isi nomor halaman `abc`, tekan Enter
26. Verifikasi tabel tetap di halaman 1
27. Ganti page size ke 25
28. Verifikasi tabel menampilkan halaman 1
29. Ganti page size kembali ke 10
30. Verifikasi tabel menampilkan halaman 1
31. Klik header Date satu kali
32. Verifikasi tabel menampilkan halaman 1
33. Ketik Search `Assign`, tekan Enter
34. Verifikasi tabel menampilkan halaman 1
35. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pembukaan dan penutupan dropdown page size, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung (S-03, R-16): Search `Budi Santoso` pada User List menyaring baris target sebelum membuka Detail (langkah 1 dan 14) karena User List dapat memuat lebih dari satu halaman (bagian 8b butir 13); langkah ini tidak mengubah data dan tidak ada TC berikutnya yang membutuhkan tabel penuh (S-09).
- TC-FA-SU-694 (pin dan unpin modal Transaction Role) ada di spec 231.
- Temuan untuk QA (S-15): (1) Expected e (fixture hanya satu halaman, multi-halaman diuji di TC-FA-SU-359 dan TC-FA-SU-1057) adalah catatan tanpa langkah observasi sehingga tidak diasersi. (2) TC tidak menyebut tabel lain yang dipakai untuk memeriksa independensi cache; spec memilih User List. Post Condition preferensi kolom kembali ke default tidak punya langkah observasi di luar Expected a dan b sehingga tidak diasersi tersendiri. (3) Langkah `[Save]` pada langkah "Buka Setup Column, sembunyikan satu kolom, klik `[Save]`, lalu buka tabel lain" ditambahkan spec tanpa dasar TC: TC-FA-SU-695 langkah 4 dan 5 hanya menutup lewat ✕ atau Esc, dan langkah 6 membandingkan tabel lain tanpa menyebut Save. Save dipilih agar perubahan tersimpan di tabel ini sebelum dibandingkan dengan User List (Expected c); pemilik TC perlu mengonfirmasi atau menyatakan cara lain.
