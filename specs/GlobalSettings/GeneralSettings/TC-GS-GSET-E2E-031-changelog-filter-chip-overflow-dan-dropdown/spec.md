---
id: TC-GS-GSET-E2E-031-changelog-filter-chip-overflow-dan-dropdown
title: "Modal Changelog: Chip Filter, Overflow +N more, Pencarian Dropdown, dan Indikator Loading Dropdown"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-79
  - TC-GS-GSET-175
  - TC-GS-GSET-176
  - TC-GS-GSET-80
  - TC-GS-GSET-177
coverage:
  web: automated
---

# Modal Changelog: Chip Filter, Overflow +N more, Pencarian Dropdown, dan Indikator Loading Dropdown

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; akun ini adalah akun default suite sehingga hook `after` tidak mengganti sesi. Halaman General Settings dibuka di hook `beforeEach`. Password tidak ditulis di spec atau fixture.
- Akun pelaku seeding lewat sesi API (tidak login UI): Total Control Client A, Andi Wijaya (`Andi W`), `totalControlGlobalSettingsB_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 2), password `Spectra.env.GS_TCB_PASSWORD` (nama env baru; pendaftaran di `spectra.config.ts` dan `.env.example` dilakukan pada tahap script).
- Environment variable: `GS_TC_PASSWORD`, `GS_TCB_PASSWORD`.
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- Seeding minimal (S-11, S-12; hook `before`, sesudah record Client A berada di baseline Pre-setup baris 10), tiga `PUT /v2/enterprise-management/general-settings` (`global-settings/general-settings/API/openapi.yaml`) berurutan, payload mengacu ke `Fixture.generalSettings.payloadAllFieldsChanged`, `Fixture.generalSettings.payloadTzJakarta`, dan `Fixture.generalSettings.payloadBaseline` (fixture belum ada; dibuat pada tahap script):
  - `PUT` oleh Budi Santoso yang mengubah kelima field dari baseline: `currencyCode` `USD`, `timezone` `UTC`, `dateFormat` `M/d/yy`, `timeFormat` `hh:mm a`, `sessionIdleTimeout` 60. Hasil: satu baris tiap Field `Currency Code`, `Time Zone`, `Date Format`, `Time Format`, `Session Idle Timeout`, Modified By `Budi S`.
  - `PUT` oleh Andi Wijaya dengan `timezone` `Asia/Jakarta` (nilai lain sama): baris Field `Time Zone`, Modified By `Andi W`.
  - `PUT` oleh Budi Santoso kembali ke baseline: baris balik Field `Currency Code`, `Date Format`, `Time Format`, `Session Idle Timeout` (Time Zone sudah `Asia/Jakarta`), Modified By `Budi S`.
  - Hasil: kelima nilai Field memiliki baris (precondition TC-GS-GSET-176 d); Field `Time Zone` memiliki baris Modified By `Budi S` dan `Andi W`; Modified By memiliki dua nilai distinct. Sepuluh baris ini adalah baris terbaru. Label opsi Currency `USD` tidak diasersi (label ditentukan programmer, NC-10).
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit (TC-GS-GSET-177): respons opsi filter `POST /v2/analytics-reporting/change-logs/options` (`global-settings/activity-log/API/openapi.yaml`; path dikonfirmasi tim FE karena `openapi.yaml` dan `low-level-design.md` General Settings tidak mencantumkan endpoint Changelog): tahan 5 detik lalu jawab normal, dipasang di langkah 1 dan 9 dan dilepas di langkah 6 dan 12. Durasi tahan adalah data uji, bukan aturan PRD (PRD §9.5 sumber opsi filter dropdown).
- Kemampuan teknis: viewport desktop lebar 1280 px (precondition TC-GS-GSET-176 e) diatur di hook `before` spec ini dan dipulihkan di hook `after`; mengukur lebar field Field terhadap panel dan memeriksa ada tidaknya scroll horizontal; membaca label chip.
- Changelog General Settings adalah audit trail permanen; asersi spec memakai pola baris, tidak pernah jumlah entri absolut (S-12). Entri tidak dihapus.
- Pemulihan di hook `after` (tetap jalan walau spec gagal di tengah): semua intercept dilepas; viewport dipulihkan; Modal Changelog ditutup; record Client A di baseline (hook suite).
- Flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` dan pemulihan baseline record: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-GSET-177: Dropdown filter menampilkan indikator loading saat opsi diambil

1. Pasang intercept pada respons opsi filter Changelog (`POST /v2/analytics-reporting/change-logs/options`): tahan 5 detik lalu jawab normal
2. Klik icon Changelog di pojok kanan atas halaman
3. Klik Filter di toolbar
4. Buka dropdown Field
5. Verifikasi skeleton atau spinner mini tampil selama opsi diambil (bukan dropdown kosong tanpa indikator)
6. Tunggu respons diterima, lalu lepas intercept respons opsi filter
7. Verifikasi opsi Field tampil (`Session Idle Timeout` dan `Time Zone`)
8. Tutup dropdown Field
9. Pasang kembali intercept pada respons opsi filter Changelog: tahan 5 detik lalu jawab normal
10. Buka dropdown Modified By
11. Verifikasi skeleton atau spinner mini tampil selama opsi diambil pada dropdown Modified By
12. Tunggu respons diterima, lalu lepas intercept respons opsi filter dan tutup dropdown Modified By

### TC-GS-GSET-79: Menghapus chip filter via (X) pada chip

13. Pilih Field `Session Idle Timeout` dan `Time Zone`
14. Klik `(X)` pada chip `Time Zone`
15. Verifikasi chip `Time Zone` hilang
16. Verifikasi chip `Session Idle Timeout` tetap
17. Buka dropdown Field
18. Verifikasi checkbox `Time Zone` ter-uncheck

