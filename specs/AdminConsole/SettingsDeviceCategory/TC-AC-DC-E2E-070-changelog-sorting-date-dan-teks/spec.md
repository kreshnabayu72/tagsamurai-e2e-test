---
id: TC-AC-DC-E2E-070-changelog-sorting-date-dan-teks
title: "Modal Changelog Category: Urutan Default, Sort Date, dan Sort Kolom Teks Action dan Category"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-188
  - TC-AC-DC-187
  - TC-AC-DC-189
coverage:
  web: automated
---

# Modal Changelog Category: Urutan Default, Sort Date, dan Sort Kolom Teks Action dan Category

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Principal `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1, nama tampil `Budi Santoso`, Modified By `Budi S`; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14), Riwayat Changelog Uji (No 17: dua belas entri, Field `Category`, pelaku `Budi S` dan `Maya P`), dan General Settings entitas uji (No 19: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Nilai persis dibaca dari tabel Pre-setup TC dan tidak ditulis ulang di luar langkah.
- Pemulihan Changelog: kemampuan fixture BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan mekanismenya) memulihkan Riwayat Changelog entitas uji ke Pre-setup No 17 di hook `before` dan `after`. Jumlah total entri (12) dan pembagian halaman pada asersi bersumber dari No 17.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-188: Urutan default Changelog: Date Newest First dengan tie pre-order terbalik

1. Klik ikon Changelog pada header Sidebar Category
2. Verifikasi baris pertama sampai keempat halaman 1: Delete `Kit Lama Anak`, Delete `Kit Lama`, Create `Tracker Seven`, Delete `Wearable`
3. Verifikasi entri paling baru berada di atas

### TC-AC-DC-187: Sort Date siklus 3 klik dengan aturan urutan pre-order untuk timestamp sama

4. Klik header Date satu kali
5. Verifikasi halaman 1 berurutan Oldest First dimulai dari `Scanner` (01/09/26)
6. Klik halaman 2 pada pagination
7. Verifikasi halaman 2 berisi `Kit Lama` (parent) lalu `Kit Lama Anak` pada timestamp sama (urutan pre-order, parent dahulu)
8. Klik halaman 1 pada pagination
9. Klik header Date kedua kali
10. Verifikasi `Kit Lama Anak` (descendant) tampil sebelum `Kit Lama` (parent) pada timestamp sama, diikuti `Tracker Seven`
11. Klik header Date ketiga kali
12. Verifikasi indikator sort Date hilang
13. Verifikasi urutan kembali ke default Date Newest First

### TC-AC-DC-189: Sort kolom teks Action dan Category: siklus 3 klik A-Z dan Z-A

14. Klik header Action sekali
15. Verifikasi seluruh baris Create (6) tampil lebih dulu dengan urutan Newest First di dalam grup
16. Verifikasi baris Delete tampil sesudah baris Create, lalu baris Edit
17. Klik header Action dua kali
18. Verifikasi baris Edit tampil lebih dulu, lalu Delete, lalu Create
19. Klik header Action sekali lagi
20. Verifikasi indikator sort Action hilang
21. Verifikasi urutan kembali default Date Newest First
22. Klik header Category sekali
23. Verifikasi urutan A-Z case-insensitive dimulai `Gateway Kit`, `Gateway Kit Plus`, `Kit Lama`, `Kit Lama`
24. Klik header Category sekali lagi
25. Verifikasi urutan Z-A case-insensitive dimulai `Wearable`, `Wearable`, `Tracker Seven`
26. Klik header Category sekali lagi
27. Verifikasi indikator sort Category hilang
28. Verifikasi urutan kembali default Date Newest First

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-188, 187, 189). Tidak ada TC hanya-BE di spec ini.
- Urutan TC di spec: 188 (default), 187, lalu 189; tidak ada aksi tulis.
- TC-AC-DC-187 klik sort Date kedua kali dilakukan pada halaman 1 karena sort mempertahankan nomor halaman (TC-AC-DC-194); langkah kembali ke halaman 1 adalah langkah penghubung.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah dari TC): langkah 8.
- Temuan untuk QA:
  - Asersi spec ini bergantung pada isi persis Riwayat Changelog Pre-setup #17 (dua belas entri, termasuk angka total 12 dan pembagian halaman), sedangkan S-12 melarang angka total absolut pada audit trail permanen dan Lampiran A belum punya butir untuk modul ini. Spec mengikuti TC dan mengandalkan kemampuan fixture BE yang memulihkan Changelog entitas uji ke #17 sebelum dan sesudah spec. Perlu keputusan pengecualian Lampiran A (setara A-5) atau entitas uji khusus Changelog.
  - TC-AC-DC-187 butir a menyebut halaman 2 berisi `Kit Lama` lalu `Kit Lama Anak` tanpa menyebut bahwa pengguna harus berpindah halaman; spec menambah klik halaman 2 dan halaman 1.
