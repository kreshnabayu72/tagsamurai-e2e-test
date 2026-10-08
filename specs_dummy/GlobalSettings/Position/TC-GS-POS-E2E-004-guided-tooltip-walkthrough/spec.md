---
id: TC-GS-POS-E2E-004-guided-tooltip-walkthrough
title: Guided Tooltip walkthrough pada tab Position
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-229
  - TC-GS-POS-230
  - TC-GS-POS-231
  - TC-GS-POS-232
  - TC-GS-POS-234
coverage:
  web: automated
---

# Guided Tooltip walkthrough pada tab Position

## Prerequisites

- `Mode: mock`. Spec ini menguji perilaku tampilan dan state penandaan yang tidak menyentuh
  endpoint write apa pun, sehingga dijalankan tim FE sebagai integration test dengan condition
  yang dikendalikan.
- Flag penandaan yang dikendalikan ada di
  `Fixture.globalSettingsPosition.guidedTooltip.flagKey`, yaitu `guided_tooltip_seen_gs-position`,
  dan nilainya dibaca lewat `Fixture.globalSettingsPosition.guidedTooltip.readFlag` serta ditulis
  ulang lewat `Fixture.globalSettingsPosition.guidedTooltip.writeFlag`. Kemampuan baca dan tulis
  flag ini disiapkan tim FE, karena spec ini perlu mengembalikan flag ke kondisi awal di beberapa
  subbagian.
- `Fixture.globalSettingsPosition.guidedTooltip.pageKey` adalah `gs-position`, sesuai §4.7 dan
  `foundation/functions/guided-tooltip.md` §16.6.
- `Fixture.globalSettingsPosition.guidedTooltip.steps` adalah daftar tiga step kanonik pada tab ini.
  Isi,title, dan description setiap step diambil dari PRD `position.md` §4.7 melalui fixture, tidak
  diketik ulang di spec ini. Jumlah step diambil dari
  `Fixture.globalSettingsPosition.guidedTooltip.totalSteps` dan indikator langkah Expected
  `"Step [N] of [Total]"` mengikuti format itu.
- `Fixture.globalSettingsPosition.guidedTooltip.stepIndicator` adalah format teks indikator langkah
  yang dipakai komponen, yaitu `Step [N] of [Total]`.
- `Fixture.globalSettingsPosition.captions.guidedTooltip.actionBack`, `.actionNext`, `.actionSkip`,
  dan `.actionDone` adalah label tombol navigasi walkthrough.
- `Fixture.globalSettingsPosition.data.viewport.desktop` adalah ukuran viewport Desktop untuk
  langkah yangebut resize.
- `Fixture.globalSettingsPosition.data.viewport.mobile` adalah ukuran viewport Mobile untuk langkah
  yang menguji tooltip sebagai bottom sheet mini.
- Target element ketiga step adalah landmark permanen, yaitu tombol `[+ Position]`, area tabel
  utama, dan tombol `Changelog` pada toolbar. Semua dijamin selalu ada saat halaman dimuat, dan
  tidak ada satu pun yang bergantung pada data baris tertentu.

## Test Steps

### Kunjungan pertama: walkthrough muncul otomatis

1. Set flag `Fixture.globalSettingsPosition.guidedTooltip.flagKey` menjadi `false` melalui
   `Fixture.globalSettingsPosition.guidedTooltip.writeFlag`
2. Verifikasi flag terbaca `false` lewat `Fixture.globalSettingsPosition.guidedTooltip.readFlag`
3. Buka `Global Settings > User > Position` untuk pertama kalinya setelah flag di-reset
4. Verifikasi walkthrough muncul otomatis tanpa perlu aksi tambahan dari pengguna
5. Verifikasi indikator langkah menampilkan `Step 1 of 3`
6. Verifikasi elemen yang di-highlight adalah tombol `[+ Position]` di toolbar
7. Verifikasi judul step 1 sesuai `Fixture.globalSettingsPosition.guidedTooltip.steps` pada indeks
   1
8. Verifikasi description step 1 sesuai `Fixture.globalSettingsPosition.guidedTooltip.steps` pada
   indeks 1
