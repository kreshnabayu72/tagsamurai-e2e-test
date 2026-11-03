---
id: TC-AC-DC-E2E-071-changelog-sorting-nilai-field-modified-by
title: "Modal Changelog Category: Sort Kolom Field, Old Value, New Value, dan Modified By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-190
  - TC-AC-DC-191
coverage:
  web: automated
---

# Modal Changelog Category: Sort Kolom Field, Old Value, New Value, dan Modified By

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Principal `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1, nama tampil `Budi Santoso`, Modified By `Budi S`; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14), Riwayat Changelog Uji (No 17: dua belas entri, Field `Category`, pelaku `Budi S` dan `Maya P`), dan General Settings entitas uji (No 19: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Nilai persis dibaca dari tabel Pre-setup TC dan tidak ditulis ulang di luar langkah.
- Pemulihan Changelog: kemampuan fixture BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan mekanismenya) memulihkan Riwayat Changelog entitas uji ke Pre-setup No 17 di hook `before` dan `after`. Jumlah total entri (12) dan pembagian halaman pada asersi bersumber dari No 17.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-190: Sort kolom Field bernilai tunggal tidak mengubah urutan baris

1. Klik ikon Changelog pada header Sidebar Category
2. Klik header Field sekali
3. Verifikasi indikator sort Field ascending
4. Verifikasi urutan baris tidak berubah dari default Date Newest First
5. Klik header Field kedua kali
6. Verifikasi indikator sort Field descending
7. Verifikasi urutan baris tidak berubah dari default Date Newest First
8. Klik header Field sekali lagi
9. Verifikasi indikator sort Field hilang

### TC-AC-DC-191: Sort Old Value dan New Value: nilai kosong selalu di akhir saat ascending dan di awal saat descending

10. Klik header Old Value sekali
11. Verifikasi Old Value ascending berurutan A-Z: `Gateway Kit`, `Kit Lama`, `Kit Lama Anak`, `Scanner`, `Scanner Pro`, `Wearable`
12. Verifikasi baris kosong (Create) berada di akhir
13. Klik header Old Value sekali lagi
14. Verifikasi enam baris kosong (Create) tampil lebih dulu
15. Verifikasi dilanjutkan `Wearable` lalu `Scanner Pro`
16. Klik header Old Value sekali lagi
17. Verifikasi indikator sort Old Value hilang
18. Verifikasi urutan kembali default Date Newest First
19. Klik header New Value sekali
20. Verifikasi New Value ascending berurutan: `Gateway Kit`, `Gateway Kit Plus`, `Kit Lama`, `Kit Lama Anak`, `Scanner`, `Scanner Max`, `Scanner Pro`, `Tracker Seven`, `Wearable`
21. Verifikasi baris kosong (Delete) berada di akhir
22. Klik header New Value sekali lagi
23. Verifikasi tiga baris kosong (Delete) tampil lebih dulu
24. Verifikasi dilanjutkan `Wearable` lalu `Tracker Seven`
25. Klik header New Value sekali lagi
26. Verifikasi indikator sort New Value hilang
27. Verifikasi urutan kembali default Date Newest First

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-190, 191). Tidak ada TC hanya-BE di spec ini.
- Pembagian TC lintas spec: TC-AC-DC-192, 193, 194, dan 195 (sort Modified By, berpindah target, nomor halaman, kolom Actions) ada di spec 072.
- TC-AC-DC-191 butir a dan c membandingkan 10 baris halaman 1; enam nilai Old Value tidak kosong dan empat baris kosong pertama pada halaman 1.
- Temuan untuk QA:
  - Asersi spec ini bergantung pada isi persis Riwayat Changelog Pre-setup #17 (dua belas entri, termasuk angka total 12 dan pembagian halaman), sedangkan S-12 melarang angka total absolut pada audit trail permanen dan Lampiran A belum punya butir untuk modul ini. Spec mengikuti TC dan mengandalkan kemampuan fixture BE yang memulihkan Changelog entitas uji ke #17 sebelum dan sesudah spec. Perlu keputusan pengecualian Lampiran A (setara A-5) atau entitas uji khusus Changelog.
  - TC-AC-DC-191 butir b dan d menyebut baris kosong 'tampil lebih dulu' tanpa menyebut urutan di dalam grup kosong; spec tidak mengasersi urutan di dalam grup.
