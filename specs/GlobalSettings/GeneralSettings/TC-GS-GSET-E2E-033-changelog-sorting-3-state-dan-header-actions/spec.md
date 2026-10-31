---
id: TC-GS-GSET-E2E-033-changelog-sorting-3-state-dan-header-actions
title: "Modal Changelog: Sorting 3-State Kolom Date dan Kolom Teks serta Header Actions Tanpa Ikon Sort"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-82
  - TC-GS-GSET-83
  - TC-GS-GSET-160
coverage:
  web: automated
---

# Modal Changelog: Sorting 3-State Kolom Date dan Kolom Teks serta Header Actions Tanpa Ikon Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; akun ini adalah akun default suite sehingga hook `after` tidak mengganti sesi. Halaman General Settings dibuka di hook `beforeEach`. Password tidak ditulis di spec atau fixture.
- Akun pelaku seeding lewat sesi API (tidak login UI): Total Control Client A, Andi Wijaya (`Andi W`), `totalControlGlobalSettingsB_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 2), password `Spectra.env.GS_TCB_PASSWORD` (nama env baru; pendaftaran di `spectra.config.ts` dan `.env.example` dilakukan pada tahap script).
- Environment variable: `GS_TC_PASSWORD`, `GS_TCB_PASSWORD`.
- Seeding minimal (S-11, S-12; hook `before`, sesudah record Client A berada di baseline Pre-setup baris 10), tiga `PUT /v2/enterprise-management/general-settings` (`global-settings/general-settings/API/openapi.yaml`) berurutan, payload mengacu ke `Fixture.generalSettings.payloadIdle60TzUtc`, `Fixture.generalSettings.payloadIdle120DateMdy`, dan `Fixture.generalSettings.payloadBaseline` (fixture belum ada; dibuat pada tahap script):
  - `PUT` oleh Budi Santoso dengan `sessionIdleTimeout` 60 dan `timezone` `UTC` (nilai lain baseline): baris Field `Session Idle Timeout` (`30 minutes` menjadi `1 hour`) dan baris Field `Time Zone` (`(UTC+07:00) Bangkok, Hanoi, Jakarta` menjadi `(UTC+00:00) UTC, Reykjavik, Accra`), Modified By `Budi S`.
  - Hook menunggu sampai menit berganti (jeda maksimum 60 detik; konvensi bagian 6 untuk Date berketelitian menit, bukan langkah `Tunggu N detik` di spec), sehingga Date baris pertama dan baris berikutnya berbeda pada menit.
  - `PUT` oleh Andi Wijaya dengan `sessionIdleTimeout` 120 dan `dateFormat` `M/d/yy`: baris Field `Session Idle Timeout` (`1 hour` menjadi `2 hours`) dan baris Field `Date Format` (`dd/MM/yy` menjadi `M/d/yy`), Modified By `Andi W`.
  - `PUT` oleh Budi Santoso kembali ke baseline: tiga baris balik (Field `Session Idle Timeout`, `Time Zone`, `Date Format`), Modified By `Budi S`.
  - Hasil: tujuh baris terbaru dengan sedikitnya dua nilai distinct pada tiap kolom yang diurutkan (S-11): Field (`Session Idle Timeout`, `Time Zone`, `Date Format`), Old Value dan New Value (mis. `30 minutes`, `1 hour`, `2 hours`, `dd/MM/yy`, `M/d/yy`, dan label Time Zone), Modified By (`Budi S` dan `Andi W`), Date (sedikitnya dua menit berbeda). Kolom Action seragam `Edit`, sehingga hanya indikator sort Action yang diperiksa (Expected TC-82 a).
- Kolom teks yang diurutkan (parameter perulangan langkah 20 sampai 25):

  | Kolom | Catatan urutan Ascending dan Descending |
  |---|---|
  | Field | A-Z case-insensitive, lalu Z-A |
  | Old Value | A-Z, lalu Z-A |
  | New Value | A-Z, lalu Z-A |
  | Modified By | A-Z, lalu Z-A |

- Changelog General Settings adalah audit trail permanen; asersi spec membandingkan urutan dan nilai antar baris, tidak pernah jumlah entri absolut (S-12). Entri tidak dihapus.
- Kemampuan teknis: membaca nilai tiap kolom baris pertama dan Date baris tabel; membaca indikator sort pada header kolom.
- Pemulihan di hook `after` (tetap jalan walau spec gagal di tengah): Modal Changelog ditutup (sort adalah state tampilan modal); record Client A di baseline (hook suite).
- Flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` dan pemulihan baseline record: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-GSET-160: Header kolom Actions (⋯) tidak memiliki ikon sort dan membuka Panel Column Visibility

