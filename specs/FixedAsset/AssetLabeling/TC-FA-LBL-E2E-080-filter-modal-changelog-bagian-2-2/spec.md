---
id: TC-FA-LBL-E2E-080-filter-modal-changelog-bagian-2-2
title: "Filter Modal Changelog (bagian 2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-301
  - TC-FA-LBL-302
  - TC-FA-LBL-303
  - TC-FA-LBL-304
coverage:
  web: automated
---

# Filter Modal Changelog (bagian 2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Changelog (Pre-setup #17; pengguna Sarah Johnson), email dari `Fixture.assetLabeling.akun.totalControlChangelog` (pola `totalControl_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_CHANGELOG_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`). Email lengkap Company Changelog tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Hook suite (`before`, `beforeEach`, `after` pada `suite.md`) berlaku, termasuk flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan state global. Fixture `fixtures/asset-labeling.json` (identitas akun dan nilai seed, tanpa rahasia) belum ada dan disediakan tim FE. Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlChangelog` (belum ada; disediakan tim FE, S-12).
- Data Pre-setup #17 (Company Changelog, hanya dibaca): log Changelog Labels memuat tujuh baris seed (Date 08 sampai 15 Sep 2026): Create `High Priority` (15 Sep 2026 14:20, Sarah J), Edit `High Priority` Color `#DC2626` ke `#EF4444` (15 Sep 2026 14:25, Sarah J), Create `Finance Department` (14 Sep 2026 11:15, David K), Edit `Finance Department` Label Name `Finance Dept` ke `Finance Department` (14 Sep 2026 11:30, David K), Create `Audit Ready` (12 Sep 2026 09:40, Sarah J), Create `Executive Asset` (10 Sep 2026 16:30, Michael W), Delete `Old Tag` (08 Sep 2026 13:00, David K). Entri TC lain (mis. Delete bertanggal hari run dari TC-FA-LBL-325) menambah entri permanen bertanggal hari run sehingga ketujuh baris seed dapat bergeser ke luar halaman pertama (pagination default 10 per halaman). Karena itu spec menerapkan Filter Date `08 Sep 2026` sampai `15 Sep 2026` (rentang inklusif) di Filter Panel Modal Changelog sebelum mengamati baris seed, dan asersi dinilai atas hasil filter itu: tepat tujuh baris seed (entri TC lain berada di luar rentang) (S-12, S-14). N = jumlah entri log dalam rentang Filter Date itu, dibaca lewat pembacaan BE sebelum aksi pertama yang diasersi.
- Kemampuan teknis: pembacaan jumlah entri log Company Changelog dalam rentang Filter Date `08 Sep 2026` sampai `15 Sep 2026` (N) lewat fixture BE yang disediakan tim FE/BE (endpoint tidak tertulis di TC); dipakai sebelum aksi pertama yang diasersi (bagian 8b butir 10).
- State global yang diubah: tidak ada. Tidak ada data dinamis; spec tidak membuat atau mengubah data backend. Search dan Filter dibersihkan antar TC dan di akhir spec.

## Test Steps

### Persiapan

1. Baca jumlah entri N Company Changelog dengan Date `08 Sep 2026` sampai `15 Sep 2026` lewat pembacaan BE

### TC-FA-LBL-301: Search lalu Filter di Changelog menghasilkan irisan

2. Klik icon Changelog di Table Tools
3. Ketik Search `Finance`, tekan Enter
4. Klik icon Filter di toolbar modal
5. Pilih rentang `08 Sep 2026` sampai `15 Sep 2026` dan `Action` = `Edit` lalu klik `[Apply]`
6. Verifikasi tabel memuat tepat satu baris: `Edit Finance Department`
7. Verifikasi keyword `Finance` tidak tereset: kotak Search masih berisi `Finance`
8. Klik `(←)` pada kotak Search
9. Tutup Modal Changelog dengan `[✕]`

### TC-FA-LBL-302: Filter lalu Search di Changelog menghasilkan irisan yang sama

