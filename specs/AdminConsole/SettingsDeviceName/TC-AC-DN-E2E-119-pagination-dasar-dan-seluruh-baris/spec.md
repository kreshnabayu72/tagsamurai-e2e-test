---
id: TC-AC-DN-E2E-119-pagination-dasar-dan-seluruh-baris
title: "Pagination List: Awal 10 Baris, Opsi Page Size, Navigasi, Input Nomor, dan Principal Melihat Seluruh Device Name"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-355
  - TC-AC-DN-356
  - TC-AC-DN-357
  - TC-AC-DN-358
  - TC-AC-DN-359
  - TC-AC-DN-559
coverage:
  web: automated
---

# Pagination List: Awal 10 Baris, Opsi Page Size, Navigasi, Input Nomor, dan Principal Melihat Seluruh Device Name

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #16 Device Name inti 9 baris (termasuk `Barcode Station` dan `Tag Reel`), #17 seed `Seed Device 001` sampai `Seed Device 120`, dan #23 Device Name panjang; total 130 baris (TC-AC-DN-559 memakai ketiganya). Tidak ada data Dinamis dan tidak ada aksi tulis.
- Nilai data dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE).
- State global: tidak ada yang diubah. Page size dan halaman dikembalikan ke 10 dan halaman 1 di akhir tiap blok. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-355: Pagination awal 10 baris per halaman

1. Verifikasi halaman 1 menampilkan 10 baris: Barcode Station, Cable Tester, Door Antenna, Field Radio, Gate Antenna, Legacy Scanner, NFC Tag, RFID Reader, Seed Device 001, Seed Device 002
2. Verifikasi page size terpilih 10

### TC-AC-DN-356: Opsi page size 10, 25, 50, 100 tanpa opsi All

3. Klik kontrol page size
4. Verifikasi Overlay Page Size memuat empat opsi: `10`, `25`, `50`, `100`
5. Verifikasi tidak ada opsi `All`
6. Tekan Esc (menutup overlay)

### TC-AC-DN-357: Mengganti page size menampilkan jumlah baris sesuai pilihan

7. Pilih page size `25`
8. Verifikasi halaman 1 menampilkan 25 baris dari 130 baris
9. Pilih page size `50`
10. Verifikasi halaman 1 menampilkan 50 baris
11. Pilih page size `100`
12. Verifikasi halaman 1 menampilkan 100 baris
13. Klik tombol halaman berikutnya
14. Verifikasi halaman 2 berisi 30 baris
15. Pilih page size `10`

### TC-AC-DN-358: Navigasi halaman berikutnya dan sebelumnya

16. Klik tombol halaman berikutnya
17. Verifikasi halaman 2 menampilkan Seed Device 003 sampai Seed Device 012
18. Klik tombol halaman sebelumnya
19. Verifikasi halaman 1 kembali menampilkan Barcode Station, Cable Tester, Door Antenna, Field Radio, Gate Antenna, Legacy Scanner, NFC Tag, RFID Reader, Seed Device 001, Seed Device 002

### TC-AC-DN-359: Input nomor halaman lalu Enter

20. Ketik `5` pada input nomor halaman, tekan Enter
21. Verifikasi halaman 5 menampilkan Seed Device 033 sampai Seed Device 042
22. Ketik `1` pada input nomor halaman, tekan Enter

### TC-AC-DN-559: Principal melihat seluruh Device Name pada List

23. Pilih page size `100` pada Overlay Page Size
24. Verifikasi halaman 1 menampilkan 100 baris
25. Verifikasi baris Barcode Station tampil di halaman 1
26. Klik tombol navigasi halaman berikutnya
27. Verifikasi halaman 2 menampilkan 30 baris
28. Verifikasi baris Tag Reel tampil di halaman 2
29. Pilih page size `10`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini tanpa aksi tulis.
- Langkah penghubung (S-03, S-09): langkah 6 menutup overlay; langkah 15, 22, dan 29 mengembalikan page size dan halaman ke awal.
- TC-AC-DN-559 (kelas a menurut indeks, `Security`) hanya mengasersi tampilan List seluruh Device Name oleh Principal, bukan respons API; tidak memakai K-1.
- Pembukaan Overlay Page Size diulang di TC-AC-DN-357 dan TC-AC-DN-559 karena kedua TC memakai page size 100 dengan precondition awal masing-masing (prinsip 13, halaman yang sama dipakai berulang).
- Urutan: mengikuti sourceTc; TC-AC-DN-559 di akhir karena mengubah page size lagi.
- Temuan untuk QA:
  - TC-AC-DN-559 Expected c ("baris `Barcode Station` dan `Tag Reel` tampil") tidak menyebut halaman; spec menempatkan Barcode Station di halaman 1 dan Tag Reel di halaman 2 berdasarkan urutan A-Z 130 baris.
