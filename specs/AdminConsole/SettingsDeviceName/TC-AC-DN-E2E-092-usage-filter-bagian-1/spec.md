---
id: TC-AC-DN-E2E-092-usage-filter-bagian-1
title: "Usage by Company: Screening Filter, Opsi Entity Type, dan Filter Entity Type"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-630
  - TC-AC-DN-606
  - TC-AC-DN-262
coverage:
  web: automated
---

# Usage by Company: Screening Filter, Opsi Entity Type, dan Filter Entity Type

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip dinyatakan di `suite.md`. Spec ini tidak mengulangnya.
- Data Pre-setup (dibaca saja, tidak diubah; nilai dirujuk lewat `Fixture.settings-device-name`): #16 Device Name inti `Gate Antenna` (Category `Antenna`, Measurement `Unit`); #18 Usage by Company untuk Device Name `Gate Antenna`: `Company A` (Principal, Total SKU 3, Total Stock 40), `Company B` (Distributor dan Client, 2, 2), `Company C` (Client, 0, 6), `Company D` (Distributor, 4, 0), `Company E` (Client, 0, 12). Daftar List default tanpa Search, Filter, atau Sidebar aktif saat spec dimulai.
- Data Dinamis: tidak ada record yang dibuat atau diubah; tabel Usage hanya dibaca.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: klik, ketik, hover, dan membaca urutan baris serta isi sel tabel Usage by Company.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-DN-630: Screening Filter Panel tabel Usage by Company: field, placeholder, dan tombol

1. Klik teks nama `Gate Antenna` pada kolom Device Name
2. Klik ikon Filter pada toolbar tabel Usage
3. Verifikasi ikon Filter berubah gelap saat panel terbuka
4. Hover ikon Filter
5. Verifikasi tooltip `Filter` tampil
6. Verifikasi Body memuat tiga field berurutan: `Entity Type`, `Total SKU`, `Total Stock`
7. Verifikasi placeholder `Entity Type` adalah "All entity types", dan placeholder `Total SKU` serta `Total Stock` masing-masing "Min" dan "Max"
8. Verifikasi tipe kontrol: `Entity Type` dropdown multi-select searchable; `Total SKU` dan `Total Stock` range Min–Max
9. Verifikasi tidak ada field `Company` di panel
10. Verifikasi Footer memuat tombol `[Clear Field]` di kiri dan `[Apply]` di kanan

### TC-AC-DN-606: Opsi filter Entity Type pada tabel Usage by Company diisi dari baris tabel

11. Klik field `Entity Type` pada Filter Panel
12. Verifikasi daftar opsi tampil dan placeholder field Entity Type adalah "All entity types"
13. Verifikasi daftar opsi hanya memuat `Principal`, `Distributor`, dan `Client` sesuai badge yang ada pada baris tabel
14. Verifikasi opsi `Partner` tidak ada dan tidak ada baris dengan badge `Partner`

### TC-AC-DN-262: Filter Entity Type pada Usage by Company

15. Pilih `Distributor` pada dropdown `Entity Type`, lalu klik `[Apply]`
16. Verifikasi baris yang tampil `Company B` (`Distributor`, `Client`) dan `Company D` (`Distributor`)
17. Verifikasi baris `Company A`, `Company C`, dan `Company E` tidak tampil
18. Klik ikon Filter pada toolbar tabel Usage
19. Klik `[Clear Field]`, lalu klik `[Apply]`
20. Klik ikon `[X]` pada dialog Detail

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan: screening panel (TC-AC-DN-630) di depan, lalu opsi dropdown (TC-AC-DN-606) pada panel yang sama, lalu filter diterapkan (TC-AC-DN-262). Satu pembukaan panel dipakai bersama blok TC-AC-DN-630 dan TC-AC-DN-606 karena keduanya hanya mengamati tanpa mengubah state.
- Langkah penghubung (S-03): membuka kembali Filter Panel, `[Clear Field]` lalu `[Apply]` untuk melepas filter sebelum dialog ditutup, dan menutup dialog Detail dengan ikon `[X]`. Opsi TC-AC-DN-262 butir a (opsi dropdown tanpa `Partner`) sudah diasersi pada blok TC-AC-DN-606 dengan langkah yang sama.
- Ukuran spec: di bawah smell 35 langkah.
- Temuan untuk QA:
  - Post Condition kosong (`-`) pada semua TC spec ini (S-01).
  - TC-AC-DN-262 butir a dan TC-AC-DN-606 butir b tumpang tindih (opsi dropdown Entity Type tanpa `Partner`); keduanya tetap diasersi di blok masing-masing.
  - TC-AC-DN-262 hanya menyebut "terapkan filter" tanpa nama tombol; spec memakai tombol `[Apply]` sesuai TC-AC-DN-630.
