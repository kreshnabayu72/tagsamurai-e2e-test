---
id: TC-FA-TDC-E2E-157-pagination-page-size-navigasi-input-halaman-dan-ganti-page-size
title: "Pagination: Page Size, Navigasi, Input Nomor Halaman, dan Penggantian Page Size"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-554
  - TC-FA-TDC-555
  - TC-FA-TDC-556
  - TC-FA-TDC-557
  - TC-FA-TDC-558
coverage:
  web: automated
---

# Pagination: Page Size, Navigasi, Input Nomor Halaman, dan Penggantian Page Size

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. Asset Type BLD-NP dan BLD-P `Building`, LAND `Land`, class lain `Non-building`.
- Data Dinamis (milik spec, dibuat di hook `before` lewat seeding API, idempotent, dihapus di `after`): 17 class Active tambahan `TDC-01` sampai `TDC-17` (Asset Type `Building`, Allowed Methods `Straight Line`, Class Name `Kelas uji 01` sampai `Kelas uji 17`), sehingga tabel berisi 26 class dengan urutan default Class Code A-Z (9 class Example Data lalu TDC-01 sampai TDC-17). Kode class memakai literal TC tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (lihat Temuan untuk QA). Page size awal adalah 10 baris per halaman (default).
- Data uji (literal TC): page size `10`, `25`, `50`, `100`; input nomor halaman `3`, `0`, `99`, `abc`; keyword Search `TDC`; Filter Asset Type `Building`.
- Kemampuan teknis: seeding class lewat API (`suite.md`); Overlay Page Size dan input nomor halaman pada footer tabel.
- State global yang diubah: Page size, nomor halaman, Search, dan Filter pada tabel (dikembalikan oleh langkah di spec dan oleh `beforeEach` suite); 17 class tambahan (dihapus hook `after`).

## Test Steps

### Pagination default 10 per halaman dan pilihan page size (TC-FA-TDC-554)

1. Verifikasi halaman 1 menampilkan 10 baris (BLD-NP sampai NB-SL dan TDC-01)
2. Buka Overlay Page Size
3. Verifikasi Overlay Page Size memuat opsi `10`, `25`, `50`, `100` tanpa opsi All
4. Pilih `25`
5. Verifikasi 25 baris tampil di halaman 1 (TDC-16 di baris ke-25)
6. Buka Overlay Page Size
7. Pilih `100`
8. Verifikasi seluruh 26 baris tampil dalam satu halaman

### Navigasi halaman: berikutnya, sebelumnya, dan input nomor halaman (TC-FA-TDC-555)

9. Buka Overlay Page Size
10. Pilih `10`
11. Klik navigasi halaman berikutnya
12. Verifikasi halaman 2 menampilkan TDC-02 sampai TDC-11
13. Klik navigasi halaman sebelumnya
14. Verifikasi kembali ke halaman 1
15. Ketik `3` pada input nomor halaman, tekan Enter
16. Verifikasi halaman 3 menampilkan TDC-12 sampai TDC-17 (6 baris)

### Input nomor halaman tidak valid diabaikan (TC-FA-TDC-556)

17. Pindah ke halaman 2
18. Ketik `0` pada input nomor halaman, tekan Enter
19. Verifikasi tabel tetap di halaman 2 dan input diabaikan
20. Ketik `99` pada input nomor halaman, tekan Enter
21. Verifikasi tabel tetap di halaman 2 dan input diabaikan
22. Ketik `abc` pada input nomor halaman, tekan Enter
23. Verifikasi tabel tetap di halaman 2 dan input diabaikan

### Mengganti page size kembali ke halaman 1 (TC-FA-TDC-557)

24. Pindah ke halaman 3
25. Ganti page size menjadi `25`
26. Verifikasi tabel pindah ke halaman 1 dengan 25 baris

### Search atau Apply Filter saat di halaman lebih dari 1 kembali ke halaman 1 (TC-FA-TDC-558)

27. Ganti page size menjadi `10`
28. Pindah ke halaman 2
29. Ketik Search `TDC`, tekan Enter
30. Verifikasi setelah Search tabel menampilkan halaman 1 (TDC-01 sampai TDC-10)
31. Pindah ke halaman 2
32. Klik icon Filter
33. Pilih Asset Type `Building`
34. Klik `[Apply]`
35. Verifikasi setelah Apply Filter tabel kembali ke halaman 1
36. Pindah ke halaman 2
37. Klik `✕` pada Search, tekan Enter
38. Verifikasi setelah Search dikosongkan tabel kembali ke halaman 1
39. Klik `Clear all` pada chip filter

## Notes

- Langkah penghubung (S-03, S-09): langkah 9 dan 10 (mengembalikan page size ke 10 sesudah TC-FA-TDC-554 memilih 100, supaya TC-FA-TDC-555 mulai dari 10 baris per halaman), langkah 27 (mengembalikan page size ke 10 sesudah langkah 25), langkah 36 (pindah ke halaman 2 sebelum mengosongkan Search, supaya asersi "kembali ke halaman 1" pada langkah 38 bermakna; S-14; TC tidak memuat langkah ini), langkah 39 (melepas Filter di akhir spec). Langkah 37 mengikuti TC-FA-TDC-558 langkah 5 ("Kosongkan Search lalu Enter") dengan cara mengosongkan "klik `✕` pada Search, tekan Enter" (8b.9).
- Spec ini 39 langkah, di atas ~35 langkah. Alasan: satu topik (Pagination tabel utama) pada dataset 26 class yang sama untuk kelima TC, tiap blok TC berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan S-01 mengharuskan satu `Verifikasi` per klausa.
- Temuan untuk QA:
  - Class Code maksimal 15 karakter: suffix `{runId}-<NNN>` (S-12) tidak muat, jadi kode `TDC-01` sampai `TDC-17` memakai literal TC dengan syarat seeding idempotent, cleanup oleh spec, dan suite serial. Kode yang sama dipakai spec 146, 152, dan 158; Lampiran A belum punya butir modul ini.
  - TC-FA-TDC-558 langkah 5 mengosongkan Search sesudah langkah 4 sudah kembali ke halaman 1, sehingga Expected c ("kembali ke halaman 1") lulus tanpa menguji; spec menambah langkah "Pindah ke halaman 2" sebelumnya.
  - TC-FA-TDC-556 Expected menyatakan "pada ketiga input tidak valid" dalam satu butir; spec mengasersinya setelah tiap input (S-01).
  - TC-FA-TDC-555 dan 557 tidak menyebut page size yang dipakai saat TC mulai (sisa TC sebelumnya); spec memulihkannya ke 10 lewat langkah penghubung.
  - Email akun Total Control tidak tertulis di TC.
