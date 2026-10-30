---
id: TC-GS-ACTLOG-E2E-046-pagination-page-size-navigasi-dan-reset-halaman-kedua-tab
title: "Pagination Kedua Tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-118
  - TC-GS-ACTLOG-119
  - TC-GS-ACTLOG-120
coverage:
  web: automated
---

# Pagination Kedua Tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (seed BE bersuffix `{runId}-046`, disediakan tim FE/BE; log bersifat append-only sehingga tidak dihapus dan spec tidak mengubahnya). N total diturunkan dari seeding:
  - Tab Session dan Tab User Action masing-masing memuat 100 baris atau lebih (TC-GS-ACTLOG-118) dan lebih dari 30 baris (TC-GS-ACTLOG-119 dan 120).
  - Hasil Search `a` memuat lebih dari 10 baris pada kedua tab (TC-GS-ACTLOG-120).
  - Irisan Search `a` dengan Activity `Login` (Tab Session) dan irisan Search `a` dengan Action `Edit` (Tab User Action) masing-masing memuat lebih dari 10 baris, sehingga halaman 2 tersedia sesudah Filter diterapkan saat Search `a` aktif (TC-GS-ACTLOG-120).
  - Kata Search `a` ditulis literal sesuai TC karena asersi berupa nomor halaman, bukan isi baris.
- Kemampuan teknis (disediakan tim FE/BE): seed BE volume 100 baris atau lebih per tab; volume tersebut tidak dapat dihasilkan lewat aksi nyata modul sumber dalam satu run.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- State global yang diubah: tidak ada di backend. State page size, halaman, Search, dan Filter tiap tab dibersihkan lewat langkah pemulihan dengan klik ulang menu sidebar Activity Log. Spec tidak membuat atau mengubah data backend. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ACTLOG-118: Pilihan page size 25, 50, 100 menampilkan jumlah baris sesuai

1. Buka Global Settings > Activity Log > Tab "Session" dengan page size `10`, lalu ubah page size ke `25`
2. Verifikasi Tab Session menampilkan tepat 25 baris
3. Ubah page size ke `50`
4. Verifikasi Tab Session menampilkan tepat 50 baris
5. Ubah page size ke `100`
6. Verifikasi Tab Session menampilkan tepat 100 baris
7. Buka pilihan page size Tab Session
8. Verifikasi opsi `10`, `25`, `50`, dan `100` tampil pada pilihan page size Tab Session
9. Verifikasi opsi `All` tidak ada pada pilihan page size Tab Session
10. Pilih opsi `10` sehingga page size Tab Session kembali ke `10`
11. Klik tab "User Action", lalu ubah page size ke `25`
12. Verifikasi Tab User Action menampilkan tepat 25 baris
13. Ubah page size ke `50`
14. Verifikasi Tab User Action menampilkan tepat 50 baris
15. Ubah page size ke `100`
16. Verifikasi Tab User Action menampilkan tepat 100 baris
17. Buka pilihan page size Tab User Action
18. Verifikasi opsi `10`, `25`, `50`, dan `100` tampil pada pilihan page size Tab User Action
19. Verifikasi opsi `All` tidak ada pada pilihan page size Tab User Action
20. Pilih opsi `10` sehingga page size Tab User Action kembali ke `10`

### Pemulihan state antar TC

21. Klik menu Activity Log di sidebar sehingga kedua tab kembali ke default

### TC-GS-ACTLOG-119: Navigasi halaman lewat tombol dan input nomor halaman

22. Pada Tab Session (page size 10) klik halaman berikutnya
23. Verifikasi halaman 2 tampil di Tab Session
24. Klik halaman sebelumnya
25. Verifikasi halaman 1 tampil di Tab Session
26. Ketik `3` pada input nomor halaman lalu tekan Enter
27. Verifikasi halaman 3 tampil di Tab Session
28. Klik tab "User Action", lalu klik halaman berikutnya
29. Verifikasi halaman 2 tampil di Tab User Action
30. Klik halaman sebelumnya
31. Verifikasi halaman 1 tampil di Tab User Action
32. Ketik `3` pada input nomor halaman lalu tekan Enter
33. Verifikasi halaman 3 tampil di Tab User Action

### Pemulihan state antar TC

34. Klik menu Activity Log di sidebar sehingga kedua tab kembali ke default

### TC-GS-ACTLOG-120: Search atau Apply Filter saat berada di halaman 2 mengembalikan ke halaman 1

35. Pada Tab Session (page size 10) buka halaman 2, ketik Search `a`, tekan Enter
36. Verifikasi halaman aktif kembali ke halaman 1 setelah Search di Tab Session
37. Buka halaman 2, klik icon Filter, pilih Activity `Login`, klik [Apply]
38. Verifikasi halaman aktif kembali ke halaman 1 setelah Apply Filter di Tab Session
39. Klik tab "User Action", buka halaman 2, ketik Search `a`, tekan Enter
40. Verifikasi halaman aktif kembali ke halaman 1 setelah Search di Tab User Action
41. Buka halaman 2, klik icon Filter, pilih Action `Edit`, klik [Apply]
42. Verifikasi halaman aktif kembali ke halaman 1 setelah Apply Filter di Tab User Action

### Pemulihan state akhir

43. Klik menu Activity Log di sidebar sehingga kedua tab kembali ke default

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md`. Urutan TC-GS-ACTLOG-118, 119, 120 dipertahankan. Kelas harness e (volume data): seed 100 baris atau lebih per tab.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 7 dan 17 (membuka pilihan page size untuk mengamati opsi), langkah 10 dan 20 (mengembalikan page size ke `10` sesuai langkah TC-118), serta langkah pemulihan 21, 34, dan 43.
- Asersi absence opsi `All` (langkah 9 dan 19) didahului `Verifikasi` opsi `10`, `25`, `50`, `100` tampil pada pilihan yang sama (langkah 8 dan 18); kedua langkah anchor itu adalah asersi tambahan di luar Expected TC (S-03).
- Spec di atas smell 35 langkah (43 langkah nominal, tanpa perulangan). Alasan: ketiga blok berada pada satu kelas harness (volume data) dengan dataset yang sama, tiap blok dimulai dari state default hasil klik ulang menu dan berdiri sendiri; langkah terbanyak berasal dari `Verifikasi` per jumlah baris dan per halaman untuk dua tab (S-01).
- Temuan untuk QA:
  - Kolom Data Uji TC-120 hanya memuat `Search: a`; nilai Filter Activity `Login` dan Action `Edit` hanya tertulis di Langkah Uji dan dipakai apa adanya.
  - TC-120 Precondition tidak menyebut irisan Search `a` dengan Filter; spec menetapkan irisan itu lebih dari 10 baris di Prerequisites.
  - TC-118 menyebut page size default `10` tetapi tidak menyebut cara memverifikasi opsi `All` selain "tidak ada"; spec membuka pilihan page size untuk mengamati opsi.
  - Post Condition semua TC bernilai `-`; tidak diasersi.