9. Verifikasi tombol `[Back]` tidak tampil pada step 1
10. Verifikasi tombol `[Skip]`, `[Next]` tampil
11. Verifikasi area di luar tooltip box darkened oleh overlay gelap
12. Verifikasi elemen target terpotong dari overlay sehingga terlihat seperti spotlight
13. Verifikasi tooltip box mendapat fokus keyboard sejak walkthrough aktif

### Kunjungan kedua: tidak muncul otomatis dan diputar ulang manual

14. Tutup walkthrough dengan tombol `[Skip]`, lalu verifikasi flag menjadi `true`
15. Tutup dan buka kembali tab `Position`
16. Verifikasi walkthrough tidak muncul otomatis pada kunjungan kedua
17. Verifikasi flag tetap `true` dan tidak di-reset oleh kunjungan kedua
18. Verifikasi tombol `[?]` tersedia di header halaman
19. Klik tombol `[?]`
20. Verifikasi walkthrough mulai ulang dari step 1
21. Verifikasi indikator langkah kembali menampilkan `Step 1 of 3`
22. Verifikasi flag tetap `true` selama replay manual berlangsung, yaitu replay tidak mereset flag

### Siklus navigasi Back, Next, dan Done

23. Klik tombol `[Next]`
24. Verifikasi indikator langkah menampilkan `Step 2 of 3`
25. Verifikasi elemen yang di-highlight adalah area tabel utama
26. Verifikasi judul dan description step 2 sesuai
    `Fixture.globalSettingsPosition.guidedTooltip.steps` pada indeks 2
27. Verifikasi tombol `[Back]` sekarang tampil
28. Klik tombol `[Back]`
29. Verifikasi indikator langkah kembali menampilkan `Step 1 of 3`
30. Verifikasi tombol `[Back]` kembali tidak tampil
31. Verifikasi isi step 1 kembali sama seperti langkah 7 dan 8, bukan step yang sudah dilewati
32. Klik tombol `[Next]` lalu `[Next]` lagi sehingga berada di step 3
33. Verifikasi indikator langkah menampilkan `Step 3 of 3`
34. Verifikasi elemen yang di-highlight adalah tombol `Changelog` di toolbar
35. Verifikasi judul dan description step 3 sesuai
    `Fixture.globalSettingsPosition.guidedTooltip.steps` pada indeks 3
36. Verifikasi tombol `[Next]` berubah menjadi `[Done]` pada step terakhir
37. Verifikasi tombol `[Skip]` masih tampil pada step terakhir
38. Klik tombol `[Done]`
39. Verifikasi walkthrough tertutup
40. Verifikasi flag `seen` bernilai `true`
41. Verifikasi tooltip box dan overlay gelap tidak lagi tampil

### Skip dari step mana pun dan klik overlay

