---
id: TC-AC-DN-E2E-117-kombinasi-independensi-kontrol
title: "Independensi Kontrol: Mengosongkan Search, Pindah Sort, Page Size, dan Empty State Pulih"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-347
  - TC-AC-DN-348
  - TC-AC-DN-349
  - TC-AC-DN-353
coverage:
  web: automated
---

# Independensi Kontrol: Mengosongkan Search, Pindah Sort, Page Size, dan Empty State Pulih

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #13 Measurement `Unit`, `Meter`; #16 Device Name inti (`Door Antenna` dan `Gate Antenna` ber-Measurement `Unit` dan Category `Antenna`, `Tag Reel` ber-Measurement `Meter`); #17 seed 120 baris; #23 nama panjang `Zona Pemindai Kode Batang Industri Tahan Banting Gudang Besar Nirkabel Pemindai Kode Batang Industri Tahan Banting Gudan` (Measurement `Unit`). Tidak ada data Dinamis dan tidak ada aksi tulis.
- Nilai data dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE).
- State global: tidak ada yang diubah. Search, Filter, Sort, dan page size dikembalikan ke awal di akhir tiap blok. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-347: Mengosongkan Search saat Filter dan Sort aktif

1. Klik ikon Filter, klik field `Measurement`, centang `Unit`, lalu klik `[Apply]`
2. Klik header `Device Name` dua kali (descending)
3. Ketik Search `Antenna`, tekan Enter
4. Klik `✕` pada Search, tekan Enter
5. Verifikasi sort Device Name descending tetap aktif
6. Verifikasi ikon Filter menampilkan indikator filter aktif
7. Verifikasi tabel menampilkan Device Name ber-Measurement Unit saja, urut Z-A, dimulai `Zona Pemindai Kode Batang Industri Tahan Banting Gudang Besar Nirkabel Pemindai Kode Batang Industri Tahan Banting Gudan` lalu Seed Device 120
8. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
9. Klik `(←)` pada kotak Search
10. Klik header `Device Name` ketiga kali (netral)

### TC-AC-DN-348: Berpindah kolom sort saat Search dan Filter aktif

11. Ketik Search `Antenna`, tekan Enter
12. Klik ikon Filter, klik field `Measurement`, centang `Unit`, lalu klik `[Apply]`
13. Klik header `Device Name`
14. Klik header `Category`
15. Verifikasi kata kunci `Antenna` tetap terisi di kolom pencarian
16. Verifikasi ikon Filter menampilkan indikator filter aktif
17. Verifikasi sort berpindah ke Category ascending
18. Verifikasi indikator sort Device Name kembali netral
19. Verifikasi tabel menampilkan 2 baris: Door Antenna dan Gate Antenna
20. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
21. Klik `(←)` pada kotak Search
22. Klik header `Category` dua kali (netral)

### TC-AC-DN-349: Empty state pulih saat salah satu kontrol penyaring dilepas

23. Ketik Search `Antenna`, tekan Enter
24. Klik ikon Filter, klik field `Measurement`, centang `Meter`, lalu klik `[Apply]`
25. Verifikasi tabel menampilkan empty state Title "No results found" dan Description "Try adjusting your search or filter."
26. Klik `✕` pada Search, tekan Enter
27. Verifikasi tabel pulih dan menampilkan 1 baris: Tag Reel (filter Meter tetap aktif)
28. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-DN-353: Mengubah page size tidak mereset Search, Filter, dan Sort

29. Ketik Search `Seed Device`, tekan Enter
30. Klik header `Device Name` dua kali (descending)
31. Ubah page size menjadi 25
32. Verifikasi kata kunci `Seed Device` tetap terisi di kolom pencarian
33. Verifikasi sort Device Name descending tetap aktif
34. Verifikasi halaman 1 menampilkan 25 baris: Seed Device 120 sampai Seed Device 096
35. Klik `(←)` pada kotak Search
36. Klik header `Device Name` ketiga kali (netral)
37. Ubah page size menjadi 10

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini tanpa aksi tulis.
- Langkah penghubung (S-03, S-09): langkah 8 sampai 10, 20 sampai 22, 28, dan 35 sampai 37 mengembalikan Filter, Search, sort, dan page size ke awal; langkah 4 dan 26 melepas Search dengan `✕` lalu Enter.
- Ukuran spec (37 langkah, di atas smell 35 langkah, kode R3): satu topik (independensi kontrol List), satu dataset 130 baris baca-saja, satu kelas harness; tiap blok memulai dari kontrol yang dikembalikan ke awal sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Urutan: mengikuti sourceTc.
- Temuan untuk QA:
  - Perilaku Filter Panel setelah `[Apply]` tidak konsisten di TC sumber (TC-AC-DN-311 dan TC-AC-DN-312 membuka panel lagi sesudah Apply, TC-AC-DN-314 menutupnya lewat klik ikon); spec mengasumsikan panel menutup setelah `[Apply]`.
  - TC-AC-DN-347 menyebut `Antenna` sebagai Search yang dilepas dan Filter `Unit`; Expected tidak menyebut hasil Search sebelum dilepas, sehingga spec tidak mengasersinya.
