---
id: TC-AC-ACTS-E2E-017-setup-column-stock-list-screening-satu-kolom-tersisa-dan-pin-ke-4
title: "Setup Column Stock List: Screening Overlay dan Popup, Satu Kolom Tersisa, dan Pin ke-4 Diblokir"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-57
  - TC-AC-ACTS-58
  - TC-AC-ACTS-64
  - TC-AC-ACTS-65
coverage:
  web: automated
---

# Setup Column Stock List: Screening Overlay dan Popup, Satu Kolom Tersisa, dan Pin ke-4 Diblokir

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup #1 (akun Total Control) dan Stock List terisi minimal 5 SKU dari RFID, NFC, BLE, dan GPS dengan nilai beragam pada tiap kolom (#12 sampai #15 dan SKU pendukung).
- Spec read-only: tidak membuat, mengubah, atau menghapus data.
- Setup Column hanya dibuka dan ditutup lewat (X); tidak ada konfigurasi yang disimpan. Hook `after` menghapus preferensi kolom tabel di browser sebagai cadangan (kemampuan disediakan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-57: Screening Overlay Column Visibility

1. Klik header kolom Column Visibility (⋯)
2. Verifikasi Overlay memuat tombol `[Setup Column]`
3. Verifikasi Daftar kolom berurutan `Photo`, `Device Name`, `SKU`, `TAG Type`, `Type`, `Brand`, `Model/Type`, `Total Registered`, `Available`, `In Use`, `Damaged/Missing`, `Last Updated`
4. Verifikasi Setiap kolom berstatus checkbox checked dan enabled (Hideable) dengan drag handle
5. Verifikasi Overlay tidak menutup tabel (tanpa backdrop)

### TC-AC-ACTS-58: Screening Popup Setup Column dan Live Preview

6. Klik `[Setup Column]`
7. Verifikasi Header popup: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan tombol close (X)
8. Verifikasi Body popup: daftar kolom `Photo`, `Device Name`, `SKU`, `TAG Type`, `Type`, `Brand`, `Model/Type`, `Total Registered`, `Available`, `In Use`, `Damaged/Missing`, `Last Updated` dengan checkbox, drag handle, dan icon Pin
9. Verifikasi Body popup memuat Live Preview urutan header
10. Verifikasi Footer popup: `[Reset to Default]` dan `[Save]` rata kanan, tanpa `[Cancel]`

### TC-AC-ACTS-64: Satu kolom tersisa tidak bisa di-uncheck

11. Hilangkan centang semua kolom kecuali satu (`Last Updated`)
12. Arahkan kursor ke checkbox kolom terakhir dan coba hilangkan centangnya
13. Verifikasi Checkbox kolom terakhir disabled
14. Verifikasi Tooltip `At least one column must remain visible.`
15. Klik icon (X) untuk menutup popup tanpa menyimpan

### TC-AC-ACTS-65: Pin ke-4 diblokir

16. Klik header (⋯), klik `[Setup Column]`
17. Klik icon Pin pada kolom `Photo`, `Device Name`, dan `SKU` (3 kolom)
18. Arahkan kursor ke icon Pin kolom `TAG Type` dan coba klik
19. Verifikasi Icon Pin kolom `TAG Type` disabled dan kolom tidak ter-pin
20. Verifikasi Tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
21. Klik icon Pin kolom `SKU` untuk melepas pin
22. Verifikasi Icon Pin kolom `TAG Type` aktif kembali
23. Klik icon (X) untuk menutup popup tanpa menyimpan

## Notes

- Langkah penghubung (S-03): menutup overlay dan popup lewat (X) tanpa menyimpan (TC-AC-ACTS-63 menyatakan perubahan dibuang tanpa dialog); hook `after` menghapus preferensi kolom.
- Temuan untuk QA (S-15): TC-AC-ACTS-64 tidak menyebut kolom yang tersisa; spec memakai `Last Updated`. TC-AC-ACTS-65 butir c menulis "Setelah satu kolom di-unpin"; spec melepas pin kolom `SKU`.
