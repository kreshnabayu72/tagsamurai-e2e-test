---
id: TC-GS-UOM-E2E-027-edit-sukses-no-op-saving-state-dan-double-click
title: "Edit Sukses, No-Op, Case-Only, Saving State, dan Klik Ganda Save"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-70
  - TC-GS-UOM-71
  - TC-GS-UOM-72
  - TC-GS-UOM-73
  - TC-GS-UOM-74
  - TC-GS-UOM-75
  - TC-GS-UOM-79
  - TC-GS-UOM-83
  - TC-GS-UOM-88
  - TC-GS-UOM-264
coverage:
  web: automated
---

# Edit Sukses, No-Op, Case-Only, Saving State, dan Klik Ganda Save

## Prerequisites

- Mode: FE+BE, dengan intercept parsial di atas backend nyata (TC-GS-UOM-88).
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor di hook `before` spec ini (seedSession). Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: mengikuti pernyataan hook suite di `suite.md` (bagian Hook suite).
- Data pre-setup Client A (data baca): `Kilogram` / `kg` (TC-GS-UOM-264 hanya membaca Symbol `kg` sebagai pembanding; tidak diubah). Fixture belum ada; tim FE menyiapkan `fixtures/measurement.json` dengan kunci `preSetupClientA`.
- Data dinamis (seeding lewat API di hook `before`, semuanya bebas relasi; tidak menumpang spec lain; menggantikan unit Population dan Pre-setup pada TC sumber agar baris bersama tidak termutasi, S-06). Semua nama memuat akhiran ` {runId}-027` sehingga satu Search `{runId}-027` menampilkan kesepuluh unit dalam satu halaman:

  | Kode | Unit awal (Unit Name / Symbol) | TC | Aksi Edit |
  |---|---|---|---|
  | A | `Noop {runId}-027` / `n27` | 73 | Save tanpa perubahan |
  | B | `Case {runId}-027` / `cs27` | 74 | Unit Name `CASE {runId}-027`, Symbol `CS27` |
  | C | `Hecta {runId}-027` / `h27` | 88 | Unit Name `Hectares {runId}-027` (respons ditahan 2 detik) |
  | D | `Gal {runId}-027` / `gal` | 70 | Unit Name `US Gal {runId}-027` |
  | E | `Oz {runId}-027` / `oz` | 71 | Symbol `oz.` |
  | F | `Lb {runId}-027` / `lb` | 72 | Unit Name `Lb Mass {runId}-027`, Symbol `lbm` |
  | G | `Set {runId}-027` / `set` | 75 | Unit Name `SET {runId}-027`, Symbol `st` |
  | H | `Trim {runId}-027` / `ha` | 83 | Symbol `  hm2 ` (spasi depan dan belakang) |
  | I | `Long {runId}-027` / `lg27` | 79 | Unit Name string 120 karakter huruf `b` berulang, dibangun helper sehingga panjang total termasuk akhiran ` {runId}-027` tepat 120 karakter (S-12) |
  | J | `Foot {runId}-027` / `ft` | 264 | Symbol `kg` |

- Cleanup di hook `after` (tidak berasumsi seeding atau rename berhasil penuh): hapus lewat API semua unit yang namanya memuat ` {runId}-027` (nama awal maupun nama hasil Edit, termasuk nama 120 karakter).
- Kemampuan teknis: `Spectra.intercept()` untuk menahan respons request Edit Measurement (`PATCH /v2/enterprise-management/measurements/{measurement_id}`) selama 2 detik (TC-GS-UOM-88) lalu melepasnya; klik ganda cepat pada `[Save]`; pembacaan state hover tombol; pembacaan Last Updated baris.
- State global: tidak ada yang diubah. Jam server dan jam browser sinkron (asersi Last Updated sesuai waktu Save, toleransi satu menit, S-12).

## Test Steps

### Persiapan

1. Ketik Search `{runId}-027`, tekan Enter
2. Verifikasi sedikitnya satu baris tampil di tabel

### TC-GS-UOM-73: Save Edit tanpa perubahan nilai menampilkan toast netral

3. Catat Last Updated baris `Noop {runId}-027`
4. Klik `⋯` baris `Noop {runId}-027` > Edit
5. Klik [Save] tanpa mengubah apa pun
6. Verifikasi toast `No changes to save.`
7. Tutup toast
8. Verifikasi modal tertutup
9. Verifikasi Last Updated baris `Noop {runId}-027` tidak berubah