10. Klik icon Changelog di Table Tools
11. Klik icon Filter di toolbar modal
12. Pilih rentang `08 Sep 2026` sampai `15 Sep 2026` dan `Action` = `Edit` lalu klik `[Apply]`
13. Ketik Search `Finance`, tekan Enter
14. Verifikasi tabel memuat tepat satu baris: `Edit Finance Department`
15. Klik `(←)` pada kotak Search
16. Tutup Modal Changelog dengan `[✕]`

### TC-FA-LBL-303: Filter Field Changelog tampil karena entitas mencatat dua nilai field

17. Klik icon Changelog di Table Tools
18. Klik icon Filter di toolbar modal
19. Verifikasi field filter `Field` tampil di Filter Panel
20. Buka dropdown `Field`
21. Verifikasi opsi `Field`: `Label Name` dan `Color`
22. Tutup Modal Changelog dengan `[✕]`

### TC-FA-LBL-304: Membuka ulang Modal Changelog tidak membawa filter ter-Apply sebelumnya

23. Klik icon Changelog di Table Tools
24. Klik icon Filter di toolbar modal
25. Pilih `Action` = `Delete` lalu klik `[Apply]`
26. Tutup Modal Changelog dengan `[✕]`
27. Klik icon Changelog di Table Tools
28. Verifikasi modal terbuka tanpa filter ter-Apply
29. Verifikasi modal memakai sort default Date Newest First
30. Klik icon Filter di toolbar modal
31. Pilih rentang `08 Sep 2026` sampai `15 Sep 2026` lalu klik `[Apply]`
32. Verifikasi tabel memuat N baris hasil Filter Date, tepat tujuh baris seed, termasuk baris non-Delete (filter `Action` = `Delete` sebelumnya tidak terbawa)
33. Verifikasi tabel memakai sort default Date Newest First
34. Tutup Modal Changelog dengan `[✕]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` (bagian 4b).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 (membaca jumlah entri N dalam rentang Filter Date sebelum Modal Changelog dibuka, TC-FA-LBL-304), `(←)` pada kotak Search (langkah 8 dan 15), dan menutup Modal Changelog dengan `[✕]` (langkah 9, 16, 22) sebagai penutup blok TC. Langkah 'Klik icon Changelog di Table Tools' (langkah 2, 10, 17, 23) adalah Langkah 1 TC-FA-LBL-301, 302, 303, dan 304 menurut TC (TC-FA-LBL-301 dan 302 kini diawali langkah ini): tiap blok membuka modal sendiri. Tidak ada pembukaan ganda: modal selalu ditutup oleh penutup blok sebelumnya (langkah 9, 16, 22), jadi pembukaan itu bukan penambahan di luar TC. Modal ditutup antar TC supaya Filter Panel dimulai tertutup (perilaku Filter pada buka ulang modal diuji TC-FA-LBL-304); TC-FA-LBL-304 sendiri menutup dan membuka modal sebagai langkahnya (langkah 26 dan 27). Urutan langkah TC-FA-LBL-304 mengikuti TC: setelah dibuka ulang modal diamati tanpa filter ter-Apply, baru Filter Date rentang seed di-Apply dan hasilnya diamati. TC-FA-LBL-301 dan TC-FA-LBL-302 menerapkan rentang Filter Date seed bersama `Action` = `Edit`, sehingga asersi dinilai atas hasil Filter Date.
- Pasangan TC filter bagian 1 (TC-FA-LBL-296 sampai TC-FA-LBL-300) ada di spec 079.
- Temuan untuk QA:
  - TC-FA-LBL-301 dan TC-FA-LBL-302 tidak menyatakan apakah Search dan Filter dari TC sebelumnya terbawa; spec membersihkan Search dengan `(←)` dan mengandalkan buka ulang modal untuk Filter (TC-FA-LBL-304).
  - TC-FA-LBL-304 tidak menyatakan apakah keyword Search ikut dibuang saat modal dibuka ulang; spec hanya mengasersi Filter dan sort default sesuai Expected.
  - Email akun Total Control Company Changelog tidak tertulis lengkap di Pre-setup #17 (hanya pola dengan `{namaCompany}`); akun disediakan tim FE.
