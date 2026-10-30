---
id: TC-GS-GSET-E2E-028-changelog-search-interaksi-kolom-dan-kolom-hidden
title: "Modal Changelog: Search, Interaksi Kotak Search, Kolom Searchable, dan Kolom Hidden"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-66
  - TC-GS-GSET-67
  - TC-GS-GSET-68
  - TC-GS-GSET-69
  - TC-GS-GSET-70
coverage:
  web: automated
---

# Modal Changelog: Search, Interaksi Kotak Search, Kolom Searchable, dan Kolom Hidden

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; akun ini adalah akun default suite sehingga hook `after` tidak mengganti sesi. Halaman General Settings dibuka di hook `beforeEach`. Password tidak ditulis di spec atau fixture.
- Akun pelaku seeding lewat sesi API (tidak login UI): Total Control Client A, Andi Wijaya (`Andi W`), `totalControlGlobalSettingsB_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 2), password `Spectra.env.GS_TCB_PASSWORD` (nama env baru; pendaftaran di `spectra.config.ts` dan `.env.example` dilakukan pada tahap script).
- Environment variable: `GS_TC_PASSWORD`, `GS_TCB_PASSWORD`.
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- Seeding minimal (S-11, S-12; hook `before`, sesudah record Client A berada di baseline Pre-setup baris 10), tiga `PUT /v2/enterprise-management/general-settings` (`global-settings/general-settings/API/openapi.yaml`) berurutan, payload mengacu ke `Fixture.generalSettings.payloadIdle60TzUtc`, `Fixture.generalSettings.payloadIdle60TzUtcDateMdy`, dan `Fixture.generalSettings.payloadBaseline` (fixture belum ada; dibuat pada tahap script):
  - `PUT` oleh Budi Santoso dengan `sessionIdleTimeout` 60 dan `timezone` `UTC` (nilai lain baseline): baris Field `Session Idle Timeout` (`30 minutes` menjadi `1 hour`) dan baris Field `Time Zone` (`(UTC+07:00) Bangkok, Hanoi, Jakarta` menjadi `(UTC+00:00) UTC, Reykjavik, Accra`), Modified By `Budi S`.
  - `PUT` oleh Andi Wijaya dengan tambahan `dateFormat` `M/d/yy`: baris Field `Date Format` (`dd/MM/yy` menjadi `M/d/yy`), Modified By `Andi W`.
  - `PUT` oleh Budi Santoso kembali ke baseline: tiga baris balik (Field `Session Idle Timeout`, `Time Zone`, `Date Format`), Modified By `Budi S`.
  - Hasil: baris dengan Field `Session Idle Timeout`, `Time Zone`, dan `Date Format`; Modified By `Budi S` dan `Andi W`; Old Value `30 minutes` dan `1 hour` (dua nilai distinct untuk Search Old Value dan New Value). Enam baris ini adalah baris terbaru sehingga tampil di halaman pertama. Field `Date Format` tidak memuat kata `Time` di kolom mana pun yang dicari (Action, Field, Old Value, New Value, Modified By) sehingga menjadi penanda baris yang tidak cocok dengan kata kunci `Time`.
- Changelog General Settings adalah audit trail permanen; asersi spec memakai pola baris, tidak pernah jumlah entri absolut (S-12). Entri tidak dihapus.
- Kemampuan teknis: mengetik di kotak Search modal; membaca teks sel kolom Date; membuka Setup Column dari header Actions (⋯); membaca dan menghapus preferensi kolom di penyimpanan browser.
- Pemulihan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom Modal Changelog dikembalikan ke default lewat penghapusan preferensi kolom Changelog di browser (mekanisme disediakan tim FE; spec mengubah visibilitas kolom Field di langkah 41 dan memulihkannya di langkah 45); Modal Changelog ditutup; record Client A di baseline (hook suite).
- Flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` dan pemulihan baseline record: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-GSET-66: Interaksi Search box Changelog: reveal, clear, submit, collapse

1. Klik icon Changelog di pojok kanan atas halaman
2. Klik icon Search di toolbar
3. Verifikasi search bar melebar
4. Verifikasi kursor fokus pada input Search
5. Verifikasi placeholder `Search action, field, or value...`
6. Ketik `Time` pada input Search
7. Verifikasi icon `(✕)` muncul
8. Verifikasi tabel belum tersaring (baris Field `Date Format` masih tampil)
9. Tekan `Enter`
10. Verifikasi tabel menampilkan baris yang cocok dengan `Time`: baris Field `Time Zone` dan baris Field `Session Idle Timeout` tampil
11. Klik `(✕)`
12. Verifikasi input Search kosong
13. Verifikasi search bar tetap terbuka
14. Verifikasi tabel tetap menampilkan hasil search terakhir (baris Field `Date Format` tetap tidak tampil)
15. Tekan `Enter` pada input kosong
16. Verifikasi tabel reset menampilkan semua data (baris Field `Date Format` tampil kembali)
17. Klik icon `(←)`
18. Verifikasi search bar menutup menjadi icon Search
19. Verifikasi tabel langsung reset (baris Field `Date Format` tampil)

### TC-GS-GSET-67: Search Changelog per kolom searchable: Action, Field, Modified By

