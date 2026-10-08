---
id: TC-GS-GSET-E2E-004-screening-opsi-dropdown-lima-field
title: Screening pilihan lima dropdown field
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-06
  - TC-GS-GSET-08
  - TC-GS-GSET-09
  - TC-GS-GSET-10
  - TC-GS-GSET-11
coverage:
  web: automated
---

# Screening opsi dropdown kelima field form

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- `Fixture.globalSettingsGeneralSettings.options` memuat daftar lengkap pilihan kelima dropdown.
- Form dalam keadaan isi (record `existing`) sehingga seluruh dropdown dapat dibuka.

## Test Steps

1. Buka halaman `Global Settings > General Settings`

### Field Currency Code

2. Klik kontrol dropdown `Currency Code`
3. Verifikasi opsi yang tampil masing-masing berformat `"[Symbol] - [Currency Name]"`, antara lain
   `Rp - Indonesian Rupiah`, `$ - US Dollar`, serta cakupan ISO 4217 lengkap (~180 kode); value
   tersimpan tetap kode ISO
4. Verifikasi daftar tidak menampilkan dobel entri dan tidak ada field "Currency Symbol" terpisah
5. Pilih opsi `$ - US Dollar`, lalu verifikasi kontrol menampilkan opsi terpilih

### Field Time Zone (searchable, label grouped)

6. Klik kontrol dropdown `Time Zone`
7. Verifikasi opsi menampilkan label berformat `(UTC±HH:MM) City1, City2, City3`, misal
   `(UTC+07:00) Bangkok, Hanoi, Jakarta`
8. Ketik nama kota parisial (misal `bangkok`); verifikasi pencarian match ke nama kota mana pun dalam
   label dan opsi terkait tampil
9. Pilih salah satu, lalu verifikasi kontrol menampilkan opsi terpilih dan nilai tersimpan berupa 1
   IANA identifier kanonik

### Field Session Idle Timeout

10. Klik kontrol dropdown `Session Idle Timeout`
11. Verifikasi opsi yang muncul persis dan berurutan `15 minutes`, `30 minutes`, `1 hour`, `2 hours`,
    `4 hours`, `8 hours` — **tidak ada opsi "Never"**
12. Pilih `8 hours`, lalu verifikasi kontrol menampilkan opsi terpilih

### Field Date Format

13. Klik kontrol dropdown `Date Format`
14. Verifikasi lima opsi tampil persis beserta contohnya: `dd/MM/yy` (`17/04/23`, default),
    `M/d/yy` (`3/17/23`), `dd MMM yy` (`03 Mar 23`), `DDD, MMM dd, yy` (`Wed, Mar 02, 23`),
    `DDD, MMM dd, yyyy` (`Wed, Mar 03, 2023`)
15. Pilih `M/d/yy`, lalu verifikasi kontrol menampilkan opsi terpilih dan contoh yang sesuai

### Field Time Format

16. Klik kontrol dropdown `Time Format`
17. Verifikasi dua opsi tampil: `hh:mm a` (contoh `02:30 PM`) dan `HH:mm` (contoh `14:30`, default)
18. Pilih `hh:mm a`, lalu verifikasi kontrol menampilkan opsi terpilih

## Notes

- Format tampilan opsi Currency Code, label Time Zone, serta contoh Date/Time mengikuti PRD `GSET-LOGIC-02`,
  `§1.3a`, `§1.3b`, dan `§4.2b`. Contoh format dievaluasi oleh tester otomasi sebagai bagian dari opsi.
- PMC-GS `FORMAT-CONTRACT` dipenuhi: tidak ada tanggal yang dikonversi oleh dropdown Date/Time; daftar
  hanya berisi pilihan format.