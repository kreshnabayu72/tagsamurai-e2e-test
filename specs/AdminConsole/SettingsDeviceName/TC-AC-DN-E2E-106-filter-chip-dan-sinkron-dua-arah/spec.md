---
id: TC-AC-DN-E2E-106-filter-chip-dan-sinkron-dua-arah
title: "Filter Panel List: Chip, Hapus Chip, Centang Dropdown, +N more, dan Sinkron Dua Arah"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-305
  - TC-AC-DN-306
  - TC-AC-DN-307
  - TC-AC-DN-308
  - TC-AC-DN-637
coverage:
  web: automated
---

# Filter Panel List: Chip, Hapus Chip, Centang Dropdown, +N more, dan Sinkron Dua Arah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #13 Measurement `Unit`, `Meter`, `Box`; #15 Brand (`Brand A`, `Brand B`, `Brand C`, `International Scanner Solutions`); #16 Device Name inti beserta SKU-nya (`Gate Antenna` dan `RFID Reader` ber-Brand B, `RFID Reader` ber-Model R1/R2); #17 seed 120 baris. Tidak ada data Dinamis dan tidak ada aksi tulis.
- Nilai data dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE).
- State global: tidak ada yang diubah. Pilihan filter yang belum di-Apply dibersihkan lewat `[Clear Field]` di akhir tiap blok. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-305: Hapus chip lewat ikon silang menghapus centang opsi

1. Klik ikon Filter di toolbar
2. Klik field `Brand`, centang `Brand A` dan `Brand B`
3. Tutup dropdown `Brand`, lalu klik ikon `(✕)` pada chip `Brand A`
4. Verifikasi chip `Brand A` hilang
5. Verifikasi chip `Brand B` tetap tampil
6. Klik field `Brand`
7. Verifikasi opsi `Brand A` di dalam dropdown tidak tercentang
8. Verifikasi opsi `Brand B` di dalam dropdown tercentang
9. Tutup dropdown `Brand`, lalu klik `[Clear Field]`

### TC-AC-DN-306: Hapus centang opsi menghapus chip

10. Klik field `Brand`, centang `Brand A` dan `Brand B`
11. Dengan dropdown tetap terbuka, hapus centang `Brand A`
12. Verifikasi chip `Brand A` hilang dari field
13. Verifikasi chip `Brand B` tetap tampil
14. Verifikasi opsi `Brand B` masih tercentang di dalam dropdown
15. Tutup dropdown `Brand`, lalu klik `[Clear Field]`

### TC-AC-DN-307: Filter ter-Apply mengikuti opsi yang tersisa setelah chip dihapus

16. Klik field `Brand`, centang `Brand B` dan `International Scanner Solutions`
17. Tutup dropdown `Brand`, lalu klik ikon `(✕)` pada chip `International Scanner Solutions`
18. Klik `[Apply]`
19. Verifikasi tabel menampilkan 2 baris: Gate Antenna dan RFID Reader (hanya Brand B yang tersisa sebagai kriteria)
20. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-DN-308: Chip melebihi lebar field diringkas menjadi `+N more`

21. Klik ikon Filter, klik field `Brand`, centang `Brand A`, `Brand B`, `Brand C`, dan `International Scanner Solutions`
22. Verifikasi field menampilkan chip sebanyak yang muat dan sisanya diringkas dalam satu chip `+N more`, dengan jumlah chip tampil ditambah N sama dengan 4
23. Verifikasi field tidak melebar keluar panel dan tidak digulir horizontal
24. Tutup dropdown `Brand`, lalu klik `[Clear Field]`

### TC-AC-DN-637: Sinkron dua arah chip dan checkbox pada field Model/Type dan Measurement

25. Klik field `Model/Type`, centang `Model R1` dan `Model R2`
26. Tutup dropdown `Model/Type`, lalu klik ikon `(✕)` pada chip `Model R1`
27. Klik field `Model/Type`
28. Verifikasi chip `Model R1` hilang
29. Verifikasi checkbox `Model R1` tidak tercentang
30. Verifikasi chip `Model R2` tetap ada
31. Verifikasi checkbox `Model R2` tercentang
32. Dengan dropdown terbuka, hilangkan centang `Model R2`
33. Verifikasi chip `Model R2` hilang saat checkbox `Model R2` dihilangkan dari dalam dropdown
34. Tutup dropdown `Model/Type`, klik field `Measurement`, centang `Unit` dan `Meter`
35. Tutup dropdown `Measurement`, lalu klik ikon `(✕)` pada chip `Unit`
36. Klik field `Measurement`
37. Verifikasi chip `Unit` hilang
38. Verifikasi checkbox `Unit` tidak tercentang
39. Verifikasi chip `Meter` tetap ada
40. Verifikasi checkbox `Meter` tercentang
41. Dengan dropdown terbuka, hilangkan centang `Meter`
42. Verifikasi chip `Meter` hilang saat checkbox `Meter` dihilangkan dari dalam dropdown
43. Klik `[Apply]`
44. Verifikasi tabel menampilkan 130 baris tanpa kriteria
45. Verifikasi badge titik pada ikon Filter tidak tampil

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini tanpa aksi tulis.
- Langkah penghubung (S-03, S-09): langkah 3, 9, 15, 17, 24, 26, 34, dan 35 menutup dropdown sebelum mengklik chip atau berpindah field, karena TC menulis "tanpa membuka dropdown"; langkah 9, 15, dan 24 membersihkan pilihan yang belum di-Apply; langkah 20 melepas filter yang di-Apply dan langkah 21 membuka kembali Filter Panel karena panel menutup setelah `[Apply]`.
- Ukuran spec (45 langkah, di atas smell 35 langkah, kode R1): Filter Panel yang sama dipakai berulang oleh lima TC dengan satu pembukaan panel yang dibagi seluruh blok (langkah 1); langkah per field tidak diulang per TC dan tiap blok memulai dari field yang dibersihkan, sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Urutan: mengikuti sourceTc; TC-AC-DN-637 (dua field, dua arah, dan Apply tanpa kriteria) di akhir karena memuat Apply yang menutup spec.
- Temuan untuk QA:
  - Perilaku Filter Panel setelah `[Apply]` tidak konsisten di TC sumber (TC-AC-DN-311 dan TC-AC-DN-312 membuka panel lagi sesudah Apply, TC-AC-DN-314 menutupnya lewat klik ikon); spec mengasumsikan panel menutup setelah `[Apply]`.
  - TC-AC-DN-637 langkah 4 dan 8 membuka dropdown setelah chip dihapus tanpa menyebut menutup dropdown sebelum mengklik chip; spec menutup dropdown dulu agar klik chip deterministik.
