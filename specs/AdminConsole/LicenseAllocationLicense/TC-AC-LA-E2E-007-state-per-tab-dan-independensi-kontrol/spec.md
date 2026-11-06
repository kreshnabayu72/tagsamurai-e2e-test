---
id: TC-AC-LA-E2E-007-state-per-tab-dan-independensi-kontrol
title: "State per Tab: Pemulihan Search Filter Sort, Independensi Tab, dan Aksi di Row List"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-35
  - TC-AC-LA-36
  - TC-AC-LA-37
  - TC-AC-LA-38
coverage:
  web: automated
---

# State per Tab: Pemulihan Search Filter Sort, Independensi Tab, dan Aksi di Row List

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status) bersifat baca-saja untuk spec ini kecuali dinyatakan lain; data destruktif dipulihkan baseline automation sebelum tiap spec (Catatan TC).
- Data Pre-setup yang dibaca: #41 alokasi `Waiting for Approval` (Allocation ID `Fixture.license-allocation-license.seed41`). N hasil Search `Sejahtera` pada tab Current dan N baris tab History diturunkan dari seeding #54 dan dicatat di `Fixture.license-allocation-license` (kunci countCurrentSejahtera, countHistory); N hasil Search `Sejahtera` dengan Filter License Type `Concurrent User` harus lebih dari 25 supaya halaman 2 dengan 25 data per halaman ada (lihat Temuan untuk QA).
- Kemampuan teknis: baca nama berkas dan jumlah baris data berkas unduhan CSV (disediakan tim FE); isi sel berkas tidak diasersi (kelas f).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-35: Kembali ke tab yang pernah dikunjungi memulihkan state

1. Klik ikon Search, ketik Search `Sejahtera`, tekan Enter
2. Klik ikon Filter, pilih License Type `Concurrent User`, lalu klik `[Apply]`
3. Urutkan kolom Quantity ascending
4. Pilih 25 data per halaman
5. Pindah ke halaman 2
6. Klik tab `History`
7. Verifikasi tab History pada kunjungan pertama: kotak Search kosong
8. Verifikasi tab History pada kunjungan pertama: tanpa filter
9. Verifikasi tab History pada kunjungan pertama: halaman 1
10. Verifikasi tab History pada kunjungan pertama: sort Last Updated Newest First
11. Klik tab `Current`
12. Verifikasi tab Current menampilkan Search `Sejahtera`
13. Verifikasi tab Current menampilkan filter License Type `Concurrent User` ter-Apply
14. Verifikasi tab Current menampilkan Sort Quantity ascending
15. Verifikasi tab Current menampilkan halaman 2
16. Verifikasi tab Current menampilkan 25 data per halaman

### TC-AC-LA-36: State satu tab tidak memengaruhi tab lain dan opsi filter Status mengikuti tab aktif

17. Kosongkan kotak search: klik `✕` pada Search, tekan Enter
18. Ketik Search `Sejahtera`, tekan Enter
19. Klik tab `History`
20. Verifikasi input Search tab History tidak membawa Search `Sejahtera`
21. Verifikasi tab History tidak membawa filter tab Current
22. Verifikasi tab History tidak membawa sort tab Current
23. Verifikasi tab History berada di halaman 1
24. Klik ikon Filter dan buka dropdown filter Status
25. Verifikasi opsi dropdown Status tab History hanya `Expired`, `Rejected`, dan `Canceled` (status yang ada pada baris tab History)
26. Tutup panel Filter

### TC-AC-LA-37: Search, Filter, Sort, paginasi, dan Download hanya pada tab aktif

27. Klik tab `Current`
28. Pulihkan state tab Current ke default: kosongkan Filter License Type `Concurrent User` lewat `[Clear Field]` lalu `[Apply]`, urutkan Last Updated Newest First, pilih 10 data per halaman dan halaman 1
29. Kosongkan kotak search: klik `✕` pada Search, tekan Enter
30. Ketik Search `Sejahtera`, tekan Enter
31. Klik Download as CSV pada tab Current
32. Verifikasi berkas yang terunduh bernama `License-Allocation-Current.csv`
33. Verifikasi jumlah baris data berkas sama dengan N hasil Search `Sejahtera` pada tab Current
34. Klik tab `History`
35. Klik Download as CSV pada tab History
36. Verifikasi berkas yang terunduh bernama `License-Allocation-History.csv`
37. Verifikasi jumlah baris data berkas sama dengan N baris tab History tanpa Search tab Current