### TC-GS-GSET-80: Search internal dropdown filter Field

19. Ketik `Time` di kotak pencarian dropdown Field
20. Verifikasi opsi menyempit ke `Time Zone` dan `Time Format`
21. Ganti isi kotak pencarian dropdown dengan `zzzz`
22. Verifikasi tidak ada opsi yang cocok
23. Kosongkan kotak pencarian dropdown, lalu tutup dropdown Field

### TC-GS-GSET-175: Menghapus chip filter via uncheck di dalam dropdown (Field dan Modified By) dan sinkron ke hasil Apply

24. Klik `[Clear Field]`
25. Pilih Field `Session Idle Timeout` dan `Time Zone`
26. Buka dropdown Field dan uncheck `Session Idle Timeout`
27. Verifikasi chip `Session Idle Timeout` hilang
28. Verifikasi chip `Time Zone` tetap
29. Klik `[Apply]`
30. Verifikasi tabel menampilkan baris Field `Time Zone`
31. Verifikasi tabel hanya memuat baris Field `Time Zone` (baris Field `Session Idle Timeout` tidak tampil)
32. Klik Filter, lalu pilih Modified By `Budi S` dan `Andi W`
33. Buka dropdown Modified By dan uncheck `Andi W`
34. Verifikasi chip `Andi W` hilang
35. Verifikasi chip `Budi S` tetap
36. Klik `[Apply]`
37. Verifikasi tabel menampilkan baris Field `Time Zone` dengan Modified By `Budi S`
38. Verifikasi baris Field `Time Zone` dengan Modified By `Andi W` tidak tampil

### TC-GS-GSET-176: Overflow chip pada field filter: chip berlebih diringkas menjadi "+N more"

39. Klik Filter, lalu klik `[Clear Field]`
40. Pilih kelima opsi Field: `Currency Code`, `Time Zone`, `Date Format`, `Time Format`, `Session Idle Timeout`
41. Verifikasi chip ditampilkan sebanyak yang muat pada lebar field dan sisanya diringkas dalam satu chip `+N more` (jumlah chip tampil ditambah N sama dengan 5)
42. Verifikasi field Field tidak melebar keluar panel
43. Verifikasi field Field tidak digulir horizontal

## Notes

- Mode: FE+BE. Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-177, 79, 80, 175, 176. Alasan: TC-177 memerlukan pembukaan Filter Panel pertama kali sehingga opsi diambil dari server (sebelum opsi tersimpan di klien) dan tidak mengubah state; TC-79 dan 80 bekerja pada pilihan sementara tanpa Apply; TC-175 memakai `[Apply]`; TC-176 terakhir karena memerlukan kelima opsi terpilih. Modal Changelog dan Filter Panel dibuka sekali (langkah 2 dan 3).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6 dan 12 (menunggu respons dan melepas intercept segera setelah pemicu, S-09), 8, 23 (menutup dropdown), 24 (`[Clear Field]` sebagai pembersih state antar blok, S-09), 32 (membuka Filter sebelum memilih Modified By), dan 39 (membuka Filter dan membersihkan pilihan blok sebelumnya). Langkah 13 pada TC-79 memilih dua opsi tanpa `[Apply]`, sesuai TC.
- Langkah 30 dan 37 `Verifikasi` baris yang seharusnya tampil adalah pembanding positif sebelum asersi absence pada langkah 31 dan 38 (bagian 8b butir 2); Expected TC-175 b dan d menyebut "hanya" tanpa pembanding.
- Spec berisi 43 langkah, di atas sekitar 35 langkah. Alasan pertahanan: semua blok satu kelas harness (filter Modal Changelog: chip, dropdown, overflow), satu akun, dan satu dataset; tiap blok memulai dari keadaan pilihan yang dibersihkan (`[Clear Field]` atau pilihan sendiri) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; TC-175 memuat delapan klausa Expected yang masing-masing wajib `Verifikasi` sendiri (S-01). Blok TC-176 (langkah 39 sampai 43) berdiri sendiri bila perlu dipisah.
- Temuan untuk QA:
  - TC-GS-GSET-80 Expected a menyebut pencarian `Time` menyempit ke `Time Zone` dan `Time Format`, padahal `Session Idle Timeout` juga memuat substring `Time` (TC-GS-GSET-156 menunjukkan Search tabel mencocokkan substring). Bila pencarian dropdown berbasis substring, opsi `Session Idle Timeout` ikut tampil dan Expected tidak terpenuhi; spec mengikuti TC dan hasilnya perlu dikonfirmasi (apakah pencarian dropdown berbasis awal kata).
  - TC-GS-GSET-177: TC tidak menyebut apakah opsi di-fetch ulang tiap dropdown dibuka; langkah "tahan lagi respons" untuk dropdown Modified By (langkah 9 dan 10) mengandaikan opsi Modified By diambil saat dropdown dibuka, bukan sekali saat Filter Panel dibuka.
  - Endpoint opsi Changelog General Settings tidak tertulis di `openapi.yaml` atau `low-level-design.md` General Settings; path di Prerequisites mengikuti kontrak Activity Log dan perlu dikonfirmasi.
  - TC-GS-GSET-176 Expected a tidak menyebut nilai N yang diharapkan pada lebar 1280 px; spec mengasersi jumlah chip tampil ditambah N sama dengan 5 sesuai TC.
  - Label opsi Currency `USD` dan Time Zone selain dua opsi PRD §4.3a ditentukan programmer (NC-09, NC-10); spec ini hanya memakai nilai Field (`Currency Code`, dan seterusnya) dan tidak mengasersi label Old Value atau New Value untuk baris Currency Code.
