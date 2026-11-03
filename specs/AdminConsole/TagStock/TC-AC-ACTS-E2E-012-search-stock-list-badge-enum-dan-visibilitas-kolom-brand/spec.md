---
id: TC-AC-ACTS-E2E-012-search-stock-list-badge-enum-dan-visibilitas-kolom-brand
title: "Search Stock List: Kelas Badge, Kelas Enum, dan Search Terikat Visibilitas Kolom Brand"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-43
  - TC-AC-ACTS-44
  - TC-AC-ACTS-47
  - TC-AC-ACTS-48
coverage:
  web: automated
---

# Search Stock List: Kelas Badge, Kelas Enum, dan Search Terikat Visibilitas Kolom Brand

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup #1 (akun Total Control) dan Stock List terisi minimal 5 SKU dari RFID, NFC, BLE, dan GPS dengan nilai beragam pada tiap kolom (#12 sampai #15 dan SKU pendukung).
- Spec read-only: tidak membuat, mengubah, atau menghapus data.
- Data Pre-setup SKU #22 (`skuPlain`: Device Name `Plain Tag`, Brand `Zenith`, Model `X1`); kata `zenith` hanya ada di kolom Brand.
- Pemulihan Setup Column: TC-AC-ACTS-47 menyembunyikan kolom `Brand` dan TC-AC-ACTS-48 menampilkannya kembali; hook `after` menghapus preferensi kolom tabel di browser (kemampuan disediakan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-43: Search kelas badge

1. Klik icon Search, ketik `core`, tekan Enter
2. Verifikasi SKU ber-Brand `Core` tampil
3. Ganti isi kotak search dengan `CORE`, tekan Enter
4. Verifikasi SKU ber-Brand `Core` tampil (huruf besar/kecil dibalik)
5. Ganti isi kotak search dengan `zzz-tidak-ada-bra`, tekan Enter
6. Verifikasi Empty state `No results found` tampil
7. Ganti isi kotak search dengan `r5`, tekan Enter
8. Verifikasi SKU ber-Model/Type `R5` tampil
9. Ganti isi kotak search dengan `R5`, tekan Enter
10. Verifikasi SKU ber-Model/Type `R5` tampil (huruf besar/kecil dibalik)
11. Ganti isi kotak search dengan `zzz-tidak-ada-mod`, tekan Enter
12. Verifikasi Empty state `No results found` tampil

### TC-AC-ACTS-44: Search kelas label enum

13. Ganti isi kotak search dengan `rfid`, tekan Enter
14. Verifikasi SKU bertipe RFID (accessibility label) tampil
15. Ganti isi kotak search dengan `RFID`, tekan Enter
16. Verifikasi SKU bertipe RFID tampil (huruf besar/kecil dibalik)
17. Ganti isi kotak search dengan `zzz-tidak-ada-tag`, tekan Enter
18. Verifikasi Empty state `No results found` tampil
19. Ganti isi kotak search dengan `object`, tekan Enter
20. Verifikasi SKU bertipe Object TAG tampil
21. Ganti isi kotak search dengan `OBJECT`, tekan Enter
22. Verifikasi SKU bertipe Object TAG tampil (huruf besar/kecil dibalik)
23. Ganti isi kotak search dengan `zzz-tidak-ada-typ`, tekan Enter
24. Verifikasi Empty state `No results found` tampil

### TC-AC-ACTS-47: Search terikat visibilitas kolom, kolom Brand di-hide

25. Klik `(←)` pada kotak Search
26. Klik header (⋯), lalu hilangkan centang kolom `Brand`
27. Verifikasi Kolom `Brand` tidak tampil
28. Klik icon Search, ketik `zenith`, tekan Enter
29. Verifikasi Empty state `No results found` tampil (keyword `zenith` tidak mencocokkan baris melalui kolom `Brand`; SKU `Fixture.tagStock.skuPlain` tidak ditemukan)

### TC-AC-ACTS-48: Search terikat visibilitas kolom, kolom Brand di-unhide

30. Klik `(←)` pada kotak Search, klik header (⋯), lalu centang kembali kolom `Brand`
31. Verifikasi Kolom `Brand` tampil kembali
32. Klik icon Search, ketik `zenith`, tekan Enter
33. Verifikasi Baris SKU `Fixture.tagStock.skuPlain` tampil (keyword `zenith` kembali mencocokkan melalui kolom `Brand`)

## Notes

- Urutan TC-AC-ACTS-47 lalu 48: kolom `Brand` sudah tersembunyi dari TC-AC-ACTS-47 sehingga TC-AC-ACTS-48 langsung mencentangnya kembali (TC sumber: "hilangkan lalu centang kembali").
- Langkah penghubung (S-03): `(←)` pada kotak Search mengosongkan dan menutup input sebelum TC berikutnya (S-09).
- Temuan untuk QA (S-15): TC-AC-ACTS-43 dan 44 menyebut Brand `Core` dan Model `R5` dari data Pre-setup tanpa memastikan keduanya ada di SKU #12; nilai mengikuti Expected TC.
