---
id: TC-GS-BRAND-E2E-071-resilience-hapus-single-bulk-dan-cek-referensi
title: "Resilience Hapus Brand: Cek Referensi Gagal, Delete Gagal, dan Bulk Delete Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-BRAND-104
  - TC-GS-BRAND-105
  - TC-GS-BRAND-124
  - TC-GS-BRAND-258
coverage:
  web: automated
---

# Resilience Hapus Brand: Cek Referensi Gagal, Delete Gagal, dan Bulk Delete Gagal

## Prerequisites

- Mode: FE+BE dengan intercept parsial di atas backend nyata (bagian 6 konvensi).
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > Master Reference > Brand.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (tetap di environment, tidak terhapus karena semua aksi hapus dipaksa gagal, tanpa suffix `{runId}`): `Orion Tech` dan `Brightway` (keduanya bebas relasi).
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi), di-seed lewat API di hook `before`: `Wisp Co {runId}-071` dan `Yew Co {runId}-071` (D-25), bebas relasi, untuk TC-GS-BRAND-124.
- Kebutuhan intercept (`Spectra.intercept()`), semuanya pada request ke endpoint Brand dan dilepas setelah dipakai:
  - respons cek referensi Brand (Check References, single dan bulk) dipaksa HTTP 500;
  - respons cek referensi Brand dipaksa timeout;
  - respons Delete Brand single dipaksa HTTP 500;
  - respons Bulk Delete Brand dipaksa HTTP 500.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): lepaskan semua intercept; hapus lewat API `Wisp Co {runId}-071` dan `Yew Co {runId}-071`.
- State global yang diubah: page size Pagination (diubah ke 25 di langkah 1, dikembalikan ke 10 di langkah 33; hook `after` menjadi cadangan). Tidak ada state global lain yang diubah.
- TC-GS-BRAND-104, 105, 124, 258: login sebagai Total Control dan berada di Global Settings > Master Reference > Brand.

## Test Steps

### TC-GS-BRAND-104: Cek referensi gagal (5xx dan timeout) saat klik Delete

1. Ubah page size Pagination menjadi 25 sehingga seluruh brand Client A tampil dalam satu halaman
2. Paksa respons cek referensi HTTP 500 (intercept)
3. Klik `⋯` pada baris Orion Tech > Delete
4. Verifikasi toast error "Error, failed to check brand references."
5. Verifikasi dialog Delete tidak tampil
6. Lepas intercept 500, paksa timeout pada respons cek referensi (intercept)
7. Klik `⋯` pada baris Orion Tech > Delete lagi
8. Verifikasi toast "Connection problem. Please try again." dengan `[Try Again]`
9. Verifikasi dialog Delete tidak tampil

### TC-GS-BRAND-258: Cek referensi gagal (5xx dan timeout) saat klik Bulk Delete

10. Lepas intercept timeout, paksa respons cek referensi HTTP 500 (intercept)
11. Centang Orion Tech dan Brightway
12. Klik `Bulk Action` > `Delete`
13. Verifikasi toast error "Error, failed to check brand references."
14. Verifikasi dialog Delete tidak tampil
15. Lepas intercept 500, paksa timeout pada respons cek referensi (intercept), pastikan Orion Tech dan Brightway masih tercentang
16. Klik `Bulk Action` > `Delete`
17. Verifikasi toast "Connection problem. Please try again." dengan `[Try Again]`
18. Verifikasi dialog Delete tidak tampil
19. Verifikasi Orion Tech dan Brightway tetap ada di tabel

### TC-GS-BRAND-105: Delete gagal 5xx

20. Lepas intercept timeout, hapus pilihan centang, paksa respons Delete Brand HTTP 500 (intercept)
21. Klik `⋯` pada baris Orion Tech > Delete → dialog `Delete Brand` tampil
22. Klik [Delete]
23. Verifikasi toast error: "Error, failed to delete brand."
24. Verifikasi Orion Tech tetap di tabel

### TC-GS-BRAND-124: Bulk Delete gagal 5xx tidak menghapus apa pun

25. Lepas intercept Delete single, paksa respons Bulk Delete HTTP 500 (intercept)
26. Search `{runId}-071` pada tabel Brand
27. Centang `Wisp Co {runId}-071` dan `Yew Co {runId}-071`
28. Klik `Bulk Action` > `Delete`
29. Klik [Delete]
30. Verifikasi toast error: "Error, failed to delete brand."
31. Verifikasi `Wisp Co {runId}-071` dan `Yew Co {runId}-071` tetap ada
32. Kosongkan Search
33. Kembalikan page size Pagination ke 10

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`. Kelas fault injection (prinsip 13b) dengan intercept parsial di atas backend nyata; hanya request browser yang di-intercept, sehingga bukan `Mode: mock`.
- Urutan TC di spec berbeda dari urutan sumber: kegagalan cek referensi single (104) dan bulk (258) berurutan karena intercept yang sama, lalu Delete single (105) dan Bulk Delete (124); semua dipaksa gagal sehingga tidak ada data yang benar-benar terhapus.
- Brand `Orion Tech` dan `Brightway` adalah Pre-setup dan tidak berubah; `Wisp Co` dan `Yew Co` diberi suffix `{runId}-071` dan dibersihkan di hook `after`.
- Spec sekitar 33 langkah dan hanya satu kelas harness (fault injection).
- Langkah penghubung: langkah 6, 10, 15, 20, dan 25 (melepas intercept yang aktif dan memasang intercept berikutnya) serta bagian "hapus pilihan centang" pada langkah 20 tidak tertulis di Langkah Uji TC sumber. Langkah 1 dan 33 (page size 25 sekali supaya Orion Tech dan Brightway terlihat dalam satu halaman dan dapat dicentang bersama, lalu dipulihkan) serta langkah 26 dan 32 (Search `{runId}-071` supaya Wisp Co dan Yew Co berada di tabel yang terlihat, lalu mengosongkan Search) juga tidak tertulis di TC sumber.
