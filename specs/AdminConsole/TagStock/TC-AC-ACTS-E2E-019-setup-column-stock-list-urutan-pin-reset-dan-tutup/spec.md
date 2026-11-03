---
id: TC-AC-ACTS-E2E-019-setup-column-stock-list-urutan-pin-reset-dan-tutup
title: "Setup Column Stock List: Geser Urutan, Pin dan Unpin, Reset to Default, serta Tutup dengan (X) atau Esc"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-60
  - TC-AC-ACTS-61
  - TC-AC-ACTS-62
  - TC-AC-ACTS-63
coverage:
  web: automated
---

# Setup Column Stock List: Geser Urutan, Pin dan Unpin, Reset to Default, serta Tutup dengan (X) atau Esc

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup #1 (akun Total Control) dan Stock List terisi minimal 5 SKU dari RFID, NFC, BLE, dan GPS dengan nilai beragam pada tiap kolom (#12 sampai #15 dan SKU pendukung).
- Pemulihan Setup Column: TC-AC-ACTS-60 dan 61 menyimpan urutan dan pin; TC-AC-ACTS-62 mengembalikan susunan default modul; hook `after` menghapus preferensi kolom tabel di browser (kemampuan disediakan tim FE).
- Kemampuan teknis: drag and drop baris Setup Column dan scroll horizontal tabel (kemampuan standar kerangka).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-60: Geser urutan kolom

1. Klik header kolom Column Visibility (⋯), lalu klik `[Setup Column]`
2. Geser kolom `Photo` ke bawah kolom `Device Name`
3. Verifikasi Live Preview mengikuti urutan baru
4. Klik `[Save]`
5. Verifikasi Tabel mengikuti urutan baru setelah Save
6. Muat ulang halaman (F5)
7. Verifikasi Urutan baru bertahan setelah F5

### TC-AC-ACTS-61: Pin dan unpin kolom

8. Klik header (⋯), klik `[Setup Column]`, klik icon Pin kolom `Photo`, klik `[Save]`
9. Scroll tabel secara horizontal
10. Verifikasi Kolom ter-pin tetap diam di sisi kiri saat scroll horizontal
11. Klik header (⋯), klik `[Setup Column]`, klik Pin kolom `Photo` lagi (unpin), klik `[Save]`
12. Scroll tabel secara horizontal
13. Verifikasi Setelah unpin kolom ikut bergeser lagi

### TC-AC-ACTS-62: Reset to Default

14. Klik header (⋯), klik `[Setup Column]`, sembunyikan kolom `Device Name`, geser `Photo`, klik `[Save]`
15. Klik header (⋯), klik `[Setup Column]`, klik `[Reset to Default]`
16. Verifikasi Preview kembali ke susunan default modul (bukan ke state tersimpan terakhir)
17. Klik `[Save]`
18. Muat ulang halaman (F5)
19. Verifikasi Susunan default bertahan setelah F5

### TC-AC-ACTS-63: Tutup dengan (X) atau Esc membuang perubahan

20. Klik header (⋯), klik `[Setup Column]`, sembunyikan kolom `Device Name` di preview
21. Klik icon (X)
22. Verifikasi Modal tertutup tanpa dialog konfirmasi
23. Verifikasi Perubahan preview dibuang; tabel memakai konfigurasi tersimpan terakhir (kolom `Device Name` tampil)
24. Klik header (⋯), klik `[Setup Column]`, sembunyikan kolom `Device Name`, tekan Esc
25. Verifikasi Modal tertutup tanpa dialog konfirmasi
26. Verifikasi Perubahan preview dibuang; kolom `Device Name` tetap tampil

## Notes

- Langkah penghubung (S-03): muat ulang F5 setelah `[Save]` (bagian Expected); TC-AC-ACTS-62 menutup dengan `[Reset to Default]` lalu `[Save]` sehingga konfigurasi tersimpan kembali ke default sebelum TC-AC-ACTS-63.
- Temuan untuk QA (S-15): TC-AC-ACTS-60 tidak menyebut kolom `Photo` setelah `Device Name` yang diverifikasi di tabel; spec mengasersi urutan baru berdasarkan Live Preview dan header tabel. TC-AC-ACTS-63 butir a menyatakan modal tertutup tanpa dialog konfirmasi; ini tidak sama dengan menutup form dirty (S-08), sehingga tidak ada langkah `[Leave]`.
