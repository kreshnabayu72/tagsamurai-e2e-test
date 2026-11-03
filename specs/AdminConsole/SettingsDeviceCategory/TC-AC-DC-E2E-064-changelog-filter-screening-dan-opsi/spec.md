---
id: TC-AC-DC-E2E-064-changelog-filter-screening-dan-opsi
title: "Modal Changelog Category: Screening Filter Panel dan Filter Multi-select"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-166
  - TC-AC-DC-167
  - TC-AC-DC-168
  - TC-AC-DC-169
  - TC-AC-DC-170
coverage:
  web: automated
---

# Modal Changelog Category: Screening Filter Panel dan Filter Multi-select

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Principal `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1, nama tampil `Budi Santoso`, Modified By `Budi S`; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14), Riwayat Changelog Uji (No 17: dua belas entri, Field `Category`, pelaku `Budi S` dan `Maya P`), dan General Settings entitas uji (No 19: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Nilai persis dibaca dari tabel Pre-setup TC dan tidak ditulis ulang di luar langkah.
- Pemulihan Changelog: kemampuan fixture BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan mekanismenya) memulihkan Riwayat Changelog entitas uji ke Pre-setup No 17 di hook `before` dan `after`. Jumlah total entri (12) dan pembagian halaman pada asersi bersumber dari No 17.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-166: Screening Filter Panel Changelog: field, tipe kontrol, tombol, dan indikator

1. Klik ikon Changelog pada header Sidebar Category
2. Klik ikon Filter pada toolbar
3. Verifikasi ikon Filter berubah gelap selama panel terbuka
4. Verifikasi field pertama Date berupa date range picker berlabel "Date"
5. Verifikasi field kedua Action berupa multi-select searchable berlabel "Action" dengan placeholder "All actions"
6. Verifikasi field ketiga Category berupa multi-select searchable berlabel "Category" dengan placeholder "All categories"
7. Verifikasi field keempat Modified By berupa multi-select searchable berlabel "Modified By" dengan placeholder "All users"
8. Verifikasi tidak ada field filter untuk Field, Old Value, dan New Value
9. Verifikasi tombol `[Clear Field]` berada di kiri footer panel
10. Verifikasi tombol `[Apply]` berada di kanan footer panel

### TC-AC-DC-167: Placeholder field Date pada Filter Panel Changelog

11. Verifikasi placeholder field Date berisi "Select date"

### TC-AC-DC-168: Filter Action multi-select: satu opsi dan gabungan opsi (OR)

12. Buka dropdown Action, centang "Edit", klik `[Apply]`
13. Verifikasi tabel menampilkan 3 baris Edit (`Gateway Kit Plus`, `Scanner Pro`, `Scanner Max`)
14. Klik ikon Filter, klik `[Clear Field]`, buka dropdown Action, centang "Create" dan "Delete", klik `[Apply]`
15. Verifikasi tabel menampilkan 9 baris (gabungan OR dalam satu field)
16. Verifikasi baris Edit tidak tampil

### TC-AC-DC-169: Filter Category multi-select menyaring berdasarkan nama snapshot

17. Klik ikon Filter, klik `[Clear Field]`, klik `[Apply]`
18. Klik ikon Filter, buka dropdown Category, centang "Scanner Pro" dan "Wearable", klik `[Apply]`
19. Verifikasi tabel menampilkan 3 baris: Edit `Scanner Pro`, Create `Wearable`, Delete `Wearable`

### TC-AC-DC-170: Filter Modified By multi-select menyaring berdasarkan pelaku

20. Klik ikon Filter, klik `[Clear Field]`, buka dropdown Modified By, centang pelaku Maya, klik `[Apply]`
21. Verifikasi tabel menampilkan 6 baris yang dilakukan Maya P
22. Verifikasi baris Budi S tidak tampil

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-166, 167, 168, 169, 170). Tidak ada TC hanya-BE di spec ini.
- TC-AC-DC-167 dikerjakan pada Filter Panel yang masih terbuka dari TC-AC-DC-166 (satu pembukaan panel untuk halaman yang dipakai berulang).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah dari TC): langkah 17.
- Temuan untuk QA:
  - Asersi spec ini bergantung pada isi persis Riwayat Changelog Pre-setup #17 (dua belas entri, termasuk angka total 12 dan pembagian halaman), sedangkan S-12 melarang angka total absolut pada audit trail permanen dan Lampiran A belum punya butir untuk modul ini. Spec mengikuti TC dan mengandalkan kemampuan fixture BE yang memulihkan Changelog entitas uji ke #17 sebelum dan sesudah spec. Perlu keputusan pengecualian Lampiran A (setara A-5) atau entitas uji khusus Changelog.
  - TC tidak menyebut apakah `[Apply]` menutup Filter Panel; spec memakai 'Klik ikon Filter' untuk membuka panel pada tiap penerapan berikutnya.
  - TC-AC-DC-170 menulis pilihan pelaku 'Maya'; opsi dropdown tampil sebagai 'Maya P' menurut TC-AC-DC-174.
