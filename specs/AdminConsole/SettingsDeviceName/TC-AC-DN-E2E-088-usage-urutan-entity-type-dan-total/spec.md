---
id: TC-AC-DN-E2E-088-usage-urutan-entity-type-dan-total
title: "Usage by Company: Urutan Company, Entity Type, Total SKU, dan Total Stock"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-246
  - TC-AC-DN-247
  - TC-AC-DN-248
  - TC-AC-DN-249
  - TC-AC-DN-250
coverage:
  web: automated
---

# Usage by Company: Urutan Company, Entity Type, Total SKU, dan Total Stock

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip dinyatakan di `suite.md`. Spec ini tidak mengulangnya.
- Data Pre-setup (dibaca saja, tidak diubah; nilai dirujuk lewat `Fixture.settings-device-name`): #16 Device Name inti `Gate Antenna` (Category `Antenna`, Measurement `Unit`); #18 Usage by Company untuk Device Name `Gate Antenna`: `Company A` (Principal, Total SKU 3, Total Stock 40), `Company B` (Distributor dan Client, 2, 2), `Company C` (Client, 0, 6), `Company D` (Distributor, 4, 0), `Company E` (Client, 0, 12). Daftar List default tanpa Search, Filter, atau Sidebar aktif saat spec dimulai.
- Data Dinamis: tidak ada record yang dibuat atau diubah; tabel Usage hanya dibaca.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: klik dan membaca isi sel tabel Usage by Company.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-DN-246: Tabel Usage by Company terurut Company A-Z secara default

1. Klik teks nama `Gate Antenna` pada kolom Device Name
2. Verifikasi baris Usage tampil berurutan `Company A`, `Company B`, `Company C`, `Company D`, `Company E`
3. Verifikasi tidak ada ikon sort yang aktif pada header kolom mana pun

### TC-AC-DN-247: Baris Company bertipe Principal pada Usage by Company

4. Verifikasi kolom Entity Type baris `Company A` menampilkan satu badge `Principal`
5. Verifikasi kolom Total SKU baris `Company A` bernilai `3`
6. Verifikasi kolom Total Stock baris `Company A` bernilai `40`

### TC-AC-DN-248: Distributor yang berlangganan sebagai Client menampilkan dua badge Entity Type

7. Verifikasi kolom Entity Type baris `Company B` menampilkan dua badge eksplisit sekaligus: `Distributor` dan `Client`
8. Verifikasi kolom Total SKU baris `Company B` bernilai `2`
9. Verifikasi kolom Total Stock baris `Company B` bernilai `2`

### TC-AC-DN-249: Baris Company bertipe Client dengan unit BYO menampilkan Total Stock lebih besar dari Total SKU

10. Verifikasi kolom Entity Type baris `Company C` menampilkan satu badge `Client`
11. Verifikasi kolom Total SKU baris `Company C` bernilai `0`
12. Verifikasi kolom Total Stock baris `Company C` bernilai `6`, lebih besar daripada Total SKU

### TC-AC-DN-250: Total Stock bernilai nol tampil sebagai angka 0

13. Verifikasi kolom Entity Type baris `Company D` menampilkan satu badge `Distributor`
14. Verifikasi kolom Total SKU baris `Company D` bernilai `4`
15. Verifikasi kolom Total Stock baris `Company D` menampilkan `0` dan bukan tanda strip atau sel kosong
16. Klik ikon `[X]` pada dialog Detail

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Satu pembukaan dialog Detail dipakai bersama oleh kelima blok TC: tidak ada state yang berubah di antara blok (hanya membaca baris), sehingga langkah "Buka halaman" dan "Klik nama" TC sumber tidak diulang per blok (prinsip 13, halaman yang sama dipakai berulang). Langkah penutup dialog di akhir adalah langkah penghubung (S-03).
- Ukuran spec: di bawah smell 35 langkah.
- Temuan untuk QA:
  - Post Condition kosong (`-`) pada semua TC spec ini (S-01).
  - TC-AC-DN-246 hingga TC-AC-DN-250 menyebut hanya lima baris `Company A` sampai `Company E`, sedangkan Pre-setup #18 juga memuat `Company F` sampai `Company I` untuk Device Name yang sama dan menyatakan baris itu "tidak muncul pada TC Usage lainnya". Spec ini mengasumsikan hanya Company A sampai E yang ada; data F sampai I dibuat hanya oleh spec yang membutuhkannya.
