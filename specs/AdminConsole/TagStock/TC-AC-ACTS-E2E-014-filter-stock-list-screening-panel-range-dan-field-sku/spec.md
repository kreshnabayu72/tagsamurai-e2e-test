---
id: TC-AC-ACTS-E2E-014-filter-stock-list-screening-panel-range-dan-field-sku
title: "Filter Stock List: Screening Panel, Field SKU Tidak Ada, Numeric Range, dan Min/Max Inklusif"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-51
  - TC-AC-ACTS-54
  - TC-AC-ACTS-91
  - TC-AC-ACTS-92
  - TC-AC-ACTS-853
coverage:
  web: automated
---

# Filter Stock List: Screening Panel, Field SKU Tidak Ada, Numeric Range, dan Min/Max Inklusif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup #1 (akun Total Control) dan Stock List terisi minimal 5 SKU dari RFID, NFC, BLE, dan GPS dengan nilai beragam pada tiap kolom (#12 sampai #15 dan SKU pendukung).
- Data seed milik spec (SKU bersuffix `{runId}-014`, di-seed lewat fixture BE di hook `before`, dihapus di hook `after`): SKU W dengan Available 100, In Use 100, Damaged/Missing 100 (Total Registered 300; masuk rentang 100 sampai 300 untuk keempat field); SKU V dengan nilai di luar rentang; empat SKU R1 sampai R4 dengan Total Registered 100, 200, 300, 400 untuk TC-AC-ACTS-91 dan 92.
- Spec read-only terhadap data milik sendiri selain seeding.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-51: Screening Filter Panel

1. Klik icon Filter
2. Verifikasi Field berurutan Device Name [All device names] | TAG Type [All types] | Type [All types] | Brand [All brands] | Model/Type [All model/type] | Total Registered [Min] – [Max] | Available [Min] – [Max] | In Use [Min] – [Max] | Damaged/Missing [Min] – [Max] | Last Updated [Select date]
3. Verifikasi Dropdown bertipe multi-select searchable; field tanggal bertipe date range picker; field numerik berupa dua input Min dan Max
4. Verifikasi Tombol footer `[Clear Field]` (kiri) dan `[Apply]` (kanan)
5. Verifikasi Icon Filter berubah gelap saat panel terbuka
6. Verifikasi Tidak ada field `SKU` di Filter Panel

### TC-AC-ACTS-853: Filter Panel tanpa field SKU; SKU tetap dapat dicari lewat Search

7. Verifikasi Filter Panel memuat Device Name, TAG Type, Type, Brand, Model/Type, Total Registered, Available, In Use, Damaged/Missing, dan Last Updated; tidak ada field `SKU` maupun opsi `All SKUs`
8. Tutup Filter Panel, klik icon Search, ketik `Fixture.tagStock.skuRfid`, tekan Enter
9. Verifikasi Search menampilkan baris SKU `RFID-ASSET-CORE-R5`
10. Klik `(←)` pada kotak Search

### TC-AC-ACTS-54: Filter numeric range

11. Klik icon Filter
12. Verifikasi Placeholder input pertama `Min`, input kedua `Max`
13. Isi Min `100` dan Max `300` pada field Total Registered, Available, In Use, dan Damaged/Missing, klik `[Apply]`
14. Verifikasi Baris SKU W tampil (nilai di antara Min dan Max inklusif)
15. Verifikasi Baris SKU V tidak tampil
16. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### TC-AC-ACTS-91: Min dan Max inklusif

17. Klik icon Filter, isi Total Registered Min `200` Max `300`, klik `[Apply]`
18. Verifikasi Baris SKU R2 (200) dan SKU R3 (300) tampil (batas inklusif)
19. Verifikasi Baris SKU R1 (100) dan SKU R4 (400) tidak tampil

### TC-AC-ACTS-92: Salah satu input kosong

20. Klik icon Filter, kosongkan Max, isi hanya Min `300`, klik `[Apply]`
21. Verifikasi Baris SKU R3 (300) dan SKU R4 (400) tampil
22. Verifikasi Baris SKU R1 (100) dan SKU R2 (200) tidak tampil
23. Klik icon Filter, kosongkan Min, isi hanya Max `200`, klik `[Apply]`
24. Verifikasi Baris SKU R1 (100) dan SKU R2 (200) tampil
25. Verifikasi Baris SKU R3 (300) dan SKU R4 (400) tidak tampil
26. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

## Notes

- Urutan TC-AC-ACTS-51 dan 853 lebih dulu (screening), lalu TC-AC-ACTS-54, 91, 92 (S-10).
- Langkah penghubung (S-03): Filter dibersihkan sebelum TC berikutnya (S-09); `(←)` mengosongkan Search.
- Temuan untuk QA (S-15): TC-AC-ACTS-54 mengisi keempat field dengan Min 100 Max 300 sekaligus (irisan AND); spec memakai SKU W dengan Available, In Use, dan Damaged/Missing masing-masing 100 agar hasil tidak kosong. Hitungan R1 sampai R4 adalah Total Registered seed spec. TC-AC-ACTS-51 butir d ("Icon Filter berubah gelap") tidak menyebut warna; spec mengasersi perubahan menjadi gelap.
