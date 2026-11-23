---
id: TC-FA-SU-E2E-255-tab-transaction-admin-log-search
title: "Tab Transaction Admin Log: Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-769
  - TC-FA-SU-770
  - TC-FA-SU-771
coverage:
  web: automated
---

# Tab Transaction Admin Log: Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso. Sub-tab Borrow berisi 5 baris sesuai Pre-setup #29 TC (Transaction ID `BRW-2026-0315`, `BRW-2026-0314`, `BRW-2026-0313`, `BRW-2026-0312`, dan satu baris Draft dengan Transaction ID `—`; tanggal `18/07/26` sampai `12/07/26`). Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Kemampuan teknis: hover ikon, kotak Search dengan ikon `✕` dan `←`, overlay Column Visibility pada header kolom `⋯`.
- State: Search dan visibilitas kolom Transaction ID berubah di sisi klien; visibilitas kolom dipulihkan dengan langkah eksplisit (langkah 38 dan 39) dan konfigurasi kolom yang tersimpan dibersihkan hook `after` suite (kemampuan hapus preferensi kolom disediakan tim FE). Tidak ada data yang dibuat spec.

## Test Steps

### TC-FA-SU-769: Siklus interaksi Search: reveal, Enter, clear, collapse

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrow
2. Klik icon Search
3. Verifikasi input Search melebar
4. Verifikasi kursor fokus pada input Search
5. Verifikasi placeholder Search `Search activity, transaction ID, asset, or borrower...` tampil
6. Hover icon Search
7. Verifikasi tooltip `Search` tampil
8. Ketik satu karakter `0` (karakter pertama dari `0313`)
9. Verifikasi icon `✕` muncul di kanan input
10. Verifikasi tabel belum tersaring (kelima baris masih tampil)
11. Ketik sisa `313`, tekan Enter
12. Verifikasi tabel tersaring menjadi `BRW-2026-0313`
13. Klik `✕` pada Search
14. Verifikasi input Search kosong
15. Verifikasi search bar tetap terbuka
16. Verifikasi kursor fokus pada input Search
17. Verifikasi tabel tetap menampilkan hasil search terakhir (`BRW-2026-0313`)
18. Tekan Enter pada input kosong
19. Verifikasi tabel kembali menampilkan semua baris
20. Ketik Search `0313`, tekan Enter
21. Klik `←` pada kotak Search
22. Verifikasi search bar menutup
23. Verifikasi tabel langsung kembali menampilkan semua baris
24. Klik icon Search
25. Verifikasi input Search kosong (keyword dikosongkan)
26. Ketik Search `  0313  ` (spasi di awal dan akhir), tekan Enter
27. Verifikasi hasil sama dengan `0313` tanpa spasi: tabel menyisakan `BRW-2026-0313`
28. Verifikasi isi input Search tidak berubah (`  0313  `)

### TC-FA-SU-770: Guard kolom non-searchable Date

29. Ganti isi kotak search dengan `18/07/26`, tekan Enter
30. Verifikasi empty state `No results found` tampil (`18/07/26` tidak mencocokkan baris lewat Search)

### TC-FA-SU-771: Search terikat visibilitas kolom Transaction ID

31. Ganti isi kotak search dengan `0313`, tekan Enter
32. Verifikasi tabel menyisakan `BRW-2026-0313`
33. Klik header kolom `⋯`
34. Hilangkan centang `Transaction ID` pada overlay Column Visibility
35. Verifikasi kolom `Transaction ID` tidak tampil dan kolom `Date`, `Activity`, `Name`, `Borrower`, dan `Group` tetap tampil
36. Ganti isi kotak search dengan `0313`, tekan Enter
37. Verifikasi tabel tidak menyisakan baris (kolom tersembunyi tidak dicari)
38. Klik header kolom `⋯`
39. Centang kembali `Transaction ID` pada overlay Column Visibility
40. Ganti isi kotak search dengan `0313`, tekan Enter
41. Verifikasi tabel menyisakan `BRW-2026-0313`
42. Klik `←` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna di User List lalu membuka sub-tab; R-16), overlay Column Visibility menutup saat kotak Search dipakai pada langkah 36 dan 40, pemulihan visibilitas kolom pada langkah 38 dan 39 (8b.14, S-03), dan pengosongan Search di akhir spec (langkah 42, S-09). Pada langkah 29, 31, 36, dan 40 kotak Search yang sudah berisi diganti isinya (8b.9); langkah 36 mengulang kata kunci yang sama setelah kolom di-hide, sehingga Enter dijalankan ulang.
- Langkah 35 (kolom lain tetap tampil) adalah anchor positif sebelum asersi hasil kosong pada langkah 37 (8b.2); TC-FA-SU-771 butir b menyebut "kolom yang tampil tetap dicari", sehingga langkah itu bukan asersi di luar TC.
- Temuan untuk QA (S-15): (1) Kolom ACC TC-FA-SU-769 sampai 771 berisi `#20`, yang di Pre-setup adalah Client `FaUserMain`, bukan akun; aktor diambil dari hook suite (Lina Marlina, Pre-setup #1). (2) TC-FA-SU-769 langkah 3 ("Ketik 1 karakter dari `0313`") tidak menyebut karakternya; spec memakai `0`. (3) Post Condition tidak ada pada ketiga TC.
- Spec ini berjumlah 42 langkah dan di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface dengan data seed yang sama; ukuran berasal dari TC-FA-SU-769 yang punya tujuh butir Expected dengan sebagian butir berklausa jamak (satu `Verifikasi` per klausa, S-01) dan delapan langkah aksi berurutan yang tidak dapat dipersingkat.