1. Klik icon Changelog di pojok kanan atas halaman
2. Catat dua baris teratas tabel (Field, Old Value, New Value, Modified By, dan Date) sebagai acuan urutan default
3. Verifikasi header kolom Actions (⋯) tidak menampilkan ikon sort
4. Klik header kolom Actions (⋯)
5. Verifikasi klik membuka Panel Column Visibility
6. Verifikasi urutan baris tidak berubah (dua baris teratas sama dengan langkah 2)
7. Klik header kolom Actions (⋯) lagi untuk menutup Panel Column Visibility

### TC-GS-GSET-83: Sorting kolom Date: Oldest First dan Newest First

8. Klik header Date
9. Verifikasi klik 1 Oldest First: baris terurut Date naik (Date baris pertama tidak lebih baru daripada Date baris terakhir halaman); catat Date baris pertama sebagai D1
10. Klik header Date
11. Verifikasi klik 2 Newest First: baris terurut Date turun dan Date baris pertama lebih baru daripada D1
12. Klik header Date
13. Verifikasi klik 3 kembali ke default Date descending (dua baris teratas sama dengan langkah 2)

### TC-GS-GSET-82: Sorting 3-state kolom teks: Action, Field, Old Value, New Value, Modified By

14. Klik header Action
15. Verifikasi klik 1 indikator sort Action Ascending
16. Klik header Action
17. Verifikasi klik 2 indikator sort Action Descending
18. Klik header Action
19. Verifikasi klik 3 indikator sort Action kembali netral dan urutan kembali default Date descending (dua baris teratas sama dengan langkah 2)

Untuk setiap baris tabel "Kolom teks yang diurutkan" pada Prerequisites (Field, Old Value, New Value, Modified By), lakukan langkah 20 sampai 25:

20. Klik header kolom tersebut
21. Verifikasi klik 1 Ascending: baris terurut A-Z menurut kolom tersebut; catat nilai kolom pada baris pertama sebagai A1
22. Klik header kolom tersebut
23. Verifikasi klik 2 Descending: baris terurut Z-A menurut kolom tersebut dan nilai kolom pada baris pertama berbeda dari A1
24. Klik header kolom tersebut
25. Verifikasi klik 3 kembali ke default Date descending (dua baris teratas sama dengan langkah 2)

## Notes

- Mode: FE+BE. Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-160, 83, 82. Alasan: TC-160 hanya mengamati header dan tidak mengubah sort (screening di awal); TC-83 lalu TC-82 mengembalikan sort ke default pada klik ketiga sehingga blok berikutnya mulai dari urutan default. Modal Changelog dibuka sekali di langkah 1.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2 (mencatat acuan urutan default untuk asersi "kembali ke default"), 7 (menutup Panel Column Visibility agar sort berikutnya tidak terhalang overlay), dan pencatatan D1 dan A1 pada `Verifikasi` langkah 9 dan 21 sebagai pembanding untuk langkah 11 dan 23 (S-11: dua nilai distinct).
- Langkah 20 sampai 25 diulang untuk empat kolom (idiom "Untuk setiap baris tabel", bagian 8b butir 7); tiap iterasi mengulang tiga `Verifikasi` (satu per klik, S-01).
- Spec berisi 25 langkah nominal dan 43 langkah dengan ekspansi, di atas sekitar 35 langkah. Alasan pertahanan: semua blok satu kelas harness (sort Modal Changelog), satu akun, dan satu dataset; tiap kolom mengembalikan sort ke default pada klik ketiga sehingga blok berikutnya berdiri sendiri; langkah berulang per kolom memakai tabel Prerequisites.
- Temuan untuk QA:
  - TC-GS-GSET-82 langkah 1 meminta mengamati "indikator sort serta urutan baris setelah tiap klik", sedangkan Expected b sampai e hanya menyebut urutan (indikator hanya pada Expected a untuk Action); spec mengasersi indikator untuk Action dan urutan baris untuk kolom lain sesuai Expected.
  - TC-GS-GSET-82 tidak menyebut urutan nilai yang berawalan angka atau tanda kurung (mis. Old Value `(UTC+07:00) ...` dan `1 hour`) pada A-Z; spec mengasersi urutan A-Z menurut perilaku aplikasi dan membandingkan baris pertama klik 1 dengan klik 2 agar tetap bermakna.
  - TC-GS-GSET-83 klik 2 (Newest First) dan klik 3 (default Date descending) menghasilkan urutan baris yang sama; perbedaan keduanya hanya pada indikator sort, yang tidak disebut Expected.
  - TC-GS-GSET-83 dan TC-GS-GSET-82 tidak menyebut cara membuktikan "Oldest First" bila sepuluh baris pertama bertanggal menit sama; spec membandingkan Date baris pertama antar-klik (langkah 9 dan 11) selain urutan pada halaman.
