---
id: TC-AC-ACHS-E2E-186-pagination-dan-kombinasi-approvals-tab-active
title: "Pagination dan Kombinasi Empat Kontrol Approvals Tab Active"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-405
  - TC-AC-ACHS-406
  - TC-AC-ACHS-407
  - TC-AC-ACHS-408
  - TC-AC-ACHS-409
coverage:
  web: automated
---

# Pagination dan Kombinasi Empat Kontrol Approvals Tab Active

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API; tanpa intercept).
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`, kata sandi `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; hook `beforeEach` suite membuka Stock List, dan spec ini membuka Approvals > Hardware Stock sebagai langkah pertama. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Approvals Hardware Stock disetel true di hook `before` suite dan dipulihkan di `after` (lihat suite.md). Suite serial (`parallel: false`).
- Data Pre-setup (hanya dibaca; spec tidak melakukan Approve, Reject, atau Cancel): Approvals Tab Active dengan 12 Subject pending (Pre-setup #21, Tabel C TC). Baris dirujuk lewat nomor baris Tabel C: `#n` (n = 1 sampai 12) berarti baris ke-n Tabel C (`Fixture.hardwareStock.p21.c[n]`). Urutan default FIFO (Requested At terlama di atas) sama dengan urutan Tabel C (#1 teratas, #12 terbawah). Nilai sel tidak ditulis di spec ini; penulis script membaca nilainya dari fixture lewat kunci pada tabel Parameter Pre-setup (R-06).
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture pada tabel berikut, dibaca dari `fixtures/hardwareStock.json` (identitas data, bukan rahasia; berkas belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Kunci fixture |
  |---|---|---|---|
  | Email akun Total Control Principal #1 | #1 | Total Control Principal; akun aktor, login di hook `before`; kata sandi `Spectra.env.AC_TC_PASSWORD` | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Type baris #n (n = 1 sampai 12) | #21 Tabel C | Activation Collision pada #1, #4, #5, #9, #11, #12; Register Duplicate pada #2, #3, #6, #7, #8, #10 | `Fixture.hardwareStock.p21.c[n].type` |
  | Matched Identifier baris #n (n = 1 sampai 12) | #21 Tabel C | Serial Number atau MAC address unik tiap baris, identitas baris hasil; #3, #9, #12 berformat MAC | `Fixture.hardwareStock.p21.c[n].matchedIdentifier` |
  | Requested By baris #n (n = 1 sampai 12) | #21 Tabel C | Client, Distributor, atau Principal (Pre-setup #23) dengan label peran dalam kurung; Distributor pada #3, #6, #8, #10 | `Fixture.hardwareStock.p21.c[n].requestedBy` |
  | Keyword Search nama Client | #21 Tabel C | diturunkan dari `Fixture.hardwareStock.p21.c[5].requestedBy`: nama Client tanpa awalan badan usaha dan tanpa label peran dalam kurung; nama yang sama muncul pada Existing Record #1 dan #11, sehingga Search menghasilkan tepat tiga baris #1, #5, #11 (semua Activation Collision) | `Fixture.hardwareStock.derived.clientCoreNameActive` |
- Pilihan spec (bukan nilai TC): TC-409 tidak menyebut Filter, sort, dan ukuran halaman yang dipakai; spec memakai Filter Type = `Activation Collision`, sort Type Ascending, dan rows per page 25. TC-406 langkah 5 sampai 6 dan TC-408 langkah 3 sampai 5 disusun ulang sesuai ukuran data 12 baris (lihat Temuan untuk QA).

## Test Steps

### Default 10 baris, opsi page size, info jumlah (TC-AC-ACHS-405)

1. Buka Approvals > Hardware Stock
2. Klik Tab `Active`
3. Verifikasi default 10 baris per halaman
4. Verifikasi info `Showing 1–10 of 12 entries`
5. Buka dropdown rows per page
6. Verifikasi opsi rows per page: 10, 25, 50, 100 (tanpa opsi All)
7. Tutup dropdown rows per page

### Next, input halaman, ganti page size (TC-AC-ACHS-406)

8. Klik `Next`
9. Verifikasi halaman 2 terbuka dengan info `Showing 11–12 of 12 entries`
10. Isi input halaman `1`, tekan Enter
11. Verifikasi tabel kembali ke halaman 1
12. Klik `Next`
13. Ganti rows per page ke 25
14. Verifikasi tabel kembali ke halaman 1 (mengganti page size selalu kembali ke halaman 1)
15. Ganti rows per page ke 10

### Input nomor halaman tidak valid diabaikan (TC-AC-ACHS-407)

16. Untuk setiap nilai `0`, `6`, `abc` (langkah 17 sampai 18): lakukan langkah berikut
17. Isi input halaman dengan nilai, tekan Enter
18. Verifikasi input diabaikan, tabel tetap di halaman 1 (`Showing 1–10 of 12 entries`)

### Search kembali ke halaman 1, ganti sort tetap di halaman sekarang (TC-AC-ACHS-408)

19. Klik `Next`
20. Ketik Search `Fixture.hardwareStock.derived.clientCoreNameActive`, tekan Enter
21. Verifikasi halaman kembali ke 1 (tabel menampilkan 3 baris dengan info `Showing 1–3 of 3 entries`)
22. Klik icon `(←)` pada kotak Search
23. Klik `Next`
24. Klik header Type sekali
25. Verifikasi nomor halaman tidak berubah, tetap halaman 2 (`Showing 11–12 of 12 entries`)
26. Klik header Type dua kali sampai netral

### Kombinasi empat kontrol dan pemulihan dari 0 hasil (TC-AC-ACHS-409)

27. Ketik Search `Fixture.hardwareStock.derived.clientCoreNameActive`, tekan Enter
28. Klik icon Filter, isi Type = `Activation Collision`, klik `[Apply]`
29. Klik header kolom Type sekali (Ascending)
30. Ubah rows per page menjadi 25
31. Verifikasi keyword `Fixture.hardwareStock.derived.clientCoreNameActive` tetap terisi di kotak Search
32. Verifikasi badge titik tampil pada ikon Filter
33. Verifikasi indikator Ascending aktif pada Type
34. Verifikasi rows per page menunjukkan 25
35. Verifikasi tabel menampilkan 3 baris: #1, #5, #11
36. Ganti isi kotak search dengan `zzqx-tidak-ada`, tekan Enter
37. Verifikasi empty state: ilustrasi dengan Title `No results found` dan Description `Try adjusting your search or filter.`
38. Kosongkan isi kotak search, tekan Enter
39. Verifikasi tabel kembali menampilkan 3 baris #1, #5, #11 sesuai Filter, Sort, dan page size yang masih aktif
40. Verifikasi badge titik Filter, indikator Ascending Type, dan rows per page 25 masih aktif
41. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
42. Klik header kolom Type dua kali sampai netral
43. Ganti rows per page ke 10
44. Klik icon `(←)` pada kotak Search

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-405 sampai 409). Tidak ada TC hanya-BE di spec ini.
- Nilai Pre-setup tidak ditulis literal; dirujuk lewat nomor item Pre-setup (#21/#22, Tabel C/D) dan kunci fixture, nilai dibaca penulis script dari tabel TC (R-06); tidak ada pengecualian S-12 dipakai. Teks antarmuka asli (nama kolom, label Type dan Category, placeholder, tooltip, teks empty state, nama berkas unduhan) tetap ditulis verbatim.
- Langkah penghubung (bukan dari langkah TC): langkah 2 (klik Tab `Active`); langkah 7 (tutup dropdown); langkah 15, 22, 26, 41 sampai 44 (memulihkan page size, Search, sort, dan Filter ke default, S-09). Langkah 12 dan 19 (Next ke halaman 2) menyiapkan keadaan halaman 2 sebelum aksi uji (S-14).
- Idiom ulang "Untuk setiap nilai" pada langkah 16 sampai 18 (3 iterasi) dengan parameter di langkah.
- Spec melewati sekitar 35 langkah (44 langkah): alasan, semua blok satu surface (Pagination Approvals Tab Active) dan satu dataset read-only; tiap blok memulihkan state sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Konfirmasi (#8): `Fixture.hardwareStock.derived.clientCoreNameActive` sama dengan substring yang ditulis TC-408 dan TC-409 (nama inti Client, bukan nilai kolom penuh); hasil pada Tabel C: tiga baris #1, #5, #11. Tidak ada perbedaan.
- Temuan untuk QA:
  - TC-406 langkah 5 ("Pilih rows per page 25, lalu klik Next jika ada halaman berikutnya") dan langkah 6 ("Pada halaman 2 ganti rows per page ke 10") bertentangan dengan data 12 baris: pada rows per page 25 tidak ada halaman 2. Spec memakai Next pada rows per page 10 (langkah 12) lalu mengganti ke 25 untuk mengasersi Expected c (kembali ke halaman 1); langkah bersyarat tidak ditulis.
  - TC-408 langkah 3 sampai 5 ("Buka halaman 2; Search `Fixture.hardwareStock.derived.clientCoreNameActive`; kembali ke halaman 2 jika ada, lalu klik header sort") tidak bisa dijalankan karena Search `Fixture.hardwareStock.derived.clientCoreNameActive` hanya menghasilkan 3 baris (satu halaman). Spec mengasersi Expected a pada Search (langkah 19 sampai 21) lalu mengasersi Expected b (sort tetap di halaman sekarang) pada halaman 2 tanpa Search (langkah 23 sampai 25).
  - TC-407 Expected menyebut input `6` "melebihi halaman terakhir" dengan 2 halaman; spec memakai `6` sesuai TC.
  - TC-409 langkah 4 sampai 6 tidak menyebut nilai Filter, kolom sort, dan page size; spec memilih sesuai Prerequisites.
