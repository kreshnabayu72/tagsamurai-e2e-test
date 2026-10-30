---
id: TC-GS-UOM-E2E-005-used-by-items-fixture-khusus-nama-sama-dan-angka-besar
title: "Used By (Items): Item Type Nama Sama di FAMS dan Supply (Tote) dan Angka Besar 1250 (Mass)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-UOM-374
  - TC-GS-UOM-375
coverage:
  web: automated
---

# Used By (Items): Item Type Nama Sama di FAMS dan Supply (Tote) dan Angka Besar 1250 (Mass)

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Nama env didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup dan Population (hanya dibaca): Pre-setup Client A (8 unit, termasuk Box dengan Used By (Items) `4`) dan Population D-01 (12 unit), di-seed idempotent oleh hook `before` sesuai "Data bersama" di `suite.md`.
- Data Dinamis milik spec (disiapkan di hook `before`, dibersihkan di hook `after`), dengan nama bersuffix per run dan spec (S-12):
  - Unit `Tote {runId}-005` / simbol `tt` (D-38) dengan Asset Name FAMS `Crate` dan Item Name Supply `Crate`. Nama `Tote` di TC sumber diganti nama bersuffix.
  - Unit `Mass {runId}-005` / simbol `ms` (D-39) dengan 1250 referensi Asset Name FAMS. Nama `Mass` di TC sumber diganti nama bersuffix.
  - Referensi lintas modul untuk kedua unit disediakan lewat fixture backend yang disediakan tim FE (tanpa endpoint karangan, S-13); pembersihan unit dan referensinya di hook `after` juga disediakan tim FE dan tidak berasumsi seeding berhasil penuh.
- Jumlah total unit N = 22 (20 unit Pre-setup dan Population + `Tote {runId}-005` + `Mass {runId}-005`), diturunkan dari seeding sehingga halaman 3 pada pagination 10 per halaman berisi 2 baris.
- Guided Tooltip: flag halaman Measurement mengikuti pernyataan hook suite di `suite.md`.
- Layar awal (Global Settings > Master Reference > Measurement) dibuka hook `beforeEach` suite.
- State global: tidak ada yang diubah. Sort dikembalikan ke urutan default di langkah 21.

## Test Steps

### TC-GS-UOM-374: Item Type bernama sama di FAMS dan Supply dihitung dua

1. Ketik Search `Tote {runId}-005`, tekan Enter
2. Perhatikan Used By (Items) baris Tote
3. Verifikasi Used By (Items) Tote `2`
4. Klik `⋯` baris Tote > Detail
5. Verifikasi Item Type List menampilkan dua baris `Crate`
6. Verifikasi dua baris `Crate` memiliki Product `Fixed Asset` dan `Supply`
7. Verifikasi Total Item `2`
8. Tutup Modal Unit Detail lewat `[✕]`
9. Klik `(←)` pada kotak Search

### TC-GS-UOM-375: Angka besar tampil apa adanya tanpa pemisah ribuan dan terurut numerik

10. Ketik Search `Mass {runId}-005`, tekan Enter
11. Perhatikan Used By (Items) baris Mass
12. Verifikasi Used By (Items) Mass `1250` tanpa pemisah ribuan
13. Verifikasi Used By (Items) Mass `1250` tidak terpotong
14. Klik `(←)` pada kotak Search
15. Klik header Used By (Items) sekali (ascending)
16. Pindah ke halaman 3 pada Pagination
17. Verifikasi Mass berada setelah Box pada urutan ascending (urutan numerik, bukan leksikografis `1250` sebelum `4`)
18. Klik angka Used By (Items) baris Mass
19. Verifikasi Total Item Modal Unit Detail Mass `1250`
20. Tutup Modal Unit Detail lewat `[✕]`
21. Klik header Used By (Items) dua kali lagi sampai urutan kembali ke default (netral)

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness: volume data khusus berupa fixture backend (referensi lintas modul dan 1250 referensi); dua TC berbagi fixture backend yang sama dan tidak ada kelas lain di spec ini.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 9, 10, dan 14 (Search nama unit untuk menemukan baris dan mengosongkan Search), 8 dan 20 (menutup Modal Unit Detail), 16 (pindah ke halaman 3 tempat Box dan Mass berada pada sort ascending: urutan Used By (Items) ascending dengan tiebreaker Unit Name A-Z menempatkan Box pada posisi 21 dan Mass pada posisi 22 dari N = 22), 21 (mengembalikan sort ke default, state tiga tahap).
- Nama unit bersuffix (`Tote {runId}-005`, `Mass {runId}-005`) menggantikan `Tote` dan `Mass` pada Data Uji TC sumber; asersi memakai nama bersuffix yang sama.
- Temuan untuk QA:
  - TC-GS-UOM-374 dan TC-GS-UOM-375 tidak menyebut mekanisme fixture backend (D-38 dan D-39 hanya "disiapkan lewat fixture backend", NC-09); kebutuhan ini ditulis di Prerequisites sebagai disediakan tim FE.
  - TC-GS-UOM-375 Expected b menyebut urutan "setelah Box" tanpa menyebut halaman; spec menurunkan halaman 3 dari N = 22.
