---
id: TC-AC-DN-E2E-116-kombinasi-search-filter-sort-bagian-1
title: "Kombinasi Search, Filter, Sort, dan Page Size: Irisan dan Clear Field"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-343
  - TC-AC-DN-344
  - TC-AC-DN-345
  - TC-AC-DN-346
coverage:
  web: automated
---

# Kombinasi Search, Filter, Sort, dan Page Size: Irisan dan Clear Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #13 Measurement `Unit`; #15 Brand `Brand B`; #16 Device Name inti beserta SKU-nya (`Gate Antenna` ber-Brand B, `Door Antenna` tanpa SKU); #17 seed 120 baris (Measurement `Unit`). Tidak ada data Dinamis dan tidak ada aksi tulis.
- Nilai data dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE).
- State global: tidak ada yang diubah. Search, Filter, Sort, dan page size dikembalikan ke awal di akhir spec. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-343: Kombinasi Search, Filter, Sort, dan Page Size bekerja bersamaan

1. Ketik Search `a`, tekan Enter
2. Klik ikon Filter, klik field `Measurement`, centang `Unit`, lalu klik `[Apply]`
3. Klik header `Device Name` dua kali (descending)
4. Ubah page size menjadi 25
5. Verifikasi kata kunci `a` tetap terisi di kolom pencarian
6. Klik ikon Filter
7. Verifikasi chip `Unit` ada di Filter Panel
8. Verifikasi sort Device Name descending aktif (panah turun)
9. Verifikasi page size 25 aktif
10. Verifikasi sedikitnya satu baris tampil dan seluruh baris ber-Measurement `Unit` (irisan Search dan Filter)
11. Verifikasi baris diurut Z-A
12. Verifikasi halaman 1 menampilkan maksimal 25 baris
13. Klik `[Clear Field]`, lalu klik `[Apply]`
14. Klik `(←)` pada kotak Search
15. Klik header `Device Name` ketiga kali (netral)
16. Ubah page size menjadi 10

### TC-AC-DN-344: Search lalu Filter menghasilkan irisan dan tidak mereset keyword

17. Ketik Search `Antenna`, tekan Enter
18. Klik ikon Filter, klik field `Brand`, centang `Brand B`, lalu klik `[Apply]`
19. Verifikasi tabel menampilkan 1 baris: Gate Antenna (cocok keyword `Antenna` dan Brand B; Door Antenna tidak punya SKU)
20. Verifikasi kata kunci `Antenna` tetap terisi di kolom pencarian
21. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
22. Klik `(←)` pada kotak Search

### TC-AC-DN-345: Filter lalu Search menghasilkan irisan yang sama

23. Klik ikon Filter, klik field `Brand`, centang `Brand B`, lalu klik `[Apply]`
24. Ketik Search `Antenna`, tekan Enter
25. Verifikasi tabel menampilkan 1 baris: Gate Antenna, identik dengan hasil Search lalu Filter
26. Klik ikon Filter
27. Verifikasi chip `Brand B` tetap ada di Filter Panel
28. Klik `[Clear Field]`, lalu klik `[Apply]`
29. Klik `(←)` pada kotak Search

### TC-AC-DN-346: Clear Field Filter saat Search dan Sort aktif mempertahankan Search dan Sort

30. Ketik Search `Antenna`, tekan Enter
31. Klik header `Device Name` dua kali (descending)
32. Klik ikon Filter, klik field `Brand`, centang `Brand B`, lalu klik `[Apply]`
33. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
34. Verifikasi tabel menampilkan 2 baris: Gate Antenna lalu Door Antenna (Search `Antenna` dan sort descending tetap berlaku)
35. Verifikasi Brand tidak lagi memfilter (ikon Filter tanpa indikator filter aktif)
36. Klik `(←)` pada kotak Search
37. Klik header `Device Name` ketiga kali (netral)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini tanpa aksi tulis.
- Langkah penghubung (S-03, S-09): langkah 13 sampai 16, 21 sampai 22, 28 sampai 29, dan 36 sampai 37 mengembalikan Filter, Search, sort, dan page size ke awal; langkah 6 membuka Filter Panel untuk membaca chip karena panel menutup setelah `[Apply]`.
- Ukuran spec (37 langkah, di atas smell 35 langkah, kode R3): satu topik (kombinasi kontrol List), satu dataset 130 baris baca-saja, satu kelas harness; tiap blok TC memulai dari kontrol yang dikembalikan ke awal sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Urutan: mengikuti sourceTc.
- Temuan untuk QA:
  - Perilaku Filter Panel setelah `[Apply]` tidak konsisten di TC sumber (TC-AC-DN-311 dan TC-AC-DN-312 membuka panel lagi sesudah Apply, TC-AC-DN-314 menutupnya lewat klik ikon); spec mengasumsikan panel menutup setelah `[Apply]`.
  - TC-AC-DN-343 Expected b ("irisan Search dan Filter, diurut Z-A, maksimal 25 baris") tidak menyebut daftar baris; spec mengasersi sifatnya tanpa daftar baris.
