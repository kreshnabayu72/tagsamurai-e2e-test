---
id: TC-GS-BRAND-E2E-035-search-toolbar-brand-name
title: "Search Toolbar Tabel Brand: Siklus Search dan Pencocokan Brand Name"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-130
  - TC-GS-BRAND-131
  - TC-GS-BRAND-133
  - TC-GS-BRAND-134
  - TC-GS-BRAND-274
coverage:
  web: automated
---

# Search Toolbar Tabel Brand: Siklus Search dan Pencocokan Brand Name

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data brand.
- Akun: Total Control Client A, `Sari Dewi (Sari D)`, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Master Reference > Brand dilakukan sekali di hook `before`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (Last Updated sebelum hari uji): Acme Corp, Brightway, Duo Brand, Helix Works, Kestrel, Lumina Co, Nimbus Gear, Northwind Co, Orion Tech, Tagline Co, Vertex Labs, Zenith Corp. Acme Corp memakai FAMS Asset Name `Forklift`; Vertex Labs memakai Supply `Toner Cartridge`.
- Seeding: Population D-01 (setara TC-GS-BRAND-1) dibuat lewat API di hook `before` dengan 12 nama literal tanpa suffix: Apex Tools, Bolt Systems, Cedar Supply, Delta Instruments, Echo Devices, Falcon Gear, Granite Works, Harbor Tech, Iris Optics, Juniper Labs, Keystone Mfg, Linear Dynamics. Hasilnya total 24 brand. Seeding idempotent: brand yang sudah ada dilewati.
- Suite berjalan serial pada Client A (spec 028, 029, dan 035 memakai nama literal Population D-01 yang sama).
- Cleanup: hook `after` menghapus hanya brand Population D-01 yang dibuat spec ini lewat API tanpa berasumsi seeding berhasil penuh, dan memulihkan visibilitas kolom (Brand Name visible), Search, dan Sort tabel ke default.
- Kemampuan teknis: Column Visibility lewat header kolom Actions (`⋯`); membaca teks sel Last Updated baris Orion Tech.
- TC-GS-BRAND-130, TC-GS-BRAND-131: Pre-setup Client A (12) dan Population D-01 (12) tersedia, total 24 brand.
- TC-GS-BRAND-133 data: teks tanggal Last Updated baris Orion Tech (dibaca dari tabel; format mengikuti General Settings).
- TC-GS-BRAND-134, TC-GS-BRAND-274: data uji `acme`, `forklift`, `toner`.

## Test Steps

### TC-GS-BRAND-130: Siklus Search toolbar: reveal, Enter, clear, Enter kosong, collapse

1. Klik icon Search
2. Verifikasi Search melebar, fokus otomatis di input, dan placeholder `Search brand...`
3. Ketik `tech` di input Search
4. Verifikasi muncul `(✕)` pada input dan tabel belum tersaring (masih 24 brand)
5. Tekan Enter
6. Verifikasi tabel hanya menampilkan Harbor Tech dan Orion Tech
7. Klik `(✕)` pada input Search
8. Verifikasi input kosong dan tabel masih tersaring (Harbor Tech dan Orion Tech)
9. Tekan Enter pada input kosong
10. Verifikasi 24 brand kembali ditampilkan
11. Ketik `tech` di input Search
12. Tekan Enter
13. Klik `(←)`
14. Verifikasi Search tertutup dan tabel langsung reset ke 24 brand

### TC-GS-BRAND-131: Search Brand Name substring dan case-insensitive

15. Klik icon Search
16. Ketik `ORI` di input Search
17. Tekan Enter
18. Verifikasi tabel hanya menampilkan Orion Tech
19. Ganti isi input Search menjadi `ech`
20. Tekan Enter
21. Verifikasi tabel menampilkan Echo Devices, Harbor Tech, dan Orion Tech

### TC-GS-BRAND-133: Search nilai Last Updated tidak mencocokkan baris

22. Baca teks Last Updated pada baris Orion Tech
23. Ganti isi input Search dengan teks tanggal Last Updated tersebut
24. Tekan Enter
25. Verifikasi tabel menampilkan empty state `No results found` (Last Updated hanya disaring lewat Filter, bukan Search)

### TC-GS-BRAND-274: Search tabel utama hanya mencocokkan Brand Name

26. Ganti isi input Search menjadi `forklift`
27. Tekan Enter
28. Verifikasi empty state `No results found` (Item Type tidak dicari)
29. Ganti isi input Search menjadi `toner`
30. Tekan Enter
31. Verifikasi empty state `No results found`
32. Ganti isi input Search menjadi `acme`
33. Tekan Enter
34. Verifikasi tabel menampilkan Acme Corp

### TC-GS-BRAND-134: Kolom Brand Name yang di-hide dikecualikan dari Search

35. Klik `(←)` untuk menutup Search dan mereset tabel
36. Klik header kolom Actions (`⋯`) untuk membuka Overlay Column Visibility
37. Sembunyikan kolom Brand Name
38. Klik icon Search
39. Ketik `acme` di input Search
40. Tekan Enter
41. Verifikasi tidak ada baris cocok: empty state `No results found` dengan teks `Try adjusting your search or filter.`
42. Klik header kolom Actions (`⋯`) untuk membuka Overlay Column Visibility
43. Tampilkan kembali kolom Brand Name
44. Ganti isi input Search menjadi `acme`
45. Tekan Enter
46. Verifikasi Acme Corp ditemukan
47. Klik `(←)` untuk menutup Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-BRAND-134 ditaruh paling akhir (urutan sumber 130, 131, 133, 134, 274) karena mengubah visibilitas kolom (Column Visibility); TC-GS-BRAND-274 dijalankan dulu pada kolom yang masih lengkap.
- Langkah penghubung (aksi tanpa `Verifikasi`): 22 (membaca teks Last Updated baris Orion Tech dari hasil Search `ech` pada langkah 21; TC sumber hanya menyebut "teks tanggal Last Updated baris Orion Tech"), 35 (menutup Search dan mereset tabel sebelum TC-GS-BRAND-134), dan 47 (menutup Search di akhir spec). Langkah 36 dan 42 (membuka Overlay Column Visibility) serta 37 dan 43 (menyembunyikan dan menampilkan kolom Brand Name) menjalankan langkah TC-GS-BRAND-134; langkah 43 sekaligus memulihkan state kolom (hook `after` menjadi cadangan).
- Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
