---
id: TC-FA-GRP-E2E-081-bulk-seleksi-persist-lintas-halaman-search-filter-dan-reset-saat-node-berganti
title: "Bulk Seleksi: Persist Lintas Halaman/Search/Filter, Dipertahankan di Node yang Sama dan Direset Saat Node Berganti, dan Retensi Saat Search/Filter Dikosongkan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-251
  - TC-FA-GRP-426
  - TC-FA-GRP-982
coverage:
  web: automated
---

# Bulk Seleksi: Persist Lintas Halaman/Search/Filter, Dipertahankan di Node yang Sama dan Direset Saat Node Berganti, dan Retensi Saat Search/Filter Dikosongkan

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control (Pre-setup No 1: `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed lewat API di `before`): 12 group level 1 kosong `Bulk K01` sampai `Bulk K12` (nama distinct, semuanya memuat huruf `K`) sehingga tabel memuat lebih dari satu halaman (page size default 10). N = jumlah total baris tabel Groups List pada tampilan All Groups (Pre-setup level 1 ditambah 12 group seed), dibaca lewat fixture BE sebelum uji dan bukan dari satu halaman tabel (8b butir 10).
- Data Dinamis tambahan (untuk TC-982): `Head Office` Pre-setup memiliki child Pre-setup; di bawah `Head Office` spec men-seed `HO Kid 1`, `HO Kid 2`, `HO Kid 3` (kosong, memuat huruf `K`) sehingga minimal tiga child. `Warehouse A` (Pre-setup) hanya dibaca sebagai node sidebar lain.
- Cleanup di `after`: hapus data seed lewat API.

## Test Steps

### TC-FA-GRP-251: Seleksi persist lintas halaman dan search

1. Centang baris 1 dan baris 2 pada halaman 1
2. Klik tombol halaman 2, lalu centang 1 baris
3. Verifikasi counter `3 groups selected`
4. Ketik Search `K`, tekan Enter
5. Verifikasi counter `3 groups selected` (ketiga baris tetap tercentang saat search aktif)
6. Klik `(←)` pada kotak Search
7. Verifikasi counter `3 groups selected` (ketiga baris tetap tercentang setelah search dikosongkan)
8. Klik (X)

### TC-FA-GRP-426: Retensi centang saat search dikosongkan

9. Ketik Search `K`, tekan Enter
10. Centang 1 baris
11. Klik `(←)` pada kotak Search
12. Verifikasi baris yang dicentang tetap tercentang
13. Verifikasi counter tetap `1 group selected`
14. Klik (X)

### TC-FA-GRP-982: Seleksi dipertahankan di node yang sama dan direset saat node berganti

15. Klik `Head Office` di sidebar
16. Centang 2 baris
17. Ketik Search `K`, tekan Enter
18. Klik `(←)` pada kotak Search
19. Verifikasi kedua baris tetap tercentang (node sidebar sama)
20. Klik `Warehouse A` di sidebar, lalu klik `Head Office` di sidebar
21. Verifikasi tidak ada baris tercentang
22. Verifikasi Bulk Action Bar hilang
23. Centang 1 baris
24. Klik `All Groups`
25. Verifikasi seleksi direset (tidak ada baris tercentang)
26. Verifikasi Bulk Action Bar hilang

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 8, 14: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Search untuk menemukan atau menyaring baris dicatat sebagai langkah penghubung (R-16); `(←)` pada kotak Search mengosongkan Search dan mereset tabel (8b butir 9).
- TC-982 Langkah 3 menyebut "search lalu clear, atau pindah halaman"; spec memakai jalur search lalu clear karena child `Head Office` hanya tiga baris (satu halaman).
- Temuan untuk QA:
  - TC-251 Langkah 4 "Search K" tidak menyebut baris mana yang cocok; spec memakai dataset yang seluruh namanya memuat `K`, sehingga search tidak menyaring baris tercentang.
  - TC-251 dan TC-426 menyebut Filter pada judul tetapi Langkah hanya memakai Search; Filter tidak diasersi.
