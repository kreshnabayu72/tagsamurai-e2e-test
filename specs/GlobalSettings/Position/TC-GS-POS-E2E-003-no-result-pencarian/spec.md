---
id: TC-GS-POS-E2E-003-no-result-pencarian
title: No result state dari pencarian yang tidak punya kecocokan
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-19
coverage:
  web: automated
---

# No result state dari pencarian yang tidak punya kecocokan

## Prerequisites

- Sudah login sebagai Role Total Control. Kredensial diambil lewat `Spectra.env.ADMIN_USERNAME` dan
  `Spectra.env.ADMIN_PASSWORD`.
- `Fixture.globalSettingsPosition.actors.totalControl` adalah akun penguji baseline.
- Berada di `Global Settings > User > Position` pada entitas uji utama, sama dengan entitas spec 001.
  Entitas ini sudah punya data Position hasil seed dan populasi, jadi kondisi yang diuji di sini
  adalah "ada data tapi tidak ada yang cocok", bukan "tidak ada data".
- `Fixture.globalSettingsPosition.data.searchNoMatch` adalah satu kata kunci yang formatnya valid
  tetapi dijamin tidak cocok dengan nama Position mana pun di entitas ini, dan tidak boleh sama
  dengan data seed `Finance Manager` maupun `HR Business Partner`.
- `Fixture.globalSettingsPosition.data.searchPartialMatch` adalah satu kata kunci yang cocok dengan
  sebagian nama Position di entitas ini. Dipakai untuk membuktikan bahwa no result pada spec ini
  memang karena kata kuncinya, bukan karena search-nya rusak.
- `Fixture.globalSettingsPosition.captions.emptyFiltered.title` adalah judul empty state hasil
  pencarian, yaitu `No results found`.
- `Fixture.globalSettingsPosition.captions.emptyFiltered.description` adalah deskripsi empty state
  hasil pencarian, yaitu `Try adjusting your search or filter.`
- `Fixture.globalSettingsPosition.captions.emptyTable.title` adalah judul empty state genuinely
  kosong, yaitu `No positions yet`. Dipakai sebagai pembeda supaya spec ini tidak lolos kalau yang
  tampil adalah empty state yang salah.
- `Fixture.globalSettingsPosition.captions.search.placeholder` adalah placeholder kolom Search,
  yaitu `Search position name...`

## Test Steps

### Membuka kolom Search

1. Klik tombol `Search` pada TableTools toolbar
2. Verifikasi kolom Search tampil dengan placeholder
   `Fixture.globalSettingsPosition.captions.search.placeholder`
3. Verifikasi tabel tetap menampilkan seluruh baris Position dan belum tersaring
4. Verifikasi input Search mendapat fokus keyboard

### Pencarian tidak berjalan sebelum menekan Enter

5. Ketik `Fixture.globalSettingsPosition.data.searchNoMatch` ke dalam kolom Search
6. Verifikasi tabel masih menampilkan seluruh baris Position, sehingga pencarian tidak berjalan
   real-time saat mengetik
7. Verifikasi tidak ada empty state yang muncul pada langkah ini
8. Verifikasi jumlah baris yang tampil sama dengan sebelum mengetik

### Pencarian dengan Enter menghasilkan no result

9. Tekan `Enter`
10. Verifikasi tabel selesai menyaring tanpa menampilkan pesan `Unable to load this data.` dan tanpa
    tombol `[Try Again]`
11. Verifikasi tidak ada baris Position yang tersisa di dalam area tabel
12. Verifikasi empty state tampil di dalam area tabel
13. Verifikasi judul empty state adalah
    `Fixture.globalSettingsPosition.captions.emptyFiltered.title`
14. Verifikasi deskripsi empty state adalah
    `Fixture.globalSettingsPosition.captions.emptyFiltered.description`
15. Verifikasi judul empty state bukan
    `Fixture.globalSettingsPosition.captions.emptyTable.title`
16. Verifikasi empty state ini berbeda dari empty state genuinely kosong pada spec 002, yaitu pada
    copy yang ditampilkan
17. Verifikasi empty state hasil pencarian tidak memuat tombol `Create Position` maupun ajakan
    membuat Position, karena masalahnya bukan katalog yang kosong melainkan pencarian yang tidak
    cocok

### Toolbar tetap utuh saat no result

18. Verifikasi tombol `[+ Position]` tetap tampil dan dapat diklik saat no result
19. Verifikasi tombol `Filter` tetap tampil dan dapat diklik
20. Verifikasi tombol `Download` tetap tampil
21. Verifikasi tombol `Changelog` tetap tampil
22. Verifikasi input Search masih menampilkan kata kunci yang diketik, sehingga user bisa mengoreksinya
23. Verifikasi footer pagination tetap tampil

### Pemulihan dengan kata kunci yang cocok

24. Hapus kata kunci dari kolom Search sampai kosong
25. Tekan `Enter`
26. Verifikasi seluruh baris Position tampil kembali
27. Verifikasi empty state `No results found` tidak lagi tampil
28. Verifikasi jumlah baris yang tampil sama dengan pada langkah 8

### Bukti bahwa no result berasal dari kata kunci, bukan search rusak

29. Ketik `Fixture.globalSettingsPosition.data.searchPartialMatch` ke dalam kolom Search
30. Tekan `Enter`
31. Verifikasi tabel menampilkan hanya Position yang namanya cocok dengan kata kunci tersebut
32. Verifikasi setiap baris yang tampil memang mengandung kata kunci itu pada kolom `Name`
33. Verifikasi tidak ada baris dengan nama yang tidak mengandung kata kunci itu
34. Verifikasi hasil ini membuktikan kolom Search berfungsi, sehingga no result pada langkah 12
    memang_correct pada kata kuncinya

## Notes

- Pencarian di modul ini dipicu lewat `Enter`, bukan real-time saat mengetik
  (PRD `position.md` §4.4 poin 3 dan §5). Langkah 5 sampai 8 sengaja memisahkan kondisi "sudah
  mengetik" dari kondisi "sudah menekan Enter" karena kalau pencarian diam-diam berjalan real-time,
  test tetap bisa lolos di langkah 31 tapi gagal menguji timing yang benar.
- Spec ini memakai entitas yang sudah terisi data, bukan entitas kosong pada spec 002. Kalau dipakai
  entitas kosong, empty state yang muncul mungkin `No positions yet` dan spec ini tidak menguji apa
  pun.
- Pemulihan dengan kata kunci yang cocok sengaja tetap diuji di spec ini walau pemulihan lengkap
  bersama filter ada di spec 026. Yang diuji di sini hanya bahwa no result bisa dibatalkan dengan
  satu tindakan di kolom Search itu sendiri, tanpa harus memuat ulang halaman.
- Subbagian terakhir dipakai sebagai pembuktian bahwa emptiness pada langkah 12 memang berasal dari
  kata kunci. Tanpa itu, spec ini akan lolos juga apabila Search selalu mengembalikan kosong untuk
  semua input.
- Copy `No results found` dipakai bersama oleh tabel utama dan Popup Changelog, sesuai §7.1. Spec ini
  hanya memverifikasinya di tabel utama; konteks Popup Changelog ada di spec 035.
