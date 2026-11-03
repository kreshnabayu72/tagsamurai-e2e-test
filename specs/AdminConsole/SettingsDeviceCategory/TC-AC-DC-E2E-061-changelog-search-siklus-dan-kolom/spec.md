---
id: TC-AC-DC-E2E-061-changelog-search-siklus-dan-kolom
title: "Modal Changelog Category: Search Siklus Interaksi, Placeholder, dan Kelas Kolom Teks"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-155
  - TC-AC-DC-156
  - TC-AC-DC-157
coverage:
  web: automated
---

# Modal Changelog Category: Search Siklus Interaksi, Placeholder, dan Kelas Kolom Teks

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Principal `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1, nama tampil `Budi Santoso`, Modified By `Budi S`; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14), Riwayat Changelog Uji (No 17: dua belas entri, Field `Category`, pelaku `Budi S` dan `Maya P`), dan General Settings entitas uji (No 19: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Nilai persis dibaca dari tabel Pre-setup TC dan tidak ditulis ulang di luar langkah.
- Pemulihan Changelog: kemampuan fixture BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan mekanismenya) memulihkan Riwayat Changelog entitas uji ke Pre-setup No 17 di hook `before` dan `after`. Jumlah total entri (12) dan pembagian halaman pada asersi bersumber dari No 17.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-155: Siklus interaksi Search: reveal, auto-focus, submit lewat Enter, clear, dan collapse

1. Klik ikon Changelog pada header Sidebar Category
2. Klik ikon Search
3. Verifikasi kursor fokus di dalam input pencarian
4. Ketik `scan` tanpa menekan Enter
5. Verifikasi icon `(✕)` muncul
6. Verifikasi tabel belum tersaring (pencarian tidak live): halaman 1 masih menampilkan 10 baris dari 12 entri
7. Tekan Enter
8. Verifikasi tabel menampilkan 3 baris yang cocok dengan "scan" (`Scanner`, `Scanner Pro`, `Scanner Max`)
9. Klik icon `(✕)`
10. Verifikasi teks pencarian hilang
11. Verifikasi kolom pencarian tetap terbuka
12. Verifikasi tabel belum reset (masih 3 baris)
13. Tekan Enter pada input kosong
14. Verifikasi tabel reset menampilkan 10 baris pada halaman 1 dari 12 entri
15. Ketik Search `kit`, tekan Enter, lalu klik icon panah `(←)` di kiri toolbar
16. Verifikasi kolom pencarian menutup menjadi ikon Search
17. Verifikasi tabel langsung reset menampilkan 10 baris pada halaman 1 dari 12 entri

### TC-AC-DC-156: Teks placeholder default pada kolom pencarian Changelog

18. Klik ikon Search
19. Verifikasi placeholder kolom pencarian berisi "Search action, category..."

### TC-AC-DC-157: Search per kelas kolom teks: Action, Category, dan Field

20. Ganti isi kotak search dengan `delet`, tekan Enter
21. Verifikasi tabel menampilkan 3 baris Delete (`Kit Lama Anak`, `Kit Lama`, `Wearable`); kata kunci cocok sebagai substring Action, bukan awalan
22. Ganti isi kotak search dengan `WEAR`, tekan Enter
23. Verifikasi tabel menampilkan 2 baris dengan Category `Wearable` (Create dan Delete); pencarian case-insensitive
24. Ganti isi kotak search dengan `categ`, tekan Enter
25. Verifikasi halaman 1 menampilkan 10 baris
26. Klik halaman 2 pada pagination
27. Verifikasi halaman 2 menampilkan 2 baris (total 12 baris cocok pada kolom Field)

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-155, 156, 157). Tidak ada TC hanya-BE di spec ini.
- Frasa 'Hapus input lalu cari' pada TC-AC-DC-157 ditulis 'Ganti isi kotak search dengan' (8b.9).
- Temuan untuk QA:
  - Asersi spec ini bergantung pada isi persis Riwayat Changelog Pre-setup #17 (dua belas entri, termasuk angka total 12 dan pembagian halaman), sedangkan S-12 melarang angka total absolut pada audit trail permanen dan Lampiran A belum punya butir untuk modul ini. Spec mengikuti TC dan mengandalkan kemampuan fixture BE yang memulihkan Changelog entitas uji ke #17 sebelum dan sesudah spec. Perlu keputusan pengecualian Lampiran A (setara A-5) atau entitas uji khusus Changelog.
