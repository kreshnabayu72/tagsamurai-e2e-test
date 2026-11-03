---
id: TC-FA-FAAL-E2E-067-search-siklus-enter-clear-collapse-kedua-tab
title: "Search: Siklus Submit Enter, Clear, dan Collapse di Tab Session dan Tab User Action"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-58
coverage:
  web: automated
---

# Search: Siklus Submit Enter, Clear, dan Collapse di Tab Session dan Tab User Action

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (butir "Env var" di `suite.md`); password tidak ditulis di spec atau fixture.
- Data: Tab Session SS-01 sampai SS-11 (Pre-setup #11); baris dipakai SS-06 (User `Budi S`, hasil Search `Budi`). Tab User Action UA-01 sampai UA-15 (Pre-setup #12) pada tanggal 18/06/26; baris dipakai UA-01 (Name `Budi Santoso`, hasil Search `Santoso`). Spec hanya membaca dan tidak mengubah data.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan data Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-58: Siklus interaksi Search di kedua tab: submit Enter, clear, dan collapse (Tab Session)

1. Klik icon Filter
2. Pilih tanggal mulai `14/07/26` dan tanggal akhir `16/07/26` pada field Date
3. Klik `[Apply]`
4. Klik icon Search, ketik `Budi` tanpa menekan Enter
5. Verifikasi icon `(✕)` muncul pada input Search
6. Verifikasi tabel belum tersaring: teks pagination `Showing 1–10 of 11 entries`
7. Tekan Enter
8. Verifikasi hanya SS-06 tampil
9. Klik icon `(✕)` pada input
10. Verifikasi input Search kosong
11. Verifikasi kursor tetap fokus di dalam input Search
12. Verifikasi tabel tetap menampilkan hasil SS-06 saja
13. Tekan Enter pada input kosong
14. Verifikasi tabel kembali menampilkan 11 baris: teks pagination `Showing 1–10 of 11 entries`
15. Ketik `Budi` pada input, tekan Enter
16. Klik icon `(←)` di kiri toolbar
17. Verifikasi kotak pencarian menutup menjadi icon Search
18. Verifikasi keyword Search kosong
19. Verifikasi tabel langsung kembali ke 11 baris: teks pagination `Showing 1–10 of 11 entries`

### TC-FA-FAAL-58: Siklus interaksi Search di kedua tab (Tab User Action)

20. Klik tab User Action
21. Klik icon Filter
22. Pilih tanggal mulai `18/06/26` dan tanggal akhir `18/06/26` pada field Date
23. Klik `[Apply]`
24. Klik icon Search, ketik `Santoso` tanpa menekan Enter
25. Verifikasi icon `(✕)` muncul pada input Search
26. Verifikasi tabel belum tersaring: teks pagination `Showing 1–10 of 15 entries`
27. Tekan Enter
28. Verifikasi hanya UA-01 (Name `Budi Santoso`) tampil
29. Klik icon `(✕)` pada input
30. Verifikasi input Search kosong
31. Verifikasi kursor tetap fokus di dalam input Search
32. Verifikasi tabel tetap menampilkan hasil UA-01 saja
33. Tekan Enter pada input kosong
34. Verifikasi tabel kembali menampilkan 15 baris: teks pagination `Showing 1–10 of 15 entries`
35. Ketik `Santoso` pada input, tekan Enter
36. Klik icon `(←)` di kiri toolbar
37. Verifikasi kotak pencarian menutup menjadi icon Search
38. Verifikasi keyword Search kosong
39. Verifikasi tabel langsung kembali ke 15 baris: teks pagination `Showing 1–10 of 15 entries`

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): langkah 1 sampai 3 dan 21 sampai 23 (menerapkan Filter Date Jendela Seed pada tiap tab sesuai precondition d TC-FA-FAAL-58). Blok Tab User Action mengulang langkah 1 sampai 5 TC-FA-FAAL-58 secara eksplisit (S-04) dengan keyword `Santoso`.
- Ukuran spec 39 langkah, di atas 35 langkah: satu TC (TC-FA-FAAL-58) menjadi satu-satunya sumber; Expected TC-FA-FAAL-58 butir a sampai e dipecah per klausa (S-01) dan diulang eksplisit di dua tab (S-04, 2 × 16 langkah), ditambah dua kali penerapan Filter Date Jendela Seed (6 langkah); satu TC tidak dipecah ke spec lain.
- Jumlah 15 baris Tab User Action diambil dari Pre-setup #12 (UA-01 sampai UA-15) dan TC-FA-FAAL-73; TC-FA-FAAL-58 sendiri tidak menyebut jumlahnya.
- Temuan untuk QA:
  - Pre-setup #11 menyebut tepat 11 baris Tab Session (dan #12 tepat 15 baris Tab User Action) tanpa menyatakan bahwa login aktor (dan spec lain pada client yang sama) menambah baris `Session started` pada log permanen. Asersi hitungan (`Showing 1–10 of 11 entries`, 15 baris) hanya benar bila data Pre-setup berada di client yang terisolasi dari login lain; spec mengikuti TC.
  - TC-FA-FAAL-58 Expected f ("perilaku pada langkah 1 sampai 5 identik") tidak menyebut jumlah baris Tab User Action sebelum Search; spec memakai 15 dari Pre-setup #12.
  - TC-FA-FAAL-58 Expected a, c, dan e memuat beberapa klausa dalam satu butir; spec memecahnya per klausa (S-01).