42. Buka ulang walkthrough lewat tombol `[?]`, lalu klik tombol `[Next]` sehingga berada di step 2
43. Klik tombol `[Skip]`
44. Verifikasi walkthrough tertutup dari step 2, bukan hanya dari step terakhir
45. Verifikasi flag tetap `true`
46. Buka ulang walkthrough lewat tombol `[?]`
47. Klik area overlay gelap, bukan tombol navigasi apa pun
48. Verifikasi walkthrough tertutup, sama seperti}}[eneffect pressing `[Skip]`
49. Verifikasi flag tetap `true`

### Keluar tanpa menyelesaikan tidak menandai flag

50. Set flag menjadi `false` kembali, lalu buka tab `Position` sehingga walkthrough muncul di step 1
51. Ubah ukuran viewport browser di tengah walkthrough
52. Verifikasi walkthrough tertutup akibat perubahan ukuran viewport
53. Verifikasi flag masih bernilai `false`, sehingga keluar tanpa menyelesaikan tidak dianggap selesai
54. Verifikasi tooltip box dan overlay tidak tampil
55. Buka tab `Position` lagi
56. Verifikasi walkthrough otomatis muncul kembali dari step 1
57. Ulangi langkah 50 sampai 55, lalu navigasi keluar dari tab `Position` ke tab `User List`
58. Verifikasi walkthrough tertutup akibat perpindahan tab
59. Verifikasi flag masih bernilai `false`
60. Buka kembali tab `Position` setelah berpindah ke `User List`
61. Verifikasi walkthrough otomatis muncul kembali dari step 1, sama seperti pada kasus resize

### Navigasi keyboard

62. Set flag menjadi `false`, lalu buka tab `Position` sehingga walkthrough muncul di step 1
63. Verifikasi tooltip box mendapat fokus keyboard tanpa perlu klik
64. Tekan tombol `Enter`
65. Verifikasi walkthrough maju ke step 2
66. Kembalikan fokus ke tooltip box, lalu tekan tombol panah `Right`
67. Verifikasi walkthrough maju ke step 3
68. Tekan tombol panah `Left`
69. Verifikasi walkthrough mundur ke step 2
70. Tekan tombol `Esc`
71. Verifikasi walkthrough tertutup
72. Verifikasi flag menjadi `true`, sehingga `Esc` diperlakukan sebagai Skip
73. Verifikasi overlay gelap tidak lagi tampil

### Perilaku di Mobile

74. Set flag menjadi `false`, lalu buka tab `Position` pada viewport
    `Fixture.globalSettingsPosition.data.viewport.mobile`
75. Verifikasi walkthrough tetap muncul
76. Verifikasi tooltip tampil sebagai bottom sheet mini
77. Verifikasi spotlight pada elemen target tetap ada
78. Verifikasi indikator langkah tetap mengikuti format yang sama
79. Verifikasi walkthrough dapat diselesaikan dari tampilan tersebut
80. Verifikasi flag menjadi `true` setelah walkthrough diselesaikan

## Notes

- **Jumlah step mengikuti PRD `position.md` §4.7, yaitu tiga, bukan dua seperti tertulis di
  TC-GS-POS-229.** Alasannya ada di `foundation/functions/guided-tooltip.md` §Aturan Terkunci nomor
  2 dan nomor 4, yang tidak boleh di-override PRD: target walkthrough wajib elemen permanen, dan
  row action termasuk yang dilarang. Step 2 pada TC-GS-POS-229 menargetkan row action `Delete`,
  sehingga violates aturan terkunci itu. Tiga step pada PRD §4.7 — tombol `[+ Position]`, area
  tabel, tombol `Changelog` — semuanya landmark permanen dan memenuhi aturan tersebut.
  Kontradiksi antara TC dan PRD ini dilaporkan di `docs/coverage/GlobalSettingsPosition.md` untuk
  diperbaiki di `tc-position.md`.
- **Title dan description tidak ditulis di spec ini.** PRD §4.7 menuliskan description dalam bahasa
  Indonesia, padahal aturan terkunci nomor 4 mewajibkan bahasa Inggris, dan §4 PRD menyatakan
  seluruh copy UI berbahasa Inggris. Karena salinannya masih ambigu, spec ini mengambil nilainya dari
  fixture sehingga tidak ikut mengunci salah satu bahasa. Copy final harus ditetapkan pemilik PRD.
- Indikator langkah Expected `Step 1 of 3` diambil dari
  `Fixture.globalSettingsPosition.guidedTooltip.totalSteps`, bukan ditulis tetap, supaya kalau
  jumlah step diubah di PRD, spec ini tidak diam-diam jadi salah.
- Subbagian keluar tanpa menyelesaikan dipecah dua, yaitu resize dan perpindahan tab, karena keduanya
  punya mekanisme browser yang berbeda meskipun hasil flag-nya sama. Menggabungkannya membuat
  sulit memastikan sumber pemicunya.
- Deskripsi target pada langkah 7, 8, dan 34 diambil dari fixture, bukan ditulis ulang, karena
  tooltip sendiri tidak punya selector stabil yang boleh diasumsikan.
- Verifikasi spotlight pada langkah 12 sengaja dibuat eksplisit karena area yang darkened saja
  tidak membuktikan bahwa elemen target benar-benar ter-cutout.
- Auto-trigger pada kunjungan pertama bergantung pada flag yang tersimpan per akun, jadi spec ini
  memanggil flag secara eksplisit di awal tiap subbagian yang memerlukan kondisi awal tertentu
  alih-alih mengandalkan urutan spec.
