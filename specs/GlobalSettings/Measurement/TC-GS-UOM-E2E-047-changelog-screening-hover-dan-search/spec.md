---
id: TC-GS-UOM-E2E-047-changelog-screening-hover-dan-search
title: "Changelog Measurement: Screening, Format Sel, Hover Modified By, Urutan Default, Tooltip, Search, dan Tutup Modal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-171
  - TC-GS-UOM-172
  - TC-GS-UOM-173
  - TC-GS-UOM-176
  - TC-GS-UOM-177
  - TC-GS-UOM-186
  - TC-GS-UOM-337
coverage:
  web: automated
---

# Changelog Measurement: Screening, Format Sel, Hover Modified By, Urutan Default, Tooltip, Search, dan Tutup Modal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` suite (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Layar awal Global Settings > Master Reference > Measurement dibuka di hook `beforeEach` suite.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel true oleh hook suite (lihat bagian "Hook suite" di `suite.md`).
- Fixture: `fixtures/measurement.json` belum ada; tim FE menyiapkannya (lihat `suite.md`, bagian Data bersama).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.
- Seeding (lewat API oleh Sari Dewi di hook `before`, urutan sebagai berikut):
  - Population D-01 (setara TC-GS-UOM-36), idempotent (nama yang sudah ada dilewati): `Centimeter`, `Foot`, `Gallon`, `Inch`, `Milliliter`, `Millimeter`, `Ounce`, `Pound`, `Roll`, `Set`, `Sheet`, `Ton`. Menghasilkan entri Changelog Create oleh `Sari D` (Old Value `—`, Field `Unit Name`); entri Create `Centimeter` dipakai TC-GS-UOM-172 dan jumlah entri lebih dari 10 dipakai TC-GS-UOM-171.
  - Unit milik spec `Gallon {runId}-047` (Symbol `gl`) dibuat, lalu Symbol-nya diubah menjadi `oz.` (entri Create lalu entri Edit, Field `Symbol`, Old Value `gl`, New Value `oz.`). Ini aksi seeding terakhir di `before`, sehingga entri Edit tersebut menjadi entri terbaru di Changelog (dipakai TC-GS-UOM-173 dan 176). Data ini menggantikan prasyarat TC-GS-UOM-71 pada TC-GS-UOM-176 (lihat Temuan untuk QA).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Gallon {runId}-047` dan unit Population yang dibuat spec ini (yang sudah ada sebelum spec dilewati). Entri Changelog tidak bisa dihapus.
- Kemampuan teknis: hover (tooltip); menyalin teks dari sel tabel; membaca teks tanggal pada kolom Date.
- Precondition TC-GS-UOM-171, 172, 173, 176, 177, 186, 337: login sebagai Total Control dan berada di Global Settings > Master Reference > Measurement. TC-GS-UOM-171, 172, 173 bergantung pada Population (TC-GS-UOM-36) yang di-seed di `before`.
- Zona waktu dan format tanggal General Settings: bawaan environment; spec tidak mengubahnya.

## Test Steps

### TC-GS-UOM-171: Screening Modal Changelog: Measurement

1. Klik icon Changelog di halaman Global Settings > Master Reference > Measurement
2. Verifikasi Header: Title `Changelog: Measurement`
3. Verifikasi Header: icon `[✕]`
4. Verifikasi Header: Table Tools `Search`, `Filter`, dan `Download` tampil
5. Verifikasi kolom tabel `Date | Action | Unit Name | Field | Old Value | New Value | Modified By | Actions (⋯)`
6. Verifikasi tabel Changelog tanpa row action
7. Verifikasi Pagination default 10 per halaman

### TC-GS-UOM-337: Hover icon toolbar Modal Changelog dan header kolom Actions menampilkan tooltip

8. Hover icon Search pada toolbar Modal Changelog
9. Verifikasi Tooltip `Search`
10. Hover icon Filter pada toolbar Modal Changelog
11. Verifikasi Tooltip `Filter`
12. Hover icon Download pada toolbar Modal Changelog
13. Verifikasi Tooltip `Download`
14. Hover header kolom Actions (⋯) tabel Changelog
15. Verifikasi Tooltip `Column Visibility`

### TC-GS-UOM-173: Urutan default Changelog adalah Date terbaru di atas

16. Verifikasi tidak ada kolom yang menampilkan panah sort aktif, termasuk Date
17. Verifikasi baris pertama (terbaru di atas) memuat Action `Edit`, Unit Name `Gallon {runId}-047`

### TC-GS-UOM-176: Search Changelog mencocokkan kolom Action, Unit Name, Field, Old Value, New Value, dan Modified By

18. Klik icon Search pada Table Tools Changelog
19. Verifikasi placeholder `Search action, unit name, field, value, or modified by...`
20. Ketik Search `edit`, tekan Enter
21. Verifikasi hasil memuat baris Action `Edit`
22. Verifikasi keyword huruf kecil `edit` menemukan Action berhuruf kapital `Edit` (tanpa membedakan huruf besar kecil)
23. Ganti isi kotak search dengan `gallon`, tekan Enter
24. Verifikasi hasil memuat baris Unit Name `Gallon {runId}-047`
25. Ganti isi kotak search dengan `symbol`, tekan Enter
26. Verifikasi hasil memuat baris Field `Symbol`
27. Ganti isi kotak search dengan `oz`, tekan Enter
28. Verifikasi hasil memuat baris New Value `oz.`
29. Ganti isi kotak search dengan `oz.`, tekan Enter
30. Verifikasi hasil memuat baris New Value `oz.`
31. Ganti isi kotak search dengan `sari`, tekan Enter
32. Verifikasi hasil memuat baris Modified By `Sari D`

### TC-GS-UOM-172: Format isi sel Changelog: strip dan hover Modified By

33. Ganti isi kotak search dengan `centimeter`, tekan Enter
34. Verifikasi hasil memuat baris Action `Create`, Unit Name `Centimeter` oleh `Sari D`
35. Verifikasi Old Value baris Create Centimeter tampil `—`
36. Verifikasi Field baris Create Centimeter `Unit Name`
37. Verifikasi New Value baris Create Centimeter `Centimeter`
38. Verifikasi sel Modified By baris Create Centimeter menampilkan `Sari D` (nama depan lengkap dan inisial nama belakang)
39. Hover sel Modified By baris Create Centimeter
40. Verifikasi Tooltip `Sari Dewi`

### TC-GS-UOM-177: Kolom Date tidak dapat dicari

41. Klik `(←)` pada kotak Search
42. Verifikasi sedikitnya satu baris tampil di tabel Changelog
43. Salin bagian tanggal (tanpa jam) dari kolom Date baris pertama, sesuai format yang tampil di kolom itu
44. Ketik Search teks tanggal yang disalin, tekan Enter
45. Verifikasi pesan `No results found`

### TC-GS-UOM-186: Modal Changelog ditutup lewat icon close dan Esc

46. Verifikasi tidak ada tombol teks `Close` pada Modal Changelog
47. Klik `[✕]`
48. Verifikasi Modal Changelog tertutup
49. Klik icon Changelog
50. Tekan Esc
51. Verifikasi Modal Changelog tertutup

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Modal Changelog dibuka sekali di langkah 1 dan dipakai berurutan untuk TC-GS-UOM-171, 337, 173, 176, 172, 177 (precondition sama: Total Control di halaman Measurement; langkah "Buka Modal Changelog" tiap TC sudah terpenuhi oleh langkah 1). TC-GS-UOM-186 menutup modal dan dijalankan terakhir (prinsip 6 konvensi 3).
- Urutan TC berbeda dari nomor sumber: TC-GS-UOM-173 (urutan default) sebelum penggunaan Search supaya diamati pada state awal (S-14); TC-GS-UOM-172 sesudah TC-GS-UOM-176 supaya baris Create Centimeter ditemukan lewat kotak Search yang sudah terbuka, bukan lewat paginasi; TC-GS-UOM-337 sesudah TC-GS-UOM-171 karena hanya mengamati toolbar.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 33 dan 44 (Search `centimeter` untuk menemukan baris target TC-GS-UOM-172; mengetik teks tanggal yang disalin pada langkah 43 untuk TC-GS-UOM-177), langkah 41 (mengosongkan Search sebelum TC-GS-UOM-177), dan langkah 43 (menyalin tanggal).
- Langkah 42 adalah `Verifikasi` pembanding (butir 2 bagian 8b), bukan dari Expected TC: Changelog terbukti memuat baris sebelum Search teks tanggal pada langkah 44.
- Langkah 22 dan 46 berasal dari klausa Expected TC (tanpa membedakan huruf besar kecil; tidak ada tombol teks `Close`). Langkah 46 memakai Title yang sudah terverifikasi di langkah 2 sebagai anchor permukaan.
- Langkah 17 bergantung pada entri Edit `Gallon {runId}-047` sebagai aksi seeding terakhir di `before`; suite serial sehingga tidak ada entri lain yang lebih baru. Spec lain tidak dijalankan bersamaan.
- Spec ini melewati sekitar 35 langkah (51 langkah). Alasan: seluruh TC adalah baca-saja pada satu Modal Changelog dengan satu seeding, satu kelas harness (fungsional). Gagalnya membuka modal di langkah 1 membuat seluruh blok kehilangan makna, sehingga memecah spec hanya menambah login, seeding, dan pembukaan modal berulang tanpa mengurangi risiko.
- Temuan untuk QA:
  - TC-GS-UOM-176 bergantung pada TC-GS-UOM-71 (Edit) yang tidak menyebut data persis; spec men-seed Edit Symbol `gl` menjadi `oz.` pada unit `Gallon {runId}-047` dari kata kunci TC (`edit`, `gallon`, `symbol`, `oz`, `oz.`). Mohon konfirmasi data yang dimaksud.
  - TC-GS-UOM-176 menulis keyword "nama aktor" tanpa nilai; spec memakai `sari` dan mengasersi Modified By `Sari D` (sel menampilkan nama depan dan inisial belakang, bukan nama lengkap).
  - TC-GS-UOM-177 menulis "tanggal hari ini" tanpa format; spec memakai teks tanggal persis seperti tampil di kolom Date baris pertama (format mengikuti General Settings).
  - TC-GS-UOM-173: kolom Date berketelitian menit; urutan dua entri dalam menit yang sama bergantung urutan penyimpanan server. Spec mengasersi baris pertama sebagai entri seeding terakhir.
