---
id: TC-FA-FAAC-E2E-119-filter-lepas-draft-kolom-dan-kombinasi
title: "Filter Tabel Asset Class: Draft Filter Panel, Hasil Kosong, Ganti Sort, dan Filter pada Kolom yang Disembunyikan"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-379
  - TC-FA-FAAC-380
  - TC-FA-FAAC-381
  - TC-FA-FAAC-382
coverage:
  web: automated
---

# Filter Tabel Asset Class: Draft Filter Panel, Hasil Kosong, Ganti Sort, dan Filter pada Kolom yang Disembunyikan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ (Heavy Equipment), VEHICLES, IT-EQ (IT Equipment), MACHINERY (Commercial Method Units of Production, Active), BLDG, STORAGE (Storage Equipment), OFFICE-NEW (Office Equipment (New)), LAND (Active) dan OFFICE-OLD (Office Equipment (Legacy), Inactive). Search `equip` mencocokkan HEAVY-EQ, IT-EQ, OFFICE-NEW, OFFICE-OLD, dan STORAGE. Seed disediakan tim FE/BE (lihat `suite.md`).
- State yang diubah spec: konfigurasi kolom tabel (kolom Commercial disembunyikan lalu ditampilkan kembali oleh langkah 34 dan 35). Pemulihan cadangan di hook `after` dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE; lihat `suite.md`).
- Populasi tabel nyata: tabel Asset Class memuat lebih dari 25 baris (sembilan kelas contoh ditambah seed lain seperti `B-*`, `PMP-01`, `B-PAGE01` sampai `B-PAGE11`, `TEMP-EQ`, dan seed spec lain), sehingga sembilan kelas contoh tidak dijamin berada bersama pada halaman 1 dan baris seed lain dapat menyela atau ikut tampil. Asersi spec ini dibatasi pada keanggotaan dan urutan RELATIF antar baris contoh (atau pada baris yang dikenali lewat Search kode); baris seed lain tidak diasersi.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-381: Tutup Filter Panel tanpa Apply membuang draft

1. Klik icon Filter untuk membuka Filter Panel
2. Pilih Active = Active, klik `[Apply]`
3. Klik icon Filter untuk membuka Filter Panel
4. Pilih Commercial Method = Straight Line (tanpa Apply)
5. Klik di luar panel untuk menutup
6. Verifikasi tabel tetap tersaring Active tanpa saringan Commercial Method
7. Klik icon Filter untuk membuka Filter Panel
8. Verifikasi panel menampilkan hanya nilai ter-Apply terakhir (Active = Active) tanpa Straight Line

### TC-FA-FAAC-380: Hasil kosong lalu pulih saat salah satu saringan dilepas

9. Ketik Search `machinery`, tekan Enter
10. Klik icon Filter untuk membuka Filter Panel
11. Pilih Active = Inactive, klik `[Apply]`
12. Verifikasi empty state dengan title `No results found` dan description `Try adjusting your search or filter.` tanpa tombol aksi
13. Verifikasi chip filter Active dan Clear all tetap tersedia di atas tabel
14. Klik Clear all
15. Verifikasi tabel pulih menampilkan baris MACHINERY

### TC-FA-FAAC-379: Ganti kolom sort saat Search dan Filter aktif

16. Ganti isi kotak search dengan `equip`, tekan Enter
17. Klik icon Filter untuk membuka Filter Panel
18. Pilih Active = Active, klik `[Apply]`
19. Klik header Class Name
20. Klik header Class Code
21. Verifikasi sort berpindah ke Class Code
22. Verifikasi indikator sort Class Name hilang
23. Verifikasi Search `equip` tetap aktif
24. Verifikasi filter Active tetap aktif

### TC-FA-FAAC-382: Filter tetap tersedia dan tetap berlaku saat kolom disembunyikan

25. Klik Clear all
26. Klik icon `←` pada kotak Search
27. Klik icon Filter untuk membuka Filter Panel
28. Pilih Commercial Method = Units of Production, klik `[Apply]`
29. Sembunyikan kolom Commercial lewat Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`, hilangkan centang Commercial)
30. Klik `[Save]`
31. Klik icon Filter untuk membuka Filter Panel
32. Verifikasi tabel tetap tersaring: baris MACHINERY tampil dan baris contoh lain (HEAVY-EQ) tidak tampil; baris seed lain bermetode Units of Production tidak diasersi
33. Verifikasi field Commercial Method tetap ada di Filter Panel dengan nilai Units of Production
34. Tampilkan kembali kolom Commercial lewat Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`, centang Commercial)
35. Klik `[Save]`
36. Klik Clear all

## Notes

- Urutan TC di dalam spec: TC-FA-FAAC-381, 380, 379, lalu 382 supaya state Search dan Filter yang dibangun TC sebelumnya dipakai ulang dan blok yang mengubah konfigurasi kolom berada di akhir (S-10). Tiap TC tetap memuat semua aksi yang diminta TC-nya.
- Langkah penghubung (S-03): langkah 10 membuka Filter Panel sebelum Apply; langkah 16 menggantikan isi kotak Search dari langkah 9; langkah 25 dan 26 (melepas filter dan menutup Search sebelum TC-FA-FAAC-382, S-09); langkah 34 dan 35 (memulihkan konfigurasi kolom, S-09); langkah 36 (melepas filter di akhir spec, S-09). Search pada langkah 9 menentukan baris target MACHINERY (R-16).
- Klausa "tabel tetap tersaring ... baris contoh lain tidak tampil" pada langkah 32 diasersi dengan satu baris pembanding yang dijamin ada (8b butir 2).
- Hasil Search `equip` dan `machinery` serta Filter Commercial Method diasersi pada keanggotaan baris contoh; baris seed lain yang cocok tidak diasersi.
- Nama literal Pre-setup (sembilan kelas contoh) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis, dan data hanya dibaca (S-06, S-12).
- Temuan untuk QA: tidak ada.
- Spec di atas 35 langkah (36 langkah): empat TC satu topik (Search dan Filter di tabel yang sama) saling memakai state yang dibangun TC sebelumnya; Expected bermajemuk dipecah satu `Verifikasi` per klausa (S-01); memecah lagi menggandakan pembangunan state Search dan Filter tanpa pemisah nyata.
