---
id: TC-GS-BRAND-E2E-002-isi-sel-brand-name-used-by-dan-last-updated
title: "Isi Sel Tabel Brand: Used By (Items), Brand Name Link, dan Nama Panjang"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-8
  - TC-GS-BRAND-267
  - TC-GS-BRAND-261
  - TC-GS-BRAND-11
  - TC-GS-BRAND-12
coverage:
  web: automated
---

# Isi Sel Tabel Brand: Used By (Items), Brand Name Link, dan Nama Panjang

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A). Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup Client A (data environment tetap, tanpa suffix; hanya dibaca): Orion Tech (bebas relasi, Used By 0), Acme Corp (FAMS Asset Name: Forklift, Used By 1), Duo Brand (FAMS: Router; Supply: Cable, Used By 2), Kestrel (FAMS: Laptop; Supply: Laptop, Used By 2), Vertex Labs (Used By 5). Total Pre-setup Client A 12 brand.
- Data Dinamis D-03: brand dengan Brand Name tepat 120 karakter, di-seed lewat API di hook `before` (setara TC-GS-BRAND-44) dan dihapus lewat API di hook `after`. Nama = bagian dasar dipotong + suffix ` {runId}-002` sehingga panjang total tepat 120 karakter. Nama utuh disimpan di fixture `fixtures/brand.json`, kunci `brandLongName002` (belum ada, disiapkan tim FE; nilai dibangun saat seeding). Pembersihan tidak berasumsi seeding berhasil penuh.
- Total brand pada tabel selama spec: 13 (12 Pre-setup + D-03), sehingga satu halaman berukuran 25 memuat semuanya.
- Guided Tooltip: hook `before` mencatat nilai awal flag `guided_tooltip_seen_gs-brand` lalu menyetelnya ke true lewat API; hook `after` memulihkan nilai awal.
- Kemampuan teknis: hover pada sel tabel dan teks Brand Name (untuk TC-GS-BRAND-11 dan TC-GS-BRAND-12).
- State global yang diubah: flag Guided Tooltip (dipulihkan seperti di atas) dan page size Pagination (diubah ke 25 di langkah 2, dikembalikan ke 10 di langkah 30; hook `after` menjadi cadangan).

## Test Steps

### TC-GS-BRAND-8: Variasi isi sel Used By (Items): 0, 1, 2, dan 5

1. Buka Global Settings > Master Reference dari sidebar → tab Brand tampil
2. Ubah page size Pagination menjadi 25 sehingga seluruh 13 brand tampil dalam satu halaman
3. Perhatikan sel Used By (Items) baris Orion Tech, Acme Corp, Duo Brand, dan Vertex Labs
4. Verifikasi Orion Tech menampilkan `0` (bukan `—`)
5. Verifikasi Acme Corp menampilkan `1`
6. Verifikasi Duo Brand menampilkan `2`
7. Verifikasi Vertex Labs menampilkan `5`
8. Verifikasi seluruh sel Used By (Items) pada keempat baris hanya berisi angka tanpa chip atau `+N More`

### TC-GS-BRAND-267: Nilai 0 pada Used By (Items) tampil `0`

9. Perhatikan sel Used By (Items) baris Orion Tech
10. Verifikasi sel menampilkan `0`
11. Verifikasi sel bukan `—`

### TC-GS-BRAND-11: Klik teks Brand Name membuka Modal Brand Detail

12. Klik teks link `Acme Corp`
13. Verifikasi Modal `Brand Detail` terbuka untuk Acme Corp, sama dengan row action `Detail`
14. Tutup Modal Brand Detail dengan `✕` di header
15. Hover teks `Orion Tech`
16. Verifikasi hover teks Brand Name mengubah warna ke warna primary produk tanpa underline

### TC-GS-BRAND-261: Item Type bernama sama di FAMS dan Supply dihitung dua pada Used By (Items)

17. Perhatikan sel Used By (Items) baris Kestrel
18. Verifikasi sel Kestrel menampilkan `2`
19. Klik header Used By (Items) (ascending)
20. Verifikasi Kestrel berada di kelompok angka 2 bersama Duo Brand
21. Verifikasi kelompok angka 2 berada setelah brand dengan angka 1
22. Klik header Used By (Items) sampai kembali ke urutan default, hapus sort

### TC-GS-BRAND-12: Brand Name sangat panjang tampil utuh tanpa truncate

23. Klik icon Search
24. Ketik nama brand D-03 (Brand Name 120 karakter, kunci `brandLongName002`) lalu tekan Enter
25. Perhatikan sel Brand Name
26. Verifikasi Brand Name tampil utuh (wrap natural), tidak dipotong `..`
27. Hover sel Brand Name
28. Verifikasi tidak ada tooltip hover pada Brand Name
29. Hapus keyword Search sehingga tabel kembali menampilkan 13 brand
30. Kembalikan page size Pagination ke 10

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah: TC-GS-BRAND-11 (klik Brand Name dan hover) ditaruh sebelum TC-GS-BRAND-261 karena TC-GS-BRAND-261 mengubah sort, sehingga posisi baris Orion Tech dan Acme Corp tetap bisa dicari dengan urutan default A-Z. TC-GS-BRAND-12 (Search) paling akhir karena Search mengubah dataset tampilan.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 2 (page size 25 sekali supaya seluruh brand terlihat tanpa menelusuri halaman), 14 (tutup Modal Brand Detail), 22 (hapus sort), 27 (hover sel sebagai cara memeriksa Expected b TC-GS-BRAND-12 "tidak ada tooltip hover"), 29 (kosongkan Search), 30 (pulihkan page size).
- TC-GS-BRAND-8 dan TC-GS-BRAND-267 sama-sama memverifikasi Orion Tech bernilai `0`; keduanya dipertahankan sebagai langkah terpisah supaya traceability per TC tetap utuh.
- TC-GS-BRAND-12 punya dependensi TC-GS-BRAND-44 (membuat D-03); di spec ini D-03 di-seed lewat API di hook `before`, tidak menumpang spec lain. Kebutuhan fixture `brandLongName002` sudah dicatat di Prerequisites.