20. Ketik Search `Edit`, tekan Enter
21. Verifikasi Action: `Edit` menemukan semua baris (baris Field `Session Idle Timeout`, `Time Zone`, dan `Date Format` tampil)
22. Ganti isi kotak search dengan `Session Idle`, tekan Enter
23. Verifikasi Field: `Session Idle` menemukan baris Field `Session Idle Timeout`
24. Ganti isi kotak search dengan `Budi`, tekan Enter
25. Verifikasi Modified By: `Budi` menemukan baris Modified By `Budi S`
26. Ganti isi kotak search dengan `edit`, tekan Enter
27. Verifikasi pencarian tanpa membedakan huruf besar kecil: `edit` menemukan baris yang sama dengan `Edit` (baris Field `Session Idle Timeout`, `Time Zone`, dan `Date Format` tampil)
28. Ganti isi kotak search dengan `zzzz`, tekan Enter
29. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.`

### TC-GS-GSET-68: Search Changelog pada kolom Old Value dan New Value

30. Ganti isi kotak search dengan `30 minutes`, tekan Enter
31. Verifikasi `30 minutes` menemukan baris Field `Session Idle Timeout` dengan Old Value `30 minutes`
32. Ganti isi kotak search dengan `1 hour`, tekan Enter
33. Verifikasi `1 hour` menemukan baris Field `Session Idle Timeout` dengan New Value `1 hour`

### TC-GS-GSET-69: Search Changelog tidak mencari kolom Date

34. Baca teks tanggal pada kolom Date baris pertama yang tampil (sesuai tampilan kolom Date)
35. Ganti isi kotak search dengan teks tanggal tersebut, tekan Enter
36. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.`

### TC-GS-GSET-70: Search tidak mencari kolom yang di-hide dan kembali mencari setelah di-unhide

37. Ganti isi kotak search dengan `Session Idle`, tekan Enter
38. Verifikasi baris Field `Session Idle Timeout` ditemukan
39. Klik `(←)` pada kotak Search
40. Buka Setup Column: klik header kolom Actions (⋯), pilih item `Setup Column...`
41. Uncheck kolom Field, klik `[Save]`
42. Ketik Search `Session Idle`, tekan Enter
43. Verifikasi kata kunci tidak mencocokkan baris: empty state `No results found`
44. Klik `(←)` pada kotak Search
45. Buka Setup Column via header kolom Actions (⋯) > `Setup Column...`, check kolom Field, klik `[Save]`
46. Ketik Search `Session Idle`, tekan Enter
47. Verifikasi kata kunci kembali mencocokkan baris Field `Session Idle Timeout`

## Notes

- Mode: FE+BE. Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-66, 67, 68, 69, 70. Alasan: TC-66 menguji kontrol Search dan menjadi screening di awal; TC-67 sampai 69 memakai Search dengan kata kunci berbeda pada tabel yang sama; TC-70 terakhir karena mengubah konfigurasi kolom (menyembunyikan lalu memulihkan kolom Field). Modal Changelog dibuka sekali di langkah 1.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 34 (membaca teks tanggal yang dipakai langkah 35, sekaligus pembanding bahwa tabel berisi baris sebelum empty state di langkah 36), 39 dan 44 (mengosongkan Search lewat `(←)`, menutup input dan mereset tabel), 40 (membuka Setup Column), serta langkah Search atomik "Ketik Search `X`, tekan Enter" yang membuka kembali input yang ditutup `(←)` (langkah 20, 42, 46). TC-70 langkah 2 "Kosongkan Search" ditulis sebagai langkah 39 dan 44.
- Langkah 8, 14, 16, dan 19 memakai baris Field `Date Format` sebagai penanda tabel tersaring atau tidak; Expected TC-66 tidak menyebut penanda ini (S-03, bagian 8b butir 2). Anchor positif langkah 14 adalah langkah 10 (baris yang cocok tampil).
- Langkah 30 dan 32 mengganti isi kotak search sekaligus mengosongkan kata kunci sebelumnya; TC-68 langkah 2 "Kosongkan Search, lalu search `1 hour`" dipenuhi dalam satu langkah ganti isi.
- Spec berisi 47 langkah, di atas sekitar 35 langkah. Alasan pertahanan: semua blok satu kelas harness (Search Modal Changelog), satu akun, dan satu dataset; setiap blok memulai dengan Search sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; Expected TC-66 dan TC-67 memuat banyak klausa yang masing-masing wajib `Verifikasi` sendiri (S-01); TC-70 memakai Setup Column hanya sebagai cara menyembunyikan kolom yang dicari. Blok TC-70 (langkah 37 sampai 47) berdiri sendiri bila perlu dipisah.
- Asersi memakai pola baris, bukan jumlah baris, sehingga entri Changelog dari run atau spec lain tidak memengaruhi hasil.
- Temuan untuk QA:
  - TC-GS-GSET-66 langkah 8 hanya bermakna bila ada baris yang tidak cocok dengan kata kunci; Data Uji tidak menyebutnya, sehingga spec men-seed baris Field `Date Format` sebagai penanda.
  - TC-GS-GSET-66 Expected f ("tabel langsung reset") tidak dapat dibedakan dari keadaan sebelumnya karena tabel sudah di-reset pada langkah 15; spec mengikuti urutan TC.
  - TC-GS-GSET-67 Expected a menyebut "menemukan semua baris" tanpa menyebut baris pembanding; spec memakai tiga Field seeding sebagai penanda.
  - TC-GS-GSET-69 Expected "penyaringan tanggal hanya lewat Filter Panel" adalah pernyataan perilaku tanpa langkah observasi di TC; spec hanya mengasersi empty state, penyaringan Date lewat Filter diuji di spec 030.
  - TC-GS-GSET-69 tidak menyebut cara memperoleh teks tanggal baris pertama (format mengikuti Date Format tersimpan); spec membaca teks sel kolom Date apa adanya.
