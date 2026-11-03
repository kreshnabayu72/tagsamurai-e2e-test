---
id: TC-AC-DN-E2E-101-search-kolom-lintas-halaman-dan-trim
title: "Search List: Brand/Model/Measurement, Lintas Halaman, Empty, Trim, dan Spasi Saja"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-277
  - TC-AC-DN-278
  - TC-AC-DN-279
  - TC-AC-DN-280
  - TC-AC-DN-281
  - TC-AC-DN-282
coverage:
  web: automated
---

# Search List: Brand/Model/Measurement, Lintas Halaman, Empty, Trim, dan Spasi Saja

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #15 Brand (`Brand C`, `International Scanner Solutions`), #16 Device Name inti beserta SKU-nya (`RFID Reader` ber-Brand A/B/C dan Model R1/R2/R3, `Barcode Station` ber-Brand `International Scanner Solutions` dan Model `Industrial Barcode Station Series Alpha`, `Tag Reel` ber-Measurement `Meter`), #17 seed `Seed Device 001` sampai `Seed Device 120`, dan #23 nama panjang; total 130 baris. Tidak ada data Dinamis dan tidak ada aksi tulis.
- Nilai data dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE).
- Kemampuan teknis: mengetik (termasuk spasi di awal dan akhir) dan menekan Enter.
- State global: tidak ada yang diubah. Kotak Search dikosongkan di akhir spec. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-277: Search Brand dan Model/Type termasuk nilai di balik `+N more`

1. Ketik Search `Brand C`, tekan Enter
2. Verifikasi tabel menampilkan 1 baris: RFID Reader
3. Verifikasi `Brand C` tidak tampil di sel Brand RFID Reader karena berada di balik chip `+1 more`
4. Ganti isi kotak search dengan `international`, tekan Enter
5. Verifikasi tabel menampilkan 1 baris: Barcode Station (cocok `International Scanner Solutions`, huruf kecil)
6. Ganti isi kotak search dengan `model r3`, tekan Enter
7. Verifikasi tabel menampilkan 1 baris: RFID Reader
8. Verifikasi `Model R3` tidak tampil di sel Model/Type RFID Reader karena berada di balik chip `+1 more`
9. Ganti isi kotak search dengan `industrial barcode`, tekan Enter
10. Verifikasi tabel menampilkan 1 baris: Barcode Station (cocok `Industrial Barcode Station Series Alpha`)

### TC-AC-DN-278: Search kolom Measurement

11. Ganti isi kotak search dengan `meter`, tekan Enter
12. Verifikasi tabel menampilkan 1 baris: Tag Reel (Measurement `Meter`)
13. Ganti isi kotak search dengan `METER`, tekan Enter
14. Verifikasi tabel menampilkan 1 baris: Tag Reel

### TC-AC-DN-279: Search menyaring seluruh dataset lintas halaman

15. Klik `(←)` pada kotak Search
16. Ketik Search `Seed Device`, tekan Enter
17. Verifikasi tabel menampilkan 120 baris hasil (Seed Device 001 sampai Seed Device 120)
18. Verifikasi pagination menampilkan 12 halaman pada 10 baris per halaman
19. Verifikasi halaman 1 menampilkan Seed Device 001 sampai Seed Device 010

### TC-AC-DN-280: Search tanpa hasil

20. Ganti isi kotak search dengan `zzzxyz`, tekan Enter
21. Verifikasi tabel menampilkan empty state Title "No results found" dan Description "Try adjusting your search or filter."
22. Verifikasi empty state bukan tampilan error
23. Verifikasi empty state tidak memuat tombol `[Try Again]`

### TC-AC-DN-281: Spasi di awal dan akhir kata kunci dibuang

24. Ganti isi kotak search dengan `  rfid reader  ` (dua spasi di awal dan akhir), tekan Enter
25. Verifikasi tabel menampilkan 1 baris: RFID Reader
26. Verifikasi isi input pencarian di layar tetap memuat spasi di awal dan akhir

### TC-AC-DN-282: Kata kunci hanya spasi

27. Ganti isi kotak search dengan `rfid`, tekan Enter
28. Ganti isi kotak search dengan tiga spasi, tekan Enter
29. Verifikasi tabel kembali ke kondisi tanpa pencarian: 130 baris
30. Verifikasi halaman 1 menampilkan Barcode Station, Cable Tester, Door Antenna, Field Radio, Gate Antenna, Legacy Scanner, NFC Tag, RFID Reader, Seed Device 001, Seed Device 002
31. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini tanpa aksi tulis.
- Langkah penghubung (S-03, S-09): langkah 15 mengosongkan Search sebelum Search `Seed Device` (kotak search ditutup dan tabel direset); langkah 27 mengisi Search `rfid` tanpa asersi (TC-AC-DN-282 tidak memberi Expected untuknya); langkah 31 mengosongkan Search di akhir spec.
- Urutan: mengikuti sourceTc; TC tanpa hasil (TC-AC-DN-280) dan Trim (TC-AC-DN-281, TC-AC-DN-282) di akhir karena state Search dibersihkan lewat langkah penghubung.
- Temuan untuk QA:
  - TC-AC-DN-277 hingga TC-AC-DN-282: TC tidak menyebut cara membaca total baris di layar; spec mengasersi jumlah baris yang terbaca dari tabel dan pagination.
  - TC-AC-DN-282 langkah 2 (Search `rfid`) tidak punya Expected; spec tidak menambahkan asersinya.