### TC-GS-UOM-74: Edit yang hanya mengubah huruf besar kecil adalah No-Op

10. Catat Last Updated baris `Case {runId}-027`
11. Klik `⋯` baris `Case {runId}-027` > Edit
12. Ubah Unit Name menjadi `CASE {runId}-027` dan Symbol menjadi `CS27`
13. Klik [Save]
14. Verifikasi toast `No changes to save.`
15. Tutup toast
16. Verifikasi baris tetap menampilkan `Case {runId}-027` / `cs27`
17. Verifikasi Last Updated baris `Case {runId}-027` tidak berubah

### TC-GS-UOM-88: Tombol Save disabled saat proses dan klik ganda menyimpan satu kali

18. Pasang intercept yang menahan respons Edit Measurement selama 2 detik
19. Klik `⋯` baris `Hecta {runId}-027` > Edit
20. Ubah Unit Name menjadi `Hectares {runId}-027`
21. Arahkan kursor ke [Save] tanpa mengklik
22. Verifikasi [Save] menampilkan state hover yang berbeda dari state default
23. Klik [Save] dua kali cepat
24. Verifikasi [Save] masuk Saving state (spinner)
25. Verifikasi [Save] disabled selama proses
26. Verifikasi [Clear Field] disabled selama proses
27. Verifikasi icon `[✕]` disabled selama proses
28. Verifikasi tepat satu toast `Success, unit has been updated.`
29. Lepas intercept respons Edit Measurement
30. Tutup toast

### TC-GS-UOM-70: Edit hanya Unit Name berhasil dan Symbol tidak berubah

31. Klik `⋯` baris `Gal {runId}-027` > Edit
32. Ubah Unit Name menjadi `US Gal {runId}-027`
33. Klik [Save]
34. Verifikasi toast `Success, unit has been updated.`
35. Tutup toast
36. Verifikasi modal tertutup
37. Verifikasi baris tampil `US Gal {runId}-027` / `gal`
38. Verifikasi Last Updated baris `US Gal {runId}-027` sesuai waktu Save (toleransi satu menit)

### TC-GS-UOM-71: Edit hanya Symbol berhasil dan Unit Name tidak berubah

39. Klik `⋯` baris `Oz {runId}-027` > Edit
40. Ubah Symbol menjadi `oz.`
41. Klik [Save]
42. Verifikasi toast `Success, unit has been updated.`
43. Tutup toast
44. Verifikasi baris `Oz {runId}-027` menampilkan Symbol `oz.`

### TC-GS-UOM-72: Edit Unit Name dan Symbol sekaligus berhasil

45. Klik `⋯` baris `Lb {runId}-027` > Edit
46. Ubah Unit Name menjadi `Lb Mass {runId}-027` dan Symbol menjadi `lbm`
47. Klik [Save]
48. Verifikasi toast `Success, unit has been updated.`
49. Tutup toast
50. Verifikasi baris tampil `Lb Mass {runId}-027` / `lbm`

### TC-GS-UOM-75: Case-only pada Unit Name bersama perubahan nyata Symbol hanya menyimpan Symbol

51. Klik `⋯` baris `Set {runId}-027` > Edit
52. Ubah Unit Name menjadi `SET {runId}-027` dan Symbol menjadi `st`
53. Klik [Save]
54. Verifikasi toast `Success, unit has been updated.`
55. Tutup toast
56. Verifikasi Unit Name baris tetap `Set {runId}-027`
57. Verifikasi Symbol baris menjadi `st`

### TC-GS-UOM-83: Edit dengan spasi depan dan belakang disimpan ter-trim

58. Klik `⋯` baris `Trim {runId}-027` > Edit
59. Ubah Symbol menjadi `  hm2 `
60. Klik [Save]
61. Verifikasi toast `Success, unit has been updated.`
62. Tutup toast
63. Verifikasi Symbol baris `Trim {runId}-027` tampil `hm2`

### TC-GS-UOM-79: Edit Unit Name tepat 120 karakter berhasil

