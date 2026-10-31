---
id: TC-GS-GSET-E2E-032-changelog-filter-clear-field-tutup-tanpa-apply-dan-kolom-hidden
title: "Modal Changelog: Clear Field Tidak Melepas Search, Tutup Filter Tanpa Apply, dan Filter Independen dari Kolom Hidden"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-81
  - TC-GS-GSET-158
  - TC-GS-GSET-179
coverage:
  web: automated
---

# Modal Changelog: Clear Field Tidak Melepas Search, Tutup Filter Tanpa Apply, dan Filter Independen dari Kolom Hidden

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; akun ini adalah akun default suite sehingga hook `after` tidak mengganti sesi. Halaman General Settings dibuka di hook `beforeEach`. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- Seeding minimal (S-11, S-12; hook `before`, sesudah record Client A berada di baseline Pre-setup baris 10), dua `PUT /v2/enterprise-management/general-settings` (`global-settings/general-settings/API/openapi.yaml`) lewat sesi API akun Budi Santoso, payload mengacu ke `Fixture.generalSettings.payloadIdle60TzUtc` dan `Fixture.generalSettings.payloadBaseline` (fixture belum ada; dibuat pada tahap script):
  - `PUT` dengan `sessionIdleTimeout` 60 dan `timezone` `UTC` (nilai lain baseline): baris Field `Session Idle Timeout` (`30 minutes` menjadi `1 hour`) dan baris Field `Time Zone` (`(UTC+07:00) Bangkok, Hanoi, Jakarta` menjadi `(UTC+00:00) UTC, Reykjavik, Accra`), Modified By `Budi S`.
  - `PUT` kembali ke baseline: baris balik Field `Session Idle Timeout` (`1 hour` menjadi `30 minutes`) dan Field `Time Zone` (label UTC menjadi label Jakarta).
  - Hasil: dua nilai Field distinct (`Session Idle Timeout` dan `Time Zone`) pada empat baris terbaru di halaman pertama; kolom Action seragam `Edit` (kata kunci Search `Edit` pada langkah 2).
- Changelog General Settings adalah audit trail permanen; asersi spec memakai pola baris, tidak pernah jumlah entri absolut (S-12). Entri tidak dihapus.
- Kemampuan teknis: mengklik area di luar Filter Panel; membuka Setup Column dari header Actions (⋯); membaca dan menghapus preferensi kolom di penyimpanan browser.
- Pemulihan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom Modal Changelog dikembalikan ke default lewat penghapusan preferensi kolom Changelog di browser (mekanisme disediakan tim FE; spec menyembunyikan kolom Field di langkah 18 dan memulihkannya di langkah 23); Modal Changelog ditutup; record Client A di baseline (hook suite).
- Flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` dan pemulihan baseline record: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-GSET-81: Clear Field melepas Filter Panel tanpa melepas Search

1. Klik icon Changelog di pojok kanan atas halaman
2. Ketik Search `Edit`, tekan Enter
3. Klik Filter, pilih Field `Session Idle Timeout`, klik `[Apply]`
4. Verifikasi tabel menampilkan baris Field `Session Idle Timeout`
5. Verifikasi baris Field `Time Zone` tidak tampil
6. Klik Filter, klik `[Clear Field]`, klik `[Apply]`
7. Verifikasi kriteria Field dilepas: baris Field `Time Zone` tampil kembali
8. Verifikasi keyword Search tetap aktif: kotak Search masih berisi `Edit`

### TC-GS-GSET-158: Menutup Filter Panel tanpa Apply membuang perubahan yang belum di-Apply

9. Klik Filter, lalu pilih Field `Time Zone` (belum `[Apply]`)
10. Klik area di luar Filter Panel
11. Verifikasi Filter Panel menutup
12. Verifikasi tabel tidak berubah: baris Field `Session Idle Timeout` dan baris Field `Time Zone` tetap tampil
13. Klik Filter lagi
14. Verifikasi field Field kosong dengan placeholder `All fields`

### TC-GS-GSET-179: Filter Changelog independen dari visibilitas kolom (kolom di-hide)

15. Pilih Field `Session Idle Timeout`, klik `[Apply]`
16. Verifikasi tabel menampilkan baris Field `Session Idle Timeout`
17. Verifikasi baris Field `Time Zone` tidak tampil
18. Buka Setup Column via header kolom Actions (⋯) > `Setup Column...`, uncheck kolom Field, klik `[Save]`
19. Verifikasi tabel tetap memuat baris Field `Session Idle Timeout` (dikenali lewat Old Value `30 minutes` dan New Value `1 hour`; filter ter-Apply tetap berlaku)
20. Verifikasi baris Field `Time Zone` tidak tampil (dikenali lewat Old Value atau New Value `(UTC+00:00) UTC, Reykjavik, Accra` dan `(UTC+07:00) Bangkok, Hanoi, Jakarta`)
21. Klik Filter
22. Verifikasi Filter Panel tetap memuat field Field dengan chip `Session Idle Timeout`
23. Tutup Filter Panel, lalu buka Setup Column via header kolom Actions (⋯) > `Setup Column...`, check kolom Field, klik `[Save]`
24. Verifikasi kolom Field tampil kembali
25. Verifikasi filter tetap aktif: baris Field `Session Idle Timeout` tampil dan baris Field `Time Zone` tidak tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-81, 158, 179. Alasan: TC-81 memakai Search aktif; TC-158 mengamati penutupan panel tanpa mengubah tabel (state filter kosong dari TC-81); TC-179 mengubah konfigurasi kolom sehingga paling akhir. Modal Changelog dibuka sekali di langkah 1; Search `Edit` tetap aktif sampai akhir spec.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 10 (menutup panel adalah aksi TC-158 langkah 2), 13, 21 (membuka Filter), dan 23 (menutup Filter Panel sebelum membuka Setup Column).
- Langkah 4, 5, 16, dan 17 `Verifikasi` baris yang tampil lalu absence baris `Time Zone` adalah pembanding sebelum langkah 7, 12, 19 sampai 20, dan 25 (bagian 8b butir 2, S-03); Expected TC-81 dan TC-179 tidak memuatnya, sedangkan langkah 4 dan 5 menjadi bukti bahwa filter Field sempat berlaku sebelum `[Clear Field]`.
- Pada langkah 19 dan 20 kolom Field tersembunyi sehingga baris dikenali lewat Old Value dan New Value hasil seeding.
- Asersi memakai pola baris (bukan jumlah baris), sehingga entri Changelog dari run atau spec lain tidak memengaruhi hasil.
- Temuan untuk QA:
  - TC-GS-GSET-81: seluruh baris Changelog General Settings bernilai Action `Edit` (PRD §4.1.1 Action), sehingga keyword Search `Edit` tidak menyaring baris apa pun; klausa "keyword Search `Edit` tetap menyaring tabel" hanya teramati lewat isi kotak Search (langkah 8). TC tidak menyebut keyword yang menyaring sebagian baris.
  - TC-GS-GSET-179 Expected b menyebut "Filter Panel tetap memuat field Field dengan chip" tanpa menyebut apakah panel harus dibuka kembali; spec membuka Filter di langkah 21.
