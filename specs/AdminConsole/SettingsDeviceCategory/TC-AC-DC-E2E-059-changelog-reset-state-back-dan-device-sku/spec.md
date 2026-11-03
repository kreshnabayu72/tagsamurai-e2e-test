---
id: TC-AC-DC-E2E-059-changelog-reset-state-back-dan-device-sku
title: "Modal Changelog Category: Isi Sel, Reset State, Tombol Back, Sub-tab Device SKU, dan Nama Category 120 Karakter"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-151
  - TC-AC-DC-153
  - TC-AC-DC-268
  - TC-AC-DC-272
  - TC-AC-DC-150
coverage:
  web: automated
---

# Modal Changelog Category: Isi Sel, Reset State, Tombol Back, Sub-tab Device SKU, dan Nama Category 120 Karakter

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Principal `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1, nama tampil `Budi Santoso`, Modified By `Budi S`; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14), Riwayat Changelog Uji (No 17: dua belas entri, Field `Category`, pelaku `Budi S` dan `Maya P`), dan General Settings entitas uji (No 19: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Nilai persis dibaca dari tabel Pre-setup TC dan tidak ditulis ulang di luar langkah.
- Pemulihan Changelog: kemampuan fixture BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan mekanismenya) memulihkan Riwayat Changelog entitas uji ke Pre-setup No 17 di hook `before` dan `after`. Jumlah total entri (12) dan pembagian halaman pada asersi bersumber dari No 17.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- Data Dinamis: node dengan nama 120 karakter `Pemindai Kode Batang Industri Tahan Banting Gudang Besar Nirkabel Pemindai Kode Batang Industri Tahan Banting Gudang Bes` (Data Uji TC-AC-DC-150, tanpa suffix karena panjang 120 karakter adalah objek uji) dibuat spec lewat UI di bawah `Rugged Scanner` (node Pre-setup No 14, hanya sebagai induk); dihapus lewat API di hook `after` bila masih ada.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-151: Nilai kolom Field dan penanda kosong Old Value atau New Value pada entri Create dan Delete

1. Klik ikon Changelog pada header Sidebar Category
2. Verifikasi kolom Field baris Create `Tracker Seven` berisi "Category"
3. Verifikasi kolom Field baris Delete `Kit Lama` berisi "Category"
4. Verifikasi Old Value baris Create `Tracker Seven` berisi "—"
5. Verifikasi New Value baris Delete `Kit Lama` berisi "—"

### TC-AC-DC-153: State Search, Filter, Sort, dan Pagination Changelog direset saat modal dibuka ulang

6. Klik header Category sekali
7. Klik halaman 2 pada pagination
8. Ketik Search `kit`, tekan Enter
9. Klik ikon Filter, buka dropdown Action, centang "Create", klik `[Apply]`
10. Tutup modal lewat icon `[×]`, lalu klik ikon Changelog pada header Sidebar Category
11. Verifikasi kotak pencarian kosong
12. Verifikasi tidak ada filter ter-Apply
13. Verifikasi urutan kembali default Date Newest First
14. Verifikasi halaman 1 menampilkan 10 baris dari 12 entri
15. Klik halaman 2 pada pagination
16. Verifikasi halaman 2 berisi 2 baris

### TC-AC-DC-268: Tombol Back browser saat modal Changelog terbuka kembali ke halaman sebelumnya dan modal tidak masuk riwayat

17. Tutup modal lewat icon `[×]`
18. Klik menu halaman Admin Console lain di sidebar (halaman bebas selain Settings > Device)
19. Buka halaman Settings > Device > Device Name lewat menu sidebar
20. Klik ikon Changelog pada header Sidebar Category
21. Tekan tombol Back browser
22. Verifikasi pengguna berada di halaman sebelumnya (halaman Admin Console lain)
23. Verifikasi modal Changelog tidak tampil
24. Tekan tombol Forward browser
25. Verifikasi halaman Device Name tampil
26. Verifikasi modal Changelog tidak tampil (modal tidak masuk riwayat browser)

### TC-AC-DC-272: Modal Changelog Category dibuka dari header Sidebar Category pada sub-tab Device SKU

27. Klik sub-tab Device SKU pada Settings > Device
28. Klik ikon Changelog pada header Sidebar Category
29. Verifikasi modal "Changelog: Category" terbuka
30. Verifikasi baris teratas modal adalah Delete `Kit Lama Anak`
31. Verifikasi halaman 1 berisi 10 baris dari 12 entri

### TC-AC-DC-150: Nama Category 120 karakter tampil utuh tanpa truncate di sel Changelog

32. Tutup modal lewat icon `[×]`, lalu klik sub-tab Device Name pada Settings > Device
33. Expand `Hardware` lalu `Handheld Reader`
34. Hover node `Rugged Scanner`, klik aksi `+ Subcategory`, ketik nama 120 karakter `Pemindai Kode Batang Industri Tahan Banting Gudang Besar Nirkabel Pemindai Kode Batang Industri Tahan Banting Gudang Bes`, klik `[Submit]`
35. Tunggu aksi selesai
36. Klik ikon Changelog pada header Sidebar Category
37. Verifikasi Category baris teratas menampilkan nama 120 karakter secara utuh (teks biasa tanpa pemotongan `..`)
38. Verifikasi New Value baris teratas menampilkan nama 120 karakter secara utuh (teks biasa tanpa pemotongan `..`)
39. Verifikasi kolom melebar mengikuti isi dan tidak ada tooltip pemotongan
40. Verifikasi tinggi baris tetap konsisten

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-151, 153, 268, 272, 150). Tidak ada TC hanya-BE di spec ini.
- Urutan TC di spec: 151, 153, 268, 272, lalu 150 (aksi tulis di akhir, S-10).
- Node tulis TC-AC-DC-150 memakai nama literal 120 karakter tanpa suffix `{runId}`: panjang 120 karakter adalah objek uji (R-06: nilai 'tepat N karakter' dihitung termasuk suffix); isolasi data dijaga dengan induk Pre-setup `Rugged Scanner` dan cleanup node di hook `after`.
- Alasan melewati sekitar 35 langkah: seluruh blok satu kelas harness (fungsional, satu permukaan modal Changelog Category) dan tiap TC berdiri sendiri dengan state yang dibersihkan antar TC, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah dari TC): langkah 15 (membuka halaman 2 sebelum Verifikasi halaman 2, S-14), langkah 17, 18, 19, 32, dan langkah 35 (Tunggu aksi selesai sesudah `[Submit]` pada langkah 34 yang hasilnya tidak diasersi, karena langkah berikutnya membuka modal Changelog, 8b butir 8).
- Temuan untuk QA:
  - Asersi spec ini bergantung pada isi persis Riwayat Changelog Pre-setup #17 (dua belas entri, termasuk angka total 12 dan pembagian halaman), sedangkan S-12 melarang angka total absolut pada audit trail permanen dan Lampiran A belum punya butir untuk modul ini. Spec mengikuti TC dan mengandalkan kemampuan fixture BE yang memulihkan Changelog entitas uji ke #17 sebelum dan sesudah spec. Perlu keputusan pengecualian Lampiran A (setara A-5) atau entitas uji khusus Changelog.
  - TC-AC-DC-268 prekondisi e menyebut pengguna sebelumnya berada di halaman Admin Console lain tanpa menyebut halamannya; spec memakai halaman bebas lewat menu sidebar (S-13: halaman tidak dikarang).
  - TC-AC-DC-153 langkah 3 hanya menyebut halaman 2 tampil dengan 2 baris; spec tidak mengasersinya karena bukan Expected.
  - Nama literal 120 karakter juga ada di Pre-setup No 14 sebagai leaf di bawah `Handheld Reader`; TC-AC-DC-150 membuat node bernama sama di bawah induk berbeda (`Rugged Scanner`). Bila aturan keunikan nama berlaku lintas induk, perlu pengecualian S-12 serupa A-2.
  - TC-AC-DC-150 butir b ('tinggi baris tetap konsisten') tidak menyebut nilai tinggi; spec mengasersi kekonsistenan secara kualitatif.