64. Klik `⋯` baris `Long {runId}-027` > Edit
65. Ganti isi Unit Name dengan string 120 karakter huruf `b` berulang (akhiran ` {runId}-027` termasuk dalam 120 karakter)
66. Klik [Save]
67. Verifikasi toast `Success, unit has been updated.`
68. Tutup toast

### TC-GS-UOM-264: Edit Symbol menjadi Symbol unit lain diizinkan

69. Klik `⋯` baris `Foot {runId}-027` > Edit
70. Ubah Symbol menjadi `kg`
71. Tunggu debounce
72. Verifikasi tidak ada error pada Symbol
73. Klik [Save]
74. Verifikasi toast `Success, unit has been updated.`
75. Tutup toast
76. Verifikasi baris `Foot {runId}-027` menampilkan Symbol `kg`
77. Ganti isi kotak search dengan `Kilogram`, tekan Enter
78. Verifikasi baris `Kilogram` menampilkan Symbol `kg`

## Notes

- Mode: FE+BE (intercept parsial untuk TC-GS-UOM-88). Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Jumlah langkah: 78.
- Urutan TC berbeda dari urutan sumber, mengikuti bagian 3 konvensi: kasus No-Op (TC-73, TC-74) yang tidak mengubah data lebih dulu, lalu saving state (TC-88), kemudian rangkaian Edit sukses. Dependensi data TC-88 (TC-83) dan TC-83 (TC-41), serta dependensi `1. TC-GS-UOM-36` pada TC lain, dipenuhi oleh seeding spec sendiri lewat API di hook `before`; spec tidak menumpang spec lain.
- Spec ini sekitar 78 langkah (di atas batas 35 langkah); alasan pertahanan: seluruh blok satu kelas (Edit dengan Save), tiap blok memakai unit milik sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan tidak ada blok yang menghapus data. Kenaikan jumlah langkah terutama berasal dari pola berulang "buka Edit, ubah, Save, verifikasi toast, tutup toast". Sepuluh TC dipetakan ke satu spec karena semuanya topik aksi yang sama (Edit) dengan kondisi data bervariasi yang disiapkan seeding.
- Langkah 2 adalah `Verifikasi` pembanding (butir 2 bagian 8b), bukan dari Expected TC.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (Search `{runId}-027` untuk menemukan baris target, tersaring pada kesepuluh unit milik spec), semua langkah "Tutup toast" (S-09: toast sukses atau netral identik berulang di-dismiss sebelum diasersi lagi), langkah 3 dan 10 (mencatat Last Updated untuk perbandingan), langkah 29 (melepas intercept, S-09), dan langkah 77 (mengganti isi kotak search ke `Kilogram` untuk membaca baris Pre-setup pembanding).
- TC-GS-UOM-73 dan TC-GS-UOM-74 (Post Condition "tidak ada entri log") tidak diasersi di spec ini (kelas g, prinsip 13g); asersi absence log berada di spec 065 (`TC-GS-UOM-E2E-065-log-absence-no-op-case-only-dan-relasi-konsumen`) dengan aksi dan baseline sendiri, sesuai bagian "Pembagian TC lintas spec" pada `docs/coverage/GlobalSettingsMeasurement.md`. Id TC-73 dan TC-74 tetap di `sourceTc` spec ini karena aksi No-Op dan toast `No changes to save.` diasersi di sini (S-05).
- Nama pada TC sumber (`Gallon`, `Ounce`, `Pound`, `Ton`, `Roll`, `Set`, `Hectare`) diganti nama milik spec bersuffix `{runId}-027` (S-06); nama pada Expected TC diganti sama.
- TC-GS-UOM-79: TC sumber menyebut "berbeda dari D-03" (Unit Name 120 karakter huruf `l`); string `b` berulang dipakai sehingga tidak bentrok dengan nama 120 karakter lain di suite.
- TC-GS-UOM-264: baris pembanding `Kilogram` dibaca lewat Search `Kilogram` karena tidak termasuk hasil Search `{runId}-027`.
- Temuan untuk QA:
  - TC-GS-UOM-88 Expected butir b menyebut `[Clear Field]` dan icon `[✕]` ikut disabled; TC tidak menyebut apakah field Unit Name juga disabled, sehingga tidak diasersi.
  - TC-GS-UOM-79 tidak menyatakan nilai Last Updated atau tampilan nama 120 karakter di tabel (dipotong atau ellipsis); hanya toast yang diasersi sesuai Expected.