### TC-AC-LA-38: Tidak ada halaman Detail dan aksi record hanya di row action

38. Klik tab `Current`, lalu kosongkan kotak search: klik `✕` pada Search, tekan Enter
39. Ketik Search Allocation ID seed `Waiting for Approval` (`Fixture.license-allocation-license.seed41`), tekan Enter
40. Klik baris pada area di luar Allocation ID, nama Client, dan row action
41. Verifikasi List tab Current masih tampil dengan baris Allocation ID seed `Waiting for Approval` (`Fixture.license-allocation-license.seed41`)
42. Verifikasi klik area baris tidak membuka halaman Detail apa pun
43. Verifikasi klik area baris tidak melakukan aksi
44. Klik ikon `⋯` baris itu
45. Verifikasi menu `⋯` memuat aksi record (`Allocation Log`, `Edit`, `Cancel Allocation`)
46. Verifikasi tidak ada tombol aksi record di luar menu `⋯`
47. Verifikasi atribut record tampil sebagai kolom List

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 17 dan 18 (mengosongkan kotak Search lalu mengetik Search baru, R-16), langkah pindah tab, langkah penutupan panel Filter, dan langkah pemulihan Search, Filter, dan Sort ke default sebelum TC-AC-LA-38 (S-09), dan langkah 28 (pemulihan Filter, Sort, dan jumlah data per halaman tab Current ke default sebelum Download TC-AC-LA-37, S-09; state itu dibawa dari TC-AC-LA-35: Filter `Concurrent User`, Sort Quantity ascending, 25 data per halaman).
- Spec ini lebih dari 35 langkah. Alasannya: semua blok satu topik (state dan independensi kontrol per tab pada List), memakai seed baca-saja dan state tab yang dibangun berurutan, sehingga TC-AC-LA-36 dan TC-AC-LA-37 memakai state tab TC-AC-LA-35 tanpa membangunnya ulang dengan biaya besar.
- Langkah penghubung (S-03): langkah 29 (`Kosongkan kotak search`) dan langkah 38 (`Kosongkan kotak search` sesudah pindah tab ke Current) mengosongkan kotak Search tab Current secara eksplisit sebelum Search baru, karena spec tidak mengandalkan apakah kotak Search terbawa setelah pindah tab.
- Asersi tambahan (S-03): langkah 41 membuktikan List dan baris seed41 masih tampil sebagai anchor positif untuk asersi absence langkah 42 dan 43 (bagian 8b butir 2); TC-AC-LA-38 Expected tidak memuat klausa anchor itu (lihat Temuan untuk QA).
- Urutan TC mengikuti TC sumber (35, 36, 37, 38); TC-AC-LA-36 bergantung pada TC-AC-LA-35 dan TC-AC-LA-37 pada state tab yang sama.
- Temuan untuk QA:
  - TC-AC-LA-35 meminta halaman 2 dengan 25 data per halaman setelah Search `Sejahtera` dan Filter `Concurrent User`; hasil kombinasi itu perlu lebih dari 25 baris, sedangkan seed #54 hanya `lebih dari 25 baris pada tab Current` secara total; keberadaan halaman 2 tidak terjamin.
  - TC-AC-LA-37 Expected (`memuat baris tab Current yang cocok Search`) memuat asersi isi berkas; spec hanya mengasersi nama berkas dan jumlah baris (kelas f, isi sel tidak diasersi).
  - TC-AC-LA-38 Expected b menyebut seluruh aksi record `hanya tersedia dari menu ⋯` tanpa menyebut aksi yang dilihat Total Control Principal pada record milik `Dewi A`; spec mengasersi aksi yang disebut TC.
  - TC-AC-LA-38 Expected a (tidak ada halaman Detail) adalah absence tanpa klausa anchor di TC; spec menambah `Verifikasi` anchor di langkah 41 (S-03).
  - TC-AC-LA-36 Expected a menyebut tab History `pada kunjungan pertama`, sedangkan TC-AC-LA-35 sudah mengunjungi tab History sebelumnya; state tab History tetap default karena tidak diubah.
